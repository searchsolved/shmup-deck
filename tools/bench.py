#!/usr/bin/env python3
"""Measure the service on a MiSTer and compare with the last release.

    python3 tools/bench.py [--host shmupdeck.local] [--minutes 30] [--game esprade] [--save]

Run before a release. It times a full rescan, watches the service sit idle
on the menu for --minutes, then launches --game and watches it for the same
time while the game runs (the case that matters most: the service should be
invisible while the ARM side is serving a core). The MiSTer is put back on the
menu afterwards. The numbers are compared with tools/bench_baseline.json and
the exit code is 1 if anything has regressed:

    memory (RSS or high-water mark)   more than 25% above the baseline
    CPU, idle and in-game             above 1% of a core, or double the baseline
    rescan time per 1,000 MRAs        more than 50% above the baseline

--save writes the new numbers as the baseline once you are happy with them.

The MiSTer is reached over SSH as root (its default password is "1"; set
SHMUP_PASS for another, and sshpass is used when installed). The sampler runs
on the MiSTer itself and is polled from here, so a Wi-Fi drop mid-run does not
lose the measurement. Nothing is left behind except /tmp/shmup_bench.log.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASELINE = os.path.join(ROOT, "tools", "bench_baseline.json")
LOG = "/tmp/shmup_bench.log"

# runs on the MiSTer: find the service, then log ticks and memory once a minute
SAMPLER = r'''
pid=""
for p in /proc/[0-9]*; do
  case "$(tr "\0" " " < $p/cmdline)" in python3*shmup_deck.py*) pid=${p#/proc/};; esac
done 2>/dev/null
[ -n "$pid" ] || { echo "no service"; exit 1; }
t0=$(awk "{print \$14+\$15}" /proc/$pid/stat); s0=$(date +%s)
echo "pid $pid ticks0 $t0 start $s0 threads $(awk '/Threads/{print $2}' /proc/$pid/status)"
while [ -d /proc/$pid ]; do
  sleep 60
  t=$(awk "{print \$14+\$15}" /proc/$pid/stat)
  echo "sample elapsed=$(( $(date +%s) - s0 )) ticks=$(( t - t0 )) rss=$(awk '/VmRSS/{print $2}' /proc/$pid/status) hwm=$(awk '/VmHWM/{print $2}' /proc/$pid/status) core=$(cat /tmp/CORENAME 2>/dev/null)"
  [ $(( $(date +%s) - s0 )) -ge MINUTES ] && break
done
echo done
'''


def ssh(host, cmd):
    base = ["ssh", "-o", "ConnectTimeout=8", "-o", "StrictHostKeyChecking=no",
            "-o", "PubkeyAuthentication=no", "-o", "PreferredAuthentications=password",
            "root@" + host, cmd]
    if shutil.which("sshpass"):
        base = ["sshpass", "-p", os.environ.get("SHMUP_PASS", "1")] + base
    r = subprocess.run(base, capture_output=True, text=True, timeout=60)
    if r.returncode:
        raise RuntimeError(r.stderr.strip() or "ssh failed")
    return r.stdout


def http(host, path, data=None):
    req = urllib.request.Request("http://%s:8190%s" % (host, path),
                                 data=json.dumps(data).encode() if data else None,
                                 headers={"Content-Type": "application/json"} if data else {})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.load(r)


def status_when_idle(host):
    for _ in range(120):
        s = http(host, "/api/status")
        if not s["scanning"]:
            return s
        time.sleep(5)
    sys.exit("the rescan did not finish in 10 minutes")


def sample(host, minutes, label):
    """Run the sampler on the MiSTer for `minutes` and return its parsed log."""
    script = SAMPLER.replace("MINUTES", str(minutes * 60))
    ssh(host, "rm -f %s; cat > /tmp/shmup_bench.sh <<'EOF'\n%s\nEOF\nsetsid nohup sh /tmp/shmup_bench.sh > %s 2>&1 < /dev/null &" % (LOG, script, LOG))
    print("%s for %d minutes" % (label, minutes), end="", flush=True)
    last = ""
    while True:
        time.sleep(60)
        try:
            out = ssh(host, "cat " + LOG)
        except Exception:
            print("?", end="", flush=True)     # Wi-Fi hiccup; the sampler carries on
            continue
        if "no service" in out:
            sys.exit("\nno shmup_deck service running on " + host)
        last = out
        print(".", end="", flush=True)
        if "done" in out.splitlines()[-1:]:
            break
    print()
    head = next(l for l in last.splitlines() if l.startswith("pid ")).split()
    samples = [dict(kv.split("=") for kv in line.split()[1:]) for line in last.splitlines() if line.startswith("sample")]
    end = samples[-1]
    elapsed, ticks = int(end["elapsed"]), int(end["ticks"])
    return {
        "rss_kb": int(end["rss"]), "hwm_kb": int(end["hwm"]),
        "cpu_pct": round(ticks / elapsed, 2),      # 100 ticks per second
        "threads": int(head[head.index("threads") + 1]),
        "minutes": elapsed // 60,
        "cores_seen": sorted({x["core"] for x in samples}),
    }


def measure(host, minutes, game):
    print("rescan...", end=" ", flush=True)
    http(host, "/api/rescan", {"full": True})
    time.sleep(3)
    s = status_when_idle(host)
    print("%s MRAs in %ss (version %s)" % (s["mras"], s["seconds"], s["version"]))
    idle = sample(host, minutes, "idle on the menu")
    now = {
        "version": s["version"], "mras": s["mras"], "rescan_seconds": s["seconds"],
        "rescan_per_1k": round(s["seconds"] * 1000 / max(s["mras"], 1), 2),
        "rss_kb": idle["rss_kb"], "hwm_kb": idle["hwm_kb"], "idle_cpu_pct": idle["cpu_pct"],
        "threads": idle["threads"], "minutes": idle["minutes"], "cores_seen": idle["cores_seen"],
    }
    if game:
        http(host, "/api/launch", {"id": game})
        time.sleep(20)                                   # let the core load
        running = http(host, "/api/status")["now_playing"]
        if running != game:
            sys.exit("%s did not start (now playing: %s)" % (game, running))
        g = sample(host, minutes, "playing %s" % game)
        ssh(host, "echo load_core /media/fat/menu.rbf > /dev/MiSTer_cmd")
        now.update(game=game, game_cpu_pct=g["cpu_pct"], rss_kb=max(now["rss_kb"], g["rss_kb"]),
                   hwm_kb=max(now["hwm_kb"], g["hwm_kb"]))
    return now


def compare(now, base):
    checks = [
        ("RSS", now["rss_kb"], base["rss_kb"] * 1.25, "%d kB"),
        ("high-water mark", now["hwm_kb"], base["hwm_kb"] * 1.25, "%d kB"),
        ("idle CPU", now["idle_cpu_pct"], max(1.0, base["idle_cpu_pct"] * 2), "%.2f%%"),
        ("in-game CPU", now.get("game_cpu_pct", 0), max(1.0, base.get("game_cpu_pct", 0) * 2), "%.2f%%"),
        ("rescan per 1k MRAs", now["rescan_per_1k"], base["rescan_per_1k"] * 1.5, "%.2fs"),
    ]
    bad = False
    for name, value, limit, fmt in checks:
        ok = value <= limit
        bad |= not ok
        print("  %-20s %-12s limit %-12s %s" % (name, fmt % value, fmt % limit, "ok" if ok else "REGRESSION"))
    return bad


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--host", default=os.environ.get("SHMUP_HOST", "shmupdeck.local"))
    ap.add_argument("--minutes", type=int, default=30)
    ap.add_argument("--game", default="esprade", help="game to run for the in-game window; '' to skip")
    ap.add_argument("--save", action="store_true", help="write these numbers as the new baseline")
    a = ap.parse_args()
    now = measure(a.host, a.minutes, a.game)
    print("version %(version)s: %(rss_kb)d kB RSS (%(hwm_kb)d kB peak), %(idle_cpu_pct).2f%% CPU idle over "
          "%(minutes)d min, %(threads)d threads, rescan %(rescan_seconds)ss for %(mras)d MRAs" % now)
    if "game_cpu_pct" in now:
        print("  %.2f%% CPU while %s ran" % (now["game_cpu_pct"], now["game"]))
    if now["cores_seen"] != ["MENU"]:
        print("  note: cores running during the idle window: %s" % ", ".join(now["cores_seen"]))
    bad = False
    if os.path.exists(BASELINE):
        with open(BASELINE) as f:
            base = json.load(f)
        print("against %s (%s):" % (os.path.relpath(BASELINE, ROOT), base["version"]))
        bad = compare(now, base)
    else:
        print("no baseline yet; run with --save to record one")
    if a.save:
        with open(BASELINE, "w") as f:
            json.dump(now, f, indent=1)
            f.write("\n")
        print("saved as the baseline")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()

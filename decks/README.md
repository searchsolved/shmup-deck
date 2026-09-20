# Shared decks

A deck is a list of games someone chose and ordered: ten to learn danmaku
on, Toaplan in release order, a friend's favourites. The decks in this
folder appear on the Decks page of every Shmup Deck, with a button to save
one to your own MiSTer.

The easy way to share yours: on your own Decks page, tap **Share with
everyone** under the deck. GitHub opens a new-file page with the deck already
in it; add your name on the author line and press Propose changes. A check
runs on the pull request, the owner merges it, and the index rebuilds itself.

By hand, the same thing is a file here by pull request:

```
decks/<slug>.json
{
 "name": "Cave, in order",
 "note": "Every Cave shooter the deck knows, oldest first.",
 "ids": ["donpachi", "ddonpach", "dfeveron"],
 "cover": "ddonpach",
 "author": "Lee Foot"
}
```

- The file name is the slug: lower-case letters, digits and dashes.
- `ids` are game ids from `shmup_deck/app/games.json`, in the order you
  want them shown. The easiest way to get them: build the deck on your own
  MiSTer, tap Share, and copy the ids out of the link.
- `note` is optional, up to 300 characters. `cover` is optional, one of the
  ids; the first game otherwise. `author` is optional.
- Between 3 and 200 games. Names up to 60 characters. Nothing offensive in
  the name, note or author; the check refuses it.

Run `python3 tools/build_deck_index.py` before opening the pull request. It
checks every file against the same rules the service applies and rewrites
`decks/index.json`, which is what the app fetches.

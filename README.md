# Sanapsis website

Static site for www.sanapsis.com in English, Finnish and Swedish, built in the "floating page" design (mockup H).

- `docs/` is the finished website. GitHub Pages serves it from the `main` branch, `/docs` folder. No build step is needed on the host.
- `build.py` makes the pages in `docs/`. All page texts are in this file. After changing a text, run `python3 build.py`.
- `docs/assets/` holds the stylesheet, the small menu script for phones, and the images.

Placeholders: text shown as `[yellow brackets]` on the pages still needs writing. Finnish and Swedish texts in yellow without brackets are Claude's draft translations from `translations.py`, waiting for review (see `translations-review.md`).

Preview with `--preview` adds `index.html` to links, for hosts that don't open folder pages (`python3 build.py --preview --out some/folder`).

Not done yet:
- The bug report form does not send anything; the form service depends on the hosting choice.
- Blog posts, Pro category videos, FAQ.
- Redirects from the old Squarespace addresses (/home, /contact, /sanapsis-plus, /sanapsis-fi, /report-a-bug, /privacy-notice).

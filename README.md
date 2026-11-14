# Sanapsis website

The website for the Sanapsis apps, in English, Finnish and Swedish.

## Status

**Live at [www.sanapsis.com](https://www.sanapsis.com).** The site is complete and replaced the old Squarespace site. It is updated regularly, mostly with new blog posts.

## How it works

It is a static site, served by GitHub Pages. There is no build step on the host.

- `docs/` is the finished website. GitHub Pages serves it from the `main` branch, `/docs` folder.
- `build.py` makes the pages in `docs/`. All page texts are in this file. After changing a text, run `python3 build.py`.
- `docs/assets/` holds the stylesheet, the small menu script for phones, and the images.
- `blog_posts.json` holds the blog posts.

Preview with `--preview` adds `index.html` to links, for hosts that don't open folder pages (`python3 build.py --preview --out some/folder`).

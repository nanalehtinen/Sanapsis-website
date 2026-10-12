"""Import the old Squarespace blog (www.sanapsis.com/blog) into blog_posts.json + docs/assets/img/blog/.

Run once: python3 tools/import_blog.py path/to/all.json
all.json = the "items" of every page of https://www.sanapsis.com/blog?format=json, newest first.
Post text is kept as written; only the HTML is simplified to the tags the new site styles.
"""
import datetime
import hashlib
import html
import json
import os
import re
import subprocess
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(ROOT, "docs", "assets", "img", "blog")
SKIP = {"script", "style", "template", "noscript", "svg", "xml", "iframe", "form"}
KEEP = {"p", "h2", "h3", "h4", "ul", "ol", "li", "strong", "em", "a", "br", "blockquote", "hr", "figure", "figcaption"}
RENAME = {"b": "strong", "i": "em", "h1": "h2"}
VOID = {"br", "hr", "img"}

# Old site pages -> new site pages (relative to the site root).
OLD_PAGES = {"": "", "home": "pro/", "sanapsis-plus": "plus/", "contact": "support/", "report-a-bug": "support/"}


def slugify(title):
    s = title.lower().replace("+", " plus ")
    s = re.sub(r"[^a-z0-9åäö]+", "-", s).strip("-")
    s = s.replace("å", "a").replace("ä", "a").replace("ö", "o")
    return s[:60].rstrip("-")


def fetch_image(url, slug, n):
    """Download one image, save as an optimised JPEG (max 1200 px wide). Returns the file name."""
    os.makedirs(os.path.join(IMG_DIR, slug), exist_ok=True)
    name = f"{n:02d}.jpg"
    out = os.path.join(IMG_DIR, slug, name)
    if not os.path.exists(out):
        tmp = out + ".src"
        subprocess.run(["curl", "-sSL", "--retry", "4", "--retry-all-errors", "-H", "Accept: image/jpeg,image/png", "-o", tmp, url + "?format=1500w"], check=True)
        subprocess.run(["convert", tmp + "[0]", "-background", "white", "-flatten", "-resize", "1200x>",
                        "-strip", "-quality", "82", "-sampling-factor", "4:2:0", out], check=True)
        os.remove(tmp)
    return name


class Cleaner(HTMLParser):
    def __init__(self, slug, slugs_by_old):
        super().__init__(convert_charrefs=True)
        self.slug, self.slugs_by_old = slug, slugs_by_old
        self.out, self.skip, self.stack, self.images = [], 0, [], []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self.skip or tag in SKIP:
            if tag in SKIP and tag not in VOID:
                self.skip += 1
            return
        tag = RENAME.get(tag, tag)
        if tag == "img":
            src = a.get("data-src") or a.get("data-image") or a.get("src") or ""
            if "squarespace" not in src:
                return
            src = src.split("?")[0]
            if src in [i[0] for i in self.images]:
                return
            name = fetch_image(src, self.slug, len(self.images) + 1)
            self.images.append((src, name))
            alt = html.escape(a.get("alt") or "", quote=True)
            self.out.append(f'<img src="ASSET/img/blog/{self.slug}/{name}" alt="{alt}" loading="lazy">')
            return
        if tag not in KEEP:
            return
        if tag == "a":
            self.out.append(f'<a href="{html.escape(self.link(a.get("href", "")), quote=True)}">')
        else:
            self.out.append(f"<{tag}>")
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in SKIP and tag not in VOID:
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        tag = RENAME.get(tag, tag)
        if tag in KEEP and tag not in VOID and tag in self.stack:
            while self.stack:
                t = self.stack.pop()
                self.out.append(f"</{t}>")
                if t == tag:
                    break

    def handle_data(self, data):
        if not self.skip:
            self.out.append(html.escape(data, quote=False))

    def link(self, href):
        m = re.match(r"(?:https?://(?:www\.)?sanapsis\.com)?/(.*)$", href)
        if not m or href.startswith("//"):
            return href
        path = m.group(1).split("?")[0].strip("/")
        if path.startswith("blog/") and path in self.slugs_by_old:
            return f"SITE/blog/{self.slugs_by_old[path]}/"
        return "SITE/" + OLD_PAGES.get(path, "")


def tidy(body):
    body = re.sub(r"\s+", " ", body)
    body = re.sub(r"<(p|h2|h3|h4|li|figcaption|em|strong)>\s*</\1>", "", body)
    body = re.sub(r"<figure>\s*</figure>", "", body)
    body = re.sub(r"\s*(</?(?:p|h2|h3|h4|ul|ol|li|figure|figcaption|blockquote|hr)>)\s*", r"\1", body)
    body = re.sub(r"(<br>)+</p>", "</p>", body)
    return body.replace("</p>", "</p>\n").replace("</figure>", "</figure>\n").strip()


def excerpt_of(item, body):
    ex = re.sub(r"<[^>]+>", " ", item.get("excerpt") or "")
    ex = html.unescape(re.sub(r"\s+", " ", ex)).strip()
    if ex:
        return ex
    first = re.search(r"<p>(.*?)</p>", body)
    text = html.unescape(re.sub(r"<[^>]+>", "", first.group(1))).strip() if first else ""
    if len(text) > 220:
        cut = text[:220]
        text = cut[: max(cut.rfind(". "), cut.rfind("! "), cut.rfind("? ")) + 1] or cut.rsplit(" ", 1)[0] + "…"
    return text


def category(title, body, date):
    """Claude's judgement for the filter chips: the old blog had no categories."""
    plus = (title + body).count("Sanapsis+")
    pro = len(re.findall(r"Sanapsis ?Pro|SANAPSIS PRO", title + body, re.I))
    if plus > pro:
        return "Sanapsis+"
    if pro or date >= "2021-04-01":
        return "SanapsisPro"
    return ""


def main(src):
    items = json.load(open(src))
    slugs, slugs_by_old = [], {}
    for it in items:
        s = slugify(it["title"].strip()) or "post"
        while s in slugs:
            s += "-2"
        slugs.append(s)
        slugs_by_old[it["fullUrl"].strip("/")] = s
    posts = []
    for it, slug in zip(items, slugs):
        c = Cleaner(slug, slugs_by_old)
        c.feed(it["body"])
        body = tidy("".join(c.out))
        date = datetime.datetime.fromtimestamp(it["publishOn"] / 1000, datetime.timezone(datetime.timedelta(hours=3))).date()
        lead = ""
        asset = (it.get("assetUrl") or "").split("?")[0]
        if asset and "squarespace" in asset and not asset.endswith("/"):
            known = dict(c.images)
            lead = f"{slug}/{known[asset]}" if asset in known else f"{slug}/{fetch_image(asset, slug, 0)}"
        elif c.images:
            lead = f"{slug}/{c.images[0][1]}"
        posts.append(dict(slug=slug, title=html.unescape(it["title"]).strip(), date=date.isoformat(),
                          old_url=it["fullUrl"], category=category(it["title"], body, date.isoformat()),
                          excerpt=excerpt_of(it, body), lead=lead, body=body))
        print(date, slug, len(c.images), "images", posts[-1]["category"] or "-")
    json.dump(posts, open(os.path.join(ROOT, "blog_posts.json"), "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1])

#!/usr/bin/env python3
"""Builds the static Sanapsis site into ./docs (served by GitHub Pages).

Run:  python3 build.py
Pages are plain HTML, so the ./docs folder can be served by GitHub Pages or
Cloudflare Pages as is. Texts live in the PAGES dictionaries below.
Text wrapped in ph() is a placeholder that still needs writing.
"""
import html
import re
import json
import urllib.parse
import os
import sys

from translations import (ABOUT, APPROVED, NANA_FI, NANA_FI_ABOUT, NANA_FI_FOOTER_BUG,
                          NANA_FI_PLUS, NANA_FI_PRO, T, EN_DRAFT, EN_DRAFT_ABOUT,
                          EN_DRAFT_PLUS, EN_DRAFT_PRO, NANA, BLOG_NAME, NANA_EN_PLUS_P2,
                          SV, SV_PRO, SV_ABOUT)

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")
if "--out" in sys.argv:
    ROOT = os.path.abspath(sys.argv[sys.argv.index("--out") + 1])

# Links taken from the current www.sanapsis.com pages.
LINKS = {
    "pro_store": {"en": "https://apps.apple.com/us/app/sanapsis/id562594448",
                  "fi": "https://apps.apple.com/fi/app/sanapsis/id562594448",
                  "sv": "https://apps.apple.com/se/app/sanapsis/id562594448"},
    "lite_store": "https://apps.apple.com/us/app/sanapsis-lite/id1498324369",
    "plus_ios": {"en": "https://apps.apple.com/us/app/sanapsis/id1538368855",
                 "fi": "https://apps.apple.com/fi/app/sanapsis/id1538368855",
                 "sv": "https://apps.apple.com/se/app/sanapsis/id1538368855"},
    "plus_android": "https://play.google.com/store/apps/details?id=net.puheklinikka.sanapsis.plus.paid",
    "survey": "https://docs.google.com/forms/d/e/1FAIpQLSdIjSR9CeAn4M-SU6pFMydha4Se2FIc-rOR6Kv4jv2Wvd8CyQ/viewform?usp=sharing",
    "email": "sanapsis@puheklinikka.net",
    # Nana, 12 Oct 2026. LinkedIn: the link Nana sent was the admin dashboard; this is the public showcase page (unverified).
    "facebook": "https://www.facebook.com/Sanapsis/",
    "linkedin": "https://www.linkedin.com/showcase/106458612/",
    "clinic": "https://www.puheklinikka.net",
}

LANGS = ["en", "fi", "sv"]
# Language being built; placeholders are labelled with it.
CUR_LANG = "en"
# Path of each page inside a language folder ("" is the home page).
SLUGS = ["", "pro/", "plus/", "about/", "support/", "blog/", "privacy/"]

ARROW = ('<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2.2" '
         'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>')
MENU_ICON = ('<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#343434" stroke-width="2" '
             'stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>')


def ph(text):
    """Placeholder: visible, highlighted, still to be written."""
    return f'<span class="ph">[{html.escape(text)}]</span>'


def draft(text, lang):
    """Claude's draft translation: highlighted until Nana approves it (translations.py)."""
    if lang in APPROVED:
        return text
    return f'<span class="ph" lang="{lang}">{text}</span>'


def en_t(english):
    """English text: Claude's new draft (highlighted) if there is one, else the current text."""
    if english in EN_DRAFT:
        return draft(html.escape(EN_DRAFT[english], quote=False), "en")
    return english


def fi_ph(english):
    """Finnish/Swedish text: Nana's text, else Claude's draft (highlighted), else a placeholder."""
    if CUR_LANG == "fi" and english in NANA_FI:
        return html.escape(NANA_FI[english], quote=False)
    if CUR_LANG == "sv" and english in SV:
        return draft(html.escape(SV[english], quote=False), "sv")
    if english in T:
        return draft(html.escape(T[english][LANGS.index(CUR_LANG) - 1], quote=False), CUR_LANG)
    return ph(f"{CUR_LANG.upper()}: {english}")


# Interface words. Finnish entries are placeholders unless the current site has them.
UI = {
    "en": {
        "nav_pro": "SanapsisPro", "nav_plus": "Sanapsis+", "nav_support": "Support",
        "nav_blog": "Blog", "nav_about": "About us", "menu": "Open menu", "skip": "Skip to content",
        "f_bug": "Report a bug", "f_survey": "User survey", "f_privacy": "Privacy notice", "f_contact": "Contact",
        "lang_label": "Language",
    },
}


def ui_placeholders(code, privacy_word, lang_word):
    def label(e):
        if e in T:
            return draft(T[e][LANGS.index(code) - 1], code)
        return ph(f"{code.upper()}: {e}")
    return {
        "nav_pro": "SanapsisPro", "nav_plus": "Sanapsis+", "nav_support": label("Support"),
        "nav_blog": label("Blog"), "nav_about": label("About"), "menu": "Menu", "skip": "Skip to content",
        "f_bug": label("Report a bug"), "f_survey": label("User survey"),
        "f_privacy": privacy_word, "f_contact": label("Contact"),
        "lang_label": lang_word,
    }


# Privacy words come from the current Finnish and Swedish Sanapsis+ pages.
UI["fi"] = ui_placeholders("fi", "Tietosuojaseloste", "Kieli")
UI["fi"]["f_bug"] = NANA_FI_FOOTER_BUG
UI["sv"] = ui_placeholders("sv", "Integritetspolicy", "Språk")
# All Swedish stays highlighted until Nana approves it (5 Oct 2026).
UI["sv"]["f_privacy"] = draft("Integritetspolicy", "sv")


# All links are relative, so the site works at a domain root or in a subfolder
# (for example a GitHub Pages project address). BASE is set per page while building.
BASE = ""
# Changes whenever site.css changes, so browsers fetch the new stylesheet instead of a cached one.
import hashlib
CSS_VERSION = hashlib.sha1(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs", "assets", "css", "site.css"), "rb").read()).hexdigest()[:8]
# --preview adds index.html to page links, for hosts that do not open folder indexes.
PREVIEW = "--preview" in sys.argv


def prefix(lang):
    return "" if lang == "en" else f"{lang}/"


def url(lang, slug):
    target = prefix(lang) + slug
    if PREVIEW:
        target += "index.html"
    return (BASE + target) or "./"


def asset(path):
    return BASE + "assets/" + path


def header(lang, slug):
    u = UI[lang]
    items = [("pro/", u["nav_pro"], "nav-pro"), ("plus/", u["nav_plus"], "nav-plus"),
             ("support/", u["nav_support"], ""), ("blog/", u["nav_blog"], ""), ("about/", u["nav_about"], "")]
    nav = []
    for s, label, cls in items:
        cur = ' aria-current="page"' if s == slug or (s == "blog/" and slug.startswith("blog/")) else ""
        c = f' class="{cls}"' if cls else ""
        nav.append(f'<a href="{url(lang, s)}"{c}{cur}>{label}</a>')
    langs = []
    for l in LANGS:
        cur = ' aria-current="true"' if l == lang else ""
        langs.append(f'<a href="{url(l, slug)}" lang="{l}" hreflang="{l}"{cur}>{l.upper()}</a>')
    return f"""<header class="site-header">
      <a class="logo" href="{url(lang, '')}"><img src="ASSET/img/logo.svg" alt="Sanapsis" width="192" height="44"></a>
      <button class="menu-toggle" type="button" aria-label="{u['menu']}" aria-expanded="false" aria-controls="main-nav">{MENU_ICON}</button>
      <nav id="main-nav" class="main-nav" aria-label="Main">
        {' '.join(nav)}
        <span class="lang-switch" aria-label="{u['lang_label']}">{''.join(langs)}</span>
      </nav>
    </header>"""


def footer(lang):
    u = UI[lang]
    return f"""<footer class="site-footer">
    <nav class="footer-nav" aria-label="Footer">
      <a href="{url(lang, 'support/')}#report">{u['f_bug']}</a>
      <a href="{LINKS['survey']}">{u['f_survey']}</a>
      <a href="{url(lang, 'privacy/')}">{u['f_privacy']}</a>
      <a href="{url(lang, 'support/')}#contact">{u['f_contact']}</a>
      <a href="{LINKS['facebook']}">Facebook</a>
      <a href="{LINKS['linkedin']}">LinkedIn</a>
    </nav>
    <!-- Logo on the right: it will become the stand.chat chat icon (Nana, 5 Oct 2026). -->
    <img class="brand" src="ASSET/img/logo-footer.svg" alt="Sanapsis" width="140" height="32">
  </footer>"""


# Social preview (Open Graph) tags, added 15-18 Oct 2026. Links must be absolute, so they point at the live domain.
SITE_URL = "https://www.sanapsis.com/"
OG_LOCALE = {"en": "en_US", "fi": "fi_FI", "sv": "sv_FI"}
# Finnish and Swedish page titles and descriptions: Claude's wording (18 Oct 2026), for Nana to check.
META_L10N = {
    "": {"fi": ("Sanapsis", "Sanapsis-sovellukset puheterapiaan: SanapsisPro ja Sanapsis+."),
         "sv": ("Sanapsis", "Sanapsis-appar för talterapi: SanapsisPro och Sanapsis+.")},
    "pro/": {"fi": ("SanapsisPro | Sanapsis", "SanapsisPro: iPad-sovellus puheterapeuteille aikuisneurologiseen puheterapiaan."),
             "sv": ("SanapsisPro | Sanapsis", "SanapsisPro: en iPad-app för talterapeuter som arbetar med vuxna.")},
    "plus/": {"fi": ("Sanapsis+ | Sanapsis", "Sanapsis+: puheen ja kielen kotiharjoitteluun iPadilla ja Android-laitteilla."),
              "sv": ("Sanapsis+ | Sanapsis", "Sanapsis+: övning av tal och språk hemma på iPad och Android.")},
    "about/": {"fi": ("Meistä | Sanapsis", "Tietoa Sanapsiksesta ja sen tekijöistä."),
               "sv": ("Om oss | Sanapsis", "Om Sanapsis och teamet bakom apparna.")},
    "support/": {"fi": ("Tuki | Sanapsis", "Ilmoita virheestä tai ota yhteyttä Sanapsis-tiimiin."),
                 "sv": ("Support | Sanapsis", "Rapportera ett fel eller kontakta Sanapsis-teamet.")},
    "privacy/": {"fi": ("Tietosuojaseloste | Sanapsis", "Miten Sanapsis käsittelee henkilötietoja."),
                 "sv": ("Integritetspolicy | Sanapsis", "Hur Sanapsis hanterar personuppgifter.")},
}
BLOG_DESC = {"en": "News and updates about the Sanapsis apps.",
             "fi": "Uutisia ja päivityksiä Sanapsis-sovelluksista (englanniksi).",
             "sv": "Nyheter och uppdateringar om Sanapsis-apparna (på engelska)."}
OG_IMAGE = {"pro/": "og/pro.jpg", "plus/": "og/plus.jpg", "about/": "og/about.jpg"}


def og_tags(lang, slug, title, description, image):
    image = image or OG_IMAGE.get(slug, "og/home.jpg")
    full = SITE_URL + prefix(lang) + slug
    e = lambda v: html.escape(v, quote=True)
    return "\n  ".join([
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="Sanapsis">',
        f'<meta property="og:title" content="{e(html.unescape(title))}">',
        f'<meta property="og:description" content="{e(description)}">',
        f'<meta property="og:url" content="{e(full)}">',
        f'<meta property="og:image" content="{SITE_URL}assets/img/{image}">',
        f'<meta property="og:locale" content="{OG_LOCALE[lang]}">',
        '<meta name="twitter:card" content="summary_large_image">',
    ])


def page(lang, slug, title, description, body, image=None):
    if lang in META_L10N.get(slug, {}):
        title, description = META_L10N[slug][lang]
    alternates = "\n  ".join(
        f'<link rel="alternate" hreflang="{l}" href="{url(l, slug)}">' for l in LANGS)
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{html.escape(description)}">
  {og_tags(lang, slug, title, description, image)}
  {alternates}
  <link rel="icon" href="ASSET/../favicon.ico">
  <link rel="stylesheet" href="ASSET/css/site.css?v={CSS_VERSION}">
  <script src="ASSET/js/menu.js" defer></script>
  <script src="ASSET/js/video.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#content">{UI[lang]['skip']}</a>
  <div class="page">
    {header(lang, slug)}
    <main id="content">
{body}
    </main>
  </div>
  {footer(lang)}
</body>
</html>
"""


# ---------------------------------------------------------------- Home

def home(lang):
    t = {
        "en": dict(
            h1="Supporting Speech Therapy with Technology",
            intro=en_t("Two separate apps, each supporting a different part of the therapy journey."),
            pro_eyebrow="For speech-language pathologists",
            pro_desc="SanapsisPro is built for professional SLPs. It transforms your iPad into a flexible, open-ended library of therapy ideas and materials.",
            pro_more="Learn more about SanapsisPro",
            plus_eyebrow="For practice at home",
            plus_desc="If you are looking for a solution to work on speech and communication at home, Sanapsis+ is built for you.",
            plus_more="Learn more about Sanapsis+",
            hero_alt="Two smiling men at a table",
        ),
        "fi": dict(
            h1=fi_ph("Supporting Speech Therapy with Technology"),
            intro=fi_ph("Two separate apps, each supporting a different part of the therapy journey."),
            pro_eyebrow=fi_ph("For speech-language pathologists"),
            pro_desc=fi_ph("SanapsisPro is built for professional SLPs. It transforms your iPad into a flexible, open-ended library of therapy ideas and materials."),
            pro_more=fi_ph("Learn more about SanapsisPro"),
            plus_eyebrow=fi_ph("For practice at home"),
            plus_desc=fi_ph("If you are looking for a solution to work on speech and communication at home, Sanapsis+ is built for you."),
            plus_more=fi_ph("Learn more about Sanapsis+"),
            hero_alt="Two smiling men at a table",
        ),
    }["en" if lang == "en" else "fi"]
    body = f"""      <div class="pad"><img class="hero" src="ASSET/img/home-hero.jpg" alt="{t['hero_alt']}"></div>
      <div class="pad home-intro">
        <h1>{t['h1']}</h1>
        <p>{t['intro']}</p>
      </div>
      <div class="pad app-cards">
        <a class="appcard pro" href="{url(lang, 'pro/')}">
          <span class="eyebrow">{t['pro_eyebrow']}</span>
          <span class="name">SanapsisPro</span>
          <span class="desc">{t['pro_desc']}</span>
          <img src="ASSET/img/pro-card.jpg" alt="Speech-language pathologist working with a client on an iPad">
          <span class="more">{t['pro_more']} {ARROW.format(c='#b35f00')}</span>
        </a>
        <a class="appcard plus" href="{url(lang, 'plus/')}">
          <span class="eyebrow">{t['plus_eyebrow']}</span>
          <span class="name">Sanapsis+</span>
          <span class="desc">{t['plus_desc']}</span>
          <img src="ASSET/img/plus-card.jpg" alt="Hands on an iPad doing a Sanapsis+ word exercise outdoors, with a small black dog in the background" style="object-position: center 40%">
          <span class="more">{t['plus_more']} {ARROW.format(c='#123966')}</span>
        </a>
      </div>"""
    return page(lang, "", "Sanapsis", "Sanapsis apps for speech and language therapy: SanapsisPro and Sanapsis+.", body)


# ---------------------------------------------------------------- SanapsisPro

# Vimeo videos of the SanapsisPro categories, taken from the old site's SanapsisPro page (12 Oct 2026).
# Semantics and Perseveration share one video there. "Key Features" is PRO_KEY_VIDEO.
PRO_VIDEOS = {"Reading": "119886306", "Writing": "119887345", "Production": "119886305",
              "Comprehension": "119886304", "Semantics": "119886307", "Perseveration": "119886307"}

PRO_KEY_VIDEO = "119886303"
# Poster stills: the Vimeo thumbnails of the same videos (fetched 12 Oct 2026, thread "Vimeo preview pictures").
PRO_VIDEO_POSTERS = {"Reading": "reading", "Writing": "writing", "Production": "production",
                     "Comprehension": "comprehension", "Semantics": "semantics-perseveration",
                     "Perseveration": "semantics-perseveration", "Key features": "key-features"}

PRO_CATEGORIES_EN = [
    # Order: Nana, 12 Oct 2026 (row 1 Production, Comprehension, Reading; row 2 Writing, Semantics, Perseveration).
    ("Production", "Basic naming (nouns), creating a sentence from given words, and giving instructions."),
    ("Comprehension", "YES/NO questions, following instructions, and questions based on text."),
    ("Reading", "Tasks from simple word and picture matching to more complex pieces of text."),
    ("Writing", "Copying letters with your fingertips, using the keyboard to fill in sentences, and complex writing tasks using paper and pen."),
    ("Semantics", 'Exercises such as "Is this simile true", which works especially well with high-level TBI patients.'),
    ("Perseveration", 'Material to work with those who tend to "get stuck" in their speech or even comprehension.'),
]


def pro(lang):
    en = lang == "en"
    paras_en = [
        "SanapsisPro is a rehabilitation app for iPad, designed for professional Speech and Language Pathologists (SLPs) working with adults who have acquired communication difficulties.",
        "It offers therapy materials across all core language areas, providing clinicians with structured examples and ideas to support the therapy process. SanapsisPro includes over 35 types of exercises organized into six categories.",
        "All materials have been specifically developed and tested for adult speech and language therapy. SanapsisPro includes all three languages, English (US), Finnish, and Swedish, in the same download.",
    ]
    f = en_t if en else fi_ph
    if lang == "fi":
        paras = NANA_FI_PRO
    elif en:
        paras = [draft(p, "en") for p in EN_DRAFT_PRO]
    elif lang == "sv":
        paras = [draft(p, "sv") for p in SV_PRO]
    else:
        paras = [f(p) for p in paras_en]
    play_icon = '<span class="play" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24"><path d="M8 5v14l11-7z" fill="#ffffff"/></svg></span>'
    # The videos exist in English only (Nana, 12 Oct 2026): FI and SV keep an empty box in their place.
    def cat_media(n):
        if not en:
            return '<div class="video-box" aria-hidden="true"></div>'
        return (f'<button class="video-poster cat-video" type="button" data-vimeo="{PRO_VIDEOS[n]}" data-ratio="4 / 3" '
                f'aria-label="Play video: {html.escape(n)}"><img src="ASSET/img/pro-videos/{PRO_VIDEO_POSTERS[n]}.jpg" alt="" loading="lazy">{play_icon}</button>')
    # FI and SV: the heading and text sit inside the box for now (Nana, 12 Oct 2026).
    cats = "\n".join(
        (f'        <div class="tile">{cat_media(n)}<h3>{f(n)}</h3><p>{f(d)}</p></div>' if en else
         f'        <div class="tile"><div class="video-box text-box"><h3>{f(n)}</h3><p>{f(d)}</p></div></div>')
        for n, d in PRO_CATEGORIES_EN)
    # Key Features video above the categories, English only, as on the old site's SanapsisPro page (Nana, 12 Oct 2026).
    # Caption: Nana's wording (12 Oct 2026).
    key_video = "" if not en else (
        '      <div class="pad key-wrap"><div class="key-video">\n'
        f'        <button class="video-poster cat-video" type="button" data-vimeo="{PRO_KEY_VIDEO}" data-ratio="4 / 3" '
        f'aria-label="Play video: Key features"><img src="ASSET/img/pro-videos/key-features.jpg" alt="" loading="lazy">{play_icon}</button>\n'
        '        <div class="key-text"><h3>Key features</h3><p>In this video, you learn about the key features of SanapsisPro. '
        'We show you how to navigate between tasks and adjust the settings.</p>'
        '<p>You will also learn why SanapsisPro does not provide direct feedback to the patient.</p></div>\n'
        '      </div></div>\n')
    body = f"""      <div class="pad"><img class="hero short" src="ASSET/img/pro-hero.jpg" alt="Therapist and client at a table with an iPad"></div>
      <div class="pad app-intro pro">
        <div class="intro-head stack">
          <div class="accent-line pro"></div>
          <div class="eyebrow">{f('For speech-language pathologists')}</div>
          <h1>SanapsisPro</h1>
        </div>
        <div class="text stack">
          <p class="lead">{paras[0]}</p>
          <div class="body-text stack">{"".join(f"<p>{p}</p>" for p in paras[1:])}</div>
          <div class="get-box">
            <div class="title">{f('Get SanapsisPro')}</div>
            <div class="note">{f('iPad. There are no in-app purchases, now or in the future. All updates, including new exercises, are included for free.')}</div>
            <a class="button pro" href="{LINKS['pro_store'][lang]}">{f('Download on the App Store')}</a>
            <a class="text-link pro" href="{LINKS['lite_store']}">{f('Try SanapsisLite first')}</a>
          </div>
        </div>
        <div class="shots">
          <img class="shot" src="ASSET/img/pro-screen-1.jpg" alt="SanapsisPro start screen with six categories: Production, Comprehension, Reading, Writing, Semantics, Perseveration" width="1024" height="746">
          <img class="shot" src="ASSET/img/pro-screen-2.jpg" alt="SanapsisPro info panel with welcome text, navigation tips and notes for therapists" width="1024" height="746">
        </div>
      </div>
      <div class="pad"><h2 class="section-title">{f('Six exercise categories')}</h2></div>
{key_video}      <div class="pad tiles categories">
{cats}
      </div>
      <div class="notice pro">
        <strong>{f('Important information')}</strong>
        <p>{f('Sanapsis is intended for use in therapy sessions under the guidance of a licensed Speech-Language Pathologist (SLP). It is not designed for independent use.')}</p>
      </div>"""
    return page(lang, "pro/", "SanapsisPro | Sanapsis",
                "SanapsisPro: an iPad app for speech-language pathologists working with adults.", body)


# ---------------------------------------------------------------- Sanapsis+

def plus(lang):
    if lang == "en":
        t = dict(
            eyebrow="For practice at home",
            lead="Sanapsis+ is designed for individuals with acquired speech and communication difficulties resulting from neurological conditions, such as aphasia, stroke, traumatic brain injury, or other neurological illnesses.",
            p2="With Sanapsis+, you can actively practice communication across all core language areas: Speaking, Listening, Reading, and Writing.",
            p3="In addition to targeted language exercises, Sanapsis+ offers ideas and guidance for working on communication skills at home and in everyday environments, because real-life situations are where communication matters most.",
            get="Get Sanapsis+",
            get_note="iPad and Android. All materials are available in English, Finnish, and Swedish.",
            ios="iPad (App Store)", android="Android (Google Play)",
            areas_title="Four core language areas",
            areas=["Speaking", "Listening", "Reading", "Writing"],
            vocab_title="Everyday vocabulary",
            vocab="Exercises use familiar, everyday vocabulary and are organized into categories including: Home, Objects, Food and Drink, Clothes, Surroundings, Travel, Recreation, and Verbs.",
            note_title="Please note",
            note="Sanapsis+ can be used independently, with a loved one, or with the guidance of a licensed Speech and Language Pathologist (SLP). However, Sanapsis+ is not a replacement for professional speech therapy. If you are experiencing difficulties with speech, language, or communication, we encourage you to contact a licensed SLP in your area for personalized support.",
            shot="ASSET/img/plus-screen-en.jpg",
            video="554958858", play="Play the Sanapsis+ intro video",
            shot_alt="Sanapsis+ start screen with four activities: Listening, Speaking, Reading, Writing",
        )
    elif lang == "sv":
        # Swedish texts below are from the current Sanapsis+ Swedish page (sanapsis.com/sanapsis-sv).
        t = dict(
            eyebrow=fi_ph("For practice at home"),
            lead="Sanapsis+ är utvecklad för personer med tal- och kommunikationssvårigheter på grund av neurologiska orsaker. Dessa kan vara exempelvis afasi, stroke, hjärnskada eller progressiva neurologiska sjukdomar.",
            p2="Med hjälp av Sanapsis+ kan du aktivera och stärka kommunikationsförmågan på ordnivå inom fyra delområden: benämning, lyssnande, läsning och skrivning.",
            p3="Förutom övningarna innehåller appen tips och idéer för att öva tal och språk i vardagen – antingen självständigt eller tillsammans med en närstående. Tipsen är kopplade till vardagliga situationer och omgivningar, eftersom där uppstår de viktigaste samtalen och de insikter som bär vidare.",
            get=fi_ph("Get Sanapsis+"),
            get_note="Sanapsis+ är lätt att använda – att komma igång med träningen är bokstavligen bara några klick ifrån!",
            ios="iPad (App Store)", android="Android (Google Play)",
            areas_title=fi_ph("Four core language areas"),
            areas=["Benämning", "Lyssnande", "Läsning", "Skrivning"],
            vocab_title=fi_ph("Everyday vocabulary"),
            vocab="Alla övningar i Sanapsis+ bygger på bekanta vardagsord inom följande kategorier: hem, föremål, mat och dryck, kläder, miljö, resor, fritid och verb. Alla övningar och material finns tillgängliga på tre språk: finska, svenska och engelska.",
            note_title=fi_ph("Please note"),
            note="Du kan använda Sanapsis+ självständigt, tillsammans med en närstående eller under handledning av en talterapeut. Sanapsis+ ersätter inte talterapi, och vi kan inte garantera dess individuella effektivitet. Om du behöver råd eller stöd i träningen rekommenderar vi att du kontaktar en legitimerad talterapeut.",
            shot="ASSET/img/plus-screen-sv.jpg",
            video="554407548", play="Play the Sanapsis+ intro video (Swedish)",
            shot_alt="Sanapsis+ start screen in Swedish with four activities: Lyssnande, Benämning, Läsning, Skrivning",
        )
    else:
        # Finnish texts below are from the current Sanapsis+ Finnish page (sanapsis.com/sanapsis-fi).
        t = dict(
            eyebrow=fi_ph("For practice at home"),
            lead="Sanapsis+ on suunniteltu henkilöille, joilla on puheen ja kommunikoinnin haasteita neurologisista syistä johtuen. Näitä voivat olla esimerkiksi afasia, aivoverenkiertohäiriö (AVH), aivovamma tai etenevät neurologiset sairaudet.",
            p2="Sanapsis+ -sovelluksen avulla voit aktivoida ja vahvistaa sanatasoista kommunikointia neljällä osa-alueella: puhuminen, kuuntelu, lukeminen ja kirjoittaminen.",
            p3="Tehtävien lisäksi sovellus tarjoaa ideoita ja neuvoja puheen ja kielen harjoitteluun arjessa – itsenäisesti tai yhdessä läheisen kanssa. Vinkit liittyvät tavallisiin tilanteisiin ja ympäristön hyödyntämiseen, sillä arjessa tapahtuva kommunikointi ja yhteiset oivallukset kantavat kauas!",
            get=fi_ph("Get Sanapsis+"),
            get_note="Sanapsis+ on helppokäyttöinen, ja harjoittelun aloittaminen on kirjaimellisesti vain muutaman napautuksen päässä!",
            ios="iPad (App Store)", android="Android (Google Play)",
            areas_title=fi_ph("Four core language areas"),
            areas=["Puhuminen", "Kuuntelu", "Lukeminen", "Kirjoittaminen"],
            vocab_title=fi_ph("Everyday vocabulary"),
            vocab="Kaikki Sanapsis+ sovelluksen tehtävät pohjautuvat tuttuihin arjen sanoihin seuraavista kategorioista: koti, esineet, ruoka ja juoma, vaatteet, ympäristö, matkustaminen, vapaa-aika ja verbit. Harjoitukset ja materiaalit ovat sisältyvät sovellukseen kolmella kielellä: suomi, ruotsi ja englanti.",
            note_title=fi_ph("Please note"),
            note="Voit käyttää Sanapsis+ -sovellusta itsenäisesti, yhdessä läheisen kanssa tai puheterapeutin ohjauksessa. Sanapsis+ ei korvaa puheterapiaa, emmekä voi taata sen yksilöllistä vaikuttavuutta. Mikäli tarvitset neuvoja tai tukea harjoitteluun, suosittelemme ottamaan yhteyttä laillistettuun puheterapeuttiin.",
            shot="ASSET/img/plus-screen-fi.jpg",
            video="544117078", play="Play the Sanapsis+ intro video (Finnish)",
            shot_alt="Sanapsis+ start screen in Finnish with four activities: Kuuntelu, Nimeäminen, Lukeminen, Kirjoittaminen",
        )
    if lang == "fi":
        t.update(NANA_FI_PLUS)
    elif lang == "en":
        t.update({k: draft(v, "en") for k, v in EN_DRAFT_PLUS.items()})
        t["p2"] = NANA_EN_PLUS_P2
    else:
        # Swedish: texts from the current Swedish page, highlighted until Nana approves them.
        for k in ("lead", "p2", "p3", "get_note", "vocab", "note"):
            t[k] = draft(t[k], "sv")
        t["areas"] = [draft(a, "sv") for a in t["areas"]]
    area_cls = ["speaking", "listening", "reading", "writing"]
    areas = "\n".join(f'        <div class="area {c}">{a}</div>' for c, a in zip(area_cls, t["areas"]))
    body = f"""      <div class="pad"><img class="hero short" src="ASSET/img/plus-hero.jpg" alt="Smiling older woman on a sofa holding a tablet" style="object-position: center 30%"></div>
      <div class="pad app-intro plus">
        <div class="text stack">
          <div class="accent-line plus"></div>
          <div class="eyebrow">{t['eyebrow']}</div>
          <h1>Sanapsis+</h1>
          <p class="lead">{t['lead']}</p>
          <div class="body-text stack"><p>{t['p2']}</p><p>{t['p3']}</p></div>
          <div class="get-box">
            <div class="title">{t['get']}</div>
            <div class="note">{t['get_note']}</div>
            <div class="buttons">
              <a class="button plus" href="{LINKS['plus_ios'][lang]}">{t['ios'].replace(' (', '<br>(')}</a>
              <a class="button plus" href="{LINKS['plus_android']}">{t['android'].replace(' (', '<br>(')}</a>
            </div>
          </div>
        </div>
        <div class="shots">
          <button class="video-poster" type="button" data-vimeo="{t['video']}" aria-label="{t['play']}">
            <img class="shot" src="{t['shot']}" alt="{t['shot_alt']}" width="2048" height="2670">
            <span class="play" aria-hidden="true"><svg width="28" height="28" viewBox="0 0 24 24"><path d="M8 5v14l11-7z" fill="#ffffff"/></svg></span>
          </button>
        </div>
      </div>
      <div class="pad"><h2 class="section-title">{t['areas_title']}</h2></div>
      <div class="pad tiles areas">
{areas}
      </div>
      <div class="pad stack" style="padding-bottom: 48px">
        <h2 style="font-weight: 600; font-size: 22px">{t['vocab_title']}</h2>
        <p class="body-text" style="margin: 0">{t['vocab']}</p>
      </div>
      <div class="notice plus">
        <strong>{t['note_title']}</strong>
        <p>{t['note']}</p>
      </div>"""
    return page(lang, "plus/", "Sanapsis+ | Sanapsis",
                "Sanapsis+: speech and language practice at home on iPad and Android.", body)


# ---------------------------------------------------------------- About

def about(lang):
    paras_en = [
        "I'm Nana, lovely to meet you! I'm a Speech-Language Pathologist with a passion for working with adults who have acquired language and communication difficulties. I'm also the lead designer behind the Sanapsis family of applications.",
        f'We began developing <strong>Sanapsis</strong> back in 2009. Our private practice, <a href="{LINKS["clinic"]}">Speech Clinic Ltd (Puheklinikka)</a>, specializes in adult neurological speech therapy. Originally, Sanapsis was created as an internal tool. We wanted something that gave us quick access to high-quality, real-life content that reflected our patients\' everyday environments. Just as importantly, we needed a tool that allowed for flexible goal setting and supported meaningful interaction between therapist and patient.',
        "After a lot (and we mean a lot!) of trial and error, <strong>SanapsisPro</strong> began to resemble the ideal we had imagined.",
        "We owe a huge thank you to our wonderful patients, who have been deeply involved in designing and testing the app. You'll even see some of their faces featured in the materials; they are truly a part of the Sanapsis story.",
        "In early 2021, we launched <strong>Sanapsis+</strong>, based on popular demand, to support independent use at home.",
        "We love to hear from colleagues. If you'd like to test Sanapsis+ with your patients, just let us know.",
    ]
    if lang == "en":
        title, hi, button = "About us", "Hi there.", "Get in touch"
        fill = lambda p: p.format(clinic=LINKS["clinic"], blog=url(lang, "blog/"))
        paras = [fill(p) if isinstance(p, NANA) else draft(fill(p), "en") for p in EN_DRAFT_ABOUT]
    else:
        title, hi, button = fi_ph("About Sanapsis"), fi_ph("Hi there."), fi_ph("Get in touch")
        if lang == "fi":
            paras = [p.format(clinic=LINKS["clinic"], blog=url(lang, "blog/")) for p in NANA_FI_ABOUT]
        else:
            paras = [draft(p.format(clinic=LINKS["clinic"], blog=url(lang, "blog/")), lang) for p in SV_ABOUT]
    ps = "\n".join(f"          <p>{p}</p>" for p in paras)
    body = f"""      <div class="pad page-head"><h1 class="page-title">{title}</h1></div>
      <div class="pad about-body" style="padding-bottom: 48px">
        <h2 class="about-hi" style="font-weight: 600; font-size: 24px">{hi}</h2>
        <div class="about-text body-text">
          <img class="about-photo" src="ASSET/img/about.jpg" alt="Two speech-language pathologists at a table">
{ps}
        </div>
      </div>
      <div class="pad cta-row"><a class="button pro" href="mailto:{LINKS['email']}">{button}</a></div>"""
    return page(lang, "about/", "About | Sanapsis", "About Sanapsis and the team behind it.", body)


# ---------------------------------------------------------------- Support

def support(lang):
    en = lang == "en"
    f = en_t if en else fi_ph
    # FAQ = a stand.chat chat box (Nana, 5 Oct 2026). This card is a mock-up until it is configured.
    # Its sample texts are Claude's and stay highlighted in every language until Nana approves them.
    chat = {
        "en": ("Hi! Ask me anything about SanapsisPro or Sanapsis+.", "Type your question…", "Send"),
        "fi": ("Hei! Kysy minulta mitä tahansa SanapsisProsta tai Sanapsis+:sta.", "Kirjoita kysymyksesi…", "Lähetä"),
        "sv": ("Hej! Fråga mig vad du vill om SanapsisPro eller Sanapsis+.", "Skriv din fråga…", "Skicka"),
    }[lang]
    # Bug reports go by email (Nana, 12 Oct 2026): GitHub Pages can't receive forms, and email lets people attach screenshots.
    # The email subject is Claude's wording.
    mail_subject = {"en": "Bug report", "fi": "Virheilmoitus", "sv": "Felrapport"}[lang]
    # Button label "Report a bug" (Nana, 12 Oct 2026); Finnish uses her footer wording.
    mail_label = {"en": "Report a bug", "fi": NANA_FI_FOOTER_BUG, "sv": draft("Rapportera ett fel", "sv")}[lang]
    # Claude changed "using the form below" to the email wording; highlight removed at Nana's request (15 Oct 2026).
    bug_text = f('Please let us know using the form below. Include the name of the exercise, a description of the task (what you see on the screen), and details of the bug or issue. The more specific, the better. Screenshots are helpful too!')
    mailto = f"mailto:{LINKS['email']}?subject={urllib.parse.quote(mail_subject)}"
    faq = f"""      <div class="faq" id="faq">
        <h2>{f('Frequently asked questions')}</h2>
        <div class="chat-card" aria-label="Chat (placeholder)">
          <div class="chat-head"><span class="chat-avatar"><img src="ASSET/img/icon.svg" alt="" width="22" height="20"></span>Sanapsis</div>
          <div class="chat-body">
            <p class="bubble">{chat[0]}</p>
          </div>
          <div class="chat-input">
            <input type="text" placeholder="{chat[1]}" disabled aria-label="{chat[1]}">
            <button type="button" disabled aria-label="{chat[2]}"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button>
          </div>
        </div>
        <p class="chat-note">{ph("stand.chat chat box goes here")}</p>
      </div>
"""
    # The chat mock-up stays hidden until stand.chat is configured (Nana, 18 Oct 2026): set CHAT_LIVE = True then.
    body = f"""      <div class="pad page-head"><h1 class="page-title">{f('Support')}</h1></div>
{faq if CHAT_LIVE else ""}      <div class="pad two-col">
        <div class="main form" id="report">
          <div class="accent-line"></div>
          <h2>{f('Report a bug')}</h2>
          <p class="body-text" style="margin: 0"><strong>{f('Found a bug in SanapsisPro or Sanapsis+?')}</strong> {bug_text}</p>
          <a class="button" href="{mailto}">{mail_label}</a>
          <p class="body-text" style="margin: 0">{f("We're always happy to hear suggestions for improvement as well!")}</p>
        </div>
        <div class="side">
          <div class="card" id="contact"><h2>{f('Contact')}</h2><a href="mailto:{LINKS['email']}">{LINKS['email']}</a></div>
          <div class="card"><h2>{f('User survey')}</h2><a href="{LINKS['survey']}">{f('Open the user survey')}</a></div>
          <div class="card"><h2>{f('Privacy')}</h2><a href="{url(lang, 'privacy/')}">{UI[lang]['f_privacy']}</a></div>
        </div>
      </div>"""
    return page(lang, "support/", "Support | Sanapsis", "Report a bug or contact the Sanapsis team.", body)


# ---------------------------------------------------------------- Blog

# All posts from the old blog (www.sanapsis.com/blog), imported 12 Oct 2026 by tools/import_blog.py.
# Post text is Nana's, unchanged; the category (filter chips) is Claude's judgement, the old blog had none.
BLOG_POSTS = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "blog_posts.json"), encoding="utf-8"))
BLOG_PER_PAGE = 10
BLOG_CATS = [("", "All", ""), ("sanapsispro/", "SanapsisPro", "pro"), ("sanapsis-plus/", "Sanapsis+", "plus")]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
          "October", "November", "December"]


def nice_date(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return f"{d} {MONTHS[m - 1]} {y}"


def post_tag(post):
    if not post["category"]:
        return ""
    cls = "plus" if post["category"] == "Sanapsis+" else "pro"
    return f' · <span class="tag {cls}">{post["category"]}</span>'


def blog_head(lang, cat):
    chips = []
    for c, label, cls in BLOG_CATS:
        classes = "chip" + (" active" if c == cat else "") + (" " + cls if cls else "")
        cur = ' aria-current="page"' if c == cat else ""
        chips.append(f'          <a class="{classes}" href="{url(lang, "blog/" + c)}"{cur}>{label}</a>')
    chips = "\n".join(chips)
    return f"""      <div class="pad blog-head" lang="en">
        <div class="stack">
          <h1 class="page-title">Blog</h1>
          <p class="blog-name">{BLOG_NAME}</p>
{'' if lang == 'en' else '          <p class="blog-lang">Blog available only in English.</p>'}
        </div>
        <nav class="chips" aria-label="Filter posts">
{chips}
        </nav>
      </div>"""


def blog_list(lang, cat, label, posts, n, pages):
    """One listing page (n = 1..pages) of the posts in a category ('' = all)."""
    base = "blog/" + cat
    rows = []
    for post in posts:
        if post["lead"]:
            thumb = f'<img class="thumb" src="ASSET/img/blog/{post["lead"]}" alt="" loading="lazy">'
        else:
            thumb = '<span class="thumb empty"><img src="ASSET/img/icon.svg" alt="" width="48" height="44"></span>'
        rows.append(f"""        <a class="post" href="{url(lang, 'blog/' + post['slug'] + '/')}">
          {thumb}
          <span class="info">
            <span class="meta">{nice_date(post['date'])}{post_tag(post)}</span>
            <span class="title">{html.escape(post['title'])}</span>
            <span class="excerpt">{html.escape(post['excerpt'])}</span>
          </span>
        </a>""")
    page_url = lambda k: url(lang, base if k == 1 else f"{base}page/{k}/")
    newer = f'<a class="text-link" href="{page_url(n - 1)}">← Newer posts</a>' if n > 1 else "<span></span>"
    older = f'<a class="text-link" href="{page_url(n + 1)}">Older posts →</a>' if n < pages else "<span></span>"
    pager = f'        <nav class="pager" aria-label="Pages">{newer}<span class="count">Page {n} of {pages}</span>{older}</nav>' if pages > 1 else ""
    body = f"""{blog_head(lang, cat)}
      <div class="posts" lang="en">
{chr(10).join(rows)}
{pager}
      </div>"""
    slug = base if n == 1 else f"{base}page/{n}/"
    title = "Blog | Sanapsis" if not cat else f"{label} | Sanapsis Blog"
    if n > 1:
        title = f"Page {n} | " + title
    return slug, page(lang, slug, title, BLOG_DESC[lang], body)


def blog_post(lang, i):
    post = BLOG_POSTS[i]
    slug = f"blog/{post['slug']}/"
    body_html = re.sub(r'SITE/([^"]*)', lambda m: url(lang, m.group(1)), post["body"])
    nav = []
    if i > 0:
        p = BLOG_POSTS[i - 1]
        nav.append(f'<a class="newer" href="{url(lang, "blog/" + p["slug"] + "/")}"><span>Newer post</span>{html.escape(p["title"])}</a>')
    if i < len(BLOG_POSTS) - 1:
        p = BLOG_POSTS[i + 1]
        nav.append(f'<a class="older" href="{url(lang, "blog/" + p["slug"] + "/")}"><span>Older post</span>{html.escape(p["title"])}</a>')
    body = f"""      <article class="pad blog-post" lang="en">
        <p class="back"><a class="text-link" href="{url(lang, 'blog/')}">← Blog</a></p>
        <h1>{html.escape(post['title'])}</h1>
        <p class="meta">{nice_date(post['date'])} · Nana Lehtinen{post_tag(post)}</p>
        <div class="post-body">
{body_html}
        </div>
        <nav class="post-nav" aria-label="More posts">{''.join(nav)}</nav>
      </article>"""
    image = f"blog/{post['lead']}" if post["lead"] else None
    return slug, page(lang, slug, f"{html.escape(post['title'])} | Sanapsis Blog", post["excerpt"], body, image)


def blog_routes():
    """Every blog page: listings (all + per category, paginated) and one page per post."""
    routes = {}
    for cat, label, _ in BLOG_CATS:
        posts = [p for p in BLOG_POSTS if not cat or p["category"] == label]
        pages = max(1, -(-len(posts) // BLOG_PER_PAGE))
        for n in range(1, pages + 1):
            slug = "blog/" + cat + ("" if n == 1 else f"page/{n}/")
            chunk = posts[(n - 1) * BLOG_PER_PAGE:n * BLOG_PER_PAGE]
            routes[slug] = lambda lang, a=(cat, label, chunk, n, pages): blog_list(lang, *a)[1]
    for i, post in enumerate(BLOG_POSTS):
        routes[f"blog/{post['slug']}/"] = lambda lang, i=i: blog_post(lang, i)[1]
    return routes


BLOG_ROUTES = blog_routes()


def blog_slugs():
    return list(BLOG_ROUTES)


def blog_render(lang, slug):
    return BLOG_ROUTES[slug](lang)


# ---------------------------------------------------------------- Privacy

from privacy_texts import PRIVACY_EN, PRIVACY_FI, PRIVACY_SV  # noqa: E402


def privacy(lang):
    content = {"en": PRIVACY_EN, "fi": PRIVACY_FI, "sv": PRIVACY_SV}[lang]
    body = f'      <div class="pad legal">\n{content}\n      </div>'
    return page(lang, "privacy/", "Privacy Notice | Sanapsis", "How Sanapsis handles personal data.", body)


# ---------------------------------------------------------------- 404

def not_found():
    body = """      <div class="pad legal">
<h1 class="page-title">Page not found</h1>
<p>Sorry, this page does not exist. <a href="./">Go to the Sanapsis home page</a>.</p>
      </div>"""
    return page("en", "", "Page not found | Sanapsis", "Page not found.", body)


BUILDERS = {"": home, "pro/": pro, "plus/": plus, "about/": about,
            "support/": support, "privacy/": privacy}


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    text = text.replace("ASSET/../", BASE).replace("ASSET/", BASE + "assets/")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


CHAT_LIVE = False

# The new site's domain. GitHub Pages reads it from docs/CNAME.
DOMAIN = "www.sanapsis.com"
# Off until the DNS switch, so the site can be tested at nanalehtinen.github.io/Sanapsis-website/ (Nana, 18 Oct 2026).
# Set DOMAIN_LIVE = True right before the DNS records are changed.
DOMAIN_LIVE = True

# Old Squarespace addresses -> new pages, so old links and search results keep working (18 Oct 2026).
# The old Finnish and Swedish pages were Sanapsis+ pages. "contact" was the old contact/bug form.
OLD_PAGES_REDIRECT = {
    "home/": "", "sanapsis/": "pro/", "sanapsis-plus/": "plus/",
    "sanapsis-fi/": "fi/plus/", "sanapsis-sv/": "sv/plus/",
    "report-a-bug/": "support/", "contact/": "support/", "privacy-notice/": "privacy/",
}


def redirect_page(old, new):
    """A tiny page at the old address that sends the visitor to the new one."""
    target = "../" * old.count("/") + new
    if PREVIEW:
        target += "index.html"
    full = SITE_URL + new
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Sanapsis</title>
  <meta name="robots" content="noindex">
  <link rel="canonical" href="{full}">
  <meta http-equiv="refresh" content="0; url={target or './'}">
  <script>location.replace({json.dumps(target or './')});</script>
</head>
<body>
  <p>This page has moved: <a href="{target or './'}">{full}</a></p>
</body>
</html>
"""


def redirects():
    pages = dict(OLD_PAGES_REDIRECT)
    for post in BLOG_POSTS:
        old = post["old_url"].strip("/") + "/"
        if old != f"blog/{post['slug']}/":
            pages[old] = f"blog/{post['slug']}/"
    return pages


def main():
    global BASE, CUR_LANG
    for lang in LANGS:
        CUR_LANG = lang
        for slug, build in BUILDERS.items():
            rel = prefix(lang) + slug
            BASE = "../" * rel.count("/")
            write(os.path.join(ROOT, rel, "index.html"), build(lang))
        for slug in blog_slugs():
            rel = prefix(lang) + slug
            BASE = "../" * rel.count("/")
            write(os.path.join(ROOT, rel, "index.html"), blog_render(lang, slug))
    BASE = ""
    write(os.path.join(ROOT, "404.html"), not_found())
    for old, new in redirects().items():
        write(os.path.join(ROOT, old, "index.html"), redirect_page(old, new))
    cname = os.path.join(ROOT, "CNAME")
    if not PREVIEW and DOMAIN_LIVE:
        write(cname, DOMAIN + "\n")
    elif os.path.exists(cname):
        os.remove(cname)
    print("Built", len(LANGS) * (len(BUILDERS) + len(blog_slugs())) + 1, "pages into", ROOT)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Builds the static Sanapsis site into ./docs (served by GitHub Pages).

Run:  python3 build.py
Pages are plain HTML, so the ./docs folder can be served by GitHub Pages or
Cloudflare Pages as is. Texts live in the PAGES dictionaries below.
Text wrapped in ph() is a placeholder that still needs writing.
"""
import html
import os
import sys

from translations import ABOUT, APPROVED, T

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
    if APPROVED:
        return text
    return f'<span class="ph" lang="{lang}">{text}</span>'


def fi_ph(english):
    """Finnish/Swedish text: the draft from translations.py if there is one, else a placeholder."""
    if english in T:
        return draft(html.escape(T[english][LANGS.index(CUR_LANG) - 1], quote=False), CUR_LANG)
    return ph(f"{CUR_LANG.upper()}: {english}")


# Interface words. Finnish entries are placeholders unless the current site has them.
UI = {
    "en": {
        "nav_pro": "Sanapsis Pro", "nav_plus": "Sanapsis+", "nav_support": "Support",
        "nav_blog": "Blog", "nav_about": "About", "menu": "Open menu", "skip": "Skip to content",
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
        "nav_pro": "Sanapsis Pro", "nav_plus": "Sanapsis+", "nav_support": label("Support"),
        "nav_blog": label("Blog"), "nav_about": label("About"), "menu": "Menu", "skip": "Skip to content",
        "f_bug": label("Report a bug"), "f_survey": label("User survey"),
        "f_privacy": privacy_word, "f_contact": label("Contact"),
        "lang_label": lang_word,
    }


# Privacy words come from the current Finnish and Swedish Sanapsis+ pages.
UI["fi"] = ui_placeholders("fi", "Tietosuojaseloste", "Kieli")
UI["sv"] = ui_placeholders("sv", "Integritetspolicy", "Språk")


# All links are relative, so the site works at a domain root or in a subfolder
# (for example a GitHub Pages project address). BASE is set per page while building.
BASE = ""
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
        cur = ' aria-current="page"' if s == slug else ""
        c = f' class="{cls}"' if cls else ""
        nav.append(f'<a href="{url(lang, s)}"{c}{cur}>{label}</a>')
    langs = []
    for l in LANGS:
        cur = ' aria-current="true"' if l == lang else ""
        langs.append(f'<a href="{url(l, slug)}" lang="{l}" hreflang="{l}"{cur}>{l.upper()}</a>')
    return f"""<header class="site-header">
      <a class="logo" href="{url(lang, '')}"><img src="ASSET/img/logo.jpg" alt="Sanapsis" width="160" height="48"></a>
      <button class="menu-toggle" type="button" aria-label="{u['menu']}" aria-expanded="false" aria-controls="main-nav">{MENU_ICON}</button>
      <nav id="main-nav" class="main-nav" aria-label="Main">
        {' '.join(nav)}
        <span class="lang-switch" aria-label="{u['lang_label']}">{''.join(langs)}</span>
      </nav>
    </header>"""


def footer(lang):
    u = UI[lang]
    return f"""<footer class="site-footer">
    <span class="brand">SANAPSIS</span>
    <nav class="footer-nav" aria-label="Footer">
      <a href="{url(lang, 'support/')}#report">{u['f_bug']}</a>
      <a href="{LINKS['survey']}">{u['f_survey']}</a>
      <a href="{url(lang, 'privacy/')}">{u['f_privacy']}</a>
      <a href="{url(lang, 'support/')}#contact">{u['f_contact']}</a>
    </nav>
  </footer>"""


def page(lang, slug, title, description, body):
    alternates = "\n  ".join(
        f'<link rel="alternate" hreflang="{l}" href="{url(l, slug)}">' for l in LANGS)
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{html.escape(description)}">
  {alternates}
  <link rel="icon" href="ASSET/../favicon.ico">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&family=Open+Sans:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="ASSET/css/site.css">
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
            intro="Two separate apps, each supporting a different part of the therapy journey.",
            pro_eyebrow="For speech-language pathologists",
            pro_desc="SanapsisPro is built for professional SLPs. It transforms your iPad into a flexible, open-ended library of therapy ideas and materials.",
            pro_more="Learn more about Sanapsis Pro",
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
            pro_more=fi_ph("Learn more about Sanapsis Pro"),
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

PRO_CATEGORIES_EN = [
    ("Reading", "Tasks from simple word and picture matching to more complex pieces of text."),
    ("Writing", "Copying letters with your fingertips, using the keyboard to fill in sentences, and complex writing tasks using paper and pen."),
    ("Production", "Basic naming (nouns), creating a sentence from given words, and giving instructions."),
    ("Comprehension", "YES/NO questions, following instructions, and questions based on text."),
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
    f = (lambda s: s) if en else fi_ph
    paras = [f(p) for p in paras_en]
    cats = "\n".join(
        f'        <div class="tile"><div class="video-slot">{ph("VIDEO")}</div><h3>{f(n)}</h3><p>{f(d)}</p></div>'
        for n, d in PRO_CATEGORIES_EN)
    body = f"""      <div class="pad"><img class="hero short" src="ASSET/img/pro-hero.jpg" alt="Therapist and client at a table with an iPad"></div>
      <div class="pad app-intro pro">
        <div class="text stack">
          <div class="accent-line pro"></div>
          <div class="eyebrow">{f('For speech-language pathologists')}</div>
          <h1>SanapsisPro</h1>
          <p class="lead">{paras[0]}</p>
          <div class="body-text stack"><p>{paras[1]}</p><p>{paras[2]}</p></div>
          <div class="get-box">
            <div class="title">{f('Get SanapsisPro')}</div>
            <div class="note">{f('iPad. There are no in-app purchases, now or in the future. All updates, including new exercises, are included for free.')}</div>
            <a class="button pro" href="{LINKS['pro_store'][lang]}">{f('Download on the App Store')}</a>
            <a class="text-link pro" href="{LINKS['lite_store']}">{f('Try Sanapsis Lite first')}</a>
          </div>
        </div>
        <div class="shots">
          <img class="shot" src="ASSET/img/pro-screen-1.jpg" alt="SanapsisPro start screen with six categories: Production, Comprehension, Reading, Writing, Semantics, Perseveration" width="1024" height="746">
          <img class="shot" src="ASSET/img/pro-screen-2.jpg" alt="SanapsisPro info panel with welcome text, navigation tips and notes for therapists" width="1024" height="746">
        </div>
      </div>
      <div class="pad"><h2 class="section-title">{f('Six exercise categories')}</h2></div>
      <div class="pad tiles categories">
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
            p2="Med hjälp av Sanapsis+ kan du aktivera och stärka kommunikationsförmågan på ordnivå inom fyra delområden: tal, lyssnande, läsning och skrivning.",
            p3="Förutom övningarna innehåller appen tips och idéer för att öva tal och språk i vardagen – antingen självständigt eller tillsammans med en närstående. Tipsen är kopplade till vardagliga situationer och omgivningar, eftersom där uppstår de viktigaste samtalen och de insikter som bär vidare.",
            get=fi_ph("Get Sanapsis+"),
            get_note="Sanapsis+ är lätt att använda – att komma igång med träningen är bokstavligen bara några klick ifrån!",
            ios="iPad (App Store)", android="Android (Google Play)",
            areas_title=fi_ph("Four core language areas"),
            areas=["Tal", "Lyssnande", "Läsning", "Skrivning"],
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
            note_title="Huomaa",
            note="Voit käyttää Sanapsis+ -sovellusta itsenäisesti, yhdessä läheisen kanssa tai puheterapeutin ohjauksessa. Sanapsis+ ei korvaa puheterapiaa, emmekä voi taata sen yksilöllistä vaikuttavuutta. Mikäli tarvitset neuvoja tai tukea harjoitteluun, suosittelemme ottamaan yhteyttä laillistettuun puheterapeuttiin.",
            shot="ASSET/img/plus-screen-fi.jpg",
            video="544117078", play="Play the Sanapsis+ intro video (Finnish)",
            shot_alt="Sanapsis+ start screen in Finnish with four activities: Kuuntelu, Nimeäminen, Lukeminen, Kirjoittaminen",
        )
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
              <a class="button plus" href="{LINKS['plus_ios'][lang]}">{t['ios']}</a>
              <a class="button plus" href="{LINKS['plus_android']}">{t['android']}</a>
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
        title, hi, button = "About Sanapsis", "Hi there.", "Get in touch"
        paras = paras_en
    else:
        title, hi, button = fi_ph("About Sanapsis"), fi_ph("Hi there."), fi_ph("Get in touch")
        paras = [draft(p.format(clinic=LINKS["clinic"]), lang) for p in ABOUT[lang]]
    ps = "\n".join(f"          <p>{p}</p>" for p in paras)
    body = f"""      <div class="pad page-head"><h1 class="page-title">{title}</h1></div>
      <div class="pad two-col" style="padding-bottom: 48px">
        <div class="main body-text stack-lg">
          <h2 style="font-weight: 600; font-size: 24px">{hi}</h2>
{ps}
        </div>
        <div class="side">
          <img class="about-photo" src="ASSET/img/about.jpg" alt="Two speech-language pathologists at a table">
        </div>
      </div>
      <div class="pad cta-row"><a class="button pro" href="{url(lang, 'support/')}#contact">{button}</a></div>"""
    return page(lang, "about/", "About | Sanapsis", "About Sanapsis and the team behind it.", body)


# ---------------------------------------------------------------- Support

def support(lang):
    en = lang == "en"
    f = (lambda s: s) if en else fi_ph
    faq = "\n".join(
        f'        <details><summary>{ph("QUESTION")}</summary><p>{ph("ANSWER")}</p></details>' for _ in range(3))
    # The form does not send anything yet: the form service depends on the hosting choice.
    body = f"""      <div class="pad page-head"><h1 class="page-title">{f('Support')}</h1></div>
      <div class="pad two-col">
        <form class="main form" id="report" onsubmit="return false">
          <div class="accent-line"></div>
          <h2>{f('Report a bug')}</h2>
          <p class="body-text" style="margin: 0"><strong>{f('Found a bug in SanapsisPro or Sanapsis+?')}</strong> {f('Please let us know using the form below. Include the name of the exercise, a description of the task (what you see on the screen), and details of the bug or issue. The more specific, the better. Screenshots are helpful too!')}</p>
          <label>{f('Name')}<input type="text" name="name" autocomplete="name"></label>
          <label>{f('Email')}<input type="email" name="email" autocomplete="email"></label>
          <label>{f('App')}<select name="app"><option>SanapsisPro</option><option>Sanapsis+</option><option>Sanapsis Lite</option></select></label>
          <label>{f('Message')}<textarea name="message" rows="5"></textarea></label>
          <label>{f('Screenshot (optional)')}<input type="file" name="screenshot" accept="image/*"></label>
          <button class="button" type="submit">{f('Send')}</button>
          <p class="body-text" style="margin: 0">{f("We're always happy to hear suggestions for improvement as well!")}</p>
        </form>
        <div class="side">
          <div class="card" id="contact"><h2>{f('Contact')}</h2><a href="mailto:{LINKS['email']}">{LINKS['email']}</a></div>
          <div class="card"><h2>{f('User survey')}</h2><a href="{LINKS['survey']}">{f('Open the user survey')}</a></div>
          <div class="card"><h2>{f('Privacy')}</h2><a href="{url(lang, 'privacy/')}">{UI[lang]['f_privacy']}</a></div>
        </div>
      </div>
      <div class="faq">
        <h2>{f('Frequently asked questions')}</h2>
{faq}
      </div>"""
    return page(lang, "support/", "Support | Sanapsis", "Report a bug or contact the Sanapsis team.", body)


# ---------------------------------------------------------------- Blog

BLOG_POSTS = [
    ("16 February 2026", "SanapsisPro", "Next up: Synopsis and a fun fact about the name Sanapsis"),
    (None, "SanapsisPro", "Summer season, fresh look"),
    (None, "SanapsisPro", "To the point!"),
    (None, "SanapsisPro", "Let's add some color!"),
]


def blog(lang):
    en = lang == "en"
    f = (lambda s: s) if en else fi_ph
    rows = []
    for date, tag, title in BLOG_POSTS:
        d = date if date else ph("DATE")
        rows.append(f"""        <a class="post" href="#">
          <span class="thumb">{ph('IMAGE')}</span>
          <span class="info">
            <span class="meta">{d} · <span class="tag">{tag}</span></span>
            <span class="title">{title}</span>
            <span class="excerpt">{ph('EXCERPT')}</span>
          </span>
        </a>""")
    posts = "\n".join(rows)
    body = f"""      <div class="pad blog-head">
        <h1 class="page-title">{f('Blog')}</h1>
        <div class="chips">
          <a class="chip active" href="#">{f('All')}</a>
          <a class="chip pro" href="#">SanapsisPro</a>
          <a class="chip plus" href="#">Sanapsis+</a>
        </div>
      </div>
      <div class="posts">
{posts}
        <div class="older"><a class="text-link" href="#">{f('Older posts')}</a></div>
      </div>"""
    return page(lang, "blog/", "Blog | Sanapsis", "News and updates about the Sanapsis apps.", body)


# ---------------------------------------------------------------- Privacy

PRIVACY_EN = """<h1 class="page-title">Privacy Notice</h1>
<p>We are committed to protecting your privacy. This Privacy Notice explains how we handle information collected through our website (www.sanapsis.com) and our iPad applications SanapsisPro and Sanapsis+.</p>
<p>The data controller responsible for your personal data is Puheklinikka Oy (Sanapsis), based in Finland. You can contact us at <a href="mailto:sanapsis@puheklinikka.net">sanapsis@puheklinikka.net</a>.</p>
<h2>Information We Collect</h2>
<p><strong>Website (www.sanapsis.com):</strong></p>
<ul>
<li>Information you voluntarily provide to us (such as name and email address through direct contact, support forms, or surveys).</li>
<li>Cookies to improve functionality and user experience.</li>
<li>No sensitive personal information (e.g., financial or health information) is collected.</li>
</ul>
<p><strong>Applications (SanapsisPro and Sanapsis+):</strong></p>
<ul>
<li>We do not collect, store, or share any personal data through our applications.</li>
<li>Our apps do not access location data, contacts, photos, microphone, or device identifiers.</li>
<li>No registration or login is required to use the applications.</li>
<li>No third-party analytics, advertising services, or tracking tools are used.</li>
</ul>
<h2>How We Use Your Information</h2>
<p>We use the information collected via our website to respond to inquiries and provide customer support, improve our website and services, and to notify you about updates, promotions, or changes to this Privacy Notice (if you have opted in). We do not sell, rent, or share your personal information with third parties, except as necessary to fulfill your requests or comply with legal obligations.</p>
<h2>Legal Basis for Processing (GDPR Compliance)</h2>
<p>If you are located in the European Economic Area (EEA), we process your personal data under the following lawful bases:</p>
<ul>
<li>Your Consent – for communications you initiate with us</li>
<li>Legitimate Interests – to operate, maintain, and improve our services and communications</li>
</ul>
<h2>Data Retention</h2>
<p>We retain user correspondence only for as long as necessary to fulfill the original purpose or to comply with legal obligations.</p>
<p>No app user data is collected or retained.</p>
<h2>Your Rights Under GDPR</h2>
<p>If you are located in the European Economic Area (EEA), you have the following rights regarding your personal data:</p>
<ul>
<li>Right to Access – Request a copy of the data we hold about you.</li>
<li>Right to Rectification – Request that we correct or update your data.</li>
<li>Right to Erasure ("Right to be Forgotten") – Request that we delete your personal data.</li>
<li>Right to Object – Object to how we process your data when we rely on legitimate interests.</li>
<li>Right to Restrict Processing – Request that we limit how we use your data.</li>
<li>Right to Data Portability – Receive your data in a structured, machine-readable format.</li>
<li>Right to Lodge a Complaint – Lodge a complaint with your local Data Protection Authority.</li>
</ul>
<p>To exercise any of these rights, please contact us at <a href="mailto:sanapsis@puheklinikka.net">sanapsis@puheklinikka.net</a>.</p>
<p>If you believe we have infringed your rights under GDPR, you have the right to lodge a complaint with your local Data Protection Authority.</p>
<h2>Your Access to and Control Over Information</h2>
<p>You may opt out of future communications from us at any time by contacting us at <a href="mailto:sanapsis@puheklinikka.net">sanapsis@puheklinikka.net</a>. You can see what data we have about you, (if any), request a correction or update, request deletion of your data, express concerns about our use of your data.</p>
<h2>Security</h2>
<p>We implement appropriate technical and organizational measures to protect your information. Website communications are encrypted using SSL/TLS protocols. Access to any personal information is restricted to employees who need it for customer support. Our servers are maintained in secure facilities. We do not collect sensitive information (such as financial or health data) via our website or applications.</p>
<h2>Cookies</h2>
<p>Our website uses cookies to recognize repeat visitors, save user preferences  and analyze website traffic. Cookies help improve site functionality but are not linked to any personally identifiable information. You can control cookie settings via your browser preferences.</p>
<h2>Third-Party Links</h2>
<p>Our website may contain links to external sites. We are not responsible for the content or privacy practices of these sites. We encourage you to read the privacy policies of any third-party websites you visit.</p>
<h2>Surveys and Contests</h2>
<p>Participation in any surveys or contests on our website is completely voluntary. Information collected (such as name, address, or demographic data) is used solely for administering the survey or contest and notifying winners.</p>
<h2>Changes to This Privacy Notice</h2>
<p>We may update this Privacy Notice as necessary. Significant changes will be posted on this page and, if appropriate, communicated directly to you.</p>
<h2>Contact Us</h2>
<p>If you have any questions, concerns, or requests regarding this Privacy Notice or your personal data, please contact us at:</p>
<p>Email: <a href="mailto:sanapsis@puheklinikka.net">sanapsis@puheklinikka.net</a></p>"""


def privacy(lang):
    if lang == "en":
        content = PRIVACY_EN
    else:
        name = {"fi": "Finnish", "sv": "Swedish"}[lang]
        content = f'<h1 class="page-title">{UI[lang]["f_privacy"]}</h1>\n<p>{fi_ph("Privacy notice in " + name)}</p>'
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
            "support/": support, "blog/": blog, "privacy/": privacy}


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    text = text.replace("ASSET/../", BASE).replace("ASSET/", BASE + "assets/")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    global BASE, CUR_LANG
    for lang in LANGS:
        CUR_LANG = lang
        for slug, build in BUILDERS.items():
            rel = prefix(lang) + slug
            BASE = "../" * rel.count("/")
            write(os.path.join(ROOT, rel, "index.html"), build(lang))
    BASE = ""
    write(os.path.join(ROOT, "404.html"), not_found())
    print("Built", len(LANGS) * len(BUILDERS) + 1, "pages into", ROOT)


if __name__ == "__main__":
    main()

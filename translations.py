"""Draft Finnish and Swedish translations, written by Claude on 4 Oct 2026.

These are drafts for Nana to review. On the pages they stay highlighted in
yellow until they are approved: move an approved text into build.py (or set
APPROVED below) to remove the highlight.

Key: the English text exactly as it appears in build.py.
Swedish follows the Finland-Swedish terms on the current Swedish page
(talterapeut, not logoped).
"""

# Languages whose drafts Nana has approved (no highlight). Nana approved FI and EN on 5 Oct 2026.
APPROVED = {"fi", "en"}

T = {
    # Navigation and footer
    "Support": ("Tuki", "Support"),
    "Blog": ("Blogi", "Blogg"),
    "About": ("Meistä", "Om oss"),
    "Report a bug": ("Ilmoita virheestä", "Rapportera ett fel"),
    "User survey": ("Käyttäjäkysely", "Användarenkät"),
    "Contact": ("Yhteystiedot", "Kontakt"),

    # Home
    "Supporting Speech Therapy with Technology": (
        "Teknologiaa puheterapian tueksi",
        "Teknik som stöd för talterapi"),
    "Two separate apps, each supporting a different part of the therapy journey.": (
        "Kaksi erillistä sovellusta, jotka tukevat kuntoutuksen eri vaiheita.",
        "Två separata appar som stöder olika delar av rehabiliteringen."),
    "For speech-language pathologists": ("Puheterapeuteille", "För talterapeuter"),
    "SanapsisPro is built for professional SLPs. It transforms your iPad into a flexible, open-ended library of therapy ideas and materials.": (
        "SanapsisPro on tehty puheterapeuteille. Se muuttaa iPadisi joustavaksi ja monipuoliseksi terapiaideoiden ja -materiaalien kirjastoksi.",
        "SanapsisPro är gjord för talterapeuter. Den förvandlar din iPad till ett flexibelt och mångsidigt bibliotek med terapiidéer och material."),
    "Learn more about SanapsisPro": ("Lue lisää SanapsisProsta", "Läs mer om SanapsisPro"),
    "For practice at home": ("Harjoitteluun kotona", "För träning hemma"),
    "If you are looking for a solution to work on speech and communication at home, Sanapsis+ is built for you.": (
        "Jos etsit tapaa harjoitella puhetta ja kommunikointia kotona, Sanapsis+ on tehty sinulle.",
        "Om du söker ett sätt att öva tal och kommunikation hemma är Sanapsis+ gjord för dig."),
    "Learn more about Sanapsis+": ("Lue lisää Sanapsis+:sta", "Läs mer om Sanapsis+"),

    # SanapsisPro page
    "SanapsisPro is a rehabilitation app for iPad, designed for professional Speech and Language Pathologists (SLPs) working with adults who have acquired communication difficulties.": (
        "SanapsisPro on iPadille suunniteltu kuntoutussovellus puheterapeuteille, jotka työskentelevät aikuisten kanssa, joilla on hankinnaisia kommunikoinnin vaikeuksia.",
        "SanapsisPro är en rehabiliteringsapp för iPad, utvecklad för talterapeuter som arbetar med vuxna med förvärvade kommunikationssvårigheter."),
    "It offers therapy materials across all core language areas, providing clinicians with structured examples and ideas to support the therapy process. SanapsisPro includes over 35 types of exercises organized into six categories.": (
        "Sovellus tarjoaa terapiamateriaalia kaikille kielen keskeisille osa-alueille sekä jäsenneltyjä esimerkkejä ja ideoita terapiaprosessin tueksi. SanapsisProssa on yli 35 tehtävätyyppiä kuudessa kategoriassa.",
        "Appen erbjuder terapimaterial inom alla centrala språkområden och ger terapeuten strukturerade exempel och idéer som stöd i terapiprocessen. SanapsisPro innehåller över 35 typer av övningar i sex kategorier."),
    "All materials have been specifically developed and tested for adult speech and language therapy. SanapsisPro includes all three languages, English (US), Finnish, and Swedish, in the same download.": (
        "Kaikki materiaalit on kehitetty ja testattu nimenomaan aikuisten puheterapiaan. SanapsisPro sisältää samassa latauksessa kaikki kolme kieltä: englannin (US), suomen ja ruotsin.",
        "Allt material har utvecklats och testats särskilt för talterapi med vuxna. SanapsisPro innehåller alla tre språk, engelska (US), finska och svenska, i samma nedladdning."),
    "Reading": ("Lukeminen", "Läsning"),
    "Tasks from simple word and picture matching to more complex pieces of text.": (
        "Tehtäviä yksinkertaisesta sanan ja kuvan yhdistämisestä vaativampiin teksteihin.",
        "Uppgifter från enkel matchning av ord och bild till mer komplexa texter."),
    "Writing": ("Kirjoittaminen", "Skrivning"),
    "Copying letters with your fingertips, using the keyboard to fill in sentences, and complex writing tasks using paper and pen.": (
        "Kirjainten jäljentämistä sormenpäällä, lauseiden täydentämistä näppäimistöllä sekä vaativampia kirjoitustehtäviä kynällä ja paperilla.",
        "Att kopiera bokstäver med fingertoppen, fylla i meningar med tangentbordet och mer krävande skrivuppgifter med papper och penna."),
    "Production": ("Tuottaminen", "Produktion"),
    "Basic naming (nouns), creating a sentence from given words, and giving instructions.": (
        "Perusnimeämistä (substantiivit), lauseen muodostamista annetuista sanoista ja ohjeiden antamista.",
        "Grundläggande benämning (substantiv), att bilda en mening av givna ord och att ge instruktioner."),
    "Comprehension": ("Ymmärtäminen", "Förståelse"),
    "YES/NO questions, following instructions, and questions based on text.": (
        "KYLLÄ/EI-kysymyksiä, ohjeiden noudattamista ja tekstiin perustuvia kysymyksiä.",
        "JA/NEJ-frågor, att följa instruktioner och frågor utifrån en text."),
    "Semantics": ("Semantiikka", "Semantik"),
    'Exercises such as "Is this simile true", which works especially well with high-level TBI patients.': (
        "Tehtäviä, kuten ”Pitääkö vertaus paikkansa”, joka toimii erityisen hyvin lievästi aivovammautuneiden kanssa.",
        "Övningar som ”Stämmer liknelsen”, som fungerar särskilt bra med patienter med lindrig hjärnskada."),
    "Perseveration": ("Perseveraatio", "Perseveration"),
    'Material to work with those who tend to "get stuck" in their speech or even comprehension.': (
        "Materiaalia niille, joiden puhe tai ymmärtäminen pyrkii ”juuttumaan”.",
        "Material för dem som tenderar att ”fastna” i sitt tal eller till och med i sin förståelse."),
    "Get SanapsisPro": ("Hanki SanapsisPro", "Skaffa SanapsisPro"),
    "iPad. There are no in-app purchases, now or in the future. All updates, including new exercises, are included for free.": (
        "iPad. Sovelluksessa ei ole sovelluksen sisäisiä ostoja, ei nyt eikä tulevaisuudessa. Kaikki päivitykset, myös uudet tehtävät, sisältyvät hintaan.",
        "iPad. Appen har inga köp i appen, varken nu eller i framtiden. Alla uppdateringar, även nya övningar, ingår utan extra kostnad."),
    "Download on the App Store": ("Lataa App Storesta", "Ladda ner från App Store"),
    "Try SanapsisLite first": ("Kokeile ensin SanapsisLitea", "Prova SanapsisLite först"),
    "Six exercise categories": ("Kuusi tehtäväkategoriaa", "Sex övningskategorier"),
    "Important information": ("Tärkeää tietoa", "Viktig information"),
    "Sanapsis is intended for use in therapy sessions under the guidance of a licensed Speech-Language Pathologist (SLP). It is not designed for independent use.": (
        "Sanapsis on tarkoitettu käytettäväksi terapiaistunnoissa laillistetun puheterapeutin ohjauksessa. Sitä ei ole suunniteltu itsenäiseen käyttöön.",
        "Sanapsis är avsedd att användas under terapisessioner med handledning av en legitimerad talterapeut. Den är inte utformad för självständig användning."),

    # Sanapsis+ page
    "Get Sanapsis+": ("Hanki Sanapsis+", "Skaffa Sanapsis+"),
    "Four core language areas": ("Neljä kielen osa-aluetta", "Fyra språkområden"),
    "Everyday vocabulary": ("Arjen sanastoa", "Vardagsord"),
    "Please note": ("Huomaa", "Observera"),

    # About page
    "About Sanapsis": ("Tietoa Sanapsiksesta", "Om Sanapsis"),
    "Hi there.": ("Hei!", "Hej!"),
    "Get in touch": ("Ota yhteyttä", "Kontakta oss"),

    # Support page
    "Found a bug in SanapsisPro or Sanapsis+?": (
        "Löysitkö virheen SanapsisProsta tai Sanapsis+:sta?",
        "Har du hittat ett fel i SanapsisPro eller Sanapsis+?"),
    "Please let us know using the form below. Include the name of the exercise, a description of the task (what you see on the screen), and details of the bug or issue. The more specific, the better. Screenshots are helpful too!": (
        "Kerro siitä meille alla olevalla lomakkeella. Mainitse tehtävän nimi, kuvaus tehtävästä (mitä näet näytöllä) ja tiedot virheestä tai ongelmasta. Mitä tarkemmin, sitä parempi. Myös kuvakaappaukset auttavat!",
        "Berätta för oss via formuläret nedan. Ange övningens namn, en beskrivning av uppgiften (vad du ser på skärmen) och detaljer om felet eller problemet. Ju mer specifikt, desto bättre. Skärmbilder hjälper också!"),
    "Name": ("Nimi", "Namn"),
    "Email": ("Sähköposti", "E-post"),
    "App": ("Sovellus", "App"),
    "Message": ("Viesti", "Meddelande"),
    "Screenshot (optional)": ("Kuvakaappaus (vapaaehtoinen)", "Skärmbild (valfritt)"),
    "Send": ("Lähetä", "Skicka"),
    "We're always happy to hear suggestions for improvement as well!": (
        "Otamme mielellämme vastaan myös kehitysehdotuksia!",
        "Vi tar också gärna emot förbättringsförslag!"),
    "Open the user survey": ("Avaa käyttäjäkysely", "Öppna användarenkäten"),
    "Privacy": ("Tietosuoja", "Integritet"),
    "Frequently asked questions": ("Usein kysyttyä", "Vanliga frågor"),

    # Blog page
    "All": ("Kaikki", "Alla"),
    "Older posts": ("Vanhemmat kirjoitukset", "Äldre inlägg"),
}

# About page paragraphs (HTML allowed). Same order as the English paragraphs.
ABOUT = {
    "fi": [
        "Olen Nana, hauska tutustua! Olen puheterapeutti, ja työskentelen erityisen mielelläni aikuisten kanssa, joilla on hankinnaisia kielen ja kommunikoinnin vaikeuksia. Olen myös Sanapsis-sovellusten pääsuunnittelija.",
        'Aloitimme <strong>Sanapsiksen</strong> kehittämisen jo vuonna 2009. Yksityisvastaanottomme <a href="{clinic}">Puheklinikka Oy</a> on erikoistunut aikuisten neurologiseen puheterapiaan. Sanapsis syntyi alun perin omaksi työkaluksemme. Halusimme nopean pääsyn laadukkaaseen, arkielämää kuvaavaan materiaaliin, joka heijastaa asiakkaidemme omaa arkiympäristöä. Yhtä tärkeää oli, että työkalu mahdollistaa joustavan tavoitteiden asettamisen ja tukee merkityksellistä vuorovaikutusta terapeutin ja asiakkaan välillä.',
        "Monen (todella monen!) kokeilun jälkeen <strong>SanapsisPro</strong> alkoi muistuttaa sitä, mitä olimme kuvitelleet.",
        "Suuri kiitos kuuluu upeille asiakkaillemme, jotka ovat olleet tiiviisti mukana sovelluksen suunnittelussa ja testauksessa. Näet osan heidän kasvoistaan myös materiaaleissa; he ovat todella osa Sanapsiksen tarinaa.",
        "Alkuvuodesta 2021 julkaisimme kysynnän vuoksi <strong>Sanapsis+</strong>-sovelluksen itsenäiseen harjoitteluun kotona.",
        "Kuulemme mielellämme kollegoilta. Jos haluat kokeilla Sanapsis+:aa asiakkaidesi kanssa, ota yhteyttä.",
    ],
    "sv": [
        "Jag heter Nana, trevligt att träffas! Jag är talterapeut och arbetar helst med vuxna som har förvärvade språk- och kommunikationssvårigheter. Jag är också huvuddesigner för Sanapsis-apparna.",
        'Vi började utveckla <strong>Sanapsis</strong> redan 2009. Vår privatpraktik <a href="{clinic}">Puheklinikka Oy</a> är specialiserad på neurologisk talterapi för vuxna. Från början skapades Sanapsis som ett internt verktyg. Vi ville ha snabb tillgång till högkvalitativt, vardagsnära material som speglar våra patienters egen vardagsmiljö. Lika viktigt var ett verktyg som ger utrymme för flexibla mål och stöder ett meningsfullt samspel mellan terapeut och patient.',
        "Efter mycket (och vi menar mycket!) prövande och omprövande började <strong>SanapsisPro</strong> likna det vi hade föreställt oss.",
        "Ett stort tack går till våra fantastiska patienter, som har varit djupt involverade i att utforma och testa appen. Du ser till och med några av deras ansikten i materialet; de är verkligen en del av Sanapsis historia.",
        "I början av 2021 lanserade vi <strong>Sanapsis+</strong> på allmän begäran, för självständig träning hemma.",
        "Vi hör gärna av kollegor. Om du vill prova Sanapsis+ med dina patienter, hör av dig.",
    ],
}


# Finnish texts written or approved by Nana (5 Oct 2026). These are shown without
# highlight and win over the drafts in T. Key: the English text in build.py.
NANA_FI = {
    # SanapsisPro page
    "Get SanapsisPro": "Hanki SanapsisPro",
    "iPad. There are no in-app purchases, now or in the future. All updates, including new exercises, are included for free.":
        "Sanapsis on kertahankinta. Sovelluksessa ei ole sovelluksen sisäisiä ostoja, ei nyt eikä tulevaisuudessa. Kaikki päivitykset, myös uudet tehtävät, ovat maksuttomia.",
    "Try SanapsisLite first": "Kokeile SanapsisLite sovellusta",
    'Exercises such as "Is this simile true", which works especially well with high-level TBI patients.':
        "Tehtäviä, kuten ”Pitääkö vertaus paikkansa”",
    "Important information": "Huomaathan!",
    "Sanapsis is intended for use in therapy sessions under the guidance of a licensed Speech-Language Pathologist (SLP). It is not designed for independent use.":
        "SanapsisPro on tarkoitettu käytettäväksi terapiassa laillistetun puheterapeutin ohjauksessa. Sitä ei ole suunniteltu itsenäiseen käyttöön. Jos etsit tukea omatoimiseen harjoitteluun, tutustu Sanapsis+ sovellukseen.",
    # Home page
    "Supporting Speech Therapy with Technology": "Teknologia puheterapian tukena",
    "Two separate apps, each supporting a different part of the therapy journey.":
        "Sanapsis-perheeseen kuuluu kaksi erillistä sovellusta, jotka tukevat puheterapeuttista harjoittelua eri tavoilla.",
    "Learn more about SanapsisPro": "Lue lisää sovelluksesta SanapsisPro",
    "Learn more about Sanapsis+": "Lue lisää sovelluksesta Sanapsis+",
    # Support page
    "Report a bug": "Ilmoita virheestä",
    "Please let us know using the form below. Include the name of the exercise, a description of the task (what you see on the screen), and details of the bug or issue. The more specific, the better. Screenshots are helpful too!":
        "Kerro siitä meille alla olevalla lomakkeella niin korjaamme virheen mitä pikimmin. Mainitse tehtävän nimi ja kuvaus (mitä näet näytöllä) ja tiedot virheestä tai ongelmasta. Mitä tarkemmin, sitä parempi. Myös kuvakaappaukset auttavat. Kiitos avusta!",
    "Found a bug in SanapsisPro or Sanapsis+?": "Löysitkö virheen SanapsisProsta tai Sanapsis+:sta?",
    "Screenshot (optional)": "Kuvakaappaus (ei pakollinen)",
    "We're always happy to hear suggestions for improvement as well!": "Otamme aina mielellämme vastaan kehitysehdotuksia!",
    # Sanapsis+ page
    "Four core language areas": "Neljä tehtävätyyppiä",
    "Please note": "Huomaathan!",
    # About page
    "About Sanapsis": "Tietoa meistä",
    "Hi there.": "Hei!",
}

# Footer link (Nana: "Ilmoita virheestä -> raportoi bugi").
NANA_FI_FOOTER_BUG = "Raportoi bugi"

NANA_FI_PRO = [
    "SanapsisPro on puheterapeuteille suunniteltu sovellus, joka tarjoaa tukea aikuisneurologisen puheterapian suunnitteluun ja toteuttamiseen. SanapsisPro sisältää laajan valikoiman harjoituksia, ideoita terapian suunnitteluun sekä materiaalia harjoituksen läpiviemiseen asiakkaan kanssa. SanapsisPron harjoitukset on ryhmitelty kuuteen tehtäväkategoriaan ja sovellus sisältää yhteensä yli 35 tehtävätyyppiä. Kaikki materiaalit on käytettävissä kolmella kielellä: suomi, ruotsi ja englanti (US).",
    "Voit tutustua SanapsisPron ideaan lataamalla SanapsisLite sovelluksen, joka tarjoaa esimerkkejä harjoituksista kolmella kielellä.",
]

NANA_FI_PLUS = dict(
    lead="Sanapsis+ on suunniteltu henkilöille, joilla on puheen ja kommunikoinnin haasteita neurologisista syistä johtuen. Näitä voivat olla esimerkiksi afasia, aivoverenkiertohäiriö (AVH), aivovamma tai etenevät neurologiset sairaudet.",
    p2="Sanapsis+ -sovelluksen avulla voit aktivoida ja vahvistaa sanatasoista kommunikointia neljällä osa-alueella: puhuminen, kuuntelu, lukeminen ja kirjoittaminen.",
    p3="Tehtävien lisäksi sovellus tarjoaa ideoita ja neuvoja puheen ja kielen harjoitteluun arjessa itsenäisesti tai yhdessä läheisen kanssa. Vinkit liittyvät tavallisiin tilanteisiin ja ympäristön hyödyntämiseen, sillä arjessa tapahtuvat yhteiset oivallukset kantavat kauas!",
    get_note="Sanapsis+ on helppokäyttöinen, ja harjoittelun aloittaminen on vain muutaman napautuksen päässä!",
    vocab="Kaikki Sanapsis+ sovelluksen tehtävät pohjautuvat tuttuihin arjen sanoihin. Voit valita harjoituskategoriaksi: koti, esineet, ruoka ja juoma, vaatteet, ympäristö, matkustaminen, vapaa-aika ja verbit. Harjoitukset ja materiaalit on käytettävissä kolmella kielellä: suomi, ruotsi ja englanti.",
)

# About page, Finnish (HTML allowed; {clinic} is the Puheklinikka link).
NANA_FI_ABOUT = [
    "Olen Nana, aikuisten puheterapiasta erityisen innostunut puheterapeutti sekä Sanapsis-sovellusten pääsuunnittelija ja kehittäjä. Onpa kiva tutustua!",
    'Olen työskennellyt aikuisneurologisten asiakkaiden kanssa vuodesta 2004. Idea Sanapsiksesta nousi alunperin suorasta terapiatyötarpeesta. Ensimmäinen Sanapsis-sovellus syntyi aikuisneurologiseen puheterapiaan erikoistuneen yrityksemme, <a href="{clinic}">Puheklinikan</a>, omaksi työkaluksi. Kaipasimme terapiatyön tueksi työvälinettä, joka helpottaa terapian suunnittelua ja toteutusta tarjoamalla monipuolisia ideoita ja työskentelymahdollisuuksia sekä nopean pääsyn materiaaliin, joka heijastaa asiakkaidemme omaa arkea ja elinympäristöä. Yhtä tärkeää meille oli, että sovellus mahdollistaa tavoitteiden joustavan asettamisen ja tukee merkityksellistä vuorovaikutusta terapeutin ja asiakkaan välillä.',
    "Monien kokeilujen ja kehitysvaiheiden myötä <strong>SanapsisPro</strong> alkoi vähitellen muistuttaa sitä työkalua, jota olimme tavoitelleet. Käsissämme oli selkeä ja monipuolinen tuki joustavaan ja vuorovaikutteiseen terapiatyöhön. Lisäsimme mukaan yksityiskohtaiset ohjeet ja runsaasti ideoita erilaisista tavoista hyödyntää sovelluksen tehtäviä. Sitten olikin mahdollista jakaa meille tärkeä työkalu kollegoille! SanapsisPron ensimmäinen versio julkaistiin App Storessa vuonna 2012. Vuonna 2021 julkaisimme SanapsisPron rinnalle kuntoutujien omatoimiseen harjoitteluun suunnitellun sovelluksen, <strong>Sanapsis+</strong>.",
    "Suuri osa Sanapsis-perheen sovellusten kehitystyöstä on toteutunut yhteistyössä upeiden asiakkaidemme kanssa. Jos olet tarkkana, saatat jopa löytää materiaaleista muutamia Puheklinikalta tuttuja kasvoja. Se jos mikä on tae siitä, että materiaalit on suunniteltu, kehitetty ja testattu nimenomaan elämänmakuiseen ja aktiiviseen puheterapiakäyttöön!",
    "Sanapsis-perheen sovellusten kehitystyö jatkuu edelleen, ja kuulemme aina mielellämme ideoita, käyttökokemuksia ja kehitysehdotuksia. Voit lähettää meille risuja, ruusuja ja muitakin kuulumisia alla olevan painikkeen kautta.",
    'Jos haluat lukea lisää ajatuksiani aikuisten puheterapiasta ja erityisesti teknologian roolista puheterapiassa, käy kurkkaamassa blogiani <a href="{blog}">All The Things I Love About Speech Therapy With Adults</a> (luettavissa vain englanniksi).',
    "Jos olet puheterapeutti ja haluat kokeilla Sanapsis+-sovellusta asiakkaidesi kanssa, ota yhteyttä, niin järjestämme sinulle mahdollisuuden ladata sovellus maksutta.",
]


# English drafts by Claude (5 Oct 2026), rewritten from Nana's Finnish texts.
# Shown highlighted on the English site until Nana approves them.
# Key: the current English text in build.py; value: the new draft.
EN_DRAFT = {
    "Two separate apps, each supporting a different part of the therapy journey.":
        "The Sanapsis family includes two separate apps, each supporting speech therapy practice in its own way.",
    "iPad. There are no in-app purchases, now or in the future. All updates, including new exercises, are included for free.":
        "SanapsisPro for iPad is a one-time purchase. There are no in-app purchases, now or in the future, and all updates, including new exercises, are free.",
    'Exercises such as "Is this simile true", which works especially well with high-level TBI patients.':
        "Exercises such as “Is this simile true?”",
    "Important information": "Please note",
    "Sanapsis is intended for use in therapy sessions under the guidance of a licensed Speech-Language Pathologist (SLP). It is not designed for independent use.":
        "SanapsisPro is intended for use in therapy under the guidance of a licensed speech-language pathologist (SLP). It is not designed for independent use. If you are looking for support for practicing on your own, take a look at Sanapsis+.",
    "Please let us know using the form below. Include the name of the exercise, a description of the task (what you see on the screen), and details of the bug or issue. The more specific, the better. Screenshots are helpful too!":
        "Please let us know using the form below, and we’ll fix it as quickly as we can. Include the name of the exercise, a description of the task (what you see on the screen), and details of the bug or issue. The more specific, the better, and screenshots help too. Thank you for your help!",
}

class NANA(str):
    """Text written by Nana: shown without highlight."""


# Blog name (Nana, 5 Oct 2026), shown under the Blog heading.
BLOG_NAME = "All The Things I Love About Speech Therapy With Adults"

# Sanapsis+ second paragraph, English, written by Nana (5 Oct 2026).
NANA_EN_PLUS_P2 = "With Sanapsis+, you can strengthen word-level communication in four areas: speaking, listening, reading, and writing."

EN_DRAFT_PRO = [
    "SanapsisPro is designed for speech-language pathologists. It supports you in planning and delivering adult neurological speech therapy, with a wide range of exercises, ideas for planning sessions, and materials for working through the exercises with your client. Over 35 exercise types are grouped into six categories, and all materials are available in three languages: English (US), Finnish, and Swedish.",
    "To get a feel for how SanapsisPro works, download SanapsisLite, which includes sample exercises in all three languages.",
]

EN_DRAFT_PLUS = dict(
    lead="Sanapsis+ is designed for people with speech and communication difficulties due to neurological conditions, such as aphasia, stroke, traumatic brain injury, or progressive neurological diseases.",
        p3="Alongside the exercises, the app offers ideas and tips for practicing speech and language in everyday life, on your own or with a loved one. The tips draw on ordinary situations and your surroundings, because small breakthroughs in daily life go a long way!",
    get_note="Sanapsis+ is easy to use, and you can start practicing in just a few taps!",
    areas_title="Four exercise types",
    vocab="All Sanapsis+ exercises are built around familiar, everyday words. You can choose from these categories: Home, Objects, Food and Drink, Clothes, Surroundings, Travel, Recreation, and Verbs. All exercises and materials are available in English, Finnish, and Swedish.",
    note="You can use Sanapsis+ on your own, with a loved one, or with the guidance of a speech-language pathologist. Sanapsis+ does not replace speech therapy, and we cannot guarantee how well it will work for each individual. If you need advice or support with your practice, we recommend contacting a licensed speech-language pathologist.",
)

EN_DRAFT_ABOUT = [
    "I’m Nana, lovely to meet you! I’m a speech-language pathologist with a special passion for working with adults, and the lead designer and developer of the Sanapsis apps.",
    'I’ve worked with adults with neurological conditions since 2004. The idea for Sanapsis came straight out of everyday therapy work: the first Sanapsis app was built as an in-house tool for <a href="{clinic}">Puheklinikka</a>, our practice specializing in adult neurological speech therapy. We wanted a tool that would make planning and delivering therapy easier, with plenty of ideas and ways of working, and quick access to materials that reflect our clients’ own daily lives and surroundings. Just as importantly, it had to allow flexible goal setting and support meaningful interaction between therapist and client.',
    "After many rounds of testing and development, <strong>SanapsisPro</strong> gradually became the tool we had been aiming for: clear, versatile support for flexible, interactive therapy. We added detailed instructions and lots of ideas for different ways to use the exercises, and then it was ready to share with colleagues. The first version of SanapsisPro was released on the App Store in 2012. In 2021, we added <strong>Sanapsis+</strong> to the family, an app designed for clients to practice independently.",
    "Much of the development of the Sanapsis apps has been done together with our wonderful clients. If you look closely, you may even spot a few familiar faces from Puheklinikka in the materials. That’s the best proof we can offer that the materials were designed, developed, and tested for real-life, active speech therapy!",
    "The work to develop the Sanapsis apps is very much ongoing and we love to hear your ideas, experiences, and suggestions. Send us your feedback, good or bad, using the button below. We also love a note just saying Hi!",
    NANA('Want to know more about our approach to adult speech therapy and the future of technology in rehabilitation? Head over to our blog <a href="{blog}">All The Things I Love About Speech Therapy With Adults</a>.'),
    "If you’re a speech-language pathologist and would like to try Sanapsis+ with your clients, get in touch and we’ll arrange a free download for you. Looking forward to hearing from you!",
]

"""Draft Finnish and Swedish translations, written by Claude on 4 Oct 2026.

These are drafts for Nana to review. On the pages they stay highlighted in
yellow until they are approved: move an approved text into build.py (or set
APPROVED below) to remove the highlight.

Key: the English text exactly as it appears in build.py.
Swedish follows the Finland-Swedish terms on the current Swedish page
(talterapeut, not logoped).
"""

APPROVED = False  # True removes the yellow highlight from every draft

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
    "Learn more about Sanapsis Pro": ("Lue lisää SanapsisProsta", "Läs mer om SanapsisPro"),
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
    "Try Sanapsis Lite first": ("Kokeile ensin Sanapsis Liteä", "Prova Sanapsis Lite först"),
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

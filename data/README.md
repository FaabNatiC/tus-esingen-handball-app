# Datenpflege – Anleitung für Redakteure

> 📝 **Diese Anleitung richtet sich an alle, die Spielergebnisse, News und Termine in der TuS Esingen Handball-App pflegen.**
>
> Du brauchst keine Programmierkenntnisse, nur einen Browser und Zugriff auf das GitHub-Repository. Die wichtigsten Schritte sind unten erklärt.
>
> Für technische App-Themen und PWA-Setup siehe [`../README.md`](../README.md).

---

## Was du hier findest

Diese Anleitung zeigt dir:

- **Welche Dateien es gibt** und wofür sie da sind
- **Wie du Spielergebnisse einträgst** (das machst du am häufigsten)
- **Was du am Saisonstart tun musst**
- **Wie du mit Sonderfällen umgehst** – Verlegungen, Wertungen, Korrekturen
- **Wie GitHub für Anfänger funktioniert** – falls du dich noch nicht auskennst

Wenn du nur schnell ein Spielergebnis nachtragen willst, springe direkt zum Kapitel [„Wöchentlich: Spielergebnisse eintragen"](#wöchentlich-spielergebnisse-eintragen).

---

## Inhaltsverzeichnis

**Grundlagen**
- [Wie die Daten aufgebaut sind](#wie-die-daten-aufgebaut-sind)
- [Wie Saisons organisiert sind](#wie-saisons-organisiert-sind)
- [Wo finde ich was?](#wo-finde-ich-was)
- [Wie wird die Tabelle berechnet?](#wie-wird-die-tabelle-berechnet)

**Datei-Referenz**
- [Die Stammdaten-Dateien](#die-stammdaten-dateien-im-detail) – `meta/teams.json`, `info.json`, `kader.json`, `training.json`
- [Die Inhaltsdateien](#die-inhaltsdateien-im-detail) – `news.json`, `partners.json`, `partner.json`
- [Die Spielbetrieb-Dateien](#die-spielbetrieb-dateien-im-detail) – `saisons/<saison>/meta.json`, `spieltage/XX-kwNN.json`, `pokalspiele.json`, `testspiele.json`

**Pflege-Workflows**
- [Wöchentlich: Spielergebnisse eintragen](#wöchentlich-spielergebnisse-eintragen)
- [Spielverlegung eintragen](#spielverlegung-eintragen)
- [Wertung wegen Nicht-Antreten](#wertung-wegen-nicht-antreten)
- [Tippfehler korrigieren](#tippfehler-korrigieren)
- [Saisonstart: Neue Saison anlegen](#saisonstart-neue-saison-anlegen)
- [Saisonende: Was passiert mit alten Daten?](#saisonende-was-passiert-mit-alten-daten)
- [Neue Mannschaft zur App hinzufügen](#neue-mannschaft-zur-app-hinzufügen)
- [Neuen Sponsor hinzufügen](#neuen-sponsor-hinzufügen)
- [News-Beitrag veröffentlichen](#news-beitrag-veröffentlichen)
- [Was du **nicht** pflegen musst](#was-du-nicht-pflegen-musst)

**GitHub-Crashkurs für Pfleger**
- [Was ist GitHub eigentlich?](#was-ist-github-eigentlich)
- [Vorbereitung](#vorbereitung)
- [Die wichtigsten Vorgänge](#die-wichtigsten-vorgänge)
- [JSON richtig schreiben](#json-richtig-schreiben)
- [Häufige Fehler und ihre Bedeutung](#häufige-fehler-und-ihre-bedeutung)
- [Wie sehe ich, dass mein Commit live ist?](#wie-sehe-ich-dass-mein-commit-live-ist)
- [Konflikte: Wenn zwei Pfleger gleichzeitig editieren](#konflikte-wenn-zwei-pfleger-gleichzeitig-editieren)
- [Was tun, wenn was schiefgeht?](#was-tun-wenn-was-schiefgeht)
- [Weiterführende Links](#weiterführende-links)

**Letzte Hinweise**
- [Wer hat Zugriff auf was?](#wer-hat-zugriff-auf-was)
- [Wo bekomme ich Hilfe?](#wo-bekomme-ich-hilfe)
- [Vorschläge zur Anleitung](#vorschläge-zur-anleitung)

---

## Wie die Daten aufgebaut sind

Alle Inhalte der App liegen im Ordner `data/` im Repository. So ist das aufgeteilt:

```
data/
├── README.md                      ← diese Anleitung
│
├── meta/
│   └── teams.json                 ← Liste aller TuS-Mannschaften
│                                    (Reihenfolge in der App)
│
├── content/
│   ├── news.json                  ← News-Beiträge auf der Startseite
│   └── partners.json              ← Hauptsponsoren (oben rechts in der App)
│
├── teams/
│   ├── 1-herren/                  ← ein Ordner pro Mannschaft
│   │   ├── info.json              ← Stammdaten + aktuelle Saison
│   │   ├── kader.json             ← Spieler und Trainer
│   │   ├── training.json          ← Trainingszeiten
│   │   ├── partner.json           ← Mannschaftssponsoren
│   │   └── saisons/
│   │       ├── 2025-26/           ← ein Ordner pro Saison
│   │       │   ├── meta.json      ← Liga-Info, Mannschaftsliste
│   │       │   ├── spieltage/
│   │       │   │   ├── 01-kw37.json  ← Spieltag 1 (gespielt in KW 37/2025)
│   │       │   │   ├── 02-kw38.json  ← Spieltag 2 (KW 38/2025)
│   │       │   │   └── ...
│   │       │   ├── pokalspiele.json ← alle Pokalspiele dieser Saison
│   │       │   └── testspiele.json  ← alle Testspiele dieser Saison
│   │       └── 2026-27/           ← nächste Saison (sobald angelegt)
│   │           └── ...
│   ├── 1-damen/
│   │   └── (gleiche Struktur wie 1-herren)
│   ├── md1-jugend/
│   │   └── (gleiche Struktur)
│   └── md2-jugend/
│       └── (gleiche Struktur)
│
├── logos-mannschaften/            ← Vereinslogos der Gegner
│   ├── tus-esingen.png
│   ├── ahrensburg.png
│   └── ...
│
├── logos-sponsoren/               ← Logos der Sponsoren
│   ├── stadtwerke.jpg
│   ├── schmidt.png
│   └── ...
│
└── archive/                       ← alte Saisons (optional)
    └── ...
```

### Die drei wichtigsten Bereiche

**`meta/` – Stammdaten der App**
Hier liegt eine zentrale Liste aller TuS-Mannschaften. Wenn eine neue Mannschaft dazukommt, wird sie hier eingetragen.

**`content/` – Allgemeine Inhalte**
News und Hauptsponsoren – also alles, was nicht zu einer einzelnen Mannschaft gehört.

**`teams/` – Alle Mannschaften**
Jede Mannschaft hat ihren eigenen Ordner. Darin liegen alle Daten zu dieser Mannschaft: Kader, Trainingszeiten, Mannschaftssponsoren und – pro Saison getrennt – alle Spiele.

---

## Wie Saisons organisiert sind

Innerhalb jeder Mannschaft sind die Spielergebnisse **nach Saison getrennt** abgelegt. So bleibt alles übersichtlich, auch wenn eine Mannschaft die Liga wechselt oder neue Gegner bekommt.

```
teams/1-herren/saisons/
├── 2025-26/                   ← Saison 2025/26
│   ├── meta.json              ← Liga-Info dieser Saison
│   ├── spieltage/             ← Liga-Spiele
│   │   ├── 01-kw37.json       ← Spieltag 1, gespielt in KW 37/2025
│   │   ├── 02-kw38.json
│   │   └── ...
│   ├── pokalspiele.json       ← Pokalspiele dieser Saison
│   └── testspiele.json        ← Testspiele dieser Saison
└── 2026-27/                   ← Saison 2026/27
    └── ...
```

**Wichtig:** In der App wird immer nur eine Saison angezeigt – die „aktuelle Saison". Welche das ist, steht in der `info.json` der Mannschaft. Du kannst eine neue Saison schon vorbereiten, ohne dass sie sofort live geht.

---

## Wo finde ich was?

| Du willst… | Datei |
|---|---|
| ein Liga-Spielergebnis eintragen | `teams/<mannschaft>/saisons/<saison>/spieltage/<XX-kwNN>.json` |
| ein Pokalspiel eintragen | `teams/<mannschaft>/saisons/<saison>/pokalspiele.json` |
| ein Testspiel eintragen | `teams/<mannschaft>/saisons/<saison>/testspiele.json` |
| eine News veröffentlichen | `content/news.json` |
| einen neuen Spieler im Kader ergänzen | `teams/<mannschaft>/kader.json` |
| Trainingszeiten ändern | `teams/<mannschaft>/training.json` |
| einen Mannschaftssponsor hinzufügen | `teams/<mannschaft>/partner.json` |
| eine Liga zur nächsten Saison anlegen | `teams/<mannschaft>/saisons/<neue-saison>/meta.json` |
| die aktuelle Saison einer Mannschaft umschalten | `teams/<mannschaft>/info.json` |
| eine neue Mannschaft zur App hinzufügen | `meta/teams.json` (plus neuer Ordner unter `teams/`) |

---

## Wie wird die Tabelle berechnet?

Die Liga-Tabelle wird **nicht von Hand gepflegt**. Stattdessen berechnet die App sie automatisch aus den Spielergebnissen aller Spieltage einer Saison.

Das heißt: Sobald du ein Ergebnis korrigierst, ändert sich die Tabelle automatisch mit. Du musst nie eine Tabelle separat anpassen.

Das funktioniert nur, wenn **alle Spiele eines Spieltags** (nicht nur die TuS-Spiele) eingetragen sind. Mehr dazu im Kapitel zur wöchentlichen Pflege.

---

# Die Stammdaten-Dateien im Detail

Dieses Kapitel beschreibt die vier Dateien, die selten verändert werden – meistens nur einmal pro Saison oder wenn sich Spieler/Trainer wechseln.

## `meta/teams.json` – Die Liste aller Mannschaften

Diese Datei kennt alle TuS-Mannschaften, die in der App angezeigt werden, und legt deren Reihenfolge fest.

### Beispiel

```json
{
  "aktualisiert": "10.05.2026",
  "teams": [
    {
      "id": "1-herren",
      "name": "1. Herren",
      "kurzname": "1. H",
      "reihenfolge": 1
    },
    {
      "id": "1-damen",
      "name": "1. Damen",
      "kurzname": "1. D",
      "reihenfolge": 2
    },
    {
      "id": "md1-jugend",
      "name": "männlich D1",
      "kurzname": "mD1",
      "reihenfolge": 3
    },
    {
      "id": "md2-jugend",
      "name": "männlich D2",
      "kurzname": "mD2",
      "reihenfolge": 4
    }
  ]
}
```

### Felder

| Feld | Pflicht | Beschreibung |
|---|---|---|
| `aktualisiert` | ja | Datum der letzten Änderung (Format: `DD.MM.YYYY`) |
| `teams` | ja | Liste aller Mannschaften |

**Pro Mannschaft:**

| Feld | Pflicht | Beschreibung |
|---|---|---|
| `id` | ja | Ordnername unter `teams/` (kleinschreibung, mit Bindestrich) |
| `name` | ja | Vollständiger Anzeigename in der App |
| `kurzname` | nein | Kurze Variante für engere Stellen (z.B. Bottom-Nav) |
| `reihenfolge` | ja | Sortierung in der App (1 = erste, dann 2, 3 ...) |

### Wann du diese Datei änderst

- **Neue Mannschaft kommt dazu:** Neuen Eintrag hinzufügen + Ordner unter `teams/` anlegen
- **Mannschaft heißt anders:** `name` und/oder `kurzname` ändern
- **Reihenfolge in der App soll anders sein:** `reihenfolge`-Werte anpassen

### Stolperfallen

- Die `id` muss **exakt** dem Ordnernamen unter `teams/` entsprechen, sonst findet die App die Mannschaft nicht
- `reihenfolge`-Werte sollten eindeutig sein (nicht zweimal `1`)
- Nach dem Speichern: Vergiss nicht, das `aktualisiert`-Datum zu ändern

---

## `teams/<id>/info.json` – Stammdaten einer Mannschaft

In dieser Datei stehen die Grunddaten einer Mannschaft – vor allem, **welche Saison gerade aktiv** ist und wie die Mannschaft in der Liga heißt.

### Beispiel (1. Herren)

```json
{
  "aktualisiert": "10.05.2026",
  "name": "1. Herren",
  "ligaTeamName": "TuS Esingen",
  "aktuelleSaison": "2025-26",
  "linkSpielplan": "https://www.handball.net/ligen/handball4all.hamburg.51/spielplan",
  "linkTabelle": "https://www.handball.net/ligen/handball4all.hamburg.51/tabelle"
}
```

### Felder

| Feld | Pflicht | Beschreibung |
|---|---|---|
| `aktualisiert` | ja | Datum der letzten Änderung |
| `name` | ja | Anzeigename der Mannschaft (gleich wie in `meta/teams.json`) |
| `ligaTeamName` | ja | Wie die Mannschaft **in der Liga** heißt (siehe Hinweis) |
| `aktuelleSaison` | ja | Welcher Saison-Ordner gerade aktiv ist (z.B. `"2025-26"`) |
| `linkSpielplan` | nein | Link zur Liga auf handball.net (für „Auf handball.net ansehen"-Button) |
| `linkTabelle` | nein | Link zur Tabelle auf handball.net |

### Wichtig: Was ist `ligaTeamName`?

Der `name` ist der Anzeigename in der App („1. Herren"). In der Liga heißt eure Mannschaft aber oft anders – meistens einfach „TuS Esingen", manchmal mit einer Nummer wie „TuS Esingen 2".

**Warum braucht die App das?**
Die App muss in den Spielergebnissen erkennen, welches Team euer eigenes ist. Sie sucht in den Spieltags-Dateien nach genau diesem Namen.

Beispiele:

| Mannschaft (`name`) | Liga-Name (`ligaTeamName`) |
|---|---|
| 1. Herren | TuS Esingen |
| 1. Damen | TuS Esingen |
| 2. Herren | TuS Esingen 2 |
| männlich D1 | TuS Esingen mD1 |
| männlich D2 | TuS Esingen mD2 |

Schau auf handball.net nach, wie die Mannschaft dort genau geschrieben ist, und übernimm das **exakt** (Groß- und Kleinschreibung, Leerzeichen).

### Wann du diese Datei änderst

- **Saisonwechsel:** `aktuelleSaison` auf die neue Saison umstellen (z.B. von `"2025-26"` auf `"2026-27"`)
- **Liga-Aufstieg/Abstieg:** Neue `linkSpielplan` und `linkTabelle` einfügen
- **Liga-Name in der Saison ändert sich:** `ligaTeamName` anpassen

### Stolperfallen

- `aktuelleSaison` muss zu einem Ordnernamen unter `saisons/` passen. Wenn du `"2026-27"` einträgst, aber den Ordner noch nicht angelegt hast, sieht die App nichts mehr.
- `ligaTeamName` muss **wortgenau** mit dem übereinstimmen, was du in den Spieltags-Dateien als `heim` oder `gast` einträgst. Ein Tippfehler hier macht die Tabellenberechnung kaputt.

---

## `teams/<id>/kader.json` – Spieler und Trainer

In dieser Datei stehen alle Spieler und Trainer einer Mannschaft. Sie wird auf der Mannschafts-Detailseite in der App angezeigt.

### Beispiel (1. Herren, gekürzt)

```json
{
  "aktualisiert": "29.04.2026",
  "mannschaft": "1. Herren",
  "liga": "Männer Oberliga Hamburg",
  "trainer": [
    {
      "name": "Fabian Wurl",
      "rolle": "Trainer",
      "alter": 32,
      "telefon": "+49 176 66860716",
      "email": "fabian.wurl@googlemail.com"
    },
    {
      "name": "Yannick Hellmich",
      "rolle": "Co-Trainer",
      "alter": 31
    },
    {
      "name": "Michel Göttsche",
      "rolle": "Physiotherapeut",
      "alter": 23
    }
  ],
  "spieler": [
    {
      "name": "Julian Hammon",
      "nummer": 16,
      "position": "Torwart",
      "alter": 21,
      "seitJahr": 2022
    },
    {
      "name": "Niklas Richters",
      "nummer": 14,
      "position": "Rückraum",
      "alter": 26,
      "seitJahr": 2019
    },
    {
      "name": "Matti Theophile",
      "nummer": 19,
      "position": "Kreisläufer",
      "alter": 21,
      "seitJahr": 2021
    }
  ]
}
```

### Felder auf oberster Ebene

| Feld | Pflicht | Beschreibung |
|---|---|---|
| `aktualisiert` | ja | Datum der letzten Änderung |
| `mannschaft` | ja | Anzeigename der Mannschaft |
| `liga` | ja | Volle Liga-Bezeichnung (z.B. „Männer Oberliga Hamburg") |
| `trainer` | ja | Liste aller Trainer (kann leer sein: `[]`) |
| `spieler` | ja | Liste aller Spieler (kann leer sein: `[]`) |

### Pro Trainer

| Feld | Pflicht | Beschreibung |
|---|---|---|
| `name` | ja | Vollständiger Name |
| `rolle` | ja | z.B. „Trainer", „Co-Trainer", „Physiotherapeut", „Spielertrainer" |
| `alter` | ja | Alter in Jahren |
| `telefon` | nein | Telefonnummer (nur bei Hauptkontakten) |
| `email` | nein | E-Mail (nur bei Hauptkontakten) |

### Pro Spieler

| Feld | Pflicht | Beschreibung |
|---|---|---|
| `name` | ja | Vollständiger Name |
| `nummer` | ja | Trikotnummer (Zahl, ohne Anführungszeichen) |
| `position` | ja | z.B. „Torwart", „Außen", „Rückraum", „Kreisläufer" |
| `alter` | ja | Alter in Jahren |
| `seitJahr` | ja | Jahr, seit dem der Spieler im Verein ist (Zahl, z.B. `2019`) |

### Wann du diese Datei änderst

- **Neuer Spieler kommt:** Neuen Eintrag in `spieler` ergänzen
- **Spieler verlässt den Verein:** Eintrag entfernen
- **Trainer wechselt:** Eintrag in `trainer` aktualisieren oder ergänzen
- **Saisonwechsel:** Alter aller Spieler/Trainer um 1 erhöhen (sofern Geburtstag vor Saisonstart liegt)

### Stolperfallen

- `nummer` und `alter` und `seitJahr` sind **Zahlen ohne Anführungszeichen**. Also `"nummer": 16`, nicht `"nummer": "16"`.
- Wenn du Telefonnummern einträgst: Format `+49 176 ...` mit Leerzeichen, in Anführungszeichen
- Bei leerem Kader: `"spieler": []` (eckige Klammern, leer) – nicht weglassen, sonst kann die Datei nicht gelesen werden

---

## `teams/<id>/training.json` – Trainingszeiten

In dieser Datei stehen die regelmäßigen Trainingszeiten der Mannschaft. Sie werden auf der Mannschafts-Detailseite angezeigt.

### Beispiel (1. Herren)

```json
{
  "aktualisiert": "30.04.2026",
  "mannschaft": "1. Herren",
  "trainingszeiten": [
    {
      "tag": "Mo",
      "von": "19:00",
      "bis": "20:30",
      "art": "Individualtraining",
      "ort": "neue-kgst"
    },
    {
      "tag": "Di",
      "von": "19:00",
      "bis": "20:30",
      "art": "Hallentraining",
      "ort": "neue-kgst"
    },
    {
      "tag": "Do",
      "von": "19:30",
      "bis": "22:00",
      "art": "Athletik + Hallentraining",
      "ort": "neue-kgst"
    }
  ]
}
```

### Felder auf oberster Ebene

| Feld | Pflicht | Beschreibung |
|---|---|---|
| `aktualisiert` | ja | Datum der letzten Änderung |
| `mannschaft` | ja | Anzeigename der Mannschaft |
| `trainingszeiten` | ja | Liste aller Trainings-Slots (kann leer sein: `[]`) |

### Pro Trainings-Slot

| Feld | Pflicht | Beschreibung |
|---|---|---|
| `tag` | ja | Wochentag als Zwei-Buchstaben-Kürzel: `Mo`, `Di`, `Mi`, `Do`, `Fr`, `Sa`, `So` |
| `von` | ja | Uhrzeit Start im Format `HH:MM` |
| `bis` | ja | Uhrzeit Ende im Format `HH:MM` |
| `art` | ja | Art des Trainings (z.B. „Hallentraining", „Athletik", „Individualtraining") |
| `ort` | ja | ID der Halle (siehe unten) |

### Hallen-IDs

Aktuell verfügbare `ort`-Werte:

| ID | Halle |
|---|---|
| `neue-kgst` | Neue KGST-Halle, Tornesch |
| `alte-kgst` | Alte KGST-Halle, Tornesch |

Wenn eine neue Halle dazukommt, muss sie im App-Code als Hallenname hinterlegt werden – sag in dem Fall im Entwickler-Chat Bescheid.

### Wann du diese Datei änderst

- **Trainingszeit verschiebt sich:** `von` und/oder `bis` anpassen
- **Neuer Trainings-Slot:** Neuen Eintrag in `trainingszeiten` ergänzen
- **Trainingspause (z.B. Sommerpause):** Eintrag entfernen oder ganze Liste leeren (`"trainingszeiten": []`)

### Stolperfallen

- Tag-Kürzel müssen genau so geschrieben sein wie oben angegeben (`Mo`, nicht `mo` oder `Montag`)
- Uhrzeiten immer mit führender Null: `09:00`, nicht `9:00`
- `ort` muss eine bekannte Hallen-ID sein, sonst zeigt die App den Eintrag ohne Hallennamen

---

# Die Inhaltsdateien im Detail

Dieses Kapitel beschreibt die Dateien, in denen die App-übergreifenden Inhalte gepflegt werden: News auf der Startseite, Hauptsponsoren und Mannschaftssponsoren.

## `content/news.json` – News-Beiträge

In dieser Datei stehen alle manuell gepflegten News-Beiträge, die auf der Startseite erscheinen. Spielergebnisse als „News" werden automatisch aus den Spieltagen generiert – die musst du hier **nicht** zusätzlich eintragen.

> ✨ **Gut zu wissen:** Du musst nur wenige Felder ausfüllen. Vieles, das früher manuell eingetragen werden musste (eindeutige ID, Anzeigedatum auf Deutsch, CSS-Klasse, Farbverlauf, Autor-Initialen), ergänzt die App automatisch aus deinen Angaben.

### Beispiel: Einfache News über das Vereinsleben

```json
{
  "aktualisiert": "10.05.2026",
  "news": [
    {
      "title": "Saisonabschlussfeier am 14. Juni",
      "lead": "Die 1. Herren feiern den 6. Tabellenplatz mit allen Fans im Vereinsheim.",
      "team": "1. Herren",
      "cat": "vereinsleben",
      "author": "Vorstand TuS Esingen",
      "sortDate": "2026-05-10",
      "body": [
        {
          "type": "text",
          "text": "Nach einer spannenden Saison laden wir alle Mitglieder, Spielerinnen und Fans zum Saisonabschluss in das Vereinsheim ein. Beginn ist um 18:00 Uhr."
        },
        {
          "type": "quote",
          "text": "Diese Saison war ein wichtiger Schritt für unsere Mannschaft.",
          "author": "Fabian Wurl, Trainer 1. Herren"
        }
      ]
    }
  ]
}
```

### Beispiel: Spielbericht mit Score-Box als Top-News

```json
{
  "title": "Wichtiger Sieg gegen Uetersen",
  "lead": "Die 1. Herren gewinnen souverän mit 30:27 in Uetersen.",
  "team": "1. Herren",
  "cat": "spielbericht",
  "author": "Fabian Wurl",
  "sortDate": "2026-04-26",
  "topNews": true,
  "matchTeam": "1-herren",
  "matchDate": "2026-04-25",
  "body": [
    {
      "type": "score",
      "home": "TSV Uetersen",
      "guest": "TuS Esingen",
      "result": "27:30",
      "liga": "Männer Oberliga Hamburg",
      "outcome": "Sieg"
    },
    {
      "type": "text",
      "text": "In einem hart umkämpften Auswärtsspiel setzten sich die Esinger Herren in der zweiten Halbzeit deutlich ab. Besonders die starke Defensive bereitete dem TSV Probleme."
    }
  ]
}
```

### Felder auf oberster Ebene

| Feld | Pflicht | Beschreibung |
|---|---|---|
| `aktualisiert` | ja | Datum der letzten Änderung |
| `news` | ja | Liste aller News-Einträge (kann leer sein: `[]`) |

### Pflichtfelder pro News-Eintrag

Diese Felder musst du immer ausfüllen:

| Feld | Beschreibung |
|---|---|
| `title` | Hauptüberschrift der News |
| `lead` | Kurzer einleitender Satz (1-2 Zeilen), wird unter dem Titel angezeigt |
| `cat` | Kategorie der News (siehe Tabelle unten) |
| `author` | Anzeigename des Autors |
| `sortDate` | Sortier- und Anzeigedatum im Format `YYYY-MM-DD` |
| `body` | Liste aller Inhalts-Blöcke der News (siehe unten) |

### Optionale Felder

Diese Felder sind nützlich, aber nicht zwingend:

| Feld | Wann verwenden | Beschreibung |
|---|---|---|
| `team` | Wenn News zu einer Mannschaft gehört | z.B. `"1. Herren"`. Wird als farbiger Tag angezeigt. |
| `topNews` | Wenn News ganz oben groß erscheinen soll | `true` oder `false` (Standard: `false`) |
| `matchTeam` | Bei Spielberichten | Mannschafts-ID (z.B. `"1-herren"`). Verhindert, dass die automatische Spielbericht-News doppelt erscheint. |
| `matchDate` | Bei Spielberichten | Spieldatum im Format `YYYY-MM-DD` (gleicher Tag wie das Spiel) |

### Felder, die du **nicht** ausfüllen musst

Die App ergänzt folgende Felder automatisch aus deinen Angaben:

| Feld | Wird abgeleitet aus |
|---|---|
| `id` | `sortDate` + Slug aus `title` (z.B. `"2026-04-26-wichtiger-sieg-gegen-uetersen"`) |
| `date` | `sortDate` → deutsches Anzeigedatum (z.B. `"26. April 2026"`) |
| `catCl` | `cat` → CSS-Klasse (z.B. `"cat-spielbericht"`) |
| `authorIni` | `author` → Initialen (z.B. `"Fabian Wurl"` → `"FW"`). Bei Vereinsnamen wie „Vorstand TuS Esingen" wird automatisch das Vereinslogo statt der Initialen angezeigt. |
| `gradient` | Bei Spielberichten: aus dem `outcome` der Score-Box (grün bei Sieg, rot bei Niederlage, orange bei Unentschieden). Bei allen anderen News: dunkler Default-Verlauf. |

> 💡 Wenn du eines dieser Felder doch manuell setzen willst (z.B. einen eigenen Gradient für eine besondere News), funktioniert das weiterhin – die App überschreibt manuell gesetzte Werte nie.

### Mögliche Kategorien

| `cat` | Bedeutung |
|---|---|
| `spielbericht` | Bericht über ein gespieltes Match |
| `vereinsleben` | Veranstaltungen, Feiern, Termine |
| `transfer` | Spieler-Wechsel, neue Trainer |
| `ankuendigung` | Wichtige Mitteilungen |

Wenn eine neue Kategorie nötig wird, muss sie im App-Code als CSS-Klasse hinterlegt werden – sag im Entwickler-Chat Bescheid.

### Body-Blöcke

Der Inhalt einer News besteht aus mehreren Blöcken. Jeder Block hat ein `type`-Feld:

**Text-Block:**
```json
{
  "type": "text",
  "text": "Hier steht der Fließtext..."
}
```

**Score-Block (Spielergebnis):**
```json
{
  "type": "score",
  "home": "TSV Uetersen",
  "guest": "TuS Esingen",
  "result": "27:30",
  "liga": "Männer Oberliga Hamburg",
  "outcome": "Sieg"
}
```

Mögliche `outcome`-Werte: `"Sieg"`, `"Niederlage"`, `"Unentschieden"` (aus TuS-Sicht). Bestimmt die Hintergrundfarbe der Score-Box **und** des Hero-Bereichs der News.

**Zitat-Block:**
```json
{
  "type": "quote",
  "text": "Diese Saison war ein wichtiger Schritt für uns.",
  "author": "Fabian Wurl, Trainer"
}
```

### Wann du diese Datei änderst

- **Neue News veröffentlichen:** Neuen Eintrag in `news` ergänzen (oben oder unten, egal – die App sortiert nach `sortDate`)
- **News korrigieren:** Eintrag bearbeiten
- **News löschen:** Eintrag aus der Liste entfernen

### Stolperfallen

- `sortDate` ist Pflicht – ohne dieses Feld wird die News falsch einsortiert
- `body` ist immer eine **Liste**, auch wenn nur ein Text-Block drin ist
- Bei `matchTeam`: ID exakt wie in `meta/teams.json` (z.B. `"1-herren"`, nicht `"1. Herren"`)
- Wenn du einen Spielbericht schreibst, **immer** `matchTeam` und `matchDate` setzen – sonst kann die App nicht erkennen, dass es zu einem konkreten Spiel gehört, und zeigt eventuell zwei News zum selben Spiel an

---

## `content/partners.json` – Hauptsponsoren

In dieser Datei stehen die **Stammdaten** aller Sponsoren des Vereins. Sie wird sowohl für die Hauptsponsoren auf der Startseite als auch von den Mannschafts-Sponsoren (`teams/<id>/partner.json`) verwendet.

### Beispiel

```json
{
  "aktualisiert": "10.05.2026",
  "stadtwerke-suedholstein": {
    "name": "Stadtwerke Südholstein",
    "logo": "data/logos-sponsoren/stadtwerke.jpg",
    "url": "https://www.sw-suedholstein.de/"
  },
  "gebr-schmidt": {
    "name": "Gebr. Schmidt GmbH",
    "logo": "data/logos-sponsoren/schmidt.png",
    "url": "https://www.gebr-schmidt.de/"
  },
  "krieg": {
    "name": "Bauunternehmen Krieg",
    "logo": "data/logos-sponsoren/krieg.png",
    "url": "https://www.bauunternehmen-krieg.de/"
  },
  "bayer": {
    "name": "Bayer AG",
    "logo": "data/logos-sponsoren/bayer.png",
    "url": "https://www.bayer.de/"
  }
}
```

### Struktur

Die Datei ist eine **flache Sammlung** aller Sponsoren mit ihrer ID als Schlüssel. Pro Sponsor:

| Feld | Pflicht | Beschreibung |
|---|---|---|
| `name` | ja | Vollständiger Name des Sponsors |
| `logo` | ja | Pfad zur Logo-Datei (relativ zur App, also z.B. `"data/logos/..."`) |
| `url` | ja | Webseite des Sponsors |

**Plus auf oberster Ebene:**

| Feld | Pflicht | Beschreibung |
|---|---|---|
| `aktualisiert` | ja | Datum der letzten Änderung |

### Wann du diese Datei änderst

- **Neuer Sponsor:** Neuen Eintrag mit eindeutiger ID hinzufügen
- **Sponsor wechselt Logo/Webseite:** Werte beim bestehenden Eintrag aktualisieren
- **Sponsor verlässt den Verein:** Eintrag entfernen (vorher prüfen, ob er noch in einer `teams/<id>/partner.json` referenziert wird)

### Stolperfallen

- Die **ID** (der Schlüssel) muss eindeutig sein und sollte aus Kleinbuchstaben mit Bindestrichen bestehen (z.B. `"stadtwerke-suedholstein"`, nicht `"Stadtwerke Südholstein"`)
- `logo` ist ein Pfad **innerhalb des Repos**, nicht eine externe URL. Die Logodatei muss vorher in `data/logos-sponsoren/` abgelegt werden.
- `aktualisiert` steht auf oberster Ebene neben den Sponsoren-IDs

---

## `teams/<id>/partner.json` – Mannschaftssponsoren

Diese Datei listet auf, welche Sponsoren bei einer Mannschaft auf der Detailseite angezeigt werden. Sie enthält **nur die IDs** der Sponsoren – die Details werden aus `content/partners.json` geladen.

### Beispiel (1. Herren)

```json
{
  "aktualisiert": "30.04.2026",
  "mannschaft": "1. Herren",
  "partner": ["gebr-schmidt", "krieg", "bayer"]
}
```

### Felder

| Feld | Pflicht | Beschreibung |
|---|---|---|
| `aktualisiert` | ja | Datum der letzten Änderung |
| `mannschaft` | ja | Anzeigename der Mannschaft |
| `partner` | ja | Liste von Sponsoren-IDs (kann leer sein: `[]`) |

### Wann du diese Datei änderst

- **Mannschaft bekommt einen neuen Sponsor:** ID zur `partner`-Liste hinzufügen
- **Sponsor zieht sich aus dieser Mannschaft zurück:** ID aus der Liste entfernen
- **Reihenfolge in der App anpassen:** IDs in der gewünschten Reihenfolge sortieren

### Stolperfallen

- Die IDs müssen **exakt** den Schlüsseln in `content/partners.json` entsprechen. Tippfehler → der Sponsor wird nicht angezeigt.
- Falls die `partner`-Liste leer ist, wird in der App der gesamte Mannschaftssponsoren-Bereich ausgeblendet
- Wenn ein Sponsor neu dazukommt, muss er **zuerst** in `content/partners.json` angelegt werden, dann kann er hier referenziert werden

---

# Die Spielbetrieb-Dateien im Detail

Dieses Kapitel beschreibt die Dateien, in denen Spielergebnisse gepflegt werden. **Diese Dateien werden am häufigsten verändert** – meistens wöchentlich nach den Spielen am Wochenende.

## `teams/<id>/saisons/<saison>/meta.json` – Liga-Stammdaten einer Saison

Diese Datei beschreibt die **Liga und Saison** einer Mannschaft: In welcher Liga wird gespielt, welche Mannschaften nehmen teil, wie viele Spieltage sind geplant, welches Punktesystem gilt. Sie wird einmal pro Saison angelegt und bei Bedarf erweitert (z.B. wenn eine neue Mannschaft in die Liga kommt).

### Beispiel (1. Herren, Saison 2025/26)

```json
{
  "saison": "2025/26",
  "liga": "Männer Oberliga Hamburg",
  "punkteSystem": "2-punkte",
  "wertungTore": { "fuerSieger": 0, "fuerVerlierer": 0 },
  "spieltageGeplant": 26,
  "linkSpielplan": "https://www.handball.net/ligen/handball4all.hamburg.51/spielplan",
  "linkTabelle": "https://www.handball.net/ligen/handball4all.hamburg.51/tabelle",
  "mannschaften": [
    { "name": "TuS Esingen",          "logo": "tus-esingen.png" },
    { "name": "Ahrensburger TSV",      "logo": "ahrensburg.png" },
    { "name": "FC St. Pauli",          "logo": "st-pauli.png" },
    { "name": "TV Fischbek",           "logo": "fischbek.png" },
    { "name": "TSV Ellerbek 2",        "logo": "ellerbek-2.png" },
    { "name": "HSG Elbvororte",        "logo": "elbvororte.png" },
    { "name": "TH Eilbeck",            "logo": "eilbeck.png" },
    { "name": "HT Norderstedt 2",      "logo": "norderstedt-2.png" },
    { "name": "TSV Uetersen",          "logo": "uetersen.png" },
    { "name": "SG Hamburg-Nord 2",     "logo": "hh-nord-2.png" },
    { "name": "1. HC Quickborn",       "logo": "quickborn.png" },
    { "name": "HG Hamburg-Barmbek 2",  "logo": "barmbek-2.png" },
    { "name": "Rellinger TV 2",        "logo": "rellingen-2.png" }
  ]
}
```

### Felder

| Feld | Pflicht | Beschreibung |
|---|---|---|
| `saison` | ja | Anzeige-Bezeichnung der Saison (z.B. `"2025/26"`) |
| `liga` | ja | Vollständiger Liga-Name |
| `punkteSystem` | ja | Aktuell nur `"2-punkte"` unterstützt (Sieg=2, Unentschieden=1, Niederlage=0) |
| `wertungTore` | ja | Wie viele Tore werden bei einer Wertung (z.B. nicht angetretener Gegner) angerechnet (siehe unten) |
| `spieltageGeplant` | ja | Anzahl der Spieltage in der Saison (z.B. 26 bei 14 Mannschaften mit Hin- und Rückrunde) |
| `linkSpielplan` | nein | Link zur Liga auf handball.net |
| `linkTabelle` | nein | Link zur Tabelle auf handball.net |
| `mannschaften` | ja | Liste aller Mannschaften der Liga (siehe unten) |

### Das Feld `wertungTore`

Bei einer Wertung (eine Mannschaft tritt nicht an) bekommt der Sieger 2 Punkte ohne dass tatsächlich gespielt wurde. Dieses Feld legt fest, mit wie vielen Toren das Spiel in die Tabellenberechnung eingeht:

```json
"wertungTore": { "fuerSieger": 0, "fuerVerlierer": 0 }
```

- **Aktuell für eure Ligen:** `0:0` – also kein Einfluss auf die Tordifferenz
- Manche Verbände werten anders (z.B. `10:0`) – prüfe das beim ersten Anlegen der Saison

### Pro Mannschaft

| Feld | Pflicht | Beschreibung |
|---|---|---|
| `name` | ja | Name der Mannschaft, **exakt** wie er in den Spielergebnissen verwendet wird |
| `logo` | ja | Dateiname des Vereinslogos in `data/logos-mannschaften/` |

### Wann du diese Datei änderst

- **Saisonstart:** Datei wird neu angelegt (oder aus letzter Saison kopiert und angepasst)
- **Neue Mannschaft kommt in die Liga (Aufsteiger):** Eintrag in `mannschaften` ergänzen
- **Mannschaft zieht sich zurück:** Eintrag entfernen
- **Liga heißt anders / Saison-Bezeichnung ändert sich:** entsprechende Felder anpassen

### Stolperfallen

- Der `name` einer Mannschaft muss **exakt** so geschrieben sein wie in den Spieltags-Dateien (`heim`, `gast`). Auch Tippfehler wie „TSV Ellerbeck" statt „TSV Ellerbek" lassen die Tabellenberechnung scheitern.
- `logo` muss eine Datei sein, die tatsächlich in `data/logos-mannschaften/` liegt. Wenn das Logo fehlt, zeigt die App einen Platzhalter.
- Falls eine Mannschaft den eigenen Verein darstellt (`"TuS Esingen"`), muss der `name` exakt dem `ligaTeamName` aus `info.json` entsprechen
- `spieltageGeplant` ist nur ein Richtwert für die App-Anzeige – die tatsächliche Anzahl kommt aus den Dateien in `spieltage/`

---

## `teams/<id>/saisons/<saison>/spieltage/XX-kwNN.json` – Ein einzelner Spieltag

In dieser Datei stehen **alle Spiele eines Spieltags** einer Liga – also nicht nur die TuS-Spiele, sondern auch die der anderen Mannschaften. Aus diesen Dateien berechnet die App die komplette Tabelle.

**Diese Datei wird wöchentlich gepflegt** – das ist der häufigste Vorgang.

### Dateinamen-Konvention

Die Dateinamen kombinieren **Spieltag-Nummer** und **Kalenderwoche** der ersten Austragung:

- `01-kw37.json` = Spieltag 1, ursprünglich angesetzt in KW 37
- `02-kw38.json` = Spieltag 2, KW 38
- `05-kw41.json` = Spieltag 5, KW 41
- `24-kw17.json` = Spieltag 24, KW 17 des Folgejahres

**Beide Zahlen sind zweistellig** (`01`, nicht `1`). So bleibt die Sortierung im Repo-Browser korrekt.

Die KW im Dateinamen ist die **ursprünglich angesetzte Spielwoche**. Wenn ein Spiel innerhalb des Spieltags unter der Woche nachgeholt oder verlegt wird, bleibt der Dateiname trotzdem `XX-kwNN.json` – im `datum`-Feld des betroffenen Spiels steht dann das tatsächliche Spieldatum.

> 💡 **Pflege-Tipp:** Auf handball.net kannst du mit dem Filter „Aktuelle Spielwoche" die laufende Spielwoche anzeigen. Die KW der angezeigten Spiele findest du im Dateinamen (z.B. KW 41 → `05-kw41.json`).

### Beispiel (Spieltag 24, 1. Herren)

```json
{
  "spieltag": 24,
  "spiele": [
    {
      "datum": "2026-04-25T17:00:00",
      "heim": "TSV Uetersen",
      "gast": "TuS Esingen",
      "toreHeim": 30,
      "toreGast": 27,
      "halle": "Seminarstraße, Uetersen",
      "status": "finished"
    },
    {
      "datum": "2026-04-25T17:30:00",
      "heim": "Ahrensburger TSV",
      "gast": "FC St. Pauli",
      "toreHeim": 32,
      "toreGast": 30,
      "halle": "Heimgarten, Ahrensburg",
      "status": "finished"
    },
    {
      "datum": "2026-04-26T15:00:00",
      "heim": "TV Fischbek",
      "gast": "TH Eilbeck",
      "toreHeim": 28,
      "toreGast": 28,
      "halle": "Süderelbe, Hamburg",
      "status": "finished"
    },
    {
      "datum": "2026-04-26T18:00:00",
      "heim": "TSV Ellerbek 2",
      "gast": "HSG Elbvororte",
      "toreHeim": 25,
      "toreGast": 31,
      "halle": "Ellerbek, Ellerbek",
      "status": "finished"
    },
    {
      "datum": "2026-04-26T16:00:00",
      "heim": "Rellinger TV 2",
      "gast": "1. HC Quickborn",
      "toreHeim": 22,
      "toreGast": 24,
      "halle": "Egenbüttel, Rellingen",
      "status": "finished"
    },
    {
      "datum": "2026-04-26T18:30:00",
      "heim": "HG Hamburg-Barmbek 2",
      "gast": "HT Norderstedt 2",
      "toreHeim": null,
      "toreGast": null,
      "halle": "Langenfort, Hamburg",
      "status": "verlegt",
      "verlegtAuf": "2026-05-10T17:00:00"
    },
    {
      "datum": "2026-04-26T17:00:00",
      "heim": "SG Hamburg-Nord 2",
      "gast": "TuS Esingen",
      "toreHeim": 0,
      "toreGast": 0,
      "halle": "Tegelsberg, Hamburg",
      "status": "wertung-gast",
      "hinweis": "WG – Hamburg-Nord 2 nicht angetreten"
    }
  ]
}
```

### Felder auf oberster Ebene

| Feld | Pflicht | Beschreibung |
|---|---|---|
| `spieltag` | ja | Nummer des Spieltags als Zahl (z.B. `24`) |
| `spiele` | ja | Liste aller Spiele dieses Spieltags |

### Pro Spiel

| Feld | Pflicht | Beschreibung |
|---|---|---|
| `datum` | ja | Datum und Uhrzeit im ISO-Format: `YYYY-MM-DDTHH:MM:SS` |
| `heim` | ja | Heimmannschaft, exakt wie in `meta.json` |
| `gast` | ja | Gastmannschaft, exakt wie in `meta.json` |
| `toreHeim` | ja | Tore der Heimmannschaft (Zahl oder `null`, wenn noch nicht gespielt) |
| `toreGast` | ja | Tore der Gastmannschaft (Zahl oder `null`, wenn noch nicht gespielt) |
| `halle` | nein | Hallenname und Stadt (wie auf handball.net) |
| `status` | ja | Status des Spiels (siehe unten) |
| `hinweis` | nein | Freier Hinweistext (z.B. Erklärung einer Wertung) |
| `verlegtAuf` | nein | Bei verlegten Spielen: neues Datum im ISO-Format |

### Die `status`-Werte

| Status | Bedeutung |
|---|---|
| `scheduled` | Spiel ist angesetzt, noch nicht gespielt. `toreHeim` und `toreGast` sind `null`. |
| `finished` | Spiel wurde gespielt, Ergebnis steht fest. |
| `wertung-heim` | Wertung **für** die Heimmannschaft, weil Gast nicht angetreten ist. Tore = was in `wertungTore` der Liga-Meta steht. |
| `wertung-gast` | Wertung **für** die Gastmannschaft, weil Heim nicht angetreten ist. Tore = was in `wertungTore` der Liga-Meta steht. |
| `verlegt` | Spiel wurde verschoben. Neues Datum steht in `verlegtAuf`. `toreHeim`/`toreGast` bleiben `null`, bis das Spiel gespielt wurde. |

**Wichtig:** Sobald ein verlegtes Spiel gespielt wurde, ändere den `status` auf `"finished"` und trage die Tore ein. Das Feld `verlegtAuf` kann dann gelöscht werden, oder du behältst es als Historie (App ignoriert es bei `finished`).

### Wie die Tabelle daraus berechnet wird

Die App geht alle Spiele aller Spieltage einer Saison durch und summiert pro Mannschaft:

- **Punkte:** 2 pro Sieg, 1 pro Unentschieden, 0 pro Niederlage
- **Spiele:** Anzahl gewerteter Spiele (alles außer `scheduled` und `verlegt`)
- **Tore (eigene und gegnerische):** Aus `toreHeim` und `toreGast`
- **Tordifferenz:** Eigene Tore minus gegnerische Tore
- **Bei Wertungen:** Punkte gehen an Sieger, Tore aus `wertungTore` der Liga-Meta

Das passiert **immer live** beim Öffnen der Mannschaftsseite. Du musst die Tabelle nie irgendwo pflegen.

### Wann du diese Datei änderst

- **Spielergebnis nach dem Wochenende eintragen:** `toreHeim`, `toreGast` ausfüllen, `status` auf `"finished"` setzen
- **Spielverlegung:** `status` auf `"verlegt"` setzen, `verlegtAuf` ergänzen
- **Wertung wegen Nicht-Antreten:** `status` auf `"wertung-heim"` oder `"wertung-gast"`, Tore aus `wertungTore` eintragen
- **Tippfehler korrigieren:** Werte direkt anpassen, App rechnet beim nächsten Aufruf neu

### Stolperfallen

- **`heim` und `gast` müssen exakt wie in `meta.json` geschrieben sein** – sonst wird das Spiel nicht in die Tabelle gerechnet
- `toreHeim` und `toreGast` sind **Zahlen ohne Anführungszeichen** oder `null`. Also `"toreHeim": 30`, nicht `"toreHeim": "30"`. Bei nicht gespieltem Status: `"toreHeim": null`.
- Datum **immer mit Uhrzeit**: `"2026-04-25T17:00:00"`. Wenn die Uhrzeit unbekannt ist, nimm `"00:00:00"` als Platzhalter.
- Bei Wertungen die Tore-Werte mit dem `wertungTore`-Feld der Liga-Meta abgleichen (typischerweise 0:0)
- `spieltag`-Nummer in der Datei und im Dateinamen müssen übereinstimmen (`12.json` → `"spieltag": 12`)

### Spieltage vorbereiten am Saisonanfang

Vor Saisonbeginn empfehle ich, **alle Spieltage einer Saison schon als Dateien anzulegen**, mit den fertigen Paarungen aus handball.net, aber `toreHeim: null`, `toreGast: null` und `status: "scheduled"`. So musst du wöchentlich nur die Tore eintragen und den Status auf `"finished"` setzen, statt jedes Mal das ganze Spiel neu zu erfassen.

---

## `teams/<id>/saisons/<saison>/pokalspiele.json` – Pokalspiele einer Saison

Pokalspiele gehören nicht zur Liga und zählen nicht für die Tabelle. Sie werden saisonweise getrennt gepflegt – pro Saison eine Datei.

### Beispiel (1. Herren, Saison 2025/26)

```json
{
  "aktualisiert": "10.05.2026",
  "spiele": [
    {
      "wettbewerb": "Männer Pokal Hamburg",
      "runde": "1. Runde",
      "datum": "2025-09-12T19:00:00",
      "heim": "TuS Esingen",
      "gast": "TSV Ellerbek 2",
      "toreHeim": 28,
      "toreGast": 25,
      "halle": "Esingen neu, Tornesch",
      "status": "finished"
    },
    {
      "wettbewerb": "Männer Pokal Hamburg",
      "runde": "Achtelfinale",
      "datum": "2026-01-10T17:00:00",
      "heim": "TuS Esingen",
      "gast": "HT Norderstedt 2",
      "toreHeim": 30,
      "toreGast": 26,
      "halle": "Esingen neu, Tornesch",
      "status": "finished"
    },
    {
      "wettbewerb": "Männer Pokal Hamburg",
      "runde": "Viertelfinale",
      "datum": "2026-03-15T19:00:00",
      "heim": "FC St. Pauli",
      "gast": "TuS Esingen",
      "toreHeim": null,
      "toreGast": null,
      "halle": "Budapester Straße, Hamburg",
      "status": "scheduled"
    }
  ]
}
```

### Felder auf oberster Ebene

| Feld | Pflicht | Beschreibung |
|---|---|---|
| `aktualisiert` | ja | Datum der letzten Änderung |
| `spiele` | ja | Liste aller Pokalspiele dieser Saison (kann leer sein: `[]`) |

### Pro Spiel

| Feld | Pflicht | Beschreibung |
|---|---|---|
| `wettbewerb` | ja | Wettbewerbsname (z.B. `"Männer Pokal Hamburg"`, `"DHB-Pokal"`) |
| `runde` | nein | Pokalrunde (z.B. `"1. Runde"`, `"Achtelfinale"`, `"Halbfinale"`, `"Finale"`) |
| `datum` | ja | Datum und Uhrzeit im ISO-Format |
| `heim` | ja | Heimmannschaft |
| `gast` | ja | Gastmannschaft |
| `toreHeim` | ja | Tore Heim (Zahl oder `null`, wenn noch nicht gespielt) |
| `toreGast` | ja | Tore Gast (Zahl oder `null`, wenn noch nicht gespielt) |
| `halle` | nein | Hallenname und Stadt |
| `status` | ja | `"scheduled"` oder `"finished"` |

### Wann du diese Datei änderst

- **Neuer Pokalauftritt steht an:** Neuen Eintrag mit `status: "scheduled"` ergänzen
- **Ergebnis nach dem Spiel:** `toreHeim`, `toreGast`, `status` auf `"finished"`
- **Pokalrunde ändert sich:** Beim Weiterkommen entsteht ein neues Spiel für die nächste Runde

### Stolperfallen

- Pokalspiele werden **nicht** für die Liga-Tabelle gewertet
- Es gibt **keinen Status für Wertungen** im KO-System – ein Forfait wird einfach als `"finished"` mit 0:0 (oder verbandsspezifischer Wertung) eingetragen
- Bei Saisonwechsel: Neue Saison bedeutet neue `pokalspiele.json`. Alte Saison bleibt im alten Saison-Ordner als Historie

---

## `teams/<id>/saisons/<saison>/testspiele.json` – Testspiele einer Saison

Testspiele (auch „Freundschaftsspiele") werden saisonweise getrennt gepflegt. Sie zählen nicht für Liga oder Pokal und dienen zur Vorbereitung oder Trainingsergänzung.

### Beispiel (1. Herren, Saison 2025/26)

```json
{
  "aktualisiert": "10.05.2026",
  "spiele": [
    {
      "anlass": "Vorbereitung Saison 2025/26",
      "datum": "2025-08-23T17:00:00",
      "heim": "TuS Esingen",
      "gast": "Ahrensburger TSV",
      "toreHeim": 26,
      "toreGast": 28,
      "halle": "Esingen neu, Tornesch",
      "status": "finished"
    },
    {
      "anlass": "Vorbereitung Saison 2025/26",
      "datum": "2025-08-30T17:00:00",
      "heim": "TuS Esingen",
      "gast": "TV Fischbek",
      "toreHeim": 28,
      "toreGast": 24,
      "halle": "Esingen neu, Tornesch",
      "status": "finished"
    },
    {
      "anlass": "Wintervorbereitung",
      "datum": "2026-01-05T19:00:00",
      "heim": "HSG Pinnau",
      "gast": "TuS Esingen",
      "toreHeim": null,
      "toreGast": null,
      "halle": "Pinneberg, Sporthalle",
      "status": "scheduled"
    }
  ]
}
```

### Felder auf oberster Ebene

| Feld | Pflicht | Beschreibung |
|---|---|---|
| `aktualisiert` | ja | Datum der letzten Änderung |
| `spiele` | ja | Liste aller Testspiele dieser Saison (kann leer sein: `[]`) |

### Pro Spiel

| Feld | Pflicht | Beschreibung |
|---|---|---|
| `anlass` | nein | Anlass des Testspiels (z.B. `"Vorbereitung Saison 2025/26"`, `"Wintervorbereitung"`, `"Trainingslager"`) |
| `datum` | ja | Datum und Uhrzeit im ISO-Format |
| `heim` | ja | Heimmannschaft |
| `gast` | ja | Gastmannschaft |
| `toreHeim` | ja | Tore Heim (Zahl oder `null`, wenn noch nicht gespielt) |
| `toreGast` | ja | Tore Gast (Zahl oder `null`, wenn noch nicht gespielt) |
| `halle` | nein | Hallenname und Stadt |
| `status` | ja | `"scheduled"` oder `"finished"` |

### Wann du diese Datei änderst

- **Neues Testspiel:** Neuen Eintrag mit `status: "scheduled"` ergänzen
- **Ergebnis nach dem Spiel:** `toreHeim`, `toreGast`, `status` auf `"finished"`
- **Testspiel wird abgesagt:** Eintrag aus der Liste entfernen (Testspiele tauchen sonst nirgendwo auf, daher kein „cancelled"-Status nötig)

### Stolperfallen

- Testspiele werden **nicht** für die Liga-Tabelle gewertet
- Im Gegensatz zu Liga- und Pokalspielen gibt es **keinen Wertungs-Status** – ein nicht zustandegekommenes Testspiel wird einfach entfernt

---

# Pflege-Workflows

Dieser Teil ist der **handlungsorientierte** Teil der Anleitung. Hier geht es nicht mehr darum, was in welcher Datei steht, sondern darum, wie du in typischen Situationen vorgehst.

Die Reihenfolge orientiert sich daran, was am häufigsten passiert – beginnend mit dem wöchentlichen Spieltag-Update am Sonntagabend.

---

## Wöchentlich: Spielergebnisse eintragen

Das ist der häufigste Vorgang. Nach jedem Spielwochenende werden die Ergebnisse aller TuS-Mannschaften und der anderen Liga-Spiele eingetragen.

### Was du brauchst

- Die Spielergebnisse des Wochenendes (z.B. über handball.net abrufbar)
- Browser-Zugang zum GitHub-Repository
- Etwa 15-25 Minuten Zeit (bei 4-5 Liga-Spielen pro Mannschaft)

### Schritt-für-Schritt-Anleitung

**1. Spieltag-Datei der Mannschaft öffnen**

Im Repository zur Datei der Mannschaft und Saison navigieren:

```
data/teams/<mannschaft>/saisons/<saison>/spieltage/<XX-kwNN>.json
```

Beispiel: Für Spieltag 24 der 1. Herren in Saison 2025/26 (Spielwoche KW 17):
```
data/teams/1-herren/saisons/2025-26/spieltage/24-kw17.json
```

> 💡 **Wie finde ich die richtige Datei?** Auf handball.net Filter „Aktuelle Spielwoche" anwenden – die angezeigte KW findest du im Dateinamen wieder.

**2. In den Edit-Modus wechseln**

Oben rechts auf das Bleistift-Symbol (✏️) klicken.

**3. Ergebnisse eintragen**

Für jedes gespielte Spiel **drei Werte** anpassen:

- `toreHeim`: Anzahl Tore der Heimmannschaft (Zahl ohne Anführungszeichen)
- `toreGast`: Anzahl Tore der Gastmannschaft (Zahl ohne Anführungszeichen)
- `status`: von `"scheduled"` auf `"finished"` ändern

**Vorher:**
```json
{
  "datum": "2026-05-02T17:00:00",
  "heim": "TuS Esingen",
  "gast": "TV Fischbek",
  "toreHeim": null,
  "toreGast": null,
  "halle": "Esingen neu, Tornesch",
  "status": "scheduled"
}
```

**Nachher:**
```json
{
  "datum": "2026-05-02T17:00:00",
  "heim": "TuS Esingen",
  "gast": "TV Fischbek",
  "toreHeim": 28,
  "toreGast": 25,
  "halle": "Esingen neu, Tornesch",
  "status": "finished"
}
```

**4. Speichern als Commit**

Unten auf der Seite das Commit-Formular ausfüllen:

- **Commit-Message:** Klar und kurz, z.B. `Spieltag 25 1. Herren: Ergebnisse eingetragen`
- Auf „Commit changes" klicken

**5. Mit der nächsten Mannschaft weitermachen**

Wiederhole die Schritte für alle anderen Mannschaften, die an diesem Wochenende gespielt haben.

### Tipp: Eigene Aufteilung im Pfleger-Team

Bei mehreren Pflegern lohnt es sich, die Mannschaften aufzuteilen:

- Pfleger A: 1. Herren, 2. Herren, männliche Jugend
- Pfleger B: 1. Damen, 2. Damen, weibliche Jugend
- Pfleger C: D-Jugend und jüngere

So weiß jeder genau, wer welche Datei am Sonntagabend bearbeitet, und es kommt nicht zu Doppelarbeit.

### Was passiert automatisch

Sobald die Ergebnisse committet sind:

1. **GitHub Pages baut die App neu** (dauert 1-2 Minuten)
2. **Beim nächsten App-Öffnen** sehen alle Nutzer die neuen Ergebnisse
3. **Die Tabelle aktualisiert sich automatisch** – du musst nichts pflegen
4. **Spielberichte-News** zu den TuS-Spielen erscheinen automatisch auf der Startseite

### Stolperfallen

- Wenn du nur die Tore eingibst, aber den `status` auf `"scheduled"` lässt, **wird das Spiel nicht gewertet**. Status immer auf `"finished"` setzen.
- `toreHeim` und `toreGast` müssen **Zahlen ohne Anführungszeichen** sein. Also `28`, nicht `"28"`.
- Wenn du dich vertippst, kannst du jederzeit zurück in die Datei gehen und korrigieren – die Tabelle rechnet beim nächsten Aufruf neu.

---

## Spielverlegung eintragen

Manchmal wird ein Spiel verschoben (Krankheit, Halle nicht verfügbar, Vereinsentscheidung). Der **Spieltag bleibt gleich**, nur Datum und Status ändern sich.

### Vorgehen

In der entsprechenden Spieltag-Datei das Spiel finden und folgende Felder anpassen:

**1. `status` auf `"verlegt"` setzen**

**2. Neues Datum im Feld `verlegtAuf` ergänzen** (im gleichen Format wie `datum`)

**3. `toreHeim` und `toreGast` bleiben auf `null`**, bis das Spiel tatsächlich gespielt wurde

**Beispiel:**

```json
{
  "datum": "2026-04-25T17:00:00",
  "heim": "HG Hamburg-Barmbek 2",
  "gast": "HT Norderstedt 2",
  "toreHeim": null,
  "toreGast": null,
  "halle": "Langenfort, Hamburg",
  "status": "verlegt",
  "verlegtAuf": "2026-05-10T17:00:00",
  "hinweis": "Wegen Hallenwartung verschoben"
}
```

Das Feld `hinweis` ist optional, hilft aber, den Grund festzuhalten.

### Wenn das verlegte Spiel später gespielt wird

Nach dem Nachholspiel:

- `status` auf `"finished"` setzen
- `toreHeim` und `toreGast` eintragen
- Das Feld `verlegtAuf` kann gelöscht werden (oder bleibt drin – die App ignoriert es bei `"finished"`)

Der ursprüngliche `spieltag` bleibt der Spieltag, an dem das Spiel laut Spielplan ursprünglich gewertet wurde – auch wenn das tatsächliche Datum später war. So bleibt die Tabellenberechnung korrekt.

---

## Wertung wegen Nicht-Antreten

Wenn eine Mannschaft nicht zum Spiel erscheint, wird das Spiel mit einer **Wertung** abgeschlossen. Der anwesende Verein bekommt die 2 Punkte, der nicht angetretene Verein 0 Punkte.

### Vorgehen

In der Spieltag-Datei das betreffende Spiel anpassen:

- `status`: `"wertung-heim"` (wenn der Gast nicht antritt → Heim gewinnt) oder `"wertung-gast"` (wenn Heim nicht antritt → Gast gewinnt)
- `toreHeim` und `toreGast`: Werte aus dem `wertungTore`-Feld der `meta.json` der Saison (in der Regel `0` und `0`)
- `hinweis`: Kurze Erklärung (optional, aber empfohlen)

**Beispiel: Gast (Hamburg-Nord 2) nicht angetreten**

```json
{
  "datum": "2026-04-26T17:00:00",
  "heim": "SG Hamburg-Nord 2",
  "gast": "TuS Esingen",
  "toreHeim": 0,
  "toreGast": 0,
  "halle": "Tegelsberg, Hamburg",
  "status": "wertung-gast",
  "hinweis": "WG – Hamburg-Nord 2 nicht angetreten"
}
```

### Was passiert in der Tabelle

Bei einer Wertung gehen 2 Punkte an den Sieger, 0 Punkte an den Verlierer, und die Tore werden gezählt wie in `wertungTore` festgelegt (Standard: 0:0, also keine Auswirkung auf die Tordifferenz).

---

## Tippfehler korrigieren

Egal, ob bei einem Spielergebnis, im Kader oder in den News – jede Datei ist im Repository nachträglich änderbar.

### Vorgehen

1. Die betreffende Datei öffnen
2. Auf den Bleistift klicken (✏️)
3. Den Fehler korrigieren
4. Mit einer aussagekräftigen Commit-Message speichern (z.B. `Tippfehler: TSV Ellerbek statt TSV Ellerbeck`)

### Was passiert in der App

- Bei **Spielergebnissen:** Die Tabelle wird beim nächsten App-Öffnen automatisch neu berechnet.
- Bei **News:** Die News wird beim nächsten App-Öffnen aktualisiert angezeigt.
- Bei **Kader/Training:** Die Mannschaftsseite zeigt beim nächsten Öffnen die neuen Daten.

### Was nicht passiert

Es gibt **keine Versionierung in der App**, die alte Versionen zeigt. Sobald du eine Korrektur committest, ist sie für alle Nutzer „die Wahrheit". Die Git-Versionshistorie im Repository bleibt natürlich erhalten.

---

## Saisonstart: Neue Saison anlegen

Vor jeder neuen Saison muss für jede Mannschaft ein neuer Saison-Ordner angelegt werden. Das ist der **aufwendigste** Workflow im Jahr und sollte am besten **ein paar Wochen vor Saisonstart** vorbereitet werden, wenn die Spielpläne von handball.net verfügbar sind.

### Schritt-für-Schritt

**1. Neuen Saison-Ordner anlegen**

Unter `data/teams/<mannschaft>/saisons/` einen neuen Ordner mit dem Saison-Namen anlegen, z.B. `2026-27/`.

> **Tipp:** Den einfachsten Weg, einen neuen Ordner anzulegen, beschreibt das spätere Kapitel „GitHub-Crashkurs". Kurz: Beim Anlegen einer Datei den vollständigen Pfad (mit Slash) als Namen eingeben, GitHub legt die Unterordner automatisch an.

**2. `meta.json` für die neue Saison erstellen**

In den neuen Saison-Ordner eine Datei `meta.json` anlegen mit:
- Liga-Name dieser Saison
- Punktesystem (`"2-punkte"`)
- Mannschaftsliste (alle Vereine der Liga)
- Geplante Anzahl Spieltage
- Links zur Liga auf handball.net

Die genauen Felder findest du im Kapitel `teams/<id>/saisons/<saison>/meta.json` weiter oben.

**3. Spieltage anlegen**

Für jeden geplanten Spieltag eine Datei in `spieltage/` anlegen, mit Dateinamen im Format `XX-kwNN.json`.

Beispiel für die ersten Spieltage einer Saison, die im September startet:
- `01-kw37.json` (Spieltag 1, KW 37)
- `02-kw38.json` (Spieltag 2, KW 38)
- ...
- `24-kw17.json` (Spieltag 24, KW 17 des Folgejahres)

Welche KW jeder Spieltag bekommt, siehst du auf handball.net im Spielplan der Liga (Datum des ersten Spiels des Spieltags → KW).

Pro Datei:
- Alle Spiele des Spieltags eintragen (mit Mannschaftsnamen, Datum, Halle nur bei TuS-Spielen)
- `toreHeim` und `toreGast` auf `null`
- `status` auf `"scheduled"`

Das ist die meiste Arbeit beim Saisonstart, weil es ~24-26 Dateien pro Mannschaft sind.

> **Tipp:** Wenn du eine bestehende Spieltag-Datei der vorigen Saison als Vorlage nutzt und Mannschaften/Datum anpasst, geht das deutlich schneller.

**4. Leere `pokalspiele.json` und `testspiele.json` anlegen**

Im neuen Saison-Ordner zwei zusätzliche Dateien anlegen:

```json
{
  "aktualisiert": "2026-08-01",
  "spiele": []
}
```

Auch wenn noch keine Pokal- oder Testspiele bekannt sind: Die Dateien sollten von Anfang an existieren (mit leerem `spiele`-Array). So vermeidet die App Fehler beim Laden, und Pfleger wissen, wo sie später Spiele eintragen sollen.

Sobald die ersten Testspiele in der Sommervorbereitung anstehen, werden sie in die `testspiele.json` eingetragen. Pokalauslosung erfolgt meist etwas später im Verband.

**5. `info.json` der Mannschaft aktualisieren**

Die `aktuelleSaison` in der `info.json` umstellen auf die neue Saison – aber **erst, wenn alle Spieltage angelegt sind**. Solange die alte Saison noch laufende Spiele hat, bleibt die alte Saison aktiv.

**6. Kader für die neue Saison prüfen**

Die `kader.json` durchgehen:
- Spieler, die den Verein verlassen haben: entfernen
- Neue Spieler: ergänzen
- Bei allen anderen: `alter` um 1 erhöhen (sofern Geburtstag vor Saisonstart liegt)

**7. Trainingszeiten anpassen**

Wenn sich die Trainingszeiten ändern, `training.json` aktualisieren.

### Reihenfolge der Schritte

Wichtig: Erst alle Inhalte vorbereiten, **dann** die `aktuelleSaison` umstellen. Sonst sehen Nutzer in der App leere Bereiche oder unvollständige Daten.

### Was du **nicht** machen musst

- Eine Tabelle anlegen – die wird automatisch berechnet
- News löschen – alte News bleiben, neue kommen oben drauf
- Sponsoren überarbeiten (nur wenn sich tatsächlich was ändert)

---

## Saisonende: Was passiert mit alten Daten?

Am Ende einer Saison passiert in der App **nichts automatisch**. Die alten Daten bleiben, bis du sie änderst.

### Empfohlenes Vorgehen

**Direkt nach Saisonende:**
- Die letzten Spielergebnisse eintragen
- Eine Saisonabschluss-News schreiben (optional)
- Die Saison-Ordnerstruktur als Vorlage für die nächste Saison nutzen

**Wenn die neue Saison vorbereitet ist:**
- `aktuelleSaison` in `info.json` der Mannschaften auf die neue Saison umstellen
- Die alten Daten bleiben im Repository erhalten

### Archivieren von alten Saisons (optional)

Wenn der `teams/`-Ordner über die Jahre zu voll wird, kannst du alte Saisons in den `data/archive/`-Ordner verschieben:

```
data/archive/2023-24/teams/1-herren/saisons/2023-24/
```

Die App schaut nicht in `archive/` – das ist nur eine Möglichkeit, alte Daten geordnet aufzubewahren, ohne die aktive Struktur zu überladen. Wann das nötig wird, hängt davon ab, wie viele Saisons im aktiven Bereich liegen.

> **Hinweis:** Falls Inhalte aus alten Saisons in der App weiterhin sichtbar sein sollen (z.B. ein „Historische Erfolge"-Bereich), muss das im App-Code zusätzlich umgesetzt werden – sag im Entwickler-Chat Bescheid.

---

## Neue Mannschaft zur App hinzufügen

Wenn eine neue Mannschaft gegründet wird (z.B. 2. Damen kommt dazu), sind folgende Schritte nötig:

### Schritt-für-Schritt

**1. Eintrag in `meta/teams.json` ergänzen**

Neue Mannschaft hinzufügen mit `id`, `name`, `kurzname` und `reihenfolge`.

**2. Neuen Mannschafts-Ordner anlegen**

Unter `data/teams/` einen Ordner mit der gleichen `id` wie in `meta/teams.json` anlegen.

**3. Stammdaten-Dateien anlegen**

In den neuen Ordner mindestens diese Dateien:
- `info.json` (mit `aktuelleSaison`, `ligaTeamName`)
- `kader.json` (kann zunächst nur Trainer enthalten, Spieler werden später ergänzt)
- `training.json` (Trainingszeiten)
- `partner.json` (Sponsoren, kann auch leer beginnen: `"partner": []`)

**4. Saison-Struktur anlegen**

`saisons/<aktuelle-saison>/meta.json` plus mindestens einen ersten Spieltag in `spieltage/01-kwNN.json` (mit der passenden KW als Suffix).

**5. Ergebnis in der App prüfen**

Nach 1-2 Minuten (GitHub Pages braucht Zeit zum Neubau) sollte die neue Mannschaft in der App erscheinen.

### Stolperfallen

- Die `id` in `meta/teams.json` muss **exakt** mit dem Ordnernamen unter `teams/` übereinstimmen
- Die `reihenfolge` muss eindeutig sein (nicht zweimal die gleiche Zahl)
- Bevor die neue Mannschaft live geht, am besten zuerst die nötigsten Inhalte (Kader, mindestens einen Spieltag) anlegen – sonst zeigt die App leere Bereiche

---

## Neuen Sponsor hinzufügen

**Reihenfolge ist hier wichtig:** Erst die Stammdaten im zentralen Sponsoren-Verzeichnis, dann die Zuordnung zu Mannschaft(en).

### Schritt-für-Schritt

**1. Sponsor-Logo in `data/logos-sponsoren/` ablegen**

Die Logo-Datei (PNG oder JPG) ins Verzeichnis `data/logos-sponsoren/` hochladen.

**2. Eintrag in `content/partners.json` anlegen**

Neuen Eintrag mit eindeutiger ID:

```json
"neuer-sponsor": {
  "name": "Neuer Sponsor GmbH",
  "logo": "data/logos-sponsoren/neuer-sponsor.png",
  "url": "https://www.neuer-sponsor.de/"
}
```

**3. Sponsor einer Mannschaft zuordnen**

In `teams/<mannschaft>/partner.json` die neue ID in die `partner`-Liste aufnehmen:

```json
{
  "aktualisiert": "10.05.2026",
  "mannschaft": "1. Herren",
  "partner": ["gebr-schmidt", "krieg", "bayer", "neuer-sponsor"]
}
```

### Stolperfallen

- Die ID in `partners.json` und in `partner.json` muss **exakt** übereinstimmen
- Wenn das Logo fehlt oder unter falschem Pfad liegt, zeigt die App statt des Logos die Initialen des Sponsor-Namens (Fallback)

---

## News-Beitrag veröffentlichen

### Schritt-für-Schritt

**1. `content/news.json` öffnen**

**2. Neuen Eintrag in die `news`-Liste einfügen**

Mit den Pflichtfeldern: `title`, `lead`, `cat`, `author`, `sortDate`, `body`.

Beispiel für eine einfache Vereinsleben-News:

```json
{
  "title": "Saisonabschlussfeier am 14. Juni",
  "lead": "Die 1. Herren feiern den 6. Tabellenplatz mit allen Fans im Vereinsheim.",
  "team": "1. Herren",
  "cat": "vereinsleben",
  "author": "Vorstand TuS Esingen",
  "sortDate": "2026-05-10",
  "body": [
    {
      "type": "text",
      "text": "Nach einer spannenden Saison laden wir alle Mitglieder, Spielerinnen und Fans zum Saisonabschluss ein. Beginn ist um 18:00 Uhr."
    }
  ]
}
```

**3. Bei Top-News: `"topNews": true` ergänzen**

Wenn die News oben groß auf der Startseite erscheinen soll.

**4. `aktualisiert`-Datum auf oberster Ebene aktualisieren**

### Tipps für gute News-Beiträge

- **Title kurz halten:** 4-8 Worte, knackig
- **Lead aussagekräftig:** Wenn jemand nur den Lead liest, soll das wichtigste rüberkommen
- **Body in mehrere Blöcke aufteilen:** Erst Text, dann Score-Box, dann ein Zitat – das wirkt lebendiger als ein langer Textblock
- **Bei Spielberichten:** Score-Block direkt am Anfang, dann Bericht-Text

### Stolperfallen

- `body` ist immer eine Liste mit eckigen Klammern `[ ... ]`, auch wenn nur ein einziger Block drin ist
- `sortDate` ist Pflicht – ohne das Feld erscheint die News in falscher Reihenfolge
- Bei Spielberichten: immer `matchTeam` und `matchDate` setzen, damit die News nicht doppelt erscheint

---

## Was du **nicht** pflegen musst

Damit dir nichts entgeht, hier die Dinge, die **automatisch** passieren – also kein Handlungsbedarf:

| Was | Wie es passiert |
|---|---|
| Liga-Tabelle | Wird live aus den Spielergebnissen berechnet |
| Spielberichte-News | Werden automatisch aus den Spieltagen erzeugt (auch ohne manuelle News) |
| Sortierung der News auf der Startseite | Automatisch nach `sortDate` |
| News-ID, Anzeigedatum, Initialen, Gradient | Werden aus den anderen Feldern abgeleitet |
| App-Update bei Nutzern | Beim nächsten App-Öffnen automatisch |
| Service Worker / Cache | Wird beim Versions-Update automatisch erneuert |

Wenn dir etwas in der App fehlt oder falsch aussieht, prüf zuerst, ob die zugrundeliegende Datei stimmt – meistens reicht das.

---

# GitHub-Crashkurs für Pfleger

Dieser Teil richtet sich an alle, die noch nie oder nur wenig mit GitHub gearbeitet haben. Hier lernst du die wichtigsten Handgriffe, die du für die Datenpflege brauchst – nicht mehr, nicht weniger.

Wenn du tiefer einsteigen willst (z.B. lokale Bearbeitung mit eigenem Editor, Git-Branches, Pull Requests), findest du dazu viele Tutorials online. Für die Daten-Pflege der App reicht das, was hier steht, vollständig aus.

---

## Was ist GitHub eigentlich?

GitHub ist eine Webseite, auf der Code und Dateien gespeichert werden. Für die App-Pflege musst du nur drei Dinge wissen:

1. **Repository** ist der „Container" für alle Dateien der App. Bei uns heißt das Repository `tus-esingen-handball-app`.
2. **Commit** ist eine Speicherung. Jede Änderung wird als Commit festgehalten – mit Datum, Autor und einer kurzen Beschreibung.
3. **GitHub Pages** ist der „Server", auf dem die App live läuft. Sobald du etwas commitest, wird die App automatisch innerhalb von 1-2 Minuten neu gebaut und ist für alle Nutzer aktualisiert.

Das war's. Du brauchst kein lokales Programm zu installieren, keinen Editor zu lernen – alles passiert im Browser.

---

## Vorbereitung

### 1. GitHub-Account anlegen

- Auf [github.com](https://github.com) gehen
- Auf „Sign up" klicken und einen Account anlegen (E-Mail, Passwort, Benutzername wählen)
- E-Mail-Bestätigung per Mail durchführen

### 2. Zugriff auf das Repository

Damit du Dateien bearbeiten kannst, muss dein Account als **Collaborator** zum Repository hinzugefügt werden. Das macht der Admin (FaabNatiC). Sag im Pfleger-Chat Bescheid mit deinem GitHub-Benutzernamen, dann bekommst du eine Einladung.

Sobald du eingeladen bist:
- Auf den Link in der E-Mail klicken
- Auf „Accept invitation" klicken
- Du landest im Repository und kannst nun Dateien bearbeiten

### 3. Repository in den Favoriten / Bookmarks

Direkter Link zum Repository:
```
https://github.com/FaabNatiC/tus-esingen-handball-app
```

Lege dir den als Bookmark an, damit du jede Woche schnell hinkommst.

---

## Die wichtigsten Vorgänge

### Eine Datei öffnen und ansehen

1. Im Repository links die Ordnerstruktur durchklicken (z.B. `data` → `teams` → `1-herren` → `saisons` → `2025-26` → `spieltage` → `25.json`)
2. Du siehst den Datei-Inhalt mit Zeilennummern

In diesem Modus kannst du nichts ändern – nur lesen.

### Eine Datei bearbeiten

1. Datei öffnen (siehe oben)
2. Rechts oben auf das **Bleistift-Symbol** (✏️) klicken
3. Der Editor öffnet sich, du kannst direkt im Text Änderungen vornehmen
4. Wenn fertig: nach unten scrollen zum Commit-Bereich (siehe nächster Abschnitt)

> **Tipp:** Wenn du die Datei nur prüfen willst, ohne zu ändern, klick nicht auf den Bleistift – sondern schließ das Tab einfach. Es passiert nichts.

### Eine Änderung speichern (Commit)

Am Ende des Edit-Modus steht ein Commit-Formular:

1. **Erste Zeile:** Kurze Beschreibung der Änderung (max. ~60 Zeichen)
2. **Optional:** Längere Beschreibung im Textfeld darunter
3. Auf „Commit changes" klicken

**Beispiele für gute Commit-Messages:**

```
Spieltag 25 1. Herren: Ergebnis Esingen vs Fischbek eingetragen
```
```
Tippfehler korrigiert: TSV Ellerbek statt TSV Ellerbeck
```
```
Saisonabschluss-News veröffentlicht
```
```
Neuer Spieler im Kader: Max Mustermann (#22)
```

**Was nicht gut ist:**

```
Update
```
```
asdf
```
```
fixed
```

Gute Commit-Messages helfen dir und den anderen Pflegern, später nachzuvollziehen, was wann geändert wurde.

### Eine neue Datei anlegen

Es gibt zwei Wege:

**Über den „Add file"-Button:**
1. In den Ordner navigieren, wo die neue Datei rein soll
2. Oben rechts auf „Add file" → „Create new file" klicken
3. Dateinamen eingeben (z.B. `26.json`)
4. Inhalt einfügen
5. Commit-Message schreiben, „Commit changes"

**Mit Schrägstrich für neue Ordner:**

Wenn du eine Datei in einem **neuen Ordner** anlegen willst, schreibst du den Ordnernamen einfach in den Dateinamen vor die Datei mit einem Schrägstrich:

```
2026-27/meta.json
```

GitHub erkennt: Hier wird ein neuer Ordner `2026-27/` angelegt mit einer Datei `meta.json` darin.

Mehrere Ebenen geht auch:

```
2026-27/spieltage/01.json
```

→ GitHub legt automatisch beide Ordner an.

### Eine Datei löschen

1. Datei öffnen
2. Rechts oben auf das **Mülleimer-Symbol** klicken (neben dem Bleistift)
3. Commit-Message schreiben, „Commit changes"

> **Vorsicht:** Im Web-Editor gibt es keinen Papierkorb. Eine gelöschte Datei ist über die Git-Historie noch wiederherstellbar, aber das ist nicht trivial. Falls du versehentlich was Wichtiges gelöscht hast, **nicht weiterarbeiten** und im Pfleger-Chat melden.

---

## JSON richtig schreiben

Alle Daten-Dateien in der App sind im JSON-Format. JSON hat ein paar Regeln, die wichtig sind – Tippfehler hier sind die häufigste Ursache für Probleme.

### Die Regeln auf einen Blick

**1. Strings stehen immer in doppelten Anführungszeichen**

✅ Richtig: `"name": "Fabian Wurl"`
❌ Falsch: `name: Fabian Wurl`
❌ Falsch: `'name': 'Fabian Wurl'` (einfache Anführungszeichen)

**2. Zahlen stehen ohne Anführungszeichen**

✅ Richtig: `"toreHeim": 28`
❌ Falsch: `"toreHeim": "28"` (das wäre ein String, kein Zahl-Wert)

**3. Wahrheitswerte: `true` und `false` ohne Anführungszeichen**

✅ Richtig: `"topNews": true`
❌ Falsch: `"topNews": "true"`

**4. Leere Werte: `null` ohne Anführungszeichen**

✅ Richtig: `"toreHeim": null`
❌ Falsch: `"toreHeim": "null"`

**5. Kommas trennen Einträge – aber kein Komma nach dem letzten Eintrag**

✅ Richtig:
```json
{
  "name": "Fabian",
  "alter": 32
}
```

❌ Falsch (Komma nach dem letzten Eintrag):
```json
{
  "name": "Fabian",
  "alter": 32,
}
```

**6. Geschwungene Klammern `{ }` umschließen Objekte, eckige Klammern `[ ]` umschließen Listen**

```json
{
  "trainer": [
    { "name": "Fabian", "alter": 32 },
    { "name": "Yannick", "alter": 31 }
  ]
}
```

### Validität prüfen

Wenn du nicht sicher bist, ob deine JSON-Datei korrekt ist:

1. Den kompletten Inhalt kopieren
2. Auf [jsonlint.com](https://jsonlint.com) einfügen
3. Auf „Validate JSON" klicken

Wenn es Fehler gibt, zeigt die Seite genau die Zeile an, in der etwas nicht stimmt.

> **Wichtig:** Validität immer **vor dem Commit** prüfen. Wenn eine kaputte JSON-Datei live geht, kann die App diese Datei nicht mehr lesen und zeigt eventuell leere Bereiche.

---

## Häufige Fehler und ihre Bedeutung

### „Unable to load data" oder leerer Bereich in der App

**Mögliche Ursachen:**
- Eine JSON-Datei ist syntaktisch kaputt (Komma vergessen, Anführungszeichen falsch)
- Eine Datei wurde versehentlich gelöscht
- Ein Pfad in einer Datei verweist auf etwas, das nicht existiert

**Vorgehen:**
1. Im Repository die zuletzt geänderten Dateien prüfen
2. Auf [jsonlint.com](https://jsonlint.com) durchchecken
3. Falls unklar: Im Pfleger-Chat melden

### Logo wird nicht angezeigt

**Mögliche Ursachen:**
- Der Dateiname im JSON stimmt nicht mit der echten Datei überein (z.B. Tippfehler oder falsche Endung)
- Das Logo liegt nicht im richtigen Verzeichnis

**Vorgehen:**
- Prüfen, ob die Logo-Datei wirklich unter `data/logos-sponsoren/` oder `data/logos-mannschaften/` liegt
- Dateiname auf Groß-/Kleinschreibung prüfen (`Logo.PNG` ≠ `logo.png`)

### Mannschaft taucht nicht in der Tabelle auf

**Mögliche Ursache:**
- Der Name der Mannschaft in den Spieltag-Dateien stimmt nicht **exakt** mit dem Namen in `meta.json` der Saison überein
- Auch ein einzelnes Leerzeichen oder ein Tippfehler reicht aus

**Vorgehen:**
- Beide Stellen vergleichen (Spielname in `spieltage/XX-kwNN.json` und in `meta.json`)
- Schreibweise angleichen

### Punktestand stimmt nicht

**Mögliche Ursache:**
- Ein Spiel hat `status: "scheduled"`, obwohl es schon gespielt wurde
- Bei einer Wertung wurde `status: "finished"` gesetzt statt `"wertung-heim"` / `"wertung-gast"`

**Vorgehen:**
- Alle Spiele der Saison durchgehen und Status prüfen

---

## Wie sehe ich, dass mein Commit live ist?

Nach einem Commit dauert es ein paar Minuten, bis die Änderung in der App sichtbar ist. So kannst du den Fortschritt verfolgen:

### Im Repository

- Auf der Hauptseite des Repositories ganz oben siehst du die zuletzt committeten Änderungen mit Datum und Uhrzeit
- Im Tab „Actions" siehst du den GitHub-Pages-Build-Prozess: gelber Punkt = läuft, grünes Häkchen = fertig, rotes Kreuz = Fehler

### In der App

- Öffne die App im Browser (am besten in einem Inkognito-Fenster, damit kein alter Cache stört)
- Beim nächsten Öffnen siehst du deine Änderung

Wenn du **schon eine installierte App** auf dem Handy hast: Beim nächsten Öffnen merkt die App, dass eine neue Version da ist, und lädt sie nach. Das kann ein paar Sekunden dauern.

---

## Konflikte: Wenn zwei Pfleger gleichzeitig editieren

Es kann passieren, dass zwei Pfleger zur gleichen Zeit dieselbe Datei bearbeiten. GitHub fängt das ab und zeigt eine **Merge-Konflikt-Warnung**, wenn der zweite seinen Commit absenden will.

### Vorgehen bei Konflikten

Über den Web-Editor sind Merge-Konflikte schwer aufzulösen. Wenn das passiert:

1. **Nichts speichern, nicht in Panik geraten**
2. Im Pfleger-Chat melden
3. Mit dem anderen Pfleger absprechen, wer welche Änderung übernimmt

### Konflikte vermeiden

Die einfachste Lösung: Klare Aufgabenverteilung. Beispiel:

- Pfleger A pflegt die Herren-Mannschaften
- Pfleger B pflegt die Damen-Mannschaften
- Pfleger C pflegt die Jugend-Mannschaften

Wenn ihr außerdem grob zur gleichen Uhrzeit pflegt (z.B. Sonntagabend ab 20 Uhr) und kurz im Pfleger-Chat ankündigt, was ihr gerade macht („Ich starte mit den Herren"), sind Konflikte praktisch ausgeschlossen.

---

## Was tun, wenn was schiefgeht?

Manchmal merkst du nach einem Commit, dass die App nicht mehr richtig funktioniert. Keine Panik – kein Schaden ist endgültig.

### Sofort-Maßnahme: Den Commit rückgängig machen

1. Im Repository auf „Commits" gehen (oben rechts, neben dem Branch-Selector)
2. Den problematischen Commit finden
3. Auf den Commit klicken
4. Rechts oben auf „Revert" – das erzeugt einen neuen Commit, der die alte Änderung rückgängig macht

Wenn du dir unsicher bist, ob du den richtigen Commit revertest – **lieber im Pfleger-Chat fragen**, statt blind weiterzuklicken.

### Wenn die App ganz kaputt ist

Sofort im Entwickler-Chat melden mit:
- Was hast du zuletzt geändert?
- Wann (ungefähr) war das?
- Was siehst du in der App?

Der Entwickler kann dann zur letzten funktionierenden Version zurückrollen.

---

## Weiterführende Links

- **GitHub Docs für Web-Editor:** [docs.github.com/en/repositories](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)
- **JSON-Validator:** [jsonlint.com](https://jsonlint.com)
- **Markdown-Spickzettel** (für News-Texte mit Formatierung): [markdownguide.org/cheat-sheet](https://www.markdownguide.org/cheat-sheet/)

---

# Letzte Hinweise

## Wer hat Zugriff auf was?

| Rolle | Was sie tun |
|---|---|
| **Pfleger** (du) | Daten bearbeiten, Spielergebnisse eintragen, News schreiben |
| **Admin** (FaabNatiC) | Neue Pfleger einladen, Repository-Struktur ändern |
| **Entwickler** (FaabNatiC) | App-Code anpassen, neue Features hinzufügen |

Aktuell sind Admin und Entwickler dieselbe Person. Wenn du nicht weißt, ob etwas Pfleger- oder Entwickler-Arbeit ist – frag im Chat.

## Wo bekomme ich Hilfe?

**Bei Fragen zur Datenpflege:**
- Im Pfleger-Chat (WhatsApp / Signal / Slack – je nach Vereinbarung)
- Bei akuten Problemen: direkt FaabNatiC anrufen

**Bei Bugs in der App:**
- Im Entwickler-Chat melden
- In der App auf den Daumen-runter-Button bei „App-Updates" tippen (falls verfügbar)

## Vorschläge zur Anleitung

Diese Anleitung wird mit der Zeit besser. Wenn dir etwas unklar ist oder ein Workflow nicht beschrieben ist – **sag Bescheid**. Wir können hier jederzeit etwas ergänzen oder umformulieren.

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

Wenn du nur schnell ein Spielergebnis nachtragen willst, springe direkt zum Kapitel **„Wöchentliche Pflege: Spielergebnisse eintragen"** (kommt in einer späteren Etappe).

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
│   │   ├── sonderspiele.json      ← Pokal- und Testspiele
│   │   └── saisons/
│   │       ├── 2025-26/           ← ein Ordner pro Saison
│   │       │   ├── meta.json      ← Liga-Info, Mannschaftsliste
│   │       │   └── spieltage/
│   │       │       ├── 01.json    ← Spieltag 1 mit allen Spielen
│   │       │       ├── 02.json    ← Spieltag 2
│   │       │       └── ...
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
├── 2025-26/           ← Saison 2025/26
│   ├── meta.json      ← Liga-Info dieser Saison
│   └── spieltage/
│       ├── 01.json
│       ├── 02.json
│       └── ...
└── 2026-27/           ← Saison 2026/27
    └── ...
```

**Wichtig:** In der App wird immer nur eine Saison angezeigt – die „aktuelle Saison". Welche das ist, steht in der `info.json` der Mannschaft. Du kannst eine neue Saison schon vorbereiten, ohne dass sie sofort live geht.

---

## Wo finde ich was?

| Du willst… | Datei |
|---|---|
| ein Spielergebnis eintragen | `teams/<mannschaft>/saisons/<saison>/spieltage/<XX>.json` |
| einen Pokalspiel-Termin nachtragen | `teams/<mannschaft>/sonderspiele.json` |
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

### Beispiel (eine einfache News + eine mit Score-Box)

```json
{
  "aktualisiert": "10.05.2026",
  "news": [
    {
      "id": "saisonabschluss-2025-26",
      "title": "Saisonabschlussfeier am 14. Juni",
      "lead": "Die 1. Herren feiern den 6. Tabellenplatz mit allen Fans im Vereinsheim.",
      "team": "1. Herren",
      "cat": "vereinsleben",
      "catCl": "cat-vereinsleben",
      "gradient": "linear-gradient(135deg, #1a1a1a 0%, #444 100%)",
      "author": "Vorstand TuS Esingen",
      "authorIni": "TuS",
      "date": "10. Mai 2026",
      "sortDate": "2026-05-10",
      "topNews": false,
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
    },
    {
      "id": "sieg-uetersen-25-04",
      "title": "Wichtiger Sieg gegen Uetersen",
      "lead": "Die 1. Herren gewinnen souverän mit 30:27 in Uetersen.",
      "team": "1. Herren",
      "cat": "spielbericht",
      "catCl": "cat-spielbericht",
      "gradient": "linear-gradient(135deg, #1a1a1a 0%, #2d4f10 60%, #639922 100%)",
      "author": "Fabian Wurl",
      "authorIni": "FW",
      "date": "26. April 2026",
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
  ]
}
```

### Felder auf oberster Ebene

| Feld | Pflicht | Beschreibung |
|---|---|---|
| `aktualisiert` | ja | Datum der letzten Änderung |
| `news` | ja | Liste aller News-Einträge (kann leer sein: `[]`) |

### Pro News-Eintrag

| Feld | Pflicht | Beschreibung |
|---|---|---|
| `id` | ja | Eindeutige ID dieser News (Kurz-Slug, z.B. `"saisonabschluss-2025-26"`) |
| `title` | ja | Hauptüberschrift der News |
| `lead` | ja | Kurzer einleitender Satz (1-2 Zeilen), wird unter dem Titel angezeigt |
| `team` | nein | Zugehörige Mannschaft (z.B. `"1. Herren"`). Wird als Tag angezeigt. |
| `cat` | ja | Kategorie der News (siehe Tabelle unten) |
| `catCl` | ja | CSS-Klasse zur Kategorie (siehe Tabelle unten) |
| `gradient` | ja | CSS-Farbverlauf für das Hero-Bild |
| `author` | ja | Anzeigename des Autors |
| `authorIni` | ja | Initialen des Autors (max. 3 Zeichen) oder `"TuS"` für das Vereinslogo |
| `date` | ja | Anzeigedatum auf Deutsch (z.B. `"26. April 2026"`) |
| `sortDate` | ja | Sortierdatum im Format `YYYY-MM-DD` (für korrekte Reihenfolge) |
| `topNews` | nein | `true` = wird ganz oben groß als Top-News angezeigt |
| `matchTeam` | nein | Bei Spielberichten: Mannschafts-ID (z.B. `"1-herren"`). Verhindert doppelte News. |
| `matchDate` | nein | Bei Spielberichten: Spieldatum (Format `YYYY-MM-DD`) |
| `body` | ja | Liste aller Inhalts-Blöcke der News (siehe unten) |

### Mögliche Kategorien

| `cat` | `catCl` | Bedeutung |
|---|---|---|
| `spielbericht` | `cat-spielbericht` | Bericht über ein gespieltes Match |
| `vereinsleben` | `cat-vereinsleben` | Veranstaltungen, Feiern, Termine |
| `transfer` | `cat-transfer` | Spieler-Wechsel, neue Trainer |
| `ankuendigung` | `cat-ankuendigung` | Wichtige Mitteilungen |

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

Mögliche `outcome`-Werte: `"Sieg"`, `"Niederlage"`, `"Unentschieden"` (aus TuS-Sicht). Bestimmt die Hintergrundfarbe der Score-Box.

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
- **News korrigieren:** Eintrag mit derselben `id` bearbeiten
- **News löschen:** Eintrag aus der Liste entfernen

### Stolperfallen

- `sortDate` ist Pflicht – ohne dieses Feld wird die News falsch einsortiert
- `id` muss **eindeutig** sein – keine zwei News mit derselben ID
- `body` ist immer eine **Liste**, auch wenn nur ein Text-Block drin ist
- Bei `matchTeam`: ID exakt wie in `meta/teams.json` (z.B. `"1-herren"`, nicht `"1. Herren"`)
- `gradient` ist CSS-Code – wenn unsicher, kopier den aus einer anderen News

---

## `content/partners.json` – Hauptsponsoren

In dieser Datei stehen die **Stammdaten** aller Sponsoren des Vereins. Sie wird sowohl für die Hauptsponsoren auf der Startseite als auch von den Mannschafts-Sponsoren (`teams/<id>/partner.json`) verwendet.

### Beispiel

```json
{
  "aktualisiert": "10.05.2026",
  "stadtwerke-suedholstein": {
    "name": "Stadtwerke Südholstein",
    "logo": "data/logos/stadtwerke.jpg",
    "url": "https://www.sw-suedholstein.de/"
  },
  "gebr-schmidt": {
    "name": "Gebr. Schmidt GmbH",
    "logo": "data/logos/schmidt.png",
    "url": "https://www.gebr-schmidt.de/"
  },
  "krieg": {
    "name": "Bauunternehmen Krieg",
    "logo": "data/logos/krieg.png",
    "url": "https://www.bauunternehmen-krieg.de/"
  },
  "bayer": {
    "name": "Bayer AG",
    "logo": "data/logos/bayer.png",
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
- `logo` ist ein Pfad **innerhalb des Repos**, nicht eine externe URL. Die Logodatei muss vorher in `data/logos/` abgelegt werden.
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

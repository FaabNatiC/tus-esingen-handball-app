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

## Was kommt als Nächstes in dieser Anleitung?

In den folgenden Kapiteln geht es Schritt für Schritt um die einzelnen Dateien und Workflows:

- **Jede Datei im Detail** – welche Felder gibt es, was ist Pflicht, was ist optional
- **Wöchentliche Spieltag-Pflege** – der häufigste Vorgang
- **Saisonstart** – neue Saison anlegen
- **Sonderfälle** – Verlegungen, Wertungen, Korrekturen
- **GitHub-Crashkurs** – wie du Dateien im Browser bearbeitest

Diese Kapitel werden Stück für Stück in dieser Datei ergänzt.

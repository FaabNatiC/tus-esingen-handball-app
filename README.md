# TuS Esingen Handball App

Eine Progressive Web App (PWA) für den TuS Esingen Handball – mit Spielplänen, Tabellen, Mannschaftsinfos, News und vielem mehr.

🌐 **Live-App:** [faabnatic.github.io/tus-esingen-handball-app](https://faabnatic.github.io/tus-esingen-handball-app/)

> 📝 **Du möchtest Spielergebnisse, News oder Termine pflegen?**
> → Die Anleitung dafür findest du unter [`data/README.md`](data/README.md).
> Du brauchst dafür keine Programmierkenntnisse.

---

## Inhalt dieser Anleitung

Diese Datei ist die **technische Dokumentation** der App – sie richtet sich an Entwickler und an die Person, die das Repository administriert.

Die folgenden Kapitel sind enthalten:

- **PWA-Paket** – aus welchen Dateien die App besteht
- **GitHub-Repo aufsetzen** – wie die nötigen Dateien ins Repository kommen
- **Installation auf Endgeräten** – wie Nutzer die App auf Android und iPhone installieren
- **Was die App zusätzlich kann** – Vollbild, Offline-Modus, Auto-Updates
- **Bei Updates an der App** – wie du eine neue Version veröffentlichst
- **Testen der PWA-Funktionalität** – wie du prüfst, ob alles korrekt aufgesetzt ist
- **Eigene Domain einrichten** – optional, falls die App später unter `app.tus-esingen.de` erreichbar sein soll

---

# PWA-Paket für TuS Esingen Handball App

Dieses Paket macht aus der Web-App eine **Progressive Web App** (PWA).
Vereinsmitglieder können die App dann auf den Homescreen ihres Handys legen
und sie verhält sich wie eine echte App (Vollbild, Offline-Modus, eigenes Icon).

## Was ist im Paket?

```
pwa-paket/
├── index.html              ← angepasste Version (PWA-Tags + Service Worker)
├── manifest.json           ← App-Beschreibung (Name, Icon, Farben)
├── sw.js                   ← Service Worker (Offline + Caching)
└── icons/
    ├── icon-192.png        ← Android Homescreen
    ├── icon-512.png        ← Splash Screen, hochauflösend
    └── apple-touch-icon.png ← iPhone Homescreen (180×180)
```

## Was musst du im GitHub-Repo tun?

1. **Die alte `index.html` ersetzen** mit der neuen aus diesem Paket
2. **Folgende neue Dateien hochladen** (in den Hauptordner):
   - `manifest.json`
   - `sw.js`
3. **Den Ordner `icons/`** komplett ins Hauptverzeichnis legen
   (mit den 3 PNG-Dateien drin)

Die Struktur im Repo sieht danach so aus:

```
tus-esingen-handball-app/
├── index.html
├── manifest.json
├── sw.js
├── icons/
│   ├── icon-192.png
│   ├── icon-512.png
│   └── apple-touch-icon.png
├── data/                   ← Alle App-Inhalte (siehe data/README.md)
│   └── ...
└── README.md               ← Diese Datei
```

4. **Committen und pushen** → GitHub Pages baut automatisch neu.

## Wie installieren Nutzer die App?

### Android (Chrome / Edge)
1. App-URL im Browser öffnen
2. Es erscheint automatisch ein Banner "Zum Startbildschirm hinzufügen"
3. Tippen → fertig. App-Icon liegt auf dem Homescreen.

Falls kein Banner erscheint:
- Menü (3 Punkte) → "App installieren" oder "Zum Startbildschirm hinzufügen"

### iPhone (Safari, Chrome, Edge, Firefox)
1. App-URL im Browser öffnen
2. Teilen-Button antippen (das Quadrat mit Pfeil nach oben)
   - In **Safari**: unten in der Mitte
   - In **Chrome**: rechts in der Adressleiste
   - In **Edge / Firefox**: im Menü
3. "Zum Home-Bildschirm" auswählen
4. Bestätigen → App-Icon erscheint auf dem Homescreen

## Was macht die App zusätzlich?

- ✅ **Vollbild-Modus** ohne Browser-Leiste
- ✅ **Offline nutzbar** – einmal geladene Seiten funktionieren ohne Empfang
- ✅ **Schneller** – Dateien werden lokal gecached
- ✅ **Eigenes Icon** auf dem Homescreen
- ✅ **Auto-Updates** – wenn du etwas änderst und pushst, holt sich die App
  beim nächsten Öffnen automatisch die neue Version

## Bei Updates an der App

Wenn du Änderungen an `index.html`, `manifest.json` oder den Icons machst:

1. In `index.html` die `APP_VERSION` erhöhen (z.B. `"0.6.21"`)
   ```js
   const APP_VERSION = "0.6.21";  // war vorher 0.6.20
   ```
2. Committen und pushen
3. Beim nächsten Öffnen der App holen sich Nutzer automatisch die neue Version

**Die `sw.js` musst du nicht mehr anfassen** – sie liest die Cache-Version automatisch aus der App-Version aus. Du musst sie nur einmalig im Repo haben.

Wenn du das `APP_VERSION`-Update vergisst, sehen Nutzer evtl. noch die alte Version aus dem Cache.

**Hinweis:** App-Icons werden von iOS sehr aggressiv gecached. Wenn das Icon
geändert wurde, müssen Nutzer die App vom Homescreen löschen und neu hinzufügen,
damit das neue Icon erscheint.

## Testen der PWA-Funktionalität

1. App-URL im Chrome auf dem Desktop öffnen
2. F12 drücken → "Application" Tab → links auf "Manifest"
3. Dort sollten alle Werte korrekt angezeigt werden
4. Unter "Service Workers" sollte der SW als "activated and running" stehen
5. Im "Lighthouse" Tab → "Progressive Web App" auswählen → Audit starten
   → Sollte 100/100 oder nahe dran erreichen

## Eigene Domain einrichten (optional)

Wenn du später `app.tus-esingen.de` statt der GitHub-URL haben willst:
1. Domain bei einem Provider registrieren (z.B. IONOS, Strato)
2. Im Repo eine `CNAME`-Datei mit `app.tus-esingen.de` als einzigen Inhalt anlegen
3. Bei deinem Domain-Provider einen CNAME-Eintrag auf `faabnatic.github.io` setzen
4. In GitHub Pages Settings die Custom Domain eintragen

---

## Verwandte Dokumentation

- [`data/README.md`](data/README.md) – Anleitung für Pfleger (Spielergebnisse, News, Termine)

# PWA-Paket für TuS Esingen Handball App

Dieses Paket macht aus deiner App eine **Progressive Web App** (PWA).
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
├── manifest.json           ← NEU
├── sw.js                   ← NEU
├── icons/                  ← NEU
│   ├── icon-192.png
│   ├── icon-512.png
│   └── apple-touch-icon.png
├── data/                   ← bestehend
│   └── ...
└── ...
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

## Was macht die App jetzt zusätzlich?

- ✅ **Vollbild-Modus** ohne Browser-Leiste
- ✅ **Offline nutzbar** – einmal geladene Seiten funktionieren ohne Empfang
- ✅ **Schneller** – Dateien werden lokal gecached
- ✅ **Eigenes Icon** auf dem Homescreen
- ✅ **Auto-Updates** – wenn du etwas änderst und pushst, holt sich die App
  beim nächsten Öffnen automatisch die neue Version

## Bei Updates an der App

Wenn du später Änderungen an `index.html`, `sw.js`, `manifest.json` oder den Icons machst:

1. In `index.html` die `APP_VERSION` erhöhen (z.B. `"0.1.7"`)
   ```js
   const APP_VERSION = "0.1.7";  // war vorher 0.1.6
   ```
2. In `sw.js` die `CACHE_VERSION` erhöhen (z.B. `'v30'`)
   ```js
   const CACHE_VERSION = 'v30';  // war vorher v29
   ```
3. Committen und pushen
4. Beim nächsten Öffnen der App holen sich Nutzer automatisch die neue Version

Wenn du das vergisst, sehen Nutzer evtl. noch die alte Version aus dem Cache.

**Hinweis:** App-Icons werden von iOS sehr aggressiv gecached. Wenn das Icon
geändert wurde, müssen Nutzer die App vom Homescreen löschen und neu hinzufügen,
damit das neue Icon erscheint.

## Testen, ob es funktioniert

1. App-URL im Chrome auf dem Desktop öffnen
2. F12 drücken → "Application" Tab → links auf "Manifest"
3. Dort sollten alle Werte korrekt angezeigt werden
4. Unter "Service Workers" sollte der SW als "activated and running" stehen
5. Im "Lighthouse" Tab → "Progressive Web App" auswählen → Audit starten
   → Sollte 100/100 oder nahe dran erreichen

## Eigene Domain (optional, später)

Wenn du später `app.tus-esingen.de` statt der GitHub-URL haben willst:
1. Domain bei einem Provider registrieren (z.B. IONOS, Strato)
2. Im Repo eine `CNAME`-Datei mit `app.tus-esingen.de` als einzigen Inhalt anlegen
3. Bei deinem Domain-Provider einen CNAME-Eintrag auf `faabnatic.github.io` setzen
4. In GitHub Pages Settings die Custom Domain eintragen

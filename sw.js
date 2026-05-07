// TuS Esingen Handball App - Service Worker
// Version bei Updates erhöhen, damit Browser den Cache aktualisiert
const CACHE_VERSION = 'v24';
const CACHE_NAME = `tus-esingen-${CACHE_VERSION}`;

// Dateien, die beim Installieren in den Cache wandern (App-Shell)
const APP_SHELL = [
  './',
  './index.html',
  './manifest.json',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/apple-touch-icon.png'
];

// Install: App-Shell cachen, sofort aktiv werden
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(APP_SHELL))
      .then(() => self.skipWaiting())
  );
});

// Activate: Alle alten Caches löschen, sofort übernehmen
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(
        keys.filter(key => key !== CACHE_NAME)
            .map(key => caches.delete(key))
      )
    ).then(() => self.clients.claim())
  );
});

// Fetch: Strategie je nach Anfrage
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);

  // Nur GET-Requests behandeln
  if (event.request.method !== 'GET') return;

  // Externe APIs (handball.net etc.): Network-First mit Cache-Fallback
  if (url.origin !== location.origin) {
    event.respondWith(
      fetch(event.request)
        .then(response => {
          if (response.ok) {
            const responseClone = response.clone();
            caches.open(CACHE_NAME).then(cache =>
              cache.put(event.request, responseClone)
            );
          }
          return response;
        })
        .catch(() => caches.match(event.request))
    );
    return;
  }

  // HTML-Dateien (index.html, '/', navigation): NETWORK-FIRST
  // Damit Updates SOFORT sichtbar sind, nicht erst nach Tagen
  const isHTML = event.request.mode === 'navigate' ||
                 event.request.destination === 'document' ||
                 url.pathname.endsWith('.html') ||
                 url.pathname === '/' ||
                 url.pathname.endsWith('/');

  if (isHTML) {
    event.respondWith(
      fetch(event.request, { cache: 'no-store' })
        .then(response => {
          if (response.ok) {
            const responseClone = response.clone();
            caches.open(CACHE_NAME).then(cache =>
              cache.put(event.request, responseClone)
            );
          }
          return response;
        })
        .catch(() => caches.match(event.request).then(c => c || caches.match('./index.html')))
    );
    return;
  }

  // Andere eigene Dateien (JS, CSS, Bilder, Icons): Cache-First mit Update im Hintergrund
  event.respondWith(
    caches.match(event.request).then(cached => {
      const fetchPromise = fetch(event.request).then(response => {
        if (response.ok) {
          const responseClone = response.clone();
          caches.open(CACHE_NAME).then(cache =>
            cache.put(event.request, responseClone)
          );
        }
        return response;
      }).catch(() => cached);

      return cached || fetchPromise;
    })
  );
});

// Nachricht-Handler: Erlaubt der App, ein sofortiges Update zu erzwingen
self.addEventListener('message', event => {
  if (event.data === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});

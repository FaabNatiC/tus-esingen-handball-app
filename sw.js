// TuS Esingen Handball App - Service Worker
// Version bei Updates erhöhen, damit Browser den Cache aktualisiert
const CACHE_VERSION = 'v2';
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

// Install: App-Shell cachen
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(APP_SHELL))
      .then(() => self.skipWaiting())
  );
});

// Activate: Alte Caches löschen
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

  // handball.net und andere externe APIs: Network-First
  // (immer aktuelle Daten holen, Cache nur als Fallback)
  if (url.origin !== location.origin) {
    event.respondWith(
      fetch(event.request)
        .then(response => {
          // Erfolgreiche Antworten cachen für Offline-Fallback
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

  // Eigene Dateien: Cache-First, im Hintergrund Update
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

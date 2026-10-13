// Kurs – service worker: apka startuje i działa bez internetu (roaming, słaby zasięg).
// Strona: najpierw sieć (świeża wersja), po 2,5 s lub offline – kopia z pamięci.
// Pliki statyczne: z pamięci, w tle odświeżane. Kursy walut (inne domeny) idą bez pośrednictwa.
const V = 'kurs-v8';
const SHELL = ['./', 'index.html', 'manifest.json', 'apple-touch-icon.png?v=2', 'icon-192.png', 'icon-512.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(V).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys()
    .then(keys => Promise.all(keys.filter(k => k !== V).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});

function timeout(ms) { return new Promise((_, rej) => setTimeout(() => rej(new Error('timeout')), ms)); }

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;

  if (req.mode === 'navigate') {
    e.respondWith(
      Promise.race([fetch(req), timeout(2500)])
        .then(res => {
          if (res && res.ok) { const copy = res.clone(); caches.open(V).then(c => c.put('index.html', copy)); }
          return res;
        })
        .catch(() => caches.match('index.html').then(r => r || caches.match('./')))
    );
    return;
  }

  e.respondWith(
    caches.match(req).then(hit => {
      const net = fetch(req).then(res => {
        if (res && res.ok) { const copy = res.clone(); caches.open(V).then(c => c.put(req, copy)); }
        return res;
      }).catch(() => hit);
      return hit || net;
    })
  );
});

// File: public/sw.js
// Mo ta: Service Worker ho tro truy cap va luu cache ngoai tuyen (Offline PWA) cho Sieu Club Hoc Tap v28.0 (Loai bo badge PLAYLIST 1/11 giup giao dien am thanh sieu toi gian va dep mat)

const CACHE_NAME = 'sieu-club-hoc-tap-v28.0';
const ASSETS_TO_CACHE = [
    './',
    './index.html'
];

// Su kien cai dat Service Worker va luu tai nguyen vao cache
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(ASSETS_TO_CACHE);
        })
    );
    self.skipWaiting();
});

// Su kien khich hoat Service Worker va dón dep cache cu
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((cache) => {
                    if (cache !== CACHE_NAME) {
                        return caches.delete(cache);
                    }
                })
            );
        })
    );
    self.clients.claim();
});

// Su kien truy van tai nguyen: Network First
self.addEventListener('fetch', (event) => {
    event.respondWith(
        fetch(event.request)
            .then((response) => {
                if (response && response.status === 200 && event.request.method === 'GET') {
                    const responseClone = response.clone();
                    caches.open(CACHE_NAME).then((cache) => {
                        cache.put(event.request, responseClone);
                    });
                }
                return response;
            })
            .catch(() => {
                return caches.match(event.request).then((cachedResponse) => {
                    if (cachedResponse) {
                        return cachedResponse;
                    }
                    if (event.request.headers.get('accept') && event.request.headers.get('accept').includes('text/html')) {
                        return caches.match('./index.html');
                    }
                });
            })
    );
});

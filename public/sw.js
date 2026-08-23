// File: public/sw.js
// Mo ta: Service Worker TURBO toc do sieu toc v39.0 (Khoi dau 5 Ve Vang, het ve lam nhiem vu nhan them)

const CACHE_NAME = 'sieu-club-hoc-tap-v39.0-initial-5-golden-tickets-mission-system';
const ASSETS_TO_PRECACHE = [
    './',
    './index.html',
    './xu_ly_3d/khong_gian_nen_3d.js',
    './xu_ly_3d/linh_vat_3d_moi.js',
    './xu_ly_3d/vong_quay_3d_moi.js',
    './xu_ly_3d/gap_thu_3d_moi.js',
    './xu_ly_3d/san_bong_3d_moi.js',
    './xu_ly_3d/dau_truong_c1_3d.js',
    './xu_ly_3d/dua_xe_3d.js',
    './xu_ly_3d/parkour_obby_3d.js',
    './hinh_anh_3d/linh_vat_3d.png',
    './hinh_anh_3d/roblox_anh_dai_dien_3d.png'
];

// 1. Cai dat va Precache toan bo tai nguyen sieu toc
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(ASSETS_TO_PRECACHE).catch((err) => {
                console.warn("Precache non-critical item warning:", err);
            });
        })
    );
    self.skipWaiting();
});

// 2. Kich hoat va don dep cache cu
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

// 3. Chien luoc TURBO: Cache-First cho Static Assets & Stale-While-Revalidate cho Data
self.addEventListener('fetch', (event) => {
    const url = new URL(event.request.url);

    // Bo qua non-GET
    if (event.request.method !== 'GET') {
        return;
    }

    // Neu la Static Assets (Scripts, CSS, Images, HTML): Tra ve Cache ngay lap tuc (0ms)
    event.respondWith(
        caches.match(event.request).then((cachedResponse) => {
            if (cachedResponse) {
                // Fetch ngam de cap nhat cache lan sau (Stale-While-Revalidate)
                fetch(event.request).then((networkResponse) => {
                    if (networkResponse && networkResponse.status === 200) {
                        caches.open(CACHE_NAME).then((cache) => {
                            cache.put(event.request, networkResponse);
                        });
                    }
                }).catch(() => {});
                return cachedResponse;
            }

            // Neu chua co trong cache -> Fetch tu mang va luu vao cache
            return fetch(event.request).then((networkResponse) => {
                if (networkResponse && networkResponse.status === 200) {
                    const responseClone = networkResponse.clone();
                    caches.open(CACHE_NAME).then((cache) => {
                        cache.put(event.request, responseClone);
                    });
                }
                return networkResponse;
            }).catch(() => {
                if (event.request.headers.get('accept') && event.request.headers.get('accept').includes('text/html')) {
                    return caches.match('./index.html');
                }
            });
        })
    );
});

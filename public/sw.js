// File: public/sw.js
// Mo ta: Service Worker TURBO toc do sieu toc - Bo nho dem offline tuc thi

const CACHE_NAME = 'sieu-club-hoc-tap-v58.0-football-edition';
const ASSETS_TO_PRECACHE = [
    './',
    './index.html',
    './xu_ly_bong_da/bong_da_dinh_cao.js',
    './xu_ly_3d/khong_gian_nen_3d.js',
    './xu_ly_3d/linh_vat_3d.js',
    './xu_ly_3d/vong_quay_3d.js',
    './xu_ly_3d/vong_quay_3d_moi.js',
    './xu_ly_3d/gap_thu_3d_moi.js',
    './xu_ly_3d/dua_xe_3d.js',
    './xu_ly_3d/cup_vo_dich_3d.js',
    './hinh_anh_3d/linh_vat_3d.png',
    './hinh_anh_3d/roblox_anh_dai_dien_3d.png',
    './hinh_anh_3d/anh_dai_dien_3d.png',
    './hinh_anh_3d/roblox_linh_vat_3d.png',
    './hinh_anh_3d/cup_world_cup_3d.png',
    './hinh_anh_3d/cup_c1_champions_league_3d.png',
    './hinh_anh_3d/trang_chao_mung_3d.png'
];

// 1. Cai dat va Precache toan bo tai nguyen sieu toc
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(ASSETS_TO_PRECACHE).catch((err) => {
                console.warn("Precache warning:", err);
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
    if (event.request.method !== 'GET') {
        return;
    }

    event.respondWith(
        caches.match(event.request).then((cachedResponse) => {
            if (cachedResponse) {
                // Fetch ngam de cap nhat cache cho lan truy cap tiep theo
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

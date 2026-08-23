// File: public/xu_ly_3d/khong_gian_nen_3d.js
// Mo ta: Xu ly hieu ung khong gian san van dong bong da 3D va qua bong da phat sang phia sau di chuyen tuong tac theo chuot

let bgScene, bgCamera, bgRenderer;
let bgMeshGroup = [];
let bgPointLight1, bgPointLight2, bgPointLight3;
let mouseX = 0, mouseY = 0;
let targetCameraX = 0, targetCameraY = 0;

function khoi_tao_khong_gian_nen_3d() {
    const canvas = document.getElementById('bg3dCanvas');
    if (!canvas || typeof THREE === 'undefined') return;

    bgScene = new THREE.Scene();
    bgCamera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
    bgCamera.position.z = 32;

    bgRenderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
    bgRenderer.setSize(window.innerWidth, window.innerHeight);
    bgRenderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    // Anh sang den pha san van dong
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
    bgScene.add(ambientLight);

    // Den pha mau xanh co san bong
    bgPointLight1 = new THREE.PointLight(0x10b981, 2.5, 120);
    bgPointLight1.position.set(15, 20, 20);
    bgScene.add(bgPointLight1);

    // Den pha mau xanh cyan neon
    bgPointLight2 = new THREE.PointLight(0x06b6d4, 2.2, 120);
    bgPointLight2.position.set(-15, -15, 15);
    bgScene.add(bgPointLight2);

    // Den pha vang hoang gia Champions League
    bgPointLight3 = new THREE.PointLight(0xf59e0b, 1.8, 100);
    bgPointLight3.position.set(0, 10, 10);
    bgScene.add(bgPointLight3);

    // Tao hat sang bui co san van dong (Grass & Floodlight Sparkles)
    const starCount = 350;
    const starGeometry = new THREE.BufferGeometry();
    const starPositions = new Float32Array(starCount * 3);

    for (let i = 0; i < starCount * 3; i++) {
        starPositions[i] = (Math.random() - 0.5) * 130;
    }

    starGeometry.setAttribute('position', new THREE.BufferAttribute(starPositions, 3));
    const starMaterial = new THREE.PointsMaterial({
        color: 0x34d399,
        size: 0.8,
        transparent: true,
        opacity: 0.85
    });

    const starField = new THREE.Points(starGeometry, starMaterial);
    bgScene.add(starField);

    // Tao cac qua bong da 3D (Soccer Ball Dodecahedron & Icosahedron) bay lo lung
    const soccerGeometries = [
        new THREE.IcosahedronGeometry(2.2, 1),
        new THREE.DodecahedronGeometry(2.0),
        new THREE.SphereGeometry(1.8, 12, 12),
        new THREE.TorusGeometry(2.0, 0.35, 12, 24)
    ];

    const soccerColors = [0x10b981, 0x06b6d4, 0xf59e0b, 0xffffff, 0x34d399];

    for (let i = 0; i < 16; i++) {
        const geom = soccerGeometries[i % soccerGeometries.length];
        const mat = new THREE.MeshStandardMaterial({
            color: soccerColors[i % soccerColors.length],
            wireframe: true,
            transparent: true,
            opacity: 0.45,
            roughness: 0.2,
            metalness: 0.6
        });

        const mesh = new THREE.Mesh(geom, mat);
        mesh.position.set(
            (Math.random() - 0.5) * 55,
            (Math.random() - 0.5) * 38,
            (Math.random() - 0.5) * 25 - 5
        );
        mesh.rotation.set(Math.random() * Math.PI, Math.random() * Math.PI, 0);

        bgScene.add(mesh);
        bgMeshGroup.push({
            mesh: mesh,
            rotSpeedX: (Math.random() - 0.5) * 0.018,
            rotSpeedY: (Math.random() - 0.5) * 0.018
        });
    }

    // Su kien di chuyen con tro chuot
    window.addEventListener('mousemove', (e) => {
        mouseX = (e.clientX / window.innerWidth - 0.5) * 2;
        mouseY = (e.clientY / window.innerHeight - 0.5) * 2;
    });

    // Su kien vuot cam ung tren dien thoai / may tinh bang
    window.addEventListener('touchmove', (e) => {
        if (e.touches.length > 0) {
            mouseX = (e.touches[0].clientX / window.innerWidth - 0.5) * 2;
            mouseY = (e.touches[0].clientY / window.innerHeight - 0.5) * 2;
        }
    });

    window.addEventListener('resize', onWindowResizeBackground);
    animateKhongGianNen();
}

function onWindowResizeBackground() {
    if (!bgCamera || !bgRenderer) return;
    bgCamera.aspect = window.innerWidth / window.innerHeight;
    bgCamera.updateProjectionMatrix();
    bgRenderer.setSize(window.innerWidth, window.innerHeight);
}

function animateKhongGianNen() {
    requestAnimationFrame(animateKhongGianNen);
    if (!bgScene || !bgRenderer) return;

    // Xoay cac qua bong da 3D
    bgMeshGroup.forEach(item => {
        item.mesh.rotation.x += item.rotSpeedX;
        item.mesh.rotation.y += item.rotSpeedY;
    });

    // Tinh toan di chuyen camera va khong gian 3D bám theo con tro chuot
    targetCameraX = mouseX * 12;
    targetCameraY = -mouseY * 8;

    bgCamera.position.x += (targetCameraX - bgCamera.position.x) * 0.08;
    bgCamera.position.y += (targetCameraY - bgCamera.position.y) * 0.08;

    // Nghieng nhe khong gian san bong 3D theo chuot
    bgScene.rotation.y = mouseX * 0.2;
    bgScene.rotation.x = mouseY * 0.12;

    // Den pha san van dong di chuyen theo chuot
    if (bgPointLight1) {
        bgPointLight1.position.x = mouseX * 25;
        bgPointLight1.position.y = -mouseY * 20;
    }

    bgCamera.lookAt(0, 0, 0);
    bgRenderer.render(bgScene, bgCamera);
}

window.addEventListener('DOMContentLoaded', () => {
    setTimeout(khoi_tao_khong_gian_nen_3d, 100);
});

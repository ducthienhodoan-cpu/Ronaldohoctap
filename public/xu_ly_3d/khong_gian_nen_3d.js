// File: khong_gian_nen_3d.js
// Mo ta: Xu ly hieu ung khong gian 3D nen phia sau di chuyen tuong tac theo con tro chuot dung Three.js

let bgScene, bgCamera, bgRenderer;
let bgMeshGroup = [];
let bgPointLight1, bgPointLight2;
let mouseX = 0, mouseY = 0;
let targetCameraX = 0, targetCameraY = 0;

function khoi_tao_khong_gian_nen_3d() {
    const canvas = document.getElementById('bg3dCanvas');
    if (!canvas || typeof THREE === 'undefined') return;

    bgScene = new THREE.Scene();
    bgCamera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
    bgCamera.position.z = 30;

    bgRenderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
    bgRenderer.setSize(window.innerWidth, window.innerHeight);
    bgRenderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    // Anh sang
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
    bgScene.add(ambientLight);

    bgPointLight1 = new THREE.PointLight(0x06b6d4, 2.0, 100);
    bgPointLight1.position.set(10, 15, 20);
    bgScene.add(bgPointLight1);

    bgPointLight2 = new THREE.PointLight(0xec4899, 2.0, 100);
    bgPointLight2.position.set(-10, -15, 10);
    bgScene.add(bgPointLight2);

    // Tao vi khoang sao 3D
    const starCount = 400;
    const starGeometry = new THREE.BufferGeometry();
    const starPositions = new Float32Array(starCount * 3);

    for (let i = 0; i < starCount * 3; i++) {
        starPositions[i] = (Math.random() - 0.5) * 120;
    }

    starGeometry.setAttribute('position', new THREE.BufferAttribute(starPositions, 3));
    const starMaterial = new THREE.PointsMaterial({
        color: 0x06b6d4,
        size: 0.7,
        transparent: true,
        opacity: 0.85
    });

    const starField = new THREE.Points(starGeometry, starMaterial);
    bgScene.add(starField);

    // Tao cac khoi hinh hoc 3D bay lo lung
    const geometries = [
        new THREE.BoxGeometry(2.2, 2.2, 2.2),
        new THREE.OctahedronGeometry(2.0),
        new THREE.TorusGeometry(1.8, 0.4, 16, 32),
        new THREE.IcosahedronGeometry(1.8)
    ];

    const colors = [0x06b6d4, 0x10b981, 0xf59e0b, 0xec4899, 0xa855f7];

    for (let i = 0; i < 18; i++) {
        const geom = geometries[i % geometries.length];
        const mat = new THREE.MeshStandardMaterial({
            color: colors[i % colors.length],
            wireframe: true,
            transparent: true,
            opacity: 0.5
        });

        const mesh = new THREE.Mesh(geom, mat);
        mesh.position.set(
            (Math.random() - 0.5) * 50,
            (Math.random() - 0.5) * 35,
            (Math.random() - 0.5) * 25 - 5
        );
        mesh.rotation.set(Math.random() * Math.PI, Math.random() * Math.PI, 0);

        bgScene.add(mesh);
        bgMeshGroup.push({
            mesh: mesh,
            rotSpeedX: (Math.random() - 0.5) * 0.02,
            rotSpeedY: (Math.random() - 0.5) * 0.02
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

    // Xoay cac khoi 3D
    bgMeshGroup.forEach(item => {
        item.mesh.rotation.x += item.rotSpeedX;
        item.mesh.rotation.y += item.rotSpeedY;
    });

    // Tinh toan di chuyen camera va khong gian 3D bám theo con tro chuot
    targetCameraX = mouseX * 14;
    targetCameraY = -mouseY * 10;

    bgCamera.position.x += (targetCameraX - bgCamera.position.x) * 0.08;
    bgCamera.position.y += (targetCameraY - bgCamera.position.y) * 0.08;

    // Nghieng nhe toan bo khong gian 3D theo chuot
    bgScene.rotation.y = mouseX * 0.25;
    bgScene.rotation.x = mouseY * 0.15;

    // Den phat sang noi bat di chuyen theo chuot
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

// File: khong_gian_nen_3d.js
// Mo ta: Xu ly hieu ung khong gian 3D nen phia sau ung dung dung Three.js

let bgScene, bgCamera, bgRenderer;
let bgMeshGroup = [];
let mouseX = 0, mouseY = 0;

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

    const pointLight = new THREE.PointLight(0x06b6d4, 1.5, 100);
    pointLight.position.set(10, 15, 20);
    bgScene.add(pointLight);

    const pointLight2 = new THREE.PointLight(0xec4899, 1.5, 100);
    pointLight2.position.set(-10, -15, 10);
    bgScene.add(pointLight2);

    // Tao vi khoang sao 3D
    const starCount = 300;
    const starGeometry = new THREE.BufferGeometry();
    const starPositions = new Float32Array(starCount * 3);

    for (let i = 0; i < starCount * 3; i++) {
        starPositions[i] = (Math.random() - 0.5) * 100;
    }

    starGeometry.setAttribute('position', new THREE.BufferAttribute(starPositions, 3));
    const starMaterial = new THREE.PointsMaterial({
        color: 0x06b6d4,
        size: 0.6,
        transparent: true,
        opacity: 0.8
    });

    const starField = new THREE.Points(starGeometry, starMaterial);
    bgScene.add(starField);

    // Tao cac khoi hinh hoc 3D bay lo lửng
    const geometries = [
        new THREE.BoxGeometry(2, 2, 2),
        new THREE.OctahedronGeometry(1.8),
        new THREE.TorusGeometry(1.5, 0.4, 16, 32),
        new THREE.IcosahedronGeometry(1.5)
    ];

    const colors = [0x06b6d4, 0x10b981, 0xf59e0b, 0xec4899, 0xa855f7];

    for (let i = 0; i < 15; i++) {
        const geom = geometries[i % geometries.length];
        const mat = new THREE.MeshStandardMaterial({
            color: colors[i % colors.length],
            wireframe: true,
            transparent: true,
            opacity: 0.45
        });

        const mesh = new THREE.Mesh(geom, mat);
        mesh.position.set(
            (Math.random() - 0.5) * 45,
            (Math.random() - 0.5) * 30,
            (Math.random() - 0.5) * 20 - 5
        );
        mesh.rotation.set(Math.random() * Math.PI, Math.random() * Math.PI, 0);

        bgScene.add(mesh);
        bgMeshGroup.push({
            mesh: mesh,
            rotSpeedX: (Math.random() - 0.5) * 0.02,
            rotSpeedY: (Math.random() - 0.5) * 0.02
        });
    }

    window.addEventListener('mousemove', (e) => {
        mouseX = (e.clientX / window.innerWidth - 0.5) * 2;
        mouseY = (e.clientY / window.innerHeight - 0.5) * 2;
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

    // Parallax di chuyen camera nhe theo chuot
    bgCamera.position.x += (mouseX * 3 - bgCamera.position.x) * 0.05;
    bgCamera.position.y += (-mouseY * 3 - bgCamera.position.y) * 0.05;
    bgCamera.lookAt(bgScene.position);

    bgRenderer.render(bgScene, bgCamera);
}

window.addEventListener('DOMContentLoaded', () => {
    setTimeout(khoi_tao_khong_gian_nen_3d, 100);
});

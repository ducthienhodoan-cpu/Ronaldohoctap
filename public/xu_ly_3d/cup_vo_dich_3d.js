// File: cup_vo_dich_3d.js
// Mo ta: Hien thi Cup Vo Dich 3D tuong tac bang Three.js

let trophyScene3D, trophyCamera3D, trophyRenderer3D, trophyMesh3D;
let isTrophy3DInitialized = false;

function khoi_tao_cup_vo_dich_3d(canvasId, loaiCup) {
    const canvas = document.getElementById(canvasId);
    if (!canvas || typeof THREE === 'undefined') return;

    trophyScene3D = new THREE.Scene();
    trophyScene3D.background = new THREE.Color(0x020617);

    const aspect = canvas.clientWidth / canvas.clientHeight || 1;
    trophyCamera3D = new THREE.PerspectiveCamera(45, aspect, 0.1, 100);
    trophyCamera3D.position.set(0, 2.5, 7);
    trophyCamera3D.lookAt(0, 1, 0);

    trophyRenderer3D = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
    trophyRenderer3D.setSize(canvas.clientWidth || 300, canvas.clientHeight || 250);
    trophyRenderer3D.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    // Anh sang chieu cup
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
    trophyScene3D.add(ambientLight);

    const spotLight = new THREE.SpotLight(0xf59e0b, 2);
    spotLight.position.set(5, 10, 5);
    trophyScene3D.add(spotLight);

    const spotLightBlue = new THREE.SpotLight(0x06b6d4, 1.5);
    spotLightBlue.position.set(-5, -5, -5);
    trophyScene3D.add(spotLightBlue);

    // Đế cúp
    const baseGeo = new THREE.CylinderGeometry(1.6, 1.8, 0.6, 32);
    const baseMat = new THREE.MeshStandardMaterial({ color: 0x0f172a, metalness: 0.9, roughness: 0.1 });
    const baseMesh = new THREE.Mesh(baseGeo, baseMat);
    baseMesh.position.y = -0.3;
    trophyScene3D.add(baseMesh);

    // Tạo Thân Cúp 3D
    trophyMesh3D = new THREE.Group();

    if (loaiCup === 'world_cup') {
        // Cup Vang World Cup 3D
        const goldMat = new THREE.MeshStandardMaterial({ color: 0xf59e0b, metalness: 0.9, roughness: 0.15 });

        const stemGeo = new THREE.CylinderGeometry(0.5, 0.9, 1.8, 32);
        const stem = new THREE.Mesh(stemGeo, goldMat);
        stem.position.y = 0.9;
        trophyMesh3D.add(stem);

        const globeGeo = new THREE.SphereGeometry(1.1, 32, 32);
        const globe = new THREE.Mesh(globeGeo, goldMat);
        globe.position.y = 2.2;
        trophyMesh3D.add(globe);
    } else {
        // Cup Bac C1 Champions League 3D (Cup Tai Voi)
        const silverMat = new THREE.MeshStandardMaterial({ color: 0xe2e8f0, metalness: 0.95, roughness: 0.1 });

        const bodyGeo = new THREE.CylinderGeometry(1.2, 0.6, 2.2, 32);
        const body = new THREE.Mesh(bodyGeo, silverMat);
        body.position.y = 1.1;
        trophyMesh3D.add(body);

        // Quai cup 2 bên
        const handleGeo = new THREE.TorusGeometry(0.7, 0.12, 16, 32, Math.PI);
        const handleLeft = new THREE.Mesh(handleGeo, silverMat);
        handleLeft.position.set(-1.1, 1.4, 0);
        handleLeft.rotation.z = Math.PI / 2;

        const handleRight = new THREE.Mesh(handleGeo, silverMat);
        handleRight.position.set(1.1, 1.4, 0);
        handleRight.rotation.z = -Math.PI / 2;

        trophyMesh3D.add(handleLeft);
        trophyMesh3D.add(handleRight);
    }

    trophyScene3D.add(trophyMesh3D);
    isTrophy3DInitialized = true;
    animateCupVoDich3D();
}

function animateCupVoDich3D() {
    if (!isTrophy3DInitialized) return;
    requestAnimationFrame(animateCupVoDich3D);
    if (!trophyScene3D || !trophyRenderer3D) return;

    if (trophyMesh3D) {
        trophyMesh3D.rotation.y += 0.015;
    }

    trophyRenderer3D.render(trophyScene3D, trophyCamera3D);
}

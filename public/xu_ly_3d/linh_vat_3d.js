// File: linh_vat_3d.js
// Mo ta: Linh Vat AI Roblox 3D tuong tac va phan hoi nguoi dung dung Three.js

let mascotScene3D, mascotCamera3D, mascotRenderer3D, mascotBotGroup3D;
let isMascotFlipping = false;
let flipAngle = 0;

function khoi_tao_linh_vat_3d() {
    const canvas = document.getElementById('canvasMascot3D');
    if (!canvas || typeof THREE === 'undefined') return;

    mascotScene3D = new THREE.Scene();

    const aspect = (canvas.clientWidth && canvas.clientHeight) ? (canvas.clientWidth / canvas.clientHeight) : 1;
    mascotCamera3D = new THREE.PerspectiveCamera(45, aspect, 0.1, 100);
    mascotCamera3D.position.set(0, 0, 5);
    mascotCamera3D.lookAt(0, 0, 0);

    mascotRenderer3D = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
    mascotRenderer3D.setSize(canvas.clientWidth || 60, canvas.clientHeight || 60);
    mascotRenderer3D.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    const ambientLight = new THREE.AmbientLight(0xffffff, 0.9);
    mascotScene3D.add(ambientLight);

    const dirLight = new THREE.DirectionalLight(0x06b6d4, 1.2);
    dirLight.position.set(3, 5, 4);
    mascotScene3D.add(dirLight);

    // Tao Robot Bot Mascot 3D
    mascotBotGroup3D = new THREE.Group();

    // Dau Robot
    const headGeo = new THREE.BoxGeometry(1.2, 1.0, 1.0);
    const headMat = new THREE.MeshStandardMaterial({ color: 0x06b6d4, metalness: 0.7, roughness: 0.2 });
    const head = new THREE.Mesh(headGeo, headMat);
    mascotBotGroup3D.add(head);

    // Mat Robot phat sang cyan
    const eyeGeo = new THREE.BoxGeometry(0.3, 0.15, 0.1);
    const eyeMat = new THREE.MeshBasicMaterial({ color: 0x10b981 });
    const eyeLeft = new THREE.Mesh(eyeGeo, eyeMat);
    eyeLeft.position.set(-0.3, 0.1, 0.51);
    const eyeRight = new THREE.Mesh(eyeGeo, eyeMat);
    eyeRight.position.set(0.3, 0.1, 0.51);
    mascotBotGroup3D.add(eyeLeft);
    mascotBotGroup3D.add(eyeRight);

    // Ăng-ten phát sáng
    const antGeo = new THREE.CylinderGeometry(0.04, 0.04, 0.5);
    const antMat = new THREE.MeshStandardMaterial({ color: 0xf59e0b });
    const ant = new THREE.Mesh(antGeo, antMat);
    ant.position.set(0, 0.75, 0);
    mascotBotGroup3D.add(ant);

    const antSphere = new THREE.Mesh(new THREE.SphereGeometry(0.12, 16, 16), new THREE.MeshBasicMaterial({ color: 0xec4899 }));
    antSphere.position.set(0, 1.0, 0);
    mascotBotGroup3D.add(antSphere);

    mascotScene3D.add(mascotBotGroup3D);

    canvas.style.cursor = 'pointer';
    canvas.addEventListener('click', () => {
        if (!isMascotFlipping) {
            isMascotFlipping = true;
            flipAngle = 0;
            if (typeof playClickSfx === 'function') playClickSfx();
        }
    });

    animateLinhVat3D();
}

function animateLinhVat3D() {
    requestAnimationFrame(animateLinhVat3D);
    if (!mascotScene3D || !mascotRenderer3D || !mascotBotGroup3D) return;

    // Hieu ung float bobbing nhe
    const time = Date.now() * 0.003;
    mascotBotGroup3D.position.y = Math.sin(time) * 0.15;

    if (isMascotFlipping) {
        flipAngle += 0.2;
        mascotBotGroup3D.rotation.y = flipAngle;
        if (flipAngle >= Math.PI * 2) {
            mascotBotGroup3D.rotation.y = 0;
            isMascotFlipping = false;
        }
    } else {
        mascotBotGroup3D.rotation.y = Math.sin(time * 0.5) * 0.2;
    }

    mascotRenderer3D.render(mascotScene3D, mascotCamera3D);
}

window.addEventListener('DOMContentLoaded', () => {
    setTimeout(khoi_tao_linh_vat_3d, 150);
});

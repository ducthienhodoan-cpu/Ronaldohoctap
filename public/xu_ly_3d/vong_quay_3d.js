// File: vong_quay_3d.js
// Mo ta: Vong Quay May Man 3D bang Three.js

let wheelScene3D, wheelCamera3D, wheelRenderer3D, wheelDisc3D;
let wheelSpinning3D = false;
let wheelTargetRotation3D = 0;

function khoi_tao_vong_quay_3d() {
    const canvas = document.getElementById('canvasWheel');
    if (!canvas || typeof THREE === 'undefined') return;

    wheelScene3D = new THREE.Scene();
    wheelScene3D.background = new THREE.Color(0x1e1b4b);

    const aspect = (canvas.clientWidth && canvas.clientHeight) ? (canvas.clientWidth / canvas.clientHeight) : 1;
    wheelCamera3D = new THREE.PerspectiveCamera(50, aspect, 0.1, 100);
    wheelCamera3D.position.set(0, 0, 5.5);
    wheelCamera3D.lookAt(0, 0, 0);

    wheelRenderer3D = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
    wheelRenderer3D.setSize(canvas.clientWidth || 180, canvas.clientHeight || 180);
    wheelRenderer3D.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    const ambientLight = new THREE.AmbientLight(0xffffff, 0.8);
    wheelScene3D.add(ambientLight);

    const dirLight = new THREE.DirectionalLight(0xffffff, 0.6);
    dirLight.position.set(2, 5, 5);
    wheelScene3D.add(dirLight);

    // Dia Vong Quay 3D
    wheelDisc3D = new THREE.Group();

    const colors = [0x06b6d4, 0x10b981, 0xf59e0b, 0xef4444, 0xa855f7, 0x3b82f6];
    const segmentAngle = (Math.PI * 2) / 6;

    for (let i = 0; i < 6; i++) {
        const shape = new THREE.Shape();
        shape.moveTo(0, 0);
        shape.arc(0, 0, 2, i * segmentAngle, (i + 1) * segmentAngle, false);
        shape.lineTo(0, 0);

        const extrudeSettings = { depth: 0.2, bevelEnabled: true, bevelSegments: 2, steps: 1, bevelSize: 0.05, bevelThickness: 0.05 };
        const geo = new THREE.ExtrudeGeometry(shape, extrudeSettings);
        const mat = new THREE.MeshStandardMaterial({ color: colors[i], metalness: 0.3, roughness: 0.3 });
        const mesh = new THREE.Mesh(geo, mat);
        wheelDisc3D.add(mesh);
    }

    // Vien vang ngoai
    const ringGeo = new THREE.TorusGeometry(2.05, 0.1, 16, 64);
    const ringMat = new THREE.MeshStandardMaterial({ color: 0xf59e0b, metalness: 0.9, roughness: 0.1 });
    const ring = new THREE.Mesh(ringGeo, ringMat);
    wheelDisc3D.add(ring);

    // Viên ngọc 3D ở giữa
    const gemGeo = new THREE.SphereGeometry(0.35, 16, 16);
    const gemMat = new THREE.MeshStandardMaterial({ color: 0xffffff, metalness: 1.0, roughness: 0.0 });
    const gem = new THREE.Mesh(gemGeo, gemMat);
    gem.position.z = 0.25;
    wheelDisc3D.add(gem);

    wheelScene3D.add(wheelDisc3D);

    // Mũi tên chỉ thưởng phía trên
    const pointerGeo = new THREE.ConeGeometry(0.25, 0.6, 16);
    const pointerMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
    const pointer = new THREE.Mesh(pointerGeo, pointerMat);
    pointer.position.set(0, 2.2, 0.3);
    pointer.rotation.z = Math.PI;
    wheelScene3D.add(pointer);

    animateVongQuay3D();
}

function quay_vong_quay_3d() {
    if (wheelSpinning3D) return;
    wheelSpinning3D = true;
    wheelTargetRotation3D = wheelDisc3D.rotation.z + Math.PI * 8 + Math.random() * Math.PI * 2;
}

function animateVongQuay3D() {
    requestAnimationFrame(animateVongQuay3D);
    if (!wheelScene3D || !wheelRenderer3D) return;

    if (wheelSpinning3D) {
        const diff = wheelTargetRotation3D - wheelDisc3D.rotation.z;
        if (diff > 0.01) {
            wheelDisc3D.rotation.z += diff * 0.06;
        } else {
            wheelDisc3D.rotation.z = wheelTargetRotation3D;
            wheelSpinning3D = false;
        }
    } else {
        wheelDisc3D.rotation.z += 0.003;
    }

    wheelRenderer3D.render(wheelScene3D, wheelCamera3D);
}

window.addEventListener('DOMContentLoaded', () => {
    setTimeout(khoi_tao_vong_quay_3d, 200);
});

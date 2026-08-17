// File: public/xu_ly_3d/gap_thu_3d.js
// Mo ta: Modul xu ly tro choi Gap Thu 3D va Canvas tuong tac tich luy XP Vercel Web App

let clawScene3D, clawCamera3D, clawRenderer3D, clawArm3D, clawPlush3D;
let clawIsOperating = false;
let clawYPosition = 2.0;
let clawState = 'idle'; // 'idle', 'lowering', 'lifting', 'returning'
let clawTargetTier = 'thuong';

const TI_LE_GAP_THU = {
    'thuong': { ten: 'Gấu Bông Thường', ti_le: 75, xp: 50, color: 0x06b6d4 },
    'hiem': { ten: 'Thỏ Bông Hiếm', ti_le: 50, xp: 200, color: 0xf59e0b },
    'huyen_thoai': { ten: 'Rồng Bông Huyền Thoại', ti_le: 25, xp: 500, color: 0xec4899 }
};

function khoi_tao_gap_thu_3d() {
    const canvas = document.getElementById('canvasClaw');
    if (!canvas || typeof THREE === 'undefined') return;

    clawScene3D = new THREE.Scene();
    clawScene3D.background = new THREE.Color(0x0f172a);

    const aspect = (canvas.clientWidth && canvas.clientHeight) ? (canvas.clientWidth / canvas.clientHeight) : (240 / 200);
    clawCamera3D = new THREE.PerspectiveCamera(45, aspect, 0.1, 100);
    clawCamera3D.position.set(0, 0.5, 6);
    clawCamera3D.lookAt(0, 0, 0);

    clawRenderer3D = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
    clawRenderer3D.setSize(canvas.clientWidth || 240, canvas.clientHeight || 200);
    clawRenderer3D.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    const ambientLight = new THREE.AmbientLight(0xffffff, 0.9);
    clawScene3D.add(ambientLight);

    const dirLight = new THREE.DirectionalLight(0xffffff, 0.8);
    dirLight.position.set(3, 8, 5);
    clawScene3D.add(dirLight);

    // Khung May Gap
    const frameGeo = new THREE.BoxGeometry(3.6, 4.2, 0.2);
    const frameMat = new THREE.MeshStandardMaterial({ color: 0x1e1b4b, wireframe: false, roughness: 0.2 });
    const frameMesh = new THREE.Mesh(frameGeo, frameMat);
    frameMesh.position.z = -1;
    clawScene3D.add(frameMesh);

    // Tay Gap 3D (Claw Arm)
    clawArm3D = new THREE.Group();
    
    // Day keo tay gap
    const stringGeo = new THREE.CylinderGeometry(0.04, 0.04, 3, 16);
    const stringMat = new THREE.MeshBasicMaterial({ color: 0xa855f7 });
    const stringMesh = new THREE.Mesh(stringGeo, stringMat);
    stringMesh.position.y = 1.5;
    clawArm3D.add(stringMesh);

    // Đau gắp kim loai
    const headGeo = new THREE.SphereGeometry(0.35, 16, 16);
    const headMat = new THREE.MeshStandardMaterial({ color: 0x06b6d4, metalness: 0.8, roughness: 0.2 });
    const headMesh = new THREE.Mesh(headGeo, headMat);
    headMesh.position.y = 0;
    clawArm3D.add(headMesh);

    // 3 Móng gắp
    for (let i = 0; i < 3; i++) {
        const angle = (i * Math.PI * 2) / 3;
        const clawLegGeo = new THREE.CylinderGeometry(0.05, 0.02, 0.6, 8);
        const clawLegMat = new THREE.MeshStandardMaterial({ color: 0xec4899, metalness: 0.9 });
        const leg = new THREE.Mesh(clawLegGeo, clawLegMat);
        leg.position.set(Math.cos(angle) * 0.25, -0.3, Math.sin(angle) * 0.25);
        leg.rotation.z = Math.cos(angle) * 0.4;
        leg.rotation.x = Math.sin(angle) * 0.4;
        clawArm3D.add(leg);
    }

    clawArm3D.position.set(0, 1.2, 0);
    clawScene3D.add(clawArm3D);

    // Thu bong 3D o duoi
    const plushGeo = new THREE.DodecahedronGeometry(0.6, 1);
    const plushMat = new THREE.MeshStandardMaterial({ color: 0x06b6d4, roughness: 0.8 });
    clawPlush3D = new THREE.Mesh(plushGeo, plushMat);
    clawPlush3D.position.set(0, -1.3, 0);
    clawScene3D.add(clawPlush3D);

    animateGapThu3D();
}

function bat_dau_gap_thu_web() {
    if (clawIsOperating) return;
    clawIsOperating = true;
    clawState = 'lowering';

    const resDiv = document.getElementById('clawResult');
    if (resDiv) {
        resDiv.style.color = '#F59E0B';
        resDiv.innerText = 'Tay gắp đang hạ xuống gắp thú...';
    }
}

function animateGapThu3D() {
    requestAnimationFrame(animateGapThu3D);
    if (!clawScene3D || !clawRenderer3D) return;

    if (clawState === 'lowering') {
        if (clawArm3D.position.y > -0.7) {
            clawArm3D.position.y -= 0.04;
        } else {
            // Roll 30% rot vs 70% thanh cong
            const roll = Math.floor(Math.random() * 100) + 1;
            if (roll <= 30) {
                // 30% Rot
                clawState = 'lifting_fail';
            } else {
                // 70% Thanh cong: ngau nhien 1 trong 3 thu bong
                const subRoll = Math.random() * 100;
                if (subRoll < 60) clawTargetTier = 'thuong';
                else if (subRoll < 90) clawTargetTier = 'hiem';
                else clawTargetTier = 'huyen_thoai';

                const info = TI_LE_GAP_THU[clawTargetTier];
                if (clawPlush3D) {
                    clawPlush3D.material.color.setHex(info.color);
                    clawPlush3D.position.y = clawArm3D.position.y - 0.5;
                }
                clawState = 'lifting_success';
            }
        }
    } else if (clawState === 'lifting_success') {
        if (clawArm3D.position.y < 1.2) {
            clawArm3D.position.y += 0.04;
            clawPlush3D.position.y = clawArm3D.position.y - 0.5;
        } else {
            clawState = 'idle';
            clawIsOperating = false;
            clawPlush3D.position.set(0, -1.3, 0);
            
            const info = TI_LE_GAP_THU[clawTargetTier];
            const resDiv = document.getElementById('clawResult');
            if (resDiv) {
                resDiv.style.color = '#10B981';
                resDiv.innerText = `Chúc mừng! Gắp thành công ${info.ten}! Nhận +${info.xp} XP!`;
            }
            if (typeof updateXPDisplay === 'function') {
                updateXPDisplay(info.xp);
            }
        }
    } else if (clawState === 'lifting_fail') {
        if (clawArm3D.position.y < 1.2) {
            clawArm3D.position.y += 0.04;
        } else {
            clawState = 'idle';
            clawIsOperating = false;
            clawPlush3D.position.set(0, -1.3, 0);

            const resDiv = document.getElementById('clawResult');
            if (resDiv) {
                resDiv.style.color = '#EF4444';
                resDiv.innerText = 'Tiếc quá! Tay gắp bị trượt rớt mất thú bông rồi. Thử lại nhé!';
            }
        }
    } else {
        // Nhẹ nhàng đung đưa tay gắp
        clawArm3D.rotation.z = Math.sin(Date.now() * 0.002) * 0.05;
    }

    clawRenderer3D.render(clawScene3D, clawCamera3D);
}

window.addEventListener('DOMContentLoaded', () => {
    setTimeout(khoi_tao_gap_thu_3d, 300);
});

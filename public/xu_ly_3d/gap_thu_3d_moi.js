// File: public/xu_ly_3d/gap_thu_3d_moi.js
// Mo ta: Dong co 3D May Gap Thu tuong tac Joystick 4 huong ho tro Ve Thong & Ve Vang va Chuc nang Quay Vong Quay Co Qua

let clawScene3D, clawCamera3D;
let clawRenderer3D_Main = null;
let clawRenderer3D_Modal = null;
let clawArm3D, clawPlush3D, prizeChuteMesh;
let clawIsOperating = false;
let clawState = 'idle'; // 'idle', 'positioning', 'lowering', 'grabbing', 'lifting', 'slipping', 'moving_to_chute', 'dropping', 'returning'
let clawTargetTier = 'thuong';
let dropY = 0.7;
let clawPosX = 0;
let clawPosZ = 0;
let countdownTimer20s = 20;
let timerIntervalId = null;
let willSlipThisTurn = false;
let isUsingGoldenTicket = false;

function lay_ve_gap_hien_tai() {
    let v = localStorage.getItem('ve_gap');
    if (!v) {
        v = '5';
        localStorage.setItem('ve_gap', '5');
    }
    return parseInt(v || '5', 10);
}

function lay_ve_vang_hien_tai() {
    let vv = localStorage.getItem('ve_vang');
    if (vv === null) {
        vv = '5';
        localStorage.setItem('ve_vang', '5');
    }
    return parseInt(vv || '5', 10);
}

function cap_nhat_hien_thi_ve_gap() {
    const v = lay_ve_gap_hien_tai();
    const vv = lay_ve_vang_hien_tai();
    const elemMain = document.getElementById('lblVeGapVal');
    const elemModal = document.getElementById('lblModalVeGapVal');
    const strText = `Vé Gắp: ${v} | Vé Vàng: ${vv}`;
    if (elemMain) elemMain.innerText = strText;
    if (elemModal) elemModal.innerText = strText;
}

function nap_5_ve_gap_mien_phi() {
    let currentV = parseInt(localStorage.getItem('ve_gap') || '5', 10);
    currentV += 5;
    localStorage.setItem('ve_gap', currentV.toString());
    cap_nhat_hien_thi_ve_gap();
    try { playClickSfx(); } catch(e) {}
}

function khoi_tao_gap_thu_3d_moi() {
    if (typeof THREE === 'undefined') return;

    cap_nhat_hien_thi_ve_gap();

    const canvasMain = document.getElementById('canvasClaw');
    const canvasModal = document.getElementById('canvasModalClaw');
    if (!canvasMain && !canvasModal) return;

    if (!clawScene3D) {
        clawScene3D = new THREE.Scene();
        clawScene3D.background = new THREE.Color(0x0f172a);

        clawCamera3D = new THREE.PerspectiveCamera(45, 1.5, 0.1, 100);
        clawCamera3D.position.set(0, 0.5, 6);
        clawCamera3D.lookAt(0, 0, 0);

        const ambientLight = new THREE.AmbientLight(0xffffff, 0.95);
        clawScene3D.add(ambientLight);

        const dirLight = new THREE.DirectionalLight(0xffffff, 0.85);
        dirLight.position.set(3, 8, 5);
        clawScene3D.add(dirLight);

        // Khung May Gap 3D
        const frameGeo = new THREE.BoxGeometry(3.8, 4.2, 0.2);
        const frameMat = new THREE.MeshStandardMaterial({ color: 0x1e1b4b, roughness: 0.2 });
        const frameMesh = new THREE.Mesh(frameGeo, frameMat);
        frameMesh.position.z = -1;
        clawScene3D.add(frameMesh);

        // Khay Nhan Thuong Phia Duoi Ben Trai
        const chuteGeo = new THREE.BoxGeometry(0.9, 0.8, 0.8);
        const chuteMat = new THREE.MeshStandardMaterial({ color: 0x10b981, metalness: 0.5, roughness: 0.3 });
        prizeChuteMesh = new THREE.Mesh(chuteGeo, chuteMat);
        prizeChuteMesh.position.set(-1.2, -1.3, 0);
        clawScene3D.add(prizeChuteMesh);

        // Tay Gap 3D (Claw Arm Group)
        clawArm3D = new THREE.Group();
        
        const stringGeo = new THREE.CylinderGeometry(0.03, 0.03, 3, 16);
        const stringMat = new THREE.MeshBasicMaterial({ color: 0xa855f7 });
        const stringMesh = new THREE.Mesh(stringGeo, stringMat);
        stringMesh.position.y = 1.5;
        clawArm3D.add(stringMesh);

        const headGeo = new THREE.SphereGeometry(0.32, 16, 16);
        const headMat = new THREE.MeshStandardMaterial({ color: 0x06b6d4, metalness: 0.8, roughness: 0.2 });
        const headMesh = new THREE.Mesh(headGeo, headMat);
        headMesh.position.y = 0;
        clawArm3D.add(headMesh);

        for (let i = 0; i < 3; i++) {
            const angle = (i * Math.PI * 2) / 3;
            const clawLegGeo = new THREE.CylinderGeometry(0.04, 0.02, 0.55, 8);
            const clawLegMat = new THREE.MeshStandardMaterial({ color: 0xec4899, metalness: 0.9 });
            const leg = new THREE.Mesh(clawLegGeo, clawLegMat);
            leg.position.set(Math.cos(angle) * 0.22, -0.28, Math.sin(angle) * 0.22);
            leg.rotation.z = Math.cos(angle) * 0.35;
            leg.rotation.x = Math.sin(angle) * 0.35;
            clawArm3D.add(leg);
        }

        clawArm3D.position.set(0, 1.2, 0);
        clawScene3D.add(clawArm3D);

        // Dong thu 15 vat pham nam o day
        for (let i = 0; i < 15; i++) {
            const itemGeo = new THREE.DodecahedronGeometry(0.3 + Math.random() * 0.1, 1);
            const itemMat = new THREE.MeshStandardMaterial({ color: Math.random() * 0xffffff, roughness: 0.6 });
            const itemMesh = new THREE.Mesh(itemGeo, itemMat);
            itemMesh.position.set((Math.random() - 0.5) * 2.2, -1.3 + Math.random() * 0.2, (Math.random() - 0.5) * 1.2);
            clawScene3D.add(itemMesh);
        }

        // Thu bong dang duoc gap 3D
        const plushGeo = new THREE.DodecahedronGeometry(0.48, 1);
        const plushMat = new THREE.MeshStandardMaterial({ color: 0x06b6d4, roughness: 0.7 });
        clawPlush3D = new THREE.Mesh(plushGeo, plushMat);
        clawPlush3D.position.set(0, -1.3, 0);
        clawScene3D.add(clawPlush3D);

        animateGapThu3DMoi();
    }

    if (canvasMain && !clawRenderer3D_Main) {
        try {
            clawRenderer3D_Main = new THREE.WebGLRenderer({ canvas: canvasMain, antialias: true, alpha: true });
            clawRenderer3D_Main.setSize(canvasMain.clientWidth || 260, canvasMain.clientHeight || 180);
            clawRenderer3D_Main.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        } catch(e) {}
    }

    if (canvasModal && !clawRenderer3D_Modal) {
        try {
            clawRenderer3D_Modal = new THREE.WebGLRenderer({ canvas: canvasModal, antialias: true, alpha: true });
            clawRenderer3D_Modal.setSize(canvasModal.clientWidth || 280, canvasModal.clientHeight || 190);
            clawRenderer3D_Modal.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        } catch(e) {}
    }
}

function moveJoystickClaw3D(dir) {
    if (clawIsOperating) return;

    const speed = 0.15;
    if (dir === 'left' && clawPosX > -1.2) clawPosX -= speed;
    if (dir === 'right' && clawPosX < 1.2) clawPosX += speed;
    if (dir === 'up' && clawPosZ > -0.8) clawPosZ -= speed;
    if (dir === 'down' && clawPosZ < 0.8) clawPosZ += speed;

    if (clawArm3D) {
        clawArm3D.position.x = clawPosX;
        clawArm3D.position.z = clawPosZ;
    }
}

function bat_dau_gap_thu_web_moi(suDungVeVang = false) {
    if (clawIsOperating) return;

    isUsingGoldenTicket = suDungVeVang;

    if (suDungVeVang) {
        let veVang = lay_ve_vang_hien_tai();
        if (veVang <= 0) {
            alert("BẠN CHƯA CÓ VÉ VÀNG! Hãy làm nhiệm vụ ngày, đạt điểm 10 bài kiểm tra hoặc đạt chuỗi Streak 7 ngày để nhận Vé Vàng nhé!");
            const resDiv = document.getElementById('clawResult');
            const resModalDiv = document.getElementById('modalClawResult');
            const msgChuaCo = "BẠN CHƯA CÓ VÉ VÀNG! Làm nhiệm vụ ngày để nhận Vé Vàng!";
            if (resDiv) { resDiv.style.color = '#EF4444'; resDiv.innerText = msgChuaCo; }
            if (resModalDiv) { resModalDiv.style.color = '#EF4444'; resModalDiv.innerText = msgChuaCo; }
            return;
        }
        veVang -= 1;
        localStorage.setItem('ve_vang', veVang.toString());
        willSlipThisTurn = Math.random() * 100 < 10; // Chế độ Vé Vàng chỉ có 10% rớt
    } else {
        let veHienTai = lay_ve_gap_hien_tai();
        if (veHienTai <= 0) {
            alert("Bạn đã hết Vé Gắp! Hãy hoàn thành 1 bài học hoặc trả lời đúng 10 câu liên tiếp để nhận thêm Vé Gắp nhé!");
            const resDiv = document.getElementById('clawResult');
            const resModalDiv = document.getElementById('modalClawResult');
            const msgHetVe = "BẠN ĐÃ HẾT VÉ GẮP! Hãy học bài để nhận thêm vé nhé!";
            if (resDiv) { resDiv.style.color = '#EF4444'; resDiv.innerText = msgHetVe; }
            if (resModalDiv) { resModalDiv.style.color = '#EF4444'; resModalDiv.innerText = msgHetVe; }
            return;
        }
        veHienTai -= 1;
        localStorage.setItem('ve_gap', veHienTai.toString());
        willSlipThisTurn = Math.random() * 100 < 60; // Chế độ Vé Thường có 60% rớt
    }

    cap_nhat_hien_thi_ve_gap();

    clawIsOperating = true;
    khoi_tao_gap_thu_3d_moi();

    countdownTimer20s = 20;
    const timerElem = document.getElementById('clawTimerText');
    const modalTimerElem = document.getElementById('modalClawTimerText');
    if (timerElem) timerElem.innerText = `Thời gian: 20s`;
    if (modalTimerElem) modalTimerElem.innerText = `Thời gian: 20s`;

    const resDiv = document.getElementById('clawResult');
    const resModalDiv = document.getElementById('modalClawResult');
    const statusMsg = suDungVeVang ? 'VÉ VÀNG KÍCH HOẠT: Tay gắp cường hóa 90% thành công!' : 'Tay gắp đang từ từ hạ xuống kẹp thú bông...';
    if (resDiv) { resDiv.style.color = suDungVeVang ? '#F59E0B' : '#00FFCC'; resDiv.innerText = statusMsg; }
    if (resModalDiv) { resModalDiv.style.color = suDungVeVang ? '#F59E0B' : '#00FFCC'; resModalDiv.innerText = statusMsg; }

    if (timerIntervalId) clearInterval(timerIntervalId);
    timerIntervalId = setInterval(() => {
        countdownTimer20s--;
        if (timerElem) timerElem.innerText = `Thời gian: ${countdownTimer20s}s`;
        if (modalTimerElem) modalTimerElem.innerText = `Thời gian: ${countdownTimer20s}s`;
        if (countdownTimer20s <= 0) {
            clearInterval(timerIntervalId);
        }
    }, 1000);

    if (clawScene3D && clawArm3D) {
        clawState = 'lowering';
    }
}

function animateGapThu3DMoi() {
    requestAnimationFrame(animateGapThu3DMoi);
    if (!clawScene3D) return;

    if (clawState === 'lowering') {
        if (clawArm3D && clawArm3D.position.y > -0.7) {
            clawArm3D.position.y -= 0.04;
        } else {
            clawState = 'lifting';
        }
    } else if (clawState === 'lifting') {
        if (clawArm3D && clawArm3D.position.y < 1.2) {
            clawArm3D.position.y += 0.04;

            if (willSlipThisTurn && clawArm3D.position.y >= 0.2) {
                clawState = 'slipping';
            } else if (clawPlush3D) {
                clawPlush3D.position.set(clawArm3D.position.x, clawArm3D.position.y - 0.45, clawArm3D.position.z);
            }
        } else {
            clawState = 'moving_to_chute';
        }
    } else if (clawState === 'slipping') {
        if (clawPlush3D && clawPlush3D.position.y > -1.3) {
            clawPlush3D.position.y -= 0.09;
        }
        if (clawArm3D && clawArm3D.position.y < 1.2) {
            clawArm3D.position.y += 0.04;
        } else {
            clawState = 'returning';
        }
    } else if (clawState === 'moving_to_chute') {
        if (clawArm3D && clawArm3D.position.x > -1.2) {
            clawArm3D.position.x -= 0.04;
            if (clawPlush3D) {
                clawPlush3D.position.set(clawArm3D.position.x, clawArm3D.position.y - 0.45, clawArm3D.position.z);
            }
        } else {
            dropY = clawArm3D.position.y - 0.45;
            clawState = 'dropping';
        }
    } else if (clawState === 'dropping') {
        if (clawPlush3D && dropY > -1.2) {
            dropY -= 0.08;
            clawPlush3D.position.set(-1.2, dropY, 0);
        } else {
            clawState = 'returning';
        }
    } else if (clawState === 'returning') {
        if (clawArm3D && clawArm3D.position.x < 0) {
            clawArm3D.position.x += 0.04;
        } else {
            if (clawArm3D) clawArm3D.position.set(0, 1.2, 0);
            clawPosX = 0; clawPosZ = 0;
            clawState = 'idle';
            clawIsOperating = false;

            if (timerIntervalId) clearInterval(timerIntervalId);
            
            const resDiv = document.getElementById('clawResult');
            const resModalDiv = document.getElementById('modalClawResult');

            if (willSlipThisTurn) {
                const msgRot = "Rất tiếc! Tay gắp bị trượt rớt thú giữa chừng (Tỉ lệ rớt 60%). Hãy thử lại lượt sau!";
                if (resDiv) { resDiv.style.color = '#EF4444'; resDiv.innerText = msgRot; }
                if (resModalDiv) { resModalDiv.style.color = '#EF4444'; resModalDiv.innerText = msgRot; }
            } else {
                const xpNhan = isUsingGoldenTicket ? 500 : 150;
                const msg = isUsingGoldenTicket ? 
                    `CHÚC MỪNG VÉ VÀNG! ĐÃ GẮP THÀNH CÔNG THÚ BÔNG BÍ MẬT! Nhận +500 Roblox XP!` :
                    `CHÚC MỪNG! ĐÃ GẮP THÀNH CÔNG THÚ BÔNG VÀO KHAY THƯỞNG! Nhận +150 Roblox XP!`;
                if (resDiv) { resDiv.style.color = '#10B981'; resDiv.innerText = msg; }
                if (resModalDiv) { resModalDiv.style.color = '#10B981'; resModalDiv.innerText = msg; }
                if (typeof updateXPDisplay === 'function') updateXPDisplay(xpNhan);
            }
        }
    } else {
        if (clawArm3D) {
            clawArm3D.rotation.z = Math.sin(Date.now() * 0.002) * 0.04;
        }
    }

    const canvasMain = document.getElementById('canvasClaw');
    if (clawRenderer3D_Main && canvasMain && canvasMain.clientWidth > 0 && canvasMain.clientHeight > 0) {
        clawRenderer3D_Main.render(clawScene3D, clawCamera3D);
    }

    const canvasModal = document.getElementById('canvasModalClaw');
    if (clawRenderer3D_Modal && canvasModal && canvasModal.clientWidth > 0 && canvasModal.clientHeight > 0) {
        clawRenderer3D_Modal.render(clawScene3D, clawCamera3D);
    }
}

window.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft' || e.key === 'a' || e.key === 'A') moveJoystickClaw3D('left');
    if (e.key === 'ArrowRight' || e.key === 'd' || e.key === 'D') moveJoystickClaw3D('right');
    if (e.key === 'ArrowUp' || e.key === 'w' || e.key === 'W') moveJoystickClaw3D('up');
    if (e.key === 'ArrowDown' || e.key === 's' || e.key === 'S') moveJoystickClaw3D('down');
});

window.addEventListener('DOMContentLoaded', () => {
    setTimeout(khoi_tao_gap_thu_3d_moi, 300);
});

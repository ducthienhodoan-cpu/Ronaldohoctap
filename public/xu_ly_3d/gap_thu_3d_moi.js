// File: public/xu_ly_3d/gap_thu_3d_moi.js
// Mo ta: Dong co 3D May Gap Thu: Tra 1 ve bat dem gio 15s, Nut GAP o giua Joystick D-Pad va Ti le rot 50%

let clawScene3D, clawCamera3D;
let clawRenderer3D_Main = null;
let clawRenderer3D_Modal = null;
let clawArm3D, clawPlush3D, prizeChuteMesh;
let clawIsOperating = false;
let clawState = 'idle'; // 'idle', 'controlling', 'lowering', 'lifting', 'slipping', 'moving_to_chute', 'dropping', 'returning'
let dropY = 0.7;
let clawPosX = 0;
let clawPosZ = 0;
let countdownTimer20s = 15;
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

function nhan_5_ve_vang_tuan_moi() {
    let currentVV = parseInt(localStorage.getItem('ve_vang') || '5', 10);
    currentVV += 5;
    localStorage.setItem('ve_vang', currentVV.toString());
    cap_nhat_hien_thi_ve_gap();
    try { playClickSfx(); } catch(e) {}
    alert("BẠN ĐÃ NHẬN THÀNH CÔNG +5 VÉ VÀNG MIỄN PHÍ CHO TUẦN MỚI!");
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
    // Cho phep dieu khien khi dang trong luot dieu khien (controlling) hoac trang thai cho (idle)
    if (clawIsOperating && clawState !== 'controlling') return;

    const speed = 0.15;
    if (dir === 'left' && clawPosX > -1.2) clawPosX -= speed;
    if (dir === 'right' && clawPosX < 1.2) clawPosX += speed;
    if (dir === 'up' && clawPosZ > -0.8) clawPosZ -= speed;
    if (dir === 'down' && clawPosZ < 0.8) clawPosZ += speed;

    if (clawArm3D) {
        clawArm3D.position.x = clawPosX;
        clawArm3D.position.z = clawPosZ;
    }
    try { playClickSfx(); } catch(e) {}
}

function bat_dau_gap_thu_web_moi(suDungVeVang = false) {
    if (clawIsOperating) {
        if (clawState === 'controlling') {
            ha_tay_gap_ngay();
        }
        return;
    }

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
        willSlipThisTurn = Math.random() < 0.10; // Chế độ Vé Vàng: 10% rớt, 90% thành công
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
        willSlipThisTurn = Math.random() < 0.50; // Đúng 50% rớt theo yêu cầu
    }

    cap_nhat_hien_thi_ve_gap();
    try { playClickSfx(); } catch(e) {}

    clawIsOperating = true;
    clawState = 'controlling';
    khoi_tao_gap_thu_3d_moi();

    // Reset vi tri tay gap ve vi tri chuan
    clawPosX = 0;
    clawPosZ = 0;
    if (clawArm3D) {
        clawArm3D.position.set(0, 1.2, 0);
    }
    if (clawPlush3D) {
        clawPlush3D.position.set(0, -1.3, 0);
    }

    countdownTimer20s = 15;
    const timerElem = document.getElementById('clawTimerText');
    const modalTimerElem = document.getElementById('modalClawTimerText');
    if (timerElem) timerElem.innerText = `Điều khiển: 15s`;
    if (modalTimerElem) modalTimerElem.innerText = `Điều khiển: 15s`;

    // Cap nhat trang thai va bat sang nut GAP & Ha Tay Gap
    cap_nhat_trang_thai_nut_ha_gap(true);

    const resDiv = document.getElementById('clawResult');
    const resModalDiv = document.getElementById('modalClawResult');
    const statusMsg = suDungVeVang ? 
        'VÉ VÀNG ĐÃ KÍCH HOẠT! Dùng Joystick chỉnh vị trí rồi bấm nút [GẮP]!' : 
        'ĐANG ĐẾM THỜI GIAN: Dùng Joystick/phím mũi tên chỉnh vị trí, rồi bấm nút [GẮP]!';
    if (resDiv) { resDiv.style.color = suDungVeVang ? '#F59E0B' : '#00FFCC'; resDiv.innerText = statusMsg; }
    if (resModalDiv) { resModalDiv.style.color = suDungVeVang ? '#F59E0B' : '#00FFCC'; resModalDiv.innerText = statusMsg; }

    if (timerIntervalId) clearInterval(timerIntervalId);
    timerIntervalId = setInterval(() => {
        countdownTimer20s--;
        if (timerElem) timerElem.innerText = `Điều khiển: ${countdownTimer20s}s`;
        if (modalTimerElem) modalTimerElem.innerText = `Điều khiển: ${countdownTimer20s}s`;
        
        if (countdownTimer20s <= 0) {
            clearInterval(timerIntervalId);
            ha_tay_gap_ngay();
        }
    }, 1000);
}

function ha_tay_gap_ngay() {
    if (clawState !== 'controlling') return;

    if (timerIntervalId) clearInterval(timerIntervalId);
    try { playClickSfx(); } catch(e) {}

    const timerElem = document.getElementById('clawTimerText');
    const modalTimerElem = document.getElementById('modalClawTimerText');
    if (timerElem) timerElem.innerText = `Đang gắp...`;
    if (modalTimerElem) modalTimerElem.innerText = `Đang gắp...`;

    const resDiv = document.getElementById('clawResult');
    const resModalDiv = document.getElementById('modalClawResult');
    const statusMsg = 'TAY GẮP ĐANG HẠ XUỐNG KẸP THÚ BÔNG...';
    if (resDiv) { resDiv.style.color = '#F59E0B'; resDiv.innerText = statusMsg; }
    if (resModalDiv) { resModalDiv.style.color = '#F59E0B'; resModalDiv.innerText = statusMsg; }

    cap_nhat_trang_thai_nut_ha_gap(false);

    // Di chuyển vị trí thú bông ở đáy về dưới tay gắp
    if (clawPlush3D && clawArm3D) {
        clawPlush3D.position.set(clawArm3D.position.x, -1.3, clawArm3D.position.z);
    }

    clawState = 'lowering';
}

function cap_nhat_trang_thai_nut_ha_gap(isControlling) {
    const btnDropMain = document.getElementById('btnDropClawMain');
    const btnDropModal = document.getElementById('btnDropClawModal');
    const btnDPadMain = document.getElementById('btnDPadGrabMain');
    const btnDPadModal = document.getElementById('btnDPadGrabModal');

    [btnDropMain, btnDropModal].forEach(btn => {
        if (!btn) return;
        if (isControlling) {
            btn.style.opacity = '1';
            btn.style.pointerEvents = 'auto';
            btn.style.animation = 'pulse 1s infinite alternate';
            btn.innerText = 'HẠ TAY GẮP (GẮP NGAY!)';
        } else {
            btn.style.opacity = '0.5';
            btn.style.pointerEvents = 'none';
            btn.style.animation = 'none';
            btn.innerText = 'HẠ TAY GẮP (GẮP NGAY)';
        }
    });

    [btnDPadMain, btnDPadModal].forEach(btn => {
        if (!btn) return;
        if (isControlling) {
            btn.style.opacity = '1';
            btn.style.pointerEvents = 'auto';
            btn.style.animation = 'pulse 1s infinite alternate';
            btn.style.background = 'linear-gradient(135deg, #EF4444, #B91C1C)';
            btn.style.color = '#FFFFFF';
            btn.style.boxShadow = '0 0 12px rgba(239, 68, 68, 0.8)';
        } else {
            btn.style.opacity = '0.6';
            btn.style.pointerEvents = 'none';
            btn.style.animation = 'none';
            btn.style.background = '#475569';
            btn.style.color = '#94A3B8';
            btn.style.boxShadow = 'none';
        }
    });
}

function animateGapThu3DMoi() {
    requestAnimationFrame(animateGapThu3DMoi);
    if (!clawScene3D) return;

    if (clawState === 'controlling') {
        // Trong che do dieu khien: Tay gap lac lu nhe tu nhien
        if (clawArm3D) {
            clawArm3D.rotation.z = Math.sin(Date.now() * 0.003) * 0.03;
        }
    } else if (clawState === 'lowering') {
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
            cap_nhat_trang_thai_nut_ha_gap(false);

            const timerElem = document.getElementById('clawTimerText');
            const modalTimerElem = document.getElementById('modalClawTimerText');
            if (timerElem) timerElem.innerText = `15s`;
            if (modalTimerElem) modalTimerElem.innerText = `15s`;
            
            const resDiv = document.getElementById('clawResult');
            const resModalDiv = document.getElementById('modalClawResult');

            if (willSlipThisTurn) {
                const msgRot = "Rất tiếc! Tay gắp bị trượt rớt thú giữa chừng (Tỉ lệ rớt 50%). Hãy căn chỉnh chuẩn và thử lại nhé!";
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
    if (e.key === ' ' || e.key === 'Enter') {
        if (clawState === 'controlling') {
            ha_tay_gap_ngay();
        }
    }
});

window.addEventListener('DOMContentLoaded', () => {
    setTimeout(khoi_tao_gap_thu_3d_moi, 300);
});

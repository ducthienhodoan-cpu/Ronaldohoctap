// File: public/xu_ly_3d/vong_quay_3d_moi.js
// Mo ta: Dong co Ve va Quay Vong Quay May Man Super Lucky Wheel 10 O voi Lucky Meter, Super Spin, Golden Spin va Jackpot

let wheel10Angle = 0;
let isWheel10Spinning = false;

const SLICES_THUONG = [
    { label: "100 Xu", color: "#06B6D4" },
    { label: "250 Xu", color: "#10B981" },
    { label: "+1 Vé Gắp", color: "#F59E0B" },
    { label: "+100 XP", color: "#3B82F6" },
    { label: "CÓ LIỀN PHẦN QUÀ", color: "#A855F7" },
    { label: "10 Kim Cương", color: "#EC4899" },
    { label: "Thú Ngẫu Nhiên", color: "#14B8A6" },
    { label: "Golden Ticket", color: "#EAB308" },
    { label: "Skin Đặc Biệt", color: "#8B5CF6" },
    { label: "JACKPOT", color: "#EF4444" }
];

const SLICES_SUPER = [
    { label: "500 Xu", color: "#0284C7" },
    { label: "1.000 Xu", color: "#059669" },
    { label: "+3 Vé Gắp", color: "#D97706" },
    { label: "+300 XP", color: "#2563EB" },
    { label: "Super Box", color: "#7C3AED" },
    { label: "30 Kim Cương", color: "#DB2777" },
    { label: "Thú Hiếm", color: "#0D9488" },
    { label: "2 Vé Vàng", color: "#CA8A04" },
    { label: "Skin Siêu Cấp", color: "#6D28D9" },
    { label: "SUPER JACKPOT", color: "#DC2626" }
];

const SLICES_GOLDEN = [
    { label: "50 Kim Cương", color: "#F59E0B" },
    { label: "Box Hoàng Gia", color: "#EAB308" },
    { label: "Thú Hoàng Gia", color: "#FBBF24" },
    { label: "+500 XP", color: "#FACC15" },
    { label: "Skin Thần Thoại", color: "#D97706" },
    { label: "100 Kim Cương", color: "#B45309" },
    { label: "Golden Cat", color: "#78350F" },
    { label: "3 Vé Vàng", color: "#FEF08A" },
    { label: "Secret Mascot", color: "#FDE047" },
    { label: "JACKPOT HOÀNG GIA", color: "#EF4444" }
];

function lay_tuan_hien_tai_web() {
    const now = new Date();
    const onejan = new Date(now.getFullYear(), 0, 1);
    const week = Math.ceil((((now - onejan) / 86400000) + onejan.getDay() + 1) / 7);
    return `${now.getFullYear()}-W${week}`;
}

function kiem_tra_tang_5_ve_vang_tuan_moi() {
    const currentWeek = lay_tuan_hien_tai_web();
    const lastWeek = localStorage.getItem('tuan_nhan_ve_vang');
    if (lastWeek !== currentWeek) {
        let vv = parseInt(localStorage.getItem('ve_vang') || '0', 10) + 5;
        localStorage.setItem('ve_vang', vv.toString());
        localStorage.setItem('tuan_nhan_ve_vang', currentWeek);
        console.log("Đã tự động cộng +5 Vé Vàng tuần mới cho học sinh!");
        return true;
    }
    return false;
}

function nhan_5_ve_vang_tuan_moi() {
    const currentWeek = lay_tuan_hien_tai_web();
    const lastWeek = localStorage.getItem('tuan_nhan_ve_vang');
    if (lastWeek !== currentWeek) {
        let vv = parseInt(localStorage.getItem('ve_vang') || '0', 10) + 5;
        localStorage.setItem('ve_vang', vv.toString());
        localStorage.setItem('tuan_nhan_ve_vang', currentWeek);
        cap_nhat_giao_dien_vong_quay_10_o();
        if (typeof cap_nhat_hien_thi_ve_gap === 'function') cap_nhat_hien_thi_ve_gap();
        alert("CHÚC MỪNG! Bạn đã nhận thành công +5 VÉ VÀNG MIỄN PHÍ của tuần này!");
    } else {
        alert("Bạn đã nhận 5 Vé Vàng miễn phí của tuần này rồi! Hãy chờ sang tuần mới hoặc hoàn thành nhiệm vụ ngày để nhận thêm Vé Vàng nhé!");
    }
}

function lay_du_lieu_vong_quay_web() {
    kiem_tra_tang_5_ve_vang_tuan_moi();

    let vq = parseInt(localStorage.getItem('ve_quay') || '5', 10);
    let vv = parseInt(localStorage.getItem('ve_vang') || '0', 10);
    let lm = parseInt(localStorage.getItem('lucky_meter') || '0', 10);
    let cq = parseInt(localStorage.getItem('chuoi_quay') || '0', 10);

    if (isNaN(vq)) vq = 5;
    if (isNaN(vv)) vv = 0;

    return { ve_quay: vq, ve_vang: vv, lucky_meter: lm, chuoi_quay: cq };
}

function cap_nhat_giao_dien_vong_quay_10_o() {
    const data = lay_du_lieu_vong_quay_web();
    
    const elemVeQuay = document.getElementById('lblVeQuayVal');
    const elemChuoi = document.getElementById('lblChuoiQuayVal');
    const elemLuckyMeter = document.getElementById('lblLuckyMeterPercent');
    const elemBar = document.getElementById('barLuckyMeterInner');

    if (elemVeQuay) elemVeQuay.innerText = `Vé Quay: ${data.ve_quay} | Vé Vàng: ${data.ve_vang}`;
    if (elemChuoi) elemChuoi.innerText = `Chuỗi Quay: ${data.chuoi_quay}`;
    if (elemLuckyMeter) elemLuckyMeter.innerText = `LUCKY METER: ${data.lucky_meter}%`;
    if (elemBar) elemBar.style.width = `${data.lucky_meter}%`;
}

function ve_vong_quay_10_o(angle = 0, loaiMode = 'thuong', canvasId = 'canvasWheel') {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width || 220;
    const h = canvas.height || 220;
    const cx = w / 2;
    const cy = h / 2;
    const radius = Math.min(cx, cy) - 6;

    let slices = SLICES_THUONG;
    if (loaiMode === 'super') slices = SLICES_SUPER;
    if (loaiMode === 'golden') slices = SLICES_GOLDEN;

    ctx.clearRect(0, 0, w, h);
    ctx.save();
    ctx.translate(cx, cy);
    ctx.rotate(angle);

    const sliceAngle = (Math.PI * 2) / 10;

    for (let i = 0; i < 10; i++) {
        const startAngle = i * sliceAngle;
        const endAngle = (i + 1) * sliceAngle;

        ctx.beginPath();
        ctx.fillStyle = slices[i].color;
        ctx.moveTo(0, 0);
        ctx.arc(0, 0, radius, startAngle, endAngle);
        ctx.fill();
        ctx.lineWidth = 2.5;
        ctx.strokeStyle = '#020617';
        ctx.stroke();

        ctx.save();
        ctx.rotate(startAngle + sliceAngle / 2);
        ctx.fillStyle = '#FFFFFF';
        ctx.font = '900 11.5px Outfit, sans-serif';
        ctx.textAlign = 'right';
        ctx.shadowColor = '#000000';
        ctx.shadowBlur = 4;
        ctx.fillText(slices[i].label, radius - 8, 4);
        ctx.restore();
    }

    // Central Cap
    ctx.beginPath();
    ctx.arc(0, 0, 22, 0, Math.PI * 2);
    ctx.fillStyle = '#020617';
    ctx.fill();
    ctx.lineWidth = 3;
    ctx.strokeStyle = (loaiMode === 'golden') ? '#F59E0B' : '#06B6D4';
    ctx.stroke();

    ctx.restore();
}

function bat_dau_quay_vong_quay_10_o(loaiQuay = 'thuong') {
    if (isWheel10Spinning) {
        console.warn("Resetting wheel spinning state fallback");
        isWheel10Spinning = false;
    }

    let data = lay_du_lieu_vong_quay_web();

    if (loaiQuay === 'golden') {
        if (data.ve_vang < 1) {
            alert("BẠN CHƯA CÓ VÉ VÀNG! Hãy làm nhiệm vụ ngày, đạt điểm 10 bài kiểm tra hoặc đạt chuỗi Streak 7 ngày để nhận Vé Vàng nhé!");
            const resDiv = document.getElementById('wheelResult');
            const resModalDiv = document.getElementById('modalWheelResult');
            const msgChuaCo = "BẠN CHƯA CÓ VÉ VÀNG! Làm nhiệm vụ ngày để nhận Vé Vàng!";
            if (resDiv) { resDiv.style.color = '#EF4444'; resDiv.innerText = msgChuaCo; }
            if (resModalDiv) { resModalDiv.style.color = '#EF4444'; resModalDiv.innerText = msgChuaCo; }
            return;
        }
        data.ve_vang -= 1;
        localStorage.setItem('ve_vang', data.ve_vang.toString());
    } else {
        if (data.ve_quay < 1) {
            alert("Bạn đã hết Vé Quay! Nhấn nút [+5 VÉ MIỄN PHÍ] hoặc hoàn thành 1 bài học để nhận thêm vé nhé!");
            const resDiv = document.getElementById('wheelResult');
            const resModalDiv = document.getElementById('modalWheelResult');
            const msgHetVe = "BẠN ĐÃ HẾT VÉ QUAY! Hãy bấm [+5 VÉ MIỄN PHÍ] để nhận thêm vé!";
            if (resDiv) { resDiv.style.color = '#EF4444'; resDiv.innerText = msgHetVe; }
            if (resModalDiv) { resModalDiv.style.color = '#EF4444'; resModalDiv.innerText = msgHetVe; }
            return;
        }
        data.ve_quay -= 1;
        localStorage.setItem('ve_quay', data.ve_quay.toString());
    }

    cap_nhat_giao_dien_vong_quay_10_o();

    isWheel10Spinning = true;
    try { playClickSfx(); } catch(e) {}

    const resDiv = document.getElementById('wheelResult');
    const resModalDiv = document.getElementById('modalWheelResult');
    const msgSpinning = `<div style="background: rgba(245, 158, 11, 0.2); border: 1.5px solid #F59E0B; padding: 8px 12px; border-radius: 10px; color: #F59E0B; font-weight: 900;">Vòng quay đang xoay tít siêu tốc...</div>`;
    if (resDiv) resDiv.innerHTML = msgSpinning;
    if (resModalDiv) resModalDiv.innerHTML = msgSpinning;

    // Roll Index target (0 - 9)
    let targetIndex = Math.floor(Math.random() * 10);
    const randRoll = Math.random() * 100;
    if (randRoll < 5) targetIndex = 9; // Jackpot 5%
    else if (randRoll < 20) targetIndex = 4; // CÓ LIỀN PHẦN QUÀ 15%

    const sliceAngle = (Math.PI * 2) / 10;
    const targetSliceAngle = targetIndex * sliceAngle + sliceAngle / 2;
    const totalSpinRotation = Math.PI * 2 * 8 + (Math.PI * 2 - targetSliceAngle); // 8 vong quay mượt mà
    const initialAngle = wheel10Angle;
    const spinDuration = 1500; // 1.5 giay xoay mượt mượt siêu đẹp
    let startTime = null;

    function animateSpin10(timestamp) {
        if (!startTime) startTime = timestamp;
        const elapsed = timestamp - startTime;
        const progress = Math.min(elapsed / spinDuration, 1);
        const easeOut = 1 - Math.pow(1 - progress, 3);

        wheel10Angle = initialAngle + totalSpinRotation * easeOut;
        ve_vong_quay_10_o(wheel10Angle, loaiQuay, 'canvasWheel');
        ve_vong_quay_10_o(wheel10Angle, loaiQuay, 'canvasModalWheel');

        if (progress < 1) {
            requestAnimationFrame(animateSpin10);
        } else {
            isWheel10Spinning = false;
            xuat_ket_qua_vong_quay_10_o(targetIndex, loaiQuay);
        }
    }

    requestAnimationFrame(animateSpin10);

    setTimeout(() => {
        if (isWheel10Spinning) {
            isWheel10Spinning = false;
            xuat_ket_qua_vong_quay_10_o(targetIndex, loaiQuay);
        }
    }, 2000);
}

function cong_xp_tai_khoan_web(amount) {
    let curXp = parseInt(localStorage.getItem('user_xp') || '1250', 10);
    curXp += amount;
    localStorage.setItem('user_xp', curXp.toString());

    let level = Math.floor(curXp / 250) + 1;
    let streak = parseInt(localStorage.getItem('user_streak') || '1', 10);

    const hdrLvl = document.getElementById('hdrUserLevel');
    if (hdrLvl) {
        hdrLvl.innerText = `Level ${level} | ${curXp} XP | ${streak} Streak`;
    }

    try {
        if (typeof updateXPDisplay === 'function') updateXPDisplay(amount);
    } catch(e) {}
}

function cong_xu_tai_khoan_web(amount) {
    let curCoins = parseInt(localStorage.getItem('user_coins') || '500', 10);
    curCoins += amount;
    localStorage.setItem('user_coins', curCoins.toString());
}

function cong_kim_cuong_tai_khoan_web(amount) {
    let curKc = parseInt(localStorage.getItem('user_diamonds') || '20', 10);
    curKc += amount;
    localStorage.setItem('user_diamonds', curKc.toString());
}

function them_vat_pham_kho_do(ten, loai) {
    let khoDo = [];
    try {
        khoDo = JSON.parse(localStorage.getItem('user_inventory') || '[]');
    } catch(e) { khoDo = []; }
    khoDo.push({
        ten: ten,
        loai: loai,
        thoi_gian: new Date().toLocaleString('vi-VN')
    });
    localStorage.setItem('user_inventory', JSON.stringify(khoDo));
}

function xuat_ket_qua_vong_quay_10_o(targetIndex, loaiQuay) {
    let data = lay_du_lieu_vong_quay_web();

    let slices = SLICES_THUONG;
    if (loaiQuay === 'golden') slices = SLICES_GOLDEN;
    else if (data.lucky_meter >= 100) slices = SLICES_SUPER;

    const reward = slices[targetIndex];

    // Cap nhat Lucky Meter (+20% moi luot)
    if (data.lucky_meter >= 100) {
        data.lucky_meter = 0;
    } else {
        data.lucky_meter = Math.min(100, data.lucky_meter + 20);
    }
    data.chuoi_quay += 1;
    localStorage.setItem('lucky_meter', data.lucky_meter.toString());
    localStorage.setItem('chuoi_quay', data.chuoi_quay.toString());

    let strMsg = '';
    let msgBackground = 'linear-gradient(135deg, #10B981, #06B6D4)';

    // 1. TRƯỜNG HỢP JACKPOT: VÀO VÍ VÉ (+1 VÉ VÀNG + 5 VÉ THƯỜNG) VÀ VÀO TÀI KHOẢN (+1000 XP)
    if (reward.label.toUpperCase().includes("JACKPOT")) {
        let soVeVang = 1;
        let soVeThuong = 5;
        let soXp = 1000;

        if (reward.label.includes("SUPER")) {
            soVeVang = 2;
            soVeThuong = 10;
            soXp = 2000;
        } else if (reward.label.includes("HOÀNG GIA")) {
            soVeVang = 3;
            soVeThuong = 15;
            soXp = 5000;
        }

        // Cập nhật vào VÍ VÉ
        let vv = parseInt(localStorage.getItem('ve_vang') || '0', 10) + soVeVang;
        let vq = parseInt(localStorage.getItem('ve_quay') || '5', 10) + soVeThuong;
        let vg = parseInt(localStorage.getItem('ve_gap') || '5', 10) + soVeThuong;
        localStorage.setItem('ve_vang', vv.toString());
        localStorage.setItem('ve_quay', vq.toString());
        localStorage.setItem('ve_gap', vg.toString());

        // Cộng vào TÀI KHOẢN
        cong_xp_tai_khoan_web(soXp);
        them_vat_pham_kho_do(reward.label, "jackpot");

        msgBackground = 'linear-gradient(135deg, #EF4444, #F59E0B)';
        strMsg = `🎉 TRÚNG JACKPOT HUYỀN THOẠI! 🎉<br>• VÀO VÍ VÉ: +${soVeVang} Vé Vàng | +${soVeThuong} Vé Thường<br>• VÀO TÀI KHOẢN: +${soXp} XP Tích Lũy & Rương Jackpot!`;
    }
    // 2. CÁC PHẦN THƯỞNG VÉ -> CẬP NHẬT VÀO VÍ VÉ
    else if (reward.label.includes("Vé Gắp")) {
        let soLuong = 1;
        if (reward.label.includes("3")) soLuong = 3;
        let v = parseInt(localStorage.getItem('ve_gap') || '5', 10) + soLuong;
        localStorage.setItem('ve_gap', v.toString());
        strMsg = `CHÚC MỪNG: TRÚNG ${reward.label.toUpperCase()}!<br>(ĐÃ CẬP NHẬT +${soLuong} VÉ VÀO VÍ VÉ GẮP THÚ)`;
    }
    else if (reward.label.includes("Golden Ticket") || reward.label.includes("Vé Vàng")) {
        let soLuongVang = 1;
        if (reward.label.includes("2")) soLuongVang = 2;
        if (reward.label.includes("3")) soLuongVang = 3;
        let vv = parseInt(localStorage.getItem('ve_vang') || '0', 10) + soLuongVang;
        localStorage.setItem('ve_vang', vv.toString());
        strMsg = `CHÚC MỪNG: TRÚNG ${reward.label.toUpperCase()}!<br>(ĐÃ CẬP NHẬT +${soLuongVang} VÉ VÀNG VÀO VÍ VÉ)`;
    }
    else if (reward.label.includes("Vé Quay")) {
        let soLuongQuay = 1;
        if (reward.label.includes("3")) soLuongQuay = 3;
        let vq = parseInt(localStorage.getItem('ve_quay') || '5', 10) + soLuongQuay;
        localStorage.setItem('ve_quay', vq.toString());
        strMsg = `CHÚC MỪNG: TRÚNG ${reward.label.toUpperCase()}!<br>(ĐÃ CẬP NHẬT +${soLuongQuay} VÉ VÀO VÍ VÉ QUAY)`;
    }
    // 3. CÁC PHẦN THƯỞNG CÒN LẠI -> CỘNG TRỰC TIẾP VÀO TÀI KHOẢN
    else {
        if (reward.label.includes("Xu")) {
            let soXu = 100;
            if (reward.label.includes("250")) soXu = 250;
            else if (reward.label.includes("500")) soXu = 500;
            else if (reward.label.includes("1.000") || reward.label.includes("1000")) soXu = 1000;
            cong_xu_tai_khoan_web(soXu);
            strMsg = `CHÚC MỪNG: TRÚNG ${reward.label.toUpperCase()}!<br>(ĐÃ CỘNG +${soXu} XU VÀO TÀI KHOẢN)`;
        }
        else if (reward.label.includes("XP")) {
            let soXp = 100;
            if (reward.label.includes("300")) soXp = 300;
            else if (reward.label.includes("500")) soXp = 500;
            cong_xp_tai_khoan_web(soXp);
            strMsg = `CHÚC MỪNG: TRÚNG ${reward.label.toUpperCase()}!<br>(ĐÃ CỘNG +${soXp} XP VÀO TÀI KHOẢN)`;
        }
        else if (reward.label.includes("Kim Cương")) {
            let soKc = 10;
            if (reward.label.includes("30")) soKc = 30;
            else if (reward.label.includes("50")) soKc = 50;
            else if (reward.label.includes("100")) soKc = 100;
            cong_kim_cuong_tai_khoan_web(soKc);
            strMsg = `CHÚC MỪNG: TRÚNG ${reward.label.toUpperCase()}!<br>(ĐÃ CỘNG +${soKc} KIM CƯƠNG VÀO TÀI KHOẢN)`;
        }
        else if (reward.label.includes("Skin")) {
            them_vat_pham_kho_do(reward.label, "skin");
            cong_xp_tai_khoan_web(200);
            strMsg = `CHÚC MỪNG: TRÚNG ${reward.label.toUpperCase()}!<br>(ĐÃ THÊM SKIN VÀO KHO ĐỒ TÀI KHOẢN & +200 XP)`;
        }
        else if (reward.label.includes("Box") || reward.label.includes("Mystery")) {
            them_vat_pham_kho_do(reward.label, "box");
            cong_xp_tai_khoan_web(250);
            strMsg = `CHÚC MỪNG: TRÚNG ${reward.label.toUpperCase()}!<br>(ĐÃ THÊM HỘP QUÀ VÀO KHO ĐỒ TÀI KHOẢN & +250 XP)`;
        }
        else {
            them_vat_pham_kho_do(reward.label, "mascot");
            cong_xp_tai_khoan_web(300);
            strMsg = `CHÚC MỪNG: TRÚNG ${reward.label.toUpperCase()}!<br>(ĐÃ THÊM LINH VẬT VÀO KHO ĐỒ TÀI KHOẢN & +300 XP)`;
        }
    }

    // Đồng bộ cập nhật giao diện Ví Vé và Máy Gắp Thú ngay lập tức
    cap_nhat_giao_dien_vong_quay_10_o();
    if (typeof cap_nhat_hien_thi_ve_gap === 'function') {
        cap_nhat_hien_thi_ve_gap();
    }

    const resDiv = document.getElementById('wheelResult');
    const resModalDiv = document.getElementById('modalWheelResult');

    if (resDiv) {
        resDiv.innerHTML = `<div style="background: ${msgBackground}; padding: 12px 16px; border-radius: 14px; font-weight: 900; color: #FFFFFF; text-shadow: 0 2px 4px rgba(0,0,0,0.5); margin-top: 8px; line-height: 1.5;">${strMsg}</div>`;
    }
    if (resModalDiv) {
        resModalDiv.innerHTML = `<div style="background: ${msgBackground}; padding: 12px 16px; border-radius: 14px; font-weight: 900; color: #FFFFFF; text-shadow: 0 2px 4px rgba(0,0,0,0.5); margin-top: 8px; line-height: 1.5;">${strMsg}</div>`;
    }
}

window.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        cap_nhat_giao_dien_vong_quay_10_o();
        ve_vong_quay_10_o(0, 'thuong', 'canvasWheel');
        ve_vong_quay_10_o(0, 'thuong', 'canvasModalWheel');
    }, 300);
});

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

function lay_du_lieu_vong_quay_web() {
    let vq = parseInt(localStorage.getItem('ve_quay') || '3', 10);
    let vv = parseInt(localStorage.getItem('ve_vang') || '1', 10);
    let lm = parseInt(localStorage.getItem('lucky_meter') || '0', 10);
    let cq = parseInt(localStorage.getItem('chuoi_quay') || '0', 10);

    const todayStr = new Date().toISOString().split('T')[0];
    const lastDate = localStorage.getItem('ngay_nhan_ve_quay');
    if (lastDate !== todayStr) {
        vq = Math.max(3, vq + 1);
        localStorage.setItem('ve_quay', vq.toString());
        localStorage.setItem('ngay_nhan_ve_quay', todayStr);
    }

    return { ve_quay: vq, ve_vang: vv, lucky_meter: lm, chuoi_quay: cq };
}

function cap_nhat_giao_dien_vong_quay_10_o() {
    const data = lay_du_lieu_vong_quay_web();
    
    const elemVeQuay = document.getElementById('lblVeQuayVal');
    const elemChuoi = document.getElementById('lblChuoiQuayVal');
    const elemLuckyMeter = document.getElementById('lblLuckyMeterPercent');
    const elemBar = document.getElementById('barLuckyMeterInner');

    if (elemVeQuay) elemVeQuay.innerText = `Vé Quay: ${data.ve_quay}`;
    if (elemChuoi) elemChuoi.innerText = `Chuỗi Quay: ${data.chuoi_quay}`;
    if (elemLuckyMeter) elemLuckyMeter.innerText = `LUCKY METER: ${data.lucky_meter}%`;
    if (elemBar) elemBar.style.width = `${data.lucky_meter}%`;
}

function ve_vong_quay_10_o(angle = 0, loaiMode = 'thuong', canvasId = 'canvasWheel') {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width || 240;
    const h = canvas.height || 240;
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
        ctx.lineWidth = 2;
        ctx.strokeStyle = '#020617';
        ctx.stroke();

        ctx.save();
        ctx.rotate(startAngle + sliceAngle / 2);
        ctx.fillStyle = '#FFFFFF';
        ctx.font = '900 11px Outfit';
        ctx.textAlign = 'right';
        ctx.fillText(slices[i].label, radius - 10, 4);
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
    if (isWheel10Spinning) return;

    let data = lay_du_lieu_vong_quay_web();

    if (loaiQuay === 'golden') {
        if (data.ve_vang < 1) {
            alert("Bạn chưa có VÉ VÀNG! Hãy điểm danh 7 ngày hoặc đạt điểm 10 kiểm tra để nhận Vé Vàng nhé!");
            return;
        }
        data.ve_vang -= 1;
        localStorage.setItem('ve_vang', data.ve_vang.toString());
    } else {
        if (data.ve_quay < 1) {
            alert("Bạn đã hết Vé Quay! Hãy hoàn thành 1 bài học để nhận thêm Vé Quay nhé!");
            return;
        }
        data.ve_quay -= 1;
        localStorage.setItem('ve_quay', data.ve_quay.toString());
    }

    isWheel10Spinning = true;
    try { playClickSfx(); } catch(e) {}

    const resDiv = document.getElementById('wheelResult');
    if (resDiv) {
        resDiv.style.color = '#F59E0B';
        resDiv.innerText = 'Vòng quay 10 ô đang xoay tít siêu tốc... Đang chờ kết quả!';
    }

    // Roll Index target (0 - 9)
    let targetIndex = Math.floor(Math.random() * 10);
    const randRoll = Math.random() * 100;
    if (randRoll < 3) targetIndex = 9; // Jackpot 3%
    else if (randRoll < 15) targetIndex = 7; // Golden Ticket 12%

    const sliceAngle = (Math.PI * 2) / 10;
    const targetSliceAngle = targetIndex * sliceAngle + sliceAngle / 2;
    const totalSpinRotation = Math.PI * 2 * 3 + (Math.PI * 2 - targetSliceAngle); // 3 vong quay chop nhang
    const initialAngle = wheel10Angle;
    const spinDuration = 300; // 0.3s nhan qua ngay lap tuc
    let startTime = null;

    function animateSpin10(timestamp) {
        if (!startTime) startTime = timestamp;
        const elapsed = timestamp - startTime;
        const progress = Math.min(elapsed / spinDuration, 1);
        const easeOut = 1 - Math.pow(1 - progress, 4);

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

    cap_nhat_giao_dien_vong_quay_10_o();

    if (reward.label.includes("Vé Gắp")) {
        let v = parseInt(localStorage.getItem('ve_gap') || '3', 10) + 1;
        localStorage.setItem('ve_gap', v.toString());
    } else if (reward.label.includes("Golden Ticket") || reward.label.includes("Vé Vàng")) {
        let vv = parseInt(localStorage.getItem('ve_vang') || '1', 10) + 1;
        localStorage.setItem('ve_vang', vv.toString());
    }

    if (typeof updateXPDisplay === 'function') updateXPDisplay(150);

    const resDiv = document.getElementById('wheelResult');
    const resModalDiv = document.getElementById('modalWheelResult');
    const strMsg = `CHÚC MỪNG: TRÚNG ${reward.label.toUpperCase()}! (CỘNG NGAY VÀO TÀI KHOẢN)`;

    if (resDiv) {
        resDiv.innerHTML = `<div style="background: linear-gradient(135deg, #10B981, #06B6D4); padding: 10px 14px; border-radius: 12px; font-weight: 900; color: #FFFFFF; text-shadow: 0 2px 4px rgba(0,0,0,0.5); margin-top: 8px;">${strMsg}</div>`;
    }
    if (resModalDiv) {
        resModalDiv.innerHTML = `<div style="background: linear-gradient(135deg, #10B981, #06B6D4); padding: 10px 14px; border-radius: 12px; font-weight: 900; color: #FFFFFF; text-shadow: 0 2px 4px rgba(0,0,0,0.5); margin-top: 8px;">${strMsg}</div>`;
    }
}

window.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        cap_nhat_giao_dien_vong_quay_10_o();
        ve_vong_quay_10_o(0, 'thuong', 'canvasWheel');
        ve_vong_quay_10_o(0, 'thuong', 'canvasModalWheel');
    }, 300);
});

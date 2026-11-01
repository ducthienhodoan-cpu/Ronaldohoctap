// Thu muc: public/xu_ly_3d
// File: video_penalty_3d.js
// Mo ta: Hoat canh Video 3D Penalty 60 FPS mo phong sut phat Cup C1, World Cup va Minigame
// Quy tac: Dung 100% ty le 100% vao goc khi dung, 50% sut len troi va 50% thu mon can pha khi sai. Khong dung icon.

(function() {
    // 1. Khoi tao Web Audio Context de tao am thanh song dong khong bi lag
    let audioCtx = null;
    function getAudioContext() {
        if (!audioCtx) {
            const AudioContextClass = window.AudioContext || window.webkitAudioContext;
            if (AudioContextClass) {
                audioCtx = new AudioContextClass();
            }
        }
        if (audioCtx && audioCtx.state === 'suspended') {
            audioCtx.resume();
        }
        return audioCtx;
    }

    function playWhistleSound() {
        try {
            const ctx = getAudioContext();
            if (!ctx) return;
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(2200, ctx.currentTime);
            osc.frequency.exponentialRampToValueAtTime(2800, ctx.currentTime + 0.12);
            osc.frequency.exponentialRampToValueAtTime(2400, ctx.currentTime + 0.25);
            gain.gain.setValueAtTime(0.18, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.28);
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start();
            osc.stop(ctx.currentTime + 0.3);
        } catch(e) {}
    }

    function playKickSound() {
        try {
            const ctx = getAudioContext();
            if (!ctx) return;
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(160, ctx.currentTime);
            osc.frequency.exponentialRampToValueAtTime(35, ctx.currentTime + 0.14);
            gain.gain.setValueAtTime(0.4, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.16);
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start();
            osc.stop(ctx.currentTime + 0.18);
        } catch(e) {}
    }

    function playGoalCheerSound() {
        try {
            const ctx = getAudioContext();
            if (!ctx) return;
            // Am thanh co vu reo ho cua khan gia san van dong
            const bufferSize = ctx.sampleRate * 1.5;
            const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
            const data = buffer.getChannelData(0);
            for (let i = 0; i < bufferSize; i++) {
                data[i] = Math.random() * 2 - 1;
            }
            const noise = ctx.createBufferSource();
            noise.buffer = buffer;
            const filter = ctx.createBiquadFilter();
            filter.type = 'bandpass';
            filter.frequency.setValueAtTime(700, ctx.currentTime);
            filter.Q.setValueAtTime(1.2, ctx.currentTime);

            const gain = ctx.createGain();
            gain.gain.setValueAtTime(0.01, ctx.currentTime);
            gain.gain.linearRampToValueAtTime(0.25, ctx.currentTime + 0.3);
            gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 1.4);

            noise.connect(filter);
            filter.connect(gain);
            gain.connect(ctx.destination);
            noise.start();
            noise.stop(ctx.currentTime + 1.5);
        } catch(e) {}
    }

    function playSaveSound() {
        try {
            const ctx = getAudioContext();
            if (!ctx) return;
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.type = 'square';
            osc.frequency.setValueAtTime(180, ctx.currentTime);
            osc.frequency.exponentialRampToValueAtTime(60, ctx.currentTime + 0.18);
            gain.gain.setValueAtTime(0.25, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.2);
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start();
            osc.stop(ctx.currentTime + 0.22);
        } catch(e) {}
    }

    // 2. Ham sinh ket qua logic Penalty theo quy tac chuan
    function sinhKetQuaPenaltyJs(laTraLoiDung, gocChiDinh) {
        const danhSachGoc = [
            { id: 1, ten: "Góc Cao Trái", tx: -0.65, ty: -0.58 },
            { id: 2, ten: "Góc Thấp Trái", tx: -0.65, ty: 0.55 },
            { id: 3, ten: "Chính Giữa", tx: 0.0, ty: -0.15 },
            { id: 4, ten: "Góc Cao Phải", tx: 0.65, ty: -0.58 },
            { id: 5, ten: "Góc Thấp Phải", tx: 0.65, ty: 0.55 }
        ];

        if (laTraLoiDung) {
            let gocChon = danhSachGoc[Math.floor(Math.random() * danhSachGoc.length)];
            if (gocChiDinh) {
                const timGoc = danhSachGoc.find(g => gocChiDinh.toLowerCase().includes(g.ten.toLowerCase()));
                if (timGoc) gocChon = timGoc;
            }

            // Thu mon bay huong nguoc lai de dam bao 100% vao luoi
            let huongThuMon = danhSachGoc.filter(g => g.id !== gocChon.id)[Math.floor(Math.random() * 4)];

            return {
                la_ban_thang: true,
                ket_qua: "vao",
                goc_id: gocChon.id,
                goc_ten: gocChon.ten,
                target_x: gocChon.tx,
                target_y: gocChon.ty,
                thu_mon_x: huongThuMon.tx,
                thu_mon_y: huongThuMon.ty,
                tieu_de: "VAOOOOOO! BAN THANG TUYET DINH!",
                mo_ta: `Cu sut cuc ki hiem hoc vao ${gocChon.ten} danh bai thu mon hoan toan!`
            };
        } else {
            // Khi tra loi sai: 50% sut len troi, 50% thu mon can pha
            const chonKieuTruot = Math.random() < 0.5 ? "sut_len_troi" : "thu_mon_can_pha";

            if (chonKieuTruot === "sut_len_troi") {
                const lechX = (Math.random() * 0.7) - 0.35;
                return {
                    la_ban_thang: false,
                    ket_qua: "sut_len_troi",
                    goc_id: 0,
                    goc_ten: "Sút Vọt Xà",
                    target_x: lechX,
                    target_y: -1.75, // Bay cao vut len troi qua xa ngang
                    thu_mon_x: 0,
                    thu_mon_y: 0,
                    tieu_de: "SUT LEN TROI! BONG BAY QUA XA NGANG!",
                    mo_ta: "Luc sut qua manh dua bong bay vot len khan dai trong su tiec nuoi!"
                };
            } else {
                const gocBay = danhSachGoc[Math.floor(Math.random() * danhSachGoc.length)];
                return {
                    la_ban_thang: false,
                    ket_qua: "thu_mon_can_pha",
                    goc_id: gocBay.id,
                    goc_ten: gocBay.ten,
                    target_x: gocBay.tx,
                    target_y: gocBay.ty,
                    thu_mon_x: gocBay.tx, // Thu mon bay dung huong va can pha
                    thu_mon_y: gocBay.ty,
                    tieu_de: "THU MON CAN PHA XUAT SAC!",
                    mo_ta: `Thu mon da phan doan chinh xac huong ${gocBay.ten} va can pha thanh cong!`
                };
            }
        }
    }

    // 3. Tao DOM Modal Container neu chua co
    let modalOverlay = null;
    let canvasEl = null;
    let ctx2d = null;
    let animFrameId = null;

    function buildModalDOM() {
        if (document.getElementById('penaltyVideoModalOverlay')) {
            modalOverlay = document.getElementById('penaltyVideoModalOverlay');
            canvasEl = document.getElementById('penaltyVideoCanvas');
            ctx2d = canvasEl.getContext('2d');
            return;
        }

        modalOverlay = document.createElement('div');
        modalOverlay.id = 'penaltyVideoModalOverlay';
        modalOverlay.style.position = 'fixed';
        modalOverlay.style.top = '0';
        modalOverlay.style.left = '0';
        modalOverlay.style.width = '100vw';
        modalOverlay.style.height = '100vh';
        modalOverlay.style.backgroundColor = 'rgba(2, 6, 23, 0.88)';
        modalOverlay.style.backdropFilter = 'blur(16px)';
        modalOverlay.style.zIndex = '99999';
        modalOverlay.style.display = 'none';
        modalOverlay.style.alignItems = 'center';
        modalOverlay.style.justifyContent = 'center';
        modalOverlay.style.padding = '16px';
        modalOverlay.style.boxSizing = 'border-box';

        const modalBox = document.createElement('div');
        modalBox.style.width = '100%';
        modalBox.style.maxWidth = '840px';
        modalBox.style.backgroundColor = '#0F172A';
        modalBox.style.border = '3px solid #06B6D4';
        modalBox.style.borderRadius = '24px';
        modalBox.style.overflow = 'hidden';
        modalBox.style.boxShadow = '0 0 50px rgba(6, 182, 212, 0.6)';
        modalBox.style.display = 'flex';
        modalBox.style.flexDirection = 'column';
        modalBox.style.position = 'relative';

        // Header
        const header = document.createElement('div');
        header.style.padding = '14px 22px';
        header.style.background = 'linear-gradient(90deg, #0F172A, #1E293B)';
        header.style.borderBottom = '2px solid rgba(6, 182, 212, 0.4)';
        header.style.display = 'flex';
        header.style.alignItems = 'center';
        header.style.justifyContent = 'space-between';

        const titleEl = document.createElement('h3');
        titleEl.id = 'penaltyModalHeaderTitle';
        titleEl.innerText = 'TRUYỀN HÌNH TRỰC TIẾP: CÚ SÚT PENALTY';
        titleEl.style.color = '#00FFCC';
        titleEl.style.fontFamily = 'var(--font-heading), sans-serif';
        titleEl.style.fontWeight = '900';
        titleEl.style.fontSize = '16px';
        titleEl.style.letterSpacing = '0.5px';
        titleEl.style.margin = '0';

        const btnSkip = document.createElement('button');
        btnSkip.innerText = 'Bỏ qua hoạt cảnh';
        btnSkip.style.background = 'rgba(255, 255, 255, 0.1)';
        btnSkip.style.border = '1px solid rgba(255, 255, 255, 0.3)';
        btnSkip.style.color = '#FFFFFF';
        btnSkip.style.padding = '6px 14px';
        btnSkip.style.borderRadius = '12px';
        btnSkip.style.cursor = 'pointer';
        btnSkip.style.fontWeight = '700';
        btnSkip.style.fontSize = '13px';
        btnSkip.onclick = function() {
            closePenaltyModal();
        };

        header.appendChild(titleEl);
        header.appendChild(btnSkip);
        modalBox.appendChild(header);

        // Canvas Area
        const canvasWrapper = document.createElement('div');
        canvasWrapper.style.position = 'relative';
        canvasWrapper.style.width = '100%';
        canvasWrapper.style.height = '440px';
        canvasWrapper.style.backgroundColor = '#021a12';
        canvasWrapper.style.overflow = 'hidden';

        canvasEl = document.createElement('canvas');
        canvasEl.id = 'penaltyVideoCanvas';
        canvasEl.width = 840;
        canvasEl.height = 440;
        canvasEl.style.width = '100%';
        canvasEl.style.height = '100%';
        canvasEl.style.display = 'block';

        // Banner Overlay inside canvas
        const bannerOverlay = document.createElement('div');
        bannerOverlay.id = 'penaltyBannerOverlay';
        bannerOverlay.style.position = 'absolute';
        bannerOverlay.style.bottom = '18px';
        bannerOverlay.style.left = '50%';
        bannerOverlay.style.transform = 'translateX(-50%)';
        bannerOverlay.style.width = '90%';
        bannerOverlay.style.maxWidth = '680px';
        bannerOverlay.style.padding = '14px 20px';
        bannerOverlay.style.borderRadius = '16px';
        bannerOverlay.style.textAlign = 'center';
        bannerOverlay.style.display = 'none';
        bannerOverlay.style.backdropFilter = 'blur(12px)';
        bannerOverlay.style.boxShadow = '0 10px 30px rgba(0,0,0,0.8)';
        bannerOverlay.style.transition = 'all 0.3s ease';

        const bannerTitle = document.createElement('div');
        bannerTitle.id = 'penaltyBannerTitle';
        bannerTitle.style.fontSize = '20px';
        bannerTitle.style.fontWeight = '900';
        bannerTitle.style.marginBottom = '6px';

        const bannerDesc = document.createElement('div');
        bannerDesc.id = 'penaltyBannerDesc';
        bannerDesc.style.fontSize = '14px';
        bannerDesc.style.fontWeight = '700';
        bannerDesc.style.color = '#F1F5F9';

        bannerOverlay.appendChild(bannerTitle);
        bannerOverlay.appendChild(bannerDesc);

        canvasWrapper.appendChild(canvasEl);
        canvasWrapper.appendChild(bannerOverlay);
        modalBox.appendChild(canvasWrapper);

        // Footer Action
        const footer = document.createElement('div');
        footer.style.padding = '14px 22px';
        footer.style.background = '#091B15';
        footer.style.display = 'flex';
        footer.style.alignItems = 'center';
        footer.style.justifyContent = 'space-between';
        footer.style.borderTop = '2px solid rgba(255, 255, 255, 0.1)';

        const footerInfo = document.createElement('div');
        footerInfo.id = 'penaltyFooterInfo';
        footerInfo.innerText = 'Trọng tài chuẩn bị nổi còi thực hiện quả đá 11m...';
        footerInfo.style.color = '#94A3B8';
        footerInfo.style.fontSize = '14px';
        footerInfo.style.fontWeight = '700';

        const btnContinue = document.createElement('button');
        btnContinue.id = 'penaltyBtnContinue';
        btnContinue.innerText = 'Tiếp Tục Trận Đấu';
        btnContinue.style.background = 'linear-gradient(135deg, #10B981, #059669)';
        btnContinue.style.border = 'none';
        btnContinue.style.color = '#FFFFFF';
        btnContinue.style.padding = '10px 24px';
        btnContinue.style.borderRadius = '14px';
        btnContinue.style.fontWeight = '800';
        btnContinue.style.fontSize = '15px';
        btnContinue.style.cursor = 'pointer';
        btnContinue.style.boxShadow = '0 0 15px rgba(16, 185, 129, 0.5)';
        btnContinue.onclick = function() {
            closePenaltyModal();
        };

        footer.appendChild(footerInfo);
        footer.appendChild(btnContinue);
        modalBox.appendChild(footer);

        modalOverlay.appendChild(modalBox);
        document.body.appendChild(modalOverlay);

        ctx2d = canvasEl.getContext('2d');
    }

    let currentFinishedCallback = null;
    let autoCloseTimer = null;

    function closePenaltyModal() {
        if (animFrameId) {
            cancelAnimationFrame(animFrameId);
            animFrameId = null;
        }
        if (autoCloseTimer) {
            clearTimeout(autoCloseTimer);
            autoCloseTimer = null;
        }
        if (modalOverlay) {
            modalOverlay.style.display = 'none';
        }
        if (typeof currentFinishedCallback === 'function') {
            const cb = currentFinishedCallback;
            currentFinishedCallback = null;
            cb();
        }
    }

    // 4. Ham chay Simulation 60 FPS Canvas
    function runPenaltySimulation(resPen, onFinished) {
        buildModalDOM();
        currentFinishedCallback = onFinished;
        modalOverlay.style.display = 'flex';

        const bannerOverlay = document.getElementById('penaltyBannerOverlay');
        const bannerTitle = document.getElementById('penaltyBannerTitle');
        const bannerDesc = document.getElementById('penaltyBannerDesc');
        const footerInfo = document.getElementById('penaltyFooterInfo');

        bannerOverlay.style.display = 'none';
        footerInfo.innerText = 'Cầu thủ đang lấy đà sút phạt...';

        playWhistleSound();

        const W = canvasEl.width;
        const H = canvasEl.height;

        // Thiet lap khung thanh (Goal Dimensions in 3D Perspective)
        const goal = {
            left: W * 0.22,
            right: W * 0.78,
            top: H * 0.22,
            bottom: H * 0.72,
            width: W * 0.56,
            height: H * 0.50,
            depth: 70
        };

        // Vi tri bong
        const startBallX = W * 0.5;
        const startBallY = H * 0.88;
        const startBallR = 18;

        // Diem muc tieu cua bong
        let targetX = W * 0.5 + (resPen.target_x * goal.width * 0.44);
        let targetY = goal.top + ((resPen.target_y + 1) * 0.5 * goal.height);

        if (resPen.ket_qua === 'sut_len_troi') {
            targetY = -80; // Vot len troi
            targetX = W * 0.5 + (resPen.target_x * goal.width * 0.5);
        }

        // Diem dich cua thu mon
        const gkBaseX = W * 0.5;
        const gkBaseY = goal.bottom - 4;
        let gkTargetX = W * 0.5 + (resPen.thu_mon_x * goal.width * 0.42);
        let gkTargetY = goal.top + ((resPen.thu_mon_y + 1) * 0.5 * goal.height);

        // State hoat canh
        let startTime = performance.now();
        const duration = 2400; // ms
        let netVibration = 0;
        let particles = [];
        let hasKicked = false;
        let hasHitResult = false;

        function renderFrame(now) {
            const elapsed = now - startTime;
            const progress = Math.min(1.0, elapsed / 1800); // Thoi gian bay 1.8s

            // Xoa nen
            ctx2d.clearRect(0, 0, W, H);

            // 1. Ve San van dong va Khong gian 3D
            const gradSky = ctx2d.createLinearGradient(0, 0, 0, H * 0.45);
            gradSky.addColorStop(0, '#020617');
            gradSky.addColorStop(0.6, '#0B192C');
            gradSky.addColorStop(1, '#06281E');
            ctx2d.fillStyle = gradSky;
            ctx2d.fillRect(0, 0, W, H * 0.45);

            // Dan den chieu sang san van dong (Floodlights)
            ctx2d.save();
            ctx2d.globalAlpha = 0.15;
            const gradLightL = ctx2d.createRadialGradient(W * 0.1, 40, 10, W * 0.1, 40, 380);
            gradLightL.addColorStop(0, '#00FFCC');
            gradLightL.addColorStop(1, 'transparent');
            ctx2d.fillStyle = gradLightL;
            ctx2d.fillRect(0, 0, W, H);

            const gradLightR = ctx2d.createRadialGradient(W * 0.9, 40, 10, W * 0.9, 40, 380);
            gradLightR.addColorStop(0, '#38BDF8');
            gradLightR.addColorStop(1, 'transparent');
            ctx2d.fillStyle = gradLightR;
            ctx2d.fillRect(0, 0, W, H);
            ctx2d.restore();

            // Mat co xanh 3D co soc san co
            const gradGrass = ctx2d.createLinearGradient(0, H * 0.42, 0, H);
            gradGrass.addColorStop(0, '#064E3B');
            gradGrass.addColorStop(0.4, '#047857');
            gradGrass.addColorStop(1, '#022C22');
            ctx2d.fillStyle = gradGrass;
            ctx2d.fillRect(0, H * 0.42, W, H * 0.58);

            // Cac duong soc co 3D
            for (let i = 0; i < 6; i++) {
                const y1 = H * (0.42 + i * 0.1);
                const y2 = H * (0.42 + (i + 0.5) * 0.1);
                ctx2d.fillStyle = i % 2 === 0 ? 'rgba(16, 185, 129, 0.12)' : 'rgba(0, 0, 0, 0.12)';
                ctx2d.fillRect(0, y1, W, y2 - y1);
            }

            // Vach ke vung cam dia va diem cham 11m
            ctx2d.strokeStyle = 'rgba(255, 255, 255, 0.6)';
            ctx2d.lineWidth = 3;
            ctx2d.beginPath();
            ctx2d.ellipse(W * 0.5, H * 0.72, W * 0.28, 45, 0, 0, Math.PI * 2);
            ctx2d.stroke();

            // Cham trang 11m
            ctx2d.fillStyle = '#FFFFFF';
            ctx2d.beginPath();
            ctx2d.arc(W * 0.5, startBallY, 5, 0, Math.PI * 2);
            ctx2d.fill();

            // 2. Ve Khung thanh va Luoi bong (3D Goal & Net)
            ctx2d.save();
            // Khung sau cua luoi (Hau luoi)
            const netBackLeft = goal.left + 25;
            const netBackRight = goal.right - 25;
            const netBackTop = goal.top - 20;

            // Luoi san co rung rinh
            const vib = Math.sin(now * 0.08) * netVibration;
            ctx2d.strokeStyle = 'rgba(255, 255, 255, 0.35)';
            ctx2d.lineWidth = 1;

            // Cac duong luoi ngang
            const netRows = 12;
            for (let r = 0; r <= netRows; r++) {
                const nyFront = goal.top + (r / netRows) * goal.height;
                const nyBack = netBackTop + (r / netRows) * (goal.height + 20) + (r > 2 ? vib : 0);
                ctx2d.beginPath();
                ctx2d.moveTo(netBackLeft, nyBack);
                ctx2d.lineTo(netBackRight, nyBack);
                ctx2d.stroke();

                ctx2d.beginPath();
                ctx2d.moveTo(goal.left, nyFront);
                ctx2d.lineTo(goal.right, nyFront);
                ctx2d.stroke();
            }

            // Cac duong luoi doc
            const netCols = 20;
            for (let c = 0; c <= netCols; c++) {
                const nxFront = goal.left + (c / netCols) * goal.width;
                const nxBack = netBackLeft + (c / netCols) * (netBackRight - netBackLeft) + vib * 0.5;
                ctx2d.beginPath();
                ctx2d.moveTo(nxFront, goal.top);
                ctx2d.lineTo(nxBack, netBackTop);
                ctx2d.lineTo(nxBack, goal.bottom);
                ctx2d.lineTo(nxFront, goal.bottom);
                ctx2d.stroke();
            }

            // Xa ngang va Cot doc khung thanh mau trang sang bong
            ctx2d.strokeStyle = '#FFFFFF';
            ctx2d.lineWidth = 8;
            ctx2d.lineCap = 'round';
            ctx2d.lineJoin = 'round';
            ctx2d.shadowColor = 'rgba(255, 255, 255, 0.8)';
            ctx2d.shadowBlur = 10;

            ctx2d.beginPath();
            ctx2d.moveTo(goal.left, goal.bottom);
            ctx2d.lineTo(goal.left, goal.top);
            ctx2d.lineTo(goal.right, goal.top);
            ctx2d.lineTo(goal.right, goal.bottom);
            ctx2d.stroke();
            ctx2d.restore();

            // 3. Tinh toan Chuyen dong cua Bong va Thu Mon theo thoi gian
            if (!hasKicked && elapsed > 250) {
                hasKicked = true;
                playKickSound();
                footerInfo.innerText = 'Bóng đã rời chân cầu thủ với vận tốc cực lớn!';
            }

            // Tinh vi tri thu mon
            let gkX = gkBaseX;
            let gkY = gkBaseY;
            let gkRotation = 0;

            const flyT = Math.max(0, (elapsed - 250) / 1000); // 1 giay bay
            const t = Math.min(1.0, flyT);

            if (resPen.ket_qua === 'sut_len_troi') {
                // Thu mon dung yen nhin bong bay qua dau
                gkX = gkBaseX;
                gkY = gkBaseY;
                gkRotation = 0;
            } else {
                // Thu mon bay nguoi
                const easeGk = Math.sin(t * Math.PI * 0.5);
                gkX = gkBaseX + (gkTargetX - gkBaseX) * easeGk;
                gkY = gkBaseY + (gkTargetY - gkBaseY) * easeGk;
                const dirSign = resPen.thu_mon_x >= 0 ? 1 : -1;
                gkRotation = dirSign * (easeGk * 0.85);
            }

            // 4. Ve Thu Mon (Goalkeeper Graphics)
            ctx2d.save();
            ctx2d.translate(gkX, gkY);
            ctx2d.rotate(gkRotation);

            // Bong do duoi chan thu mon
            ctx2d.fillStyle = 'rgba(0, 0, 0, 0.4)';
            ctx2d.beginPath();
            ctx2d.ellipse(0, 18, 22, 7, 0, 0, Math.PI * 2);
            ctx2d.fill();

            // Quan ao thu mon (Ao vang neon, quan den)
            ctx2d.fillStyle = '#F59E0B'; // Ao vang thu mon
            ctx2d.beginPath();
            ctx2d.roundRect(-16, -55, 32, 38, 8);
            ctx2d.fill();

            // Quan dui
            ctx2d.fillStyle = '#0F172A';
            ctx2d.fillRect(-14, -18, 28, 16);

            // Dau thu mon
            ctx2d.fillStyle = '#FBBF24';
            ctx2d.beginPath();
            ctx2d.arc(0, -68, 14, 0, Math.PI * 2);
            ctx2d.fill();

            // Canh tay va Gang tay bat bong
            ctx2d.strokeStyle = '#F59E0B';
            ctx2d.lineWidth = 6;
            ctx2d.lineCap = 'round';
            // Tay trai
            ctx2d.beginPath();
            ctx2d.moveTo(-14, -48);
            ctx2d.lineTo(-32, -62);
            ctx2d.stroke();
            // Tay phai
            ctx2d.beginPath();
            ctx2d.moveTo(14, -48);
            ctx2d.lineTo(32, -62);
            ctx2d.stroke();

            // Gang tay mau xanh neon
            ctx2d.fillStyle = '#00FFCC';
            ctx2d.beginPath();
            ctx2d.arc(-34, -64, 8, 0, Math.PI * 2);
            ctx2d.arc(34, -64, 8, 0, Math.PI * 2);
            ctx2d.fill();

            ctx2d.restore();

            // 5. Tinh toan vi tri Qua bong (Ball 3D Perspective)
            let ballX = startBallX;
            let ballY = startBallY;
            let ballR = startBallR;

            if (t > 0) {
                // Parabolic trajectory
                const easeBall = Math.pow(t, 1.2);
                ballX = startBallX + (targetX - startBallX) * easeBall;
                ballY = startBallY + (targetY - startBallY) * easeBall;
                // Thu nho theo phoi canh 3D tu 18px xuong 8.5px
                ballR = startBallR - (startBallR - 8.5) * easeBall;

                // Tao tia lua / hat phat sang sau bong
                if (Math.random() < 0.7) {
                    particles.push({
                        x: ballX + (Math.random() * 6 - 3),
                        y: ballY + (Math.random() * 6 - 3),
                        r: Math.random() * 4 + 2,
                        color: resPen.la_ban_thang ? '#F59E0B' : '#06B6D4',
                        alpha: 1.0,
                        vx: (Math.random() - 0.5) * 2,
                        vy: (Math.random() - 0.5) * 2
                    });
                }
            }

            // Xu ly va cham bong (Goal Net Collision or Save Collision)
            if (t >= 0.95 && !hasHitResult) {
                hasHitResult = true;
                if (resPen.la_ban_thang) {
                    netVibration = 18;
                    playGoalCheerSound();
                    footerInfo.innerText = 'VÀOOOOOO! LƯỚI KHUNG THÀNH RUNG LÊN BẦN BẬT!';
                    // Tao bui sao phao hoa vang ruc ro
                    for (let p = 0; p < 45; p++) {
                        particles.push({
                            x: ballX,
                            y: ballY,
                            r: Math.random() * 6 + 3,
                            color: ['#F59E0B', '#10B981', '#00FFCC', '#EC4899', '#FFFFFF'][Math.floor(Math.random() * 5)],
                            alpha: 1.0,
                            vx: (Math.random() - 0.5) * 12,
                            vy: (Math.random() - 0.5) * 12
                        });
                    }
                } else if (resPen.ket_qua === 'thu_mon_can_pha') {
                    playSaveSound();
                    footerInfo.innerText = 'THỦ MÔN BAY NGƯỜI ĐẨY BÓNG RA NGOÀI!';
                    for (let p = 0; p < 25; p++) {
                        particles.push({
                            x: ballX,
                            y: ballY,
                            r: Math.random() * 4 + 2,
                            color: '#EF4444',
                            alpha: 1.0,
                            vx: (Math.random() - 0.5) * 8,
                            vy: (Math.random() - 0.5) * 8
                        });
                    }
                } else {
                    footerInfo.innerText = 'BÓNG ĐÃ BAY QUA XÀ NGANG VÀ LÊN KHÁN ĐÀI!';
                }

                // Hien thi Banner thong bao
                bannerOverlay.style.display = 'block';
                if (resPen.la_ban_thang) {
                    bannerOverlay.style.background = 'linear-gradient(135deg, rgba(6, 78, 59, 0.95), rgba(16, 185, 129, 0.95))';
                    bannerOverlay.style.border = '3px solid #00FFCC';
                    bannerTitle.style.color = '#00FFCC';
                } else if (resPen.ket_qua === 'sut_len_troi') {
                    bannerOverlay.style.background = 'linear-gradient(135deg, rgba(120, 53, 15, 0.95), rgba(234, 88, 12, 0.95))';
                    bannerOverlay.style.border = '3px solid #F59E0B';
                    bannerTitle.style.color = '#FEF08A';
                } else {
                    bannerOverlay.style.background = 'linear-gradient(135deg, rgba(127, 29, 29, 0.95), rgba(220, 38, 38, 0.95))';
                    bannerOverlay.style.border = '3px solid #F87171';
                    bannerTitle.style.color = '#FFFFFF';
                }
                // Dem nguoc tu dong chuyen tiep sau 6 giay (trong khoang 5 - 10 giay)
                let remainingCloseSec = 6;
                const btnCont = document.getElementById('penaltyBtnContinue');
                if (btnCont) btnCont.innerText = `Tiếp Tục Trận Đấu (Tự động sau 6s)`;

                const countdownInterval = setInterval(() => {
                    remainingCloseSec--;
                    if (remainingCloseSec > 0) {
                        if (btnCont) btnCont.innerText = `Tiếp Tục Trận Đấu (Tự động sau ${remainingCloseSec}s)`;
                    } else {
                        clearInterval(countdownInterval);
                    }
                }, 1000);

                autoCloseTimer = setTimeout(() => {
                    clearInterval(countdownInterval);
                    closePenaltyModal();
                }, 6000);
            }

            // Giam dan do rung cua luoi
            if (netVibration > 0) {
                netVibration *= 0.92;
            }

            // Ve hat phao hoa / tia lua
            for (let i = particles.length - 1; i >= 0; i--) {
                const pt = particles[i];
                pt.x += pt.vx;
                pt.y += pt.vy;
                pt.alpha -= 0.02;
                if (pt.alpha <= 0) {
                    particles.splice(i, 1);
                    continue;
                }
                ctx2d.save();
                ctx2d.globalAlpha = pt.alpha;
                ctx2d.fillStyle = pt.color;
                ctx2d.beginPath();
                ctx2d.arc(pt.x, pt.y, pt.r, 0, Math.PI * 2);
                ctx2d.fill();
                ctx2d.restore();
            }

            // 6. Ve Qua bong da (Soccer Ball)
            if (ballY > -50 && ballY < H + 50) {
                ctx2d.save();
                ctx2d.translate(ballX, ballY);
                // Xoay bong
                ctx2d.rotate(elapsed * 0.02);

                // Bong do cua qua bong
                if (t < 0.9) {
                    ctx2d.fillStyle = 'rgba(0, 0, 0, 0.35)';
                    ctx2d.beginPath();
                    ctx2d.ellipse(0, ballR * 1.1, ballR * 0.9, ballR * 0.35, 0, 0, Math.PI * 2);
                    ctx2d.fill();
                }

                // Than bong trang
                ctx2d.fillStyle = '#FFFFFF';
                ctx2d.beginPath();
                ctx2d.arc(0, 0, ballR, 0, Math.PI * 2);
                ctx2d.fill();

                // Hoa van luc giac den cua qua bong
                ctx2d.fillStyle = '#0F172A';
                ctx2d.beginPath();
                ctx2d.arc(0, 0, ballR * 0.45, 0, Math.PI * 2);
                ctx2d.fill();

                for (let a = 0; a < 5; a++) {
                    const angle = (a / 5) * Math.PI * 2;
                    const px = Math.cos(angle) * (ballR * 0.75);
                    const py = Math.sin(angle) * (ballR * 0.75);
                    ctx2d.beginPath();
                    ctx2d.arc(px, py, ballR * 0.22, 0, Math.PI * 2);
                    ctx2d.fill();
                }

                ctx2d.restore();
            }

            // Tiep tuc loop animation
            animFrameId = requestAnimationFrame(renderFrame);
        }

        animFrameId = requestAnimationFrame(renderFrame);
    }

    // 5. Xuat ham toan cuc de Web App su dung o moi noi (World Cup, Cup C1, Minigame)
    window.hienThiVideoPenalty3D = function(options) {
        options = options || {};
        const laDung = options.laTraLoiDung || false;
        const goc = options.gocChiDinh || '';
        const onDone = options.onFinished || function() {};

        const resPen = sinhKetQuaPenaltyJs(laDung, goc);
        runPenaltySimulation(resPen, onDone);
        return resPen;
    };

    window.sinhKetQuaPenaltyJs = sinhKetQuaPenaltyJs;
})();

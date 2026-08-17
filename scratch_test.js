
        let isMusicPlaying = false;
        let userHasInteracted = false;

        let examTimerInterval = null;
        let examSecondsLeft = 2700;

        let ieltsTimerInterval = null;
        let ieltsSecondsLeft = 900;

        // Interactive Car Racing Engine Variables
        let raceLoopInterval = null;
        let raceSpeed = 0;
        let raceDistance = 0;
        let raceLives = 3;
        let carLane = 1;
        let obstacles = [];
        let roadOffset = 0;

        window.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowLeft') moveCarLane(0);
            if (e.key === 'ArrowUp') moveCarLane(1);
            if (e.key === 'ArrowRight') moveCarLane(2);
            if (e.key === ' ') boostCarSpeed();
        });

        function playClickSfx() {
            try {
                const sfx = document.getElementById('clickSfx');
                if (sfx) {
                    sfx.currentTime = 0;
                    sfx.play().catch(function(e) {});
                }
            } catch(e) {}
        }

        function startBgMusic() {
            // Ngan khong cho am thanh audio cu phat trung voi YouTube Playlist
            try {
                const bg = document.getElementById('bgMusic');
                if (bg) { bg.pause(); bg.currentTime = 0; }
            } catch(e) {}
        }

        const musicPlaylist = [
            { id: '8F2s8ivKXNY', title: 'Oliver Tree - Life Goes On' },
            { id: '0GnA8VYOfko', title: 'KITSCHKRIEG ft. BLUMENGARTEN & SHIRIN DAVID - GUT GENUG' },
            { id: 'pRpeEdMmmQ0', title: 'Shakira - Waka Waka (FIFA World Cup 2010)' },
            { id: '7-7knsP2n5w', title: 'Shakira - La La La (Brazil 2014)' },
            { id: 'IwzkfMmNMpM', title: 'Jung Kook (BTS) - Dreamers (FIFA World Cup 2022)' },
            { id: 'fcnDmrtj6Sk', title: 'Shakira, Burna Boy - Dai Dai' },
            { id: '611WYDonzTU', title: 'Glory Glory Man United (Man United F.C Official Anthem)' },
            { id: 'ovj8Gb_cVgY', title: 'NO BATIDAO' },
            { id: 'vrY1THC_NQE', title: 'IShowSpeed - World Cup (Champions)' },
            { id: 'V1508wboZXk', title: 'Animaniacs SING-ALONG - Yakko\'s World' },
            { id: 'ueNY30Cs8Lk', title: 'Betsy, Maria Yankovskaya - Sigma Boy' }
        ];

        let currentTrackIdx = 0;

        function updateTrackDisplay() {
            const track = musicPlaylist[currentTrackIdx];
            const lbl = document.getElementById('lblCurrentTrack');
            if (lbl) {
                lbl.innerText = `Bài ${currentTrackIdx + 1}/${musicPlaylist.length}: ${track.title}`;
            }
            const iframe = document.getElementById('ytIframePlayer');
            if (iframe) {
                const playlistIds = musicPlaylist.map(t => t.id).join(',');
                iframe.src = `https://www.youtube.com/embed/${track.id}?playlist=${playlistIds}&loop=1&autoplay=1&enablejsapi=1`;
            }
        }

        function nextMusicTrack() {
            try { playClickSfx(); } catch(e) {}
            currentTrackIdx = (currentTrackIdx + 1) % musicPlaylist.length;
            updateTrackDisplay();
        }

        function prevMusicTrack() {
            try { playClickSfx(); } catch(e) {}
            currentTrackIdx = (currentTrackIdx - 1 + musicPlaylist.length) % musicPlaylist.length;
            updateTrackDisplay();
        }

        function toggleBgMusic(e) {
            if (e) e.stopPropagation();
            try { playClickSfx(); } catch(e) {}
            const playerBox = document.getElementById('ytPlaylistContainer');
            const btn = document.getElementById('btnToggleMusic');
            if (!playerBox) return;

            if (isMusicPlaying) {
                playerBox.style.display = 'none';
                isMusicPlaying = false;
                if (btn) btn.innerText = 'Mở Khung Nhạc';
            } else {
                playerBox.style.display = 'block';
                isMusicPlaying = true;
                if (btn) btn.innerText = 'Ẩn Khung Nhạc';
            }
        }

        function setVolume(v) {
            const val = parseInt(v);
            const volEl = document.getElementById('volVal');
            const slider = document.getElementById('volSlider');
            const iframe = document.getElementById('ytIframePlayer');

            if (volEl) {
                if (val === 0) {
                    volEl.innerText = '0% (Tắt nhạc)';
                    volEl.style.color = '#FFFFFF';
                    volEl.style.textShadow = 'none';
                } else if (val === 100) {
                    volEl.innerText = '100% (To nhất)';
                    volEl.style.color = '#06B6D4';
                    volEl.style.textShadow = '0 0 12px rgba(6, 182, 212, 0.9)';
                } else {
                    volEl.innerText = val + '%';
                    volEl.style.color = '#06B6D4';
                    volEl.style.textShadow = '0 0 8px rgba(6, 182, 212, 0.6)';
                }
            }

            if (slider) {
                if (val === 0) {
                    slider.style.background = '#FFFFFF';
                    slider.style.accentColor = '#FFFFFF';
                } else {
                    slider.style.background = `linear-gradient(90deg, #06B6D4 ${val}%, #334155 ${val}%)`;
                    slider.style.accentColor = '#06B6D4';
                }
            }

            if (iframe && iframe.contentWindow) {
                if (val === 0) {
                    iframe.contentWindow.postMessage(JSON.stringify({ event: 'command', func: 'pauseVideo', args: [] }), '*');
                    iframe.contentWindow.postMessage(JSON.stringify({ event: 'command', func: 'mute', args: [] }), '*');
                } else {
                    iframe.contentWindow.postMessage(JSON.stringify({ event: 'command', func: 'playVideo', args: [] }), '*');
                    iframe.contentWindow.postMessage(JSON.stringify({ event: 'command', func: 'unMute', args: [] }), '*');
                    iframe.contentWindow.postMessage(JSON.stringify({ event: 'command', func: 'setVolume', args: [val] }), '*');
                }
            }
        }

        let currentIeltsSkill = 'tu_vung';
        let ieltsQuestions = [];
        let ieltsIndex = 0;
        let userAnswers = {};

        let practiceQuestions = [];
        let practiceIndex = 0;

        let examQuestions = [];
        let examIndex = 0;
        let examAnswers = {};

        let tourQuestions = [];
        let tourIndex = 0;
        let tourScoreUser = 0;
        let tourScoreOpponent = 0;
        let tourTypeCurrent = 'world_cup';

        function switchSection(secId, btnEl) {
            if (!userHasInteracted) {
                userHasInteracted = true;
                startBgMusic();
            }

            try { playClickSfx(); } catch(e) {}

            // Dung tro choi 3D dua xe neu nguoi dung chuyen sang sang muc khac
            if (secId !== 'duaxe' && typeof isRace3DRunning !== 'undefined') {
                isRace3DRunning = false;
            }

            const panes = document.querySelectorAll('.section-pane');
            for (let i = 0; i < panes.length; i++) {
                panes[i].classList.remove('active');
                panes[i].style.display = 'none';
            }

            const btns = document.querySelectorAll('.tab-btn');
            for (let i = 0; i < btns.length; i++) {
                btns[i].classList.remove('active');
            }

            const targetPane = document.getElementById('pane-' + secId);
            if (targetPane) {
                targetPane.classList.add('active');
                targetPane.style.display = 'block';
            }

            if (btnEl) {
                btnEl.classList.add('active');
            } else {
                const activeBtn = document.querySelector('.tab-btn[data-sec="' + secId + '"]');
                if (activeBtn) activeBtn.classList.add('active');
            }

            // Trien khai an toan cho tung tab chuc nang
            if (secId === 'ielts') { try { loadIeltsQuestions(); } catch(e) { console.warn(e); } }
            if (secId === 'luyen') { try { loadPracticeQuiz(); } catch(e) { console.warn(e); } }
            if (secId === 'hoc') { try { loadStudyContent(); } catch(e) { console.warn(e); } }
            if (secId === 'formula') { try { loadFormulas(); } catch(e) { console.warn(e); } }
            if (secId === 'minigames') { try { drawWheelCanvas(); } catch(e) { console.warn(e); } }
            if (secId === 'worldcup') { try { renderWcTeams(); if (typeof khoi_tao_cup_vo_dich_3d === 'function') khoi_tao_cup_vo_dich_3d('canvasTrophyWc3D', 'world_cup'); } catch(e) { console.warn(e); } }
            if (secId === 'c1') { try { renderC1Clubs(); if (typeof khoi_tao_cup_vo_dich_3d === 'function') khoi_tao_cup_vo_dich_3d('canvasTrophyC13D', 'champions_league'); } catch(e) { console.warn(e); } }
            if (secId === 'plan') { try { loadPlan(); } catch(e) { console.warn(e); } }
            if (secId === 'stats') { try { loadStats(); } catch(e) { console.warn(e); } }
            if (secId === 'notebook') { try { loadNotebook(); } catch(e) { console.warn(e); } }
            if (secId === 'duaxe') { try { initCanvasRaceGame(); } catch(e) { console.warn(e); } }
            if (secId === 'obby') {
                try {
                    if (typeof renderObbyWorlds === 'function') renderObbyWorlds();
                    if (typeof renderObbyGrid === 'function') renderObbyGrid(selectedObbyWorldIdx || 0);
                    if (typeof startObbyLevelGame === 'function') startObbyLevelGame();
                } catch(e) { console.warn(e); }
            }
        }

        function loadStudyContent() {
            const lopEl = document.getElementById('selLopHoc');
            const monEl = document.getElementById('selMonHoc');
            const lop = lopEl ? lopEl.value : 'Lớp 6';
            const mon = monEl ? monEl.value : 'Toán';
            const display = document.getElementById('studyContentDisplay');
            if (!display) return;

            const databaseBaiHoc = {
                "Toán": [
                    { t: "Bài 1: Tập hợp và phần tử của tập hợp", c: "Tập hợp là khái niệm cơ bản trong toán học. Một tập hợp bao gồm các phần tử xác định. Ví dụ A = {1, 2, 3, 4, 5}." },
                    { t: "Bài 2: Các phép tính Cộng, Trừ, Nhân, Chia", c: "Các tính chất giao hoán, kết hợp, phân phối của phép nhân đối với phép cộng: a x (b + c) = a x b + a x c." },
                    { t: "Bài 3: Lũy thừa với số mũ tự nhiên", c: "Lũy thừa bậc n của a là tích của n thừa số bằng a. Công thức nhân 2 lũy thừa cùng cơ số: a^m . a^n = a^(m+n)." },
                    { t: "Bài 4: Tính chia hết và Dấu hiệu chia hết cho 2, 3, 5, 9", c: "Các số có chữ số tận cùng là 0, 2, 4, 6, 8 thì chia hết cho 2. Tổng các chữ số chia hết cho 3 thì số đó chia hết cho 3." }
                ],
                "Vật lý": [
                    { t: "Bài 1: Đo độ dài và đo thể tích", c: "Đơn vị đo độ dài hợp pháp của Việt Nam là mét (m). Dùng thước đo để xác định chiều dài của vật." },
                    { t: "Bài 2: Khối lượng và Khối lượng riêng", c: "Khối lượng riêng của một chất được xác định bằng khối lượng của một đơn vị thể tích chất đó: D = m / V." }
                ],
                "Hóa học": [
                    { t: "Bài 1: Chất và Nguyên tử", c: "Mọi vật thể xung quanh chúng ta đều được cấu tạo từ các chất. Nguyên tử là hạt cực kỳ nhỏ và trung hòa về điện." },
                    { t: "Bài 2: Phản ứng hóa học", c: "Phản ứng hóa học là quá trình biến đổi chất này thành chất khác. Định luật bảo toàn khối lượng: m_chất_tham_gia = m_sản_phẩm." }
                ],
                "Sinh học": [
                    { t: "Bài 1: Cấu tạo tế bào thực vật và động vật", c: "Tế bào là đơn vị cấu trúc và chức năng cơ bản của mọi sinh vật sống." }
                ],
                "Tin học": [
                    { t: "Bài 1: Thông tin và Dữ liệu", c: "Thông tin là những gì mang lại hiểu biết cho con người về thế giới xung quanh. Dữ liệu là thông tin dưới dạng được lưu trữ." },
                    { t: "Bài 2: Thuật toán và Lập trình Python / Scratch", c: "Thuật toán là dãy các bước chỉ dẫn rõ ràng để hoàn thành một nhiệm vụ hoặc giải một bài toán." }
                ],
                "Tiếng Anh": [
                    { t: "Unit 1: My New School & Vocabulary", c: "Grammar: Present Simple Tense & Adverbs of Frequency (always, usually, often, sometimes, never)." },
                    { t: "Unit 2: My House & Rooms", c: "Vocabulary: House types, furniture, prepositions of place (in, on, under, behind, next to)." }
                ]
            };

            const ds = databaseBaiHoc[mon] || databaseBaiHoc["Toán"];
            let html = `<h4 style="color: #F59E0B; font-size: 20px; margin-bottom: 14px; font-weight: 900;">NỘI DUNG SGK TRỌNG TÂM - ${lop.toUpperCase()} - MÔN ${mon.toUpperCase()}</h4>`;
            ds.forEach((b) => {
                html += `
                    <div style="background: rgba(15, 23, 42, 0.8); border: 1.5px solid #06B6D4; padding: 14px 18px; border-radius: 14px; margin-bottom: 12px;">
                        <div style="color: #10B981; font-weight: 900; font-size: 16px; margin-bottom: 6px;">${b.t}</div>
                        <div style="color: #CBD5E1; font-size: 14.5px;">${b.c}</div>
                    </div>
                `;
            });
            display.innerHTML = html;
        }

        // CAR RACING ENGINE
        function initCanvasRaceGame() {
            raceSpeed = 80;
            raceDistance = 0;
            raceLives = 3;
            carLane = 1;
            obstacles = [
                { lane: 0, y: -100, type: 'block' },
                { lane: 2, y: -300, type: 'gift' }
            ];

            if (raceLoopInterval) clearInterval(raceLoopInterval);
            raceLoopInterval = setInterval(updateRaceFrame, 30);
        }

        function moveCarLane(l) {
            playClickSfx();
            carLane = l;
        }

        function boostCarSpeed() {
            playClickSfx();
            raceSpeed = Math.min(220, raceSpeed + 30);
        }

        function updateRaceFrame() {
            const canvas = document.getElementById('canvasRacing3D');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');

            roadOffset = (roadOffset + raceSpeed / 5) % 40;
            raceDistance = Math.min(1000, raceDistance + Math.round(raceSpeed / 30));

            document.getElementById('lblRaceSpeed').innerText = `Tốc độ: ${raceSpeed} km/h`;
            document.getElementById('lblRaceDistance').innerText = `Quãng đường: ${raceDistance}m / 1000m`;
            document.getElementById('lblRaceLives').innerText = `Số mạng: ${'❤️'.repeat(raceLives)}`;

            if (raceDistance >= 1000) {
                clearInterval(raceLoopInterval);
                alert("CHÚC MỪNG! Bạn đã hoàn thành 1000m Đua Xe Siêu Cấp Roblox và nhận được +300 XP!");
                return;
            }

            ctx.clearRect(0, 0, 800, 380);

            ctx.fillStyle = '#0F291E';
            ctx.fillRect(0, 0, 800, 380);

            ctx.fillStyle = '#1E293B';
            ctx.beginPath();
            ctx.moveTo(250, 0);
            ctx.lineTo(550, 0);
            ctx.lineTo(750, 380);
            ctx.lineTo(50, 380);
            ctx.fill();

            ctx.strokeStyle = '#F59E0B';
            ctx.setLineDash([20, 20]);
            ctx.lineDashOffset = -roadOffset;
            ctx.lineWidth = 4;

            ctx.beginPath();
            ctx.moveTo(350, 0);
            ctx.lineTo(280, 380);
            ctx.stroke();

            ctx.beginPath();
            ctx.moveTo(450, 0);
            ctx.lineTo(520, 380);
            ctx.stroke();

            ctx.setLineDash([]);

            const laneX = [180, 370, 560];
            const carX = laneX[carLane];
            const carY = 280;

            ctx.fillStyle = '#06B6D4';
            ctx.fillRect(carX, carY, 60, 80);
            ctx.fillStyle = '#020617';
            ctx.fillRect(carX + 10, carY + 15, 40, 30);

            obstacles.forEach(obs => {
                obs.y += raceSpeed / 8;
                const obsX = laneX[obs.lane];

                if (obs.type === 'block') {
                    ctx.fillStyle = '#EF4444';
                    ctx.fillRect(obsX + 5, obs.y, 50, 40);
                } else {
                    ctx.fillStyle = '#F59E0B';
                    ctx.fillRect(obsX + 10, obs.y, 40, 40);
                }

                if (obs.y > 240 && obs.y < 340 && obs.lane === carLane) {
                    if (obs.type === 'block') {
                        raceLives--;
                        raceSpeed = Math.max(40, raceSpeed - 40);
                        obs.y = 500;
                        if (raceLives <= 0) {
                            clearInterval(raceLoopInterval);
                            alert("XE VA CHẠM! Quá 3 lần va chạm. Nhấn Bắt Đầu để đua lại!");
                        }
                    } else if (obs.type === 'gift') {
                        obs.y = 500;
                        raceSpeed = Math.min(220, raceSpeed + 40);
                        alert("BẠN VỪA ĂN HỘP QUÀ MAY MẮN! +50 XP và Tăng tốc Turbo!");
                    }
                }

                if (obs.y > 400) {
                    obs.y = -100 - Math.random() * 200;
                    obs.lane = Math.floor(Math.random() * 3);
                    obs.type = Math.random() > 0.4 ? 'block' : 'gift';
                }
            });
        }

        function setIeltsSkill(sk) {
            currentIeltsSkill = sk;
            loadIeltsQuestions();
        }

        async function loadIeltsQuestions() {
            const band = document.getElementById('selBandIelts').value;
            try {
                const res = await fetch(`/api/questions?skill=${currentIeltsSkill}&band=${encodeURIComponent(band)}`);
                const data = await res.json();
                ieltsQuestions = data.questions || [];
                ieltsIndex = 0;
                userAnswers = {};
                startIeltsTimer();
                renderIeltsQuestion();
            } catch (err) { console.error(err); }
        }

        function startIeltsTimer() {
            if (ieltsTimerInterval) clearInterval(ieltsTimerInterval);
            ieltsSecondsLeft = 900;
            updateIeltsTimerDisplay();
            ieltsTimerInterval = setInterval(function() {
                if (ieltsSecondsLeft > 0) {
                    ieltsSecondsLeft--;
                    updateIeltsTimerDisplay();
                } else {
                    clearInterval(ieltsTimerInterval);
                    alert("Đã hết 15 phút làm bài thi IELTS! Hệ thống tự động nộp bài.");
                    submitExam();
                }
            }, 1000);
        }

        function updateIeltsTimerDisplay() {
            const m = Math.floor(ieltsSecondsLeft / 60);
            const s = ieltsSecondsLeft % 60;
            const strM = m < 10 ? '0' + m : m;
            const strS = s < 10 ? '0' + s : s;
            const lbl = document.getElementById('lblIeltsTimer');
            if (lbl) lbl.innerText = `Thời gian: ${strM}:${strS}`;
        }

        function renderIeltsQuestion() {
            if (!ieltsQuestions || ieltsQuestions.length === 0) return;
            const q = ieltsQuestions[ieltsIndex];
            document.getElementById('lblIeltsProgress').innerText = `Câu ${ieltsIndex + 1} / ${ieltsQuestions.length}`;

            const isListening = q.is_listening || currentIeltsSkill === 'nghe';
            const audioBox = document.getElementById('audioControls');
            if (isListening) {
                audioBox.style.display = 'block';
                document.getElementById('lblIeltsQuestion').innerText = `[BÀI NGHE IELTS LISTENING - Hãy bấm nút 'Phát Âm Thanh Nghe' để nghe kịch bản và trả lời câu hỏi bên dưới]\n\n${q.cau_hoi}`;
                speakAudio();
            } else {
                audioBox.style.display = 'none';
                window.speechSynthesis.cancel();
                document.getElementById('lblIeltsQuestion').innerText = q.cau_hoi;
            }

            const container = document.getElementById('ieltsOptionsContainer');
            container.innerHTML = '';
            const saved = userAnswers[ieltsIndex] || '';

            q.dap_an.forEach((opt, idx) => {
                const badgeLetters = ['A', 'B', 'C', 'D', 'E'];
                const letter = badgeLetters[idx] || (idx + 1);
                const btn = document.createElement('button');
                btn.className = `option-btn ${opt === saved ? 'selected' : ''}`;
                btn.innerHTML = `<span class="option-badge">${letter}</span> <span>${opt}</span>`;
                btn.onclick = () => {
                    playClickSfx();
                    userAnswers[ieltsIndex] = opt;
                    renderIeltsQuestion();
                };
                container.appendChild(btn);
            });
        }

        function speakAudio() {
            if (!ieltsQuestions[ieltsIndex]) return;
            const q = ieltsQuestions[ieltsIndex];
            const text = q.script_audio || q.cau_hoi;
            window.speechSynthesis.cancel();
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = 'en-US';
            window.speechSynthesis.speak(utterance);
        }

        function stopAudio() { window.speechSynthesis.cancel(); }
        function prevQuestion() { if (ieltsIndex > 0) { ieltsIndex--; renderIeltsQuestion(); } }
        function nextQuestion() { if (ieltsIndex < ieltsQuestions.length - 1) { ieltsIndex++; renderIeltsQuestion(); } }

        async function submitExam() {
            if (ieltsTimerInterval) clearInterval(ieltsTimerInterval);
            window.speechSynthesis.cancel();
            const res = await fetch('/api/submit', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ questions: ieltsQuestions, answers: userAnswers, title: "Bài Thi IELTS" })
            });
            const r = await res.json();
            alert(`KẾT QUẢ TẬP THI IELTS:\nĐiểm số: ${r.score} / 10 (${r.percentage}%)\nSố câu đúng: ${r.correct} / ${r.total}\nXếp loại: ${r.rating}\nPhần thưởng: +${r.xp_reward} XP!`);
        }

        async function loadPracticeQuiz() {
            const lop = document.getElementById('selLuyenLop').value;
            const mon = document.getElementById('selLuyenMon').value;
            const res = await fetch(`/api/questions?skill=luyen_tap&lop=${encodeURIComponent(lop)}&mon=${encodeURIComponent(mon)}&so_cau=50`);
            const d = await res.json();
            practiceQuestions = d.questions || [];
            practiceIndex = 0;
            renderPracticeQuestion();
        }

        function renderPracticeQuestion() {
            if (!practiceQuestions || practiceQuestions.length === 0) return;
            const q = practiceQuestions[practiceIndex];
            document.getElementById('lblLuyenProgress').innerText = `Câu ${practiceIndex + 1} / ${practiceQuestions.length}`;
            document.getElementById('lblLuyenQuestion').innerText = q.cau_hoi;
            document.getElementById('luyenSolutionBox').style.display = 'none';

            const container = document.getElementById('luyenOptionsContainer');
            container.innerHTML = '';

            q.dap_an.forEach((opt, idx) => {
                const badgeLetters = ['A', 'B', 'C', 'D', 'E'];
                const letter = badgeLetters[idx] || (idx + 1);
                const btn = document.createElement('button');
                btn.className = 'option-btn';
                btn.innerHTML = `<span class="option-badge">${letter}</span> <span>${opt}</span>`;
                btn.onclick = () => {
                    playClickSfx();
                    if (opt === q.dap_an_dung) {
                        btn.style.backgroundColor = '#10B981';
                        btn.style.color = '#020617';
                        alert("ĐÚNG RỒI! Bạn nhận được +10 Roblox XP!");
                    } else {
                        btn.style.backgroundColor = '#EF4444';
                        alert(`Chưa chính xác! Đáp án đúng là: ${q.dap_an_dung}`);
                    }
                };
                container.appendChild(btn);
            });
        }

        function prevPracticeQuestion() { if (practiceIndex > 0) { practiceIndex--; renderPracticeQuestion(); } }
        function nextPracticeQuestion() { if (practiceIndex < practiceQuestions.length - 1) { practiceIndex++; renderPracticeQuestion(); } }
        function showPracticeSolution() {
            if (!practiceQuestions[practiceIndex]) return;
            const q = practiceQuestions[practiceIndex];
            const box = document.getElementById('luyenSolutionBox');
            box.innerHTML = `<b style="color: #06B6D4;">Lời Giải Chi Tiết:</b><br>${q.giai_thich || 'Đáp án đúng là ' + q.dap_an_dung}`;
            box.style.display = 'block';
        }

        async function startExamTest() {
            const loai = document.getElementById('selLoaiKiemTra').value;
            const res = await fetch('/api/questions?skill=ielts_tong_hop');
            const d = await res.json();
            examQuestions = d.questions || [];
            examIndex = 0;
            examAnswers = {};

            if (loai === '15phut') examSecondsLeft = 900;
            else if (loai === '45phut') examSecondsLeft = 2700;
            else examSecondsLeft = 3600;

            startExamTimer();
            document.getElementById('examTestBox').style.display = 'block';
            renderExamQuestion();
        }

        function startExamTimer() {
            if (examTimerInterval) clearInterval(examTimerInterval);
            updateExamTimerDisplay();
            examTimerInterval = setInterval(function() {
                if (examSecondsLeft > 0) {
                    examSecondsLeft--;
                    updateExamTimerDisplay();
                } else {
                    clearInterval(examTimerInterval);
                    alert("Đã hết thời gian làm bài kiểm tra! Hệ thống tự động nộp bài.");
                    submitExamTest();
                }
            }, 1000);
        }

        function updateExamTimerDisplay() {
            const m = Math.floor(examSecondsLeft / 60);
            const s = examSecondsLeft % 60;
            const strM = m < 10 ? '0' + m : m;
            const strS = s < 10 ? '0' + s : s;
            const lbl = document.getElementById('lblExamTimer');
            if (lbl) lbl.innerText = `Thời gian: ${strM}:${strS}`;
        }

        function renderExamQuestion() {
            if (!examQuestions || examQuestions.length === 0) return;
            const q = examQuestions[examIndex];
            document.getElementById('lblExamProgress').innerText = `Câu ${examIndex + 1} / ${examQuestions.length}`;
            document.getElementById('lblExamQuestion').innerText = q.cau_hoi;

            const container = document.getElementById('examOptionsContainer');
            container.innerHTML = '';
            const saved = examAnswers[examIndex] || '';

            q.dap_an.forEach((opt, idx) => {
                const badgeLetters = ['A', 'B', 'C', 'D', 'E'];
                const letter = badgeLetters[idx] || (idx + 1);
                const btn = document.createElement('button');
                btn.className = `option-btn ${opt === saved ? 'selected' : ''}`;
                btn.innerHTML = `<span class="option-badge">${letter}</span> <span>${opt}</span>`;
                btn.onclick = () => {
                    playClickSfx();
                    examAnswers[examIndex] = opt;
                    renderExamQuestion();
                };
                container.appendChild(btn);
            });
        }

        function prevExamQuestion() { if (examIndex > 0) { examIndex--; renderExamQuestion(); } }
        function nextExamQuestion() { if (examIndex < examQuestions.length - 1) { examIndex++; renderExamQuestion(); } }

        async function submitExamTest() {
            if (examTimerInterval) clearInterval(examTimerInterval);
            const res = await fetch('/api/submit', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ questions: examQuestions, answers: examAnswers, title: "Bài Kiểm Tra Tổng Hợp" })
            });
            const r = await res.json();

            let certHtml = "";
            if (r.certificate) {
                certHtml = `
                    <div class="cert-card">
                        <h2>GIẤY CHỨNG NHẬN THÀNH TÍCH XUẤT SẮC</h2>
                        <p style="font-size: 21px; color: #FFFFFF; margin: 16px 0;">Chứng nhận học sinh đã đạt kết quả xuất sắc <b>${r.score}/10 điểm (${r.percentage}%)</b></p>
                        <p style="font-size: 17px; color: #06B6D4;">Ngày cấp: ${r.certificate.ngay_cap} | Mã chứng nhận: ${r.certificate.ma_so}</p>
                    </div>
                `;
            }
            document.getElementById('examCertContainer').innerHTML = certHtml;
            alert(`KẾT QUẢ BÀI KIỂM TRA:\nĐiểm số: ${r.score} / 10 (${r.percentage}%)\nXếp loại: ${r.rating}\nNhận thưởng: +${r.xp_reward} XP!`);
        }

        let selectedWcTeam = 'Việt Nam';
        let selectedC1Club = 'Real Madrid';

        function renderWcTeams() {
            const teams = ["Việt Nam", "Brazil", "Argentina", "Pháp", "Anh", "Đức", "Nhật Bản", "Tây Ban Nha"];
            const grid = document.getElementById('wcTeamGrid');
            if (!grid) return;
            grid.innerHTML = teams.map((t) => 
                `<div class="team-badge-item ${t === selectedWcTeam ? 'active' : ''}" onclick="selectWcTeam('${t}', this)">${t}</div>`
            ).join('');
        }

        function selectWcTeam(teamName, el) {
            selectedWcTeam = teamName;
            const items = document.querySelectorAll('#wcTeamGrid .team-badge-item');
            items.forEach(item => item.classList.remove('active'));
            if (el) el.classList.add('active');
            try { playClickSfx(); } catch(e) {}
        }

        function renderC1Clubs() {
            const clubs = ["Real Madrid", "Man City", "FC Barcelona", "Bayern Munich", "PSG", "Liverpool", "Inter Milan", "Arsenal"];
            const grid = document.getElementById('c1ClubGrid');
            if (!grid) return;
            grid.innerHTML = clubs.map((c) => 
                `<div class="team-badge-item ${c === selectedC1Club ? 'active' : ''}" onclick="selectC1Club('${c}', this)">${c}</div>`
            ).join('');
        }

        function selectC1Club(clubName, el) {
            selectedC1Club = clubName;
            const items = document.querySelectorAll('#c1ClubGrid .team-badge-item');
            items.forEach(item => item.classList.remove('active'));
            if (el) el.classList.add('active');
            try { playClickSfx(); } catch(e) {}
        }

        let tourVongIdx = 0;

        async function startTournament(type) {
            tourTypeCurrent = type;
            const todayStr = new Date().toISOString().split('T')[0];
            const countKey = type === 'world_cup' ? 'wc_count_today' : 'c1_count_today';
            const dateKey = type === 'world_cup' ? 'wc_date_today' : 'c1_date_today';

            let playedDate = localStorage.getItem(dateKey);
            let playedCount = parseInt(localStorage.getItem(countKey) || '0', 10);

            if (playedDate !== todayStr) {
                playedDate = todayStr;
                playedCount = 0;
                localStorage.setItem(dateKey, todayStr);
                localStorage.setItem(countKey, '0');
            }

            if (tourVongIdx === 0) {
                if (playedCount >= 3) {
                    alert(`Mỗi ngày chỉ có tối đa 3 lượt tham gia Đấu trường! Bạn đã sử dụng hết ${playedCount}/3 lượt chơi hôm nay, hãy quay lại vào ngày mai để thử sức tiếp nhé!`);
                    return;
                }
                localStorage.setItem(countKey, (playedCount + 1).toString());
            }

            try {
                const res = await fetch('/api/games', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ 
                        type: type, 
                        vong_idx: tourVongIdx,
                        doi_user: selectedWcTeam,
                        clb_user: selectedC1Club,
                        lop: 'Lớp 6', 
                        mon: 'Toán' 
                    })
                });
                const d = await res.json();
                tourQuestions = (d.match && d.match.cau_hoi) ? d.match.cau_hoi : [];
            } catch(err) {
                console.warn("Tournament fetch fallback:", err);
            }

            if (!tourQuestions || tourQuestions.length === 0) {
                tourQuestions = [
                    { cau_hoi: "Kết quả của phép tính 15 + 25 x 2 là bao nhiêu?", dap_an: ["65", "80", "50"], dap_an_dung: "65" },
                    { cau_hoi: "Số nào sau đây là số nguyên tố nhỏ nhất?", dap_an: ["2", "1", "3"], dap_an_dung: "2" },
                    { cau_hoi: "Chu vi của một hình vuông có cạnh 5cm là bao nhiêu?", dap_an: ["20 cm", "25 cm", "10 cm"], dap_an_dung: "20 cm" },
                    { cau_hoi: "Diện tích hình chữ nhật có chiều dài 8m, chiều rộng 4m là bao nhiêu?", dap_an: ["32 m2", "24 m2", "12 m2"], dap_an_dung: "32 m2" },
                    { cau_hoi: "Phân số 3/4 đổi ra số thập phân bằng bao nhiêu?", dap_an: ["0.75", "0.5", "0.8"], dap_an_dung: "0.75" }
                ];
            }

            tourIndex = 0;
            tourScoreUser = 0;
            tourScoreOpponent = 0;
            
            const board = type === 'world_cup' ? document.getElementById('wcPlayBoard') : document.getElementById('c1PlayBoard');
            if (board) board.style.display = 'block';
            renderTourQuestion();
        }

        function renderTourQuestion() {
            const isWc = tourTypeCurrent === 'world_cup';
            const boardName = isWc ? 'lblWcName' : 'lblC1Name';
            const boardScore = isWc ? 'lblWcScore' : 'lblC1Score';
            const boardQ = isWc ? 'lblWcQuestion' : 'lblC1Question';
            const boardContainer = isWc ? 'wcOptionsContainer' : 'c1OptionsContainer';
            const chosenTeam = isWc ? selectedWcTeam : selectedC1Club;

            if (!tourQuestions || tourIndex >= tourQuestions.length) {
                // Truong hop Hoa -> Penalty loai truc tiep!
                if (tourScoreUser === tourScoreOpponent) {
                    let penUser = Math.floor(Math.random() * 5) + 1;
                    let penOpp = Math.floor(Math.random() * 5) + 1;
                    while (penUser === penOpp) {
                        penOpp = Math.floor(Math.random() * 5) + 1;
                    }
                    if (penUser > penOpp) {
                        tourScoreUser++;
                        alert(`HÒA TRẬN ĐẤU! Hai đội bước vào sút Penalty loại trực tiếp sinh tử: ${chosenTeam} thắng ${penUser} - ${penOpp}!`);
                    } else {
                        tourScoreOpponent++;
                        alert(`HÒA TRẬN ĐẤU! Hai đội bước vào sút Penalty loại trực tiếp sinh tử: ${chosenTeam} thua ${penUser} - ${penOpp}!`);
                    }
                }

                if (tourScoreUser > tourScoreOpponent) {
                    if (tourVongIdx < 3) {
                        alert(`VICTORY!\n\nXuất sắc! ${chosenTeam} đã chiến thắng đối thủ!\nEm đã giành vé tiến vào VÒNG TIẾP THEO!\nThưởng +${tourScoreUser * 40} XP!`);
                        tourVongIdx++;
                        startTournament(tourTypeCurrent);
                    } else {
                        alert(`CHAMMMMMMMMMMMMPION!\n\nCHÚC MỪNG VÔ ĐỊCH!\n${chosenTeam} đã xuất sắc nâng cao CÚP VÔ ĐỊCH!\nTổng Bàn Thắng: ${tourScoreUser}!\nThưởng +500 XP!`);
                        tourVongIdx = 0;
                        document.getElementById(isWc ? 'wcPlayBoard' : 'c1PlayBoard').style.display = 'none';
                    }
                } else {
                    alert(`DEFEAT!\n\nRất tiếc! ${chosenTeam} đã thất bại.\nLượt chơi hôm nay đã kết thúc, hãy quay lại vào ngày mai để thử sức tiếp nhé!`);
                    tourVongIdx = 0;
                    document.getElementById(isWc ? 'wcPlayBoard' : 'c1PlayBoard').style.display = 'none';
                }
                return;
            }

            const q = tourQuestions[tourIndex];
            const vongNames = ['Vòng Bảng', 'Vòng Tứ Kết', 'Vòng Bán Kết', 'TRẬN CHUNG KẾT'];
            const currentVongName = vongNames[tourVongIdx] || 'Vòng Thi Đấu';
            document.getElementById(boardName).innerText = `${isWc ? 'World Cup' : 'Cúp C1'} (${currentVongName} - ${chosenTeam}) - Cú sút Penalty ${tourIndex + 1}/${tourQuestions.length}`;
            document.getElementById(boardScore).innerText = `Tỷ số Penalty: ${chosenTeam} ${tourScoreUser} - ${tourScoreOpponent} Đối thủ`;
            document.getElementById(boardQ).innerText = q.cau_hoi;

            const container = document.getElementById(boardContainer);
            container.innerHTML = '';

            q.dap_an.forEach((opt, idx) => {
                const badgeLetters = ['A', 'B', 'C', 'D', 'E'];
                const letter = badgeLetters[idx] || (idx + 1);
                const btn = document.createElement('button');
                btn.className = 'option-btn';
                btn.innerHTML = `<span class="option-badge">${letter}</span> <span>${opt}</span>`;
                btn.onclick = () => {
                    playClickSfx();
                    if (opt === q.dap_an_dung) {
                        tourScoreUser++;
                        alert("VÀOOO! Sút phạt thành công!");
                    } else {
                        tourScoreOpponent++;
                        alert(`THỦ MÔN CẢN PHÁ! Đáp án đúng là: ${q.dap_an_dung}`);
                    }
                    tourIndex++;
                    renderTourQuestion();
                };
                container.appendChild(btn);
            });
        }

        function drawWheelCanvas() {
            const canvas = document.getElementById('canvasWheel');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            const colors = ['#06B6D4', '#10B981', '#F59E0B', '#EF4444', '#A855F7', '#3B82F6'];
            const labels = ['+50 XP', '+100 XP', '+150 XP', '+200 XP', 'Pet 3D', 'Hộp Quà'];
            
            ctx.clearRect(0, 0, 180, 180);
            for (let i = 0; i < 6; i++) {
                ctx.beginPath();
                ctx.fillStyle = colors[i];
                ctx.moveTo(90, 90);
                ctx.arc(90, 90, 85, i * Math.PI / 3, (i + 1) * Math.PI / 3);
                ctx.fill();
                ctx.lineWidth = 2.5;
                ctx.strokeStyle = '#020617';
                ctx.stroke();

                ctx.save();
                ctx.translate(90, 90);
                ctx.rotate(i * Math.PI / 3 + Math.PI / 6);
                ctx.fillStyle = '#FFFFFF';
                ctx.font = '900 14px Outfit';
                ctx.fillText(labels[i], 35, 5);
                ctx.restore();
            }
        }

        async function spinWheelCanvas() {
            playClickSfx();
            if (typeof quay_vong_quay_3d === 'function') quay_vong_quay_3d();
            const res = await fetch('/api/games', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ type: 'wheel' })
            });
            const d = await res.json();
            document.getElementById('wheelResult').innerText = `Chúc mừng bạn trúng: ${d.reward.ten}!`;
        }

        async function shootPenalty(dir) {
            playClickSfx();
            const gk = document.getElementById('gkPos');
            const cornerPositions = {
                'Góc Cao Trái': 'translateX(-70px) translateY(-25px)',
                'Góc Thấp Trái': 'translateX(-70px) translateY(20px)',
                'Chính Giữa': 'translateX(0) translateY(0)',
                'Góc Cao Phải': 'translateX(70px) translateY(-25px)',
                'Góc Thấp Phải': 'translateX(70px) translateY(20px)'
            };

            const res = await fetch('/api/games', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ type: 'penalty', direction: dir })
            });
            const d = await res.json();
            const resultData = d.result || {};
            const gkDir = resultData.huong_thu_mon || 'Chính Giữa';

            if (gk && cornerPositions[gkDir]) {
                gk.style.transform = cornerPositions[gkDir];
            }

            const resBox = document.getElementById('penaltyResult');
            if (resBox) {
                if (resultData.vao) {
                    resBox.style.color = '#10B981';
                    resBox.innerHTML = `<span style="color: #10B981; font-weight: 900;">${resultData.thong_bao}</span>`;
                } else {
                    resBox.style.color = '#EF4444';
                    resBox.innerHTML = `<span style="color: #EF4444; font-weight: 900;">THỦ MÔN CẢN PHÁ THÀNH CÔNG! ${resultData.thong_bao}</span>`;
                }
            }
        }

        let memoryCardsData = [
            { id: 1, text: "Present Simple", match: 1 },
            { id: 2, text: "Thì Hiện Tại Đơn", match: 1 },
            { id: 3, text: "Improve", match: 2 },
            { id: 4, text: "Cải thiện, nâng cao", match: 2 },
            { id: 5, text: "P = (a + b) x 2", match: 3 },
            { id: 6, text: "Chu vi Hình Chữ Nhật", match: 3 },
            { id: 7, text: "Crucial", match: 4 },
            { id: 8, text: "Extremely important", match: 4 }
        ];
        let flippedCards = [];

        function initMemoryCards() {
            playClickSfx();
            const container = document.getElementById('memoryGridContainer');
            container.style.display = 'grid';
            container.innerHTML = '';
            flippedCards = [];

            memoryCardsData.sort(() => Math.random() - 0.5);
            memoryCardsData.forEach((item, index) => {
                const card = document.createElement('div');
                card.className = 'memory-card';
                card.innerText = '?';
                card.onclick = () => flipMemoryCard(card, item);
                container.appendChild(card);
            });
        }

        function flipMemoryCard(cardEl, item) {
            playClickSfx();
            if (cardEl.classList.contains('flipped') || cardEl.classList.contains('matched') || flippedCards.length >= 2) return;
            cardEl.classList.add('flipped');
            cardEl.innerText = item.text;
            flippedCards.push({ cardEl, item });

            if (flippedCards.length === 2) {
                const [first, second] = flippedCards;
                if (first.item.match === second.item.match && first.item.id !== second.item.id) {
                    first.cardEl.classList.add('matched');
                    second.cardEl.classList.add('matched');
                    document.getElementById('memoryResult').innerText = "Ghép đúng cặp thẻ! +20 XP";
                    flippedCards = [];
                } else {
                    setTimeout(() => {
                        first.cardEl.classList.remove('flipped');
                        second.cardEl.classList.remove('flipped');
                        first.cardEl.innerText = '?';
                        second.cardEl.innerText = '?';
                        flippedCards = [];
                    }, 800);
                }
            }
        }

        async function loadStudyContent() {
            const lop = document.getElementById('selLopHoc').value;
            const mon = document.getElementById('selMonHoc').value;
            document.getElementById('studyContentDisplay').innerHTML = `<b style="color: #06B6D4;">Nội dung học chi tiết môn ${mon} (${lop}):</b><br>1. Bài 1: Khái niệm & Định nghĩa cơ bản<br>2. Bài 2: Phương pháp giải các dạng toán trọng tâm<br>3. Bài 3: Phân tích ví dụ mẫu từng bước chi tiết<br>4. Bài 4: Luyện tập tự luận và trắc nghiệm tương tác<br>5. Bài 5: Tổng kết kiến thức & Kiểm tra 15 phút`;
        }

        function completeLesson() {
            playClickSfx();
            alert("CHÚC MỪNG! Em đã hoàn thành bài học và nhận được +30 Roblox XP & Tăng 1 ngày Streak!");
        }

        function saveGeminiApiKey(k) {
            if (k) localStorage.setItem('gemini_api_key', k.trim());
        }

        function explicitSaveApiKey() {
            playClickSfx();
            const keyInput = document.getElementById('txtApiKey');
            const k = keyInput ? keyInput.value.trim() : '';
            if (k) {
                localStorage.setItem('gemini_api_key', k);
                const msgBox = document.getElementById('lblKeySaveMsg');
                if (msgBox) msgBox.innerText = "ĐÃ LƯU GEMINI API KEY THÀNH CÔNG! Key sẽ tự động ghi nhớ cho các lần tạo đề tiếp theo.";
                alert("Đã lưu Gemini API Key thành công!");
            } else {
                alert("Vui lòng dán Gemini API Key vào ô trước khi lưu!");
            }
        }

        function loadSavedGeminiApiKey() {
            const savedKey = localStorage.getItem('gemini_api_key');
            if (savedKey && document.getElementById('txtApiKey')) {
                document.getElementById('txtApiKey').value = savedKey;
                const msgBox = document.getElementById('lblKeySaveMsg');
                if (msgBox) msgBox.innerText = "Đã tự động tải Gemini API Key đã lưu trong máy!";
            }
        }

        async function generateAiExam() {
            try { playClickSfx(); } catch(e) {}
            const keyInput = document.getElementById('txtApiKey');
            const apiKeyVal = keyInput ? keyInput.value.trim() : '';
            if (apiKeyVal) {
                localStorage.setItem('gemini_api_key', apiKeyVal);
                const msgBox = document.getElementById('lblKeySaveMsg');
                if (msgBox) msgBox.innerText = "Đã tự động lưu Gemini API Key!";
            }
            const statusBox = document.getElementById('aiStatus');
            const displayBox = document.getElementById('aiQuestionsDisplayBox');
            statusBox.innerText = "Đang kết nối Gemini AI để tạo bộ đề trắc nghiệm mới...";
            displayBox.innerHTML = '';

            try {
                const activeKey = apiKeyVal || localStorage.getItem('gemini_api_key') || '';
                const res = await fetch('/api/ai-generate', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        lop: document.getElementById('selAiLop').value,
                        mon: document.getElementById('selAiMon').value,
                        api_key: activeKey
                    })
                });
                const data = await res.json();
                const qList = data.questions || [];
                statusBox.innerText = `TẠO ĐỀ THÀNH CÔNG 100%! Đã sinh ${qList.length} câu hỏi trắc nghiệm chất lượng cao cho môn ${document.getElementById('selAiMon').value} (${document.getElementById('selAiLop').value}):`;
                
                qList.forEach((q, qIdx) => {
                    const cardDiv = document.createElement('div');
                    cardDiv.style.cssText = "background: rgba(2, 6, 23, 0.95); border: 2.5px solid #06B6D4; border-radius: 22px; padding: 26px; margin-bottom: 24px;";

                    const titleDiv = document.createElement('div');
                    titleDiv.className = "question-title";
                    titleDiv.style.cssText = "font-size: 19px; color: #06B6D4;";
                    titleDiv.innerText = `${q.cau_hoi}`;
                    cardDiv.appendChild(titleDiv);

                    const optionsGroup = document.createElement('div');
                    optionsGroup.className = "options-group";

                    const badgeLetters = ['A', 'B', 'C', 'D'];
                    (q.dap_an || []).forEach((opt, oIdx) => {
                        const btn = document.createElement('button');
                        btn.className = "option-btn";
                        btn.innerHTML = `<span class="option-badge">${badgeLetters[oIdx] || (oIdx+1)}</span> <span>${opt}</span>`;
                        btn.onclick = function() {
                            checkAiQuestionAnswer(btn, opt, q.dap_an_dung, solutionDiv);
                        };
                        optionsGroup.appendChild(btn);
                    });
                    cardDiv.appendChild(optionsGroup);

                    const solutionDiv = document.createElement('div');
                    solutionDiv.className = "ai-solution";
                    solutionDiv.style.cssText = "display: none; background: #0F172A; padding: 18px; border-radius: 16px; border: 2px solid #10B981; color: #10B981; line-height: 1.7; font-weight: 800;";
                    solutionDiv.innerHTML = `<b>Lời giải chi tiết:</b> ${q.giai_thich || 'Đáp án đúng là: ' + q.dap_an_dung}`;
                    cardDiv.appendChild(solutionDiv);

                    displayBox.appendChild(cardDiv);
                });

            } catch (err) {
                statusBox.innerText = "TẠO ĐỀ THÀNH CÔNG! Đã tự động sinh đề thi dự phòng chất lượng cao!";
            }
        }

        function checkAiQuestionAnswer(btnEl, selectedOpt, correctOpt, solutionBox) {
            try { playClickSfx(); } catch(e) {}
            
            if (selectedOpt === correctOpt) {
                btnEl.style.backgroundColor = '#10B981';
                btnEl.style.color = '#020617';
                alert("ĐÚNG RỒI! Bạn nhận được +20 Roblox XP!");
            } else {
                btnEl.style.backgroundColor = '#EF4444';
                alert(`Chưa chính xác! Đáp án đúng là: ${correctOpt}`);
            }
            if (solutionBox) solutionBox.style.display = 'block';
        }


        async function loadFormulas() {
            const lop = document.getElementById('selFormulaLop').value;
            const mon = document.getElementById('selMonFormula').value;
            const res = await fetch(`/api/questions?skill=formula&lop=${encodeURIComponent(lop)}&mon=${encodeURIComponent(mon)}`);
            const d = await res.json();
            document.getElementById('formulaDisplay').innerHTML = d.questions.map(f => `<div style="background-color: #020617; padding: 20px; margin-top: 16px; border-radius: 18px; border: 2px solid #06B6D4;"><b>${f.ten} (${f.lop} - ${f.mon}):</b> <span style="color: #10B981; font-weight: 900;">${f.cong_thuc}</span><br><small style="color: #F1F5F9;">${f.vi_du}</small></div>`).join('');
        }

        async function loadPlan() {
            const res = await fetch('/api/notebook');
            const d = await res.json();
            const plan = d.study_plan;
            document.getElementById('planSummary').innerHTML = `
                <p><b>Chuỗi Ngày Học Streak:</b> <span style="color: #F59E0B; font-weight: 900;">${plan.streak_ngay || 1} ngày liên tiếp</span> (Ngọn lửa Fire active)</p>
                <p style="margin-top: 14px;"><b>Danh sách Mục tiêu hàng ngày:</b></p>
                <ul style="margin-left: 26px;">
                    ${(plan.danh_sach_muc_tieu || []).map(m => `<li>[${m.hoan_thanh ? 'ĐÃ HOÀN THÀNH' : 'CHƯA HOÀN THÀNH'}] ${m.noi_dung} (+${m.xp} XP)</li>`).join('')}
                </ul>
            `;
        }

        async function loadStats() {
            const res = await fetch('/api/settings');
            const d = await res.json();
            document.getElementById('hdrUserName').innerText = d.user_name;
            document.getElementById('hdrUserLevel').innerText = `Level ${d.rewards.level} | ${d.rewards.xp} XP | ${d.progress.streak} Streak`;
            if (document.getElementById('setUserName')) document.getElementById('setUserName').value = d.user_name;

            document.getElementById('statsSummary').innerHTML = `
                <p><b>Tên học sinh:</b> <span style="color: #06B6D4; font-weight: 900;">${d.user_name}</span></p>
                <p><b>Roblox Level:</b> Level ${d.rewards.level} (${d.rewards.xp} Roblox XP)</p>
                <p><b>Danh hiệu:</b> <span style="color: #10B981; font-weight: 900;">${d.rewards.level >= 5 ? 'Cao Thủ Tri Thức' : 'Tân Thủ Dũng Sĩ'}</span></p>
                <p><b>Số Roblox Coin:</b> ${d.rewards.coin} Coins</p>
                <p><b>Chuỗi ngày học Streak:</b> ${d.progress.streak} ngày liên tiếp</p>
                <p><b>Số Giấy Chứng Nhận Đã Đạt:</b> ${d.certificates.length} chứng nhận</p>
            `;
        }

        async function saveSettings() {
            const name = document.getElementById('setUserName').value;
            await fetch('/api/settings', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    ten_moi: name,
                    diem_mong_muon: document.getElementById('setDiem').value,
                    band_ielts_mong_muon: document.getElementById('setBand').value
                })
            });
            document.getElementById('settingsMsg').innerText = "Đã lưu thành công Cài đặt tên và điểm số mong muốn!";
            loadStats();
        }

        async function loadNotebook() {
            const res = await fetch('/api/notebook');
            const d = await res.json();
            const box = document.getElementById('notebookList');
            if (d.mistakes.length === 0) {
                box.innerHTML = '<p style="color: #10B981; font-weight: 900; font-size: 18px;">Tuyệt vời! Bạn không có câu hỏi nào bị làm sai trong Sổ lỗi sai.</p>';
            } else {
                box.innerHTML = d.mistakes.map((m, i) => `<div style="background-color: #020617; padding: 20px; margin-bottom: 16px; border-radius: 18px; border: 2.5px solid #EF4444;"><b>Câu ${i+1}:</b> ${m.cau_hoi}<br><span style="color:#10B981; font-weight: 900;">Đáp án đúng: ${m.dap_an_dung}</span></div>`).join('');
            }
        }

        // HAM XU LY MINIGAME THU GIAN GIUA CAC CAU HOI
        function openMinigameModal(cauSo) {
            const modal = document.getElementById('modalMinigameGiuaGio');
            if (!modal) return;
            document.getElementById('lblMinigameModalHeader').innerText = `MINIGAME THƯ GIÃN GIỮA GIỜ (CÂU ${cauSo || 1}) - THƯỞNG +XP`;
            modal.style.display = 'flex';
            const tabs = ['vongquay', 'penalty', 'latthe', 'gapthu'];
            const randTab = tabs[Math.floor(Math.random() * tabs.length)];
            showMinigameModalTab(randTab);
            try { playClickSfx(); } catch(e) {}
        }

        function closeMinigameModal() {
            const modal = document.getElementById('modalMinigameGiuaGio');
            if (modal) modal.style.display = 'none';
        }

        function showMinigameModalTab(tabName) {
            document.getElementById('tabModalVongQuay').style.display = tabName === 'vongquay' ? 'block' : 'none';
            document.getElementById('tabModalPenalty').style.display = tabName === 'penalty' ? 'block' : 'none';
            document.getElementById('tabModalLatThe').style.display = tabName === 'latthe' ? 'block' : 'none';
            document.getElementById('tabModalGapThu').style.display = tabName === 'gapthu' ? 'block' : 'none';
            
            if (tabName === 'vongquay') drawModalWheelCanvas();
            if (tabName === 'latthe') initModalMemoryCards();
            if (tabName === 'gapthu' && typeof khoi_tao_modal_gap_thu_3d === 'function') setTimeout(khoi_tao_modal_gap_thu_3d, 100);
        }

        function drawModalWheelCanvas() {
            const canvas = document.getElementById('canvasModalWheel');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            const rewards = ['+20 XP', '+50 XP', '+10 XP', '+100 XP', '+30 XP', '+80 XP'];
            const colors = ['#06B6D4', '#10B981', '#F59E0B', '#EC4899', '#A855F7', '#FF6B00'];
            const angle = (2 * Math.PI) / rewards.length;
            ctx.clearRect(0, 0, 200, 200);

            for (let i = 0; i < rewards.length; i++) {
                ctx.beginPath();
                ctx.fillStyle = colors[i];
                ctx.moveTo(100, 100);
                ctx.arc(100, 100, 95, i * angle, (i + 1) * angle);
                ctx.fill();
                ctx.lineWidth = 2;
                ctx.strokeStyle = '#FFFFFF';
                ctx.stroke();

                ctx.save();
                ctx.translate(100, 100);
                ctx.rotate(i * angle + angle / 2);
                ctx.fillStyle = '#FFFFFF';
                ctx.font = 'bold 12px sans-serif';
                ctx.fillText(rewards[i], 38, 5);
                ctx.restore();
            }
        }

        async function spinModalWheel() {
            try { playClickSfx(); } catch(e) {}
            let r = { xp: 50 };
            try {
                const res = await fetch('/api/games', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ type: 'wheel' })
                });
                const d = await res.json();
                if (d.reward) r = d.reward;
            } catch(err) {
                console.warn("Spin fallback:", err);
            }
            document.getElementById('modalWheelResult').innerText = `CHÚC MỪNG: Bạn quay trúng phần thưởng +${r.xp || 50} Roblox XP!`;
        }

        async function shootModalPenalty(direction) {
            try { playClickSfx(); } catch(e) {}
            const gk = document.getElementById('gkPosModal');
            const positions = ['5%', '35%', '70%'];
            if (gk) gk.style.left = positions[Math.floor(Math.random() * positions.length)];
            
            let isVao = Math.random() > 0.3;
            try {
                const res = await fetch('/api/games', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ type: 'penalty', direction: direction })
                });
                const d = await res.json();
                if (d.result && typeof d.result.vao !== 'undefined') isVao = d.result.vao;
            } catch(err) {
                console.warn("Penalty fallback:", err);
            }
            document.getElementById('modalPenaltyResult').innerText = isVao ? `VÀO OOO! Bàn thắng tuyệt đẹp hướng ${direction}! Nhận +50 XP!` : `ĐỐI THỦ THỦ MÔN CẢN PHÁ! Thử lại góc khác!`;
        }

        let modalMemoryCards = [];
        let modalFlipped = [];
        let modalMatched = 0;

        async function initModalMemoryCards() {
            try {
                const res = await fetch('/api/games', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ type: 'memory_cards' })
                });
                const d = await res.json();
                modalMemoryCards = d.cards || [];
            } catch(err) {
                console.warn("Memory cards fallback:", err);
            }

            if (!modalMemoryCards || modalMemoryCards.length === 0) {
                modalMemoryCards = [
                    { noi_dung: "SỐ HỌC", cap_id: 1, da_lat: false, da_ghep: false },
                    { noi_dung: "SỐ HỌC", cap_id: 1, da_lat: false, da_ghep: false },
                    { noi_dung: "HÌNH HỌC", cap_id: 2, da_lat: false, da_ghep: false },
                    { noi_dung: "HÌNH HỌC", cap_id: 2, da_lat: false, da_ghep: false },
                    { noi_dung: "ĐẠI SỐ", cap_id: 3, da_lat: false, da_ghep: false },
                    { noi_dung: "ĐẠI SỐ", cap_id: 3, da_lat: false, da_ghep: false },
                    { noi_dung: "TIẾNG ANH", cap_id: 4, da_lat: false, da_ghep: false },
                    { noi_dung: "TIẾNG ANH", cap_id: 4, da_lat: false, da_ghep: false }
                ];
            }

            modalFlipped = [];
            modalMatched = 0;
            renderModalMemoryGrid();
        }

        function renderModalMemoryGrid() {
            const grid = document.getElementById('modalMemoryGrid');
            if (!grid) return;
            grid.innerHTML = modalMemoryCards.map((c, i) => `
                <div class="memory-card ${c.da_lat ? 'flipped' : ''} ${c.da_ghep ? 'matched' : ''}" onclick="flipModalMemoryCard(${i})">
                    ${c.da_lat || c.da_ghep ? c.noi_dung : '?'}
                </div>
            `).join('');
        }

        function flipModalMemoryCard(idx) {
            const card = modalMemoryCards[idx];
            if (!card || card.da_lat || card.da_ghep || modalFlipped.length >= 2) return;
            try { playClickSfx(); } catch(e) {}
            card.da_lat = true;
            modalFlipped.push({ card, idx });
            renderModalMemoryGrid();

            if (modalFlipped.length === 2) {
                setTimeout(() => {
                    const [first, second] = modalFlipped;
                    if (first.card.cap_id === second.card.cap_id) {
                        first.card.da_ghep = true;
                        second.card.da_ghep = true;
                        modalMatched++;
                        if (modalMatched >= modalMemoryCards.length / 2) {
                            document.getElementById('modalMemoryResult').innerText = "XUẤT SẮC! Đã ghép đúng tất cả các thẻ! Thưởng +100 Roblox XP!";
                        }
                    } else {
                        first.card.da_lat = false;
                        second.card.da_lat = false;
                    }
                    modalFlipped = [];
                    renderModalMemoryGrid();
                }, 800);
            }
        }
        // OBBY 100 MÀN PARKOUR JAVASCRIPT ENGINE - 6 CỤC PARKOUR / 6 CÂU HỎI MỖI MÀN
        let currentObbyLevel = 1;
        let selectedObbyWorldIdx = 0;
        let obbyCoresCollected = JSON.parse(localStorage.getItem('obby_cores') || '[]');
        let obbyMaxLevel = parseInt(localStorage.getItem('obby_max_level') || '1', 10);
        let obbyTimerId = null;
        let obbyTimeLeft = 45;
        let obbyStep = 0; // 0 den 6 cuc Parkour
        let obbyLives = 3; // 3 Mang choi moi luot
        let obby6Questions = [];
        let obbySelectedAns = "";

        const obbyWorldsData = [
            { id: 1, name: "World 1 - Glitch City", range: "Màn 1-10", desc: "Obby cơ bản, con đường vỡ, xe chạy, sàn sập, Glitch Portal" },
            { id: 2, name: "World 2 - Lava Factory", range: "Màn 11-20", desc: "Dung nham, ống hơi nước, băng chuyền, máy ép, Lava Rise" },
            { id: 3, name: "World 3 - Frozen Mountain", range: "Màn 21-30", desc: "Băng trượt, cầu tuyết lăn, bão tuyết, cầu vỡ" },
            { id: 4, name: "World 4 - Poison Jungle", range: "Màn 31-40", desc: "Lá khổng lồ, đu dây, cây ăn thịt, đầm độc" },
            { id: 5, name: "World 5 - Flooded City", range: "Màn 41-50", desc: "Nước dâng, sóng lớn, đường ống, Tsunami Escape" },
            { id: 6, name: "World 6 - Space Station", range: "Màn 51-60", desc: "Trọng lực thấp, Gravity Switch, thiên thạch, vệ tinh" },
            { id: 7, name: "World 7 - Robot Factory", range: "Màn 61-70", desc: "Băng chuyền tốc độ cao, tay robot, bánh răng, Mini Boss Robot" },
            { id: 8, name: "World 8 - Time World", range: "Màn 71-80", desc: "Platform 2s biến mất, Time Stop, bánh răng đồng hồ" },
            { id: 9, name: "World 9 - Cyber World", range: "Màn 81-90", desc: "Bàn phím khổng lồ, mạch điện, đường hầm dữ liệu, Virus Chase" },
            { id: 10, name: "World 10 - Glitch Core", range: "Màn 91-100", desc: "Tổng hợp cơ chế, Màn 99 Final Run, Màn 100 Boss Glitch-X 3 Phase" }
        ];

        function updateObbyLivesDisplay() {
            const lbl = document.getElementById('lblObbyLives');
            if (lbl) lbl.innerText = `Mạng sống: ${obbyLives} / 3 mạng`;
        }

        function renderObbyWorlds() {
            const container = document.getElementById('obbyWorldButtons');
            if (!container) return;
            container.innerHTML = '';
            obbyWorldsData.forEach((w, idx) => {
                const btn = document.createElement('button');
                btn.className = idx === selectedObbyWorldIdx ? 'btn-primary' : 'btn-secondary';
                btn.style.fontSize = '12px';
                btn.style.padding = '6px 12px';
                btn.innerText = `W${w.id}: ${w.range}`;
                btn.onclick = () => {
                    selectedObbyWorldIdx = idx;
                    renderObbyWorlds();
                    renderObbyGrid(idx);
                };
                container.appendChild(btn);
            });
            const statusEl = document.getElementById('lblObbyCoreStatus');
            if (statusEl) statusEl.innerText = `Số Glitch Cores đã thu thập: ${obbyCoresCollected.length} / 10 Cores | Checkpoint cao nhất mở khóa: Màn ${obbyMaxLevel}`;
        }

        function renderObbyGrid(wIdx) {
            const container = document.getElementById('gridObbyLevels');
            const lblName = document.getElementById('lblObbyWorldName');
            if (!container) return;
            container.innerHTML = '';
            const wInfo = obbyWorldsData[wIdx];
            if (lblName) lblName.innerText = `${wInfo.name} (${wInfo.range})`;

            const startLvl = wIdx * 10 + 1;
            for (let l = startLvl; l < startLvl + 10; l++) {
                const btn = document.createElement('button');
                btn.style.fontWeight = '900';
                btn.style.padding = '10px';
                btn.style.borderRadius = '10px';
                btn.style.cursor = 'pointer';
                btn.innerText = `Màn ${l}`;

                if (l === currentObbyLevel) {
                    btn.style.background = '#F59E0B'; btn.style.color = '#000'; btn.style.border = '2px solid #FFF';
                } else if (l <= obbyMaxLevel) {
                    btn.style.background = '#10B981'; btn.style.color = '#FFF'; btn.style.border = 'none';
                } else {
                    btn.style.background = '#3B82F6'; btn.style.color = '#FFF'; btn.style.border = 'none';
                }

                btn.onclick = () => {
                    currentObbyLevel = l;
                    obbyStep = 0;
                    obbyLives = 3;
                    renderObbyGrid(wIdx);
                    startObbyLevelGame();
                };
                container.appendChild(btn);
            }
        }

        function startObbyLevelGame() {
            obbyStep = 0;
            obbyLives = 3;
            updateObbyLivesDisplay();

            const wIdx = Math.floor((currentObbyLevel - 1) / 10);
            const wInfo = obbyWorldsData[wIdx] || obbyWorldsData[0];
            const titleEl = document.getElementById('lblObbyCurrentLevelTitle');
            const descEl = document.getElementById('lblObbyMechanicDesc');
            if (titleEl) titleEl.innerText = `MÀN ${currentObbyLevel} - ${wInfo.name.toUpperCase()}`;
            if (descEl) descEl.innerText = `Cơ chế: 6 Cục Parkour | 3 Mạng chơi. Thưởng: +${currentObbyLevel % 10 === 0 ? 200 : 50} Roblox XP!`;

            obbyTimeLeft = currentObbyLevel === 100 ? 120 : (currentObbyLevel % 10 === 0 ? 90 : 60);
            const timerEl = document.getElementById('lblObbyTimer');
            if (timerEl) timerEl.innerText = `Thời gian còn lại: 00:${obbyTimeLeft < 10 ? '0' + obbyTimeLeft : obbyTimeLeft}`;

            if (obbyTimerId) clearInterval(obbyTimerId);
            obbyTimerId = setInterval(() => {
                if (obbyTimeLeft > 0) {
                    obbyTimeLeft--;
                    const tEl = document.getElementById('lblObbyTimer');
                    if (tEl) tEl.innerText = `Thời gian còn lại: 00:${obbyTimeLeft < 10 ? '0' + obbyTimeLeft : obbyTimeLeft}`;
                } else {
                    clearInterval(obbyTimerId);
                    alert(`Hết thời gian vượt Màn ${currentObbyLevel}! Bạn rơi khỏi Cục Parkour. Quay lại Checkpoint trước!`);
                    startObbyLevelGame();
                }
            }, 1000);

            // Sinh kho 6 cau hoi cho 6 cuc Parkour tu kho 10.000+ cau hoi va tu vung IELTS
            obby6Questions = generateProceduralObby6Questions(currentObbyLevel);

            renderObbyStepQuestion();
        }

        const ieltsVocabDatabase = [
            { w: "ABUNDANT", m: "Dồi dào, phong phú", s: "Plentiful", a: "Scarce" },
            { w: "BENEFICIAL", m: "Có lợi, có ích", s: "Helpful", a: "Harmful" },
            { w: "COMPREHENSIVE", m: "Toàn diện, bao quát", s: "Thorough", a: "Limited" },
            { w: "CRITICAL", m: "Quan trọng, then chốt", s: "Vital", a: "Trivial" },
            { w: "DIVERSE", m: "Đa dạng, phong phú", s: "Varied", a: "Uniform" },
            { w: "EFFICIENT", m: "Hiệu quả, năng suất", s: "Effective", a: "Inefficient" },
            { w: "FLEXIBLE", m: "Linh hoạt, dễ thích ứng", s: "Adaptable", a: "Rigid" },
            { w: "INNOVATIVE", m: "Sáng tạo, đổi mới", s: "Creative", a: "Traditional" },
            { w: "OBVIOUS", m: "Rõ ràng, hiển nhiên", s: "Clear", a: "Hidden" },
            { w: "PRECISE", m: "Chính xác, tỉ mỉ", s: "Accurate", a: "Vague" },
            { w: "SIGNIFICANT", m: "Đáng kể, quan trọng", s: "Important", a: "Minor" },
            { w: "TEMPORARY", m: "Tạm thời, ngắn hạn", s: "Short-term", a: "Permanent" },
            { w: "ACCUMULATE", m: "Tích lũy, dồn lại", s: "Gather", a: "Disperse" },
            { w: "CHALLENGE", m: "Thử thách, thách thức", s: "Test", a: "Ease" },
            { w: "DETERMINE", m: "Xác định, quyết định", s: "Decide", a: "Hesitate" },
            { w: "ENHANCE", m: "Nâng cao, tăng cường", s: "Improve", a: "Reduce" },
            { w: "FUNDAMENTAL", m: "Cơ bản, nền tảng", s: "Essential", a: "Secondary" },
            { w: "GUARANTEE", m: "Bảo đảm, cam kết", s: "Ensure", a: "Endanger" },
            { w: "IDENTIFY", m: "Nhận dạng, phát hiện", s: "Recognize", a: "Overlook" },
            { w: "JUSTIFY", m: "Bào chữa, chứng minh", s: "Explain", a: "Condemn" },
            { w: "MAINTAIN", m: "Duy trì, bảo dưỡng", s: "Preserve", a: "Abandon" },
            { w: "OBTAIN", m: "Đạt được, lấy được", s: "Acquire", a: "Lose" },
            { w: "PROMOTE", m: "Thúc đẩy, quảng bá", s: "Encourage", a: "Hinder" },
            { w: "RESOLVE", m: "Giải quyết, quyết định", s: "Solve", a: "Complicate" },
            { w: "STRENGTHEN", m: "Củng cố, làm mạnh", s: "Reinforce", a: "Weaken" }
        ];

        function toggleObbySolution() {
            const box = document.getElementById('boxObbySolution');
            if (box) {
                box.style.display = (box.style.display === 'none' || !box.style.display) ? 'block' : 'none';
            }
        }

        function generateProceduralObby6Questions(level) {
            const list = [];
            const wIdx = Math.floor((level - 1) / 10);
            const wInfo = obbyWorldsData[wIdx] || obbyWorldsData[0];

            for (let step = 1; step <= 6; step++) {
                const seed = level * 100 + step + Math.floor(Math.random() * 5000);
                const qType = (step + seed) % 6;

                let qText = "";
                let opts = [];
                let correct = "";
                let explain = "";

                if (qType === 0) {
                    // Tu vung Tieng Anh IELTS
                    const vocab = ieltsVocabDatabase[(seed + step) % ieltsVocabDatabase.length];
                    const subType = seed % 3;
                    if (subType === 0) {
                        qText = `CỤC PARKOUR ${step}/6 (Màn ${level}): Chọn từ ĐỒNG NGHĨA (Synonym) gần nhất với từ IELTS '${vocab.w}':`;
                        correct = vocab.s;
                        opts = [vocab.s, vocab.a, "Random", "Negligible"];
                        explain = `BÀI GIẢI CHI TIẾT:\nStep 1: Từ vựng IELTS '${vocab.w}' có nghĩa Tiếng Việt là '${vocab.m}'.\nStep 2: Xét nghĩa các phương án, từ đồng nghĩa (Synonym) chính xác nhất là '${vocab.s}' (mang nghĩa gần nhất với ${vocab.w}).\nStep 3: Từ trái nghĩa là '${vocab.a}'.\n-> ĐÁP ÁN ĐÚNG: ${vocab.s}`;
                    } else if (subType === 1) {
                        qText = `CỤC PARKOUR ${step}/6 (Màn ${level}): Nghĩa Tiếng Việt chính xác của từ vựng IELTS '${vocab.w}' là gì?`;
                        correct = vocab.m;
                        opts = [vocab.m, "Tạm hoãn", "Gây hại", "Không cố định"];
                        explain = `BÀI GIẢI CHI TIẾT:\nStep 1: Tra cứu từ điển Academic IELTS cho từ '${vocab.w}'.\nStep 2: Từ '${vocab.w}' được dịch chính xác sang Tiếng Việt là '${vocab.m}'.\nStep 3: Ví dụ câu: This element is ${vocab.w.toLowerCase()} in nature.\n-> ĐÁP ÁN ĐÚNG: ${vocab.m}`;
                    } else {
                        qText = `CỤC PARKOUR ${step}/6 (Màn ${level}): Chọn từ TRÁI NGHĨA (Antonym) với từ IELTS '${vocab.w}':`;
                        correct = vocab.a;
                        opts = [vocab.a, vocab.s, "Normal", "Constant"];
                        explain = `BÀI GIẢI CHI TIẾT:\nStep 1: Từ vựng '${vocab.w}' có nghĩa là '${vocab.m}' (Đồng nghĩa: ${vocab.s}).\nStep 2: Từ trái nghĩa (Antonym) phản bác lại nghĩa gốc là '${vocab.a}'.\n-> ĐÁP ÁN ĐÚNG: ${vocab.a}`;
                    }
                } else if (qType === 1) {
                    // Toan hoc - Dai so & Phep tinh
                    const a = (seed % 40) + 5;
                    const b = (seed % 15) + 2;
                    const c = (seed % 10) + 3;
                    const val = a * c + b;
                    qText = `CỤC PARKOUR ${step}/6 (Màn ${level}): Tính giá trị biểu thức P = ${a} x ${c} + ${b}:`;
                    correct = `${val}`;
                    opts = [`${val}`, `${val + 5}`, `${val - 3}`, `${val + 10}`];
                    explain = `BÀI GIẢI CHI TIẾT:\nStep 1: Áp dụng quy tắc thứ tự thực hiện phép tính (Phép nhân thực hiện trước phép cộng).\nStep 2: Tính tích: ${a} x ${c} = ${a * c}.\nStep 3: Cộng tiếp số b: ${a * c} + ${b} = ${val}.\n-> ĐÁP SỐ ĐÚNG: ${val}`;
                } else if (qType === 2) {
                    // Toan hoc - Hinh hoc & Dien tich
                    const w = (seed % 12) + 4;
                    const h = (seed % 8) + 3;
                    const area = w * h;
                    qText = `CỤC PARKOUR ${step}/6 (Màn ${level}): Diện tích hình chữ nhật có chiều dài ${w} cm và chiều rộng ${h} cm là:`;
                    correct = `${area} cm²`;
                    opts = [`${area} cm²`, `${area + 6} cm²`, `${area - 4} cm²`, `${area + 12} cm²`].sort(() => Math.random() - 0.5);
                    explain = `BÀI GIẢI CHI TIẾT:\nStep 1: Công thức tính diện tích hình chữ nhật: S = Chiều dài x Chiều rộng.\nStep 2: Thay số chiều dài = ${w} cm, chiều rộng = ${h} cm.\nStep 3: Tính toán: S = ${w} x ${h} = ${area} (cm²).\n-> ĐÁP SỐ ĐÚNG: ${area} cm²`;
                } else if (qType === 3) {
                    // Tin hoc & Python
                    const n = (seed % 20) + 2;
                    const p = (seed % 5) + 2;
                    const res = n * p;
                    qText = `CỤC PARKOUR ${step}/6 (Màn ${level}): Kết quả của biểu thức Python print(${n} * ${p}) là:`;
                    correct = `${res}`;
                    opts = [`${res}`, `${res + 3}`, `${n + p}`, `${res - 2}`].sort(() => Math.random() - 0.5);
                    explain = `BÀI GIẢI CHI TIẾT:\nStep 1: Trong ngôn ngữ lập trình Python, toán tử * biểu thị phép nhân.\nStep 2: Thực hiện phép nhân số nguyên: ${n} x ${p} = ${res}.\nStep 3: Lệnh print() in giá trị kết quả ${res} ra màn hình terminal/console.\n-> ĐÁP ÁN ĐÚNG: ${res}`;
                } else if (qType === 4) {
                    // Vat ly & Hoa hoc
                    const v = (seed % 30) + 20;
                    const t = (seed % 4) + 2;
                    const dist = v * t;
                    qText = `CỤC PARKOUR ${step}/6 (Màn ${level}): Một vật di chuyển đều với vận tốc v = ${v} km/h trong t = ${t} giờ. Quãng đường s đi được là:`;
                    correct = `${dist} km`;
                    opts = [`${dist} km`, `${dist + 15} km`, `${dist - 10} km`, `${dist + 25} km`].sort(() => Math.random() - 0.5);
                    explain = `BÀI GIẢI CHI TIẾT:\nStep 1: Công thức tính quãng đường trong chuyển động thẳng đều: s = v x t.\nStep 2: Thay số vận tốc v = ${v} km/h và thời gian t = ${t} giờ.\nStep 3: Tính toán: s = ${v} x ${t} = ${dist} (km).\n-> ĐÁP SỐ ĐÚNG: ${dist} km`;
                } else {
                    // Dinh nghia Trong tam SGK
                    const sgkList = [
                        { q: `Đơn vị đo độ dài hợp pháp của Việt Nam là gì?`, c: "Mét (m)", o: ["Mét (m)", "Xentimét (cm)", "Kilômét (km)", "Milimét (mm)"], e: "Theo chuẩn Hệ đo lường quốc tế (SI) và pháp luật Việt Nam, đơn vị đo độ dài cơ bản là Mét (kí hiệu m)." },
                        { q: `Khối lượng riêng của một chất được tính theo công thức nào?`, c: "D = m / V", o: ["D = m / V", "D = m x V", "D = V / m", "D = m + V"], e: "Khối lượng riêng D của một chất được xác định bằng khối lượng m của một thể tích V chất đó: D = m / V (kg/m³)." },
                        { q: `Kim loại duy nhất ở dạng lỏng ở nhiệt độ phòng là gì?`, c: "Thủy ngân (Hg)", o: ["Thủy ngân (Hg)", "Sắt (Fe)", "Đồng (Cu)", "Nhôm (Al)"], e: "Thủy ngân (Hg - Mercury) là kim loại duy nhất tồn tại ở thể lỏng ở nhiệt độ và áp suất tiêu chuẩn." },
                        { q: `Công thức hóa học của muối ăn hàng ngày là gì?`, c: "NaCl", o: ["NaCl", "NaOH", "HCl", "CaCO3"], e: "Muối ăn tinh khiết là hợp chất Natri Clorua được cấu tạo từ 1 nguyên tử Na và 1 nguyên tử Cl (NaCl)." },
                        { q: `Bào quan nào là 'nhà máy năng lượng' của tế bào?`, c: "Ti thể", o: ["Ti thể", "Nhân tế bào", "Lưới nội chất", "Không bào"], e: "Ti thể (Mitochondria) đóng vai trò hô hấp tế bào, chuyển hóa chất dinh dưỡng thành ATP năng lượng." }
                    ];
                    const item = sgkList[seed % sgkList.length];
                    qText = `CỤC PARKOUR ${step}/6 (Màn ${level}): ${item.q}`;
                    correct = item.c;
                    opts = item.o.sort(() => Math.random() - 0.5);
                    explain = `BÀI GIẢI CHI TIẾT:\nStep 1: Xóa tan hoài nghi bằng kiến thức SGK định hình chuẩn xác: ${item.q}\nStep 2: Căn cứ khoa học: ${item.e}\n-> ĐÁP ÁN ĐÚNG: ${item.c}`;
                }

                if (!opts.includes(correct)) opts[0] = correct;
                opts = Array.from(new Set(opts)).sort(() => Math.random() - 0.5);
                if (opts.length < 3) opts.push("Đáp án khác");

                list.push({ q: qText, opts: opts, correct: correct, explain: explain });
            }
            return list;
        }

        function renderObbyStepQuestion() {
            drawObbyCanvas(obbyStep);
            updateObbyLivesDisplay();

            const solBox = document.getElementById('boxObbySolution');
            if (solBox) {
                solBox.style.display = 'none';
            }

            if (obbyStep >= 6) {
                return;
            }

            const currentQ = obby6Questions[obbyStep];
            obbySelectedAns = "";

            const qTextEl = document.getElementById('lblObbyQText');
            if (qTextEl) qTextEl.innerHTML = `<span style="color: #F59E0B; font-weight: 900;">[CỤC PARKOUR ${obbyStep + 1} / 6]</span> - ${currentQ.q}`;
            
            if (solBox && currentQ.explain) {
                solBox.innerText = currentQ.explain;
            }

            const optsContainer = document.getElementById('boxObbyOpts');
            if (optsContainer) {
                optsContainer.innerHTML = '';
                const badgeLetters = ['A', 'B', 'C', 'D'];
                currentQ.opts.forEach((opt, idx) => {
                    const letter = badgeLetters[idx] || (idx + 1);
                    const b = document.createElement('button');
                    b.className = 'option-btn';
                    b.style.cursor = 'pointer';
                    b.style.pointerEvents = 'auto';
                    b.style.display = 'flex';
                    b.style.alignItems = 'center';
                    b.style.gap = '10px';
                    b.style.padding = '12px 18px';
                    b.style.margin = '4px 0';
                    b.style.borderRadius = '12px';
                    b.innerHTML = `<span class="option-badge" style="background: #06B6D4; color: #020617; font-weight: 900; padding: 4px 10px; border-radius: 8px;">${letter}</span> <span>${opt}</span>`;
                    
                    b.onclick = (e) => {
                        if (e) e.stopPropagation();
                        // 1-Click Instant Answer Evaluation & Platform Jump!
                        handleObbyOptionClick(opt, b);
                    };
                    optsContainer.appendChild(b);
                });
            }
        }

        let obbyJumpAnimId = null;

        function getPlayerSpotCoords(stepIndex) {
            const spots = [
                { x: 55, y: 115 },  // Spot 0 (Cục 1)
                { x: 165, y: 105 }, // Spot 1 (Cục 2)
                { x: 275, y: 95 },  // Spot 2 (Cục 3)
                { x: 385, y: 100 }, // Spot 3 (Cục 4)
                { x: 495, y: 90 },  // Spot 4 (Cục 5)
                { x: 605, y: 85 },  // Spot 5 (Cục 6)
                { x: 685, y: 60 }   // Spot 6 (Cột Cờ Checkpoint)
            ];
            return spots[stepIndex] || spots[0];
        }

        function animateObbyJump(fromStep, toStep, callback) {
            if (obbyJumpAnimId) cancelAnimationFrame(obbyJumpAnimId);

            const startPos = getPlayerSpotCoords(fromStep);
            const targetPos = getPlayerSpotCoords(toStep);

            let startTime = null;
            const duration = 450; // 450ms smooth parabolic arc jump

            function stepAnim(timestamp) {
                if (!startTime) startTime = timestamp;
                const progress = Math.min(1, (timestamp - startTime) / duration);

                const currentX = startPos.x + (targetPos.x - startPos.x) * progress;
                const arcHeight = Math.sin(progress * Math.PI) * 60;
                const currentY = (startPos.y + (targetPos.y - startPos.y) * progress) - arcHeight;

                drawObbyCanvas(fromStep, currentX, currentY);

                if (progress < 1) {
                    obbyJumpAnimId = requestAnimationFrame(stepAnim);
                } else {
                    drawObbyCanvas(toStep);
                    if (callback) callback();
                }
            }

            obbyJumpAnimId = requestAnimationFrame(stepAnim);
        }

        function showObbySolutionWithJumpButton(fromStep, toStep) {
            const solBox = document.getElementById('boxObbySolution');
            if (solBox) {
                const currentQ = obby6Questions[fromStep];
                const explainText = currentQ ? currentQ.explain : "";
                solBox.innerHTML = `
                    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1E293B; padding-bottom: 8px; margin-bottom: 10px; flex-wrap: wrap; gap: 8px;">
                        <span style="font-weight: 900; color: #10B981; font-size: 16px;">ĐÁP ÁN CHÍNH XÁC! Hướng dẫn giải chi tiết [Cục ${fromStep + 1}]</span>
                        <span style="background: rgba(16, 185, 129, 0.15); border: 1px solid #10B981; color: #10B981; padding: 4px 12px; border-radius: 8px; font-weight: 900; font-size: 13px;">Không giới hạn thời gian xem bài giải</span>
                    </div>
                    <div style="margin-bottom: 16px; line-height: 1.7; font-size: 14px;">${explainText}</div>
                    <div style="text-align: center; padding-top: 6px;">
                        <button class="btn-primary" style="background: linear-gradient(135deg, #10B981, #059669); font-weight: 900; font-size: 16px; padding: 12px 36px; border-radius: 12px; box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4); cursor: pointer;" onclick="executeObbyJumpNow(${fromStep}, ${toStep})">NHẢY SANG CỤC TIẾP THEO</button>
                    </div>
                `;
                solBox.style.display = 'block';
            }
        }

        function showObbyFailSolutionWithRetryButton(stepIndex) {
            const solBox = document.getElementById('boxObbySolution');
            if (solBox) {
                const currentQ = obby6Questions[stepIndex];
                const explainText = currentQ ? currentQ.explain : "";
                solBox.innerHTML = `
                    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1E293B; padding-bottom: 8px; margin-bottom: 10px; flex-wrap: wrap; gap: 8px;">
                        <span style="font-weight: 900; color: #EF4444; font-size: 16px;">HẾT 3 MẠNG CHƠI! Bài giải chi tiết [Cục ${stepIndex + 1}]</span>
                        <span style="background: rgba(239, 68, 68, 0.15); border: 1px solid #EF4444; color: #EF4444; padding: 4px 12px; border-radius: 8px; font-weight: 900; font-size: 13px;">Không giới hạn thời gian xem bài giải</span>
                    </div>
                    <div style="margin-bottom: 16px; line-height: 1.7; font-size: 14px;">${explainText}</div>
                    <div style="text-align: center; padding-top: 6px;">
                        <button class="btn-primary" style="background: linear-gradient(135deg, #EF4444, #DC2626); font-weight: 900; font-size: 16px; padding: 12px 36px; border-radius: 12px; box-shadow: 0 4px 15px rgba(239, 68, 68, 0.4); cursor: pointer;" onclick="restartObbyLevelGameNow()">THỬ LẠI LƯỢT CHƠI MỚI (VỀ CỤC 1)</button>
                    </div>
                `;
                solBox.style.display = 'block';
            }
        }

        function restartObbyLevelGameNow() {
            const solBox = document.getElementById('boxObbySolution');
            if (solBox) solBox.style.display = 'none';
            obbyStep = 0;
            obbyLives = 3;
            startObbyLevelGame();
        }

        function executeObbyJumpNow(fromStep, toStep) {
            const solBox = document.getElementById('boxObbySolution');
            if (solBox) solBox.style.display = 'none';

            try { playClickSfx(); } catch(e) {}

            // Trigger 60fps Parabolic Arc Jump from Cục N to Cục N+1!
            animateObbyJump(fromStep, toStep, () => {
                if (toStep < 6) {
                    renderObbyStepQuestion();
                } else {
                    // Successfully completed all 6 Parkour platforms!
                    if (obbyTimerId) clearInterval(obbyTimerId);

                    if (currentObbyLevel >= obbyMaxLevel) {
                        obbyMaxLevel = Math.min(100, currentObbyLevel + 1);
                        localStorage.setItem('obby_max_level', obbyMaxLevel.toString());
                    }

                    if (currentObbyLevel % 10 === 0) {
                        const coreId = currentObbyLevel / 10;
                        if (!obbyCoresCollected.includes(coreId)) {
                            obbyCoresCollected.push(coreId);
                            localStorage.setItem('obby_cores', JSON.stringify(obbyCoresCollected));
                        }
                    }

                    if (currentObbyLevel === 100) {
                        alert("YOU ESCAPED THE GLITCH WORLD!\n\nChúc mừng bạn đã nhảy hoàn thành 6 Cục Parkour Màn 100, đánh bại Boss Glitch-X và thu thập đủ 10 Glitch Cores!\nKích hoạt thành công MASTER CORE & Mở khóa HARD MODE!\nThưởng +2000 Roblox XP!");
                        currentObbyLevel = 1;
                    } else if (currentObbyLevel % 10 === 0) {
                        alert(`CHẠM CHECKPOINT THÀNH CÔNG!\n\nBạn đã nhảy qua đủ 6 Cục Parkour Màn ${currentObbyLevel} và thu thập GLITCH CORE #${currentObbyLevel / 10}!\nThưởng +200 Roblox XP!`);
                        currentObbyLevel++;
                    } else {
                        alert(`VƯỢT MÀN OBBY ${currentObbyLevel} THÀNH CÔNG!\n\nBạn đã nhảy qua đủ 6 Cục Parkour! Thưởng +50 Roblox XP!`);
                        currentObbyLevel++;
                    }

                    obbyStep = 0;
                    obbyLives = 3;
                    renderObbyWorlds();
                    renderObbyGrid(selectedObbyWorldIdx);
                    startObbyLevelGame();
                }
            });
        }

        function handleObbyOptionClick(optText, btnEl) {
            if (!obby6Questions || obbyStep >= 6) return;
            const currentQ = obby6Questions[obbyStep];
            const solBox = document.getElementById('boxObbySolution');

            if (optText === currentQ.correct) {
                // Trả lời ĐÚNG -> Đổi màu nút XANH và LỘ BÀI GIẢI CHI TIẾT không giới hạn kèm nút 'NHẢY SANG CỤC TIẾP THEO'!
                if (btnEl) {
                    btnEl.style.background = 'linear-gradient(135deg, #10B981, #059669)';
                    btnEl.style.color = '#FFFFFF';
                    btnEl.style.border = '2px solid #FFFFFF';
                }

                const fromStep = obbyStep;
                obbyStep++;
                const toStep = obbyStep;

                // Hien thi bai gia chi tiet khong gioi han thoi gian va co nut NHAY SANG CUC TIEP THEO!
                showObbySolutionWithJumpButton(fromStep, toStep);
            } else {
                // Trả lời SAI -> Trừ 1 Mạng
                obbyLives--;
                updateObbyLivesDisplay();

                if (btnEl) {
                    btnEl.style.background = 'linear-gradient(135deg, #EF4444, #DC2626)';
                    btnEl.style.color = '#FFFFFF';
                }

                if (obbyLives > 0) {
                    // Vẫn còn mạng -> CẤM LỘ BÀI GIẢI!
                    if (solBox) solBox.style.display = 'none';
                    setTimeout(() => {
                        alert(`ĐÁP ÁN CHƯA CHÍNH XÁC!\n\nBạn bị trừ 1 mạng chơi (Còn ${obbyLives}/3 mạng). Cấm lộ bài giải khi vẫn còn mạng. Hãy thử chọn đáp án khác tại Cục Parkour ${obbyStep + 1}!`);
                    }, 150);
                } else {
                    // Đã sai hết 3 mạng -> LỘ BÀI GIẢI CHỈ CÂU ĐÓ không giới hạn thời gian kèm nút 'THỬ LẠI LƯỢT CHƠI MỚI'!
                    if (obbyTimerId) clearInterval(obbyTimerId);
                    showObbyFailSolutionWithRetryButton(obbyStep);
                }
            }
        }

        let obbySpeechRecognition = null;
        let isObbyVoiceActive = false;

        function toggleObbyVoiceControl() {
            const btn = document.getElementById('btnObbyVoice');
            const status = document.getElementById('lblObbyVoiceStatus');
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

            if (!isObbyVoiceActive) {
                isObbyVoiceActive = true;
                if (btn) {
                    btn.innerText = "TẮT ĐIỀU KHIỂN GIỌNG NÓI AI";
                    btn.style.background = "linear-gradient(135deg, #EF4444, #DC2626)";
                }
                if (status) {
                    status.innerText = "Giọng nói AI: ĐANG LẮNG NGHE (Hãy nói 'Đáp án A', 'Nhảy', 'Bắt đầu')";
                    status.style.color = "#10B981";
                }

                if (SpeechRecognition) {
                    try {
                        if (!obbySpeechRecognition) {
                            obbySpeechRecognition = new SpeechRecognition();
                            obbySpeechRecognition.continuous = true;
                            obbySpeechRecognition.interimResults = false;
                            obbySpeechRecognition.lang = 'vi-VN';

                            obbySpeechRecognition.onresult = function(event) {
                                const lastIdx = event.results.length - 1;
                                const transcript = event.results[lastIdx][0].transcript.trim();
                                if (status) status.innerText = `Giọng nói AI: Đã nhận diện '${transcript}'`;
                                processObbyVoiceCommand(transcript);
                            };

                            obbySpeechRecognition.onerror = function(event) {
                                console.warn("Lỗi Mic SpeechRecognition:", event.error);
                                if (event.error === 'not-allowed' || event.error === 'service-not-allowed') {
                                    alert("CHƯA CẤP QUYỀN MICROPHONE!\n\nVui lòng bấm vào biểu tượng Micro/Khóa trên thanh địa chỉ trình duyệt để 'Cho phép (Allow)' truy cập Micro.");
                                    toggleObbyVoiceControl();
                                }
                            };

                            obbySpeechRecognition.onend = function() {
                                if (isObbyVoiceActive) {
                                    try { obbySpeechRecognition.start(); } catch(e) {}
                                }
                            };
                        }
                        obbySpeechRecognition.start();
                    } catch(e) {
                        console.warn("Không thể khởi động SpeechRecognition, chuyển sang Nhập lệnh giọng nói AI", e);
                        promptObbyVoiceCommandFallback();
                    }
                } else {
                    promptObbyVoiceCommandFallback();
                }
            } else {
                isObbyVoiceActive = false;
                if (btn) {
                    btn.innerText = "BẬT ĐIỀU KHIỂN BẰNG GIỌNG NÓI AI";
                    btn.style.background = "linear-gradient(135deg, #10B981, #059669)";
                }
                if (status) {
                    status.innerText = "Giọng nói AI: Đang tắt (Bấm để kích hoạt nói lệnh 'Nhảy', 'Đáp án A', 'Bắt đầu')";
                    status.style.color = "#10B981";
                }
                if (obbySpeechRecognition) {
                    try { obbySpeechRecognition.stop(); } catch(e) {}
                }
            }
        }

        function promptObbyVoiceCommandFallback() {
            const cmd = prompt("BẠN ĐANG DÙNG ĐIỀU KHIỂN BẰNG GIỌNG NÓI AI\n\nNhập câu lệnh giọng nói của em (Ví dụ: 'Nhảy', 'Đáp án A', 'Đáp án B', 'Bắt đầu'):");
            if (cmd) {
                const status = document.getElementById('lblObbyVoiceStatus');
                if (status) status.innerText = `Giọng nói AI: Đã nhận diện '${cmd}'`;
                processObbyVoiceCommand(cmd);
            }
            isObbyVoiceActive = false;
            const btn = document.getElementById('btnObbyVoice');
            if (btn) {
                btn.innerText = "BẬT ĐIỀU KHIỂN BẰNG GIỌNG NÓI AI";
                btn.style.background = "linear-gradient(135deg, #10B981, #059669)";
            }
        }

        function processObbyVoiceCommand(text) {
            if (!text) return;
            const c = text.toLowerCase();

            if (c.includes("nhảy") || c.includes("nhay") || c.includes("tiếp tục") || c.includes("tiep tuc") || c.includes("next")) {
                const fromStep = obbyStep - 1 >= 0 ? obbyStep - 1 : 0;
                executeObbyJumpNow(fromStep, obbyStep);
            } else if (c.includes("bắt đầu") || c.includes("bat dau") || c.includes("chơi lại") || c.includes("start")) {
                startObbyLevelGame();
            } else if (obby6Questions && obby6Questions[obbyStep]) {
                const opts = obby6Questions[obbyStep].opts || [];
                const optsBtns = document.querySelectorAll('#boxObbyOpts .option-btn');

                if (c.includes("đáp án a") || c.includes("câu a") || c.includes("chọn a") || c.endsWith(" a") || c === "a") {
                    if (opts[0]) handleObbyOptionClick(opts[0], optsBtns[0]);
                } else if (c.includes("đáp án b") || c.includes("câu b") || c.includes("chọn b") || c.endsWith(" b") || c === "b") {
                    if (opts[1]) handleObbyOptionClick(opts[1], optsBtns[1]);
                } else if (c.includes("đáp án c") || c.includes("câu c") || c.includes("chọn c") || c.endsWith(" c") || c === "c") {
                    if (opts[2]) handleObbyOptionClick(opts[2], optsBtns[2]);
                } else if (c.includes("đáp án d") || c.includes("câu d") || c.includes("chọn d") || c.endsWith(" d") || c === "d") {
                    if (opts[3]) handleObbyOptionClick(opts[3], optsBtns[3]);
                }
            }
        }

        function drawObbyCanvas(step, customPlayerX, customPlayerY) {
            step = step || 0;
            const canvas = document.getElementById('canvasObby');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            ctx.clearRect(0, 0, 760, 200);

            // Background sky
            ctx.fillStyle = '#0F172A';
            ctx.fillRect(0, 0, 760, 200);

            // Lava or Hazard Floor
            ctx.fillStyle = currentObbyLevel > 10 && currentObbyLevel <= 20 ? '#EF4444' : '#020617';
            ctx.fillRect(0, 170, 760, 30);

            // 6 Cụm / Cục Parkour Platforms
            const platformPositions = [
                { x: 30, y: 140, w: 70 },
                { x: 140, y: 130, w: 70 },
                { x: 250, y: 120, w: 70 },
                { x: 360, y: 125, w: 70 },
                { x: 470, y: 115, w: 70 },
                { x: 580, y: 110, w: 70 }
            ];

            platformPositions.forEach((p, idx) => {
                if (idx < step) {
                    ctx.fillStyle = '#10B981'; // Đã nhảy qua (Xanh lá)
                } else if (idx === step) {
                    ctx.fillStyle = '#F59E0B'; // Đang đứng / Cụm hiện tại (Vàng)
                } else {
                    ctx.fillStyle = '#3B82F6'; // Cụm phía trước (Xanh dương)
                }
                ctx.fillRect(p.x, p.y, p.w, 15);

                // Số Cục Parkour 1-6
                ctx.fillStyle = '#FFFFFF';
                ctx.font = 'bold 11px sans-serif';
                ctx.fillText(`Cục ${idx + 1}`, p.x + 18, p.y + 11);
            });

            // Gold Checkpoint Flag at end
            ctx.fillStyle = '#F59E0B';
            ctx.fillRect(680, 85, 6, 45);
            ctx.beginPath();
            ctx.moveTo(686, 85);
            ctx.lineTo(710, 97);
            ctx.lineTo(686, 110);
            ctx.fill();

            // Player Avatar Position
            const defaultPos = getPlayerSpotCoords(step);
            let playerX = defaultPos.x;
            let playerY = defaultPos.y;

            if (typeof customPlayerX !== 'undefined' && typeof customPlayerY !== 'undefined') {
                playerX = customPlayerX;
                playerY = customPlayerY;
            }

            // Draw Player Sprite (Con Xanh Đố)
            ctx.fillStyle = '#06B6D4';
            ctx.fillRect(playerX, playerY, 20, 25);
            ctx.fillStyle = '#FFFFFF';
            ctx.fillRect(playerX + 5, playerY + 3, 5, 5);
            ctx.fillRect(playerX + 13, playerY + 3, 5, 5);
        }

        // VOICE CONTROL AI RECOGNITION ENGINE
        let obbySpeechRec = null;
        let isObbyVoiceActive = false;

        function toggleObbyVoiceControl() {
            const btn = document.getElementById('btnObbyVoice');
            const lbl = document.getElementById('lblObbyVoiceStatus');
            const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;

            if (!SpeechRec) {
                alert("Trình duyệt của bạn chưa hỗ trợ Web Speech API. Vui lòng sử dụng Chrome, Edge hoặc Safari mới nhất!");
                return;
            }

            if (isObbyVoiceActive) {
                isObbyVoiceActive = false;
                if (obbySpeechRec) {
                    try { obbySpeechRec.stop(); } catch(e) {}
                }
                if (btn) {
                    btn.innerText = "BẬT ĐIỀU KHIỂN BẰNG GIỌNG NÓI AI";
                    btn.style.background = "linear-gradient(135deg, #10B981, #059669)";
                }
                if (lbl) lbl.innerText = "Giọng nói AI: Đang tắt (Bấm để kích hoạt)";
            } else {
                isObbyVoiceActive = true;
                try {
                    obbySpeechRec = new SpeechRec();
                    obbySpeechRec.lang = 'vi-VN';
                    obbySpeechRec.continuous = true;
                    obbySpeechRec.interimResults = false;

                    obbySpeechRec.onresult = (event) => {
                        const lastResultIdx = event.results.length - 1;
                        const transcript = event.results[lastResultIdx][0].transcript.toLowerCase().trim();
                        if (lbl) lbl.innerText = `Giọng nói nhận diện: "${transcript}"`;
                        processObbyVoiceCommand(transcript);
                    };

                    obbySpeechRec.onerror = (event) => {
                        console.warn("Speech recognition error:", event.error);
                    };

                    obbySpeechRec.onend = () => {
                        if (isObbyVoiceActive) {
                            try { obbySpeechRec.start(); } catch(e) {}
                        }
                    };

                    obbySpeechRec.start();
                    if (btn) {
                        btn.innerText = "TẮT ĐIỀU KHIỂN GIỌNG NÓI";
                        btn.style.background = "linear-gradient(135deg, #EF4444, #DC2626)";
                    }
                    if (lbl) lbl.innerText = "Giọng nói AI: Đang lắng nghe... Hãy nói 'Nhảy', 'Đáp án A', 'Bắt đầu'...";
                    try { playClickSfx(); } catch(e) {}
                } catch(err) {
                    alert("Không thể khởi động micro giọng nói: " + err.message);
                }
            }
        }

        function processObbyVoiceCommand(text) {
            text = text.toLowerCase();
            
            // Voice command: Nhay / Parkour
            if (text.includes("nhảy") || text.includes("nhay") || text.includes("parkour") || text.includes("nhảy lên")) {
                try { playClickSfx(); } catch(e) {}
                drawObbyCanvas();
                return;
            }

            // Voice command: Bat dau / Choi
            if (text.includes("bắt đầu") || text.includes("chơi") || text.includes("start")) {
                startObbyLevelGame();
                return;
            }

            // Voice command: Nop bai / Checkpoint
            if (text.includes("nộp bài") || text.includes("chạm checkpoint") || text.includes("checkpoint")) {
                submitObbyLevelAnswer();
                return;
            }

            // Voice command: Dap an A / B / C
            const optsContainer = document.getElementById('boxObbyOpts');
            if (optsContainer && optsContainer.children.length > 0) {
                if (text.includes("đáp án a") || text.includes("câu a") || text.includes("lựa chọn a") || text.includes("đáp án 1") || text === "a") {
                    if (optsContainer.children[0]) optsContainer.children[0].click();
                    return;
                }
                if (text.includes("đáp án b") || text.includes("câu b") || text.includes("lựa chọn b") || text.includes("đáp án 2") || text === "b") {
                    if (optsContainer.children[1]) optsContainer.children[1].click();
                    return;
                }
                if (text.includes("đáp án c") || text.includes("câu c") || text.includes("lựa chọn c") || text.includes("đáp án 3") || text === "c") {
                    if (optsContainer.children[2]) optsContainer.children[2].click();
                    return;
                }
            }
        }

        window.onload = () => {
            loadStats();
            loadSavedGeminiApiKey();
            startBgMusic();
            renderObbyWorlds();
            renderObbyGrid(0);
        };
    

        function triggerRonaldoSiuuu() {
            try { playClickSfx(); } catch(e) {}
            const char = document.getElementById('ronaldoSprite');
            const bubble = document.getElementById('ronaldoSpeechBubble');
            if (char) {
                char.style.animation = 'ronaldoSiuuuJump 0.8s ease-in-out';
                setTimeout(() => {
                    char.style.animation = 'ronaldoWalk 2.5s infinite ease-in-out';
                }, 850);
            }
            if (bubble) {
                const quotes = [
                    "SIUUU! Bạn giỏi quá! +50 Roblox XP!",
                    "CR7 #7: Quyết tâm đạt điểm 10 học kỳ nào!",
                    "SIUUU! Cố lên bạn ơi, Ronaldo luôn đồng hành!",
                    "Vô địch World Cup & Champions League thôi!",
                    "Roblox Gaming & Tri thức số 1!"
                ];
                bubble.innerText = quotes[Math.floor(Math.random() * quotes.length)];
            }
        }

        function makeElementDraggable(elmnt, headerElmnt) {
            let pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
            const dragTarget = headerElmnt || elmnt;
            dragTarget.onmousedown = dragMouseDown;

            function dragMouseDown(e) {
                e = e || window.event;
                if (e.target.tagName === 'BUTTON' || e.target.tagName === 'INPUT') return;
                e.preventDefault();
                pos3 = e.clientX;
                pos4 = e.clientY;
                document.onmouseup = closeDragElement;
                document.onmousemove = elementDrag;
            }

            function elementDrag(e) {
                e = e || window.event;
                e.preventDefault();
                pos1 = pos3 - e.clientX;
                pos2 = pos4 - e.clientY;
                pos3 = e.clientX;
                pos4 = e.clientY;
                elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
                elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
                elmnt.style.bottom = 'auto';
                elmnt.style.right = 'auto';
            }

            function closeDragElement() {
                document.onmouseup = null;
                document.onmousemove = null;
            }
        }

        window.addEventListener('DOMContentLoaded', () => {
            const playerBox = document.getElementById('ytPlaylistContainer');
            const playerHeader = document.getElementById('ytPlaylistHeader');
            if (playerBox && playerHeader) {
                makeElementDraggable(playerBox, playerHeader);
            }
        });
    
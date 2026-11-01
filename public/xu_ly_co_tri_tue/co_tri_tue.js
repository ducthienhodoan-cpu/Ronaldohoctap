// Thu muc: public/xu_ly_co_tri_tue
// File: co_tri_tue.js
// Mo ta: Xu ly tuong tac giao dien Web cho Co Vua va Co Tuong - Dau Tri Ky Thu

(function () {
    "use strict";

    // Du lieu du phong khi offline hoac ket noi kem
    const DU_LIEU_CO_VUA_FALLBACK = {
        pieces: [
            { id: "tot", ten: "Tot (Pawn)", ky_hieu: "P", diem_gia_tri: 1, cach_di: "Di thang 1 o (nuoc dau duoc di 2 o). Khong duoc di lui.", cach_an: "An cheo 1 o ve phia truoc.", luu_y: "Co kha nang phong cap thanh Hau khi tien den hang cuoi cung." },
            { id: "ma", ten: "Ma (Knight)", ky_hieu: "N", diem_gia_tri: 3, cach_di: "Di theo hinh chu L (2 o mot huong va 1 o vuong goc).", cach_an: "An quan tai o dich den cua chu L.", luu_y: "Quan duy nhat co the nhay qua dau cac quan khac tren ban co." },
            { id: "tuong", ten: "Tuong (Bishop)", ky_hieu: "B", diem_gia_tri: 3, cach_di: "Di cheo theo cac o cung mau khong gioi han so o neu khong bi chan.", cach_an: "An quan tren duong cheo cua minh.", luu_y: "Moi ben co 1 Tuong o sang va 1 Tuong o toi, phoi hop kiem soat ban co." },
            { id: "xe", ten: "Xe (Rook)", ky_hieu: "R", diem_gia_tri: 5, cach_di: "Di ngang hoac doc khong gioi han so o neu khong bi chan.", cach_an: "An quan tren duong ngang hoac doc cua minh.", luu_y: "Quan co nang chu luc o giai doan trung cuoc va tan cuoc, tham gia Nhap thanh." },
            { id: "hau", ten: "Hau (Queen)", ky_hieu: "Q", diem_gia_tri: 9, cach_di: "Ket hop suc manh cua Xe va Tuong: di ngang, doc hoac cheo khong gioi han so o.", cach_an: "An quan tren moi duong di cua minh.", luu_y: "Quan co manh nhat ban co, can bao ve can than khong nen dua ra tran qua som." },
            { id: "vua", ten: "Vua (King)", ky_hieu: "K", diem_gia_tri: 999, cach_di: "Di 1 o theo bat ky huong nao (ngang, doc, cheo) vao o an toan.", cach_an: "An quan ke ben khong co bao ve.", luu_y: "Quan co toi thuong, bi chieu het la thua cuoc. Cuoi van tro thanh quan tan cong." }
        ],
        special_rules: [
            { ten: "Nhap thanh (Castling)", mo_ta: "Vua di 2 o ve phia Xe, Xe nhay qua Vua sang o ke ben. Dieu kien ca hai quan chua tung di chuyen va khong bi chieu." },
            { ten: "Bat tot qua duong (En Passant)", mo_ta: "Khi Tot doi phuong di 2 o dung canh Tot minh o hang 5, minh co quyen an Tot do nhu the no chi di 1 o." },
            { ten: "Phong cap (Pawn Promotion)", mo_ta: "Tot tien xuong hang 8 (Trang) hoac hang 1 (Den) duoc doi ngay thanh Hau, Xe, Tuong hoac Ma tuy chon." },
            { ten: "Chieu het va Co hoa (Checkmate & Stalemate)", mo_ta: "Chieu het la thang cuoc. Neu khong bi chieu nhung khong con nuoc di hop le thi van co hoa (the hoa Pat)." }
        ],
        openings: [
            { ten: "Khai cuoc Y (Italian Game)", nuoc: "1. e4 e5 2. Nf3 Nc6 3. Bc4", y_nghia: "Nhanh chong phat trien Ma va Tuong, kiem soat trung tam va nham vao diem yeu f7." },
            { ten: "Phong thu Sicilia (Sicilian Defense)", nuoc: "1. e4 c5", y_nghia: "Phan cong bat doi xung gay gat tu canh hau, tao the tran doi cong hap dan." },
            { ten: "Gambit Hau (Queen's Gambit)", nuoc: "1. d4 d5 2. c4", y_nghia: "Thi sinh tot c4 de keo tot doi phuong roi khoi trung tam va gianh quyen chu dong." },
            { ten: "Khai cuoc Tay Ban Nha (Ruy Lopez)", nuoc: "1. e4 e5 2. Nf3 Nc6 3. Bb5", y_nghia: "Gay suc ep lau dai len quan Ma bao ve trung tam e5 cua Den." }
        ],
        tactics: [
            { ten: "Don chia doi (Fork)", mo_ta: "Mot quan co (dac biet la Ma hoac Tot) tan cong dong thoi hai muc tieu gia tri cao cua doi phuong." },
            { ten: "Don ghim quan (Pin)", mo_ta: "Tan cong quan co ma phia sau la quan gia tri cao hon (nhu Vua hoac Hau), khien no khong the di chuyen." },
            { ten: "Don xien (Skewer)", mo_ta: "Quan co gia tri cao o phia truoc bi tan cong phai thao chay, lam lo quan gia tri phia sau bi bat." },
            { ten: "Don chieu mo (Discovered Attack)", mo_ta: "Di chuyen mot quan mo duong cho quan khac phia sau chieu tuong hoac tan cong bat ngo." }
        ],
        masters: [
            { ten: "Le Quang Liem", danh_hieu: "Sieu Dai kien tuong quoc te Viet Nam", thanh_tich: "Vo dich Co chop the gioi 2013, Elo dinh cao 2740+." },
            { ten: "Magnus Carlsen", danh_hieu: "Vua co the gioi hien dai (Na Uy)", thanh_tich: "Elo cao nhat lich su 2882, vo dich tat ca the thuc co." },
            { ten: "Garry Kasparov", danh_hieu: "Huyen thoai co vua the ky 20 (Nga)", thanh_tich: "Giu ngoi vo dich the gioi 15 nam lien tiep (1985 - 2000)." }
        ]
    };

    const DU_LIEU_CO_TUONG_FALLBACK = {
        pieces: [
            { id: "tuong_soai", ten: "Tuong / Soai (General)", ky_hieu: "TG", vi_tri: "O giua hang day trong Cuu Cung", cach_di: "Di tung o mot ngang hoac doc trong Cuu Cung. Khong duoc ra khoi cung.", quy_tac: "Luat mat Tuong: Hai Tuong khong bao gio duoc nhin thay nhau truc dien tren cung mot cot doc." },
            { id: "si", ten: "Si (Advisor)", ky_hieu: "SI", vi_tri: "Hai ben canh Tuong", cach_di: "Di cheo 1 o moi nuoc trong Cuu Cung.", quy_tac: "Nhiem vu ho ve Tuong, khong duoc ra khoi Cuu Cung." },
            { id: "tuong_voi", ten: "Tuong / Voi (Elephant)", ky_hieu: "TU", vi_tri: "Hai ben Si o hang day", cach_di: "Di cheo 2 o vuong (2x2).", quy_tac: "Khong duoc sang song. Neu co quan o giua duong cheo thi bi Can mat Tuong." },
            { id: "xe", ten: "Xe (Chariot)", ky_hieu: "XE", vi_tri: "Hai goc ban co", cach_di: "Di ngang hoac doc khong gioi han o neu khong bi can. An quan tren duong di.", quy_tac: "Quan co manh nhat ban co tuong, suc co dong va tan cong cao nhat." },
            { id: "phao", ten: "Phao (Cannon)", ky_hieu: "PH", vi_tri: "Hang 3 cach mep 2 o", cach_di: "Di ngang doc nhu Xe khi khong an quan.", quy_tac: "Khi an quan bat buoc phai nhay qua dung 1 quan co khac lam Ngoi." },
            { id: "ma", ten: "Ma (Horse)", ky_hieu: "MA", vi_tri: "Giua Xe va Tuong", cach_di: "Di theo hinh chu nhat (1 doc va 1 cheo hoac 1 ngang va 1 cheo).", quy_tac: "Bi Can chan Ma neu co quan dung o o lien ke theo huong buoc." },
            { id: "tot_binh", ten: "Tot / Binh (Soldier)", ky_hieu: "TO", vi_tri: "5 quan o hang 4", cach_di: "Chua sang song chi tien 1 o. Qua song duoc di thang hoac ngang 1 o.", quy_tac: "Tuyet doi khong bao gio duoc di lui. Sang song tro nen vo cung loi hai." }
        ],
        board_features: [
            { ten: "So Ha Han Gioi (Song)", y_nghia: "Ranh gioi giua 2 ben, Tuong khong duoc qua song, Tot qua song bat dau duoc di ngang." },
            { ten: "Cuu Cung (Cung Tuong)", y_nghia: "Khu vuc 3x3 co 2 duong cheo o moi dau san, Tuong va Si khong the roi khoi day." },
            { ten: "90 Giao Diem (Lo co)", y_nghia: "Quan co dat tai cac giao diem cua 9 duong doc va 10 duong ngang thay vi dat trong o." }
        ],
        tactics: [
            { ten: "Sat phap Ma Hau Phao", mo_ta: "Ma khong che cua thoat cua Tuong, dong thoi lam ngoi cho Phao phia sau chieu thang mat Tuong." },
            { ten: "Song Xe Toa Thanh", mo_ta: "Hai Xe tien sau vao Cuu Cung doi phuong, lien hoan chieu ep Tuong vao the het nuoc do." },
            { ten: "Diep Phao (Phao trung)", mo_ta: "Hai Phao cung nam tren mot duong, Phao truoc lam ngoi cho Phao sau chieu Tuong doi thu." },
            { ten: "Dai Dao Tieu Doi (Xe chem Si)", mo_ta: "Xe quyet doan chem Si pha toang phong tuyen Cuu Cung mo duong cho cac quan khac tran vao." }
        ],
        openings: [
            { ten: "Duong Dau Phao (Phao dau)", mo_ta: "Phao vao trung lo tan cong truc dien vao Tot dau va trung tam doi thu." },
            { ten: "Binh Phong Ma", mo_ta: "Hai Ma cung nhay len giu Tot dau, tao buc tuong phong thu vung chac va phan cong sac sao." },
            { ten: "Khoi Ma Cuoc", mo_ta: "Nuoc dau nhay Ma len giu trung lo, the tran uyen chuyen va giu nhieu bien hoa chien thuat." }
        ],
        masters: [
            { ten: "Lai Ly Huynh", danh_hieu: "Ky vuong so 1 Viet Nam", thanh_tich: "Vo dich the gioi Co nhanh 2022, nhieu nam vo dich quoc gia." },
            { ten: "Ho Vinh Hoa", danh_hieu: "Thap lien ba Trung Quoc", thanh_tich: "10 lan vo dich lien tiep, sang tao nhieu the tran khai cuoc kinh dien." }
        ]
    };

    const KHO_CAU_DO_FALLBACK = [
        {
            id: "cv_1",
            the_co: "Trang co Vua o g1, Xe o e1. Den co Vua o e8 dang o giua ban co va bi Xe kiem soat cot e.",
            cau_hoi: "Trong co vua, quan co nao la quan duy nhat co the nhay qua dau cac quan co khac tren ban co?",
            cac_lua_chon: ["A. Quan Tuong", "B. Quan Ma", "C. Quan Xe", "D. Quan Hau"],
            dap_an_dung: "B",
            giai_thich: "Quan Ma co cach di hinh chu L va la quan co duy nhat tren ban co duoc phep nhay qua dau bat ky quan nao."
        },
        {
            id: "cv_2",
            the_co: "Den vua di quan Tot tu d7 len d5 (di 2 o). Trang dang co quan Tot dung o o e5 ngay ben canh.",
            cau_hoi: "Trang co the su dung luat dac biet nao ngay lap tuc de bat quan Tot d5 cua Den?",
            cac_lua_chon: ["A. Luat Phong cap", "B. Luat Nhap thanh xa", "C. Luat Bat tot qua duong (En Passant)", "D. Luat Chieu het nhanh"],
            dap_an_dung: "C",
            giai_thich: "Luat Bat tot qua duong cho phep Tot Trang o hang 5 an Tot Den vua di 2 o ben canh bang cach di cheo xuong d6."
        },
        {
            id: "cv_3",
            the_co: "Quan Ma Trang nhay vao o e7 chieu Vua Den o g8, dong thoi tan cong quan Hau Den dang dung o c8.",
            cau_hoi: "Don chien thuat ma quan Ma Trang vua thuc hien duoc goi la don gi?",
            cac_lua_chon: ["A. Don chia doi (Fork)", "B. Don ghim quan (Pin)", "C. Don xien (Skewer)", "D. Don chieu mo"],
            dap_an_dung: "A",
            giai_thich: "Don chia doi la khi mot quan co (dac biet la Ma) tan cong dong thoi hai muc tieu gia tri cao khien doi thu khong the cuu het ca hai."
        },
        {
            id: "ct_1",
            the_co: "Hai ben dang giao tranh o trung lo. Tuong Do va Tuong Den cung nam tren duong doc lo 5 ma khong co quan can o giua.",
            cau_hoi: "Theo luat co tuong, tinh huong hai Tuong doi dien nhau truc tiep tren cung mot lo doc ma khong co quan chan duoc goi la gi?",
            cac_lua_chon: ["A. Luat mat Tuong - Nuoc di lam lo mat Tuong la pham luat", "B. Duoc phep va hai ben bat tay hoa co", "C. Ben nao di sau se bi chieu het ngay", "D. Ca hai Tuong deu bi loai khoi ban co"],
            dap_an_dung: "A",
            giai_thich: "Luat mat Tuong quy dinh hai Tuong khong bao gio duoc doi mat truc tiep tren cung mot cot doc ma khong co quan can."
        },
        {
            id: "ct_2",
            the_co: "Quan Phao Do muon an quan Xe Den dang dung o phia xa tren cung mot duong ngang.",
            cau_hoi: "Dieu kien bat buoc de quan Phao co the an quan doi phuong trong co tuong la gi?",
            cac_lua_chon: ["A. Phai co dung mot quan co bat ky o giua lam Ngoi", "B. Phai dung sat ngay ben canh quan Xe", "C. Phai co hai quan co o giua moi an duoc", "D. Khong can quan nao o giua, an giong nhu quan Xe"],
            dap_an_dung: "A",
            giai_thich: "Trong co tuong, quan Phao khi di chuyen khong can ngoi, nhung khi an quan doi phuong bat buoc phai co dung 1 quan lam Ngoi nhay qua."
        },
        {
            id: "ct_3",
            the_co: "Quan Ma Do dinh nhay vao de chieu Tuong Den, nhung ngay o lien ke truoc mat Ma co mot quan Tot dung chan.",
            cau_hoi: "Hien tuong nay trong co tuong duoc goi la gi va quan Ma co nhay duoc khong?",
            cac_lua_chon: ["A. Can chan Ma - Ma khong duoc phep nhay theo huong do", "B. Ma duoc phep nhay qua dau quan Tot", "C. Can mat Tuong - Ma van di binh thuong", "D. Ma phai an quan Tot do truoc"],
            dap_an_dung: "A",
            giai_thich: "Co tuong co quy tac Can chan Ma: neu co quan co dung o o lien ke theo huong Ma dinh buoc thi Ma bi can chan va khong the nhay."
        }
    ];

    const THE_CO_MAU_FALLBACK = [
        {
            id: "the_cv_1",
            loai: "co_vua",
            tieu_de: "Don Chia Doi Cua Ma Trang (Fork)",
            mo_ta: "Ma Trang o o c7 chieu Vua Den dong thoi bat quan Xe Den o a8.",
            loi_khuyen: "Luon de phong cac o ma quan Ma doi phuong co the nhay toi de bat doi quan.",
            ben_di_truoc: "Quan Trang (White)",
            nuoc_tiep_theo: "Vua Den buoc phai di chuyen tranh chieu, Ma Trang an Xe Den o a8 thu ve 5 diem."
        },
        {
            id: "the_cv_2",
            loai: "co_vua",
            tieu_de: "Chieu Het Hoc Gia (Scholar's Mate)",
            mo_ta: "Hau Trang an vao f7 chieu het Vua Den nho su bao ve cua Tuong Trang o c4.",
            loi_khuyen: "O khai cuoc diem f7 rat de bi tan cong, Den can phat trien Ma len f6 de chan Hau.",
            ben_di_truoc: "Quan Trang (White)",
            nuoc_tiep_theo: "Hau Trang an f7 ket thuc van co trong 4 nuoc neu Den phong thu so ho."
        },
        {
            id: "the_ct_1",
            loai: "co_tuong",
            tieu_de: "Sat Phap Ma Hau Phao",
            mo_ta: "Ma Do khoa cua thoat cua Tuong Den, Phao Do dung phia sau Ma chieu thang mat Tuong.",
            loi_khuyen: "Canh giac cao do khi thay Ma va Phao doi phuong hop luc tan cong vao mot lo.",
            ben_di_truoc: "Quan Do (Red)",
            nuoc_tiep_theo: "Tuong Den khong the di chuyen vi Ma can duong, khong an duoc Phao o xa, ket thuc tran."
        },
        {
            id: "the_ct_2",
            loai: "co_tuong",
            tieu_de: "Song Xe Toa Thanh Pha Cung",
            mo_ta: "Hai Xe Do chim xuong hang day va hang ap day cua Cuu Cung doi phuong.",
            loi_khuyen: "Phong tuyen Si va Tuong can duoc bao ve chat che de ngan Xe doi phuong ap sat.",
            ben_di_truoc: "Quan Do (Red)",
            nuoc_tiep_theo: "Xe 1 chieu ep Tuong len, Xe 2 ap sat chieu het buoc Tuong phai dau hang."
        }
    ];

    let currentQuizIndex = 0;
    let quizList = KHO_CAU_DO_FALLBACK;
    let userProgress = {
        cau_da_giai: [],
        tong_diem_exp: 0,
        danh_hieu: "Ky Thu Tap Su"
    };

    // Khoi tao du lieu tu serverless API hoac local storage
    async function napDuLieuCoTriTue() {
        try {
            const res = await fetch("/api/chess");
            if (res.ok) {
                const data = await res.json();
                if (data.status === "success") {
                    hienThiCoVua(data.co_vua || DU_LIEU_CO_VUA_FALLBACK);
                    hienThiCoTuong(data.co_tuong || DU_LIEU_CO_TUONG_FALLBACK);
                    if (data.co_vua && data.co_tuong) {
                        quizList = (data.co_vua.puzzles || []).concat(data.co_tuong.puzzles || []);
                    }
                    if (data.progress) {
                        userProgress = data.progress;
                        capNhatHeaderBadge();
                    }
                    hienThiTheCoMau(data.sample_positions || THE_CO_MAU_FALLBACK);
                    taiCauDo(0);
                    return;
                }
            }
        } catch (e) {
            console.warn("Khong the tai /api/chess, su dung du lieu du phong offline:", e);
        }

        // Fallback offline
        hienThiCoVua(DU_LIEU_CO_VUA_FALLBACK);
        hienThiCoTuong(DU_LIEU_CO_TUONG_FALLBACK);
        quizList = KHO_CAU_DO_FALLBACK;
        hienThiTheCoMau(THE_CO_MAU_FALLBACK);
        taiCauDo(0);
    }

    function capNhatHeaderBadge() {
        const badgeTitle = document.getElementById("chess-badge-title");
        const badgeExp = document.getElementById("chess-badge-exp");
        if (badgeTitle) badgeTitle.innerText = userProgress.danh_hieu || "Ky Thu Tap Su";
        if (badgeExp) badgeExp.innerText = `EXP Co: ${userProgress.tong_diem_exp || 0}`;
    }

    function hienThiCoVua(data) {
        const container = document.getElementById("chess-vua-pieces-grid");
        if (!container) return;

        container.innerHTML = "";
        (data.pieces || []).forEach(p => {
            const card = document.createElement("div");
            card.className = "chess-piece-card";
            card.innerHTML = `
                <div class="chess-piece-badge">${p.ky_hieu}</div>
                <div class="chess-piece-info">
                    <div class="chess-piece-title">${p.ten} <span class="chess-val-pill">${p.diem_gia_tri} diem</span></div>
                    <div class="chess-piece-desc"><strong>Cach di:</strong> ${p.cach_di}</div>
                    <div class="chess-piece-desc"><strong>Cach an:</strong> ${p.cach_an}</div>
                    <div class="chess-piece-note"><strong>Luu y:</strong> ${p.luu_y}</div>
                </div>
            `;
            container.appendChild(card);
        });

        const specialContainer = document.getElementById("chess-vua-special-rules");
        if (specialContainer && data.special_rules) {
            specialContainer.innerHTML = "";
            data.special_rules.forEach(r => {
                const item = document.createElement("div");
                item.className = "chess-rule-item";
                item.innerHTML = `
                    <div class="chess-rule-title">${r.ten}</div>
                    <div class="chess-rule-desc">${r.mo_ta || r.dieu_kien || ""}</div>
                `;
                specialContainer.appendChild(item);
            });
        }
    }

    function hienThiCoTuong(data) {
        const container = document.getElementById("chess-tuong-pieces-grid");
        if (!container) return;

        container.innerHTML = "";
        (data.pieces || []).forEach(p => {
            const card = document.createElement("div");
            card.className = "chess-piece-card xiangqi-card";
            card.innerHTML = `
                <div class="xiangqi-piece-badge">${p.ky_hieu}</div>
                <div class="chess-piece-info">
                    <div class="chess-piece-title">${p.ten}</div>
                    <div class="chess-piece-desc"><strong>Vi tri:</strong> ${p.vi_tri}</div>
                    <div class="chess-piece-desc"><strong>Cach di:</strong> ${p.cach_di}</div>
                    <div class="chess-piece-note xiangqi-note"><strong>Quy tac:</strong> ${p.quy_tac || p.luat_dac_biet || ""}</div>
                </div>
            `;
            container.appendChild(card);
        });

        const tacticsContainer = document.getElementById("chess-tuong-tactics");
        if (tacticsContainer && data.tactics) {
            tacticsContainer.innerHTML = "";
            data.tactics.forEach(t => {
                const item = document.createElement("div");
                item.className = "chess-rule-item xiangqi-rule-item";
                item.innerHTML = `
                    <div class="chess-rule-title xiangqi-title">${t.ten}</div>
                    <div class="chess-rule-desc">${t.mo_ta}</div>
                `;
                tacticsContainer.appendChild(item);
            });
        }
    }

    function hienThiTheCoMau(positions) {
        const select = document.getElementById("chess-select-sample");
        if (!select) return;

        select.innerHTML = "";
        positions.forEach((pos, idx) => {
            const opt = document.createElement("option");
            opt.value = idx;
            opt.textContent = pos.tieu_de;
            select.appendChild(opt);
        });

        select.addEventListener("change", function () {
            const pos = positions[parseInt(this.value, 10)] || positions[0];
            capNhatThongTinTheCo(pos);
        });

        if (positions.length > 0) {
            capNhatThongTinTheCo(positions[0]);
        }
    }

    function capNhatThongTinTheCo(pos) {
        const titleEl = document.getElementById("chess-sample-title");
        const descEl = document.getElementById("chess-sample-desc");
        const moveEl = document.getElementById("chess-sample-move");
        const tipEl = document.getElementById("chess-sample-tip");

        if (titleEl) titleEl.innerText = pos.tieu_de.toUpperCase();
        if (descEl) descEl.innerText = `${pos.mo_ta} (Ben di truoc: ${pos.ben_di_truoc})`;
        if (moveEl) moveEl.innerText = `Nuoc di toi uu: ${pos.nuoc_tiep_theo}`;
        if (tipEl) tipEl.innerText = `Loi khuyen chien luoc: ${pos.loi_khuyen}`;
    }

    function taiCauDo(idx) {
        if (!quizList || quizList.length === 0) return;
        currentQuizIndex = idx % quizList.length;
        const q = quizList[currentQuizIndex];

        const sitEl = document.getElementById("chess-quiz-situation");
        const quesEl = document.getElementById("chess-quiz-question");
        const optsContainer = document.getElementById("chess-quiz-options");
        const resultEl = document.getElementById("chess-quiz-result");

        if (sitEl) sitEl.innerText = `Tinh huong the co: ${q.the_co}`;
        if (quesEl) quesEl.innerText = q.cau_hoi;
        if (resultEl) {
            resultEl.innerText = "Hay chon dap an dung de nhan +30 XP va +15 Coin!";
            resultEl.className = "chess-quiz-feedback default-feedback";
        }

        if (optsContainer) {
            optsContainer.innerHTML = "";
            (q.cac_lua_chon || []).forEach((opt, optIdx) => {
                const optLetter = ["A", "B", "C", "D"][optIdx];
                const btn = document.createElement("button");
                btn.className = "chess-opt-btn";
                btn.innerText = opt;
                btn.onclick = () => kiemTraDapAn(q, optLetter, btn);
                optsContainer.appendChild(btn);
            });
        }
    }

    async function kiemTraDapAn(q, chosenLetter, btnClicked) {
        const allBtns = document.querySelectorAll(".chess-opt-btn");
        allBtns.forEach(b => b.disabled = true);

        const dung = (chosenLetter.trim().toUpperCase() === q.dap_an_dung.trim().toUpperCase());
        const resultEl = document.getElementById("chess-quiz-result");

        if (dung) {
            btnClicked.classList.add("correct-btn");
            userProgress.tong_diem_exp = (userProgress.tong_diem_exp || 0) + 30;
            if (!userProgress.cau_da_giai.includes(q.id)) {
                userProgress.cau_da_giai.push(q.id);
            }
            if (userProgress.cau_da_giai.length >= 8) {
                userProgress.danh_hieu = "Dai Kien Tuong Hoc Duong";
            } else if (userProgress.cau_da_giai.length >= 4) {
                userProgress.danh_hieu = "Kien Tuong Tre Tuoi";
            } else if (userProgress.cau_da_giai.length >= 2) {
                userProgress.danh_hieu = "Ky Thu Nhi Tri Tue";
            }

            if (resultEl) {
                resultEl.innerText = `CHINH XAC! (+30 XP, +15 Coin)\nGiai thich: ${q.giai_thich}`;
                resultEl.className = "chess-quiz-feedback correct-feedback";
            }

            capNhatHeaderBadge();

            // Gui len serverless API
            try {
                fetch("/api/chess", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ action: "solve_puzzle", puzzle_id: q.id, answer: chosenLetter })
                });
            } catch (e) {
                // Ignore network error in background
            }
        } else {
            btnClicked.classList.add("incorrect-btn");
            allBtns.forEach((b, idx) => {
                const optLetter = ["A", "B", "C", "D"][idx];
                if (optLetter === q.dap_an_dung) {
                    b.classList.add("correct-btn");
                }
            });

            if (resultEl) {
                resultEl.innerText = `CHUA CHINH XAC! (Dap an dung la ${q.dap_an_dung})\nGiai thich: ${q.giai_thich}`;
                resultEl.className = "chess-quiz-feedback incorrect-feedback";
            }
        }
    }

    window.switchChessSubTab = function (subId, btn) {
        const panes = document.querySelectorAll('.chess-subtab-pane');
        panes.forEach(p => p.style.display = 'none');
        const target = document.getElementById('chess-subpane-' + subId);
        if (target) target.style.display = 'block';

        if (btn && btn.parentElement) {
            const btns = btn.parentElement.querySelectorAll('.fb-subtab-btn');
            btns.forEach(b => {
                b.classList.remove('active');
                b.style.background = '';
            });
            btn.classList.add('active');
            btn.style.background = 'linear-gradient(135deg, #4F46E5, #3730A3)';
        }
    };

    // Gan su kien khi tai xong trang
    document.addEventListener("DOMContentLoaded", () => {
        napDuLieuCoTriTue();

        const btnNext = document.getElementById("chess-btn-next-quiz");
        if (btnNext) {
            btnNext.addEventListener("click", () => {
                taiCauDo(currentQuizIndex + 1);
            });
        }

        const btnVua = document.getElementById("chess-filter-vua");
        if (btnVua) {
            btnVua.addEventListener("click", () => {
                quizList = KHO_CAU_DO_FALLBACK.filter(q => q.id.startsWith("cv"));
                taiCauDo(0);
            });
        }

        const btnTuong = document.getElementById("chess-filter-tuong");
        if (btnTuong) {
            btnTuong.addEventListener("click", () => {
                quizList = KHO_CAU_DO_FALLBACK.filter(q => q.id.startsWith("ct"));
                taiCauDo(0);
            });
        }

        const btnAll = document.getElementById("chess-filter-all");
        if (btnAll) {
            btnAll.addEventListener("click", () => {
                quizList = KHO_CAU_DO_FALLBACK;
                taiCauDo(0);
            });
        }
    });

})();

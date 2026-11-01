// Thu muc: public/xu_ly_bong_da
// File: bong_da_dinh_cao.js
// Mo ta: Xu ly toan bo giao dien va logic tuong tac Sieu Sao Bong Da va Doi Hinh Trong Mo tren trinh duyet Web Vercel

let fbCurrentSubTab = 'doi_hinh';
let fbSelectedFormation = '4-3-3';
let fbCurrentTeam = null;
let fbPlayersPool = [];
let fbLegendsList = [];
let fbRulesList = [];
let fbScienceList = [];
let fbActiveSlotKey = 'ST';
let fbMatchSim = null;
let fbMatchTimer = null;
let fbMatchSituationIdx = 0;
let fbQuizCurrent = null;

// Cac toa do vi tri tren san co (phan tram top va left)
const fbFormationCoordinates = {
    '4-3-3': {
        'GK': { top: 86, left: 50 },
        'LB': { top: 70, left: 16 },
        'CB1': { top: 72, left: 38 },
        'CB2': { top: 72, left: 62 },
        'RB': { top: 70, left: 84 },
        'CDM': { top: 52, left: 50 },
        'CM': { top: 40, left: 32 },
        'CAM': { top: 38, left: 68 },
        'LW': { top: 18, left: 18 },
        'ST': { top: 14, left: 50 },
        'RW': { top: 18, left: 82 }
    },
    '4-4-2': {
        'GK': { top: 86, left: 50 },
        'LB': { top: 70, left: 16 },
        'CB1': { top: 72, left: 38 },
        'CB2': { top: 72, left: 62 },
        'RB': { top: 70, left: 84 },
        'LM': { top: 46, left: 16 },
        'CM1': { top: 48, left: 38 },
        'CM2': { top: 48, left: 62 },
        'RM': { top: 46, left: 84 },
        'ST1': { top: 16, left: 35 },
        'ST2': { top: 16, left: 65 }
    },
    '3-5-2': {
        'GK': { top: 86, left: 50 },
        'CB1': { top: 72, left: 25 },
        'CB2': { top: 74, left: 50 },
        'CB3': { top: 72, left: 75 },
        'LWB': { top: 48, left: 14 },
        'CDM': { top: 54, left: 50 },
        'CM1': { top: 40, left: 35 },
        'CM2': { top: 40, left: 65 },
        'RWB': { top: 48, left: 86 },
        'ST1': { top: 16, left: 35 },
        'ST2': { top: 16, left: 65 }
    }
};

// Kho cau thu mac dinh neu offline
const fbDefaultPlayers = [
    { id: "cauthu_1", ten: "Thibaut Courtois", vi_tri_chuan: "GK", quoc_tich: "Bi", pac: 60, sho: 30, pas: 75, def: 92, phy: 88, ovr: 90 },
    { id: "cauthu_2", ten: "Alisson Becker", vi_tri_chuan: "GK", quoc_tich: "Brazil", pac: 62, sho: 35, pas: 85, def: 90, phy: 85, ovr: 89 },
    { id: "cauthu_3", ten: "Dang Van Lam", vi_tri_chuan: "GK", quoc_tich: "Viet Nam", pac: 65, sho: 30, pas: 72, def: 85, phy: 86, ovr: 84 },
    { id: "cauthu_4", ten: "Virgil van Dijk", vi_tri_chuan: "CB", quoc_tich: "Ha Lan", pac: 82, sho: 60, pas: 78, def: 95, phy: 92, ovr: 92 },
    { id: "cauthu_5", ten: "Ruben Dias", vi_tri_chuan: "CB", quoc_tich: "Bo Dao Nha", pac: 78, sho: 50, pas: 75, def: 93, phy: 90, ovr: 90 },
    { id: "cauthu_6", ten: "Que Ngoc Hai", vi_tri_chuan: "CB", quoc_tich: "Viet Nam", pac: 74, sho: 58, pas: 76, def: 86, phy: 85, ovr: 84 },
    { id: "cauthu_7", ten: "Alphonso Davies", vi_tri_chuan: "LB", quoc_tich: "Canada", pac: 96, sho: 68, pas: 80, def: 82, phy: 84, ovr: 87 },
    { id: "cauthu_8", ten: "Doan Van Hau", vi_tri_chuan: "LB", quoc_tich: "Viet Nam", pac: 82, sho: 70, pas: 75, def: 84, phy: 87, ovr: 84 },
    { id: "cauthu_9", ten: "Achraf Hakimi", vi_tri_chuan: "RB", quoc_tich: "Maroc", pac: 95, sho: 76, pas: 82, def: 81, phy: 83, ovr: 88 },
    { id: "cauthu_10", ten: "Vu Van Thanh", vi_tri_chuan: "RB", quoc_tich: "Viet Nam", pac: 84, sho: 72, pas: 78, def: 82, phy: 84, ovr: 83 },
    { id: "cauthu_11", ten: "Rodri Hernandez", vi_tri_chuan: "CDM", quoc_tich: "Tay Ban Nha", pac: 76, sho: 80, pas: 90, def: 92, phy: 90, ovr: 93 },
    { id: "cauthu_12", ten: "Kevin De Bruyne", vi_tri_chuan: "CAM", quoc_tich: "Bi", pac: 78, sho: 88, pas: 96, def: 68, phy: 79, ovr: 92 },
    { id: "cauthu_13", ten: "Luka Modric", vi_tri_chuan: "CM", quoc_tich: "Croatia", pac: 75, sho: 82, pas: 93, def: 74, phy: 76, ovr: 90 },
    { id: "cauthu_14", ten: "Jude Bellingham", vi_tri_chuan: "CAM", quoc_tich: "Anh", pac: 85, sho: 88, pas: 86, def: 80, phy: 87, ovr: 91 },
    { id: "cauthu_15", ten: "Nguyen Quang Hai", vi_tri_chuan: "CAM", quoc_tich: "Viet Nam", pac: 80, sho: 84, pas: 88, def: 65, phy: 74, ovr: 85 },
    { id: "cauthu_16", ten: "Nguyen Hoang Duc", vi_tri_chuan: "CM", quoc_tich: "Viet Nam", pac: 81, sho: 80, pas: 86, def: 78, phy: 82, ovr: 85 },
    { id: "cauthu_17", ten: "Cristiano Ronaldo", vi_tri_chuan: "ST", quoc_tich: "Bo Dao Nha", pac: 86, sho: 94, pas: 82, def: 40, phy: 88, ovr: 93 },
    { id: "cauthu_18", ten: "Lionel Messi", vi_tri_chuan: "RW", quoc_tich: "Argentina", pac: 84, sho: 92, pas: 95, def: 38, phy: 72, ovr: 93 },
    { id: "cauthu_19", ten: "Kylian Mbappe", vi_tri_chuan: "LW", quoc_tich: "Phap", pac: 97, sho: 92, pas: 84, def: 42, phy: 80, ovr: 93 },
    { id: "cauthu_20", ten: "Erling Haaland", vi_tri_chuan: "ST", quoc_tich: "Na Uy", pac: 91, sho: 95, pas: 70, def: 48, phy: 92, ovr: 92 },
    { id: "cauthu_21", ten: "Vinicius Junior", vi_tri_chuan: "LW", quoc_tich: "Brazil", pac: 96, sho: 86, pas: 82, def: 35, phy: 74, ovr: 90 },
    { id: "cauthu_22", ten: "Nguyen Tien Linh", vi_tri_chuan: "ST", quoc_tich: "Viet Nam", pac: 81, sho: 85, pas: 72, def: 44, phy: 83, ovr: 84 },
    { id: "cauthu_23", ten: "Huynh Nhu", vi_tri_chuan: "ST", quoc_tich: "Viet Nam", pac: 83, sho: 86, pas: 80, def: 46, phy: 78, ovr: 85 }
];

async function initFootballHub() {
    try {
        const res = await fetch('/api/football');
        const data = await res.json();
        if (data.status === 'success') {
            fbPlayersPool = data.players || fbDefaultPlayers;
            fbLegendsList = data.legends || [];
            fbRulesList = data.rules || [];
            fbScienceList = data.science || [];
            fbCurrentTeam = data.current_team || getFbLocalTeam();
        }
    } catch (err) {
        console.warn("Football API fetch fallback to local:", err);
        fbPlayersPool = fbDefaultPlayers;
        fbCurrentTeam = getFbLocalTeam();
    }

    if (!fbCurrentTeam) {
        fbCurrentTeam = {
            so_do: "4-3-3",
            ten_doi_bong: "Dream Team EduVerse",
            danh_sach_da_chinh: {
                "GK": "cauthu_1", "LB": "cauthu_7", "CB1": "cauthu_4", "CB2": "cauthu_5",
                "RB": "cauthu_9", "CDM": "cauthu_11", "CM": "cauthu_13", "CAM": "cauthu_15",
                "LW": "cauthu_19", "ST": "cauthu_17", "RW": "cauthu_18"
            }
        };
    }

    fbSelectedFormation = fbCurrentTeam.so_do || '4-3-3';
    renderFootballPitch();
    renderFootballLegends();
    renderFootballRulesAndScience();
    renderFootballOpponents();
}

function getFbLocalTeam() {
    const raw = localStorage.getItem('eduverse_fb_team');
    if (raw) {
        try { return JSON.parse(raw); } catch (e) {}
    }
    return null;
}

function saveFbLocalTeam(team) {
    localStorage.setItem('eduverse_fb_team', JSON.stringify(team));
}

function switchFootballSubTab(tabKey, btnEl) {
    fbCurrentSubTab = tabKey;
    document.querySelectorAll('.fb-subtab-btn').forEach(b => b.classList.remove('active'));
    if (btnEl) btnEl.classList.add('active');

    document.querySelectorAll('.fb-subtab-pane').forEach(p => p.style.display = 'none');
    const target = document.getElementById('fb-subpane-' + tabKey);
    if (target) target.style.display = 'block';

    try { playClickSfx(); } catch (e) {}

    if (tabKey === 'doi_hinh') renderFootballPitch();
    if (tabKey === 'huyen_thoai') renderFootballLegends();
    if (tabKey === 'luat_fifa') renderFootballRulesAndScience();
}

function onFbFormationChange(newFormation) {
    fbSelectedFormation = newFormation;
    fbCurrentTeam.so_do = newFormation;
    renderFootballPitch();
    try { playClickSfx(); } catch (e) {}
}

function renderFootballPitch() {
    const pitch = document.getElementById('fbPitchContainer');
    if (!pitch) return;

    const coords = fbFormationCoordinates[fbSelectedFormation] || fbFormationCoordinates['4-3-3'];
    const daChinh = fbCurrentTeam.danh_sach_da_chinh || {};
    const playersDict = {};
    fbPlayersPool.forEach(p => { playersDict[p.id] = p; });

    let pitchHtml = `
        <div class="fb-pitch-field">
            <div class="fb-pitch-center-circle"></div>
            <div class="fb-pitch-half-line"></div>
            <div class="fb-pitch-penalty-box-top"></div>
            <div class="fb-pitch-penalty-box-bottom"></div>
    `;

    let totalOvr = 0;
    let count = 0;

    for (const [posKey, coord] of Object.entries(coords)) {
        let pId = daChinh[posKey];
        if (!pId) {
            // Chon cau thu phu hop vi tri
            const candidate = fbPlayersPool.find(p => p.vi_tri_chuan === posKey.replace(/[0-9]/g, '')) || fbPlayersPool[count % fbPlayersPool.length];
            pId = candidate.id;
            daChinh[posKey] = pId;
        }

        const p = playersDict[pId] || fbPlayersPool[0];
        totalOvr += (p.ovr || 85);
        count++;

        pitchHtml += `
            <div class="fb-player-slot" style="top: ${coord.top}%; left: ${coord.left}%;" onclick="openFbPlayerPicker('${posKey}')" title="Bấm để thay thế cầu thủ">
                <div class="fb-player-badge">${posKey}</div>
                <div class="fb-player-card-mini">
                    <div class="fb-player-ovr">${p.ovr}</div>
                    <div class="fb-player-name">${p.ten}</div>
                    <div class="fb-player-sub">${p.quoc_tich}</div>
                </div>
            </div>
        `;
    }

    pitchHtml += `</div>`;
    pitch.innerHTML = pitchHtml;

    const avgOvr = count > 0 ? (totalOvr / count).toFixed(1) : '90.0';
    const ovrBadge = document.getElementById('fbTeamOvrBadge');
    if (ovrBadge) {
        ovrBadge.innerText = `Sức Mạnh Toàn Đội: ${avgOvr} OVR`;
    }
}

function openFbPlayerPicker(slotKey) {
    fbActiveSlotKey = slotKey;
    const modal = document.getElementById('fbPlayerPickerModal');
    const slotTitle = document.getElementById('fbPickerSlotTitle');
    const grid = document.getElementById('fbPickerPlayerGrid');
    if (!modal || !grid) return;

    if (slotTitle) {
        slotTitle.innerText = `Chọn Cầu Thủ Cho Vị Trí: ${slotKey}`;
    }

    grid.innerHTML = '';
    const cleanPos = slotKey.replace(/[0-9]/g, '');

    // Sap xep cau thu phu hop vi tri len dau
    const sorted = [...fbPlayersPool].sort((a, b) => {
        const matchA = a.vi_tri_chuan === cleanPos ? 1 : 0;
        const matchB = b.vi_tri_chuan === cleanPos ? 1 : 0;
        return matchB - matchA;
    });

    sorted.forEach(p => {
        const card = document.createElement('div');
        card.className = 'fb-picker-card';
        card.innerHTML = `
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <span style="font-weight: 900; color: #F59E0B; font-size: 16px;">${p.ovr} OVR</span>
                <span style="background: rgba(16, 185, 129, 0.2); color: #10B981; padding: 2px 8px; border-radius: 6px; font-weight: bold; font-size: 12px;">${p.vi_tri_chuan}</span>
            </div>
            <div style="font-weight: 800; font-size: 15px; color: #FFFFFF; margin-bottom: 4px;">${p.ten}</div>
            <div style="font-size: 12px; color: #94A3B8; margin-bottom: 8px;">Quốc tịch: ${p.quoc_tich}</div>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 4px; font-size: 11px; text-align: center; background: rgba(0,0,0,0.3); padding: 4px; border-radius: 6px;">
                <div><span style="color:#94A3B8;">PAC:</span> <b>${p.pac}</b></div>
                <div><span style="color:#94A3B8;">SHO:</span> <b>${p.sho}</b></div>
                <div><span style="color:#94A3B8;">PAS:</span> <b>${p.pas}</b></div>
                <div><span style="color:#94A3B8;">DEF:</span> <b>${p.def}</b></div>
                <div><span style="color:#94A3B8;">PHY:</span> <b>${p.phy}</b></div>
                <div><span style="color:#00FFCC;">OVR:</span> <b>${p.ovr}</b></div>
            </div>
        `;
        card.onclick = () => {
            selectFbPlayerForSlot(p.id);
        };
        grid.appendChild(card);
    });

    modal.style.display = 'flex';
}

function selectFbPlayerForSlot(playerId) {
    if (!fbCurrentTeam.danh_sach_da_chinh) fbCurrentTeam.danh_sach_da_chinh = {};
    fbCurrentTeam.danh_sach_da_chinh[fbActiveSlotKey] = playerId;
    closeFbPlayerPicker();
    renderFootballPitch();
    try { playClickSfx(); } catch (e) {}
}

function closeFbPlayerPicker() {
    const modal = document.getElementById('fbPlayerPickerModal');
    if (modal) modal.style.display = 'none';
}

async function saveFbDreamTeam() {
    saveFbLocalTeam(fbCurrentTeam);
    try {
        await fetch('/api/football', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ action: 'save_team', team: fbCurrentTeam })
        });
    } catch (e) {}

    alert("XÁC NHẬN: Đã lưu Đội Hình Trong Mơ 11 Siêu Sao thành công vào hệ thống!");
}

// --- MO PHONG TRAN DAU 90 PHUT ---
function renderFootballOpponents() {
    const sel = document.getElementById('fbSelectOpponent');
    if (!sel) return;
    sel.innerHTML = `
        <option value="opp_allstars">Siêu Sao Thế Giới All-Stars (Sức mạnh 94)</option>
        <option value="opp_europe">Liên Quân Châu Âu UEFA Legends (Sức mạnh 92)</option>
        <option value="opp_vietnam">Thế Hệ Vàng Việt Nam All-Stars (Sức mạnh 89)</option>
    `;
}

async function startFbMatchSimulation() {
    const oppSel = document.getElementById('fbSelectOpponent');
    const oppId = oppSel ? oppSel.value : 'opp_allstars';

    try {
        const res = await fetch('/api/football', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ action: 'start_match', opponent_id: oppId })
        });
        const d = await res.json();
        if (d.status === 'success' && d.match) {
            fbMatchSim = d.match;
        }
    } catch (e) {
        console.warn("Fallback local match:", e);
    }

    if (!fbMatchSim) {
        fbMatchSim = {
            doi_thu: { ten: "Siêu Sao Thế Giới All-Stars", suc_manh: 94 },
            ti_so_nha: 0,
            ti_so_khach: 0,
            tinh_huong_list: [
                {
                    phut: 18,
                    tieu_de: "Đột phá cánh và chuyền bóng xoáy xuyên tuyến",
                    mo_ta_tinh_huong: "Tiền đạo cánh đang dẫn bóng tốc độ bên cánh trái, đối mặt 2 hậu vệ đối phương. Em hãy chỉ đạo cách xử lý chính xác:",
                    cau_hoi: "Để quả bóng đi cuộn xoáy hình cánh cung ra sau lưng hậu vệ, cầu thủ cần tiếp xúc vào phần nào của trái bóng?",
                    cac_lua_chon: [
                        { phuong_an: "Sút bằng má trong mu bàn chân tạo hiệu ứng Magnus", dung: true },
                        { phuong_an: "Sút bằng mũi giày trực diện thẳng", dung: false },
                        { phuong_an: "Sút bằng gót chân từ dưới lên", dung: false }
                    ],
                    binh_luan_dung: "VÀOOOO! Đường bóng xoáy Magnus mẫu mực, tiền đạo băng vào đệm bóng cận thành tung lưới mở tỉ số!",
                    binh_luan_sai: "Rất tiếc! Cú tiếp xúc bóng không chuẩn khiến bóng đi nhẹ và thủ môn bắt gọn."
                },
                {
                    phut: 36,
                    tieu_de: "Đá phạt trực tiếp cự ly 22 mét trước vòng cấm",
                    mo_ta_tinh_huong: "Đội nhà được hưởng quả sút phạt trực tiếp nguy hiểm ngay trước vòng 16m50.",
                    cau_hoi: "Khoảng cách quy định tối thiểu từ quả bóng đến hàng rào đối phương theo luật FIFA là bao nhiêu mét?",
                    cac_lua_chon: [
                        { phuong_an: "9.15 mét (tương đương 10 yards)", dung: true },
                        { phuong_an: "5.5 mét", dung: false },
                        { phuong_an: "11 mét", dung: false }
                    ],
                    binh_luan_dung: "SIUUUU! Cú sút phạt kiểu lá vàng rơi Knuckleball cắm thẳng vào góc chữ A không thể cản phá!",
                    binh_luan_sai: "Bóng chạm đúng đầu hàng rào chắn và đi chệch cột dọc ra ngoài."
                },
                {
                    phut: 55,
                    tieu_de: "Phản công siêu tốc 3 đánh 2",
                    mo_ta_tinh_huong: "Cắt được bóng từ giữa sân, đội nhà mở đợt phản công chớp nhoáng với 3 tiền đạo.",
                    cau_hoi: "Nếu bóng bay với vận tốc 90 km/h (25 m/s) qua quãng đường 50m, thời gian bóng đến chân tiền đạo là bao nhiêu?",
                    cac_lua_chon: [
                        { phuong_an: "2 giây (t = s / v = 50 / 25 = 2s)", dung: true },
                        { phuong_an: "4 giây", dung: false },
                        { phuong_an: "1 giây", dung: false }
                    ],
                    binh_luan_dung: "TUYỆT VỜI! Đường chuyền vượt tuyến chuẩn xác từng mi-li-mét, tiền đạo tung cú sút chéo góc nhân đôi cách biệt!",
                    binh_luan_sai: "Tiền đạo di chuyển quá sớm trước đường chuyền nên bị trọng tài thổi phạt việt vị."
                },
                {
                    phut: 74,
                    tieu_de: "Cản phá pha đối mặt nguy hiểm của đối phương",
                    mo_ta_tinh_huong: "Đối thủ phản công sắc lẹm, tiền đạo đối mặt trực diện với thủ môn đội nhà trong vòng cấm.",
                    cau_hoi: "Để thu hẹp góc sút của tiền đạo đối phương hiệu quả nhất, thủ môn cần thực hiện động tác nào?",
                    cac_lua_chon: [
                        { phuong_an: "Chủ động lao ra rút ngắn cự ly và giang rộng hai tay hạ thấp trọng tâm", dung: true },
                        { phuong_an: "Đứng yên trên vạch vôi cầu môn chờ đợi", dung: false },
                        { phuong_an: "Nhảy sang một góc trước", dung: false }
                    ],
                    binh_luan_dung: "CẢN PHÁ XUẤT THẦN! Thủ môn băng ra cực nhanh khép chặt góc sút khiến cú dứt điểm bật ra ngoài đường biên!",
                    binh_luan_sai: "Tiền đạo đối phương đã bấm bóng tinh tế qua người rút ngắn tỉ số trận đấu."
                },
                {
                    phut: 90,
                    tieu_de: "Cú sút phạt đền Penalty quyết định trận đấu",
                    mo_ta_tinh_huong: "Phút 90+2 bù giờ cuối cùng, đội nhà được hưởng quả phạt đền Penalty từ cự ly 11 mét.",
                    cau_hoi: "Theo luật FIFA, khi thực hiện quả phạt đền Penalty, thủ môn bắt buộc phải giữ vị trí nào trước khi bóng lăn?",
                    cac_lua_chon: [
                        { phuong_an: "Ít nhất một phần của bàn chân phải chạm hoặc ở trên vạch vôi cầu môn", dung: true },
                        { phuong_an: "Được tự do bước lên phía trước 2 mét", dung: false },
                        { phuong_an: "Phải ngồi xổm xuống sân", dung: false }
                    ],
                    binh_luan_dung: "BÀN THẮNG QUYẾT ĐỊNH! Cú sút lừa thủ môn đánh lừa góc cản phá, ấn định chiến thắng vang dội cho đội nhà!",
                    binh_luan_sai: "Cú sút đi vọt xà ngang trong sự tiếc nuối của người hâm mộ."
                }
            ]
        };
    }

    fbMatchSituationIdx = 0;
    document.getElementById('fbMatchBoard').style.display = 'block';
    renderFbMatchSituation();
}

function renderFbMatchSituation() {
    if (!fbMatchSim) return;
    const sim = fbMatchSim;
    const list = sim.tinh_huong_list || [];

    document.getElementById('fbScoreDreamTeam').innerText = sim.ti_so_nha;
    document.getElementById('fbScoreOpponent').innerText = sim.ti_so_khach;
    document.getElementById('fbOpponentName').innerText = sim.doi_thu.ten;

    if (fbMatchSituationIdx >= list.length) {
        // Ket thuc 90 phut
        document.getElementById('fbMatchClock').innerText = "Phút: 90' HẾT GIỜ";
        document.getElementById('fbSitTitle').innerText = "TRẬN ĐẤU KẾT THÚC";
        document.getElementById('fbSitDesc').innerText = `Tỉ số chung cuộc: Dream Team ${sim.ti_so_nha} - ${sim.ti_so_khach} ${sim.doi_thu.ten}.`;
        document.getElementById('fbSitQuestion').innerText = "";
        document.getElementById('fbSitOptions').innerHTML = `
            <button class="btn-primary" style="margin-top: 15px; padding: 12px 24px;" onclick="startFbMatchSimulation()">Thi Đấu Trận Mới</button>
        `;

        if (sim.ti_so_nha > sim.ti_so_khach) {
            alert(`CHIẾN THẮNG!\n\nXuất sắc! Dream Team của em đã đánh bại ${sim.doi_thu.ten} với tỉ số ${sim.ti_so_nha} - ${sim.ti_so_khach}!\nThưởng +100 XP học tập!`);
            try { congDiemThuongWeb(100); } catch (e) {}
        } else if (sim.ti_so_nha === sim.ti_so_khach) {
            alert(`HÒA KỊCH TÍNH!\n\nTrận hòa nghẹt thở ${sim.ti_so_nha} - ${sim.ti_so_khach}! Thưởng +50 XP!`);
            try { congDiemThuongWeb(50); } catch (e) {}
        } else {
            alert(`THẤT BẠI SÁT NÚT!\n\nĐội bạn đã thi đấu kiên cường! Hãy rèn luyện thêm chiến thuật nhé! Thưởng +20 XP!`);
            try { congDiemThuongWeb(20); } catch (e) {}
        }
        return;
    }

    const sit = list[fbMatchSituationIdx];
    document.getElementById('fbMatchClock').innerText = `Phút: ${sit.phut}'`;
    document.getElementById('fbSitTitle').innerText = `Phút ${sit.phut}: ${sit.tieu_de}`;
    document.getElementById('fbSitDesc').innerText = sit.mo_ta_tinh_huong;
    document.getElementById('fbSitQuestion').innerText = `Thử thách chiến thuật: ${sit.cau_hoi}`;

    const optsContainer = document.getElementById('fbSitOptions');
    optsContainer.innerHTML = '';

    sit.cac_lua_chon.forEach((opt, idx) => {
        const btn = document.createElement('button');
        btn.className = 'fb-sit-btn';
        const letters = ['A', 'B', 'C'];
        btn.innerHTML = `<span style="background: #10B981; color: #022C22; font-weight: 900; padding: 4px 10px; border-radius: 8px; margin-right: 10px;">${letters[idx]}</span> <span>${opt.phuong_an}</span>`;
        btn.onclick = () => {
            handleFbSituationChoice(opt, sit);
        };
        optsContainer.appendChild(btn);
    });
}

function handleFbSituationChoice(opt, sit) {
    try { playClickSfx(); } catch (e) {}
    const isCorrect = opt.dung;
    const sim = fbMatchSim;

    if (isCorrect) {
        sim.ti_so_nha++;
        document.getElementById('fbCommentaryBox').innerText = `Bình luận viên: ${sit.binh_luan_dung}`;
        document.getElementById('fbCommentaryBox').style.color = '#10B981';
    } else {
        if (Math.random() < 0.6) sim.ti_so_khach++;
        document.getElementById('fbCommentaryBox').innerText = `Bình luận viên: ${sit.binh_luan_sai}`;
        document.getElementById('fbCommentaryBox').style.color = '#EF4444';
    }

    fbMatchSituationIdx++;
    renderFbMatchSituation();
}

// --- BACH KHOA HUYEN THOAI & TRI THUC BONG DA ---
function renderFootballLegends() {
    const listEl = document.getElementById('fbLegendsGrid');
    if (!listEl) return;

    listEl.innerHTML = '';
    const legends = fbLegendsList.length > 0 ? fbLegendsList : [
        { id: "cr7", ten: "Cristiano Ronaldo", biet_danh: "CR7", quoc_tich: "Bồ Đào Nha", vi_tri: "Tiền đạo", so_ao: 7, cau_lac_bo: "Real Madrid, Man United, Al Nassr", ky_luc: "Hơn 900 bàn thắng chính thức, 5 Quả Bóng Vàng", loi_khuyen: "Thành công không phải sự ngẫu nhiên, đó là kỷ luật và ý chí phi thường." },
        { id: "messi", ten: "Lionel Messi", biet_danh: "El Pulga", quoc_tich: "Argentina", vi_tri: "Tiền đạo", so_ao: 10, cau_lac_bo: "Barcelona, Inter Miami", ky_luc: "8 Quả Bóng Vàng, Vô địch World Cup 2022", loi_khuyen: "Hãy luôn kiên trì ngay cả khi xuất phát điểm có nhiều khó khăn." },
        { id: "pele", ten: "Pele", biet_danh: "Vua Bóng Đá", quoc_tich: "Brazil", vi_tri: "Tiền đạo", so_ao: 10, cau_lac_bo: "Santos FC", ky_luc: "3 lần Vô địch World Cup lịch sử", loi_khuyen: "Bóng đá là bài học về sự gắn kết đồng đội và tình yêu thương." },
        { id: "maradona", ten: "Diego Maradona", biet_danh: "Cậu Bé Vàng", quoc_tich: "Argentina", vi_tri: "Tiền vệ tấn công", so_ao: 10, cau_lac_bo: "Napoli, Boca Juniors", ky_luc: "Bàn thắng thế kỷ qua 5 cầu thủ tại World Cup 1986", loi_khuyen: "Đam mê mãnh liệt có thể làm nên những điều kỳ diệu." },
        { id: "mbappe", ten: "Kylian Mbappe", biet_danh: "Ninja Rùa", quoc_tich: "Pháp", vi_tri: "Tiền đạo", so_ao: 9, cau_lac_bo: "Real Madrid, PSG", ky_luc: "Hat-trick chung kết World Cup 2022", loi_khuyen: "Tuổi trẻ hãy dám ước mơ lớn và bứt phá giới hạn bản thân." },
        { id: "haaland", ten: "Erling Haaland", biet_danh: "Cỗ Máy Ghi Bàn", quoc_tich: "Na Uy", vi_tri: "Tiền đạo cắm", so_ao: 9, cau_lac_bo: "Man City, Dortmund", ky_luc: "Kỷ lục 36 bàn thắng trong 1 mùa giải Ngoại Hạng Anh", loi_khuyen: "Tập trung tối đa vào từng cơ hội nhỏ mỗi ngày." },
        { id: "modric", ten: "Luka Modric", biet_danh: "Nhạc Trưởng", quoc_tich: "Croatia", vi_tri: "Tiền vệ trung tâm", so_ao: 10, cau_lac_bo: "Real Madrid", ky_luc: "Quả Bóng Vàng 2018, Á quân World Cup", loi_khuyen: "Sự thông minh chiến thuật và lòng quả cảm vượt trên mọi thể hình." },
        { id: "quanghai", ten: "Nguyễn Quang Hải", biet_danh: "Hải Con", quoc_tich: "Việt Nam", vi_tri: "Tiền vệ tấn công", so_ao: 19, cau_lac_bo: "Công An Hà Nội, Hà Nội FC", ky_luc: "Siêu phẩm Cầu vồng trong tuyết Thường Châu 2018", loi_khuyen: "Tự hào màu cờ sắc áo Việt Nam và luôn vươn tầm châu lục." },
        { id: "huynhnhu", ten: "Huỳnh Như", biet_danh: "Nụ Cười Vàng", quoc_tich: "Việt Nam", vi_tri: "Tiền đạo", so_ao: 9, cau_lac_bo: "Lank FC, TP Hồ Chí Minh", ky_luc: "5 Quả Bóng Vàng nữ Việt Nam, World Cup 2023", loi_khuyen: "Con gái cũng có thể chơi bóng xuất chúng và tự tin bước ra thế giới." }
    ];

    legends.forEach(lg => {
        const item = document.createElement('div');
        item.className = 'fb-legend-card';
        item.innerHTML = `
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <h4 style="font-size: 18px; color: #F59E0B; font-weight: 900;">${lg.ten}</h4>
                <span style="background: rgba(6, 182, 212, 0.2); color: #06B6D4; padding: 3px 10px; border-radius: 8px; font-weight: bold; font-size: 13px;">#${lg.so_ao} - ${lg.quoc_tich}</span>
            </div>
            <p style="font-size: 13.5px; color: #E2E8F0; margin-bottom: 6px;"><b>Biệt danh:</b> ${lg.biet_danh} | <b>Vị trí:</b> ${lg.vi_tri}</p>
            <p style="font-size: 13px; color: #94A3B8; margin-bottom: 6px;"><b>CLB:</b> ${lg.cau_lac_bo}</p>
            <p style="font-size: 13.5px; color: #10B981; margin-bottom: 8px; line-height: 1.5;"><b>Kỷ lục:</b> ${lg.ky_luc}</p>
            <div style="background: rgba(2, 44, 34, 0.7); border-left: 3px solid #F59E0B; padding: 8px 12px; border-radius: 6px; font-style: italic; font-size: 13px; color: #CBD5E1;">
                "${lg.loi_khuyen}"
            </div>
        `;
        listEl.appendChild(item);
    });
}

async function loadFootballQuiz() {
    try {
        const res = await fetch('/api/football', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ action: 'quiz' })
        });
        const d = await res.json();
        if (d.status === 'success' && d.quiz) {
            fbQuizCurrent = d.quiz;
        }
    } catch (e) {}

    if (!fbQuizCurrent) {
        fbQuizCurrent = {
            cau_hoi: "Cầu thủ nào trong lịch sử bóng đá thế giới đã giành được 8 Quả Bóng Vàng danh giá?",
            dap_an: ["Lionel Messi", "Cristiano Ronaldo", "Pele", "Zinedine Zidane"],
            dap_an_dung: "Lionel Messi",
            giai_thich: "Lionel Messi lập kỷ lục vô tiền khoáng hậu với 8 Quả Bóng Vàng sau chức vô địch World Cup 2022."
        };
    }

    document.getElementById('fbQuizQuestion').innerText = fbQuizCurrent.cau_hoi;
    document.getElementById('fbQuizResult').innerText = "";

    const container = document.getElementById('fbQuizOptions');
    container.innerHTML = '';

    fbQuizCurrent.dap_an.forEach((opt, idx) => {
        const btn = document.createElement('button');
        btn.className = 'fb-sit-btn';
        const letters = ['A', 'B', 'C', 'D'];
        btn.innerHTML = `<span style="background: #06B6D4; color: #022C22; font-weight: 900; padding: 4px 10px; border-radius: 8px; margin-right: 10px;">${letters[idx]}</span> <span>${opt}</span>`;
        btn.onclick = () => {
            const isCorrect = (opt === fbQuizCurrent.dap_an_dung);
            const resEl = document.getElementById('fbQuizResult');
            if (isCorrect) {
                resEl.innerText = `CHÍNH XÁC! Thưởng +30 XP! Giải thích: ${fbQuizCurrent.giai_thich}`;
                resEl.style.color = '#10B981';
                try { congDiemThuongWeb(30); } catch (e) {}
            } else {
                resEl.innerText = `CHƯA CHÍNH XÁC! Đáp án đúng là: ${fbQuizCurrent.dap_an_dung}. Giải thích: ${fbQuizCurrent.giai_thich}`;
                resEl.style.color = '#EF4444';
            }
        };
        container.appendChild(btn);
    });
}

// --- CAM NANG LUAT FIFA & KHOA HOC BONG DA ---
function renderFootballRulesAndScience() {
    const rulesContainer = document.getElementById('fbRulesContainer');
    const scienceContainer = document.getElementById('fbScienceContainer');
    if (!rulesContainer || !scienceContainer) return;

    rulesContainer.innerHTML = '';
    const rules = fbRulesList.length > 0 ? fbRulesList : [
        { ten_luat: "Luật Việt Vị (Offside)", tom_tat: "Cầu thủ ở vị trí việt vị nếu đứng gần đường biên ngang đối phương hơn cả bóng và cầu thủ phòng ngự cuối cùng thứ hai (sau thủ môn) khi đồng đội chuyền bóng.", luu_y_de_nho: "Không bị việt vị khi nhận bóng từ Ném biên, Phạt góc hoặc Phát bóng cầu môn." },
        { ten_luat: "Luật Phạt Đền (Penalty)", tom_tat: "Áp dụng khi cầu thủ phòng ngự phạm lỗi trực tiếp trong khu vực 16m50 của đội mình. Cú sút thực hiện từ chấm 11 mét.", luu_y_de_nho: "Thủ môn phải giữ ít nhất 1 chân trên vạch vôi khi bóng được đá." },
        { ten_luat: "Luật Thẻ Vàng và Thẻ Đỏ", tom_tat: "Thẻ vàng cảnh cáo lỗi nguy hiểm hoặc phi thể thao. Nhận 2 thẻ vàng trong 1 trận tương đương 1 thẻ đỏ, cầu thủ phải rời sân ngay lập tức.", luu_y_de_nho: "Đội bị thẻ đỏ không được thay thế cầu thủ và phải thi đấu thiếu người." },
        { ten_luat: "Công Nghệ Trọng Tài Video VAR", tom_tat: "Hệ thống camera siêu chậm và vạch kẻ 3D hỗ trợ trọng tài chính trong 4 trường hợp: Bàn thắng, Phạt đền, Thẻ đỏ trực tiếp và Nhận diện sai cầu thủ.", luu_y_de_nho: "Trọng tài chính trên sân luôn là người đưa ra quyết định cuối cùng." }
    ];

    rules.forEach(r => {
        const box = document.createElement('div');
        box.className = 'fb-rule-box';
        box.innerHTML = `
            <h4 style="color: #06B6D4; font-size: 17px; margin-bottom: 8px; font-weight: 900;">${r.ten_luat}</h4>
            <p style="color: #E2E8F0; font-size: 13.5px; line-height: 1.6; margin-bottom: 8px;">${r.tom_tat}</p>
            <div style="background: rgba(6, 182, 212, 0.15); border-left: 3px solid #06B6D4; padding: 6px 10px; border-radius: 6px; color: #CBD5E1; font-size: 12.5px;">
                <b>Lưu ý quan trọng:</b> ${r.luu_y_de_nho}
            </div>
        `;
        rulesContainer.appendChild(box);
    });

    scienceContainer.innerHTML = '';
    const science = fbScienceList.length > 0 ? fbScienceList : [
        { chu_de: "Hiệu Ứng Xoáy Magnus (Vật Lý 8)", khoa_hoc: "Khi quả bóng xoay tròn trong không khí, vận tốc dòng khí một bên nhanh hơn bên kia tạo chênh lệch áp suất, sinh ra lực Magnus đẩy bóng bay theo quỹ đạo hình quả chuối uốn lượn qua hàng rào.", mon_hoc: "Vật Lý 8 (Áp suất chất lưu)" },
        { chu_de: "Vận Tốc Sút Bóng v = s / t (Vật Lý 7)", khoa_hoc: "Một cú sút 108 km/h đổi ra bằng 30 m/s. Ở cự ly 20 mét, bóng bay vào lưới chỉ mất 0.66 giây, nhanh hơn tốc độ phản xạ của mắt người (0.2s - 0.3s).", mon_hoc: "Toán & Vật Lý 7 (Vận tốc chuyển động)" },
        { chu_de: "Tỉ Lệ Kiểm Soát Bóng & Xác Suất xG (Toán 7 & 8)", khoa_hoc: "Tỉ lệ kiểm soát bóng = (Thời gian có bóng / Tổng thời gian thi đấu) x 100%. Chỉ số xG đo lường xác suất thành bàn từ 0 đến 1 dựa vào góc sút và khoảng cách.", mon_hoc: "Toán 7 & 8 (Tỉ số phần trăm và Thống kê)" },
        { chu_de: "Góc Sút Tối Ưu (Hình Học 7)", khoa_hoc: "Càng tiến vào trung lộ đối diện cầu môn, góc sút mở rộng tối đa trên 35 độ. Khi chạy sát đường biên ngang, góc sút bị thu hẹp thành góc nhọn rất nhỏ khó ghi bàn.", mon_hoc: "Hình Học 7 (Góc trong tam giác)" }
    ];

    science.forEach(s => {
        const box = document.createElement('div');
        box.className = 'fb-rule-box';
        box.style.border = '1.5px solid #10B981';
        box.innerHTML = `
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <h4 style="color: #10B981; font-size: 17px; font-weight: 900;">${s.chu_de}</h4>
                <span style="background: rgba(16, 185, 129, 0.2); color: #6EE7B7; padding: 2px 8px; border-radius: 6px; font-size: 12px; font-weight: bold;">${s.mon_hoc}</span>
            </div>
            <p style="color: #E2E8F0; font-size: 13.5px; line-height: 1.6;">${s.khoa_hoc}</p>
        `;
        scienceContainer.appendChild(box);
    });
}

function congDiemThuongWeb(xp) {
    if (typeof userXp !== 'undefined') {
        userXp += xp;
        const xpEl = document.getElementById('userXpVal');
        if (xpEl) xpEl.innerText = userXp;
        localStorage.setItem('eduverse_user_xp', userXp.toString());
    }
}

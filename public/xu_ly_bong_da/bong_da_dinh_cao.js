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
let fbSkillsHealthList = [];
let fbActiveSlotKey = 'ST';
let fbMatchSim = null;
let fbMatchTimer = null;
let fbMatchSituationIdx = 0;
let fbQuizCurrent = null;

// Cac toa do vi tri tren san co (phan tram top va left) cho 6 so do chien thuat
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
    },
    '4-2-3-1': {
        'GK': { top: 86, left: 50 },
        'LB': { top: 70, left: 16 },
        'CB1': { top: 72, left: 38 },
        'CB2': { top: 72, left: 62 },
        'RB': { top: 70, left: 84 },
        'CDM1': { top: 54, left: 36 },
        'CDM2': { top: 54, left: 64 },
        'LM': { top: 32, left: 18 },
        'CAM': { top: 34, left: 50 },
        'RM': { top: 32, left: 82 },
        'ST': { top: 14, left: 50 }
    },
    '5-3-2': {
        'GK': { top: 86, left: 50 },
        'LWB': { top: 62, left: 14 },
        'CB1': { top: 74, left: 30 },
        'CB2': { top: 76, left: 50 },
        'CB3': { top: 74, left: 70 },
        'RWB': { top: 62, left: 86 },
        'CM1': { top: 44, left: 32 },
        'CM2': { top: 44, left: 68 },
        'CAM': { top: 30, left: 50 },
        'ST1': { top: 16, left: 36 },
        'ST2': { top: 16, left: 64 }
    },
    '4-1-4-1': {
        'GK': { top: 86, left: 50 },
        'LB': { top: 70, left: 16 },
        'CB1': { top: 72, left: 38 },
        'CB2': { top: 72, left: 62 },
        'RB': { top: 70, left: 84 },
        'CDM': { top: 54, left: 50 },
        'LM': { top: 34, left: 16 },
        'CM1': { top: 36, left: 38 },
        'CM2': { top: 36, left: 62 },
        'RM': { top: 34, left: 84 },
        'ST': { top: 14, left: 50 }
    }
};

// Kho 38 cau thu mac dinh
const fbDefaultPlayers = [
    { id: "cauthu_1", ten: "Thibaut Courtois", vi_tri_chuan: "GK", quoc_tich: "Bi", pac: 60, sho: 30, pas: 75, def: 92, phy: 88, ovr: 90 },
    { id: "cauthu_2", ten: "Alisson Becker", vi_tri_chuan: "GK", quoc_tich: "Brazil", pac: 62, sho: 35, pas: 85, def: 90, phy: 85, ovr: 89 },
    { id: "cauthu_3", ten: "Dang Van Lam", vi_tri_chuan: "GK", quoc_tich: "Viet Nam", pac: 65, sho: 30, pas: 72, def: 85, phy: 86, ovr: 84 },
    { id: "cauthu_24", ten: "Manuel Neuer", vi_tri_chuan: "GK", quoc_tich: "Duc", pac: 64, sho: 40, pas: 91, def: 91, phy: 87, ovr: 90 },
    { id: "cauthu_4", ten: "Virgil van Dijk", vi_tri_chuan: "CB", quoc_tich: "Ha Lan", pac: 82, sho: 60, pas: 78, def: 95, phy: 92, ovr: 92 },
    { id: "cauthu_5", ten: "Ruben Dias", vi_tri_chuan: "CB", quoc_tich: "Bo Dao Nha", pac: 78, sho: 50, pas: 75, def: 93, phy: 90, ovr: 90 },
    { id: "cauthu_6", ten: "Que Ngoc Hai", vi_tri_chuan: "CB", quoc_tich: "Viet Nam", pac: 74, sho: 58, pas: 76, def: 86, phy: 85, ovr: 84 },
    { id: "cauthu_26", ten: "William Saliba", vi_tri_chuan: "CB", quoc_tich: "Phap", pac: 84, sho: 45, pas: 77, def: 92, phy: 88, ovr: 89 },
    { id: "cauthu_27", ten: "Bui Hoang Viet Anh", vi_tri_chuan: "CB", quoc_tich: "Viet Nam", pac: 76, sho: 55, pas: 74, def: 84, phy: 85, ovr: 83 },
    { id: "cauthu_7", ten: "Alphonso Davies", vi_tri_chuan: "LB", quoc_tich: "Canada", pac: 96, sho: 68, pas: 80, def: 82, phy: 84, ovr: 87 },
    { id: "cauthu_8", ten: "Doan Van Hau", vi_tri_chuan: "LB", quoc_tich: "Viet Nam", pac: 82, sho: 70, pas: 75, def: 84, phy: 87, ovr: 84 },
    { id: "cauthu_9", ten: "Achraf Hakimi", vi_tri_chuan: "RB", quoc_tich: "Maroc", pac: 95, sho: 76, pas: 82, def: 81, phy: 83, ovr: 88 },
    { id: "cauthu_10", ten: "Vu Van Thanh", vi_tri_chuan: "RB", quoc_tich: "Viet Nam", pac: 84, sho: 72, pas: 78, def: 82, phy: 84, ovr: 83 },
    { id: "cauthu_29", ten: "Joao Cancelo", vi_tri_chuan: "RB", quoc_tich: "Bo Dao Nha", pac: 87, sho: 75, pas: 86, def: 81, phy: 76, ovr: 87 },
    { id: "cauthu_11", ten: "Rodri Hernandez", vi_tri_chuan: "CDM", quoc_tich: "Tay Ban Nha", pac: 76, sho: 80, pas: 90, def: 92, phy: 90, ovr: 93 },
    { id: "cauthu_13", ten: "Luka Modric", vi_tri_chuan: "CM", quoc_tich: "Croatia", pac: 75, sho: 82, pas: 93, def: 74, phy: 76, ovr: 90 },
    { id: "cauthu_16", ten: "Nguyen Hoang Duc", vi_tri_chuan: "CM", quoc_tich: "Viet Nam", pac: 81, sho: 80, pas: 86, def: 78, phy: 82, ovr: 85 },
    { id: "cauthu_31", ten: "Do Hung Dung", vi_tri_chuan: "CM", quoc_tich: "Viet Nam", pac: 80, sho: 75, pas: 84, def: 82, phy: 83, ovr: 84 },
    { id: "cauthu_32", ten: "Nguyen Tuan Anh", vi_tri_chuan: "CM", quoc_tich: "Viet Nam", pac: 78, sho: 74, pas: 88, def: 77, phy: 75, ovr: 83 },
    { id: "cauthu_33", ten: "Eduardo Camavinga", vi_tri_chuan: "CDM", quoc_tich: "Phap", pac: 84, sho: 70, pas: 83, def: 85, phy: 85, ovr: 87 },
    { id: "cauthu_34", ten: "Federico Valverde", vi_tri_chuan: "CM", quoc_tich: "Uruguay", pac: 90, sho: 84, pas: 85, def: 82, phy: 86, ovr: 89 },
    { id: "cauthu_35", ten: "Declan Rice", vi_tri_chuan: "CDM", quoc_tich: "Anh", pac: 80, sho: 72, pas: 84, def: 88, phy: 87, ovr: 88 },
    { id: "cauthu_12", ten: "Kevin De Bruyne", vi_tri_chuan: "CAM", quoc_tich: "Bi", pac: 78, sho: 88, pas: 96, def: 68, phy: 79, ovr: 92 },
    { id: "cauthu_14", ten: "Jude Bellingham", vi_tri_chuan: "CAM", quoc_tich: "Anh", pac: 85, sho: 88, pas: 86, def: 80, phy: 87, ovr: 91 },
    { id: "cauthu_15", ten: "Nguyen Quang Hai", vi_tri_chuan: "CAM", quoc_tich: "Viet Nam", pac: 80, sho: 84, pas: 88, def: 65, phy: 74, ovr: 85 },
    { id: "cauthu_36", ten: "Pedri Gonzalez", vi_tri_chuan: "CAM", quoc_tich: "Tay Ban Nha", pac: 82, sho: 76, pas: 90, def: 70, phy: 73, ovr: 88 },
    { id: "cauthu_37", ten: "Phil Foden", vi_tri_chuan: "CAM", quoc_tich: "Anh", pac: 88, sho: 86, pas: 88, def: 60, phy: 70, ovr: 89 },
    { id: "cauthu_17", ten: "Cristiano Ronaldo", vi_tri_chuan: "ST", quoc_tich: "Bo Dao Nha", pac: 86, sho: 94, pas: 82, def: 40, phy: 88, ovr: 93 },
    { id: "cauthu_18", ten: "Lionel Messi", vi_tri_chuan: "RW", quoc_tich: "Argentina", pac: 84, sho: 92, pas: 95, def: 38, phy: 72, ovr: 93 },
    { id: "cauthu_19", ten: "Kylian Mbappe", vi_tri_chuan: "LW", quoc_tich: "Phap", pac: 97, sho: 92, pas: 84, def: 42, phy: 80, ovr: 93 },
    { id: "cauthu_20", ten: "Erling Haaland", vi_tri_chuan: "ST", quoc_tich: "Na Uy", pac: 91, sho: 95, pas: 70, def: 48, phy: 92, ovr: 92 },
    { id: "cauthu_21", ten: "Vinicius Junior", vi_tri_chuan: "LW", quoc_tich: "Brazil", pac: 96, sho: 86, pas: 82, def: 35, phy: 74, ovr: 90 },
    { id: "cauthu_22", ten: "Nguyen Tien Linh", vi_tri_chuan: "ST", quoc_tich: "Viet Nam", pac: 81, sho: 85, pas: 72, def: 44, phy: 83, ovr: 84 },
    { id: "cauthu_23", ten: "Huynh Nhu", vi_tri_chuan: "ST", quoc_tich: "Viet Nam", pac: 83, sho: 86, pas: 80, def: 46, phy: 78, ovr: 85 },
    { id: "cauthu_38", ten: "Lamine Yamal", vi_tri_chuan: "RW", quoc_tich: "Tay Ban Nha", pac: 92, sho: 82, pas: 86, def: 40, phy: 68, ovr: 87 },
    { id: "cauthu_39", ten: "Bukayo Saka", vi_tri_chuan: "RW", quoc_tich: "Anh", pac: 89, sho: 85, pas: 84, def: 65, phy: 78, ovr: 88 },
    { id: "cauthu_40", ten: "Son Heung-min", vi_tri_chuan: "LW", quoc_tich: "Han Quoc", pac: 88, sho: 89, pas: 83, def: 45, phy: 75, ovr: 88 },
    { id: "cauthu_41", ten: "Nguyen Van Toan", vi_tri_chuan: "RW", quoc_tich: "Viet Nam", pac: 90, sho: 78, pas: 76, def: 50, phy: 72, ovr: 82 }
];

async function initFootballHub() {
    try {
        const res = await fetch('/api/football');
        const data = await res.json();
        if (data.status === 'success') {
            fbPlayersPool = (data.players && data.players.length > 0) ? data.players : fbDefaultPlayers;
            fbLegendsList = data.legends || [];
            fbRulesList = data.rules || [];
            fbScienceList = data.science || [];
            fbSkillsHealthList = data.skills_health || [];
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
                "GK": "cauthu_1", "LB": "cauthu_7", "CB1": "cauthu_4", "CB2": "cauthu_5", "RB": "cauthu_9",
                "CDM": "cauthu_11", "CM": "cauthu_13", "CAM": "cauthu_15",
                "LW": "cauthu_19", "ST": "cauthu_17", "RW": "cauthu_18"
            }
        };
    }

    fbSelectedFormation = fbCurrentTeam.so_do || '4-3-3';
    const formSel = document.getElementById('fbSelectFormation');
    if (formSel) {
        formSel.value = fbSelectedFormation;
    }

    renderFootballPitch();
    renderFootballLegends();
    renderFootballRulesAndScience();
    renderFootballOpponents();
}

function getFbLocalTeam() {
    const saved = localStorage.getItem('fb_dream_team_v2');
    if (saved) {
        try { return JSON.parse(saved); } catch (e) {}
    }
    return null;
}

function saveFbLocalTeam(team) {
    localStorage.setItem('fb_dream_team_v2', JSON.stringify(team));
}

function switchFbSubTab(subTab, btn) {
    fbCurrentSubTab = subTab;
    document.querySelectorAll('.fb-subtab-btn').forEach(b => {
        b.classList.remove('active');
        if (b.dataset && b.dataset.subtab === subTab) b.classList.add('active');
    });
    if (btn) btn.classList.add('active');

    document.querySelectorAll('.fb-subtab-pane').forEach(pane => {
        pane.style.display = 'none';
    });

    const target = document.getElementById(`fb-subpane-${subTab}`) || document.getElementById(`fbSubTab_${subTab}`);
    if (target) {
        target.style.display = 'block';
    }

    if ((subTab === 'tran_dau' || subTab === 'trandau') && !fbMatchSim) {
        const board = document.getElementById('fbMatchBoard');
        if (board) board.style.display = 'block';
        startFbMatchSimulation();
    }
}

window.switchFootballSubTab = switchFbSubTab;
window.switchFbSubTab = switchFbSubTab;
window.onFbFormationChange = function(formationId) {
    changeFbFormation(formationId);
};

function changeFbFormation(formationId) {
    fbSelectedFormation = formationId;
    if (!fbCurrentTeam) fbCurrentTeam = {};
    fbCurrentTeam.so_do = formationId;

    const coords = fbFormationCoordinates[formationId] || fbFormationCoordinates['4-3-3'];
    const currentSlots = fbCurrentTeam.danh_sach_da_chinh || {};
    const newSlots = {};
    const keys = Object.keys(coords);

    keys.forEach((slot, idx) => {
        if (currentSlots[slot]) {
            newSlots[slot] = currentSlots[slot];
        } else {
            newSlots[slot] = fbPlayersPool[idx % fbPlayersPool.length].id;
        }
    });

    fbCurrentTeam.danh_sach_da_chinh = newSlots;
    renderFootballPitch();
}

function renderFootballPitch() {
    const pitch = document.getElementById('fbPitchContainer') || document.getElementById('fbSoccerPitch');
    if (!pitch) return;

    const coords = fbFormationCoordinates[fbSelectedFormation] || fbFormationCoordinates['4-3-3'];
    const squad = fbCurrentTeam.danh_sach_da_chinh || {};
    const playerMap = {};
    fbPlayersPool.forEach(p => { playerMap[p.id] = p; });

    let pitchHtml = `
        <div class="fb-pitch-grass">
            <div class="fb-pitch-line fb-pitch-center-circle"></div>
            <div class="fb-pitch-line fb-pitch-halfway"></div>
            <div class="fb-pitch-line fb-pitch-box-top"></div>
            <div class="fb-pitch-line fb-pitch-box-bottom"></div>
            <div class="fb-pitch-line fb-pitch-spot-top"></div>
            <div class="fb-pitch-line fb-pitch-spot-bottom"></div>
    `;

    let totalOvr = 0;
    let count = 0;

    for (const slotKey in coords) {
        const c = coords[slotKey];
        const playerId = squad[slotKey];
        const p = playerMap[playerId] || fbPlayersPool[0];
        totalOvr += p.ovr;
        count++;

        const isExactPos = (p.vi_tri_chuan === slotKey.replace(/[0-9]/g, ''));
        const bonusTag = isExactPos ? '<span class="fb-pos-synergy">+0.5</span>' : '';

        pitchHtml += `
            <div class="fb-pitch-card" style="top: ${c.top}%; left: ${c.left}%;" onclick="openFbPlayerPicker('${slotKey}')">
                <div class="fb-card-slot">${slotKey} ${bonusTag}</div>
                <div class="fb-card-ovr">${p.ovr}</div>
                <div class="fb-card-name">${p.ten}</div>
                <div class="fb-card-pos">${p.vi_tri_chuan}</div>
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
        <option value="opp_allstars">Sieu Sao The Gioi All-Stars (Suc manh 94)</option>
        <option value="opp_europe">Lien Quan Chau Au UEFA Legends (Suc manh 92)</option>
        <option value="opp_vietnam">The He Vang Viet Nam All-Stars (Suc manh 89)</option>
        <option value="opp_southamerica">Con Mua Samba Nam My CONMEBOL (Suc manh 93)</option>
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
            doi_thu: { ten: "Sieu Sao The Gioi All-Stars", suc_manh: 94 },
            ti_so_nha: 0,
            ti_so_khach: 0,
            tinh_huong_list: [
                {
                    phut: 12,
                    tieu_de: "Dot pha canh va chuyen bong xuyen tuyen",
                    mo_ta_tinh_huong: "Tien dao canh doi nha cam bong dot pha ben hanh lang trai, hai hau ve doi ban dang lao ra ap sat.",
                    cau_hoi: "De qua bong di cuon xoay vong cung ra sau lung hang phong ngu doi ban vao cho tien dao cam bang vao, cau thu nen tiep xuc vao phan nao cua trai bong?",
                    cac_lua_chon: [
                        { phuong_an: "Sut vao ma trong mu ban chan de tao hieu ung Magnus cuon xoay", dung: true },
                        { phuong_an: "Sut bang mui giay thang truc dien", dung: false },
                        { phuong_an: "Sut bang got chan tu duoi len", dung: false }
                    ],
                    binh_luan_dung: "VAOOOO! Mot pha cat bong sieu hang tao hieu ung xoay Magnus hoan hao, tien dao cam bang vao dem bong tung luoi mo ti so!",
                    binh_luan_sai: "Rat tiec, pha tiep xuc bong thieu chinh xac da khien qua bong di nhe va nam gon trong tay thu mon doi ban."
                },
                {
                    phut: 36,
                    tieu_de: "Da phat truc tiep hang rao cu ly 22 met",
                    mo_ta_tinh_huong: "Doi nha duoc huong qua phat sat vong cam. Hang rao doi ban gom 5 nguoi cao to bat nhay.",
                    cau_hoi: "Khoang cach tu qua bong den hang rao doi phuong theo luat FIFA quy dinh toi thieu la bao nhieu met?",
                    cac_lua_chon: [
                        { phuong_an: "9.15 met (tuong duong 10 yards)", dung: true },
                        { phuong_an: "5.5 met", dung: false },
                        { phuong_an: "11 met", dung: false }
                    ],
                    binh_luan_dung: "SIUUUU! Cu sut phat theo phong cach Knuckleball hinh la vang roi cam thang vao goc chu A! Khong the can pha!",
                    binh_luan_sai: "Bong cham dung dau mot cau thu tren hang rao va di chech cot doc ra ngoai."
                },
                {
                    phut: 52,
                    tieu_de: "Phan cong chop nhoang 3 danh 2",
                    mo_ta_tinh_huong: "Doi ban dang dang cao doi hinh thi mat bong. Doi nha to chuc phan cong sieu toc voi bo 3 tan cong.",
                    cau_hoi: "Neu qua bong bay voi van toc 90 km/h vuot qua quang duong 45 met toi vi tri tien dao, thi thoi gian bong bay la bao nhieu giay?",
                    cac_lua_chon: [
                        { phuong_an: "1.8 giay (vi 90 km/h = 25 m/s, thoi gian t = 45 / 25 = 1.8s)", dung: true },
                        { phuong_an: "3.5 giay", dung: false },
                        { phuong_an: "0.5 giay", dung: false }
                    ],
                    binh_luan_dung: "TUYET VOI! Duong chuyen vuot tuyen chuan xac tung mi-li-met, tien dao nhan bong tung cu sut cheo goc nhan doi cach biet!",
                    binh_luan_sai: "Do tinh toan sai thoi diem buoc chay nen tien dao da bi bat loi viet vi."
                },
                {
                    phut: 76,
                    tieu_de: "Khong chien: Pha phat goc phut 76",
                    mo_ta_tinh_huong: "Doi nha duoc huong qua phat goc. Cac trung ve cao to da dang len tham gia khong chien.",
                    cau_hoi: "Khi mot cau thu bat cao danh dau, de qua bong di cam hiem hoc xuong goc luoi, diem tiep xuc tot nhat tren qua bong la gi?",
                    cac_lua_chon: [
                        { phuong_an: "Dung tran tiep xuc vao nua tren cua qua bong kem theo gap co nhe", dung: true },
                        { phuong_an: "Dung dinh dau tiep xuc vao day duoi qua bong", dung: false },
                        { phuong_an: "Dung tai de danh dau", dung: false }
                    ],
                    binh_luan_dung: "DANH DAU HOAN HAO! Cu danh dau cam xuong dat khien thu mon phai bo tay nhin bong bay vao luoi!",
                    binh_luan_sai: "Pha danh dau bi loi nhip, bong bay vot xa ngang len khan dai."
                },
                {
                    phut: 90,
                    tieu_de: "Cu sut phat den Penalty dinh doat tran dau",
                    mo_ta_tinh_huong: "Phut bu gio cuoi cung 90+2, doi nha duoc huong qua phat den penalty sau mot pha truy can trai phep trong vong cam.",
                    cau_hoi: "Khi thuc hien qua phat den Penalty tu cham 11m, luat FIFA quy dinh thu mon doi phuong phai giu vi tri nhu the nao truoc khi bong duoc da?",
                    cac_lua_chon: [
                        { phuong_an: "It nhat mot phan cua ban chan phai cham hoac o tren vach voi cau mon", dung: true },
                        { phuong_an: "Duoc phep buoc len phia truoc 2 met de gay ap luc", dung: false },
                        { phuong_an: "Phai ngoi xuong san", dung: false }
                    ],
                    binh_luan_dung: "BAN THANG QUYET DINH! Cu sut quyet doan vao goc cao khung thanh an dinh chien thang ve vang cho doi nha!",
                    binh_luan_sai: "Cu sut di qua cao so voi xa ngang, tieng coi ket thuc tran dau vang len."
                }
            ]
        };
    }

    fbMatchSituationIdx = 0;
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
        document.getElementById('fbMatchClock').innerText = "Phut: 90' HET GIO";
        document.getElementById('fbSitTitle').innerText = "TRAN DAU KET THUC";
        document.getElementById('fbSitDesc').innerText = `Ti so chung cuoc: Dream Team ${sim.ti_so_nha} - ${sim.ti_so_khach} ${sim.doi_thu.ten}.`;
        document.getElementById('fbSitQuestion').innerText = "";
        document.getElementById('fbSitOptions').innerHTML = `
            <button class="btn-primary" style="margin-top: 15px; padding: 12px 24px;" onclick="startFbMatchSimulation()">Thi Dau Tran Moi</button>
        `;

        if (sim.ti_so_nha > sim.ti_so_khach) {
            alert(`CHIEN THANG!\n\nXuat sac! Dream Team cua em da danh bai ${sim.doi_thu.ten} voi ti so ${sim.ti_so_nha} - ${sim.ti_so_khach}!\nThuong +100 XP hoc tap!`);
            try { congDiemThuongWeb(100); } catch (e) {}
        } else if (sim.ti_so_nha === sim.ti_so_khach) {
            alert(`HOA KICH TINH!\n\nTran hoa nghet tho ${sim.ti_so_nha} - ${sim.ti_so_khach}! Thuong +50 XP!`);
            try { congDiemThuongWeb(50); } catch (e) {}
        } else {
            alert(`THAT BAI SAT NUT!\n\nDoi ban da thi dau kien cuong! Hay tiep tuc ren luyen chien thuat nhe! Thuong +20 XP!`);
            try { congDiemThuongWeb(20); } catch (e) {}
        }
        return;
    }

    const sit = list[fbMatchSituationIdx];
    document.getElementById('fbMatchClock').innerText = `Phut: ${sit.phut}'`;
    document.getElementById('fbSitTitle').innerText = `Phut ${sit.phut}: ${sit.tieu_de}`;
    document.getElementById('fbSitDesc').innerText = sit.mo_ta_tinh_huong;
    document.getElementById('fbSitQuestion').innerText = `Thu thach chien thuat: ${sit.cau_hoi}`;

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

    // Quy tac: 30% chac chan vao, 30% chac chan khong vao, 40% do ban quyet dinh
    const r = Math.random();
    let isGoal = false;
    let lyDo = "";

    if (r < 0.30) {
        isGoal = true;
        lyDo = " (30% sieu pham may man chac chan vao)";
    } else if (r < 0.60) {
        isGoal = false;
        lyDo = " (30% bong dap cot doc xa ngang)";
    } else {
        isGoal = Boolean(isCorrect);
        lyDo = isGoal ? " (40% do ban quyet dinh chinh xac)" : " (40% do phan doan chua dung)";
    }

    if (isGoal) {
        sim.ti_so_nha++;
        document.getElementById('fbCommentaryBox').innerText = `Binh luan vien: ${sit.binh_luan_dung}${lyDo}`;
        document.getElementById('fbCommentaryBox').style.color = '#10B981';
    } else {
        if (Math.random() < 0.6) sim.ti_so_khach++;
        document.getElementById('fbCommentaryBox').innerText = `Binh luan vien: ${sit.binh_luan_sai}${lyDo}`;
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
        { id: "cr7", ten: "Cristiano Ronaldo", biet_danh: "CR7", quoc_tich: "Bo Dao Nha", vi_tri: "Tien dao", so_ao: 7, cau_lac_bo: "Real Madrid, Man United, Al Nassr", ky_luc: "Hon 900 ban thang chinh thuc, 5 Qua Bong Vang", loi_khuyen: "Thanh cong khong phai su ngau nhien, do la ky luat va y chi phi thuong." },
        { id: "messi", ten: "Lionel Messi", biet_danh: "El Pulga", quoc_tich: "Argentina", vi_tri: "Tien dao", so_ao: 10, cau_lac_bo: "Barcelona, Inter Miami", ky_luc: "8 Qua Bong Vang, Vo dich World Cup 2022", loi_khuyen: "Hay luon kien tri ngay ca khi xuat phat diem co nhieu kho khan." },
        { id: "pele", ten: "Pele", biet_danh: "Vua Bong Da", quoc_tich: "Brazil", vi_tri: "Tien dao", so_ao: 10, cau_lac_bo: "Santos FC", ky_luc: "3 lan Vo dich World Cup lich su", loi_khuyen: "Bong da la bai hoc ve su gan ket dong doi va tinh yeu thuong." },
        { id: "maradona", ten: "Diego Maradona", biet_danh: "Cau Be Vang", quoc_tich: "Argentina", vi_tri: "Tien ve tan cong", so_ao: 10, cau_lac_bo: "Napoli, Boca Juniors", ky_luc: "Ban thang the ky qua 5 cau thu tai World Cup 1986", loi_khuyen: "Dam me manh liet co the lam nen nhung dieu ky dieu." },
        { id: "ronaldo_r9", ten: "Ronaldo de Lima", biet_danh: "Nguoi Ngoai Hanh Tinh", quoc_tich: "Brazil", vi_tri: "Tien dao cam", so_ao: 9, cau_lac_bo: "Real Madrid, Inter Milan, Barcelona", ky_luc: "2 lan Vo dich World Cup, Vua pha luoi World Cup 2002", loi_khuyen: "Nhung chan thuong dau don nhat cung khong the dap tat khao khat tro lai san co." },
        { id: "ronaldinho", ten: "Ronaldinho Gaucho", biet_danh: "Ao Thuat Gia San Co", quoc_tich: "Brazil", vi_tri: "Tien ve canh", so_ao: 10, cau_lac_bo: "Barcelona, AC Milan, PSG", ky_luc: "Qua Bong Vang 2005, Vo dich World Cup 2002", loi_khuyen: "Bong da la niem vui. Hay choi bong voi tinh yeu thuan khiet." },
        { id: "zidane", ten: "Zinedine Zidane", biet_danh: "Zizou", quoc_tich: "Phap", vi_tri: "Tien ve tan cong", so_ao: 10, cau_lac_bo: "Real Madrid, Juventus", ky_luc: "Cu dup chung ket World Cup 1998, 3 Cup C1 tren cuong vi HLV", loi_khuyen: "Su hao hoa the hien o kha nang dua ra quyet dinh dung dan nhat." },
        { id: "cruyff", ten: "Johan Cruyff", biet_danh: "Thanh Johan", quoc_tich: "Ha Lan", vi_tri: "Tien ve / Tien dao", so_ao: 14, cau_lac_bo: "Ajax, Barcelona", ky_luc: "Khai sinh triet ly Bong da tong luc, 3 Qua Bong Vang", loi_khuyen: "Choi bong bang cai dau truoc khi choi bang doi chan." },
        { id: "beckenbauer", ten: "Franz Beckenbauer", biet_danh: "Hoang De Bong Da", quoc_tich: "Duc", vi_tri: "Libero", so_ao: 5, cau_lac_bo: "Bayern Munich", ky_luc: "Vo dich World Cup ca khi lam cau thu va HLV, 2 Qua Bong Vang", loi_khuyen: "Nguoi chi huy thuc thu luon truyen su tu tin va diem tinh cho toan doi." },
        { id: "mbappe", ten: "Kylian Mbappe", biet_danh: "Toc Do Sieu Am", quoc_tich: "Phap", vi_tri: "Tien dao", so_ao: 9, cau_lac_bo: "Real Madrid, PSG", ky_luc: "Hat-trick chung ket World Cup 2022", loi_khuyen: "Tuoi tre hay dam mo uoc lon va but pha gioi han ban than." },
        { id: "haaland", ten: "Erling Haaland", biet_danh: "Co May Ghi Ban", quoc_tich: "Na Uy", vi_tri: "Tien dao cam", so_ao: 9, cau_lac_bo: "Man City, Dortmund", ky_luc: "Ky luc 36 ban thang 1 mua giai Ngoai Hang Anh", loi_khuyen: "Tap trung cao do vao tung co hoi va khong bao gio thoa man." },
        { id: "quanghai", ten: "Nguyen Quang Hai", biet_danh: "Hai Con", quoc_tich: "Viet Nam", vi_tri: "Tien ve", so_ao: 19, cau_lac_bo: "CAHN, Ha Noi FC", ky_luc: "Sieu pham Cau vong tuyet Thuong Chau 2018", loi_khuyen: "Luon no luc vi mau co sac ao va niem tu hao dan toc Viet Nam." },
        { id: "huynhnhu", ten: "Huynh Nhu", biet_danh: "Nu Tuong San Co", quoc_tich: "Viet Nam", vi_tri: "Tien dao", so_ao: 9, cau_lac_bo: "Lank FC, TP Ho Chi Minh", ky_luc: "5 Qua Bong Vang Nu Viet Nam, World Cup 2023", loi_khuyen: "Phu nu Viet Nam co the lam nen nhung dieu ky dieu neu kien tri." }
    ];

    legends.forEach(l => {
        const card = document.createElement('div');
        card.className = 'fb-legend-card';
        card.innerHTML = `
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
                <div>
                    <h3 style="color: #F59E0B; font-size: 18px; font-weight: 900; margin: 0;">${l.ten}</h3>
                    <div style="color: #6EE7B7; font-size: 13px; font-weight: 700;">${l.biet_danh} | So ao: #${l.so_ao}</div>
                </div>
                <span style="background: rgba(16, 185, 129, 0.2); color: #10B981; padding: 2px 8px; border-radius: 6px; font-size: 12px; font-weight: bold;">${l.quoc_tich}</span>
            </div>
            <div style="color: #CBD5E1; font-size: 13px; margin-bottom: 6px;"><b>CLB:</b> ${l.cau_lac_bo}</div>
            <div style="color: #94A3B8; font-size: 12.5px; margin-bottom: 8px;"><b>Ky luc:</b> ${l.ky_luc}</div>
            <div style="background: rgba(0,0,0,0.3); padding: 8px; border-radius: 8px; border-left: 3px solid #F59E0B; font-size: 12.5px; color: #E2E8F0; font-style: italic;">
                "${l.loi_khuyen}"
            </div>
        `;
        listEl.appendChild(card);
    });
}

function loadFootballQuiz() {
    const list = [
        {
            cau_hoi: "Cau thu duy nhat trong lich su bong da the gioi tung 3 lan vo dich FIFA World Cup la ai?",
            dap_an: ["Pele", "Diego Maradona", "Cristiano Ronaldo", "Zinedine Zidane"],
            dap_an_dung: "Pele",
            giai_thich: "Pele (Brazil) da cung doi tuyen vo dich vao cac nam 1958, 1962 va 1970."
        },
        {
            cau_hoi: "Hieu ung vat ly nao giup qua bong xoay tao quy dao bay uon cong vong cung qua hang rao?",
            dap_an: ["Hieu ung Magnus", "Hieu ung Doppler", "Dinh luat Van vat hap dan", "Hieu ung Quang dien"],
            dap_an_dung: "Hieu ung Magnus",
            giai_thich: "Hieu ung Magnus sinh ra do su chanh lech ap suat khi vat the xoay tron trong chat luu (khong khi)."
        },
        {
            cau_hoi: "Ban thang 'Cau vong tuyet' cua Nguyen Quang Hai duoc ghi vao luoi doi tuyen nao?",
            dap_an: ["U23 Uzbekistan", "U23 Qatar", "U23 Iraq", "U23 Han Quoc"],
            dap_an_dung: "U23 Uzbekistan",
            giai_thich: "Quang Hai ghi sieu pham da phat trong tran chung ket U23 Chau A 2018 tai Thuong Chau giua troi tuyet."
        },
        {
            cau_hoi: "Mot qua bong duoc sut voi van toc 108 km/h. Doi ra don vi met tren giay (m/s) thi bang bao nhieu?",
            dap_an: ["30 m/s", "25 m/s", "36 m/s", "20 m/s"],
            dap_an_dung: "30 m/s",
            giai_thich: "Ta lay 108 chia cho 3.6 = 30 m/s."
        },
        {
            cau_hoi: "De phong ngua nguy co dut day chang cheo truoc (ACL) khi da bong, hoc sinh can thuc hien bien phap nao?",
            dap_an: ["Khoi dong dong 10-15 phut va tap tiep dat bang mui chan", "Ngoi yen truoc khi vao san", "Uong nuoc co ga", "Sut that manh ngay tu dau"],
            dap_an_dung: "Khoi dong dong 10-15 phut va tap tiep dat bang mui chan",
            giai_thich: "Khoi dong dong kich hoat co quanh khop goi va giam toi 70% nguy co chan thuong day chang cheo."
        }
    ];

    fbQuizCurrent = list[Math.floor(Math.random() * list.length)];
    const qEl = document.getElementById('fbQuizQuestion');
    const resEl = document.getElementById('fbQuizResult');
    if (!qEl || !resEl) return;

    qEl.innerText = fbQuizCurrent.cau_hoi;
    resEl.innerText = '';

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
                resEl.innerText = `CHINH XAC! Thuong +30 XP! Giai thich: ${fbQuizCurrent.giai_thich}`;
                resEl.style.color = '#10B981';
                try { congDiemThuongWeb(30); } catch (e) {}
            } else {
                resEl.innerText = `CHUA CHINH XAC! Dap an dung la: ${fbQuizCurrent.dap_an_dung}. Giai thich: ${fbQuizCurrent.giai_thich}`;
                resEl.style.color = '#EF4444';
            }
        };
        container.appendChild(btn);
    });
}

// --- CAM NANG LUAT FIFA, KY NANG & KHOA HOC BONG DA ---
function renderFootballRulesAndScience() {
    const rulesContainer = document.getElementById('fbRulesContainer');
    const scienceContainer = document.getElementById('fbScienceContainer');
    const skillsContainer = document.getElementById('fbSkillsContainer');
    if (!rulesContainer || !scienceContainer) return;

    rulesContainer.innerHTML = '';
    const rules = fbRulesList.length > 0 ? fbRulesList : [
        { ten_luat: "Luat Viet Vi (Offside)", tom_tat: "Cau thu o vi tri viet vi neu dung gan duong bien ngang doi phuong hon ca bong va cau thu phong ngu cuoi cung thu hai khi dong doi chuyen bong.", luu_y_de_nho: "Khong bi viet vi khi nhan bong tu Nem bien, Phat goc hoac Phat bong cau mon." },
        { ten_luat: "Luat Phat Den (Penalty)", tom_tat: "Ap dung khi cau thu phong ngu pham loi truc tiep trong khu vuc 16m50 cua doi minh. Cu sut thuc hien tu cham 11 met.", luu_y_de_nho: "Thu mon phai giu it nhat 1 chan tren vach voi khi bong duoc da." },
        { ten_luat: "Luat The Vang va The Do", tom_tat: "The vang canh cao loi nguy hiem. Nhan 2 the vang trong 1 tran tuong duong 1 the do, cau thu phai roi san ngay lap tuc.", luu_y_de_nho: "Doi bi the do phai thi dau thieu nguoi suot thoi gian con lai." },
        { ten_luat: "Cong Nghe Trong Tai Video VAR", tom_tat: "Camera sieu cham va vach ke 3D ho tro trong tai chinh trong 4 truong hop: Ban thang, Phat den, The do truc tiep va Nhan dien sai cau thu.", luu_y_de_nho: "Trong tai chinh tren san luon la nguoi dua ra quyet dinh cuoi cung." }
    ];

    rules.forEach(r => {
        const box = document.createElement('div');
        box.className = 'fb-rule-box';
        box.innerHTML = `
            <h4 style="color: #06B6D4; font-size: 17px; margin-bottom: 8px; font-weight: 900;">${r.ten_luat}</h4>
            <p style="color: #E2E8F0; font-size: 13.5px; line-height: 1.6; margin-bottom: 8px;">${r.tom_tat}</p>
            <div style="background: rgba(6, 182, 212, 0.15); border-left: 3px solid #06B6D4; padding: 6px 10px; border-radius: 6px; color: #CBD5E1; font-size: 12.5px;">
                <b>Luu y quan trong:</b> ${r.luu_y_de_nho}
            </div>
        `;
        rulesContainer.appendChild(box);
    });

    scienceContainer.innerHTML = '';
    const science = fbScienceList.length > 0 ? fbScienceList : [
        { chu_de: "Hieu Ung Xoay Magnus (Vat Ly 8)", khoa_hoc: "Khi qua bong xoay tron trong khong khi, su chenh lech van toc dong khi tao ra luc Magnus day bong uon cong qua hang rao danh lua thu mon.", mon_hoc: "Vat Ly 8 (Ap suat chat luu)" },
        { chu_de: "Van Toc Sut Bong v = s / t (Vat Ly 7)", khoa_hoc: "Mot cu sut 108 km/h doi ra bang 30 m/s. O khoang cach 20 met, bong vao luoi chi mat 0.66 giay, nhanh hon toc do phan xa cua con nguoi (0.2s - 0.3s).", mon_hoc: "Toan & Vat Ly 7 (Van toc chuyen dong)" },
        { chu_de: "Ti Le Kiem Soat Bong & xG (Toan 7 & 8)", khoa_hoc: "Ti le kiem soat bong = (Thoi gian co bong / Tong thoi gian bong song) x 100%. Chi so xG do xac suat ghi ban tu 0 den 1 dua vao vi tri va goc sut.", mon_hoc: "Toan 7 & 8 (Ti so phan tram va Thong ke)" },
        { chu_de: "Goc Sut Toi Uu (Hinh Hoc 7)", khoa_hoc: "Cang tien vao chinh dien cau mon, goc sut mo rong toi da tren 35 do. Khi chay sat goc bien ngang, goc sut thu hep thanh goc nhon kho ghi ban.", mon_hoc: "Hinh Hoc 7 (Goc trong tam giac)" }
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

    // Neu co skillsContainer thi render cam nang ky nang
    if (skillsContainer) {
        skillsContainer.innerHTML = '';
        const skills = fbSkillsHealthList.length > 0 ? fbSkillsHealthList : [
            { ten_ky_nang: "Ky thuat Sut mu chinh dien (Knuckleball)", loai: "ky_nang", cach_thuc_hien: "Chay da thang, khoa co chan, tiep xuc dung tam qua bong bang mu giay chinh dien.", hieu_qua: "Bong bay lieng khong xoay, thu mon khong the doan duoc quy dao." },
            { ten_ky_nang: "Ky thuat Do buoc mot dinh chan (First Touch)", loai: "ky_nang", cach_thuc_hien: "Mo rong long ban chan, hoi ru chan ve sau khi tiep xuc bong de triet tieu xung luc.", hieu_qua: "Bong nam ngay trong tam kiem soat cho nhip sut hoac chuyen tiep theo." },
            { ten_ky_nang: "Ky thuat Dao chan qua nguoi (Step-over)", loai: "ky_nang", cach_thuc_hien: "Dua chan vong qua bong tu trong ra ngoai nhac vai danh lua hau ve.", hieu_qua: "Lam hau ve mat trong tam, mo toang khoang trong de burt toc." },
            { ten_ky_nang: "Khoi dong dong phong ngua dut day chang cheo (ACL)", loai: "suc_khoe", cach_thuc_hien: "Khoi dong 10-15 phut lam am khop goi, luyen tiep dat bang mui chan voi dau goi hoi chui.", hieu_qua: "Giam toi 70% nguy co chan thuong day chang cheo o lua tuoi hoc sinh." },
            { ten_ky_nang: "Phong ngua lat somi co chan va cang co", loai: "suc_khoe", cach_thuc_hien: "Chon giay vua van, buoc chat day giay. Tiep dat can bang bang ca hai chan khi tranh chap bong bong.", hieu_qua: "Bao ve bao khop co chan, tranh bi bong gan hoac lat co chan." }
        ];

        skills.forEach(sk => {
            const box = document.createElement('div');
            box.className = 'fb-rule-box';
            const isSkill = sk.loai === 'ky_nang';
            box.style.border = isSkill ? '1.5px solid #F59E0B' : '1.5px solid #EC4899';
            const badgeBg = isSkill ? 'rgba(245, 158, 11, 0.2)' : 'rgba(236, 72, 153, 0.2)';
            const badgeColor = isSkill ? '#F59E0B' : '#EC4899';
            const badgeText = isSkill ? 'KY NANG THUC CHIEN' : 'SUC KHOE & PHONG NGUa';

            box.innerHTML = `
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <h4 style="color: ${badgeColor}; font-size: 17px; font-weight: 900;">${sk.ten_ky_nang}</h4>
                    <span style="background: ${badgeBg}; color: ${badgeColor}; padding: 2px 8px; border-radius: 6px; font-size: 11px; font-weight: bold;">${badgeText}</span>
                </div>
                <p style="color: #E2E8F0; font-size: 13px; line-height: 1.5; margin-bottom: 6px;"><b>Cach thuc hien:</b> ${sk.cach_thuc_hien}</p>
                <div style="background: rgba(0,0,0,0.3); border-left: 3px solid ${badgeColor}; padding: 6px 10px; border-radius: 6px; color: #CBD5E1; font-size: 12.5px;">
                    <b>Hieu qua:</b> ${sk.hieu_qua}
                </div>
            `;
            skillsContainer.appendChild(box);
        });
    }
}

function congDiemThuongWeb(xp) {
    if (typeof userXp !== 'undefined') {
        userXp += xp;
        const xpEl = document.getElementById('userXpVal');
        if (xpEl) xpEl.innerText = userXp;
        localStorage.setItem('eduverse_user_xp', userXp.toString());
    }
}

window.initFootballHub = initFootballHub;
window.renderFootballPitch = renderFootballPitch;
window.openFbPlayerPicker = openFbPlayerPicker;
window.closeFbPlayerPicker = closeFbPlayerPicker;
window.saveFbDreamTeam = saveFbDreamTeam;
window.startFbMatchSimulation = startFbMatchSimulation;
window.loadFootballQuiz = loadFootballQuiz;
window.renderFootballLegends = renderFootballLegends;
window.renderFootballRulesAndScience = renderFootballRulesAndScience;

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        initFootballHub();
    });
} else {
    initFootballHub();
}


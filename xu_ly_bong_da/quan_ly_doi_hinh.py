# Thu muc: xu_ly_bong_da
# File: quan_ly_doi_hinh.py
# Mo ta: Quan ly he thong xay dung Doi hinh trong mo (Dream Team 11) va chi so cau thu

import json
import os

FILE_DOI_HINH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "du_lieu", "doi_hinh_bong_da.json"))

def lay_danh_sach_so_do():
    """Tra ve 6 so do chien thuat kinh dien the gioi."""
    return [
        {
            "id": "4-3-3",
            "ten": "4-3-3 Tan Cong Ruc Lua",
            "triet_ly": "Kiem soat the tran bang toc do hai bien, pressing tam cao va ho tro trung tuyen",
            "mo_ta": "Hai tien dao canh toc do khoet sau vao nach hang thu doi phuong, tien ve tru thu hoi bong va phat dong tan cong nhanh.",
            "vi_tri": ["GK", "LB", "CB1", "CB2", "RB", "CDM", "CM", "CAM", "LW", "ST", "RW"]
        },
        {
            "id": "4-4-2",
            "ten": "4-4-2 Can Bang Truyen Thong",
            "triet_ly": "Ket cau doi hinh can xung, phan bo luc luong deu tren toan mat san",
            "mo_ta": "Bo doi tien dao song sat ho tro nhau ghi ban, hai tien ve bien tat bong vao vong cam va bo doi tien ve trung tam danh chan.",
            "vi_tri": ["GK", "LB", "CB1", "CB2", "RB", "LM", "CM1", "CM2", "RM", "ST1", "ST2"]
        },
        {
            "id": "3-5-2",
            "ten": "3-5-2 Kiem Soat Trung Tuyen",
            "triet_ly": "Ap dao so luong o tuyen giua va co gian linh hoat theo tinh huong",
            "mo_ta": "Ba trung ve vung chac, hai cau thu chay bien len cong ve thu toan dien, hang tien ve day dac giup ap dat the tran.",
            "vi_tri": ["GK", "CB1", "CB2", "CB3", "LWB", "CDM", "CM1", "CM2", "RWB", "ST1", "ST2"]
        },
        {
            "id": "4-2-3-1",
            "ten": "4-2-3-1 Kiem Soat Hien Dai",
            "triet_ly": "Su dung 2 tien ve tru phong ngu mo neo va 1 ho cong kien thiet so 10",
            "mo_ta": "So do thinh hanh nhat bong da hien dai nho su can bang tuyet doi giua phong ngu vung vang va tan cong da dang.",
            "vi_tri": ["GK", "LB", "CB1", "CB2", "RB", "CDM1", "CDM2", "CAM", "LM", "RM", "ST"]
        },
        {
            "id": "5-3-2",
            "ten": "5-3-2 Phong Ngu Phan Cong Bien",
            "triet_ly": "Buc tuong thep nhieu lop va phan cong chop nhoang",
            "mo_ta": "5 hau ve khoa chat moi khoang trong truoc khung thanh, cho doi thoi co cuop bong va phat dong duong chuyen dai cho 2 tien dao.",
            "vi_tri": ["GK", "LWB", "CB1", "CB2", "CB3", "RWB", "CM1", "CM2", "CAM", "ST1", "ST2"]
        },
        {
            "id": "4-1-4-1",
            "ten": "4-1-4-1 Pressing Tam Cao Chuyen Doi Mau",
            "triet_ly": "Phong toa khong gian ngay tai 1/3 san doi phuong",
            "mo_ta": "Hang tien ve 4 nguoi dang cao gay suc ep lien tuc, buoc doi thu mac sai lam de ghi ban nhanh chong.",
            "vi_tri": ["GK", "LB", "CB1", "CB2", "RB", "CDM", "LM", "CM1", "CM2", "RM", "ST"]
        }
    ]

def lay_kho_cau_thu_tuyen_chon():
    """Tra ve kho du lieu 38 cau thu sieu sao the gioi va Viet Nam de hoc sinh lua chon vao doi hinh."""
    return [
        # --- THU MON (GK) ---
        {"id": "cauthu_1", "ten": "Thibaut Courtois", "vi_tri_chuan": "GK", "quoc_tich": "Bi", "pac": 60, "sho": 30, "pas": 75, "def": 92, "phy": 88, "ovr": 90},
        {"id": "cauthu_2", "ten": "Alisson Becker", "vi_tri_chuan": "GK", "quoc_tich": "Brazil", "pac": 62, "sho": 35, "pas": 85, "def": 90, "phy": 85, "ovr": 89},
        {"id": "cauthu_3", "ten": "Dang Van Lam", "vi_tri_chuan": "GK", "quoc_tich": "Viet Nam", "pac": 65, "sho": 30, "pas": 72, "def": 85, "phy": 86, "ovr": 84},
        {"id": "cauthu_24", "ten": "Manuel Neuer", "vi_tri_chuan": "GK", "quoc_tich": "Duc", "pac": 64, "sho": 40, "pas": 91, "def": 91, "phy": 87, "ovr": 90},
        {"id": "cauthu_25", "ten": "Bui Tan Truong", "vi_tri_chuan": "GK", "quoc_tich": "Viet Nam", "pac": 61, "sho": 28, "pas": 70, "def": 82, "phy": 84, "ovr": 82},

        # --- HAU VE TRUNG TAM (CB) ---
        {"id": "cauthu_4", "ten": "Virgil van Dijk", "vi_tri_chuan": "CB", "quoc_tich": "Ha Lan", "pac": 82, "sho": 60, "pas": 78, "def": 95, "phy": 92, "ovr": 92},
        {"id": "cauthu_5", "ten": "Ruben Dias", "vi_tri_chuan": "CB", "quoc_tich": "Bo Dao Nha", "pac": 78, "sho": 50, "pas": 75, "def": 93, "phy": 90, "ovr": 90},
        {"id": "cauthu_6", "ten": "Que Ngoc Hai", "vi_tri_chuan": "CB", "quoc_tich": "Viet Nam", "pac": 74, "sho": 58, "pas": 76, "def": 86, "phy": 85, "ovr": 84},
        {"id": "cauthu_26", "ten": "William Saliba", "vi_tri_chuan": "CB", "quoc_tich": "Phap", "pac": 84, "sho": 45, "pas": 77, "def": 92, "phy": 88, "ovr": 89},
        {"id": "cauthu_27", "ten": "Bui Hoang Viet Anh", "vi_tri_chuan": "CB", "quoc_tich": "Viet Nam", "pac": 76, "sho": 55, "pas": 74, "def": 84, "phy": 85, "ovr": 83},
        {"id": "cauthu_28", "ten": "Antonio Rudiger", "vi_tri_chuan": "CB", "quoc_tich": "Duc", "pac": 86, "sho": 55, "pas": 72, "def": 91, "phy": 90, "ovr": 89},

        # --- HAU VE BIEN (LB / RB / LWB / RWB) ---
        {"id": "cauthu_7", "ten": "Alphonso Davies", "vi_tri_chuan": "LB", "quoc_tich": "Canada", "pac": 96, "sho": 68, "pas": 80, "def": 82, "phy": 84, "ovr": 87},
        {"id": "cauthu_8", "ten": "Doan Van Hau", "vi_tri_chuan": "LB", "quoc_tich": "Viet Nam", "pac": 82, "sho": 70, "pas": 75, "def": 84, "phy": 87, "ovr": 84},
        {"id": "cauthu_9", "ten": "Achraf Hakimi", "vi_tri_chuan": "RB", "quoc_tich": "Maroc", "pac": 95, "sho": 76, "pas": 82, "def": 81, "phy": 83, "ovr": 88},
        {"id": "cauthu_10", "ten": "Vu Van Thanh", "vi_tri_chuan": "RB", "quoc_tich": "Viet Nam", "pac": 84, "sho": 72, "pas": 78, "def": 82, "phy": 84, "ovr": 83},
        {"id": "cauthu_29", "ten": "Joao Cancelo", "vi_tri_chuan": "RB", "quoc_tich": "Bo Dao Nha", "pac": 87, "sho": 75, "pas": 86, "def": 81, "phy": 76, "ovr": 87},
        {"id": "cauthu_30", "ten": "Trent Alexander-Arnold", "vi_tri_chuan": "RB", "quoc_tich": "Anh", "pac": 80, "sho": 77, "pas": 93, "def": 80, "phy": 76, "ovr": 88},

        # --- TIEN VE PHONG NGU & TRUNG TAM (CDM / CM) ---
        {"id": "cauthu_11", "ten": "Rodri Hernandez", "vi_tri_chuan": "CDM", "quoc_tich": "Tay Ban Nha", "pac": 76, "sho": 80, "pas": 90, "def": 92, "phy": 90, "ovr": 93},
        {"id": "cauthu_13", "ten": "Luka Modric", "vi_tri_chuan": "CM", "quoc_tich": "Croatia", "pac": 75, "sho": 82, "pas": 93, "def": 74, "phy": 76, "ovr": 90},
        {"id": "cauthu_16", "ten": "Nguyen Hoang Duc", "vi_tri_chuan": "CM", "quoc_tich": "Viet Nam", "pac": 81, "sho": 80, "pas": 86, "def": 78, "phy": 82, "ovr": 85},
        {"id": "cauthu_31", "ten": "Do Hung Dung", "vi_tri_chuan": "CM", "quoc_tich": "Viet Nam", "pac": 80, "sho": 75, "pas": 84, "def": 82, "phy": 83, "ovr": 84},
        {"id": "cauthu_32", "ten": "Nguyen Tuan Anh", "vi_tri_chuan": "CM", "quoc_tich": "Viet Nam", "pac": 78, "sho": 74, "pas": 88, "def": 77, "phy": 75, "ovr": 83},
        {"id": "cauthu_33", "ten": "Eduardo Camavinga", "vi_tri_chuan": "CDM", "quoc_tich": "Phap", "pac": 84, "sho": 70, "pas": 83, "def": 85, "phy": 85, "ovr": 87},
        {"id": "cauthu_34", "ten": "Federico Valverde", "vi_tri_chuan": "CM", "quoc_tich": "Uruguay", "pac": 90, "sho": 84, "pas": 85, "def": 82, "phy": 86, "ovr": 89},
        {"id": "cauthu_35", "ten": "Declan Rice", "vi_tri_chuan": "CDM", "quoc_tich": "Anh", "pac": 80, "sho": 72, "pas": 84, "def": 88, "phy": 87, "ovr": 88},

        # --- TIEN VE TAN CONG & CANH (CAM / LM / RM) ---
        {"id": "cauthu_12", "ten": "Kevin De Bruyne", "vi_tri_chuan": "CAM", "quoc_tich": "Bi", "pac": 78, "sho": 88, "pas": 96, "def": 68, "phy": 79, "ovr": 92},
        {"id": "cauthu_14", "ten": "Jude Bellingham", "vi_tri_chuan": "CAM", "quoc_tich": "Anh", "pac": 85, "sho": 88, "pas": 86, "def": 80, "phy": 87, "ovr": 91},
        {"id": "cauthu_15", "ten": "Nguyen Quang Hai", "vi_tri_chuan": "CAM", "quoc_tich": "Viet Nam", "pac": 80, "sho": 84, "pas": 88, "def": 65, "phy": 74, "ovr": 85},
        {"id": "cauthu_36", "ten": "Pedri Gonzalez", "vi_tri_chuan": "CAM", "quoc_tich": "Tay Ban Nha", "pac": 82, "sho": 76, "pas": 90, "def": 70, "phy": 73, "ovr": 88},
        {"id": "cauthu_37", "ten": "Phil Foden", "vi_tri_chuan": "CAM", "quoc_tich": "Anh", "pac": 88, "sho": 86, "pas": 88, "def": 60, "phy": 70, "ovr": 89},

        # --- TIEN DAO CANH & CAM (LW / RW / ST) ---
        {"id": "cauthu_17", "ten": "Cristiano Ronaldo", "vi_tri_chuan": "ST", "quoc_tich": "Bo Dao Nha", "pac": 86, "sho": 94, "pas": 82, "def": 40, "phy": 88, "ovr": 93},
        {"id": "cauthu_18", "ten": "Lionel Messi", "vi_tri_chuan": "RW", "quoc_tich": "Argentina", "pac": 84, "sho": 92, "pas": 95, "def": 38, "phy": 72, "ovr": 93},
        {"id": "cauthu_19", "ten": "Kylian Mbappe", "vi_tri_chuan": "LW", "quoc_tich": "Phap", "pac": 97, "sho": 92, "pas": 84, "def": 42, "phy": 80, "ovr": 93},
        {"id": "cauthu_20", "ten": "Erling Haaland", "vi_tri_chuan": "ST", "quoc_tich": "Na Uy", "pac": 91, "sho": 95, "pas": 70, "def": 48, "phy": 92, "ovr": 92},
        {"id": "cauthu_21", "ten": "Vinicius Junior", "vi_tri_chuan": "LW", "quoc_tich": "Brazil", "pac": 96, "sho": 86, "pas": 82, "def": 35, "phy": 74, "ovr": 90},
        {"id": "cauthu_22", "ten": "Nguyen Tien Linh", "vi_tri_chuan": "ST", "quoc_tich": "Viet Nam", "pac": 81, "sho": 85, "pas": 72, "def": 44, "phy": 83, "ovr": 84},
        {"id": "cauthu_23", "ten": "Huynh Nhu", "vi_tri_chuan": "ST", "quoc_tich": "Viet Nam", "pac": 83, "sho": 86, "pas": 80, "def": 46, "phy": 78, "ovr": 85},
        {"id": "cauthu_38", "ten": "Lamine Yamal", "vi_tri_chuan": "RW", "quoc_tich": "Tay Ban Nha", "pac": 92, "sho": 82, "pas": 86, "def": 40, "phy": 68, "ovr": 87},
        {"id": "cauthu_39", "ten": "Bukayo Saka", "vi_tri_chuan": "RW", "quoc_tich": "Anh", "pac": 89, "sho": 85, "pas": 84, "def": 65, "phy": 78, "ovr": 88},
        {"id": "cauthu_40", "ten": "Son Heung-min", "vi_tri_chuan": "LW", "quoc_tich": "Han Quoc", "pac": 88, "sho": 89, "pas": 83, "def": 45, "phy": 75, "ovr": 88},
        {"id": "cauthu_41", "ten": "Nguyen Van Toan", "vi_tri_chuan": "RW", "quoc_tich": "Viet Nam", "pac": 90, "sho": 78, "pas": 76, "def": 50, "phy": 72, "ovr": 82}
    ]

def khoi_tao_doi_hinh_mac_dinh():
    """Khoi tao doi hinh mac dinh 4-3-3 voi cac sieu sao hang dau."""
    return {
        "so_do": "4-3-3",
        "ten_doi_bong": "Dream Team EduVerse",
        "danh_sach_da_chinh": {
            "GK": "cauthu_1",     # Thibaut Courtois
            "LB": "cauthu_7",     # Alphonso Davies
            "CB1": "cauthu_4",    # Virgil van Dijk
            "CB2": "cauthu_5",    # Ruben Dias
            "RB": "cauthu_9",     # Achraf Hakimi
            "CDM": "cauthu_11",   # Rodri Hernandez
            "CM": "cauthu_13",    # Luka Modric
            "CAM": "cauthu_15",   # Nguyen Quang Hai
            "LW": "cauthu_19",    # Kylian Mbappe
            "ST": "cauthu_17",    # Cristiano Ronaldo
            "RW": "cauthu_18"     # Lionel Messi
        },
        "diem_nang_cap_tich_luy": 120
    }

def doc_doi_hinh_hien_tai():
    """Doc du lieu doi hinh tu file JSON, neu chua co thi tao moi."""
    if not os.path.exists(FILE_DOI_HINH):
        du_lieu = khoi_tao_doi_hinh_mac_dinh()
        try:
            luu_doi_hinh_hien_tai(du_lieu)
        except Exception:
            pass
        return du_lieu
    try:
        with open(FILE_DOI_HINH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        du_lieu = khoi_tao_doi_hinh_mac_dinh()
        return du_lieu

def luu_doi_hinh_hien_tai(du_lieu):
    """Luu du lieu doi hinh xuong file JSON."""
    try:
        os.makedirs(os.path.dirname(FILE_DOI_HINH), exist_ok=True)
        with open(FILE_DOI_HINH, "w", encoding="utf-8") as f:
            json.dump(du_lieu, f, ensure_ascii=False, indent=2)
        return True
    except Exception:
        return False

def tinh_suc_manh_tong_hop(doi_hinh_dict):
    """
    Tinh diem suc manh tong hop (Team Overall Rating) cua 11 cau thu tren san.
    Cong them diem cong huong vi tri neu cau thu duoc xep dung vi tri so truong.
    """
    kho = {c["id"]: c for c in lay_kho_cau_thu_tuyen_chon()}
    da_chinh = doi_hinh_dict.get("danh_sach_da_chinh", {})
    if not da_chinh:
        return 85
    
    tong_ovr = 0
    dem = 0
    diem_cong_huong = 0

    for pos, cid in da_chinh.items():
        if cid in kho:
            ct = kho[cid]
            base_ovr = ct["ovr"]
            # Kiem tra vi tri so truong
            vi_tri_chuan = ct.get("vi_tri_chuan", "")
            # So khop linh hoat (vi du CB1, CB2 deu khop voi CB)
            if vi_tri_chuan in pos or pos.startswith(vi_tri_chuan):
                diem_cong_huong += 0.5
            tong_ovr += base_ovr
            dem += 1
    
    if dem == 0:
        return 85
    
    trung_binh = (tong_ovr / dem) + min(diem_cong_huong / dem, 2.0)
    return round(trung_binh, 1)

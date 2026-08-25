# Thu muc: xu_ly_tro_choi
# File: quan_ly_gap_thu_moi.py
# Mo ta: Thuat toan backend va quan ly he thong May Gap Thu 3D da tinh nang va tich luy ve gap tu hoc tap sang Tieng Viet co dau

import os
import json
import random
from xu_ly_hoc_tap.he_thong_thuong import cong_phan_thuong

DUONG_DAN_GAP_THU = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "du_lieu", "he_thong_gap_thu.json"))

CAC_MAY_GAP = {
    "cute": {"id": "cute", "ten": "Máy 1 - Cute Claw", "level_yeu_cau": 1, "mo_ta": "Máy gắp dễ thương miễn phí từ Level 1"},
    "dino": {"id": "dino", "ten": "Máy 2 - Dino Claw", "level_yeu_cau": 5, "mo_ta": "Máy gắp chủ đề Khủng Long mở ở Level 5"},
    "football": {"id": "football", "ten": "Máy 3 - Football Claw", "level_yeu_cau": 10, "mo_ta": "Máy gắp Đấu trường Bóng đá mở ở Level 10"},
    "future": {"id": "future", "ten": "Máy 4 - Future Claw", "level_yeu_cau": 20, "mo_ta": "Máy gắp Robot Tương lai mở ở Level 20"},
    "galaxy": {"id": "galaxy", "ten": "Máy 5 - Galaxy Claw", "level_yeu_cau": 30, "mo_ta": "Máy gắp Vũ trụ Galaxy mở ở Level 30"},
    "golden": {"id": "golden", "ten": "Máy 6 - Golden Machine", "level_yeu_cau": 50, "mo_ta": "Máy gắp Hoàng Gia chỉ chứa vật phẩm Hiếm đến Bí Mật"}
}

DANH_MUC_BO_SUU_TAP = {
    "animal": {
        "ten": "Animal Collection",
        "danh_sach": ["Gấu Bông", "Mèo Con", "Chó Con", "Cáo Tinh Anh", "Panda Trí Tuệ"],
        "thuong_xp": 1000
    },
    "dinosaur": {
        "ten": "Dinosaur Collection",
        "danh_sach": ["T-Rex", "Triceratops", "Raptor"],
        "thuong_xp": 1000
    },
    "robot": {
        "ten": "Robot Collection",
        "danh_sach": ["Robot Đỏ", "Robot Xanh", "Mecha Chiến Đấu"],
        "thuong_xp": 1000
    },
    "football": {
        "ten": "Football Collection",
        "danh_sach": ["Bóng Vàng", "Găng Thủ Môn", "Mascot Bóng Đá"],
        "thuong_xp": 1000
    },
    "galaxy": {
        "ten": "Galaxy Collection",
        "danh_sach": ["Galaxy Cat", "Space Bear", "Cosmic Dragon", "Nebula Fox", "Star Robot"],
        "thuong_xp": 2000
    }
}

DANH_SACH_VAT_PHAM = {
    "thuong": [
        {"ten": "Gấu Bông", "bo": "animal", "xp": 50, "coin": 0},
        {"ten": "Mèo Con", "bo": "animal", "xp": 50, "coin": 0},
        {"ten": "Chó Con", "bo": "animal", "xp": 50, "coin": 0}
    ],
    "hiem": [
        {"ten": "Cáo Tinh Anh", "bo": "animal", "xp": 150, "coin": 20},
        {"ten": "Panda Trí Tuệ", "bo": "animal", "xp": 150, "coin": 20},
        {"ten": "Khủng Long Nhỏ", "bo": "dinosaur", "xp": 150, "coin": 20},
        {"ten": "Triceratops", "bo": "dinosaur", "xp": 150, "coin": 20},
        {"ten": "Raptor", "bo": "dinosaur", "xp": 150, "coin": 20}
    ],
    "sieu_hiem": [
        {"ten": "T-Rex", "bo": "dinosaur", "xp": 300, "coin": 50},
        {"ten": "Robot Đỏ", "bo": "robot", "xp": 300, "coin": 50},
        {"ten": "Robot Xanh", "bo": "robot", "xp": 300, "coin": 50},
        {"ten": "Bóng Vàng", "bo": "football", "xp": 300, "coin": 50},
        {"ten": "Găng Thủ Môn", "bo": "football", "xp": 300, "coin": 50}
    ],
    "huyen_thoai": [
        {"ten": "Mecha Chiến Đấu", "bo": "robot", "xp": 600, "coin": 100},
        {"ten": "Mascot Bóng Đá", "bo": "football", "xp": 600, "coin": 100},
        {"ten": "Galaxy Cat", "bo": "galaxy", "xp": 600, "coin": 100},
        {"ten": "Space Bear", "bo": "galaxy", "xp": 600, "coin": 100}
    ],
    "bi_mat": [
        {"ten": "Cosmic Dragon", "bo": "galaxy", "xp": 1200, "coin": 300},
        {"ten": "Nebula Fox", "bo": "galaxy", "xp": 1200, "coin": 300},
        {"ten": "Star Robot", "bo": "galaxy", "xp": 1200, "coin": 300},
        {"ten": "Golden Capsule Thưởng", "bo": "galaxy", "xp": 1500, "coin": 500}
    ]
}

def lay_du_lieu_gap_thu():
    """Tải thông tin cấu hình tài sản vé gắp và bộ sưu tập."""
    import datetime
    today_str = datetime.date.today().isoformat()

    if not os.path.exists(DUONG_DAN_GAP_THU):
        data_default = {
            "ve_gap": 5,
            "ve_vang": 5,
            "level": 1,
            "combo_streak": 0,
            "super_claw": False,
            "may_hien_tai": "cute",
            "may_da_mo_khoa": ["cute"],
            "bo_suu_tap": {
                "animal": [],
                "dinosaur": [],
                "robot": [],
                "football": [],
                "galaxy": []
            },
            "ngay_nhan_ve": today_str,
            "nhiem_vu_ngay": {
                "hoan_thanh_bai_hoc": False,
                "dung_10_cau_lien_tiep": False,
                "nhiem_vu_ngay_xong": False
            }
        }
        luu_du_lieu_gap_thu(data_default)
        return data_default
    try:
        import datetime
        today_str = datetime.date.today().isoformat()
        with open(DUONG_DAN_GAP_THU, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Kiem tra diem danh ngay moi -> Cong 3 Ve Thường + 1 Ve Vang
            if data.get("ngay_nhan_ve") != today_str:
                data["ve_gap"] = max(5, data.get("ve_gap", 0) + 3)
                data["ve_vang"] = max(5, data.get("ve_vang", 0) + 1)
                data["ngay_nhan_ve"] = today_str
                luu_du_lieu_gap_thu(data)
            return data
    except Exception:
        return {
            "ve_gap": 5, "ve_vang": 5, "level": 1, "combo_streak": 0, "super_claw": False,
            "may_hien_tai": "cute", "may_da_mo_khoa": ["cute"],
            "bo_suu_tap": {"animal": [], "dinosaur": [], "robot": [], "football": [], "galaxy": []},
            "ngay_nhan_ve": "",
            "nhiem_vu_ngay": {"hoan_thanh_bai_hoc": False, "dung_10_cau_lien_tiep": False, "nhiem_vu_ngay_xong": False}
        }

def luu_du_lieu_gap_thu(data):
    """Lưu trữ thông tin máy gắp thú vào file JSON."""
    try:
        thu_muc = os.path.dirname(DUONG_DAN_GAP_THU)
        if not os.path.exists(thu_muc):
            os.makedirs(thu_muc)
        with open(DUONG_DAN_GAP_THU, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except Exception:
        return False

def cong_ve_gap_tu_hoc_tap(loai_hieu_suat="bai_hoc"):
    """Tự động thưởng Vé Gắp hoặc Vé Vàng khi học sinh đạt thành tích học tập."""
    data = lay_du_lieu_gap_thu()
    msg = ""
    if loai_hieu_suat == "bai_hoc":
        data["ve_gap"] += 1
        msg = "Chúc mừng em đã hoàn thành Bài học! Nhận ngay +1 Vé Gắp!"
    elif loai_hieu_suat == "dung_10_cau":
        data["ve_gap"] += 1
        msg = "Chúc mừng em đã trả lời đúng 10 câu liên tiếp! Nhận ngay +1 Vé Gắp!"
    elif loai_hieu_suat == "nhiem_vu_ngay":
        data["ve_gap"] += 2
        msg = "Chúc mừng em hoàn thành Nhiệm vụ ngày! Nhận ngay +2 Vé Gắp!"
    elif loai_hieu_suat == "ve_vang" or loai_hieu_suat == "diem_10":
        data["ve_vang"] += 1
        msg = "Xuất sắc! Đạt thành tích cao học tập! Nhận ngay +1 VÉ VÀNG (Golden Ticket)!"
    
    luu_du_lieu_gap_thu(data)
    return msg, data["ve_gap"], data["ve_vang"]

def thuc_hien_luot_gap_moi(may_id="cute", su_dung_ve_vang=False):
    """
    Xử lý thuật toán 1 lượt gắp thú:
    - Trừ vé gắp tương ứng.
    - Tính toán tỉ lệ Rarity ngẫu nhiên có trọng số.
    - Tính điểm Combo và kích hoạt Super Claw.
    - Cập nhật Bộ sưu tập.
    """
    data = lay_du_lieu_gap_thu()

    # Kiểm tra số lượng vé
    if su_dung_ve_vang or may_id == "golden":
        if data["ve_vang"] < 1:
            return False, "Bạn không có đủ VÉ VÀNG (Golden Ticket) để tham gia Máy Vàng!", data
        data["ve_vang"] -= 1
    else:
        if data["ve_gap"] < 1:
            return False, "Bạn đã hết Vé Gắp! Hãy hoàn thành bài học để kiếm thêm vé nhé!", data
        data["ve_gap"] -= 1

    # Cập nhật level và máy đã mở khóa
    user_level = data.get("level", 1)
    for mid, mobj in CAC_MAY_GAP.items():
        if user_level >= mobj["level_yeu_cau"] and mid not in data["may_da_mo_khoa"]:
            data["may_da_mo_khoa"].append(mid)

    # Tính tỉ lệ rớt thú: 50% rớt thú giữa chừng (Trừ khi Super Claw hoặc Vé Vàng)
    ti_le_rot = 50 if not (su_dung_ve_vang or may_id == "golden" or data.get("super_claw")) else 10
    if random.random() * 100 < ti_le_rot:
        data["combo_streak"] = 0
        data["super_claw"] = False
        luu_du_lieu_gap_thu(data)
        return True, {
            "rot_thu": True,
            "tier": "none",
            "nhan_rarity": "[TRƯỢT RỚT]",
            "item": "Không có",
            "xp": 0,
            "coin": 0,
            "combo": 0,
            "super_claw": False,
            "thong_bao": "Rất tiếc! Tay gắp bị trượt rớt thú giữa chừng (Tỉ lệ rớt 50%). Hãy căn chỉnh chuẩn và thử lại nhé!",
            "ve_gap": data["ve_gap"],
            "ve_vang": data["ve_vang"]
        }, data

    # Roll tỉ lệ Rarity
    if su_dung_ve_vang or may_id == "golden":
        # Tỉ lệ Máy Vàng: Hiếm 40%, Siêu Hiếm 35%, Huyền Thoại 20%, Bí Mật 5%
        roll = random.random() * 100
        if roll < 40: tier = "hiem"
        elif roll < 75: tier = "sieu_hiem"
        elif roll < 95: tier = "huyen_thoai"
        else: tier = "bi_mat"
    else:
        # Tỉ lệ Máy Thường: Thường 50%, Hiếm 28%, Siêu Hiếm 15%, Huyền Thoại 6%, Bí Mật 1%
        roll = random.random() * 100
        if roll < 50: tier = "thuong"
        elif roll < 78: tier = "hiem"
        elif roll < 93: tier = "sieu_hiem"
        elif roll < 99: tier = "huyen_thoai"
        else: tier = "bi_mat"

    vat_pham = random.choice(DANH_SACH_VAT_PHAM[tier])
    ten_item = vat_pham["ten"]
    bo_id = vat_pham["bo"]
    xp_goc = vat_pham["xp"]
    coin_goc = vat_pham["coin"]

    # Xử lý Combo Streak
    data["combo_streak"] += 1
    he_so_combo = 1.0
    if data["combo_streak"] == 2:
        he_so_combo = 1.2
    elif data["combo_streak"] == 3:
        he_so_combo = 1.5
    elif data["combo_streak"] >= 5:
        he_so_combo = 2.0
        data["super_claw"] = True

    xp_thuc_te = int(xp_goc * he_so_combo)
    coin_thuc_te = int(coin_goc * he_so_combo)

    # Thưởng cho người dùng
    cong_phan_thuong(xp_thuc_te)

    # Cập nhật Bộ sưu tập
    danh_sach_bo = data["bo_suu_tap"].get(bo_id, [])
    mo_khoa_moi = False
    if ten_item not in danh_sach_bo:
        danh_sach_bo.append(ten_item)
        data["bo_suu_tap"][bo_id] = danh_sach_bo
        mo_khoa_moi = True

    # Kiểm tra hoàn thành Bộ sưu tập
    thong_bao_bo = ""
    if bo_id in DANH_MUC_BO_SUU_TAP:
        bo_info = DANH_MUC_BO_SUU_TAP[bo_id]
        if len(danh_sach_bo) == len(bo_info["danh_sach"]):
            cong_phan_thuong(bo_info["thuong_xp"])
            thong_bao_bo = f" HOÀN THÀNH {bo_info['ten'].upper()}! Nhận thêm +{bo_info['thuong_xp']} XP!"

    luu_du_lieu_gap_thu(data)

    nhan_rarity = {
        "thuong": "[THƯỜNG]",
        "hiem": "[HIẾM]",
        "sieu_hiem": "[SIÊU HIẾM]",
        "huyen_thoai": "[HUYỀN THOẠI]",
        "bi_mat": "[BÍ MẬT - GOLDEN]"
    }

    thong_bao_ket_qua = f"GẮP THÀNH CÔNG {nhan_rarity[tier]} '{ten_item}'! Thưởng +{xp_thuc_te} XP (Combo {data['combo_streak']}x)!{thong_bao_bo}"

    return True, {
        "tier": tier,
        "nhan_rarity": nhan_rarity[tier],
        "item": ten_item,
        "bo_suu_tap": bo_id,
        "xp": xp_thuc_te,
        "coin": coin_thuc_te,
        "combo": data["combo_streak"],
        "super_claw": data["super_claw"],
        "mo_khoa_moi": mo_khoa_moi,
        "thong_bao": thong_bao_ket_qua,
        "ve_gap": data["ve_gap"],
        "ve_vang": data["ve_vang"]
    }, data

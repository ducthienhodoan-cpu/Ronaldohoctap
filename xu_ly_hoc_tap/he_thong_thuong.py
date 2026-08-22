# Thu muc: xu_ly_hoc_tap
# File: he_thong_thuong.py
# Mo ta: Quan ly phan thuong Gamification (XP, Coin, Level, Huy hieu, Danh hieu) sang Tieng Viet co dau

import json
import os

FILE_THUONG = "he_thong_thuong.json"

def lay_thong_tin_thuong():
    """Lấy thông tin điểm kinh nghiệm, xu, level và huy hiệu của học sinh chuẩn Tiếng Việt có dấu."""
    if not os.path.exists(FILE_THUONG):
        thong_tin_mac_dinh = {
            "xp": 150,
            "coin": 50,
            "level": 2,
            "danh_hieu": "Học sinh Tích cực",
            "danh_sach_huy_hieu": ["Huy hiệu Khởi đầu", "Huy hiệu Siêng năng"]
        }
        luu_thong_tin_thuong(thong_tin_mac_dinh)
        return thong_tin_mac_dinh
    
    try:
        with open(FILE_THUONG, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {
            "xp": 100,
            "coin": 20,
            "level": 1,
            "danh_hieu": "Tân binh EduVerse",
            "danh_sach_huy_hieu": ["Huy hiệu Khởi đầu"]
        }

def luu_thong_tin_thuong(du_lieu):
    """Lưu thông tin phần thưởng vào file JSON local."""
    try:
        with open(FILE_THUONG, "w", encoding="utf-8") as f:
            json.dump(du_lieu, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print("Lỗi khi lưu hệ thống thưởng:", e)

def cong_phan_thuong(diem_so=0, so_cau_dung=None):
    """Cộng XP và Coin dựa trên kết quả bài làm hoặc cộng điểm XP trực tiếp mà không bị TypeError/ValueError."""
    du_lieu = lay_thong_tin_thuong()
    
    if so_cau_dung is None or not isinstance(so_cau_dung, (int, float)):
        # Nếu chỉ truyền 1 tham số (vd: cong_phan_thuong(100)) hoặc so_cau_dung là chuỗi, coi diem_so là XP trực tiếp
        try:
            xp_nhan = int(diem_so)
        except Exception:
            xp_nhan = 50
        coin_nhan = max(1, xp_nhan // 5)
    else:
        xp_nhan = int(so_cau_dung * 10)
        coin_nhan = int(so_cau_dung * 2)
    
    du_lieu["xp"] += xp_nhan
    du_lieu["coin"] += coin_nhan
    
    # Cập nhật level (mỗi 200 XP lên 1 Level)
    level_moi = (du_lieu["xp"] // 200) + 1
    if level_moi > du_lieu["level"]:
        du_lieu["level"] = level_moi
        du_lieu["danh_sach_huy_hieu"].append(f"Huy hiệu Cấp độ {level_moi}")
        
    # Cập nhật danh hiệu
    if du_lieu["level"] >= 5:
        du_lieu["danh_hieu"] = "Chuyên gia EduVerse"
    elif du_lieu["level"] >= 3:
        du_lieu["danh_hieu"] = "Học sinh Xuất sắc"
        
    luu_thong_tin_thuong(du_lieu)
    return xp_nhan, coin_nhan

def cong_xp_truc_tiep(xp_cong, coin_cong=0):
    """Cộng trực tiếp XP và Coin vào tài khoản học sinh."""
    return cong_phan_thuong(diem_so=xp_cong, so_cau_dung=None)


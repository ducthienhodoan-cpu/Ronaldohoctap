# Thu muc: xu_ly_tro_choi
# File: quan_ly_obby.py
# Mo ta: Logic xu ly dau truong Obby 100 Man Parkour Vuot Chuong Ngoai Vat Glitch World

import os
import json

FILE_TIEN_DO_OBBY = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "du_lieu", "tien_do_obby.json"))

def lay_danh_sach_10_world():
    """Tra ve danh sach 10 World Obby va co che dac biet."""
    return [
        {"id": 1, "ten": "World 1 - Glitch City", "vong": "Màn 1-10", "co_che": "Obby co ban, con duong vo, xe chay, san sap, Glitch Portal", "core_id": 1},
        {"id": 2, "ten": "World 2 - Lava Factory", "vong": "Màn 11-20", "co_che": "Dung nham, ong hoi nuoc, bang chuyen, may ep, Lava Rise", "core_id": 2},
        {"id": 3, "ten": "World 3 - Frozen Mountain", "vong": "Màn 21-30", "co_che": "Bang trut, cau tuyet lan, bao tuyet, cau vo", "core_id": 3},
        {"id": 4, "ten": "World 4 - Poison Jungle", "vong": "Màn 31-40", "co_che": "La khong lo, du day, cay an thit, dam doc", "core_id": 4},
        {"id": 5, "ten": "World 5 - Flooded City", "vong": "Màn 41-50", "co_che": "Nuoc dang, song lon, duong ong, Tsunami Escape", "core_id": 5},
        {"id": 6, "ten": "World 6 - Space Station", "vong": "Màn 51-60", "co_che": "Trong luc thap, Gravity Switch, thien thach, ve tinh", "core_id": 6},
        {"id": 7, "ten": "World 7 - Robot Factory", "vong": "Màn 61-70", "co_che": "Bang chuyen toc do cao, tay robot, banh rang, Mini Boss Robot", "core_id": 7},
        {"id": 8, "ten": "World 8 - Time World", "vong": "Màn 71-80", "co_che": "Platform 2s bien mat, Time Stop, banh rang dong ho", "core_id": 8},
        {"id": 9, "ten": "World 9 - Cyber World", "vong": "Màn 81-90", "co_che": "Ban phim khong lo, mach dien, duong ham du lieu, Virus Chase", "core_id": 9},
        {"id": 10, "ten": "World 10 - Glitch Core", "vong": "Màn 91-100", "co_che": "Tong hop co che, Man 99 Final Run, Man 100 Boss Glitch-X 3 Phase", "core_id": 10}
    ]

def lay_thong_tin_man_obby(so_man):
    """Tra ve thong tin co che va chuong ngoai vat cua man choi bat ky tu 1 den 100."""
    so_man = max(1, min(100, int(so_man)))
    world_id = ((so_man - 1) // 10) + 1
    danh_sach_world = lay_danh_sach_10_world()
    world_info = danh_sach_world[world_id - 1]

    # Ten man va mo ta chi tiet
    ten_man = f"Màn {so_man}"
    is_checkpoint = (so_man % 10 == 0)
    is_boss = (so_man == 100)

    return {
        "so_man": so_man,
        "ten_man": ten_man,
        "world_id": world_id,
        "ten_world": world_info["ten"],
        "co_che": world_info["co_che"],
        "is_checkpoint": is_checkpoint,
        "is_boss": is_boss,
        "thoi_gian_lim": 90 if is_boss else (60 if is_checkpoint else 45),
        "thuong_xp": 500 if is_boss else (200 if is_checkpoint else 50)
    }

def doc_tien_do_obby():
    """Doc tien do Checkpoint va Glitch Core nguoi dung da mo khoa."""
    if not os.path.exists(FILE_TIEN_DO_OBBY):
        du_lieu_mac_dinh = {
            "man_hien_tai": 1,
            "man_cao_nhat": 1,
            "cores_da_lay": [],
            "hard_mode_unlocked": False
        }
        ghi_tien_do_obby(du_lieu_mac_dinh)
        return du_lieu_mac_dinh

    try:
        with open(FILE_TIEN_DO_OBBY, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"man_hien_tai": 1, "man_cao_nhat": 1, "cores_da_lay": [], "hard_mode_unlocked": False}

def ghi_tien_do_obby(du_lieu):
    """Ghi tien do Obby vao tệp json du lieu."""
    try:
        os.makedirs(os.path.dirname(FILE_TIEN_DO_OBBY), exist_ok=True)
        with open(FILE_TIEN_DO_OBBY, "w", encoding="utf-8") as f:
            json.dump(du_lieu, f, ensure_ascii=False, indent=4)
    except Exception:
        pass

def luu_hoan_thanh_man_obby(so_man):
    """Luu ket qua qua man Obby va cong Glitch Core neu o Checkpoint."""
    tiendo = doc_tien_do_obby()
    so_man = int(so_man)
    
    if so_man >= tiendo.get("man_cao_nhat", 1):
        tiendo["man_cao_nhat"] = min(100, so_man + 1)
    
    tiendo["man_hien_tai"] = min(100, so_man + 1)

    # Cong Glitch Core o cac man 10, 20, 30...
    if so_man % 10 == 0:
        core_id = so_man // 10
        cores = tiendo.get("cores_da_lay", [])
        if core_id not in cores:
            cores.append(core_id)
            tiendo["cores_da_lay"] = cores

    if so_man == 100:
        tiendo["hard_mode_unlocked"] = True

    ghi_tien_do_obby(tiendo)
    return tiendo

# Thu muc: xu_ly_co_tri_tue
# File: quan_ly_ban_co.py
# Mo ta: Quan ly du lieu ban co mau, the co chien thuat va tien do giai do co hoc cua hoc sinh

import os
import json

DUONG_DAN_TIEN_DO = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "du_lieu", "tien_do_co_tri_tue.json")
)

def khoi_tao_ban_co_vua_mac_dinh():
    """
    Tra ve mang 8x8 dai dien cho ban co vua tieu chuan luc bat dau tran.
    Cac chu cai in hoa dai dien cho quan Trang, chu thuong dai dien cho quan Den:
    R/r: Xe, N/n: Ma, B/b: Tuong, Q/q: Hau, K/k: Vua, P/p: Tot, '': O trong.
    """
    ban_co = [
        ["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "N", "B", "Q", "K", "B", "N", "R"]
    ]
    return ban_co

def khoi_tao_ban_co_tuong_mac_dinh():
    """
    Tra ve mang 10 hang x 9 cot dai dien cho ban co tuong tieu chuan luc bat dau tran.
    Tien to R_ (Do - Red) va B_ (Den - Black):
    TG: Tuong/Soai, SI: Si, TU: Tuong/Voi, MA: Ma, XE: Xe, PH: Phao, TO: Tot/Binh.
    """
    ban_co = [["" for _ in range(9)] for _ in range(10)]
    
    # Quan Den (hang 0 den 3)
    ban_co[0] = ["B_XE", "B_MA", "B_TU", "B_SI", "B_TG", "B_SI", "B_TU", "B_MA", "B_XE"]
    ban_co[2][1] = "B_PH"
    ban_co[2][7] = "B_PH"
    ban_co[3][0] = "B_TO"
    ban_co[3][2] = "B_TO"
    ban_co[3][4] = "B_TO"
    ban_co[3][6] = "B_TO"
    ban_co[3][8] = "B_TO"
    
    # Quan Do (hang 6 den 9)
    ban_co[6][0] = "R_TO"
    ban_co[6][2] = "R_TO"
    ban_co[6][4] = "R_TO"
    ban_co[6][6] = "R_TO"
    ban_co[6][8] = "R_TO"
    ban_co[7][1] = "R_PH"
    ban_co[7][7] = "R_PH"
    ban_co[9] = ["R_XE", "R_MA", "R_TU", "R_SI", "R_TG", "R_SI", "R_TU", "R_MA", "R_XE"]
    
    return ban_co

def lay_danh_sach_the_co_mau():
    """
    Tra ve danh sach cac the co tieu bieu minh hoa chien thuat thuc te
    giup hoc sinh de dang quan sat va hoc hoi.
    """
    return [
        {
            "id": "the_cv_1",
            "loai": "co_vua",
            "tieu_de": "The co Don Chia Doi cua Ma Trang",
            "mo_ta": "Ma Trang o o c7 chieu Vua Den dong thoi bat quan Xe Den o a8.",
            "loi_khuyen": "Khi choi, luon quan sat cac o ma quan Ma co the nhay vao de khong bi dinh don chia doi.",
            "ben_di_truoc": "Quan Trang (White)",
            "nuoc_tiep_theo": "Vua Den phai di chuyen tranh chieu, Ma Trang an Xe Den o a8 thu ve 5 diem."
        },
        {
            "id": "the_cv_2",
            "loai": "co_vua",
            "tieu_de": "The Chieu Het Hoc Gia (Scholar's Mate)",
            "mo_ta": "Hau Trang o f7 chieu het Vua Den nho su bao ve cua Tuong Trang o c4.",
            "loi_khuyen": "Diem yeu f7 chi co Vua bao ve trong khai cuoc. Den can phat trien Ma len f6 de ngan Hau tiep can.",
            "ben_di_truoc": "Quan Trang (White)",
            "nuoc_tiep_theo": "Hau Trang an vao f7 chieu het trong 4 nuoc neu Den khong phong thu dung cach."
        },
        {
            "id": "the_ct_1",
            "loai": "co_tuong",
            "tieu_de": "Sat Phap Ma Hau Phao Tuyeet Ky",
            "mo_ta": "Ma Do khoa cua thoat cua Tuong Den, Phao Do dung phia sau Ma chieu thang mat Tuong.",
            "loi_khuyen": "Canh giac cao do khi thay Ma va Phao doi phuong tap trung cung mot huong tan cong.",
            "ben_di_truoc": "Quan Do (Red)",
            "nuoc_tiep_theo": "Tuong Den khong the chay vi Ma can duong, khong an duoc Phao vi o xa, ket thuc van co."
        },
        {
            "id": "the_ct_2",
            "loai": "co_tuong",
            "tieu_de": "Song Xe Toa Thanh Pha Cung",
            "mo_ta": "Hai Xe Do chim xuong hang day va hang ap day cua Cuu Cung doi phuong.",
            "loi_khuyen": "Giua vung hang Si va Tieu Tuong la phong tuyen song con de ngan chan Xe doi phuong ap sat.",
            "ben_di_truoc": "Quan Do (Red)",
            "nuoc_tiep_theo": "Xe 1 chieu Tuong len, Xe 2 ap sat chieu dut diem khong cho Tuong quay ve."
        }
    ]

def doc_tien_do_co_tri_tue():
    """Doc file tien do giai do the co cua hoc sinh."""
    if not os.path.exists(DUONG_DAN_TIEN_DO):
        mac_dinh = {
            "cau_da_giai": [],
            "tong_diem_exp": 0,
            "danh_hieu": "Ky Thu Tap Su",
            "so_cau_dung": 0,
            "so_cau_sai": 0
        }
        return mac_dinh
    try:
        with open(DUONG_DAN_TIEN_DO, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {
            "cau_da_giai": [],
            "tong_diem_exp": 0,
            "danh_hieu": "Ky Thu Tap Su",
            "so_cau_dung": 0,
            "so_cau_sai": 0
        }

def luu_tien_do_co_tri_tue(du_lieu):
    """Ghi du lieu tien do giai do co vao file JSON an toan."""
    try:
        os.makedirs(os.path.dirname(DUONG_DAN_TIEN_DO), exist_ok=True)
        with open(DUONG_DAN_TIEN_DO, "w", encoding="utf-8") as f:
            json.dump(du_lieu, f, ensure_ascii=False, indent=4)
        return True
    except Exception:
        return False

def xu_ly_tra_loi_cau_do(id_cau_hoi, dap_an_chon):
    """
    Xu ly cham dap an cau do the co (co vua hoac co tuong).
    Neu dung: cong 30 XP, 15 Coin va cap nhat danh hieu ky thu.
    """
    from xu_ly_co_tri_tue.quan_ly_co_vua import lay_kho_cau_do_co_vua
    from xu_ly_co_tri_tue.quan_ly_co_tuong import lay_kho_cau_do_co_tuong
    
    tat_ca_cau_do = lay_kho_cau_do_co_vua() + lay_kho_cau_do_co_tuong()
    cau_tim_thay = None
    for c in tat_ca_cau_do:
        if c["id"] == id_cau_hoi:
            cau_tim_thay = c
            break
            
    if not cau_tim_thay:
        return {"thanh_cong": False, "thong_bao": "Khong tim thay cau hoi hop le."}
        
    dung = (dap_an_chon.strip().upper() == cau_tim_thay["dap_an_dung"].strip().upper())
    
    tien_do = doc_tien_do_co_tri_tue()
    xp_nhan = 0
    coin_nhan = 0
    
    if dung:
        if id_cau_hoi not in tien_do.get("cau_da_giai", []):
            tien_do["cau_da_giai"].append(id_cau_hoi)
            xp_nhan = 30
            coin_nhan = 15
            tien_do["tong_diem_exp"] = tien_do.get("tong_diem_exp", 0) + xp_nhan
            tien_do["so_cau_dung"] = tien_do.get("so_cau_dung", 0) + 1
            
            # Tich hop he thong thuong chung cua ung dung
            try:
                from xu_ly_hoc_tap.he_thong_thuong import cong_phan_thuong
                cong_phan_thuong(diem_so=10.0, so_cau_dung=1)
            except Exception:
                pass
        else:
            xp_nhan = 5
            coin_nhan = 2
            
        # Cap nhat danh hieu
        so_dung = len(tien_do.get("cau_da_giai", []))
        if so_dung >= 8:
            tien_do["danh_hieu"] = "Dai Kien Tuong Hoc Duong"
        elif so_dung >= 5:
            tien_do["danh_hieu"] = "Kien Tuong Tre Tuoi"
        elif so_dung >= 2:
            tien_do["danh_hieu"] = "Ky Thu Nhi Tri Tue"
        else:
            tien_do["danh_hieu"] = "Ky Thu Tap Su"
            
        luu_tien_do_co_tri_tue(tien_do)
        return {
            "thanh_cong": True,
            "ket_qua": "Dung",
            "giai_thich": cau_tim_thay["giai_thich"],
            "xp_nhan": xp_nhan,
            "coin_nhan": coin_nhan,
            "danh_hieu": tien_do["danh_hieu"],
            "tong_exp": tien_do["tong_diem_exp"]
        }
    else:
        tien_do["so_cau_sai"] = tien_do.get("so_cau_sai", 0) + 1
        luu_tien_do_co_tri_tue(tien_do)
        return {
            "thanh_cong": True,
            "ket_qua": "Sai",
            "dap_an_dung": cau_tim_thay["dap_an_dung"],
            "giai_thich": cau_tim_thay["giai_thich"],
            "xp_nhan": 0,
            "coin_nhan": 0,
            "danh_hieu": tien_do["danh_hieu"],
            "tong_exp": tien_do["tong_diem_exp"]
        }

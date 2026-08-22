# Thu muc: xu_ly_tro_choi
# File: quan_ly_vong_bang.py
# Mo ta: Module quan ly logic va quy tac tinh diem 3 tran dau Vong Bang cho World Cup va Champions League

def kiem_tra_qua_vong_bang(danh_sach_ket_qua):
    """
    Kiem tra doi bong co vuot qua Vong Bang (3 tran) de vao Vong Tu Ket hay khong.
    Quy tac:
    - Thang - Thang - Thang (3 tran thang) -> PASS
    - Thang - Thang - Thua (2 tran thang, 1 tran thua) -> PASS
    - Thang - Thang - Hoa (2 tran thang, 1 tran hoa) -> PASS
    - Cac truong hop me khac (it hon 2 tran thang) -> FAIL (Bi loai).
    """
    if not danh_sach_ket_qua or len(danh_sach_ket_qua) < 3:
        return False

    so_thang = danh_sach_ket_qua.count("thang")
    
    # Neu dat tu 2 tran thang tro len tuong duong 3 thang, 2 thang 1 thua, 2 thang 1 hoa -> ĐU ĐIEU KIEN PASS
    if so_thang >= 2:
        return True
    return False

def lay_danh_sach_doi_thu_vong_bang(ten_doi_user, danh_sach_tat_ca_doi):
    """
    Tra ve danh sach 3 doi thu khac nhau cho 3 tran dau Vong Bang.
    """
    tat_ca = [d for d in danh_sach_tat_ca_doi if d != ten_doi_user]
    if len(tat_ca) >= 3:
        return tat_ca[:3]
    elif len(tat_ca) > 0:
        return (tat_ca * 3)[:3]
    return ["Doi thu 1", "Doi thu 2", "Doi thu 3"]

def tao_chuoi_tom_tat_vong_bang(danh_sach_ket_qua):
    """
    Tao chuoi van ban mo ta ket qua 3 tran dau Vong Bang cho hoc sinh THCS de hieu.
    """
    ten_ket_qua = {
        "thang": "Thắng",
        "hoa": "Hòa",
        "thua": "Thua"
    }
    ds_str = [ten_ket_qua.get(k, "Chưa đá") for k in danh_sach_ket_qua]
    so_thang = danh_sach_ket_qua.count("thang")
    so_hoa = danh_sach_ket_qua.count("hoa")
    so_thua = danh_sach_ket_qua.count("thua")

    tong_ket_text = f"Trận 1: {ds_str[0] if len(ds_str) > 0 else 'Chưa đá'}, Trận 2: {ds_str[1] if len(ds_str) > 1 else 'Chưa đá'}, Trận 3: {ds_str[2] if len(ds_str) > 2 else 'Chưa đá'}"
    thong_ke_text = f"Tổng cộng: {so_thang} Thắng, {so_hoa} Hòa, {so_thua} Thua"
    
    return f"{tong_ket_text}\n({thong_ke_text})"

# Thu muc: xu_ly_kiem_tra
# File: bo_cham_diem.py
# Mo ta: Dong co cham diem tu dong, tu dong luu cau sai vao So Loi Sai, hien thi loi giai va phan tich noi dung con yeu sang Tieng Viet co dau

from xu_ly_so_tay.quan_ly_so_loi_sai import them_cau_loi_sai, xoa_cau_loi_sai

def cham_bai_lam(danh_sach_cau_hoi, danh_sach_cung_cap):
    """Chấm điểm bài làm của học sinh, tự động lưu câu làm sai vào Sổ Lỗi Sai và trả về báo cáo chi tiết chuẩn Tiếng Viet co dau."""
    so_cau_dung = 0
    so_cau_sai = 0
    chi_tiet_ket_qua = []
    cac_phan_yeu = []

    for idx, cau_hoi in enumerate(danh_sach_cau_hoi):
        dap_an_user = danh_sach_cung_cap.get(idx, "")
        dap_an_dung = cau_hoi.get("dap_an_dung", "")
        
        is_correct = False
        if str(dap_an_user).strip().lower() == str(dap_an_dung).strip().lower():
            is_correct = True
            so_cau_dung += 1
            # Xóa khỏi Sổ Lỗi Sai nếu học sinh đã trả lời đúng lại câu này
            xoa_cau_loi_sai(cau_hoi.get("cau_hoi", ""))
        else:
            so_cau_sai += 1
            chuong_ref = cau_hoi.get("chuong", "Kiến thức tổng hợp")
            if chuong_ref not in cac_phan_yeu:
                cac_phan_yeu.append(chuong_ref)
            # TỰ ĐỘNG LƯU VÀO SỔ LỖI SAI KHI HỌC SINH TRẢ LỜI SAI
            them_cau_loi_sai(cau_hoi, dap_an_chong_sai=str(dap_an_user))


        chi_tiet_ket_qua.append({
            "cau_so": idx + 1,
            "cau_hoi": cau_hoi.get("cau_hoi", ""),
            "dap_an_user": dap_an_user,
            "dap_an_dung": dap_an_dung,
            "dung_sai": is_correct,
            "giai_thich": cau_hoi.get("giai_thich", "Chưa có giải thích chi tiết.")
        })

    tong_cau = len(danh_sach_cau_hoi)
    diem_so = round((so_cau_dung / tong_cau) * 10, 1) if tong_cau > 0 else 0
    phan_tram = round((so_cau_dung / tong_cau) * 100, 1) if tong_cau > 0 else 0

    # Xếp loại học sinh
    xep_loai = "Chưa đạt"
    if phan_tram >= 90:
        xep_loai = "Xuất sắc"
    elif phan_tram >= 80:
        xep_loai = "Giỏi"
    elif phan_tram >= 65:
        xep_loai = "Khá"
    elif phan_tram >= 50:
        xep_loai = "Trung bình"

    return {
        "diem_so": diem_so,
        "phan_tram": phan_tram,
        "so_cau_dung": so_cau_dung,
        "so_cau_sai": so_cau_sai,
        "tong_cau": tong_cau,
        "xep_loai": xep_loai,
        "chi_tiet": chi_tiet_ket_qua,
        "noi_dung_yeu": cac_phan_yeu
    }

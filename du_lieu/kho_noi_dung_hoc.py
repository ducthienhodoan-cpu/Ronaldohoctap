# Thu muc: du_lieu
# File: kho_noi_dung_hoc.py
# Mo ta: Cung cap du lieu chuong trinh hoc tu Lop 1 den Lop 12 va 5 Chu de rieng theo tung Mon sang Tieng Viet co dau

def lay_danh_sach_lop():
    """Trả về danh sách tất cả các lớp học từ Lớp 1 đến Lớp 12."""
    return [f"Lớp {i}" for i in range(1, 13)]

def lay_danh_sach_mon_hoc(ten_lop):
    """Trả về danh sách môn học tương ứng với từng lớp."""
    if ten_lop in ["Lớp 1", "Lớp 2"]:
        return ["Toán", "Tiếng Việt", "Đạo đức", "Tự nhiên và Xã hội", "Tiếng Anh", "Tin học"]
    elif ten_lop == "Lớp 3":
        return ["Toán", "Tiếng Việt", "Tự nhiên và Xã hội", "Công nghệ", "Tin học", "Tiếng Anh"]
    elif ten_lop in ["Lớp 4", "Lớp 5"]:
        return ["Toán", "Tiếng Việt", "Khoa học", "Lịch sử và Địa lí", "Tin học"]
    elif ten_lop in ["Lớp 6", "Lớp 7", "Lớp 8", "Lớp 9"]:
        return ["Toán", "Ngữ văn", "Khoa học tự nhiên", "Lịch sử và Địa lí", "Tin học"]
    else:
        return [
            "Toán", "Ngữ văn", "Tiếng Anh", "Vật lí", 
            "Hóa học", "Sinh học", "Tin học", "Địa lí", 
            "Lịch sử", "Giáo dục kinh tế và pháp luật"
        ]

def lay_chu_de_theo_lop_va_mon(ten_lop, ten_mon):
    """Trả về ĐÚNG 5 CHỦ ĐỀ BÀI HỌC theo Lớp và Môn học được chọn."""
    if "Toán" in ten_mon:
        return [
            f"Chủ đề 1: Số học, Đại số và Các phép tính ({ten_lop})",
            f"Chủ đề 2: Phương trình, Biểu thức và Hàm số ({ten_lop})",
            f"Chủ đề 3: Hình học phẳng và Hình học không gian ({ten_lop})",
            f"Chủ đề 4: Thống kê, Dữ liệu và Xác suất ứng dụng ({ten_lop})",
            f"Chủ đề 5: Bài tập nâng cao và Luyện thi tổng hợp ({ten_lop})"
        ]
    elif "Tin" in ten_mon:
        return [
            f"Chủ đề 1: Máy tính, Hệ điều hành và Thiết bị số ({ten_lop})",
            f"Chủ đề 2: Mạng máy tính, Internet và An toàn thông tin ({ten_lop})",
            f"Chủ đề 3: Thuật toán, Sơ đồ khối và Tư duy máy tính ({ten_lop})",
            f"Chủ đề 4: Lập trình Python và Cấu trúc dữ liệu ({ten_lop})",
            f"Chủ đề 5: Dự án sáng tạo Minigame và Phần mềm ({ten_lop})"
        ]
    elif "Văn" in ten_mon or "Tiếng Việt" in ten_mon:
        return [
            f"Chủ đề 1: Đọc hiểu văn bản và Tác phẩm tiêu biểu ({ten_lop})",
            f"Chủ đề 2: Biện pháp tu từ và Đơn vị Tiếng Việt ({ten_lop})",
            f"Chủ đề 3: Tập làm văn Tự sự, Miêu tả và Biểu cảm ({ten_lop})",
            f"Chủ đề 4: Văn Nghị luận và Bày tỏ quan điểm cá nhân ({ten_lop})",
            f"Chủ đề 5: Ôn tập tổng hợp và Cảm thụ văn học ({ten_lop})"
        ]
    else:
        return [
            f"Chủ đề 1: Kiến thức nền tảng và Lý thuyết cơ bản {ten_mon} ({ten_lop})",
            f"Chủ đề 2: Khám phá thí nghiệm và Hiện tượng thực tế ({ten_lop})",
            f"Chủ đề 3: Bài tập vận dụng và Phương pháp giải nhanh ({ten_lop})",
            f"Chủ đề 4: Ứng dụng khoa học vào Đời sống hàng ngày ({ten_lop})",
            f"Chủ đề 5: Tổng ôn chuyên đề và Kiểm tra đánh giá ({ten_lop})"
        ]

def lay_chu_de_theo_lop(ten_lop):
    """Hàm bổ trợ lấy danh sách chủ đề theo lớp."""
    return lay_chu_de_theo_lop_va_mon(ten_lop, "Toán")

def lay_danh_sach_chuong(ten_lop, ten_mon):
    """Trả về danh sách chương học và bài học của môn học thuộc lớp được chọn."""
    danh_sach_chu_de = lay_chu_de_theo_lop_va_mon(ten_lop, ten_mon)
    danh_sach_chuong = []
    for idx, chu_de in enumerate(danh_sach_chu_de):
        danh_sach_chuong.append({
            "ten": chu_de,
            "bai": [
                f"Bài {idx*2 + 1}: Lý thuyết trọng tâm {ten_mon}",
                f"Bài {idx*2 + 2}: Luyện tập và Bài tập vận dụng"
            ]
        })
    return danh_sach_chuong

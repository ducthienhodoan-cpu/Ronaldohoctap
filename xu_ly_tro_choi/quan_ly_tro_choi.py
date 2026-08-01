# Thu muc: xu_ly_tro_choi
# File: quan_ly_tro_choi.py
# Mo ta: Module quan ly logic du lieu minigames gom Sieu Go Phim 3 phut doan van sang Tieng Viet co dau

import random
import os
import json

PATH_GHI_CHU = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ghi_chu_hoc_tap.json"))

def sinh_phep_tinh_math_racer(ten_lop="Lớp 6"):
    """Sinh ngẫu nhiên một phép tính toán học kèm các phương án đáp án cho game Đua xe Toán học."""
    loai = random.choice(["cong", "tru", "nhan", "chia", "phuc_hop"])
    
    if loai == "cong":
        a = random.randint(10, 99)
        b = random.randint(10, 99)
        cau_hoi = f"{a} + {b} = ?"
        dap_an_dung = a + b
    elif loai == "tru":
        a = random.randint(30, 150)
        b = random.randint(10, a)
        cau_hoi = f"{a} - {b} = ?"
        dap_an_dung = a - b
    elif loai == "nhan":
        a = random.randint(3, 15)
        b = random.randint(4, 12)
        cau_hoi = f"{a} x {b} = ?"
        dap_an_dung = a * b
    elif loai == "chia":
        b = random.randint(2, 12)
        dap_an_dung = random.randint(5, 20)
        a = b * dap_an_dung
        cau_hoi = f"{a} : {b} = ?"
    else:
        a = random.randint(2, 8)
        b = random.randint(3, 9)
        c = random.randint(5, 20)
        cau_hoi = f"{a} x {b} + {c} = ?"
        dap_an_dung = a * b + c

    # Tạo 4 phương án lựa chọn
    dap_an_sai_set = set()
    while len(dap_an_sai_set) < 3:
        offset = random.choice([-10, -5, -2, -1, 1, 2, 5, 10, 15])
        val = dap_an_dung + offset
        if val != dap_an_dung and val >= 0:
            dap_an_sai_set.add(val)
            
    cac_dap_an = list(dap_an_sai_set) + [dap_an_dung]
    random.shuffle(cac_dap_an)

    return {
        "cau_hoi": cau_hoi,
        "dap_an_dung": str(dap_an_dung),
        "dap_an": [str(x) for x in cac_dap_an]
    }


def lay_danh_sach_the_memory(ten_mon="Toán"):
    """Trả về danh sách các cặp thẻ ghi nhớ thuật ngữ Tin học & Tiếng Anh THCS."""
    cac_cap = [
        ("Python", "Ngôn ngữ lập trình phổ biến"),
        ("Variable", "Biến dùng lưu trữ dữ liệu"),
        ("Algorithm", "Thuật toán giải quyết vấn đề"),
        ("Loop", "Vòng lặp thực hiện nhiều lần"),
        ("Function", "Hàm xử lý một nhiệm vụ"),
        ("Compiler", "Trình biên dịch mã nguồn"),
        ("Database", "Cơ sở dữ liệu lưu trữ"),
        ("Boolean", "Kiểu dữ liệu Đúng hoặc Sai")
    ]
    
    selected_pairs = random.sample(cac_cap, 4)
    the_list = []
    for pair_id, (tu_a, tu_b) in enumerate(selected_pairs):
        the_list.append({"pair_id": pair_id, "noi_dung": tu_a})
        the_list.append({"pair_id": pair_id, "noi_dung": tu_b})
        
    random.shuffle(the_list)
    return the_list


def lay_doan_van_sieu_go_phim():
    """Trả về danh sách các đoạn văn ngắn giáo dục rèn luyện cho game Siêu Gõ Phím 3 phút."""
    cac_doan_van = [
        "Học tập là chuyến hành trình khám phá tri thức không bao giờ dừng lại. Việc rèn luyện kỹ năng gõ phím nhanh và chuẩn xác giúp em tiếp thu bài học hiệu quả và phát triển tư duy sắc bén mỗi ngày.",
        "Tin học và Toán học là chìa khóa vàng mở ra thế giới công nghệ tương lai. Việc kiên trì luyện tập gõ phím giúp em làm chủ máy tính và tự tin sáng tạo ra những sản phẩm phần mềm hữu ích.",
        "Máy tính giúp con người xử lý thông tin tự động với tốc độ vượt trội. Khi em làm chủ kỹ năng gõ bàn phím và tư duy thuật toán, em có thể chinh phục các kỳ thi Tin học trẻ một cách dễ dàng.",
        "Sự kiên trì và cẩn thận trong từng dòng lệnh lập trình sẽ mang lại cho em những thành quả vô cùng tự hào. Hãy luyện tập gõ phím mỗi ngày để nâng cao phản xạ và tốc độ của bản thân."
    ]
    return random.choice(cac_doan_van)


def tinh_bieu_thuc_may_tinh(bieu_thuc_str):
    """Tính toán biểu thức số học an toàn cho ứng dụng Máy tính Khoa học."""
    try:
        biens = bieu_thuc_str.replace("x", "*").replace(":", "/").replace("^", "**")
        allowed_chars = "0123456789+-*/(). "
        if not all(c in allowed_chars for c in biens):
            return "Lỗi: Biểu thức chứa ký tự không hợp lệ!"
        val = eval(biens)
        if isinstance(val, float):
            return f"{val:.4f}".rstrip("0").rstrip(".")
        return str(val)
    except ZeroDivisionError:
        return "Lỗi: Không thể chia cho số 0!"
    except Exception:
        return "Lỗi: Biểu thức toán học không hợp lệ!"


def luu_ghi_chu_hoc_tap(noi_dung_text):
    """Lưu nội dung sổ tay ghi chú của học sinh."""
    try:
        data = {"ghi_chu": noi_dung_text}
        with open(PATH_GHI_CHU, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception:
        return False


def lay_ghi_chu_hoc_tap():
    """Tải nội dung sổ tay ghi chú đã lưu."""
    if os.path.exists(PATH_GHI_CHU):
        try:
            with open(PATH_GHI_CHU, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("ghi_chu", "")
        except Exception:
            pass
    return "Ghi lại công thức và lịch ôn tập tại đây..."

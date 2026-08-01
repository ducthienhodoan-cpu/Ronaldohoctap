# Thu muc: du_lieu_giao_duc
# File: kho_cong_thuc.py
# Mo ta: Kho du lieu cong thuc va khai niem trong tam cac mon hoc THCS (Toan, Ly, Hoa, Anh, Tin) sang Tieng Viet co dau

DULIEU_CONG_THUC = {
    "Lớp 6": {
        "Toán": [
            {
                "ten": "Quy tắc chuyển vế",
                "cong_thuc": "Khi chuyển một số hạng từ vế này sang vế kia của một đẳng thức, ta phải đổi dấu số hạng đó: cộng thành trừ, trừ thành cộng.",
                "vi_du": "Bài giải chi tiết: Tìm x biết x + 15 = 40 => Step 1: Chuyển +15 sang vế phải thành -15 => Step 2: x = 40 - 15 => Đáp số x = 25."
            },
            {
                "ten": "Công thức tính chu vi và diện tích hình chữ nhật",
                "cong_thuc": "Chu vi: P = (a + b) x 2 | Diện tích: S = a x b",
                "vi_du": "Bài giải chi tiết: Chiều dài a = 12 cm, chiều rộng b = 8 cm => Step 1: P = (12 + 8) x 2 = 40 cm. Step 2: S = 12 x 8 = 96 cm²."
            },
            {
                "ten": "Công thức tính chu vi và diện tích hình vuông",
                "cong_thuc": "Chu vi: P = a x 4 | Diện tích: S = a x a",
                "vi_du": "Bài giải chi tiết: Cạnh a = 7 cm => Step 1: Chu vi P = 7 x 4 = 28 cm. Step 2: Diện tích S = 7 x 7 = 49 cm²."
            }
        ],
        "Khoa học tự nhiên": [
            {
                "ten": "Đơn vị đo chuẩn SI",
                "cong_thuc": "Chiều dài: mét (m) | Khối lượng: kilôgam (kg) | Thời gian: giây (s) | Nhiệt độ: độ C (°C)",
                "vi_du": "1 km = 1000 m | 1 kg = 1000 g | 1 giờ = 3600 giây"
            },
            {
                "ten": "Khái niệm biến đổi vật lý và biến đổi hóa học",
                "cong_thuc": "Biến đổi vật lý: Không tạo ra chất mới. Biến đổi hóa học: Có tạo ra chất mới.",
                "vi_du": "Nước đá tan thành nước lỏng = Biến đổi vật lý. Đốt cháy gỗ thành than = Biến đổi hóa học."
            }
        ],
        "Tiếng Anh": [
            {
                "ten": "Thì Hiện tại đơn (Present Simple Tense)",
                "cong_thuc": "Khẳng định: S + V(s/es) | Phủ định: S + do/does + not + V | Nghi vấn: Do/Does + S + V?",
                "vi_du": "She walks to school every day. / They do not play football on Monday."
            }
        ]
    },
    "Lớp 7": {
        "Toán": [
            {
                "ten": "Giá trị tuyệt đối của một số thực",
                "cong_thuc": "|x| = x nếu x >= 0 | |x| = -x nếu x < 0",
                "vi_du": "Bài giải chi tiết: Tìm x biết |x - 2| = 6 => TH1: x - 2 = 6 => x = 8. TH2: x - 2 = -6 => x = -4. Đáp số x thuộc {8, -4}."
            },
            {
                "ten": "Các trường hợp bằng nhau của tam giác",
                "cong_thuc": "1. Cạnh - Cạnh - Cạnh (c-c-c) | 2. Cạnh - Góc - Cạnh (c-g-c) | 3. Góc - Cạnh - Góc (g-c-g)",
                "vi_du": "Bài giải chi tiết: Xét tam giác ABC và DEF có AB=DE, góc B=góc E, BC=EF => Hai tam giác bằng nhau theo trường hợp c-g-c."
            }
        ],
        "Tin học": [
            {
                "ten": "Các kiểu dữ liệu cơ bản trong Python",
                "cong_thuc": "int: số nguyên | float: số thực | str: chuỗi ký tự | bool: giá trị đúng/sai (True/False)",
                "vi_du": "a = 10 (int) | b = 3.14 (float) | c = 'Python' (str) | d = True (bool)"
            },
            {
                "ten": "Cú pháp vòng lặp for và hàm range trong Python",
                "cong_thuc": "for i in range(n): thực hiện n lần lặp với i chạy từ 0 đến n-1.",
                "vi_du": "for i in range(5): print(i) => in ra các số 0, 1, 2, 3, 4"
            }
        ]
    },
    "Lớp 8": {
        "Toán": [
            {
                "ten": "7 Hằng đẳng thức đáng nhớ",
                "cong_thuc": "1. (a+b)² = a² + 2ab + b² | 2. (a-b)² = a² - 2ab + b² | 3. a² - b² = (a-b)(a+b)",
                "vi_du": "Bài giải chi tiết: Rút gọn (x + 3)² - 6x => Step 1: Khai triển = x² + 6x + 9 - 6x => Step 2: Thu gọn = x² + 9."
            },
            {
                "ten": "Định lý Py-ta-go trong tam giác vuông",
                "cong_thuc": "Trong một tam giác vuông, bình phương cạnh huyền bằng tổng bình phương hai cạnh góc vuông: c² = a² + b²",
                "vi_du": "Bài giải chi tiết: AB = 6 cm, AC = 8 cm => Step 1: BC² = 6² + 8² = 36 + 64 = 100 => Step 2: BC = sqrt(100) = 10 cm."
            }
        ],
        "Khoa học tự nhiên": [
            {
                "ten": "Công thức tính khối lượng riêng D và áp suất p",
                "cong_thuc": "Khối lượng riêng: D = m / V | Áp suất: p = F / S",
                "vi_du": "Khối lượng m = 7800 kg, thể tích V = 1 m³ => D = 7800 kg/m³"
            }
        ]
    },
    "Lớp 9": {
        "Toán": [
            {
                "ten": "Công thức nghiệm của phương trình bậc hai ax² + bx + c = 0",
                "cong_thuc": "Tính Delta = b² - 4ac. Nếu Delta > 0: x1,2 = (-b ± sqrt(Delta)) / (2a)",
                "vi_du": "Bài giải chi tiết: x² - 5x + 6 = 0 => Step 1: Delta = (-5)² - 4x1x6 = 1 => Step 2: x1 = (5+1)/2 = 3, x2 = (5-1)/2 = 2."
            },
            {
                "ten": "Hệ thức Lượng trong Tam giác vuông",
                "cong_thuc": "b² = a x b' | c² = a x c' | h² = b' x c' | a x h = b x c",
                "vi_du": "Bài giải chi tiết: Tam giác vuông có BH = 4 cm, CH = 9 cm => Step 1: h² = 4 x 9 = 36 => Step 2: Chiều cao h = sqrt(36) = 6 cm."
            }
        ],
        "Tiếng Anh": [
            {
                "ten": "Câu điều kiện loại 1 và loại 2 (Conditional Sentences)",
                "cong_thuc": "Loại 1 (Có thật): If + S + V(present), S + will + V | Loại 2 (Giả định): If + S + V(past), S + would + V",
                "vi_du": "If it rains tomorrow, I will stay at home. / If I were you, I would study harder."
            }
        ]
    }
}


def lay_danh_sach_cong_thuc(ten_lop="Lớp 6", ten_mon="Tất cả"):
    """Lay danh sach cong thuc tra cuu theo Lop va Mon hoc."""
    if ten_lop not in DULIEU_CONG_THUC:
        ten_lop = "Lớp 6"
    
    ket_qua = []
    mon_dict = DULIEU_CONG_THUC[ten_lop]
    
    for mon, ds in mon_dict.items():
        if ten_mon == "Tất cả" or ten_mon == mon:
            for item in ds:
                item_copy = dict(item)
                item_copy["mon"] = mon
                item_copy["lop"] = ten_lop
                ket_qua.append(item_copy)
    return ket_qua

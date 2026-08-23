# Thu muc: du_lieu_giao_duc
# File: kho_cong_thuc.py
# Mo ta: Kho du lieu cong thuc va khai niem trong tam cac mon hoc THCS (Toan, Ly, Hoa, Anh, Tin) sang Tieng Viet co dau

DULIEU_CONG_THUC = {
    "Lớp 1": {
        "Toán": [
            {
                "ten": "Bảng cộng trừ trong phạm vi 10 & 100",
                "cong_thuc": "Quy tắc: a + b = b + a (Giao hoán) | a - b = c <=> c + b = a",
                "vi_du": "Ví dụ: 7 + 3 = 10; 10 - 4 = 6; 25 + 14 = 39."
            },
            {
                "ten": "So sánh số và thứ tự các số",
                "cong_thuc": "Dấu lớn (>), Dấu bé (<), Dấu bằng (=)",
                "vi_du": "Ví dụ: 18 < 20; 45 > 39; 50 = 50."
            }
        ],
        "Tiếng Anh": [
            {
                "ten": "Đại từ nhân xưng và Động từ to be cơ bản",
                "cong_thuc": "I am, You are, He/She is, We/They are",
                "vi_du": "Ví dụ: I am a student. / She is my teacher."
            }
        ]
    },
    "Lớp 2": {
        "Toán": [
            {
                "ten": "Bảng nhân 2 và Bảng nhân 5",
                "cong_thuc": "2 x n = tích số chẵn | 5 x n = tích tận cùng là 0 hoặc 5",
                "vi_du": "Ví dụ: 2 x 8 = 16; 5 x 7 = 35; 5 x 9 = 45."
            },
            {
                "ten": "Đơn vị đo độ dài cơ bản",
                "cong_thuc": "1 m = 10 dm = 100 cm | 1 km = 1000 m",
                "vi_du": "Ví dụ: Đổi 3m = 300cm; 2m 50cm = 250cm."
            }
        ],
        "Tiếng Anh": [
            {
                "ten": "Danh từ số nhiều thêm -s/-es",
                "cong_thuc": "Danh từ số ít + s/es => Danh từ số nhiều",
                "vi_du": "Ví dụ: one cat -> two cats; one box -> three boxes."
            }
        ]
    },
    "Lớp 3": {
        "Toán": [
            {
                "ten": "Bảng cửu chương nhân chia từ 1 đến 9",
                "cong_thuc": "a x b = b x a | (a x b) : a = b",
                "vi_du": "Ví dụ: 7 x 8 = 56; 56 : 7 = 8; 9 x 9 = 81."
            },
            {
                "ten": "Chu vi và diện tích hình chữ nhật",
                "cong_thuc": "Chu vi: P = (dài + rộng) x 2 | Diện tích: S = dài x rộng",
                "vi_du": "Ví dụ: Chiều dài 8cm, rộng 5cm => P = (8+5)x2 = 26cm; S = 8x5 = 40 cm²."
            }
        ],
        "Tin học": [
            {
                "ten": "Thao tác chuột và bàn phím máy tính",
                "cong_thuc": "Nhấp chuột trái (Select), Nhấp đúp (Open), Nhấp chuột phải (Menu)",
                "vi_du": "Phím cách (Space) tạo dấu cách; Phím Enter xuống dòng."
            }
        ]
    },
    "Lớp 4": {
        "Toán": [
            {
                "ten": "Cộng trừ nhân chia Phân số",
                "cong_thuc": "Cùng mẫu: a/c + b/c = (a+b)/c | Nhân: (a/b) x (c/d) = (a x c)/(b x d)",
                "vi_du": "Ví dụ: 2/5 + 1/5 = 3/5; (2/3) x (4/5) = 8/15."
            },
            {
                "ten": "Tìm hai số khi biết Tổng và Hiệu",
                "cong_thuc": "Số lớn = (Tổng + Hiệu) : 2 | Số bé = (Tổng - Hiệu) : 2",
                "vi_du": "Ví dụ: Tổng = 40, Hiệu = 10 => Số lớn = (40+10):2 = 25; Số bé = (40-10):2 = 15."
            }
        ],
        "Khoa học": [
            {
                "ten": "Sự truyền nhiệt và dẫn nhiệt",
                "cong_thuc": "Kim loại dẫn nhiệt tốt | Không khí, gỗ dẫn nhiệt kém",
                "vi_du": "Ví dụ: Nồi kim loại giúp nấu chín thức ăn nhanh chóng."
            }
        ]
    },
    "Lớp 5": {
        "Toán": [
            {
                "ten": "Công thức Chuyển động đều (Vận tốc, Quãng đường, Thời gian)",
                "cong_thuc": "Quãng đường: s = v x t | Vận tốc: v = s : t | Thời gian: t = s : v",
                "vi_du": "Ví dụ: Vận tốc v = 60 km/h, thời gian t = 2h => Quãng đường s = 60 x 2 = 120 km."
            },
            {
                "ten": "Diện tích Hình tam giác và Hình thang",
                "cong_thuc": "Tam giác: S = (đáy x cao) : 2 | Hình thang: S = ((đáy lớn + đáy bé) x cao) : 2",
                "vi_du": "Ví dụ: Đáy 10cm, cao 6cm => S_tam_giác = (10 x 6):2 = 30 cm²."
            }
        ],
        "Khoa học": [
            {
                "ten": "Năng lượng tái tạo",
                "cong_thuc": "Nguồn năng lượng sạch: Mặt trời, Gió, Nước chảy, Địa nhiệt",
                "vi_du": "Ví dụ: Pin mặt trời chuyển quang năng thành điện năng."
            }
        ]
    },
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

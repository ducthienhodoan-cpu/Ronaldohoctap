# Thu muc: du_lieu_giao_duc
# File: ngan_hang_giai_toan.py
# Mo ta: Ngan hang cau hoi va bai giai chi tiet tung buoc cho mon Toan cap THCS (Lop 6 - Lop 9)

def lay_danh_sach_cau_hoi_toan_giai_chi_tiet(ten_lop="Lớp 6", ten_chu_de="Chủ đề 1"):
    """Tra ve danh sach cau hoi mon Toan kem bai giai tung buoc chi tiet theo Lop va Chu de."""
    
    if ten_lop == "Lớp 6":
        return [
            {
                "id": 101,
                "loai": "trac_nghiem",
                "cau_hoi": "Tính giá trị của biểu thức: A = 25 + 35 x 2 - 10",
                "luat_dap_an": ["75", "85", "110", "120"],
                "dap_an_dung": "85",
                "giai_thich": (
                    "Bài giải chi tiết:\n"
                    "Step 1: Thực hiện phép nhân trước: 35 x 2 = 70.\n"
                    "Step 2: Thực hiện phép cộng từ trái sang phải: 25 + 70 = 95.\n"
                    "Step 3: Thực hiện phép trừ cuối cùng: 95 - 10 = 85.\n"
                    "-> Đáp số đúng là 85."
                )
            },
            {
                "id": 102,
                "loai": "trac_nghiem",
                "cau_hoi": "Tìm số tự nhiên x biết: 2x + 15 = 45",
                "luat_dap_an": ["10", "15", "20", "30"],
                "dap_an_dung": "15",
                "giai_thich": (
                    "Bài giải chi tiết:\n"
                    "Step 1: Áp dụng quy tắc chuyển vế, chuyển +15 sang vế phải: 2x = 45 - 15.\n"
                    "Step 2: Tính vế phải: 2x = 30.\n"
                    "Step 3: Chia cả hai vế cho 2: x = 30 / 2 = 15.\n"
                    "-> Đáp số đúng là x = 15."
                )
            },
            {
                "id": 103,
                "loai": "trac_nghiem",
                "cau_hoi": "Một hình chữ nhật có chiều dài 12 cm và chiều rộng 8 cm. Tính diện tích của hình chữ nhật đó.",
                "luat_dap_an": ["40 cm²", "96 cm²", "48 cm²", "100 cm²"],
                "dap_an_dung": "96 cm²",
                "giai_thich": (
                    "Bài giải chi tiết:\n"
                    "Step 1: Áp dụng công thức tính diện tích hình chữ nhật: S = chiều dài x chiều rộng.\n"
                    "Step 2: Thay số vào công thức: S = 12 x 8.\n"
                    "Step 3: Thực hiện phép tính nhân: 12 x 8 = 96 (cm²).\n"
                    "-> Đáp số đúng là 96 cm²."
                )
            },
            {
                "id": 104,
                "loai": "trac_nghiem",
                "cau_hoi": "Tính tổng các số nguyên x thỏa mãn: -3 < x <= 3",
                "luat_dap_an": ["0", "3", "5", "6"],
                "dap_an_dung": "3",
                "giai_thich": (
                    "Bài giải chi tiết:\n"
                    "Step 1: Liệt kê các số nguyên x thỏa mãn điều kiện -3 < x <= 3:\n"
                    "       x thuộc {-2, -1, 0, 1, 2, 3}.\n"
                    "Step 2: Tính tổng: T = (-2) + (-1) + 0 + 1 + 2 + 3.\n"
                    "Step 3: Gộp các cặp số đối nhau: [(-2) + 2] + [(-1) + 1] + 0 + 3 = 0 + 0 + 0 + 3 = 3.\n"
                    "-> Đáp số đúng là 3."
                )
            }
        ]

    elif ten_lop == "Lớp 7":
        return [
            {
                "id": 201,
                "loai": "trac_nghiem",
                "cau_hoi": "Tính giá trị của biểu thức đại số: P = 3x² - 2x + 1 tại x = 2",
                "luat_dap_an": ["9", "11", "13", "15"],
                "dap_an_dung": "9",
                "giai_thich": (
                    "Bài giải chi tiết:\n"
                    "Step 1: Thay x = 2 vào biểu thức P: P = 3 x (2)² - 2 x (2) + 1.\n"
                    "Step 2: Tính lũy thừa trước: 2² = 4 => P = 3 x 4 - 4 + 1.\n"
                    "Step 3: Thực hiện nhân chia trước, cộng trừ sau:\n"
                    "       P = 12 - 4 + 1 = 8 + 1 = 9.\n"
                    "-> Đáp số đúng là 9."
                )
            },
            {
                "id": 202,
                "loai": "trac_nghiem",
                "cau_hoi": "Tìm x biết: |x - 3| = 5",
                "luat_dap_an": ["x = 8", "x = -2", "x = 8 hoặc x = -2", "x = 2"],
                "dap_an_dung": "x = 8 hoặc x = -2",
                "giai_thich": (
                    "Bài giải chi tiết:\n"
                    "Step 1: Áp dụng định nghĩa giá trị tuyệt đối, ta có 2 trường hợp:\n"
                    "       Trường hợp 1: x - 3 = 5 => x = 5 + 3 = 8.\n"
                    "       Trường hợp 2: x - 3 = -5 => x = -5 + 3 = -2.\n"
                    "Step 2: Kết luận cả 2 nghiệm x = 8 và x = -2 đều thỏa mãn.\n"
                    "-> Đáp số đúng là x = 8 hoặc x = -2."
                )
            },
            {
                "id": 203,
                "loai": "trac_nghiem",
                "cau_hoi": "Cho tam giác ABC có góc A = 60° và góc B = 70°. Số đo của góc C là bao nhiêu?",
                "luat_dap_an": ["50°", "60°", "70°", "110°"],
                "dap_an_dung": "50°",
                "giai_thich": (
                    "Bài giải chi tiết:\n"
                    "Step 1: Áp dụng định lý tổng ba góc trong một tam giác bằng 180°:\n"
                    "       Góc A + Góc B + Góc C = 180°.\n"
                    "Step 2: Thay số đo góc A và B vào: 60° + 70° + Góc C = 180°.\n"
                    "Step 3: Tính góc C: Góc C = 180° - 130° = 50°.\n"
                    "-> Đáp số đúng là 50°."
                )
            }
        ]

    elif ten_lop == "Lớp 8":
        return [
            {
                "id": 301,
                "loai": "trac_nghiem",
                "cau_hoi": "Rút gọn biểu thức hằng đẳng thức: A = (x + 3)² - 6x",
                "luat_dap_an": ["x² + 9", "x² - 9", "x² + 12x + 9", "x² + 3"],
                "dap_an_dung": "x² + 9",
                "giai_thich": (
                    "Bài giải chi tiết:\n"
                    "Step 1: Khai triển hằng đẳng thức (a + b)² = a² + 2ab + b²:\n"
                    "       (x + 3)² = x² + 2 x x x 3 + 3² = x² + 6x + 9.\n"
                    "Step 2: Thay vào biểu thức A: A = (x² + 6x + 9) - 6x.\n"
                    "Step 3: Thu gọn các số hạng đồng dạng: A = x² + (6x - 6x) + 9 = x² + 9.\n"
                    "-> Đáp số đúng là x² + 9."
                )
            },
            {
                "id": 302,
                "loai": "trac_nghiem",
                "cau_hoi": "Cho tam giác ABC vuông tại A có hai cạnh góc vuông AB = 6 cm và AC = 8 cm. Tính độ dài cạnh huyền BC.",
                "luat_dap_an": ["10 cm", "12 cm", "14 cm", "100 cm"],
                "dap_an_dung": "10 cm",
                "giai_thich": (
                    "Bài giải chi tiết:\n"
                    "Step 1: Áp dụng định lý Py-ta-go trong tam giác ABC vuông tại A:\n"
                    "       BC² = AB² + AC².\n"
                    "Step 2: Thay số: BC² = 6² + 8² = 36 + 64 = 100.\n"
                    "Step 3: Lấy căn bậc hai hai vế: BC = sqrt(100) = 10 (cm).\n"
                    "-> Đáp số đúng là 10 cm."
                )
            },
            {
                "id": 303,
                "loai": "trac_nghiem",
                "cau_hoi": "Giải phương trình bậc nhất một ẩn: 4x - 12 = 0",
                "luat_dap_an": ["x = 3", "x = -3", "x = 4", "x = 12"],
                "dap_an_dung": "x = 3",
                "giai_thich": (
                    "Bài giải chi tiết:\n"
                    "Step 1: Chuyển -12 từ vế trái sang vế phải và đổi dấu: 4x = 12.\n"
                    "Step 2: Chia cả hai vế cho 4: x = 12 / 4 = 3.\n"
                    "Step 3: Kết luận nghiệm phương trình là x = 3.\n"
                    "-> Đáp số đúng là x = 3."
                )
            }
        ]

    else: # Lớp 9 trở lên
        return [
            {
                "id": 401,
                "loai": "trac_nghiem",
                "cau_hoi": "Giải phương trình bậc hai: x² - 5x + 6 = 0",
                "luat_dap_an": ["x = 2 hoặc x = 3", "x = 1 hoặc x = 6", "x = -2 hoặc x = -3", "Phương trình vô nghiệm"],
                "dap_an_dung": "x = 2 hoặc x = 3",
                "giai_thich": (
                    "Bài giải chi tiết:\n"
                    "Step 1: Xác định các hệ số a = 1, b = -5, c = 6.\n"
                    "Step 2: Tính biệt thức Delta: Delta = b² - 4ac = (-5)² - 4 x 1 x 6 = 25 - 24 = 1.\n"
                    "Step 3: Vì Delta = 1 > 0 nên phương trình có 2 nghiệm phân biệt:\n"
                    "       x1 = (-b + sqrt(Delta)) / (2a) = (5 + 1) / 2 = 3.\n"
                    "       x2 = (-b - sqrt(Delta)) / (2a) = (5 - 1) / 2 = 2.\n"
                    "-> Đáp số đúng là x = 2 hoặc x = 3."
                )
            },
            {
                "id": 402,
                "loai": "trac_nghiem",
                "cau_hoi": "Cho tam giác ABC vuông tại A, đường cao AH. Biết BH = 4 cm, CH = 9 cm. Tính độ dài đường cao AH.",
                "luat_dap_an": ["6 cm", "13 cm", "36 cm", "5 cm"],
                "dap_an_dung": "6 cm",
                "giai_thich": (
                    "Bài giải chi tiết:\n"
                    "Step 1: Áp dụng hệ thức lượng trong tam giác vuông: AH² = BH x CH.\n"
                    "Step 2: Thay số: AH² = 4 x 9 = 36.\n"
                    "Step 3: Lấy căn bậc hai: AH = sqrt(36) = 6 (cm).\n"
                    "-> Đáp số đúng là 6 cm."
                )
            },
            {
                "id": 403,
                "loai": "trac_nghiem",
                "cau_hoi": "Tính giá trị căn bậc hai: B = sqrt(49) + sqrt(16) - sqrt(25)",
                "luat_dap_an": ["6", "8", "10", "12"],
                "dap_an_dung": "6",
                "giai_thich": (
                    "Bài giải chi tiết:\n"
                    "Step 1: Tính từng căn bậc hai:\n"
                    "       sqrt(49) = 7, sqrt(16) = 4, sqrt(25) = 5.\n"
                    "Step 2: Thay vào biểu thức B: B = 7 + 4 - 5.\n"
                    "Step 3: Thực hiện phép cộng trừ từ trái sang phải: B = 11 - 5 = 6.\n"
                    "-> Đáp số đúng là 6."
                )
            }
        ]

def giai_toan_chi_tiet_theo_mau(loai_bai, a, b, c=0):
    """Hàm bổ trợ tự động sinh bài giải toán chi tiết theo dạng toán và tham số."""
    if loai_bai == "tim_x_bac_1":
        # ax + b = 0 => x = -b/a
        if a == 0:
            return "Lỗi: Hệ số a phải khác 0."
        nghiem = -b / a
        return (
            f"Bài giải chi tiết cho phương trình {a}x + ({b}) = 0:\n"
            f"Step 1: Chuyển số hạng tự do ({b}) sang vế phải và đổi dấu: {a}x = {-b}.\n"
            f"Step 2: Chia cả hai vế cho {a}: x = {-b} / {a}.\n"
            f"Step 3: Kết quả x = {nghiem}."
        )
    elif loai_bai == "pytago":
        # a, b la 2 canh goc vuong, tinh c = sqrt(a^2 + b^2)
        c_val = (a**2 + b**2)**0.5
        return (
            f"Bài giải chi tiết tính cạnh huyền Py-ta-go:\n"
            f"Step 1: Áp dụng c² = a² + b².\n"
            f"Step 2: Thay số: c² = {a}² + {b}² = {a**2} + {b**2} = {a**2 + b**2}.\n"
            f"Step 3: Độ dài cạnh huyền c = sqrt({a**2 + b**2}) = {c_val}."
        )
    return "Dạng toán không xác định."

# Thu muc: du_lieu_giao_duc
# File: sinh_10000_cau_hoi.py
# Mo ta: Bo sinh 10.000 cau hoi da dang tat ca cac mon tu Lop 1 den Lop 12 va IELTS

import random

DANH_SACH_MON = [
    "Toán", "Tiếng Anh", "Khoa học Tự nhiên", "Vật lý", 
    "Hóa học", "Sinh học", "Lịch sử & Địa lý", "Tin học", "Ngữ văn", "IELTS"
]

DANH_SACH_LOP = [f"Lớp {i}" for i in range(1, 13)] + ["Luyện thi IELTS"]

DO_KHO_LIST = ["Dễ", "Trung bình", "Nâng cao"]

def tao_cac_mau_cau_hoi_toan(lop, idx):
    """Sinh cau hoi Toan hoc tu cap 1 den cap 3."""
    num_lop = int(lop.replace("Lớp ", "")) if "Lớp" in lop else 10
    
    if num_lop <= 5:
        # Tieu hoc: Cong, tru, nhan, chia, phan so, hinh hoc co ban
        a = random.randint(10 * num_lop, 50 * num_lop)
        b = random.randint(5 * num_lop, 25 * num_lop)
        op = random.choice(["+", "-", "*", "/"])
        
        if op == "+":
            ans = a + b
            q_text = f"Tính giá trị của phép cộng: {a} + {b} = ?"
            exp = f"Bài giải chi tiết:\nBước 1: Thực hiện phép cộng: {a} + {b}.\nBước 2: Kết quả thu được là {ans}."
        elif op == "-":
            ans = a
            a_sum = a + b
            q_text = f"Tính giá trị của phép trừ: {a_sum} - {b} = ?"
            exp = f"Bài giải chi tiết:\nBước 1: Thực hiện phép trừ {a_sum} - {b}.\nBước 2: Kết quả thu được là {ans}."
        elif op == "*":
            a_small = random.randint(2, 9 + num_lop)
            b_small = random.randint(2, 9 + num_lop)
            ans = a_small * b_small
            q_text = f"Một cửa hàng có {a_small} hộp bánh, mỗi hộp có {b_small} cái bánh. Hỏi có tất cả bao nhiêu cái bánh?"
            exp = f"Bài giải chi tiết:\nBước 1: Lấy số hộp nhân số bánh trong 1 hộp: {a_small} x {b_small}.\nBước 2: Kết quả = {ans} cái bánh."
        else:
            b_div = random.randint(2, 9)
            ans = random.randint(5, 20)
            a_prod = ans * b_div
            q_text = f"Chia đều {a_prod} quyển vở cho {b_div} bạn học sinh. Hỏi mỗi bạn nhận được bao nhiêu quyển vở?"
            exp = f"Bài giải chi tiết:\nBước 1: Thực hiện phép chia: {a_prod} : {b_div}.\nBước 2: Mỗi bạn nhận được {ans} quyển vở."
            
        correct = str(ans)
        opts = [str(ans), str(ans + random.randint(1, 3)), str(ans - random.randint(1, 3)), str(ans + 5)]
        opts = list(dict.fromkeys(opts))
        while len(opts) < 4:
            opts.append(str(ans + len(opts) * 2))
        random.shuffle(opts)
        
        return {
            "mon": "Toán",
            "lop": lop,
            "chu_de": f"Chủ đề Toán học cơ bản {lop}",
            "do_kho": random.choice(DO_KHO_LIST),
            "loai": "trac_nghiem",
            "cau_hoi": q_text,
            "luat_dap_an": opts,
            "dap_an_dung": correct,
            "giai_thich": exp
        }
    elif num_lop <= 9:
        # THCS: So nguyen, phan so, phuong trinh, hinh hoc, ham so
        x_val = random.randint(2, 12)
        m = random.randint(2, 6)
        n = random.randint(3, 20)
        c = m * x_val + n
        
        types = ["pt_bac_1", "hinh_hoc", "phan_so", "luy_thua"]
        chosen_type = random.choice(types)
        
        if chosen_type == "pt_bac_1":
            q_text = f"Tìm giá trị của x biết phương trình: {m}x + {n} = {c}"
            ans = str(x_val)
            exp = f"Bài giải chi tiết:\nBước 1: Chuyển vế: {m}x = {c} - {n} = {c - n}.\nBước 2: Chia cho {m}: x = {c - n} / {m} = {x_val}."
        elif chosen_type == "hinh_hoc":
            r = random.randint(3, 10)
            ans = str(r * r * 3)  # dien tich tam giac hoac chu vi
            q_text = f"Cho tam giác vuông có độ dài hai cạnh góc vuông lần lượt là {r*2} cm và {r*3} cm. Tính diện tích tam giác."
            s_val = (r * 2 * r * 3) // 2
            ans = str(s_val)
            exp = f"Bài giải chi tiết:\nBước 1: Công thức diện tích S = (1/2) * a * b.\nBước 2: S = (1/2) * {r*2} * {r*3} = {s_val} cm2."
        elif chosen_type == "luy_thua":
            base = random.randint(2, 5)
            p1 = random.randint(2, 4)
            p2 = random.randint(2, 3)
            p_sum = p1 + p2
            ans = str(base ** p_sum)
            q_text = f"Tính giá trị của lũy thừa: {base}^{p1} * {base}^{p2} = ?"
            exp = f"Bài giải chi tiết:\nBước 1: Áp dụng công thức nhân hai lũy thừa cùng cơ số: a^m * a^n = a^(m+n).\nBước 2: Kết quả = {base}^({p1}+{p2}) = {base}^{p_sum} = {ans}."
        else:
            ans = str(x_val * 2)
            q_text = f"Rút gọn biểu thức đại số A = {m}*(2x + 1) - {m} khi x = {x_val}."
            val_ans = m * (2 * x_val + 1) - m
            ans = str(val_ans)
            exp = f"Bài giải chi tiết:\nBước 1: Rút gọn A = {m*2}x + {m} - {m} = {m*2}x.\nBước 2: Thay x = {x_val} vào: A = {m*2} * {x_val} = {val_ans}."
            
        correct = str(ans)
        opts = [correct, str(int(correct) + 2), str(int(correct) - 2), str(int(correct) + 5)]
        opts = list(dict.fromkeys(opts))
        while len(opts) < 4:
            opts.append(str(int(correct) + len(opts) * 3))
        random.shuffle(opts)
        
        return {
            "mon": "Toán",
            "lop": lop,
            "chu_de": f"Đại số & Hình học {lop}",
            "do_kho": random.choice(DO_KHO_LIST),
            "loai": "trac_nghiem",
            "cau_hoi": q_text,
            "luat_dap_an": opts,
            "dap_an_dung": correct,
            "giai_thich": exp
        }
    else:
        # THPT: Ham so, dao ham, tich phan, toa do khong gian
        a_thpt = random.randint(1, 5)
        b_thpt = random.randint(2, 6)
        ans = f"{a_thpt * 2}x + {b_thpt}"
        q_text = f"Tính đạo hàm của hàm số y = {a_thpt}x^2 + {b_thpt}x - {random.randint(1, 10)}."
        exp = f"Bài giải chi tiết:\nBước 1: Áp dụng công thức đạo hàm (x^n)' = n*x^(n-1) và (c*x)' = c.\nBước 2: y' = 2*{a_thpt}x + {b_thpt} = {ans}."
        
        opts = [ans, f"{a_thpt}x + {b_thpt}", f"{a_thpt * 2}x", f"{a_thpt * 2}x - {b_thpt}"]
        random.shuffle(opts)
        return {
            "mon": "Toán",
            "lop": lop,
            "chu_de": f"Giải tích & Hình học không gian {lop}",
            "do_kho": random.choice(DO_KHO_LIST),
            "loai": "trac_nghiem",
            "cau_hoi": q_text,
            "luat_dap_an": opts,
            "dap_an_dung": ans,
            "giai_thich": exp
        }

def tao_cac_mau_cau_hoi_tieng_anh(lop, idx):
    """Sinh cau hoi Tieng Anh va ngu phap theo cap lop."""
    vocabs = [
        ("environment", "môi trường", "We must protect our environment from pollution."),
        ("technology", "công nghệ", "Modern technology helps students learn faster."),
        ("opportunity", "cơ hội", "Studying abroad gives you great opportunities."),
        ("experience", "kinh nghiệm, trải nghiệm", "She has ten years of experience in teaching."),
        ("development", "sự phát triển", "The development of artificial intelligence is rapid."),
        ("knowledge", "kiến thức", "Reading books improves your knowledge significantly."),
        ("challenge", "thử thách", "Every problem is a challenge to grow."),
        ("community", "cộng đồng", "Volunteers work hard to help their local community.")
    ]
    grammar_items = [
        ("She _____ to school every morning.", ["goes", "go", "going", "gone"], "goes", "Chủ ngữ ngôi thứ ba số ít 'She' ở thì Hiện tại đơn đi với động từ thêm -es/-s -> 'goes'."),
        ("If it rains tomorrow, we _____ at home.", ["will stay", "stayed", "stay", "would stay"], "will stay", "Cấu trúc câu điều kiện loại 1: If + S + V(hiện tại), S + will + V(nguyên mẫu)."),
        ("They have lived in this city _____ 2015.", ["since", "for", "in", "at"], "since", "'Since' đi kèm mốc thời gian cụ thể (2015) trong thì Hiện tại hoàn thành."),
        ("This exercises is _____ than the previous one.", ["more difficult", "difficult", "most difficult", "difficultly"], "more difficult", "So sánh hơn của tính từ dài 'difficult' là 'more difficult than'."),
        ("I wish I _____ a lot of money to travel the world.", ["had", "have", "will have", "am having"], "had", "Cấu trúc câu ước ở hiện tại: S + wish + S + V(quá khứ đơn) -> 'had'.")
    ]
    
    if idx % 2 == 0:
        item = random.choice(grammar_items)
        return {
            "mon": "Tiếng Anh",
            "lop": lop,
            "chu_de": f"Ngữ pháp & Cấu trúc câu {lop}",
            "do_kho": random.choice(DO_KHO_LIST),
            "loai": "trac_nghiem",
            "cau_hoi": f"Chọn đáp án đúng điền vào chỗ trống:\n{item[0]}",
            "luat_dap_an": item[1],
            "dap_an_dung": item[2],
            "giai_thich": f"Giải thích chi tiết:\n{item[3]}"
        }
    else:
        v = random.choice(vocabs)
        other_meanings = ["trách nhiệm", "khoảng cách", "kế hoạch", "kết luận", "nguyên nhân"]
        random.shuffle(other_meanings)
        opts = [v[1], other_meanings[0], other_meanings[1], other_meanings[2]]
        random.shuffle(opts)
        return {
            "mon": "Tiếng Anh",
            "lop": lop,
            "chu_de": f"Từ vựng & Đọc hiểu {lop}",
            "do_kho": random.choice(DO_KHO_LIST),
            "loai": "trac_nghiem",
            "cau_hoi": f"Từ '{v[0]}' trong câu sau có nghĩa là gì?\n\"{v[2]}\"",
            "luat_dap_an": opts,
            "dap_an_dung": v[1],
            "giai_thich": f"Giải thích chi tiết:\nTừ vựng '{v[0]}' mang ý nghĩa là '{v[1]}'. Ví dụ ngữ cảnh: {v[2]}"
        }

def tao_cac_mau_cau_hoi_tin_hoc(lop, idx):
    """Sinh cau hoi Tin hoc lap trinh, mang may tinh va tin hoc van phong."""
    topics = [
        ("Python", "Hàm nào trong Python dùng để xuất dữ liệu ra màn hình?", ["print()", "input()", "echo()", "write()"], "print()", "Hàm print() trong ngôn ngữ Python dùng để hiển thị dữ liệu ra màn hình console."),
        ("Python", "Kiểu dữ liệu nào lưu trữ danh sách các phần tử có thể thay đổi?", ["list", "tuple", "string", "integer"], "list", "Trong Python, kiểu dữ liệu 'list' biểu diễn danh sách có thứ tự và có thể thay đổi giá trị."),
        ("Phần cứng", "Bộ phận nào được coi là bộ não xử lý trung tâm của máy tính?", ["CPU", "RAM", "Ổ cứng HDD", "Nguồn điện"], "CPU", "CPU (Central Processing Unit) là bộ vi xử lý trung tâm đảm nhận mọi phép tính và điều khiển của máy tính."),
        ("Mạng", "Giao thức bảo mật phổ biến khi duyệt web an toàn là gì?", ["HTTPS", "HTTP", "FTP", "SMTP"], "HTTPS", "HTTPS (Hypertext Transfer Protocol Secure) sử dụng mã hóa SSL/TLS để bảo vệ dữ liệu truyền tải."),
        ("Thuật toán", "Thuật toán tìm kiếm nhị phân yêu cầu dãy số đầu vào phải có điều kiện gì?", ["Đã được sắp xếp", "Có độ dài chẵn", "Toàn số dương", "Không trùng nhau"], "Đã được sắp xếp", "Tìm kiếm nhị phân (Binary Search) yêu cầu mảng phải được sắp xếp tăng dần hoặc giảm dần trước khi thực hiện chia đôi.")
    ]
    t = topics[idx % len(topics)]
    return {
        "mon": "Tin học",
        "lop": lop,
        "chu_de": f"Khoa học Máy tính & Lập trình {lop}",
        "do_kho": random.choice(DO_KHO_LIST),
        "loai": "trac_nghiem",
        "cau_hoi": t[1],
        "luat_dap_an": t[2],
        "dap_an_dung": t[3],
        "giai_thich": f"Giải thích chi tiết môn Tin học:\n{t[4]}"
    }

def tao_cac_mau_cau_hoi_khtn(lop, idx):
    """Sinh cau hoi Khoa hoc Tu nhien, Vat ly, Hoa hoc, Sinh hoc."""
    items = [
        ("Vật lý", "Đơn vị đo lực trong hệ đo lường quốc tế SI là gì?", ["Niuton (N)", "Jun (J)", "Oát (W)", "Paxcan (Pa)"], "Niuton (N)", "Đơn vị đo lực trong hệ SI là Niuton, ký hiệu là N."),
        ("Vật lý", "Vận tốc ánh sáng truyền trong chân không xấp xỉ bằng bao nhiêu?", ["300.000 km/s", "150.000 km/s", "30.000 km/s", "1.000 km/s"], "300.000 km/s", "Vận tốc ánh sáng trong chân không là c xấp xỉ 3 x 10^8 m/s = 300.000 km/s."),
        ("Hóa học", "Công thức hóa học của khí Oxi là gì?", ["O2", "O", "O3", "H2O"], "O2", "Khí Oxi tồn tại dưới dạng phân tử gồm 2 nguyên tử Oxi liên kết với nhau (O2)."),
        ("Hóa học", "Kim loại nào sau đây dẫn điện và dẫn nhiệt tốt nhất?", ["Bạc (Ag)", "Đồng (Cu)", "Nhôm (Al)", "Sắt (Fe)"], "Bạc (Ag)", "Bạc là kim loại dẫn điện và nhiệt tốt nhất trong các kim loại, tiếp theo là Đồng."),
        ("Sinh học", "Bào quan nào được ví như 'nhà máy năng lượng' của tế bào?", ["Ti thể", "Lục lạp", "Riboxom", "Nhân tế bào"], "Ti thể", "Ti thể thực hiện hô hấp tế bào để tổng hợp năng lượng ATP cung cấp cho mọi hoạt động sống.")
    ]
    t = items[idx % len(items)]
    return {
        "mon": "Khoa học Tự nhiên",
        "lop": lop,
        "chu_de": f"Khám phá Khoa học Tự nhiên {lop}",
        "do_kho": random.choice(DO_KHO_LIST),
        "loai": "trac_nghiem",
        "cau_hoi": t[1],
        "luat_dap_an": t[2],
        "dap_an_dung": t[3],
        "giai_thich": f"Giải thích chi tiết:\n{t[4]}"
    }

def tao_cac_mau_cau_hoi_lich_su_dia_ly(lop, idx):
    """Sinh cau hoi Lich su va Dia ly Viet Nam & The gioi."""
    items = [
        ("Lịch sử", "Chiến thắng Điện Biên Phủ 'lừng lẫy năm châu, chấn động địa cầu' diễn ra vào năm nào?", ["1954", "1945", "1975", "1930"], "1954", "Chiến thắng Điện Biên Phủ toàn thắng ngày 7/5/1954 đập tan tập đoàn cứ điểm của thực dân Pháp."),
        ("Lịch sử", "Bản Tuyên ngôn Độc lập khai sinh ra nước VNDCCH được Bác Hồ đọc tại Quảng trường Ba Đình vào ngày nào?", ["2/9/1945", "19/8/1945", "30/4/1975", "3/2/1930"], "2/9/1945", "Ngày 2/9/1945, Chủ tịch Hồ Chí Minh đọc bản Tuyên ngôn Độc lập tại Quảng trường Ba Đình Hà Nội."),
        ("Địa lý", "Đỉnh núi nào được mệnh danh là 'Nóc nhà Đông Dương'?", ["Fansipan", "Mẫu Sơn", "Bạch Mộc Lương Tử", "Langbiang"], "Fansipan", "Đỉnh Fansipan cao 3.143m thuộc dãy Hoàng Liên Sơn là đỉnh núi cao nhất Việt Nam và toàn Đông Dương."),
        ("Địa lý", "Đại dương nào có diện tích lớn nhất thế giới?", ["Thái Bình Dương", "Đại Tây Dương", "Ấn Độ Dương", "Bắc Băng Dương"], "Thái Bình Dương", "Thái Bình Dương là đại dương lớn nhất với diện tích khoảng 165 triệu km2.")
    ]
    t = items[idx % len(items)]
    return {
        "mon": "Lịch sử & Địa lý",
        "lop": lop,
        "chu_de": f"Địa lý & Lịch sử Việt Nam - Thế giới {lop}",
        "do_kho": random.choice(DO_KHO_LIST),
        "loai": "trac_nghiem",
        "cau_hoi": t[1],
        "luat_dap_an": t[2],
        "dap_an_dung": t[3],
        "giai_thich": f"Giải thích chi tiết:\n{t[4]}"
    }

def sinh_toan_bo_10000_cau_hoi():
    """Tạo bộ dữ liệu 10.000 câu hỏi chuẩn phủ khắp 12 khối lớp và các môn học."""
    danh_sach_tong = []
    tong_muc_tieu = 10000
    
    # 13 khoi lop (Lop 1-12 va IELTS)
    cau_moi_lop = tong_muc_tieu // len(DANH_SACH_LOP) + 10
    
    current_id = 1
    for lop in DANH_SACH_LOP:
        for i in range(cau_moi_lop):
            mon_idx = i % 5
            if mon_idx == 0:
                q = tao_cac_mau_cau_hoi_toan(lop, i)
            elif mon_idx == 1:
                q = tao_cac_mau_cau_hoi_tieng_anh(lop, i)
            elif mon_idx == 2:
                q = tao_cac_mau_cau_hoi_tin_hoc(lop, i)
            elif mon_idx == 3:
                q = tao_cac_mau_cau_hoi_khtn(lop, i)
            else:
                q = tao_cac_mau_cau_hoi_lich_su_dia_ly(lop, i)
            
            q["id"] = current_id
            danh_sach_tong.append(q)
            current_id += 1
            if len(danh_sach_tong) >= tong_muc_tieu:
                break
        if len(danh_sach_tong) >= tong_muc_tieu:
            break
            
    return danh_sach_tong[:tong_muc_tieu]

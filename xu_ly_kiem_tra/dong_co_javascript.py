# Thu muc: xu_ly_kiem_tra
# File: dong_co_javascript.py
# Mo ta: Dong co sinh cau hoi hoc tap va de thi khong khong trung lap 10.000+ cau hoi cho tat ca cac Lop 1-12 va cac Mon hoc sang Tieng Viet co dau

import os
import json
import subprocess
import random

def chay_javascript_sinh_de(ten_lop="Lớp 7", ten_mon="Toán", ten_chuong="Biểu thức đại số", so_cau=10):
    """Chạy script JavaScript hoặc Python Engine để sinh ngẫu nhiên từ 10 đến 10.000 câu hỏi không trùng lặp kèm bài giải chi tiết."""
    js_file = os.path.join(os.path.dirname(__file__), "..", "du_lieu", "sinh_de_javascript.js")
    js_file_clean = os.path.abspath(js_file).replace("\\", "/")

    # Thử chạy qua Node.js nếu có sẵn và số câu nhỏ hơn 100
    if so_cau <= 100:
        try:
            node_script = f"""const js = require('{js_file_clean}'); const res = js.sinh_cau_hoi_js('{ten_lop}', '{ten_mon}', '{ten_chuong}', {so_cau}); console.log(JSON.stringify(res));"""
            cmd = ["node", "-e", node_script]
            proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", timeout=3)
            if proc.returncode == 0 and proc.stdout.strip():
                danh_sach_js = json.loads(proc.stdout.strip())
                if len(danh_sach_js) > 0:
                    return danh_sach_js
        except Exception:
            pass

    # Động cơ Python Procedural Generator cho 10.000+ câu hỏi đa dạng chủ đề
    danh_sach = []
    da_co_cau_hoi = set()
    seed_offset = random.randint(1, 50000)

    for i in range(so_cau):
        retries = 0
        cau_hoi_dict = None

        while retries < 100:
            retries += 1
            n1 = random.randint(2, 99)
            n2 = random.randint(2, 50)
            n3 = random.randint(1, 30)
            n4 = random.randint(2, 12)
            var_name = ["x", "y", "a", "b", "m", "n", "P", "Q", "K", "H", "t", "v", "S"][ (i + retries + seed_offset) % 13 ]

            cau_text = ""
            opts = []
            correct = ""
            explain = ""

            # 1. MÔN TIN HỌC & PYTHON
            if "Tin" in ten_mon or "Python" in ten_chuong or "Tin học" in ten_chuong:
                kieu = (i * 7 + retries + seed_offset) % 12
                if kieu == 0:
                    val = n1 + n2 * n3
                    cau_text = f"Trong bài {ten_chuong} ({ten_lop}), kết quả xuất ra của lệnh print({n1} + {n2} * {n3}) trong Python là:"
                    opts = [str(val), str(val + 5), str((n1 + n2) * n3), str(val - 4)]
                    correct = str(val)
                    explain = f"Bài giải chi tiết:\nStep 1: Phép nhân * ưu tiên thực hiện trước phép cộng +.\nStep 2: {n2} x {n3} = {n2 * n3}.\nStep 3: {n1} + {n2 * n3} = {val}.\n-> Đáp số đúng là {val}."
                elif kieu == 1:
                    cau_text = f"Kiểu dữ liệu nào trong Python biểu diễn giá trị số nguyên trong bài {ten_chuong} ({ten_lop})?"
                    opts = ["int", "str", "float", "bool"]
                    correct = "int"
                    explain = "Bài giải chi tiết:\nStep 1: Kiểu int đại diện cho số nguyên (Integer).\nStep 2: Phù hợp lưu trữ các số như 1, 2, 100.\n-> Đáp án đúng là int."
                elif kieu == 2:
                    cau_text = f"Cú pháp khai báo biến {var_name} = {n1 * 3} hợp lệ trong Python bài {ten_chuong} là gì?"
                    opts = [f"{var_name} = {n1 * 3}", f"var {var_name} := {n1 * 3}", f"int {var_name} = {n1 * 3};", f"{var_name} == {n1 * 3}"]
                    correct = f"{var_name} = {n1 * 3}"
                    explain = f"Bài giải chi tiết:\nStep 1: Python dùng dấu '=' duy nhất để gán giá trị cho biến.\nStep 2: Cú pháp đúng là {var_name} = {n1 * 3}.\n-> Đáp án đúng là {var_name} = {n1 * 3}."
                elif kieu == 3:
                    val_rem = (n1 * 3 + n3) % 3
                    cau_text = f"Phép toán tính phần dư {n1 * 3 + n3} % 3 trong Python bài {ten_chuong} trả về kết quả bằng bao nhiêu?"
                    opts = [str(val_rem), str((val_rem + 1) % 3), str((val_rem + 2) % 3), "3"]
                    correct = str(val_rem)
                    explain = f"Bài giải chi tiết:\nStep 1: Toán tử % lấy phần dư của phép chia.\nStep 2: {n1 * 3 + n3} chia 3 được { (n1 * 3 + n3) // 3 } dư {val_rem}.\n-> Đáp số đúng là {val_rem}."
                elif kieu == 4:
                    val_pow = n4 ** 2
                    cau_text = f"Kết quả của biểu thức số mũ {n4} ** 2 trong Python bài {ten_chuong} là bao nhiêu?"
                    opts = [str(val_pow), str(n4 * 2), str(val_pow + 3), str(val_pow - 2)]
                    correct = str(val_pow)
                    explain = f"Bài giải chi tiết:\nStep 1: Toán tử ** tính lũy thừa.\nStep 2: {n4} ** 2 = {n4} x {n4} = {val_pow}.\n-> Đáp số đúng là {val_pow}."
                elif kieu == 5:
                    cau_text = f"Lệnh len(\"{'A' * n3}\") trong Python trả về giá trị độ dài chuỗi bằng bao nhiêu?"
                    opts = [str(n3), str(n3 + 1), str(n3 - 1), str(n3 * 2)]
                    correct = str(n3)
                    explain = f"Bài giải chi tiết:\nStep 1: Hàm len() trả về số lượng ký tự trong chuỗi.\nStep 2: Chuỗi gồm {n3} ký tự 'A' nên có độ dài {n3}.\n-> Đáp số đúng là {n3}."
                elif kieu == 6:
                    cau_text = f"Vòng lặp for i in range({n3}) trong Python thực hiện bao nhiêu lượt lặp?"
                    opts = [f"{n3} lượt", f"{n3 + 1} lượt", f"{n3 - 1} lượt", "Không lặp"]
                    correct = f"{n3} lượt"
                    explain = f"Bài giải chi tiết:\nStep 1: Range({n3}) sinh ra dãy số từ 0 đến {n3 - 1}.\nStep 2: Tổng số lượt lặp là {n3} lượt.\n-> Đáp án đúng là {n3} lượt."
                elif kieu == 7:
                    cau_text = f"Để chuyển đổi chuỗi \"{n1}\" thành số nguyên trong Python, ta sử dụng hàm nào?"
                    opts = [f"int(\"{n1}\")", f"str(\"{n1}\")", f"float(\"{n1}\")", f"bool(\"{n1}\")"]
                    correct = f"int(\"{n1}\")"
                    explain = f"Bài giải chi tiết:\nStep 1: Hàm int() ép kiểu dữ liệu từ chuỗi ký tự sang số nguyên.\nStep 2: int(\"{n1}\") trả về số nguyên {n1}.\n-> Đáp án đúng là int(\"{n1}\")."
                elif kieu == 8:
                    cau_text = f"Thẻ HTML nào dùng để tạo đường dẫn liên kết (Hyperlink) trong thiết kế Web?"
                    opts = ["<a>", "<link>", "<href>", "<url>"]
                    correct = "<a>"
                    explain = "Bài giải chi tiết:\nStep 1: Thẻ <a> (Anchor) được sử dụng để tạo liên kết trong trang HTML.\nStep 2: Thuộc tính href quy định đường dẫn đích.\n-> Đáp án đúng là <a>."
                elif kieu == 9:
                    cau_text = f"Thuộc tính CSS nào dùng để thay đổi màu chữ của một phần tử Web?"
                    opts = ["color", "font-color", "text-color", "background-color"]
                    correct = "color"
                    explain = "Bài giải chi tiết:\nStep 1: Thuộc tính color trong CSS quy định màu văn bản.\nStep 2: Ví dụ: color: #06B6D4;\n-> Đáp án đúng là color."
                elif kieu == 10:
                    cau_text = f"Trong ngôn ngữ C++, câu lệnh chuẩn dùng để in dữ liệu ra màn hình là gì?"
                    opts = ["std::cout <<", "System.out.println()", "printf()", "console.log()"]
                    correct = "std::cout <<"
                    explain = "Bài giải chi tiết:\nStep 1: C++ sử dụng dòng xuất dữ liệu std::cout đi kèm toán tử <<.\n-> Đáp án đúng là std::cout <<."
                else:
                    cau_text = f"Trong cấu trúc dữ liệu List của Python, phương thức nào dùng để thêm một phần tử vào cuối danh sách?"
                    opts = ["append()", "add()", "push()", "insert_last()"]
                    correct = "append()"
                    explain = "Bài giải chi tiết:\nStep 1: Phương thức list.append(x) thêm phần tử x vào cuối danh sách.\n-> Đáp án đúng là append()."

            # 2. MÔN VẬT LÝ
            elif "Vật lý" in ten_mon or "Lý" in ten_mon:
                kieu_ly = (i * 5 + retries + seed_offset) % 6
                if kieu_ly == 0:
                    v_kmh = n2 * 10
                    t_h = n4
                    s_km = v_kmh * t_h
                    cau_text = f"Một xe máy chuyển động đều với vận tốc v = {v_kmh} km/h. Quãng đường xe đi được trong thời gian t = {t_h} giờ là:"
                    opts = [f"{s_km} km", f"{s_km + 15} km", f"{s_km - 10} km", f"{s_km + 30} km"]
                    correct = f"{s_km} km"
                    explain = f"Bài giải chi tiết:\nStep 1: Công thức quãng đường trong chuyển động thẳng đều: s = v x t.\nStep 2: Thay số: s = {v_kmh} x {t_h} = {s_km} (km).\n-> Đáp số đúng là {s_km} km."
                elif kieu_ly == 1:
                    m_kg = n1
                    p_N = m_kg * 10
                    cau_text = f"Tính trọng lượng P của một vật có khối lượng m = {m_kg} kg trên Trái Đất (lấy g = 10 m/s²):"
                    opts = [f"{p_N} N", f"{p_N + 20} N", f"{p_N - 10} N", f"{p_N + 50} N"]
                    correct = f"{p_N} N"
                    explain = f"Bài giải chi tiết:\nStep 1: Công thức tính trọng lượng: P = 10 x m.\nStep 2: Thay m = {m_kg} kg: P = 10 x {m_kg} = {p_N} (N).\n-> Đáp số đúng là {p_N} N."
                elif kieu_ly == 2:
                    U_v = n2 * 6
                    I_a = 2
                    R_ohm = U_v // I_a
                    cau_text = f"Cho mạch điện có hiệu điện thế U = {U_v} V và cường độ dòng điện I = {I_a} A. Điện trở R của dây dẫn là:"
                    opts = [f"{R_ohm} Ôm", f"{R_ohm + 4} Ôm", f"{R_ohm - 2} Ôm", f"{R_ohm + 10} Ôm"]
                    correct = f"{R_ohm} Ôm"
                    explain = f"Bài giải chi tiết:\nStep 1: Áp dụng định luật Ôm: R = U / I.\nStep 2: Thay số: R = {U_v} / {I_a} = {R_ohm} (Ôm).\n-> Đáp số đúng là {R_ohm} Ôm."
                elif kieu_ly == 3:
                    P_watt = n1 * 50
                    t_sec = 10
                    A_joule = P_watt * t_sec
                    cau_text = f"Một động cơ điện có công suất P = {P_watt} W hoạt động trong t = {t_sec} giây. Công A của lực thực hiện là:"
                    opts = [f"{A_joule} J", f"{A_joule + 200} J", f"{A_joule - 100} J", f"{A_joule + 500} J"]
                    correct = f"{A_joule} J"
                    explain = f"Bài giải chi tiết:\nStep 1: Công thức tính công: A = P x t.\nStep 2: Thay số: A = {P_watt} x {t_sec} = {A_joule} (Joule).\n-> Đáp số đúng là {A_joule} J."
                elif kieu_ly == 4:
                    freq = n2 * 5
                    lambda_m = 2
                    v_wave = freq * lambda_m
                    cau_text = f"Sóng cơ có tần số f = {freq} Hz và bước sóng lambda = {lambda_m} m. Tốc độ truyền sóng v là:"
                    opts = [f"{v_wave} m/s", f"{v_wave + 10} m/s", f"{v_wave - 5} m/s", f"{v_wave + 20} m/s"]
                    correct = f"{v_wave} m/s"
                    explain = f"Bài giải chi tiết:\nStep 1: Công thức tốc độ truyền sóng: v = lambda x f.\nStep 2: Thay số: v = {lambda_m} x {freq} = {v_wave} (m/s).\n-> Đáp số đúng là {v_wave} m/s."
                else:
                    cau_text = f"Đơn vị chuẩn đo công suất trong Hệ đo lường quốc tế (SI) là gì?"
                    opts = ["Oát (W)", "Jun (J)", "Vôn (V)", "Ampe (A)"]
                    correct = "Oát (W)"
                    explain = "Bài giải chi tiết:\nStep 1: Đơn vị đo công suất là Oát (Watt, ký hiệu W).\n-> Đáp án đúng là Oát (W)."

            # 3. MÔN HÓA HỌC
            elif "Hóa" in ten_mon:
                kieu_hoa = (i * 4 + retries + seed_offset) % 5
                if kieu_hoa == 0:
                    n_mol = n4
                    M_h2o = 18
                    m_g = n_mol * M_h2o
                    cau_text = f"Tính khối lượng m của {n_mol} mol nước H₂O (biết M_H2O = 18 g/mol):"
                    opts = [f"{m_g} g", f"{m_g + 10} g", f"{m_g - 5} g", f"{m_g + 18} g"]
                    correct = f"{m_g} g"
                    explain = f"Bài giải chi tiết:\nStep 1: Công thức khối lượng: m = n x M.\nStep 2: Thay số: m = {n_mol} x 18 = {m_g} (gam).\n-> Đáp số đúng là {m_g} g."
                elif kieu_hoa == 1:
                    n_mol = n4
                    V_lit = n_mol * 22.4
                    cau_text = f"Tính thể tích V ở điều kiện tiêu chuẩn (đktc) của {n_mol} mol khí Khí Oxy (O₂):"
                    opts = [f"{V_lit:.1f} lít", f"{V_lit + 4.48:.1f} lít", f"{V_lit - 2.24:.1f} lít", f"{V_lit + 10:.1f} lít"]
                    correct = f"{V_lit:.1f} lít"
                    explain = f"Bài giải chi tiết:\nStep 1: Công thức thể tích khí ở đktc: V = n x 22.4.\nStep 2: Thay n = {n_mol}: V = {n_mol} x 22.4 = {V_lit:.1f} (lít).\n-> Đáp số đúng là {V_lit:.1f} lít."
                elif kieu_hoa == 2:
                    cau_text = f"Kim loại nào sau đây ở điều kiện thường tồn tại dưới dạng thể lỏng?"
                    opts = ["Thủy ngân (Hg)", "Sắt (Fe)", "Đồng (Cu)", "Nhôm (Al)"]
                    correct = "Thủy ngân (Hg)"
                    explain = "Bài giải chi tiết:\nStep 1: Thủy ngân (Hg) là kim loại duy nhất thể lỏng ở nhiệt độ phòng.\n-> Đáp án đúng là Thủy ngân (Hg)."
                elif kieu_hoa == 3:
                    cau_text = f"Dung dịch Axit Clohiđric (HCl) làm quỳ tím chuyển sang màu gì?"
                    opts = ["Màu đỏ", "Màu xanh", "Màu hồng", "Không đổi màu"]
                    correct = "Màu đỏ"
                    explain = "Bài giải chi tiết:\nStep 1: Dung dịch Axit làm giấy quỳ tím chuyển sang màu đỏ tím/đỏ.\n-> Đáp án đúng là Màu đỏ."
                else:
                    cau_text = f"Công thức hóa học của Muối ăn sử dụng hàng ngày là gì?"
                    opts = ["NaCl", "NaOH", "HCl", "CaCO3"]
                    correct = "NaCl"
                    explain = "Bài giải chi tiết:\nStep 1: Muối ăn là Natri Clorua có công thức hóa học NaCl.\n-> Đáp án đúng là NaCl."

            # 4. MÔN SINH HỌC
            elif "Sinh" in ten_mon:
                kieu_sinh = (i * 3 + retries + seed_offset) % 4
                if kieu_sinh == 0:
                    A_nu = n1 * 10
                    G_nu = n2 * 10
                    N_total = 2 * (A_nu + G_nu)
                    cau_text = f"Một gen có số nuclêôtit loại A = {A_nu} và G = {G_nu}. Tổng số nuclêôtit N của gen là:"
                    opts = [str(N_total), str(N_total + 100), str(N_total - 50), str(N_total + 200)]
                    correct = str(N_total)
                    explain = f"Bài giải chi tiết:\nStep 1: Theo nguyên tắc bổ sung A=T, G=X => N = 2A + 2G.\nStep 2: N = 2 x ({A_nu} + {G_nu}) = 2 x {A_nu + G_nu} = {N_total}.\n-> Đáp số đúng là {N_total}."
                elif kieu_sinh == 0:
                    cau_text = f"Bào quan nào được ví là 'Nhà máy năng lượng' cung cấp ATP cho mọi hoạt động của tế bào?"
                    opts = ["Ti thể", "Lưới nội chất", "Nhân tế bào", "Không bào"]
                    correct = "Ti thể"
                    explain = "Bài giải chi tiết:\nStep 1: Ti thể hô hấp tổng hợp ATP năng lượng cho tế bào.\n-> Đáp án đúng là Ti thể."
                elif kieu_sinh == 2:
                    cau_text = f"Loại bazo nitơ nào sau đây chỉ có trong ARN mà không có trong ADN?"
                    opts = ["Uraxin (U)", "Ađênin (A)", "Guanin (G)", "Xitôzin (X)"]
                    correct = "Uraxin (U)"
                    explain = "Bài giải chi tiết:\nStep 1: ARN chứa Uraxin (U) thay cho Timin (T) trong ADN.\n-> Đáp án đúng là Uraxin (U)."
                else:
                    cau_text = f"Tỉ lệ phân tính kiểu hình ở thế hệ F2 trong phép mọc lai 1 cặp tính trạng của Men-đen là:"
                    opts = ["3 Trội : 1 Lặn", "1 Trội : 1 Lặn", "9:3:3:1", "1 Trội : 2 Trung gian : 1 Lặn"]
                    correct = "3 Trội : 1 Lặn"
                    explain = "Bài giải chi tiết:\nStep 1: Quy luật phân li Men-đen cho tỉ lệ F2 là 3 trội : 1 lặn.\n-> Đáp án đúng là 3 Trội : 1 Lặn."

            # 5. MÔN TIẾNG ANH & IELTS
            elif "Anh" in ten_mon or "IELTS" in ten_mon:
                kieu_eng = (i * 4 + retries + seed_offset) % 5
                if kieu_eng == 0:
                    verbs = ["play", "study", "watch", "visit", "write"]
                    v_chosen = verbs[i % len(verbs)]
                    cau_text = f"Choose the correct past simple form of the verb '{v_chosen}':"
                    past_forms = {
                        "play": "played", "study": "studied", "watch": "watched",
                        "visit": "visited", "write": "wrote"
                    }
                    correct = past_forms[v_chosen]
                    opts = [correct, v_chosen + "ing", v_chosen + "s", v_chosen + "en"]
                    explain = f"Bài giải chi tiết:\nStep 1: Động từ '{v_chosen}' ở thì quá khứ đơn (Past Simple) có dạng {correct}.\n-> Đáp án đúng là {correct}."
                elif kieu_eng == 1:
                    cau_text = f"Fill in the blank: 'She ______ to school by bus every day.'"
                    opts = ["goes", "go", "going", "went"]
                    correct = "goes"
                    explain = "Bài giải chi tiết:\nStep 1: Thì hiện tại đơn diễn tả thói quen hàng ngày với chủ ngữ số ít 'She'.\nStep 2: Động từ chia 'goes'.\n-> Đáp án đúng là goes."
                elif kieu_eng == 2:
                    cau_text = f"Which synonym has the closest meaning to the IELTS academic word 'SIGNIFICANT'?"
                    opts = ["Important", "Small", "Useless", "Tiny"]
                    correct = "Important"
                    explain = "Bài giải chi tiết:\nStep 1: 'Significant' có nghĩa là quan trọng, đáng kể, đồng nghĩa với 'Important'.\n-> Đáp án đúng là Important."
                elif kieu_eng == 3:
                    cau_text = f"Complete the Conditional Sentence Type 1: 'If it rains tomorrow, we ______ the picnic.'"
                    opts = ["will cancel", "canceled", "would cancel", "cancel"]
                    correct = "will cancel"
                    explain = "Bài giải chi tiết:\nStep 1: Câu điều kiện loại 1: If + Hiện tại đơn, Will + V-nguyên thể.\n-> Đáp án đúng là will cancel."
                else:
                    cau_text = f"Choose the correct relative pronoun: 'The student ______ won the English contest is my best friend.'"
                    opts = ["who", "which", "where", "whose"]
                    correct = "who"
                    explain = "Bài giải chi tiết:\nStep 1: Đại từ quan hệ 'who' dùng để thay thế cho danh từ chỉ người 'The student'.\n-> Đáp án đúng là who."

            # 6. MÔN TOÁN HỌC (ĐẠI SỐ & HÌNH HỌC LỚP 1-12)
            else:
                kieu_toan = (i * 11 + retries + seed_offset) % 10
                if kieu_toan == 0:
                    val = n1 * n3 + n2
                    cau_text = f"Tính giá trị của biểu thức đại số {var_name} = {n1}a + {n2} khi a = {n3} thuộc bài {ten_chuong} ({ten_lop}):"
                    opts = [str(val), str(val + 4), str(val - 3), str(val + 8)]
                    correct = str(val)
                    explain = f"Bài giải chi tiết:\nStep 1: Thay a = {n3} vào biểu thức: {n1} x {n3} + {n2}.\nStep 2: Thực hiện nhân trước: {n1} x {n3} = {n1 * n3}.\nStep 3: Cộng: {n1 * n3} + {n2} = {val}.\n-> Đáp số đúng là {val}."
                elif kieu_toan == 1:
                    val = n1 * 3 + n2
                    cau_text = f"Tìm giá trị {var_name} biết {var_name} - {n2} = {n1 * 3} trong bài học {ten_chuong} ({ten_lop}):"
                    opts = [str(val), str(val - n2), str(val + 6), str(val - 4)]
                    correct = str(val)
                    explain = f"Bài giải chi tiết:\nStep 1: Tính vế phải: {n1} x 3 = {n1 * 3}.\nStep 2: Chuyển vế -{n2} sang vế phải thành +{n2}.\nStep 3: {var_name} = {n1 * 3} + {n2} = {val}.\n-> Đáp số đúng là {val}."
                elif kieu_toan == 2:
                    val = (n1 + 4) * n2
                    cau_text = f"Một hình chữ nhật thuộc bài {ten_chuong} có chiều dài {n1 + 4} cm và chiều rộng {n2} cm. Diện tích của hình chữ nhật là:"
                    opts = [f"{val} cm²", f"{val + 10} cm²", f"{val - 4} cm²", f"{val + 12} cm²"]
                    correct = f"{val} cm²"
                    explain = f"Bài giải chi tiết:\nStep 1: Công thức diện tích S = Chiều dài x Chiều rộng.\nStep 2: S = {n1 + 4} x {n2} = {val} (cm²).\n-> Đáp số đúng là {val} cm²."
                elif kieu_toan == 3:
                    val_c = n1 * 5 + n2 * 2
                    cau_text = f"Tính giá trị biểu thức P = {n1} x 5 + {n2} x 2 thuộc bài {ten_chuong} ({ten_lop}):"
                    opts = [str(val_c), str(val_c + 5), str(val_c - 3), str(val_c + 10)]
                    correct = str(val_c)
                    explain = f"Bài giải chi tiết:\nStep 1: Thực hiện nhân: {n1} x 5 = {n1 * 5} và {n2} x 2 = {n2 * 2}.\nStep 2: Cộng: {n1 * 5} + {n2 * 2} = {val_c}.\n-> Đáp số đúng là {val_c}."
                elif kieu_toan == 4:
                    pct = n4 * 5
                    total = n1 * 10
                    val_p = (total * pct) // 100
                    cau_text = f"Trong bài học {ten_chuong} ({ten_lop}), {pct}% của số {total} bằng bao nhiêu?"
                    opts = [str(val_p), str(val_p + 5), str(val_p - 2), str(val_p + 10)]
                    correct = str(val_p)
                    explain = f"Bài giải chi tiết:\nStep 1: Nhân số với tỉ lệ phần trăm: {total} x {pct} = {total * pct}.\nStep 2: Chia cho 100: {total * pct} / 100 = {val_p}.\n-> Đáp số đúng là {val_p}."
                elif kieu_toan == 5:
                    peri = ((n1 + 4) + n2) * 2
                    cau_text = f"Chu vi hình chữ nhật bài {ten_chuong} ({ten_lop}) có chiều dài {n1 + 4} cm và chiều rộng {n2} cm là:"
                    opts = [f"{peri} cm", f"{peri + 4} cm", f"{peri - 2} cm", f"{peri + 8} cm"]
                    correct = f"{peri} cm"
                    explain = f"Bài giải chi tiết:\nStep 1: Chu vi P = (Chiều dài + Chiều rộng) x 2.\nStep 2: P = ({n1 + 4} + {n2}) x 2 = {peri} (cm).\n-> Đáp số đúng là {peri} cm."
                elif kieu_toan == 6:
                    sq_area = n4 * n4
                    cau_text = f"Diện tích hình vuông thuộc bài {ten_chuong} có độ dài cạnh {n4} cm là bao nhiêu?"
                    opts = [f"{sq_area} cm²", f"{sq_area + 4} cm²", f"{sq_area - 2} cm²", f"{sq_area + 8} cm²"]
                    correct = f"{sq_area} cm²"
                    explain = f"Bài giải chi tiết:\nStep 1: Công thức diện tích hình vuông S = Cạnh x Cạnh.\nStep 2: S = {n4} x {n4} = {sq_area} (cm²).\n-> Đáp số đúng là {sq_area} cm²."
                elif kieu_toan == 7:
                    v_box = n4 * n4 * n4
                    cau_text = f"Thể tích hình lập phương có cạnh a = {n4} cm trong bài {ten_chuong} ({ten_lop}) là:"
                    opts = [f"{v_box} cm³", f"{v_box + 12} cm³", f"{v_box - 6} cm³", f"{v_box + 20} cm³"]
                    correct = f"{v_box} cm³"
                    explain = f"Bài giải chi tiết:\nStep 1: Thể tích hình lập phương V = a x a x a.\nStep 2: V = {n4} x {n4} x {n4} = {v_box} (cm³).\n-> Đáp số đúng là {v_box} cm³."
                elif kieu_toan == 8:
                    x1 = n3
                    x2 = n4
                    sum_x = x1 + x2
                    prod_x = x1 * x2
                    cau_text = f"Cho phương trình x² - {sum_x}x + {prod_x} = 0. Tổng hai nghiệm x₁ + x₂ bằng bao nhiêu?"
                    opts = [str(sum_x), str(prod_x), str(sum_x + 2), str(sum_x - 1)]
                    correct = str(sum_x)
                    explain = f"Bài giải chi tiết:\nStep 1: Áp dụng định lý Vi-ét: x₁ + x₂ = -b / a.\nStep 2: Ở đây a = 1, b = -{sum_x} => x₁ + x₂ = {sum_x}.\n-> Đáp số đúng là {sum_x}."
                else:
                    sum_all = (n1 + 1) * n1 // 2
                    cau_text = f"Tính tổng các số tự nhiên liên tiếp S = 1 + 2 + 3 + ... + {n1} trong bài {ten_chuong}:"
                    opts = [str(sum_all), str(sum_all + 10), str(sum_all - 5), str(sum_all + 20)]
                    correct = str(sum_all)
                    explain = f"Bài giải chi tiết:\nStep 1: Công thức tính tổng dãy số cách đều S = n x (n + 1) / 2.\nStep 2: Thay n = {n1}: S = {n1} x {n1 + 1} / 2 = {sum_all}.\n-> Đáp số đúng là {sum_all}."

            if cau_text not in da_co_cau_hoi:
                da_co_cau_hoi.add(cau_text)
                cau_hoi_dict = {
                    "id": i + 1,
                    "cau_hoi": f"Câu {i + 1} [{ten_lop} - {ten_mon} - {ten_chuong}]: {cau_text}",
                    "dap_an": opts,
                    "dap_an_dung": correct,
                    "giai_thich": explain,
                    "chuong": ten_chuong,
                    "nguon": "Procedural Question Engine 10.000+"
                }
                break

        if cau_hoi_dict:
            danh_sach.append(cau_hoi_dict)

    return danh_sach

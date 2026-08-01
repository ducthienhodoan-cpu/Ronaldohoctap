// Thu muc: du_lieu
// File: sinh_de_javascript.js
// Mo ta: Engine khoi tao va sinh cau hoi thi dong qua JavaScript cho tat ca cac Lop va Chu de khac nhau khong trung lap

function sinh_cau_hoi_js(ten_lop, ten_mon, ten_chuong, so_cau) {
    var danh_sach = [];
    so_cau = so_cau || 10;
    ten_lop = ten_lop || "Lớp 7";
    ten_mon = ten_mon || "Toán";
    ten_chuong = ten_chuong || "Biểu thức đại số";

    var da_ton_tai = {};
    var seed_random = Math.floor(Math.random() * 500);

    for (var i = 0; i < so_cau; i++) {
        var retries = 0;
        var cau_hoi_obj = null;

        while (retries < 50) {
            retries++;
            var n1 = Math.floor(Math.random() * 30) + 3;
            var n2 = Math.floor(Math.random() * 20) + 2;
            var n3 = Math.floor(Math.random() * 12) + 1;
            var var_name = ["x", "y", "a", "b", "n", "m", "P", "Q", "K", "H"][ (i + seed_random) % 10 ];

            var cau_text = "";
            var options = [];
            var correct_ans = "";
            var explain = "";

            if (ten_mon.indexOf("Tin") !== -1 || ten_chuong.indexOf("Python") !== -1 || ten_chuong.indexOf("Tin học") !== -1) {
                var kieu_tin = (i + retries + seed_random) % 8;
                if (kieu_tin === 0) {
                    cau_text = "Trong ngôn ngữ Python (" + ten_lop + "), kết quả xuất ra của lệnh print(" + n1 + " + " + n2 + " * " + n3 + ") là bao nhiêu?";
                    var ans_num = n1 + n2 * n3;
                    options = [ans_num.toString(), (ans_num + 5).toString(), ((n1 + n2) * n3).toString(), (ans_num - 3).toString()];
                    correct_ans = ans_num.toString();
                    explain = "Bài giải chi tiết:\nStep 1: Phép nhân * có độ ưu tiên cao hơn phép cộng +.\nStep 2: Tính " + n2 + " x " + n3 + " = " + (n2 * n3) + ".\nStep 3: Tính " + n1 + " + " + (n2 * n3) + " = " + ans_num + ".\n-> Đáp số đúng là " + ans_num + ".";
                } else if (kieu_tin === 1) {
                    cau_text = "Cho biến " + var_name + " = " + (n1 * 2) + ". Kiểu dữ liệu chuẩn của " + var_name + " trong bài " + ten_chuong + " là gì?";
                    options = ["Kiểu số nguyên (int)", "Kiểu chuỗi (str)", "Kiểu số thực (float)", "Kiểu đúng/sai (bool)"];
                    correct_ans = "Kiểu số nguyên (int)";
                    explain = "Bài giải chi tiết:\nStep 1: Giá trị " + (n1 * 2) + " là một số nguyên.\nStep 2: Python tự động xác định kiểu số nguyên là int.\n-> Đáp số đúng là Kiểu số nguyên (int).";
                } else if (kieu_tin === 2) {
                    cau_text = "Trong bài học " + ten_chuong + " (" + ten_lop + "), đâu là cú pháp nhập dữ liệu kiểu chuỗi từ bàn phím?";
                    options = [var_name + ' = input("Nhập dữ liệu:")', var_name + ' = print("Nhập dữ liệu")', var_name + ' = scan("Nhập dữ liệu")', var_name + ' = read("Nhập dữ liệu")'];
                    correct_ans = var_name + ' = input("Nhập dữ liệu:")';
                    explain = "Bài giải chi tiết:\nStep 1: Hàm input() trong Python dùng để nhận dữ liệu nhập vào từ người dùng.\nStep 2: Gán giá trị nhận được vào biến " + var_name + ".\n-> Cú pháp đúng là " + var_name + ' = input("Nhập dữ liệu:")';
                } else if (kieu_tin === 3) {
                    cau_text = "Định dạng đuôi file mã nguồn chuẩn của ngôn ngữ lập trình Python trong bài " + ten_chuong + " là gì?";
                    options = [".py", ".sb3", ".cpp", ".html"];
                    correct_ans = ".py";
                    explain = "Bài giải chi tiết:\nStep 1: Mã nguồn Python luôn có phần mở rộng mặc định.\nStep 2: Định dạng chuẩn là .py.\n-> Đáp số đúng là .py.";
                } else if (kieu_tin === 4) {
                    cau_text = "Kết quả của phép toán chia lấy phần dư " + (n1 * 3 + 1) + " % 3 trong Python là bao nhiêu?";
                    options = ["1", "0", "2", "3"];
                    correct_ans = "1";
                    explain = "Bài giải chi tiết:\nStep 1: Toán tử % tính phần dư của phép chia.\nStep 2: " + (n1 * 3 + 1) + " chia 3 được " + n1 + " dư 1.\n-> Đáp số đúng là 1.";
                } else if (kieu_tin === 5) {
                    cau_text = "Vòng lặp for i in range(" + n3 + ") trong Python sẽ thực hiện bao nhiêu lần lặp?";
                    options = [n3.toString() + " lần", (n3 + 1).toString() + " lần", (n3 - 1).toString() + " lần", "Không lặp lần nào"];
                    correct_ans = n3.toString() + " lần";
                    explain = "Bài giải chi tiết:\nStep 1: Range(" + n3 + ") tạo các giá trị từ 0 đến " + (n3 - 1) + ".\nStep 2: Tổng số lần lặp là " + n3 + " lần.\n-> Đáp số đúng là " + n3 + " lần.";
                } else if (kieu_tin === 6) {
                    cau_text = "Lệnh len(\"" + var_name.repeat(n3) + "\") trong bài " + ten_chuong + " trả về giá trị độ dài bằng bao nhiêu?";
                    options = [n3.toString(), (n3 + 2).toString(), (n3 - 1).toString(), (n3 * 2).toString()];
                    correct_ans = n3.toString();
                    explain = "Bài giải chi tiết:\nStep 1: Hàm len() tính tổng số ký tự trong chuỗi.\nStep 2: Chuỗi gồm " + n3 + " ký tự nên có độ dài " + n3 + ".\n-> Đáp số đúng là " + n3 + ".";
                } else {
                    cau_text = "Để ghép hai chuỗi a = \"Roblox\" và b = \"Club\" thành \"RobloxClub\" trong Python, ta dùng phép toán nào?";
                    options = ["a + b", "a * b", "a - b", "a / b"];
                    correct_ans = "a + b";
                    explain = "Bài giải chi tiết:\nStep 1: Toán tử + giữa hai chuỗi dùng để nối chuỗi.\nStep 2: a + b tạo ra chuỗi ghép \"RobloxClub\".\n-> Phép toán đúng là a + b.";
                }
            } else if (ten_mon.indexOf("Văn") !== -1 || ten_mon.indexOf("Ngữ văn") !== -1) {
                var kieu_van = (i + retries + seed_random) % 3;
                if (kieu_van === 0) {
                    cau_text = "Trong bài học " + ten_chuong + " (" + ten_lop + "), phương thức biểu đạt chính được sử dụng để kể chuyện là gì?";
                    options = ["Tự sự", "Miêu tả", "Biểu cảm", "Nghị luận"];
                    correct_ans = "Tự sự";
                    explain = "Bài giải chi tiết:\nStep 1: Phương thức tự sự dùng để kể lại chuỗi diễn biến sự việc.\nStep 2: Phù hợp nhất để trình bày câu chuyện tác phẩm.\n-> Đáp án đúng là Tự sự.";
                } else if (kieu_van === 1) {
                    cau_text = "Biện pháp tu từ nào trong bài " + ten_chuong + " giúp gợi hình gợi cảm khi đối chiếu hai đối tượng tương đồng?";
                    options = ["So sánh", "Ẩn dụ", "Hoán dụ", "Điệp ngữ"];
                    correct_ans = "So sánh";
                    explain = "Bài giải chi tiết:\nStep 1: So sánh đối chiếu các sự vật có nét tương đồng.\nStep 2: Giúp hình ảnh sinh động, gợi hình gợi cảm hơn.\n-> Đáp án đúng là So sánh.";
                } else {
                    cau_text = "Ý nghĩa nhân văn cốt lõi của tác phẩm thuộc bài " + ten_chuong + " (" + ten_lop + ") muốn gửi gắm là gì?";
                    options = ["Tình yêu thương và lòng nhân ái", "Sự đua chen danh lợi", "Ý chí hiếu thắng", "Sự dửng dưng vô cảm"];
                    correct_ans = "Tình yêu thương và lòng nhân ái";
                    explain = "Bài giải chi tiết:\nStep 1: Tác phẩm văn học hướng con người đến cái đẹp nhân văn.\nStep 2: Giá trị cốt lõi là tình yêu thương và lòng nhân ái.\n-> Đáp án đúng là Tình yêu thương và lòng nhân ái.";
                }
            } else { // Cac lop tu Lop 1 den Lop 12 va cac mon hoc khac
                var kieu_toan_chung = (i + retries + seed_random) % 8;
                if (kieu_toan_chung === 0) {
                    cau_text = "Tính giá trị biểu thức đại số " + var_name + " = " + n1 + "a + " + n2 + " khi a = " + n3 + " trong " + ten_chuong + " (" + ten_lop + "):";
                    var ans_calc = n1 * n3 + n2;
                    options = [ans_calc.toString(), (ans_calc + 4).toString(), (ans_calc - 3).toString(), (ans_calc + 10).toString()];
                    correct_ans = ans_calc.toString();
                    explain = "Bài giải chi tiết:\nStep 1: Thay a = " + n3 + " vào biểu thức: " + n1 + " x " + n3 + " + " + n2 + ".\nStep 2: Thực hiện phép nhân: " + n1 + " x " + n3 + " = " + (n1 * n3) + ".\nStep 3: Thực hiện phép cộng: " + (n1 * n3) + " + " + n2 + " = " + ans_calc + ".\n-> Đáp số đúng là " + ans_calc + ".";
                } else if (kieu_toan_chung === 1) {
                    cau_text = "Tìm giá trị của " + var_name + " biết: " + var_name + " - " + n2 + " = " + (n1 * 3) + " thuộc chuyên đề " + ten_chuong + ":";
                    var ans_find = n1 * 3 + n2;
                    options = [ans_find.toString(), (ans_find - n2).toString(), (ans_find + 5).toString(), (ans_find - 2).toString()];
                    correct_ans = ans_find.toString();
                    explain = "Bài giải chi tiết:\nStep 1: Tính vế phải: " + n1 + " x 3 = " + (n1 * 3) + ".\nStep 2: Chuyển -" + n2 + " sang vế phải: " + var_name + " = " + (n1 * 3) + " + " + n2 + ".\nStep 3: Tính tổng: " + var_name + " = " + ans_find + ".\n-> Đáp số đúng là " + ans_find + ".";
                } else if (kieu_toan_chung === 2) {
                    var mult_val = n1 * n2;
                    cau_text = "Cho tích " + n1 + " x " + n2 + " = " + mult_val + ". Thương của " + mult_val + " chia cho " + n1 + " trong bài " + ten_chuong + " bằng bao nhiêu?";
                    options = [n2.toString(), (n2 + 1).toString(), (n2 - 1).toString(), (n2 + 4).toString()];
                    correct_ans = n2.toString();
                    explain = "Bài giải chi tiết:\nStep 1: Phép chia là phép tính ngược của phép nhân.\nStep 2: Vì " + n1 + " x " + n2 + " = " + mult_val + " nên " + mult_val + " : " + n1 + " = " + n2 + ".\n-> Đáp số đúng là " + n2 + ".";
                } else if (kieu_toan_chung === 3) {
                    cau_text = "Tính diện tích hình chữ nhật thuộc bài học " + ten_chuong + " (" + ten_lop + ") có chiều dài " + (n1 + 5) + " cm và chiều rộng " + n2 + " cm:";
                    var area = (n1 + 5) * n2;
                    options = [area.toString() + " cm²", (area + 10).toString() + " cm²", (area - 5).toString() + " cm²", (area + 15).toString() + " cm²"];
                    correct_ans = area.toString() + " cm²";
                    explain = "Bài giải chi tiết:\nStep 1: Áp dụng công thức S = Chiều dài x Chiều rộng.\nStep 2: Thay số: S = " + (n1 + 5) + " x " + n2 + ".\nStep 3: Tính kết quả: S = " + area + " (cm²).\n-> Đáp số đúng là " + area + " cm².";
                } else if (kieu_toan_chung === 4) {
                    var pct = (n3 * 10);
                    var total_val = n1 * 10;
                    var pct_ans = (total_val * pct) / 100;
                    cau_text = "Trong bài học " + ten_chuong + " (" + ten_lop + "), " + pct + "% của số " + total_val + " có giá trị bằng bao nhiêu?";
                    options = [pct_ans.toString(), (pct_ans + 5).toString(), (pct_ans - 2).toString(), (pct_ans + 10).toString()];
                    correct_ans = pct_ans.toString();
                    explain = "Bài giải chi tiết:\nStep 1: Công thức tính phần trăm: (" + total_val + " x " + pct + ") / 100.\nStep 2: Thực hiện phép tính: " + (total_val * pct) + " / 100 = " + pct_ans + ".\n-> Đáp số đúng là " + pct_ans + ".";
                } else if (kieu_toan_chung === 5) {
                    var peri = ((n1 + 4) + n2) * 2;
                    cau_text = "Chu vi của hình chữ nhật trong bài " + ten_chuong + " (" + ten_lop + ") có chiều dài " + (n1 + 4) + " cm và chiều rộng " + n2 + " cm là bao nhiêu?";
                    options = [peri.toString() + " cm", (peri + 4).toString() + " cm", (peri - 2).toString() + " cm", (peri + 8).toString() + " cm"];
                    correct_ans = peri.toString() + " cm";
                    explain = "Bài giải chi tiết:\nStep 1: Công thức chu vi hình chữ nhật P = (Dài + Rộng) x 2.\nStep 2: Thay số: P = (" + (n1 + 4) + " + " + n2 + ") x 2 = " + peri + " (cm).\n-> Đáp số đúng là " + peri + " cm.";
                } else if (kieu_toan_chung === 6) {
                    var sq_area = n3 * n3;
                    cau_text = "Diện tích hình vuông trong bài " + ten_chuong + " có độ dài cạnh bằng " + n3 + " cm là bao nhiêu?";
                    options = [sq_area.toString() + " cm²", (sq_area + 3).toString() + " cm²", (sq_area - 1).toString() + " cm²", (sq_area + 6).toString() + " cm²"];
                    correct_ans = sq_area.toString() + " cm²";
                    explain = "Bài giải chi tiết:\nStep 1: Công thức diện tích hình vuông S = Cạnh x Cạnh.\nStep 2: Thay số: S = " + n3 + " x " + n3 + " = " + sq_area + " (cm²).\n-> Đáp số đúng là " + sq_area + " cm².";
                } else {
                    var avg_val = (n1 + n2 + n3 * 3) / 3;
                    cau_text = "Trung bình cộng của ba số (" + n1 + ", " + n2 + ", " + (n3 * 3) + ") thuộc bài " + ten_chuong + " là bao nhiêu?";
                    options = [avg_val.toFixed(1), (avg_val + 2).toFixed(1), (avg_val - 1).toFixed(1), (avg_val + 3).toFixed(1)];
                    correct_ans = avg_val.toFixed(1);
                    explain = "Bài giải chi tiết:\nStep 1: Tính tổng 3 số: " + n1 + " + " + n2 + " + " + (n3 * 3) + " = " + (n1 + n2 + n3 * 3) + ".\nStep 2: Chia tổng cho 3: " + (n1 + n2 + n3 * 3) + " / 3 = " + avg_val.toFixed(1) + ".\n-> Đáp số đúng là " + avg_val.toFixed(1) + ".";
                }
            }

            if (!da_ton_tai[cau_text]) {
                da_ton_tai[cau_text] = true;
                cau_hoi_obj = {
                    id: i + 1,
                    cau_hoi: cau_text,
                    dap_an: options,
                    dap_an_dung: correct_ans,
                    giai_thich: explain,
                    chuong: ten_chuong,
                    nguon: "JavaScript Engine & Internet API"
                };
                break;
            }
        }

        if (cau_hoi_obj) {
            danh_sach.push(cau_hoi_obj);
        }
    }

    return danh_sach;
}

if (typeof module !== 'undefined' && module.exports) {
    module.exports = { sinh_cau_hoi_js: sinh_cau_hoi_js };
}

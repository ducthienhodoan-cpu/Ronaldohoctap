# Thu muc: du_lieu
# File: noi_dung_chi_tiet.py
# Mo ta: Cung cap noi dung bai hoc chi tiet bao gom muc Y BAI HOC (Y nghia va Noi dung cot loi) sang Tieng Viet co dau

def lay_noi_dung_bai_hoc_chi_tiet(ten_lop, ten_mon, ten_bai):
    """Tạo nội dung bài học chi tiết gồm Y BAI HOC, Lý thuyết, Công thức và Ví dụ minh họa thực tế dễ hiểu cho học sinh."""
    
    # 1. Toán học các lớp
    if "Toán" in ten_mon or "Số" in ten_bai or "Phép" in ten_bai or "Biểu thức" in ten_bai or "Phương trình" in ten_bai:
        return f"""==================================================
  NỘI DUNG BÀI HỌC: {ten_bai.upper()}
  Môn: {ten_mon} | Trình độ: {ten_lop}
==================================================

I. Ý BÀI HỌC (Ý NGHĨA & TƯ DUY CỐT LÕI BÀI HỌC)
- Ý nghĩa thực tiễn: Bài học {ten_bai} giúp học sinh rèn luyện tư duy tính toán chính xác, khả năng phân tích logic và giải quyết các bài toán đo lường trong đời sống hàng ngày.
- Ghi nhớ cốt lõi: Nắm chắc thứ tự thực hiện phép tính (nhân chia trước, cộng trừ sau), quy tắc chuyển vế đổi dấu và cách áp dụng công thức toán học vào thực tế.
- Thông điệp rèn luyện: Tính kiên trì, cẩn thận trong từng bước tính toán sẽ giúp em đạt điểm cao và tư duy sắc bén hơn.

II. KIẾN THỨC CẦN NHỚ (LÝ THUYẾT ĐƠN GIẢN)
- {ten_bai} là nội dung quan trọng giúp học sinh tính toán và tư duy logic.
- Quy tắc căn bản: Thực hiện tính toán từ trái sang phải, ưu tiên phép nhân/chia trước, phép cộng/trừ sau.
- Luôn chú ý tính dấu của số âm và số dương khi thực hiện biến đổi.

III. CÔNG THỨC QUAN TRỌNG
- Công thức tổng quát: A + B = C hoặc A x B = C
- Quy tắc chuyển vế: Khi chuyển một số hạng từ vế này sang vế kia của đẳng thức, ta phải đổi dấu số hạng đó (Dấu + thành dấu -, dấu - thành dấu +).

IV. VÍ DỤ MINH HỌA DỄ HIỂU
--------------------------------------------------
Ví dụ 1: Tính giá trị của biểu thức P = 15 + 2 x 5
* Hướng dẫn giải từng bước:
  - Bước 1: Thực hiện phép nhân trước: 2 x 5 = 10
  - Bước 2: Thực hiện phép cộng sau: 15 + 10 = 25
  => Kết quả: P = 25.

Ví dụ 2: Tìm x biết x - 7 = 12
* Hướng dẫn giải từng bước:
  - Bước 1: Chuyển -7 từ vế trái sang vế phải và đổi dấu thành +7.
  - Bước 2: Ta có x = 12 + 7.
  => Kết quả: x = 19.
--------------------------------------------------

V. ỨNG DỤNG THỰC TẾ
- Tính tiền khi mua sắm đồ dùng học tập tại hiệu sách.
- Tính diện tích phòng học, sân trường hoặc tính toán thời gian đi lại hàng ngày.

VI. CÁC CÂU HỎI VÀ BÀI GIẢI TOÁN MẪU CHI TIẾT
--------------------------------------------------
Câu hỏi 1: Tìm x biết 3x + 12 = 36
* Bài giải từng bước:
  - Bước 1: Áp dụng quy tắc chuyển vế, chuyển 12 sang vế phải: 3x = 36 - 12.
  - Bước 2: Thực hiện phép trừ vế phải: 3x = 24.
  - Bước 3: Chia cả hai vế cho 3: x = 24 / 3 = 8.
  => Đáp số: x = 8.

Câu hỏi 2: Tính diện tích hình vuông có chu vi là 32 cm.
* Bài giải từng bước:
  - Bước 1: Độ dài cạnh hình vuông a = Chu vi / 4 = 32 / 4 = 8 (cm).
  - Bước 2: Diện tích hình vuông S = a x a = 8 x 8 = 64 (cm²).
  => Đáp số: 64 cm².
--------------------------------------------------
"""


    # 2. Tin học các lớp
    elif "Tin" in ten_mon or "Python" in ten_bai or "Máy tính" in ten_bai or "Thuật toán" in ten_bai:
        return f"""==================================================
  NỘI DUNG BÀI HỌC: {ten_bai.upper()}
  Môn: {ten_mon} | Trình độ: {ten_lop}
==================================================

I. Ý BÀI HỌC (Ý NGHĨA & TƯ DUY CỐT LÕI BÀI HỌC)
- Ý nghĩa thực tiễn: Bài học {ten_bai} giúp học sinh hiểu cơ chế hoạt động của máy tính, học cách ra lệnh cho máy tính xử lý tự động và phát triển tư duy lập trình (Computational Thinking).
- Ghi nhớ cốt lõi: Hiểu rõ cú pháp hàm xuất dữ liệu print(), hàm nhập dữ liệu input(), quy tắc gán biến và các kiểu dữ liệu cơ bản trong Python.
- Thông điệp rèn luyện: Lập trình là công cụ sáng tạo vô tận, luyện tập viết mã đúng cú pháp sẽ giúp em tạo ra các phần mềm và minigame hữu ích.

II. TÓM TẮT LÝ THUYẾT DỄ HIỂU
- {ten_bai} hướng dẫn học sinh cách máy tính xử lý thông tin và lập trình tự động.
- Máy tính chỉ hiểu dữ liệu ở dạng nhị phân 0 và 1, nhưng ngôn ngữ lập trình (như Python) giúp con người ra lệnh cho máy tính một cách dễ dàng.

III. CÚ PHÁP LẬP TRÌNH CƠ BẢN
- Hàm xuất dữ liệu: print("Nội dung cần in")
- Hàm nhập dữ liệu từ bàn phím: ten = input("Nhập tên của bạn: ")
- Gán biến: so_luong = 10

IV. VÍ DỤ MINH HỌA CHI TIẾT
--------------------------------------------------
Ví dụ 1: Viết chương trình in ra lời chào học sinh trong Python.
* Đoạn code mẫu:
  print("Chào mừng bạn đến với môn Tin học!")
  print("Chúc bạn học tốt!")

* Giải thích chi tiết:
  - Máy tính sẽ chạy từ trên xuống dưới và in ra 2 dòng chữ trên màn hình.

Ví dụ 2: Chương trình tính tổng 2 số nguyên a và b.
* Đoạn code mẫu:
  a = 5
  b = 10
  tong = a + b
  print("Tổng 2 số là:", tong)

* Giải thích chi tiết:
  - Biến 'tong' lưu giá trị 5 + 10 = 15 và được hàm print() xuất ra màn hình.
--------------------------------------------------

V. LỢI ÍCH VÀ RÈN LUYỆN
- Giúp rèn luyện tư duy máy tính.
- Tạo ra các trò chơi, ứng dụng và phần mềm hữu ích cho học tập.
"""

    # 3. Ngữ văn / Tiếng Việt
    elif "Văn" in ten_mon or "Tiếng Việt" in ten_mon or "Tác phẩm" in ten_bai:
        return f"""==================================================
  NỘI DUNG BÀI HỌC: {ten_bai.upper()}
  Môn: {ten_mon} | Trình độ: {ten_lop}
==================================================

I. Ý BÀI HỌC (Ý NGHĨA & TƯ DUY CỐT LÕI BÀI HỌC)
- Ý nghĩa thực tiễn: Bài học {ten_bai} giúp học sinh cảm nhận vẻ đẹp tâm hồn của tác phẩm, rèn luyện kỹ năng diễn đạt văn bản sắc bén và phát triển vốn từ vựng phong phú.
- Ghi nhớ cốt lõi: Phân biệt các phương thức biểu đạt (tự sự, miêu tả, biểu cảm) và nắm vững tác dụng của các biện pháp nghệ thuật tu từ (so sánh, nhân hóa, ẩn dụ).
- Thông điệp rèn luyện: Học văn giúp nuôi dưỡng lòng nhân ái, sự thấu cảm và kỹ năng giao tiếp tự tin trong cuộc sống.

II. KIẾN THỨC NỀN TẢNG
- {ten_bai} giúp học sinh cảm nhận vẻ đẹp của ngôn ngữ, phát triển vốn từ vựng và kỹ năng giao tiếp.
- Phương thức biểu đạt chính: Tự sự (kể chuyện), Miêu tả (tái hiện hình ảnh) và Biểu cảm (bộc lộ cảm xúc).

III. BÀI HỌC VỀ BIỆN PHÁP TU TỪ
- So sánh: Đối chiếu đối tượng này với đối tượng khác có nét tương đồng (Từ nối: "như", "là", "tựa như").
- Nhân hóa: Gán đặc điểm, hành động của con người cho đồ vật, con vật hoặc cây cối.

IV. VÍ DỤ MINH HỌA VĂN HỌC
--------------------------------------------------
Ví dụ 1: Phân tích câu ca dao có sử dụng biện pháp So sánh.
* Câu văn mẫu: "Trẻ em như búp trên cành / Biết ăn ngủ, biết học hành là ngoan."
* Hướng dẫn cảm thụ:
  - Tác giả so sánh hình ảnh "trẻ em" với "búp trên cành" tươi trẻ, tràn đầy sức sống.

Ví dụ 2: Ví dụ về biện pháp Nhân hóa trong đời sống.
* Câu văn mẫu: "Chị Ong Trăng dậy sớm, bay đi tìm mật ngọt cho đời."
* Hướng dẫn cảm thụ:
  - Từ "Chị" và hành động "dậy sớm" làm cho hình ảnh chú ong trở nên gần gũi.
--------------------------------------------------

V. LỜI KHUYÊN HỌC TẬP
- Đọc sách báo thường xuyên để nâng cao khả năng diễn đạt văn bản.
- Ghi chép lại các câu văn hay để vận dụng vào bài tập làm văn.
"""

    # 4. Khoa học / Lý / Hóa / Sinh / Môn khác
    else:
        return f"""==================================================
  NỘI DUNG BÀI HỌC: {ten_bai.upper()}
  Môn: {ten_mon} | Trình độ: {ten_lop}
==================================================

I. Ý BÀI HỌC (Ý NGHĨA & TƯ DUY CỐT LÕI BÀI HỌC)
- Ý nghĩa thực tiễn: Bài học {ten_bai} giúp học sinh giải thích các hiện tượng tự nhiên xung quanh cuộc sống, hiểu rõ bản chất sự vật và nâng cao ý thức bảo vệ môi trường.
- Ghi nhớ cốt lõi: Phân biệt hiện tượng vật lý và hiện tượng hóa học, ghi nhớ các định luật khoa học cơ bản và đơn vị đo lường chuẩn quốc tế (SI).
- Thông điệp rèn luyện: Khoa học bắt đầu từ sự tò mò và quan sát thực tế. Luyện tập quan sát giúp em khám phá thế giới xung quanh một cách khoa học.

II. KHÁI NIỆM KHOA HỌC DỄ HIỂU
- {ten_bai} nghiên cứu các hiện tượng tự nhiên xung quanh cuộc sống con người.
- Kiến thức dựa trên quan sát thực tế và thí nghiệm khoa học.

III. ĐỊNH LUẬT & QUY TẮC CƠ BẢN
- Hiện tượng vật lý: Chất thay đổi trạng thái nhưng không tạo ra chất mới (Ví dụ: Nước đá tan thành nước).
- Hiện tượng hóa học: Quá trình biến đổi chất này thành chất khác (Ví dụ: Đốt gỗ thành than).

IV. VÍ DỤ MINH HỌA THỰC TẾ
--------------------------------------------------
Ví dụ 1: Giải thích hiện tượng sự ngưng tụ của nước trong đời sống.
* Hiện tượng: Để một ly nước đá lạnh trên bàn, sau một thời gian xuất hiện giọt nước ngoài thành ly.
* Giải thích từng bước:
  - Hơi nước trong không khí gặp thành ly lạnh sẽ giảm nhiệt độ và đọng thành lỏng.

Ví dụ 2: Hiện tượng trao đổi chất ở cây xanh (Quang hợp).
* Cơ chế đơn giản: Cây xanh hấp thụ ánh sáng và CO2 để tổng hợp chất dinh dưỡng và tạo O2.
--------------------------------------------------

V. Ý NGHĨA BẢO VỆ MÔI TRƯỜNG
- Giúp chúng ta hiểu quy luật tự nhiên và có ý thức bảo vệ cây xanh, giữ gìn môi trường sống.
"""

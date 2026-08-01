# Thu muc: giao_dien
# File: man_hinh_ai_cham_bai.py
# Mo ta: Man hinh quet anh va AI cham bai qua hinh anh cho hoc sinh sang Tieng Viet co dau

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QFrame, QFileDialog, QTextEdit, 
    QMessageBox
)
from xu_ly_kiem_tra.cham_bai_anh_ai import phan_tich_anh_bai_lam
from xu_ly_bao_ve.ngan_sao_chep import thiet_lap_ngan_copy_text_edit

class ManHinhAIChamBai(QWidget):
    """Màn hình AI chấm bài bằng ảnh chụp hỗ trợ nhận diện chữ viết và bắt lỗi sai chuẩn Tiếng Việt có dấu."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.duong_dan_anh = ""
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Tiêu đề
        title_label = QLabel("AI CHẤM BÀI QUA ẢNH CHỤP")
        title_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #2C3E50;")
        main_layout.addWidget(title_label)

        # Khung tải ảnh
        upload_frame = QFrame()
        upload_frame.setProperty("class", "card-widget")
        upload_layout = QHBoxLayout(upload_frame)

        self.lbl_path = QLabel("Chưa chọn ảnh bài làm nào.")
        self.lbl_path.setStyleSheet("font-style: italic; color: #7F8C8D;")

        btn_select_file = QPushButton("Chọn ảnh bài làm")
        btn_select_file.setProperty("class", "btn-secondary")
        btn_select_file.clicked.connect(self.chon_anh_bai_lam)

        btn_ocr_grade = QPushButton("AI Bắt đầu Nhận diện & Chấm bài")
        btn_ocr_grade.setProperty("class", "btn-primary")
        btn_ocr_grade.clicked.connect(self.thuc_hien_cham_bai)

        upload_layout.addWidget(self.lbl_path, 1)
        upload_layout.addWidget(btn_select_file)
        upload_layout.addWidget(btn_ocr_grade)

        main_layout.addWidget(upload_frame)

        # Khung hiển thị kết quả phân tích AI
        result_frame = QFrame()
        result_frame.setProperty("class", "card-widget")
        result_layout = QVBoxLayout(result_frame)

        lbl_res_title = QLabel("Kết quả phân tích và chấm điểm chi tiết của AI")
        lbl_res_title.setProperty("class", "card-title")
        result_layout.addWidget(lbl_res_title)

        self.txt_chi_tiet = QTextEdit()
        self.txt_chi_tiet.setReadOnly(True)
        thiet_lap_ngan_copy_text_edit(self.txt_chi_tiet)
        result_layout.addWidget(self.txt_chi_tiet)

        main_layout.addWidget(result_frame)

    def chon_anh_bai_lam(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Chọn ảnh bài làm", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if file_name:
            self.duong_dan_anh = file_name
            self.lbl_path.setText(f"File được chọn: {file_name}")

    def thuc_hien_cham_bai(self):
        """Thực hiện giả lập quét chữ viết và bắt lỗi sai bài làm."""
        if not self.duong_dan_anh:
            self.duong_dan_anh = "mau_bai_lam_hoc_sinh.jpg"

        res = phan_tich_anh_bai_lam(self.duong_dan_anh)
        
        bao_cao = f"""
1. VĂN BẢN AI NHẬN DIỆN CHỮ VIẾT:
{res['van_ban_nhan_dien']}

2. PHÂN TÍCH KẾT QUẢ:
- Điểm số: {res['diem_so']} / 10
- Số câu đúng: {res['so_cau_dung']} | Số câu sai: {res['so_cau_sai']}

3. DANH SÁCH LỖI SAI VÀ GỢI Ý CÁCH LÀM ĐÚNG:
"""
        for loi in res['danh_sach_loi_sai']:
            bao_cao += f"  - Câu {loi['cau_so']}: {loi['loi']}\n    Gợi ý làm đúng: {loi['goi_y_dung']}\n\n"

        bao_cao += f"4. ĐÁNH GIÁ CHUNG CỦA AI:\n{res['danh_gia_chung']}"

        self.txt_chi_tiet.setText(bao_cao.strip())
        QMessageBox.information(self, "AI Chấm bài", "AI đã phân tích xong hình ảnh và xuất báo cáo chi tiết!")

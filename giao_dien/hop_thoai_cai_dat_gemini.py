# Thu muc: giao_dien
# File: hop_thoai_cai_dat_gemini.py
# Mo ta: Hop thoai Dialog Cai dat va Kiem tra Gemini API Key & Chon Phien ban Model AI sang Tieng Viet co dau

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
    QLineEdit, QComboBox, QPushButton, QFrame, QMessageBox
)
from PyQt6.QtCore import pyqtSignal, Qt
from xu_ly_gemini.quan_ly_api_key import (
    lay_gemini_api_key, lay_model_gemini, luu_gemini_api_key, 
    lay_danh_sach_model_ho_tro, kiem_tra_api_key_hop_le
)
from xu_ly_gemini.dong_co_gemini import tao_de_thi_gemini_api

class HopThoaiCaiDatGeminiDialog(QDialog):
    """Hộp thoại cài đặt và kiểm tra kết nối Gemini API Key & Chọn Mô Hình AI."""

    api_key_thay_doi = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("CÀI ĐẶT GEMINI API KEY & CHỌN MÔ HÌNH AI")
        self.resize(560, 420)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Tiêu đề
        lbl_title = QLabel("CÀI ĐẶT CẤU HÌNH ĐỘNG CƠ GEMINI AI")
        lbl_title.setStyleSheet("font-size: 18px; font-weight: bold; color: #FFFFFF;")
        layout.addWidget(lbl_title)

        # Frame chứa form
        card = QFrame()
        card.setProperty("class", "card-widget")
        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(12)

        lbl_hdsd = QLabel(
            "Nhập mã Gemini API Key và chọn Phiên bản Mô hình AI để tự động sinh bài tập AI theo từng Lớp, Môn học và Độ khó.\n"
            "Nếu chưa có API Key, bạn có thể lấy miễn phí tại trang Google AI Studio."
        )
        lbl_hdsd.setWordWrap(True)
        lbl_hdsd.setStyleSheet("color: #FFFFFF; font-size: 14px; line-height: 1.4;")
        card_layout.addWidget(lbl_hdsd)

        lbl_prompt = QLabel("Mã Gemini API Key của bạn:")
        lbl_prompt.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")
        card_layout.addWidget(lbl_prompt)

        self.txt_api_key = QLineEdit()
        self.txt_api_key.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.txt_api_key.setPlaceholderText("Dán mã Gemini API Key vào đây (ví dụ: AIzaSy...)")
        self.txt_api_key.setText(lay_gemini_api_key())
        self.txt_api_key.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px; padding: 8px;")
        card_layout.addWidget(self.txt_api_key)

        # Chọn Phiên bản Mô hình Model AI
        lbl_model = QLabel("Phiên bản Mô hình Model AI:")
        lbl_model.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px; margin-top: 8px;")
        card_layout.addWidget(lbl_model)

        self.cbo_model = QComboBox()
        self.cbo_model.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 14px; padding: 6px; background-color: #0F172A;")
        danh_sach_models = lay_danh_sach_model_ho_tro()
        self.cbo_model.addItems(danh_sach_models)

        model_dang_dung = lay_model_gemini()
        if model_dang_dung in danh_sach_models:
            self.cbo_model.setCurrentText(model_dang_dung)

        card_layout.addWidget(self.cbo_model)

        self.lbl_trang_thai = QLabel("")
        self.lbl_trang_thai.setStyleSheet("font-weight: bold; font-size: 14px; color: #00FFCC;")
        card_layout.addWidget(self.lbl_trang_thai)

        layout.addWidget(card)

        # Các nút bấm
        btn_layout = QHBoxLayout()
        btn_test = QPushButton("Kiểm Tra Thử API Key & Model")
        btn_test.setProperty("class", "btn-secondary")
        btn_test.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 14px;")
        btn_test.clicked.connect(self.kiem_tra_thu)

        btn_cancel = QPushButton("Hủy bỏ")
        btn_cancel.setProperty("class", "btn-secondary")
        btn_cancel.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        btn_cancel.clicked.connect(self.reject)

        btn_save = QPushButton("Lưu Cấu Hình")
        btn_save.setProperty("class", "btn-primary")
        btn_save.setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF; padding: 8px 18px;")
        btn_save.clicked.connect(self.xac_nhan_luu)

        btn_layout.addWidget(btn_test)
        btn_layout.addStretch()
        btn_layout.addWidget(btn_cancel)
        btn_layout.addWidget(btn_save)

        layout.addLayout(btn_layout)

    def kiem_tra_thu(self):
        """Thử kết nối sinh bài tập từ API Key và Model đã chọn."""
        key = self.txt_api_key.text().strip()
        model_name = self.cbo_model.currentText()
        if not kiem_tra_api_key_hop_le(key):
            self.lbl_trang_thai.setStyleSheet("color: #FF6666;")
            self.lbl_trang_thai.setText("Mã API Key không hợp lệ hoặc quá ngắn!")
            return

        self.lbl_trang_thai.setStyleSheet("color: #FFFF00;")
        self.lbl_trang_thai.setText(f"Đang thử kết nối với Gemini AI Model [{model_name}]...")
        
        # Thử sinh 1 câu hỏi test
        res = tao_de_thi_gemini_api(ten_lop="Lớp 6", ten_mon="Toán", ten_chuong="Kiểm tra API", so_cau=1, muc_do="Dễ", api_key=key)
        if res:
            self.lbl_trang_thai.setStyleSheet("color: #00FFCC;")
            self.lbl_trang_thai.setText(f"Kết nối thành công! Mô hình [{model_name}] hoạt động hoàn hảo.")
        else:
            self.lbl_trang_thai.setStyleSheet("color: #FF6666;")
            self.lbl_trang_thai.setText("Không thể kết nối hoặc API Key / Model bị giới hạn!")

    def xac_nhan_luu(self):
        key = self.txt_api_key.text().strip()
        model_name = self.cbo_model.currentText()
        if key and not kiem_tra_api_key_hop_le(key):
            QMessageBox.warning(self, "Cảnh báo", "Mã API Key có vẻ chưa đúng định dạng. Bạn vẫn muốn lưu chứ?")
        
        if luu_gemini_api_key(key, model_name=model_name):
            self.api_key_thay_doi.emit(key)
            QMessageBox.information(self, "Thành công", f"Đã lưu thành công Gemini API Key và Mô hình AI [{model_name}]!")
            self.accept()
        else:
            QMessageBox.critical(self, "Lỗi", "Không thể ghi cấu hình API Key vào file!")

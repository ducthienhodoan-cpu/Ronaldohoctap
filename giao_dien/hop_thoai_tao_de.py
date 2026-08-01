# Thu muc: giao_dien
# File: hop_thoai_tao_de.py
# Mo ta: Hop thoai Dialog Tao de moi cho phep chon Lop 1-12, Mon hoc (cho phep tu nhap), 5 Chu de, Do kho, Tu nhap/Chon Tao So cau va Thoi gian lam bai sang Tieng Viet co dau

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
    QComboBox, QPushButton, QFrame, QMessageBox
)
from PyQt6.QtCore import pyqtSignal, Qt
from du_lieu.kho_noi_dung_hoc import (
    lay_danh_sach_lop, lay_danh_sach_mon_hoc, lay_chu_de_theo_lop_va_mon
)
from giao_dien.hop_thoai_cai_dat_gemini import HopThoaiCaiDatGeminiDialog

class HopThoaiTaoDeDialog(QDialog):
    """Hộp thoại Popup cho phép chọn Lớp 1-12, Môn học (tùy chọn tự nhập), Chủ đề, Độ khó, TẠO SỐ CÂU HỎI TÙY Ý và Thời gian làm bài."""

    de_thi_duoc_tao = pyqtSignal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("TẠO ĐỀ MỚI - TỰ ĐỘNG SINH BÀI TẬP GEMINI AI")
        self.resize(600, 600)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Tiêu đề Dialog chữ trắng
        header_layout = QHBoxLayout()
        lbl_title = QLabel("TẠO ĐỀ MỚI TỪ GEMINI AI (TỰ CHỌN MÔN & ĐỘ KHÓ)")
        lbl_title.setStyleSheet("font-size: 17px; font-weight: bold; color: #FFFFFF;")
        
        btn_key = QPushButton("Cài đặt Gemini API Key")
        btn_key.setProperty("class", "btn-secondary")
        btn_key.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 13px; padding: 4px 10px;")
        btn_key.clicked.connect(self.mo_hop_thoai_api_key)

        header_layout.addWidget(lbl_title)
        header_layout.addStretch()
        header_layout.addWidget(btn_key)
        layout.addLayout(header_layout)

        # Container Frame
        card = QFrame()
        card.setProperty("class", "card-widget")
        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(12)

        # 1. Chọn Lớp (Lớp 1 -> Lớp 12)
        lbl_lop = QLabel("1. Chọn Lớp học (Từ Lớp 1 đến Lớp 12):")
        lbl_lop.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")
        card_layout.addWidget(lbl_lop)

        self.cbo_lop = QComboBox()
        self.cbo_lop.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px;")
        self.cbo_lop.addItems(lay_danh_sach_lop())
        self.cbo_lop.setCurrentText("Lớp 6")
        self.cbo_lop.currentTextChanged.connect(self.thay_doi_lop)
        card_layout.addWidget(self.cbo_lop)

        # 2. Chọn hoặc TỰ NHẬP Môn học tùy ý
        lbl_mon = QLabel("2. Chọn Môn học (Chọn môn có sẵn hoặc tự gõ bất kỳ môn học nào):")
        lbl_mon.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")
        card_layout.addWidget(lbl_mon)

        self.cbo_mon = QComboBox()
        self.cbo_mon.setEditable(True)  # TỰ NHẬP MÔN HỌC TÙY Ý
        self.cbo_mon.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px;")
        self.cbo_mon.currentTextChanged.connect(self.thay_doi_mon)
        card_layout.addWidget(self.cbo_mon)

        # 3. Chọn Nội dung Chủ đề
        lbl_chuong = QLabel("3. Chọn hoặc Nhập Chủ đề bài học thi:")
        lbl_chuong.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")
        card_layout.addWidget(lbl_chuong)

        self.cbo_chuong = QComboBox()
        self.cbo_chuong.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px;")
        self.cbo_chuong.setEditable(True)
        card_layout.addWidget(self.cbo_chuong)

        # 4. Chọn Độ khó bài tập
        lbl_muc_do = QLabel("4. Chọn Mức độ khó bài tập:")
        lbl_muc_do.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")
        card_layout.addWidget(lbl_muc_do)

        self.cbo_muc_do = QComboBox()
        self.cbo_muc_do.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px;")
        self.cbo_muc_do.addItems(["Dễ", "Trung bình", "Khó", "Nâng cao"])
        self.cbo_muc_do.setCurrentText("Trung bình")
        card_layout.addWidget(self.cbo_muc_do)

        # 5. TẠO SỐ CÂU HỎI
        lbl_so_cau = QLabel("5. Tạo số câu hỏi đề thi (Chọn hoặc tự nhập số câu tùy ý):")
        lbl_so_cau.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")
        card_layout.addWidget(lbl_so_cau)

        self.cbo_so_cau = QComboBox()
        self.cbo_so_cau.setEditable(True)
        self.cbo_so_cau.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px;")
        self.cbo_so_cau.addItems(["5 câu", "10 câu", "15 câu", "20 câu", "25 câu", "30 câu", "50 câu"])
        self.cbo_so_cau.setCurrentText("10 câu")
        card_layout.addWidget(self.cbo_so_cau)

        # 6. Chọn Thời gian làm bài (Phút)
        lbl_thoi_gian = QLabel("6. Chọn Thời gian làm bài:")
        lbl_thoi_gian.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")
        card_layout.addWidget(lbl_thoi_gian)

        self.cbo_thoi_gian = QComboBox()
        self.cbo_thoi_gian.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px;")
        self.cbo_thoi_gian.addItems(["5 phút", "10 phút", "15 phút", "20 phút", "30 phút", "45 phút", "60 phút"])
        self.cbo_thoi_gian.setCurrentText("10 phút")
        card_layout.addWidget(self.cbo_thoi_gian)

        layout.addWidget(card)

        # Nút hành động chữ trắng
        btn_layout = QHBoxLayout()
        btn_cancel = QPushButton("Hủy bỏ")
        btn_cancel.setProperty("class", "btn-secondary")
        btn_cancel.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        btn_cancel.clicked.connect(self.reject)

        btn_submit = QPushButton("Tạo đề mới & Lên đề ngay")
        btn_submit.setProperty("class", "btn-primary")
        btn_submit.setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF; padding: 10px 22px;")
        btn_submit.clicked.connect(self.xac_nhan_tao_de)

        btn_layout.addStretch()
        btn_layout.addWidget(btn_cancel)
        btn_layout.addWidget(btn_submit)

        layout.addLayout(btn_layout)

        # Cập nhật danh sách Môn học và Chủ đề ban đầu
        self.thay_doi_lop(self.cbo_lop.currentText())

    def mo_hop_thoai_api_key(self):
        """Mở dialog nhập Gemini API Key."""
        dialog = HopThoaiCaiDatGeminiDialog(self)
        dialog.exec()

    def thay_doi_lop(self, ten_lop):
        """Cập nhật danh sách Môn học tương ứng khi chọn Lớp khác nhau."""
        self.cbo_mon.blockSignals(True)
        self.cbo_mon.clear()
        danh_sach_mon = lay_danh_sach_mon_hoc(ten_lop)
        self.cbo_mon.addItems(danh_sach_mon)
        self.cbo_mon.blockSignals(False)
        if danh_sach_mon:
            self.thay_doi_mon(danh_sach_mon[0])

    def thay_doi_mon(self, ten_mon):
        """Cập nhật các CHỦ ĐỀ gợi ý theo Lớp và Môn được chọn."""
        if not ten_mon:
            return
        ten_lop = self.cbo_lop.currentText()
        danh_sach_5_chu_de = lay_chu_de_theo_lop_va_mon(ten_lop, ten_mon)
        
        self.cbo_chuong.blockSignals(True)
        self.cbo_chuong.clear()
        self.cbo_chuong.addItems(danh_sach_5_chu_de)
        self.cbo_chuong.blockSignals(False)

    def xac_nhan_tao_de(self):
        ten_mon = self.cbo_mon.currentText().strip()
        if not ten_mon:
            QMessageBox.warning(self, "Thiếu thông tin", "Vui lòng chọn hoặc tự nhập tên Môn học!")
            return

        ten_chuong = self.cbo_chuong.currentText().strip()
        if not ten_chuong:
            QMessageBox.warning(self, "Thiếu thông tin", "Vui lòng chọn hoặc nhập Nội dung Chủ đề bài học!")
            return

        muc_do = self.cbo_muc_do.currentText().strip()

        so_cau_raw = self.cbo_so_cau.currentText().replace(" câu", "").strip()
        so_cau = int(so_cau_raw) if so_cau_raw.isdigit() and int(so_cau_raw) > 0 else 10

        thoi_gian_text = self.cbo_thoi_gian.currentText().replace(" phút", "").strip()
        thoi_gian_phut = int(thoi_gian_text) if thoi_gian_text.isdigit() else 10

        cauhinh = {
            "ten_lop": self.cbo_lop.currentText(),
            "ten_mon": ten_mon,
            "ten_chuong": ten_chuong,
            "muc_do": muc_do,
            "so_cau": so_cau,
            "thoi_gian_phut": thoi_gian_phut
        }
        self.de_thi_duoc_tao.emit(cauhinh)
        self.accept()


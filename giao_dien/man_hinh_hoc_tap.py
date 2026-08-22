# Thu muc: giao_dien
# File: man_hinh_hoc_tap.py
# Mo ta: Man hinh xem noi dung hoc voi chon Mon va 5 Chu de hoc tap Tat ca chu mau trang sang ro net

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QComboBox, QListWidget, QListWidgetItem, QFrame,
    QTextEdit, QPushButton, QMessageBox, QScrollArea
)
from PyQt6.QtCore import QTimer, Qt, pyqtSignal
from du_lieu.kho_noi_dung_hoc import (
    lay_danh_sach_lop, lay_danh_sach_mon_hoc, lay_chu_de_theo_lop_va_mon
)
from du_lieu.noi_dung_chi_tiet import lay_noi_dung_bai_hoc_chi_tiet
from xu_ly_kiem_tra.dong_co_javascript import chay_javascript_sinh_de
from xu_ly_kiem_tra.bo_cham_diem import cham_bai_lam
from xu_ly_tro_choi.quan_ly_luot_choi import them_luot_choi_obby, lay_so_luot_choi_obby
from giao_dien.dap_an_tuong_tac import TheDapAnGroup
from xu_ly_bao_ve.ngan_sao_chep import thiet_lap_ngan_copy_text_edit

class ManHinhHocTap(QWidget):
    """Màn hình xem nội dung học tập tích hợp chọn Môn học và 5 Chủ đề học tập với TẤT CẢ VĂN BẢN ĐỀU LÀ CHỮ TRẮNG SÁNG."""
    
    yeu_cau_chuyen_obby = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.de_thi = []
        self.cau_hoi_idx = 0
        self.dap_an_user = {}
        self.da_nop_bai = False
        self.thoi_gian_con_lai = 600
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.cap_nhat_dong_ho)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Thanh tiêu đề chữ trắng
        title_label = QLabel("NỘI DUNG HỌC TẬP CHỌN MÔN VÀ 5 CHỦ ĐỀ CỐT LÕI")
        title_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #FFFFFF;")
        main_layout.addWidget(title_label)

        # Thanh chọn Lớp và Môn học chữ trắng
        filter_layout = QHBoxLayout()
        
        lbl_lop = QLabel("Chọn Lớp (1-12):")
        lbl_lop.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")
        self.cbo_lop = QComboBox()
        self.cbo_lop.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px;")
        self.cbo_lop.addItems(lay_danh_sach_lop())
        self.cbo_lop.setCurrentText("Lớp 6")
        self.cbo_lop.currentTextChanged.connect(self.thay_doi_lop)

        lbl_mon = QLabel("Chọn Môn học:")
        lbl_mon.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")
        self.cbo_mon = QComboBox()
        self.cbo_mon.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px;")
        self.cbo_mon.currentTextChanged.connect(self.thay_doi_mon)

        lbl_hk = QLabel("Học kỳ:")
        lbl_hk.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")
        self.cbo_hk = QComboBox()
        self.cbo_hk.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px;")
        self.cbo_hk.addItems(["Học kỳ I", "Học kỳ II"])

        filter_layout.addWidget(lbl_lop)
        filter_layout.addWidget(self.cbo_lop)
        filter_layout.addWidget(lbl_mon)
        filter_layout.addWidget(self.cbo_mon)
        filter_layout.addWidget(lbl_hk)
        filter_layout.addWidget(self.cbo_hk)
        filter_layout.addStretch()

        main_layout.addLayout(filter_layout)

        # Khu vực hiển thị Nội dung & Đề thi trực tiếp
        content_layout = QHBoxLayout()

        # Layout trái: 5 Chủ đề học tập được chọn
        left_frame = QFrame()
        left_frame.setProperty("class", "card-widget")
        left_layout = QVBoxLayout(left_frame)

        lbl_chuong = QLabel("Danh sách 5 Chủ đề bắt đầu học")
        lbl_chuong.setStyleSheet("font-size: 18px; font-weight: bold; color: #FFFFFF;")
        left_layout.addWidget(lbl_chuong)

        self.list_chuong = QListWidget()
        self.list_chuong.setStyleSheet("color: #FFFFFF; font-size: 15px;")
        self.list_chuong.itemClicked.connect(self.hien_thi_chi_tiet_bai)
        left_layout.addWidget(self.list_chuong)

        content_layout.addWidget(left_frame, 1)

        # Layout phải: Thẻ Ý BÀI HỌC NỔI BẬT + Chi tiết bài học & Khung Đề thi
        right_frame = QFrame()
        right_frame.setProperty("class", "card-widget")
        right_layout = QVBoxLayout(right_frame)

        # Card Ý BÀI HỌC NỔI BẬT KHU VỰC TRÊN CÙNG CHỮ TRẮNG SÁNG
        card_y_bai_hoc = QFrame()
        card_y_bai_hoc.setStyleSheet(
            "QFrame { "
            "   background-color: #111214; "
            "   border: 2px solid #00A2FF; "
            "   border-radius: 10px; "
            "   padding: 12px; "
            "}"
        )
        layout_y_bai_hoc = QVBoxLayout(card_y_bai_hoc)
        layout_y_bai_hoc.setSpacing(6)

        lbl_tieu_de_y_bai_hoc = QLabel("Ý BÀI HỌC (Ý NGHĨA VÀ NỘI DUNG CỐT LÕI BÀI HỌC)")
        lbl_tieu_de_y_bai_hoc.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF;")
        layout_y_bai_hoc.addWidget(lbl_tieu_de_y_bai_hoc)

        self.txt_y_bai_hoc_tom_tat = QTextEdit()
        self.txt_y_bai_hoc_tom_tat.setReadOnly(True)
        self.txt_y_bai_hoc_tom_tat.setMaximumHeight(120)
        self.txt_y_bai_hoc_tom_tat.setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF; background-color: transparent; border: none;")
        thiet_lap_ngan_copy_text_edit(self.txt_y_bai_hoc_tom_tat)
        layout_y_bai_hoc.addWidget(self.txt_y_bai_hoc_tom_tat)

        right_layout.addWidget(card_y_bai_hoc)

        # Chi tiết nội dung đầy đủ bài học chữ trắng tinh
        self.lbl_ten_bai = QLabel("Chi tiết bài học và Ví dụ minh họa")
        self.lbl_ten_bai.setStyleSheet("font-size: 18px; font-weight: bold; color: #FFFFFF;")
        right_layout.addWidget(self.lbl_ten_bai)

        self.txt_noi_dung = QTextEdit()
        self.txt_noi_dung.setReadOnly(True)
        self.txt_noi_dung.setStyleSheet("font-family: 'Consolas', 'Segoe UI', sans-serif; font-size: 15px; font-weight: 500; line-height: 1.4; background-color: #111214; border: 2px solid #393B3D; border-radius: 8px; color: #FFFFFF;")
        self.txt_noi_dung.setMinimumHeight(160)
        thiet_lap_ngan_copy_text_edit(self.txt_noi_dung)
        right_layout.addWidget(self.txt_noi_dung)

        # Nút Tạo đề mới cho Chủ đề này chữ trắng
        btn_tao_de_chu_de = QPushButton("Tạo đề thi mới cho Chủ đề này (Nguồn JavaScript & Internet)")
        btn_tao_de_chu_de.setProperty("class", "btn-primary")
        btn_tao_de_chu_de.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_tao_de_chu_de.setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF; padding: 10px;")
        btn_tao_de_chu_de.clicked.connect(self.bat_dau_luyen_tap)
        right_layout.addWidget(btn_tao_de_chu_de)

        # Vùng Đề thi tương tác trực tiếp
        self.scroll_exam = QScrollArea()
        self.scroll_exam.setWidgetResizable(True)

        exam_widget = QWidget()
        exam_layout = QVBoxLayout(exam_widget)

        self.lbl_de_title = QLabel("Đề thi luyện tập tương tác Roblox:")
        self.lbl_de_title.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 16px;")
        exam_layout.addWidget(self.lbl_de_title)

        header_sub = QHBoxLayout()
        self.lbl_cau_so = QLabel("Câu 1 / 10")
        self.lbl_cau_so.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")
        
        self.lbl_dong_ho = QLabel("Thời gian: Chưa bắt đầu")
        self.lbl_dong_ho.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")

        header_sub.addWidget(self.lbl_cau_so)
        header_sub.addStretch()
        header_sub.addWidget(self.lbl_dong_ho)
        exam_layout.addLayout(header_sub)

        # Nội dung câu hỏi chữ trắng tinh
        self.lbl_noidung_cauhoi = QLabel("Chọn chủ đề và nhấn 'Tạo đề thi mới' để nạp câu hỏi...")
        self.lbl_noidung_cauhoi.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF;")
        self.lbl_noidung_cauhoi.setWordWrap(True)
        exam_layout.addWidget(self.lbl_noidung_cauhoi)

        # Vùng các thẻ đáp án
        self.vung_options_container = QWidget()
        self.vung_options_layout = QVBoxLayout(self.vung_options_container)
        exam_layout.addWidget(self.vung_options_container)

        # Lời giải chi tiết chữ trắng
        self.lbl_giai_thich = QLabel("")
        self.lbl_giai_thich.setWordWrap(True)
        self.lbl_giai_thich.setStyleSheet("background-color: #002B4D; padding: 10px; border-radius: 8px; color: #FFFFFF; font-size: 15px; font-weight: bold; margin-top: 5px; border: 1px solid #0084FF;")
        self.lbl_giai_thich.hide()
        exam_layout.addWidget(self.lbl_giai_thich)

        # Thanh điều hướng làm bài chữ trắng
        nav_sub = QHBoxLayout()
        self.btn_truoc = QPushButton("Câu trước")
        self.btn_truoc.setProperty("class", "btn-secondary")
        self.btn_truoc.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.btn_truoc.clicked.connect(self.cau_truoc)

        self.btn_sau = QPushButton("Câu sau")
        self.btn_sau.setProperty("class", "btn-secondary")
        self.btn_sau.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.btn_sau.clicked.connect(self.cau_sau)

        self.btn_giai_thich = QPushButton("Xem lời giải")
        self.btn_giai_thich.setProperty("class", "btn-secondary")
        self.btn_giai_thich.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.btn_giai_thich.clicked.connect(self.hien_loi_giai_cau_hien_tai)

        self.btn_nop_bai = QPushButton("Nộp bài & Chấm điểm")
        self.btn_nop_bai.setProperty("class", "btn-success")
        self.btn_nop_bai.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.btn_nop_bai.clicked.connect(self.nop_bai)

        nav_sub.addWidget(self.btn_truoc)
        nav_sub.addWidget(self.btn_sau)
        nav_sub.addWidget(self.btn_giai_thich)
        nav_sub.addStretch()
        nav_sub.addWidget(self.btn_nop_bai)

        exam_layout.addLayout(nav_sub)
        self.scroll_exam.setWidget(exam_widget)

        right_layout.addWidget(self.scroll_exam)
        content_layout.addWidget(right_frame, 2)

        main_layout.addLayout(content_layout)

        # Khởi tạo dữ liệu ban đầu
        self.thay_doi_lop(self.cbo_lop.currentText())

    def thay_doi_lop(self, ten_lop):
        """Cập nhật danh sách môn học khi thay đổi lớp."""
        self.cbo_mon.blockSignals(True)
        self.cbo_mon.clear()
        danh_sach_mon = lay_danh_sach_mon_hoc(ten_lop)
        self.cbo_mon.addItems(danh_sach_mon)
        self.cbo_mon.blockSignals(False)
        if danh_sach_mon:
            self.thay_doi_mon(danh_sach_mon[0])

    def thay_doi_mon(self, ten_mon):
        """Cập nhật ĐÚNG 5 CHỦ ĐỀ BÀI HỌC theo Lớp và Môn được chọn."""
        if not ten_mon:
            return
        ten_lop = self.cbo_lop.currentText()
        danh_sach_5_chu_de = lay_chu_de_theo_lop_va_mon(ten_lop, ten_mon)
        
        self.list_chuong.clear()
        for idx, chu_de in enumerate(danh_sach_5_chu_de):
            item_chu_de = QListWidgetItem(chu_de)
            self.list_chuong.addItem(item_chu_de)

        if self.list_chuong.count() > 0:
            self.list_chuong.setCurrentRow(0)
            self.hien_thi_chi_tiet_bai(self.list_chuong.item(0))

    def hien_thi_chi_tiet_bai(self, item):
        """Hiển thị nội dung bài học với TẤT CẢ VĂN BẢN LÀ CHỮ TRẮNG."""
        if not item:
            return
        
        ten_bai = item.text().strip()
        ten_mon = self.cbo_mon.currentText()
        ten_lop = self.cbo_lop.currentText()

        self.lbl_ten_bai.setText(f"Bài học: {ten_bai} ({ten_mon} - {ten_lop})")
        
        noi_dung = lay_noi_dung_bai_hoc_chi_tiet(ten_lop, ten_mon, ten_bai).strip()
        self.txt_noi_dung.setText(noi_dung)

        # Trích xuất và hiển thị mục Ý BÀI HỌC vào ô tóm tắt trên cùng chữ trắng
        if "I. Ý BÀI HỌC" in noi_dung:
            parts = noi_dung.split("II. KIẾN THỨC CẦN NHỚ")
            if len(parts) > 1:
                y_bai_hoc_text = parts[0].replace("==================================================", "").strip()
                lines = [line for line in y_bai_hoc_text.split('\n') if line.strip()]
                self.txt_y_bai_hoc_tom_tat.setText("\n".join(lines).strip())
            else:
                self.txt_y_bai_hoc_tom_tat.setText(noi_dung[:300].strip())
        else:
            self.txt_y_bai_hoc_tom_tat.setText("Bài học giúp học sinh rèn luyện tư duy logic và vận dụng kiến thức vào thực tế.")

    def bat_dau_luyen_tap(self):
        """Tải đề thi mới riêng biệt cho Chủ đề hiện tại từ JavaScript Engine & Internet API."""
        item = self.list_chuong.currentItem()
        ten_bai = item.text().strip() if item else "Chủ đề bài học"
        ten_lop = self.cbo_lop.currentText()
        ten_mon = self.cbo_mon.currentText()

        self.de_thi = chay_javascript_sinh_de(ten_lop, ten_mon, ten_bai, 10)
        self.cau_hoi_idx = 0
        self.dap_an_user = {}
        self.da_nop_bai = False
        self.lbl_giai_thich.hide()
        self.thoi_gian_con_lai = 600

        self.lbl_de_title.setText(f"ĐỀ THI MỚI: {ten_lop.upper()} - {ten_mon.upper()} - CHỦ ĐỀ: {ten_bai.upper()}")
        self.timer.start(1000)
        self.hien_thi_cau_hoi()
        QMessageBox.information(self, "Tạo đề thành công", f"Đã nạp thành công đề mới cho {ten_lop} - Môn {ten_mon} - Chủ đề: {ten_bai}!")

    def cap_nhat_dong_ho(self):
        if self.thoi_gian_con_lai > 0:
            self.thoi_gian_con_lai -= 1
            phut = self.thoi_gian_con_lai // 60
            giay = self.thoi_gian_con_lai % 60
            self.lbl_dong_ho.setText(f"Thời gian: {phut:02d}:{giay:02d}")
        else:
            self.timer.stop()
            QMessageBox.warning(self, "Hết giờ", "Hết thời gian làm bài! Hệ thống tự động nộp bài.")
            self.nop_bai()

    def hien_thi_cau_hoi(self):
        if not self.de_thi:
            return

        cau_current = self.de_thi[self.cau_hoi_idx]
        self.lbl_cau_so.setText(f"Câu {self.cau_hoi_idx + 1} / {len(self.de_thi)}")
        self.lbl_noidung_cauhoi.setText(cau_current["cau_hoi"])

        # Xóa options cũ
        for i in reversed(range(self.vung_options_layout.count())):
            widget = self.vung_options_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        dap_an_da_luu = self.dap_an_user.get(self.cau_hoi_idx, "")
        widget_options = TheDapAnGroup(cau_current["dap_an"], dap_an_hien_tai=dap_an_da_luu)
        widget_options.dap_an_thay_doi.connect(self.luu_dap_an)
        self.vung_options_layout.addWidget(widget_options)

        # Cập nhật lời giải chính xác cho đúng câu hỏi hiện tại
        if self.da_nop_bai or not self.lbl_giai_thich.isHidden():
            self.cap_nhat_lbl_giai_thich()

    def cap_nhat_lbl_giai_thich(self):
        if not self.de_thi:
            return
        cau_current = self.de_thi[self.cau_hoi_idx]
        nguon = cau_current.get('nguon', 'JavaScript Engine & Internet API')
        dap_an = cau_current.get('dap_an_dung', '')
        giai_thich = cau_current.get('giai_thich', '')
        self.lbl_giai_thich.setText(f"[Nguồn dữ liệu: {nguon}]\nĐáp án đúng của Câu {self.cau_hoi_idx + 1}: {dap_an}\n\n{giai_thich}")
        self.lbl_giai_thich.show()

    def hien_loi_giai_cau_hien_tai(self):
        if self.lbl_giai_thich.isHidden():
            self.cap_nhat_lbl_giai_thich()
        else:
            self.lbl_giai_thich.hide()

    def luu_dap_an(self, text):
        self.dap_an_user[self.cau_hoi_idx] = text

    def cau_truoc(self):
        if self.cau_hoi_idx > 0:
            self.cau_hoi_idx -= 1
            self.hien_thi_cau_hoi()

    def cau_sau(self):
        if self.cau_hoi_idx < len(self.de_thi) - 1:
            self.cau_hoi_idx += 1
            self.hien_thi_cau_hoi()

    def nop_bai(self):
        self.timer.stop()
        if not self.de_thi:
            return

        self.da_nop_bai = True
        ket_qua = cham_bai_lam(self.de_thi, self.dap_an_user)

        # Cong 1 luot choi Obby khi hoan thanh bài luyen tap
        luot_moi = them_luot_choi_obby(1)

        msg = f"""
KẾT QUẢ BÀI LÀM:
- Đề thi: {self.lbl_de_title.text()}
- Điểm số: {ket_qua['diem_so']} / 10 ({ket_qua['phan_tram']}%)
- Số câu đúng: {ket_qua['so_cau_dung']} / {ket_qua['tong_cau']}
- Xếp loại: {ket_qua['xep_loai']}
- Phần thưởng: +1 LƯỢT CHƠI OBBY!
- Nguồn đề thi: JavaScript & Internet API
        """
        QMessageBox.information(self, "Kết quả luyện tập", msg)
        self.cap_nhat_lbl_giai_thich()

        reply = QMessageBox.question(
            self,
            "THƯỞNG LƯỢT CHƠI OBBY",
            f"CHÚC MỪNG! Em đã làm xong bài tập và nhận được +1 LƯỢT CHƠI OBBY!\n"
            f"Số lượt chơi Obby khả dụng hiện tại: {luot_moi} lượt.\n\n"
            f"Em có muốn sang Đấu Trường Obby để chơi ngay không?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.Yes
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.yeu_cau_chuyen_obby.emit()

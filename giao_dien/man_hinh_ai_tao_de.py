# Thu muc: giao_dien
# File: man_hinh_ai_tao_de.py
# Mo ta: Man hinh AI tao de thi chay ngam luong QThread chong dung app, bo loc QGridLayout rong rai khong bi che chu sang Tieng Viet co dau

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QFrame, QMessageBox, QScrollArea, QGridLayout,
    QComboBox, QCheckBox
)

from PyQt6.QtCore import QTimer, Qt
from du_lieu.kho_noi_dung_hoc import (
    lay_danh_sach_lop, lay_danh_sach_mon_hoc, lay_chu_de_theo_lop_va_mon
)
from xu_ly_gemini.luong_sinh_de import LuongSinhDeGemini
from xu_ly_kiem_tra.bo_cham_diem import cham_bai_lam
from giao_dien.dap_an_tuong_tac import TheDapAnGroup
from giao_dien.hop_thoai_tao_de import HopThoaiTaoDeDialog
from giao_dien.hop_thoai_cai_dat_gemini import HopThoaiCaiDatGeminiDialog
from giao_dien.hop_thoai_minigame_giua_gio import HopThoaiMinigameGiuaGioDialog


class ManHinhAITaoDe(QWidget):
    """Màn hình AI Tạo đề thi hỗ trợ tự động sinh bằng Gemini API Key với Lớp, Môn học (tự chọn/tự nhập), Độ khó, Chủ đề và Thời gian."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.de_thi = []
        self.cau_hoi_idx = 0
        self.dap_an_user = {}
        self.da_nop_bai = False
        self.thoi_gian_con_lai = 600
        self.luong_sinh_de = None
        self.thoi_gian_phut_tam = 10
        self.thong_bao_tam = True
        self.cac_cau_da_choi_minigame = set()

        self.timer = QTimer(self)

        self.timer.timeout.connect(self.cap_nhat_dong_ho)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(12)

        # Tiêu đề chữ trắng
        title_label = QLabel("AI TẠO ĐỀ THI THÔNG MINH (GEMINI API - CHỌN/TỰ NHẬP MÔN, ĐỘ KHÓ VÀ CHỦ ĐỀ)")
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #FFFFFF;")
        main_layout.addWidget(title_label)

        # Thanh chọn Lớp, Môn học, Độ khó, Chủ đề, Số câu và Thời gian trình bày theo Grid 2 hàng rộng rãi
        filter_frame = QFrame()
        filter_frame.setProperty("class", "card-widget")
        filter_layout = QVBoxLayout(filter_frame)
        filter_layout.setContentsMargins(15, 12, 15, 12)
        filter_layout.setSpacing(10)

        grid_filter = QGridLayout()
        grid_filter.setHorizontalSpacing(15)
        grid_filter.setVerticalSpacing(10)

        # QSS chuẩn cho combobox không bị che chữ
        qss_combo = "QComboBox { font-size: 14px; font-weight: bold; color: #FFFFFF; background-color: #002244; padding: 6px 10px; border: 1px solid #00A2FF; border-radius: 6px; min-height: 28px; }"
        qss_lbl = "QLabel { font-size: 14px; font-weight: bold; color: #FFFFFF; }"

        # Hàng 0: Lớp, Môn, Độ khó
        lbl_lop = QLabel("Lớp học:")
        lbl_lop.setStyleSheet(qss_lbl)
        self.cbo_lop = QComboBox()
        self.cbo_lop.setStyleSheet(qss_combo)
        self.cbo_lop.addItems(lay_danh_sach_lop())
        self.cbo_lop.setCurrentText("Lớp 6")
        self.cbo_lop.currentTextChanged.connect(self.thay_doi_lop)

        lbl_mon = QLabel("Môn học (Tự nhập):")
        lbl_mon.setStyleSheet(qss_lbl)
        self.cbo_mon = QComboBox()
        self.cbo_mon.setEditable(True)  # Cho phép tự gõ tên môn
        self.cbo_mon.setStyleSheet(qss_combo)
        self.cbo_mon.currentTextChanged.connect(self.thay_doi_mon)

        lbl_muc_do = QLabel("Độ khó:")
        lbl_muc_do.setStyleSheet(qss_lbl)
        self.cbo_muc_do = QComboBox()
        self.cbo_muc_do.setStyleSheet(qss_combo)
        self.cbo_muc_do.addItems(["Dễ", "Trung bình", "Khó", "Nâng cao"])
        self.cbo_muc_do.setCurrentText("Trung bình")

        grid_filter.addWidget(lbl_lop, 0, 0)
        grid_filter.addWidget(self.cbo_lop, 0, 1)
        grid_filter.addWidget(lbl_mon, 0, 2)
        grid_filter.addWidget(self.cbo_mon, 0, 3)
        grid_filter.addWidget(lbl_muc_do, 0, 4)
        grid_filter.addWidget(self.cbo_muc_do, 0, 5)

        # Hàng 1: Chủ đề, Tạo số câu, Thời gian
        lbl_chu_de = QLabel("Chủ đề bài học:")
        lbl_chu_de.setStyleSheet(qss_lbl)
        self.cbo_chu_de = QComboBox()
        self.cbo_chu_de.setEditable(True)
        self.cbo_chu_de.setStyleSheet(qss_combo)

        lbl_so_cau = QLabel("Tạo số câu:")
        lbl_so_cau.setStyleSheet(qss_lbl)
        self.cbo_so_cau = QComboBox()
        self.cbo_so_cau.setEditable(True)
        self.cbo_so_cau.setStyleSheet(qss_combo)
        self.cbo_so_cau.addItems(["5 câu", "10 câu", "15 câu", "20 câu", "25 câu", "30 câu", "50 câu"])
        self.cbo_so_cau.setCurrentText("10 câu")

        lbl_tg = QLabel("Thời gian làm:")
        lbl_tg.setStyleSheet(qss_lbl)
        self.cbo_thoi_gian = QComboBox()
        self.cbo_thoi_gian.setStyleSheet(qss_combo)
        self.cbo_thoi_gian.addItems(["5 phút", "10 phút", "15 phút", "20 phút", "30 phút", "45 phút", "60 phút"])
        self.cbo_thoi_gian.setCurrentText("10 phút")

        grid_filter.addWidget(lbl_chu_de, 1, 0)
        grid_filter.addWidget(self.cbo_chu_de, 1, 1)
        grid_filter.addWidget(lbl_so_cau, 1, 2)
        grid_filter.addWidget(self.cbo_so_cau, 1, 3)
        grid_filter.addWidget(lbl_tg, 1, 4)
        grid_filter.addWidget(self.cbo_thoi_gian, 1, 5)

        filter_layout.addLayout(grid_filter)

        # Hàng nút bấm chức năng
        row_btn = QHBoxLayout()
        row_btn.setSpacing(10)

        self.btn_tao_de_truc_tiep = QPushButton("Gemini AI Tạo Đề Thi Ngay")
        self.btn_tao_de_truc_tiep.setProperty("class", "btn-primary")
        self.btn_tao_de_truc_tiep.setStyleSheet("font-size: 14px; font-weight: bold; color: #FFFFFF; padding: 8px 18px;")
        self.btn_tao_de_truc_tiep.clicked.connect(self.tao_de_truc_tiep)

        self.btn_open_dialog = QPushButton("Tùy chọn nâng cao (Popup)")
        self.btn_open_dialog.setProperty("class", "btn-secondary")
        self.btn_open_dialog.setStyleSheet("font-size: 14px; font-weight: bold; color: #FFFFFF; padding: 8px 16px;")
        self.btn_open_dialog.clicked.connect(self.mo_hop_thoai_tao_de)

        self.btn_cai_dat_gemini = QPushButton("Cài đặt Gemini API Key")
        self.btn_cai_dat_gemini.setProperty("class", "btn-secondary")
        self.btn_cai_dat_gemini.setStyleSheet("font-size: 14px; font-weight: bold; color: #FFFFFF; padding: 8px 16px;")
        self.btn_cai_dat_gemini.clicked.connect(self.mo_hop_thoai_cai_dat_gemini)

        self.btn_minigame = QPushButton("Minigame Thư Giãn Giữa Giờ")
        self.btn_minigame.setProperty("class", "btn-primary")
        self.btn_minigame.setStyleSheet("font-size: 14px; font-weight: bold; color: #FFFFFF; padding: 8px 16px; background-color: #00A2FF;")
        self.btn_minigame.clicked.connect(self.mo_minigame_giua_gio)

        self.chk_auto_minigame = QCheckBox("Chơi Minigame sau mỗi câu")
        self.chk_auto_minigame.setChecked(True)
        self.chk_auto_minigame.setStyleSheet("color: #00FFCC; font-weight: bold; font-size: 14px;")

        row_btn.addWidget(self.btn_tao_de_truc_tiep)
        row_btn.addWidget(self.btn_open_dialog)
        row_btn.addWidget(self.btn_cai_dat_gemini)
        row_btn.addWidget(self.btn_minigame)
        row_btn.addWidget(self.chk_auto_minigame)
        row_btn.addStretch()



        filter_layout.addLayout(row_btn)
        main_layout.addWidget(filter_frame)

        # Khu vực hiển thị đề thi làm bài trực tiếp bọc trong QScrollArea
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("QScrollArea { border: none; background-color: transparent; }")

        self.exam_frame = QFrame()
        self.exam_frame.setProperty("class", "card-widget")
        exam_layout = QVBoxLayout(self.exam_frame)
        exam_layout.setContentsMargins(15, 15, 15, 15)

        # Header thông tin bài thi chữ trắng
        self.lbl_de_info = QLabel("Thông tin đề thi: Chọn/Tự nhập Môn học, Độ khó và Chủ đề ở trên rồi nhấn 'Gemini AI Tạo Đề Thi Ngay'.")
        self.lbl_de_info.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")
        self.lbl_de_info.setWordWrap(True)
        exam_layout.addWidget(self.lbl_de_info)

        header_exam = QHBoxLayout()
        self.lbl_cau_so = QLabel("Câu 1 / 10")
        self.lbl_cau_so.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF;")
        
        self.lbl_dong_ho = QLabel("Thời gian: Chưa bắt đầu")
        self.lbl_dong_ho.setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF; background-color: #002B4D; padding: 4px 14px; border-radius: 12px; border: 2px solid #00A2FF;")

        header_exam.addWidget(self.lbl_cau_so)
        header_exam.addStretch()
        header_exam.addWidget(self.lbl_dong_ho)
        exam_layout.addLayout(header_exam)

        # Nội dung câu hỏi chữ trắng
        self.lbl_noidung = QLabel("Nội dung câu hỏi sẽ xuất hiện tại đây...")
        self.lbl_noidung.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF; min-height: 50px;")
        self.lbl_noidung.setWordWrap(True)
        exam_layout.addWidget(self.lbl_noidung)

        # Thẻ phương án đáp án
        self.vung_options = QWidget()
        self.vung_options_layout = QVBoxLayout(self.vung_options)
        exam_layout.addWidget(self.vung_options)

        # Vùng hiển thị giải thích chi tiết chữ trắng
        self.lbl_giai_thich = QLabel("")
        self.lbl_giai_thich.setWordWrap(True)
        self.lbl_giai_thich.setStyleSheet("background-color: #002B4D; padding: 12px; border-radius: 8px; color: #FFFFFF; font-size: 15px; font-weight: bold; margin-top: 10px; border: 2px solid #0084FF;")
        self.lbl_giai_thich.hide()
        exam_layout.addWidget(self.lbl_giai_thich)

        self.scroll_area.setWidget(self.exam_frame)
        main_layout.addWidget(self.scroll_area)

        # Thanh điều hướng làm bài chữ trắng
        nav_layout = QHBoxLayout()
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
        self.btn_nop_bai.clicked.connect(self.nop_bai_thi)

        nav_layout.addWidget(self.btn_truoc)
        nav_layout.addWidget(self.btn_sau)
        nav_layout.addWidget(self.btn_giai_thich)
        nav_layout.addStretch()
        nav_layout.addWidget(self.btn_nop_bai)

        main_layout.addLayout(nav_layout)

        # Tải danh sách Lớp và Môn ban đầu
        self.thay_doi_lop(self.cbo_lop.currentText())

    def thay_doi_lop(self, ten_lop):
        """Cập nhật danh sách môn học khi chọn Lớp."""
        self.cbo_mon.blockSignals(True)
        self.cbo_mon.clear()
        danh_sach_mon = lay_danh_sach_mon_hoc(ten_lop)
        self.cbo_mon.addItems(danh_sach_mon)
        self.cbo_mon.blockSignals(False)
        if danh_sach_mon:
            self.thay_doi_mon(danh_sach_mon[0])

    def thay_doi_mon(self, ten_mon):
        """Cập nhật các Chủ đề gợi ý khi chọn/nhập Môn học."""
        if not ten_mon:
            return
        ten_lop = self.cbo_lop.currentText()
        danh_sach_5_chu_de = lay_chu_de_theo_lop_va_mon(ten_lop, ten_mon)
        
        self.cbo_chu_de.blockSignals(True)
        self.cbo_chu_de.clear()
        self.cbo_chu_de.addItems(danh_sach_5_chu_de)
        self.cbo_chu_de.blockSignals(False)

        self.timer.stop()
        self.lbl_dong_ho.setText("Thời gian: Chưa bắt đầu")
        self.lbl_noidung.setText("Chọn/nhập Môn học, Độ khó và Chủ đề ở trên rồi nhấn 'Gemini AI Tạo Đề Thi Ngay'.")

    def tao_de_truc_tiep(self, thong_bao=True):
        """Tạo đề thi trực tiếp từ thông số đã chọn trên thanh bộ lọc."""
        ten_lop = self.cbo_lop.currentText()
        ten_mon = self.cbo_mon.currentText().strip()
        if not ten_mon:
            QMessageBox.warning(self, "Thiếu thông tin", "Vui lòng chọn hoặc tự gõ tên Môn học!")
            return

        muc_do = self.cbo_muc_do.currentText().strip()
        ten_chu_de = self.cbo_chu_de.currentText().strip() if self.cbo_chu_de.currentText().strip() else "Kiến thức tổng hợp"
        
        raw_so_cau = self.cbo_so_cau.currentText().replace(" câu", "").strip()
        so_cau = int(raw_so_cau) if raw_so_cau.isdigit() and int(raw_so_cau) > 0 else 10

        tg_text = self.cbo_thoi_gian.currentText().replace(" phút", "").strip()
        thoi_gian_phut = int(tg_text) if tg_text.isdigit() else 10

        self.len_de_thi(ten_lop, ten_mon, ten_chu_de, so_cau, muc_do=muc_do, thoi_gian_phut=thoi_gian_phut, thong_bao=thong_bao)

    def mo_hop_thoai_tao_de(self):
        """Mở Hộp thoại Dialog tùy chọn nâng cao."""
        dialog = HopThoaiTaoDeDialog(self)
        dialog.de_thi_duoc_tao.connect(self.xu_ly_de_thi_tu_dialog)
        dialog.exec()

    def mo_hop_thoai_cai_dat_gemini(self):
        """Mở Hộp thoại cài đặt mã Gemini API Key."""
        dialog = HopThoaiCaiDatGeminiDialog(self)
        dialog.exec()

    def xu_ly_de_thi_tu_dialog(self, cauhinh):
        thoi_gian_phut = cauhinh.get("thoi_gian_phut", 10)
        muc_do = cauhinh.get("muc_do", "Trung bình")
        self.len_de_thi(cauhinh["ten_lop"], cauhinh["ten_mon"], cauhinh["ten_chuong"], cauhinh["so_cau"], muc_do=muc_do, thoi_gian_phut=thoi_gian_phut, thong_bao=True)

    def len_de_thi(self, ten_lop, ten_mon, ten_chuong, so_cau=10, muc_do="Trung bình", thoi_gian_phut=10, thong_bao=True):
        """Khởi chạy QThread ngầm sinh đề thi Gemini AI để giao diện luôn mượt mà không bị đơ giật lag."""
        self.timer.stop()
        self.thoi_gian_phut_tam = thoi_gian_phut
        self.thong_bao_tam = thong_bao
        self.lbl_giai_thich.hide()

        # Cập nhật giao diện trạng thái đang tải
        self.lbl_de_info.setText(f"ĐANG KHỞI TẠO BÀI TẬP BẰNG GEMINI AI ({ten_lop} - {ten_mon} - {muc_do})... VUI LÒNG CHỜ TRONG GIÂY LÁT!")
        self.lbl_noidung.setText("Hệ thống đang kết nối Gemini AI để tự động tạo bộ câu hỏi thông minh. Giao diện vẫn hoạt động mượt mà...")
        self.lbl_dong_ho.setText("Thời gian: Đang khởi tạo...")

        # Vô hiệu hóa nút tạo đề tạm thời để tránh bấm liên tục
        self.btn_tao_de_truc_tiep.setEnabled(False)
        self.btn_tao_de_truc_tiep.setText("Đang Gemini AI tạo đề...")

        # Khởi chạy luồng chạy ngầm QThread
        self.luong_sinh_de = LuongSinhDeGemini(ten_lop, ten_mon, ten_chuong, so_cau, muc_do, self)
        self.luong_sinh_de.de_thi_da_sinh.connect(self.xu_ly_ket_qua_sinh_de_ngam)
        self.luong_sinh_de.start()

    def xu_ly_ket_qua_sinh_de_ngam(self, danh_sach_de, err_msg):
        """Nhận kết quả từ Luồng QThread ngầm khi hoàn thành."""
        self.btn_tao_de_truc_tiep.setEnabled(True)
        self.btn_tao_de_truc_tiep.setText("Gemini AI Tạo Đề Thi Ngay")

        if not danh_sach_de:
            QMessageBox.warning(self, "Thông báo", err_msg if err_msg else "Không thể sinh đề thi. Vui lòng thử lại!")
            self.lbl_noidung.setText("Lỗi khởi tạo bài tập từ Gemini AI. Vui lòng kiểm tra lại API Key hoặc kết nối mạng.")
            return

        self.de_thi = danh_sach_de
        self.cau_hoi_idx = 0
        self.dap_an_user = {}
        self.da_nop_bai = False
        self.thoi_gian_con_lai = self.thoi_gian_phut_tam * 60

        cau_dau = self.de_thi[0]
        ten_lop = cau_dau.get("lop", self.cbo_lop.currentText())
        ten_mon = cau_dau.get("mon_hoc", self.cbo_mon.currentText())
        muc_do = cau_dau.get("muc_do", self.cbo_muc_do.currentText())
        ten_chuong = cau_dau.get("chuong", self.cbo_chu_de.currentText())
        nguon_de = cau_dau.get("nguon", "Gemini AI")

        self.lbl_de_info.setText(f"ĐỀ THI: {ten_lop.upper()} - MÔN: {ten_mon.upper()} - ĐỘ KHÓ: {muc_do.upper()} - CHỦ ĐỀ: {ten_chuong.upper()} ({len(self.de_thi)} CÂU - {self.thoi_gian_phut_tam} PHÚT)")
        self.timer.start(1000)
        self.hien_thi_cau_hoi()

        if self.thong_bao_tam:
            QMessageBox.information(self, "Lên đề thành công", f"AI ({nguon_de}) đã tạo thành công đề thi:\n- {ten_lop} | Môn: {ten_mon}\n- Độ khó: {muc_do}\n- Chủ đề: {ten_chuong}\n- Số câu: {len(self.de_thi)} câu ({self.thoi_gian_phut_tam} phút)")

    def cap_nhat_dong_ho(self):
        if self.thoi_gian_con_lai > 0:
            self.thoi_gian_con_lai -= 1
            phut = self.thoi_gian_con_lai // 60
            giay = self.thoi_gian_con_lai % 60
            self.lbl_dong_ho.setText(f"Thời gian: {phut:02d}:{giay:02d}")
        else:
            self.timer.stop()
            QMessageBox.warning(self, "Hết giờ", "Hết thời gian làm bài! Hệ thống tự động nộp bài.")
            self.nop_bai_thi()

    def hien_thi_cau_hoi(self):
        if not self.de_thi:
            return

        cau_current = self.de_thi[self.cau_hoi_idx]
        self.lbl_cau_so.setText(f"Câu {self.cau_hoi_idx + 1} / {len(self.de_thi)}")
        self.lbl_noidung.setText(cau_current["cau_hoi"])

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
        nguon = cau_current.get('nguon', 'Gemini AI API')
        muc_do = cau_current.get('muc_do', 'Trung bình')
        dap_an = cau_current.get('dap_an_dung', '')
        giai_thich = cau_current.get('giai_thich', '')
        self.lbl_giai_thich.setText(f"[Nguồn dữ liệu: {nguon} | Độ khó: {muc_do}]\nĐáp án đúng của Câu {self.cau_hoi_idx + 1}: {dap_an}\n\n{giai_thich}")
        self.lbl_giai_thich.show()

    def hien_loi_giai_cau_hien_tai(self):
        if self.lbl_giai_thich.isHidden():
            self.cap_nhat_lbl_giai_thich()
        else:
            self.lbl_giai_thich.hide()

    def luu_dap_an(self, text):
        self.dap_an_user[self.cau_hoi_idx] = text
        if text and self.chk_auto_minigame.isChecked() and self.cau_hoi_idx not in self.cac_cau_da_choi_minigame:
            self.cac_cau_da_choi_minigame.add(self.cau_hoi_idx)
            dlg = HopThoaiMinigameGiuaGioDialog(self)
            dlg.mo_tab_ngau_nhien(self.cau_hoi_idx + 1)
            dlg.exec()


    def cau_truoc(self):
        if self.cau_hoi_idx > 0:
            self.cau_hoi_idx -= 1
            self.hien_thi_cau_hoi()

    def cau_sau(self):
        if self.cau_hoi_idx < len(self.de_thi) - 1:
            self.cau_hoi_idx += 1
            self.hien_thi_cau_hoi()

    def mo_minigame_giua_gio(self):
        """Mở Hộp thoại Minigame thư giãn giữa giờ học."""
        dlg = HopThoaiMinigameGiuaGioDialog(self)
        dlg.exec()

    def nop_bai_thi(self):
        self.timer.stop()
        if not self.de_thi:
            return

        self.da_nop_bai = True
        ket_qua = cham_bai_lam(self.de_thi, self.dap_an_user)
        nguon_de = self.de_thi[0].get("nguon", "Gemini AI API") if self.de_thi else "Gemini AI"
        msg = f"""
KẾT QUẢ BÀI LÀM:
- Thông tin đề: {self.lbl_de_info.text().replace('ĐỀ THI: ', '')}
- Điểm số: {ket_qua['diem_so']} / 10 ({ket_qua['phan_tram']}%)
- Số câu đúng: {ket_qua['so_cau_dung']} / {ket_qua['tong_cau']}
- Xếp loại: {ket_qua['xep_loai']}
- Nguồn câu hỏi: {nguon_de}
        """
        QMessageBox.information(self, "Kết quả bài thi", msg)
        self.cap_nhat_lbl_giai_thich()

        # Mở minigame thư giãn giữa giờ sau bài thi
        self.mo_minigame_giua_gio()


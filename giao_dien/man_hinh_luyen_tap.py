# Thu muc: giao_dien
# File: man_hinh_luyen_tap.py
# Mo ta: Man hinh luyen tap tich hop chon Mon, 5 Chu de, Tao so cau va Thoi gian luyen tap sang Tieng Viet co dau

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QLineEdit, QPushButton, QFrame, QMessageBox, QScrollArea,
    QComboBox, QCheckBox
)

from PyQt6.QtCore import QTimer, Qt
from du_lieu.ngan_hang_cau_hoi import lay_cau_hoi_luyen_tap
from du_lieu.kho_noi_dung_hoc import (
    lay_danh_sach_lop, lay_danh_sach_mon_hoc, lay_chu_de_theo_lop_va_mon
)
from xu_ly_kiem_tra.dong_co_javascript import chay_javascript_sinh_de
from xu_ly_kiem_tra.bo_cham_diem import cham_bai_lam
from xu_ly_hoc_tap.he_thong_thuong import cong_phan_thuong
from giao_dien.dap_an_tuong_tac import TheDapAnGroup, KhungGhepCap, KhungSapXep
from giao_dien.hop_thoai_tao_de import HopThoaiTaoDeDialog
from giao_dien.hop_thoai_chung_nhan import HopThoaiChungNhan
from giao_dien.hop_thoai_minigame_giua_gio import HopThoaiMinigameGiuaGioDialog


class ManHinhLuyenTap(QWidget):
    """Màn hình thực hành luyện tập hỗ trợ chọn Môn học, 5 Chủ đề, TẠO SỐ CÂU HỎI và CHỌN THỜI GIAN LUYỆN TẬP với TẤT CẢ VĂN BẢN LÀ CHỮ TRẮNG SÁNG."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.danh_sach_cau_hoi = []
        self.cau_so_hien_tai = 0
        self.cau_tra_loi_user = {}
        self.da_nop_bai = False
        self.thoi_gian_con_lai = 600
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.cap_nhat_dong_ho)
        
        self.lop_hien_tai = "Lớp 6"
        self.mon_hien_tai = "Toán"
        self.chu_de_hien_tai = "Chủ đề 1: Số học, Đại số và Các phép tính (Lớp 6)"
        self.cac_cau_da_choi_minigame = set()

        self.init_ui()


    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Tiêu đề chữ trắng
        title_label = QLabel("HỆ THỐNG LUYỆN TẬP BÀI TẬP TƯƠNG TÁC (CHỌN MÔN, 5 CHỦ ĐỀ, TẠO SỐ CÂU VÀ THỜI GIAN)")
        title_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #FFFFFF;")
        main_layout.addWidget(title_label)

        # Thanh chọn Lớp, Chọn Môn, 5 Chủ đề, TẠO SỐ CÂU và THỜI GIAN LUYỆN TẬP chữ trắng
        filter_frame = QFrame()
        filter_frame.setProperty("class", "card-widget")
        filter_layout = QHBoxLayout(filter_frame)

        lbl_lop = QLabel("Lớp:")
        lbl_lop.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")
        self.cbo_lop = QComboBox()
        self.cbo_lop.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px;")
        self.cbo_lop.addItems(lay_danh_sach_lop())
        self.cbo_lop.setCurrentText("Lớp 6")
        self.cbo_lop.currentTextChanged.connect(self.thay_doi_lop)

        lbl_mon = QLabel("Môn:")
        lbl_mon.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")
        self.cbo_mon = QComboBox()
        self.cbo_mon.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px;")
        self.cbo_mon.currentTextChanged.connect(self.thay_doi_mon)

        lbl_chu_de = QLabel("5 Chủ đề:")
        lbl_chu_de.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")
        self.cbo_chu_de = QComboBox()
        self.cbo_chu_de.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px;")

        lbl_so_cau = QLabel("Tạo số câu:")
        lbl_so_cau.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")
        self.cbo_so_cau = QComboBox()
        self.cbo_so_cau.setEditable(True)  # TỰ NHẬP BẤT KỲ SỐ CÂU HỎI NÀO
        self.cbo_so_cau.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px;")
        self.cbo_so_cau.addItems(["5 câu", "10 câu", "15 câu", "20 câu", "25 câu", "30 câu", "50 câu"])
        self.cbo_so_cau.setCurrentText("10 câu")

        lbl_tg = QLabel("Thời gian:")
        lbl_tg.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")
        self.cbo_thoi_gian = QComboBox()
        self.cbo_thoi_gian.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px;")
        self.cbo_thoi_gian.addItems(["5 phút", "10 phút", "15 phút", "20 phút", "30 phút", "45 phút", "60 phút"])
        self.cbo_thoi_gian.setCurrentText("10 phút")

        btn_bat_dau_luyen = QPushButton("Bắt đầu Luyện tập Chủ đề này")
        btn_bat_dau_luyen.setProperty("class", "btn-primary")
        btn_bat_dau_luyen.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px;")
        btn_bat_dau_luyen.clicked.connect(self.bat_dau_luyen_tap_theo_chu_de)

        self.chk_auto_minigame = QCheckBox("Chơi Minigame sau mỗi câu")
        self.chk_auto_minigame.setChecked(True)
        self.chk_auto_minigame.setStyleSheet("color: #00FFCC; font-weight: bold; font-size: 14px;")

        filter_layout.addWidget(lbl_lop)
        filter_layout.addWidget(self.cbo_lop)
        filter_layout.addWidget(lbl_mon)
        filter_layout.addWidget(self.cbo_mon)
        filter_layout.addWidget(lbl_chu_de)
        filter_layout.addWidget(self.cbo_chu_de, 2)
        filter_layout.addWidget(lbl_so_cau)
        filter_layout.addWidget(self.cbo_so_cau)
        filter_layout.addWidget(lbl_tg)
        filter_layout.addWidget(self.cbo_thoi_gian)
        filter_layout.addWidget(self.chk_auto_minigame)
        filter_layout.addWidget(btn_bat_dau_luyen)

        main_layout.addWidget(filter_frame)


        # Thanh trạng thái câu hỏi & Đồng hồ đếm ngược
        status_layout = QHBoxLayout()
        self.lbl_tiendo = QLabel("Câu hỏi 1 / 10")
        self.lbl_tiendo.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF;")
        
        self.lbl_dong_ho = QLabel("Thời gian còn lại: Chưa bắt đầu")
        self.lbl_dong_ho.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF; background-color: #002B4D; padding: 6px 16px; border-radius: 14px; border: 2px solid #00A2FF;")

        status_layout.addWidget(self.lbl_tiendo)
        status_layout.addStretch()
        status_layout.addWidget(self.lbl_dong_ho)
        main_layout.addLayout(status_layout)

        # Khung hiển thị câu hỏi
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        
        self.card_question = QFrame()
        self.card_question.setProperty("class", "card-widget")
        self.card_layout = QVBoxLayout(self.card_question)

        self.lbl_noidung_cauhoi = QLabel("Chọn Môn học, Tạo số câu, Thời gian và 1 trong 5 Chủ đề trên rồi nhấn 'Bắt đầu Luyện tập'")
        self.lbl_noidung_cauhoi.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF;")
        self.lbl_noidung_cauhoi.setWordWrap(True)
        self.card_layout.addWidget(self.lbl_noidung_cauhoi)

        # Vùng điền/bấm chọn đáp án
        self.vung_dap_an_container = QWidget()
        self.vung_dap_an_layout = QVBoxLayout(self.vung_dap_an_container)
        self.card_layout.addWidget(self.vung_dap_an_container)

        # Vùng hiển thị lời giải và đáp án đúng chữ trắng
        self.lbl_giai_thich = QLabel("")
        self.lbl_giai_thich.setWordWrap(True)
        self.lbl_giai_thich.setStyleSheet("background-color: #002B4D; padding: 12px; border-radius: 10px; color: #FFFFFF; font-size: 15px; font-weight: bold; margin-top: 10px; border: 2px solid #0084FF;")
        self.lbl_giai_thich.hide()
        self.card_layout.addWidget(self.lbl_giai_thich)

        self.scroll_area.setWidget(self.card_question)
        main_layout.addWidget(self.scroll_area)

        # Thanh điều hướng câu hỏi & Nộp bài chữ trắng
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

        self.btn_nop_bai = QPushButton("Nộp bài và Chấm điểm")
        self.btn_nop_bai.setProperty("class", "btn-success")
        self.btn_nop_bai.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.btn_nop_bai.clicked.connect(self.nop_bai)

        self.btn_minigame = QPushButton("Minigame Thư Giãn Giữa Giờ")
        self.btn_minigame.setProperty("class", "btn-primary")
        self.btn_minigame.setStyleSheet("color: #FFFFFF; font-weight: bold; background-color: #00A2FF;")
        self.btn_minigame.clicked.connect(self.mo_minigame_giua_gio)

        nav_layout.addWidget(self.btn_truoc)
        nav_layout.addWidget(self.btn_sau)
        nav_layout.addWidget(self.btn_giai_thich)
        nav_layout.addWidget(self.btn_minigame)
        nav_layout.addStretch()
        nav_layout.addWidget(self.btn_nop_bai)

        main_layout.addLayout(nav_layout)


        # Load dữ liệu Lớp và Môn ban đầu
        self.thay_doi_lop(self.cbo_lop.currentText())

    def thay_doi_lop(self, ten_lop):
        """Cập nhật danh sách môn học khi thay đổi Lớp."""
        self.cbo_mon.blockSignals(True)
        self.cbo_mon.clear()
        danh_sach_mon = lay_danh_sach_mon_hoc(ten_lop)
        self.cbo_mon.addItems(danh_sach_mon)
        self.cbo_mon.blockSignals(False)
        if danh_sach_mon:
            self.thay_doi_mon(danh_sach_mon[0])

    def thay_doi_mon(self, ten_mon):
        """Cập nhật ĐÚNG 5 CHỦ ĐỀ LUYỆN TẬP khi chọn môn học."""
        if not ten_mon:
            return
        ten_lop = self.cbo_lop.currentText()
        danh_sach_5_chu_de = lay_chu_de_theo_lop_va_mon(ten_lop, ten_mon)
        
        self.cbo_chu_de.blockSignals(True)
        self.cbo_chu_de.clear()
        self.cbo_chu_de.addItems(danh_sach_5_chu_de)
        self.cbo_chu_de.blockSignals(False)

        self.timer.stop()
        self.lbl_dong_ho.setText("Thời gian còn lại: Chưa bắt đầu")

    def bat_dau_luyen_tap_theo_chu_de(self):
        """Sinh đúng số câu hỏi và đặt Thời gian đếm ngược được chọn cho Chủ đề."""
        self.lop_hien_tai = self.cbo_lop.currentText()
        self.mon_hien_tai = self.cbo_mon.currentText()
        self.chu_de_hien_tai = self.cbo_chu_de.currentText() if self.cbo_chu_de.currentText() else "Chủ đề 1"

        raw_so_cau = self.cbo_so_cau.currentText().replace(" câu", "").strip()
        so_cau = int(raw_so_cau) if raw_so_cau.isdigit() and int(raw_so_cau) > 0 else 10

        tg_text = self.cbo_thoi_gian.currentText().replace(" phút", "").strip()
        thoi_gian_phut = int(tg_text) if tg_text.isdigit() else 10

        self.danh_sach_cau_hoi = chay_javascript_sinh_de(self.lop_hien_tai, self.mon_hien_tai, self.chu_de_hien_tai, so_cau)
        self.cau_so_hien_tai = 0
        self.cau_tra_loi_user = {}
        self.da_nop_bai = False
        self.lbl_giai_thich.hide()
        self.thoi_gian_con_lai = thoi_gian_phut * 60
        self.lbl_dong_ho.setText(f"Thời gian còn lại: {thoi_gian_phut:02d}:00")
        self.timer.start(1000)
        self.hien_thi_cau_hoi_hien_tai()

    def cap_nhat_dong_ho(self):
        if self.thoi_gian_con_lai > 0:
            self.thoi_gian_con_lai -= 1
            phut = self.thoi_gian_con_lai // 60
            giay = self.thoi_gian_con_lai % 60
            self.lbl_dong_ho.setText(f"Thời gian còn lại: {phut:02d}:{giay:02d}")
        else:
            self.timer.stop()
            QMessageBox.warning(self, "Hết giờ", "Hết thời gian làm bài! Hệ thống tự động nộp bài.")
            self.nop_bai()

    def hien_thi_cau_hoi_hien_tai(self):
        """Cập nhật UI hiển thị câu hỏi hiện tại chữ trắng sáng."""
        if not self.danh_sach_cau_hoi:
            return

        cau_hoi = self.danh_sach_cau_hoi[self.cau_so_hien_tai]
        
        ten_loai = {
            "trac_nghiem": "Trắc nghiệm",
            "dung_sai": "Đúng / Sai",
            "dien_cho_trong": "Điền vào chỗ trống",
            "ghep_cap": "Ghép cặp",
            "sap_xep": "Sắp xếp",
            "tu_luan_ngan": "Tự luận ngắn"
        }.get(cau_hoi.get('loai', 'trac_nghiem'), "Trắc nghiệm")

        self.lbl_tiendo.setText(f"Câu hỏi {self.cau_so_hien_tai + 1} / {len(self.danh_sach_cau_hoi)} (Dạng: {ten_loai})")
        self.lbl_noidung_cauhoi.setText(cau_hoi["cau_hoi"])

        # Xóa các widget vùng đáp án cũ
        for i in reversed(range(self.vung_dap_an_layout.count())): 
            widget = self.vung_dap_an_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        loai = cau_hoi.get("loai", "trac_nghiem")
        dap_an_da_luu = self.cau_tra_loi_user.get(self.cau_so_hien_tai, "")

        if loai in ["trac_nghiem", "dung_sai"] or "dap_an" in cau_hoi:
            options = cau_hoi.get("luat_dap_an") or cau_hoi.get("dap_an", [])
            widget_dap_an = TheDapAnGroup(options, dap_an_hien_tai=dap_an_da_luu)
            widget_dap_an.dap_an_thay_doi.connect(self.luu_dap_an)
            self.vung_dap_an_layout.addWidget(widget_dap_an)

        elif loai == "ghep_cap":
            dict_pairs = cau_hoi.get("luat_dap_an", {})
            widget_ghep = KhungGhepCap(dict_pairs, dap_an_hien_tai=dap_an_da_luu)
            widget_ghep.dap_an_thay_doi.connect(self.luu_dap_an)
            self.vung_dap_an_layout.addWidget(widget_ghep)

        elif loai == "sap_xep":
            danh_sach_buoc = cau_hoi.get("luat_dap_an", [])
            widget_sap_xep = KhungSapXep(danh_sach_buoc, dap_an_hien_tai=dap_an_da_luu)
            widget_sap_xep.dap_an_thay_doi.connect(self.luu_dap_an)
            self.vung_dap_an_layout.addWidget(widget_sap_xep)

        else: # dien_cho_trong, tu_luan_ngan
            txt_input = QLineEdit()
            txt_input.setStyleSheet("color: #FFFFFF; font-size: 15px; font-weight: bold; background-color: #111214; border: 2px solid #393B3D;")
            txt_input.setPlaceholderText("Nhập câu trả lời của em vào đây...")
            txt_input.setText(str(dap_an_da_luu))
            txt_input.textChanged.connect(self.luu_dap_an)
            self.vung_dap_an_layout.addWidget(txt_input)

        # Cập nhật vùng lời giải theo câu hỏi hiện tại nếu đã nộp bài hoặc đang mở
        if self.da_nop_bai or not self.lbl_giai_thich.isHidden():
            self.cap_nhat_lbl_giai_thich()

    def cap_nhat_lbl_giai_thich(self):
        """Cập nhật nội dung lời giải chính xác chữ trắng."""
        if not self.danh_sach_cau_hoi:
            return
        cau_current = self.danh_sach_cau_hoi[self.cau_so_hien_tai]
        nguon = cau_current.get('nguon', 'JavaScript Engine & Internet API')
        dap_an = cau_current.get('dap_an_dung', '')
        giai_thich = cau_current.get('giai_thich', '')
        self.lbl_giai_thich.setText(f"[Nguồn dữ liệu: {nguon}]\nĐáp án đúng của Câu {self.cau_so_hien_tai + 1}: {dap_an}\n\n{giai_thich}")
        self.lbl_giai_thich.show()

    def hien_loi_giai_cau_hien_tai(self):
        """Mở/Tắt vùng xem lời giải cho câu hỏi hiện tại."""
        if self.lbl_giai_thich.isHidden():
            self.cap_nhat_lbl_giai_thich()
        else:
            self.lbl_giai_thich.hide()

    def luu_dap_an(self, text):
        """Lưu đáp án của câu hỏi hiện tại và tự động chơi 1 Minigame ngẫu nhiên."""
        self.cau_tra_loi_user[self.cau_so_hien_tai] = text
        if text and self.chk_auto_minigame.isChecked() and self.cau_so_hien_tai not in self.cac_cau_da_choi_minigame:
            self.cac_cau_da_choi_minigame.add(self.cau_so_hien_tai)
            dlg = HopThoaiMinigameGiuaGioDialog(self)
            dlg.mo_tab_ngau_nhien(self.cau_so_hien_tai + 1)
            dlg.exec()


    def cau_truoc(self):
        if self.cau_so_hien_tai > 0:
            self.cau_so_hien_tai -= 1
            self.hien_thi_cau_hoi_hien_tai()

    def cau_sau(self):
        if self.cau_so_hien_tai < len(self.danh_sach_cau_hoi) - 1:
            self.cau_so_hien_tai += 1
            self.hien_thi_cau_hoi_hien_tai()

    def mo_minigame_giua_gio(self):
        """Mở Hộp thoại Minigame thư giãn giữa giờ học."""
        dlg = HopThoaiMinigameGiuaGioDialog(self)
        dlg.exec()

    def nop_bai(self):
        """Chấm điểm bài luyện tập và hiển thị kết quả kèm Giấy chứng nhận hoàn thành và Minigame thư giãn."""
        self.timer.stop()
        self.da_nop_bai = True
        ket_qua = cham_bai_lam(self.danh_sach_cau_hoi, self.cau_tra_loi_user)
        xp_nhan, coin_nhan = cong_phan_thuong(ket_qua["diem_so"], ket_qua["so_cau_dung"])

        msg = f"""
KẾT QUẢ LUYỆN TẬP:
- Điểm số: {ket_qua['diem_so']} / 10 ({ket_qua['phan_tram']}%)
- Số câu đúng: {ket_qua['so_cau_dung']} / {ket_qua['tong_cau']}
- Xếp loại: {ket_qua['xep_loai']}
- Phần thưởng đạt được: +{xp_nhan} XP và +{coin_nhan} Coin!

Gợi ý: Lời giải chi tiết của từng câu hỏi đã được tự động hiển thị bên dưới.
        """
        QMessageBox.information(self, "Kết quả luyện tập", msg)
        self.cap_nhat_lbl_giai_thich()

        # Hiển thị Giấy chứng nhận hoàn thành bài tập chủ đề
        dlg_cert = HopThoaiChungNhan(
            parent=self, 
            lop=self.lop_hien_tai, 
            chu_de=self.chu_de_hien_tai, 
            phan_tram_diem=ket_qua['phan_tram'], 
            diem_so=ket_qua['diem_so']
        )
        dlg_cert.exec()

        # Mở minigame thư giãn giữa giờ sau bài luyện tập
        self.mo_minigame_giua_gio()


# Thu muc: giao_dien
# File: man_hinh_tap_thi_ielts.py
# Mo ta: Man hinh Tap Thi IELTS tong hop ho tro Luyen Nghe TTS an van ban, may tu dong doc va phan loai Band diem target sang Tieng Viet co dau

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QFrame, QMessageBox, QScrollArea, QCheckBox,
    QComboBox
)
from PyQt6.QtCore import QTimer, Qt

from xu_ly_ielts.du_lieu_ielts import (
    lay_danh_sach_tu_vung_ielts, lay_danh_sach_ngu_phap_va_thi,
    lay_bai_doc_ielts_reading, lay_bai_nghe_ielts_listening,
    lay_de_thi_ielts_tong_hop
)
from xu_ly_kiem_tra.bo_cham_diem import cham_bai_lam
from xu_ly_hoc_tap.he_thong_thuong import cong_phan_thuong
from xu_ly_am_thanh.quan_ly_am_thanh import QuanLyAmThanh
from giao_dien.dap_an_tuong_tac import TheDapAnGroup
from giao_dien.hop_thoai_minigame_giua_gio import HopThoaiMinigameGiuaGioDialog

class ManHinhTapThiIELTS(QWidget):
    """Màn hình Tập Thi IELTS tổng hợp với Luyện Nghe TTS máy đọc ẩn văn bản kịch bản."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.de_thi = []
        self.cau_hoi_idx = 0
        self.dap_an_user = {}
        self.da_nop_bai = False
        self.thoi_gian_con_lai = 900
        self.phan_mon_hien_tai = "KT Từ Vựng"
        self.cac_cau_da_choi_minigame = set()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.cap_nhat_dong_ho)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(12)

        # Tiêu đề chính chữ trắng
        lbl_title = QLabel("TẬP THI IELTS TỔNG HỢP - TỪ VỰNG, NGỮ PHÁP, CÁC THÌ, ĐỌC VÀ NGHE")
        lbl_title.setStyleSheet("font-size: 20px; font-weight: bold; color: #FFFFFF;")
        main_layout.addWidget(lbl_title)

        # Thanh chọn Band điểm & phân môn IELTS chữ trắng
        filter_frame = QFrame()
        filter_frame.setProperty("class", "card-widget")
        filter_layout = QVBoxLayout(filter_frame)
        filter_layout.setContentsMargins(12, 10, 12, 10)
        filter_layout.setSpacing(10)

        # Hàng 1: Chọn Band điểm mục tiêu Target
        row_band = QHBoxLayout()
        lbl_band = QLabel("Chọn Band điểm IELTS Target:")
        lbl_band.setStyleSheet("font-size: 14px; font-weight: bold; color: #FFFFFF;")
        
        self.cbo_band_ielts = QComboBox()
        self.cbo_band_ielts.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 14px;")
        self.cbo_band_ielts.addItems([
            "Band 4.5 - 5.0 (Cơ bản)",
            "Band 5.5 - 6.0 (Trung cấp)",
            "Band 6.5 - 7.0 (Nâng cao)",
            "Band 7.5 - 8.5+ (Xuất sắc)"
        ])
        self.cbo_band_ielts.setCurrentText("Band 5.5 - 6.0 (Trung cấp)")
        self.cbo_band_ielts.currentTextChanged.connect(self.thay_doi_band)

        self.chk_auto_minigame = QCheckBox("Chơi Minigame sau mỗi câu")
        self.chk_auto_minigame.setChecked(True)
        self.chk_auto_minigame.setStyleSheet("color: #00FFCC; font-weight: bold; font-size: 13px; margin-left: 10px;")

        row_band.addWidget(lbl_band)
        row_band.addWidget(self.cbo_band_ielts)
        row_band.addWidget(self.chk_auto_minigame)
        row_band.addStretch()
        filter_layout.addLayout(row_band)

        # Hàng 2: Nút chọn phân môn
        row_btn_skill = QHBoxLayout()
        row_btn_skill.setSpacing(8)

        self.btn_tu_vung = QPushButton("KT Từ Vựng IELTS")
        self.btn_tu_vung.setProperty("class", "btn-primary")
        self.btn_tu_vung.setStyleSheet("font-size: 13px; font-weight: bold; color: #FFFFFF; padding: 8px 14px;")
        self.btn_tu_vung.clicked.connect(lambda: self.chuyen_phan_mon("KT Từ Vựng"))

        self.btn_ngu_phap = QPushButton("Ngữ Pháp & Các Thì")
        self.btn_ngu_phap.setProperty("class", "btn-secondary")
        self.btn_ngu_phap.setStyleSheet("font-size: 13px; font-weight: bold; color: #FFFFFF; padding: 8px 14px;")
        self.btn_ngu_phap.clicked.connect(lambda: self.chuyen_phan_mon("Ngữ Pháp & Các Thì"))

        self.btn_doc = QPushButton("Đọc Hiểu Reading")
        self.btn_doc.setProperty("class", "btn-secondary")
        self.btn_doc.setStyleSheet("font-size: 13px; font-weight: bold; color: #FFFFFF; padding: 8px 14px;")
        self.btn_doc.clicked.connect(lambda: self.chuyen_phan_mon("Đọc Hiểu Reading"))

        self.btn_nghe = QPushButton("Luyện Nghe Listening")
        self.btn_nghe.setProperty("class", "btn-secondary")
        self.btn_nghe.setStyleSheet("font-size: 13px; font-weight: bold; color: #FFFFFF; padding: 8px 14px;")
        self.btn_nghe.clicked.connect(lambda: self.chuyen_phan_mon("Luyện Nghe Listening"))

        self.btn_tong_hop = QPushButton("Đề Thi IELTS Tổng Hợp")
        self.btn_tong_hop.setProperty("class", "btn-secondary")
        self.btn_tong_hop.setStyleSheet("font-size: 13px; font-weight: bold; color: #FFFFFF; padding: 8px 14px;")
        self.btn_tong_hop.clicked.connect(lambda: self.chuyen_phan_mon("Đề Thi IELTS Tổng Hợp"))

        row_btn_skill.addWidget(self.btn_tu_vung)
        row_btn_skill.addWidget(self.btn_ngu_phap)
        row_btn_skill.addWidget(self.btn_doc)
        row_btn_skill.addWidget(self.btn_nghe)
        row_btn_skill.addWidget(self.btn_tong_hop)
        row_btn_skill.addStretch()

        filter_layout.addLayout(row_btn_skill)
        main_layout.addWidget(filter_frame)

        # Khu vực bài làm bọc trong ScrollArea
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("QScrollArea { border: none; background-color: transparent; }")

        self.exam_frame = QFrame()
        self.exam_frame.setProperty("class", "card-widget")
        exam_layout = QVBoxLayout(self.exam_frame)
        exam_layout.setContentsMargins(15, 15, 15, 15)

        # Header bài thi
        self.lbl_de_info = QLabel("Thông tin phân môn Tập Thi IELTS...")
        self.lbl_de_info.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")
        exam_layout.addWidget(self.lbl_de_info)

        header_exam = QHBoxLayout()
        self.lbl_cau_so = QLabel("Câu 1 / 10")
        self.lbl_cau_so.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF;")
        
        self.lbl_dong_ho = QLabel("Thời gian: 15:00")
        self.lbl_dong_ho.setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF; background-color: #002B4D; padding: 4px 14px; border-radius: 12px; border: 2px solid #00A2FF;")

        header_exam.addWidget(self.lbl_cau_so)
        header_exam.addStretch()
        header_exam.addWidget(self.lbl_dong_ho)
        exam_layout.addLayout(header_exam)

        # Nút điều khiển âm thanh Listening TTS riêng
        self.row_audio = QHBoxLayout()
        self.btn_phat_am_thanh = QPushButton("Phát Âm Thanh Nghe (Listen to Audio)")
        self.btn_phat_am_thanh.setProperty("class", "btn-primary")
        self.btn_phat_am_thanh.setStyleSheet("font-size: 14px; font-weight: bold; color: #FFFFFF; padding: 8px 16px; background-color: #00A2FF;")
        self.btn_phat_am_thanh.clicked.connect(self.phat_am_thanh_nghe)

        self.btn_dung_am_thanh = QPushButton("Dừng Âm Thanh")
        self.btn_dung_am_thanh.setProperty("class", "btn-secondary")
        self.btn_dung_am_thanh.setStyleSheet("font-size: 14px; font-weight: bold; color: #FFFFFF; padding: 8px 16px;")
        self.btn_dung_am_thanh.clicked.connect(self.dung_am_thanh_nghe)

        self.row_audio.addWidget(self.btn_phat_am_thanh)
        self.row_audio.addWidget(self.btn_dung_am_thanh)
        self.row_audio.addStretch()
        exam_layout.addLayout(self.row_audio)

        # Nội dung câu hỏi chữ trắng
        self.lbl_noidung = QLabel("Nội dung câu hỏi IELTS...")
        self.lbl_noidung.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF; min-height: 60px;")
        self.lbl_noidung.setWordWrap(True)
        exam_layout.addWidget(self.lbl_noidung)

        # Các thẻ phương án đáp án
        self.vung_options = QWidget()
        self.vung_options_layout = QVBoxLayout(self.vung_options)
        exam_layout.addWidget(self.vung_options)

        # Vùng hiển thị giải thích chi tiết
        self.lbl_giai_thich = QLabel("")
        self.lbl_giai_thich.setWordWrap(True)
        self.lbl_giai_thich.setStyleSheet("background-color: #002B4D; padding: 12px; border-radius: 8px; color: #FFFFFF; font-size: 15px; font-weight: bold; margin-top: 10px; border: 2px solid #0084FF;")
        self.lbl_giai_thich.hide()
        exam_layout.addWidget(self.lbl_giai_thich)

        self.scroll_area.setWidget(self.exam_frame)
        main_layout.addWidget(self.scroll_area)

        # Thanh điều hướng làm bài
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

        self.btn_minigame = QPushButton("Minigame Thư Giãn")
        self.btn_minigame.setProperty("class", "btn-primary")
        self.btn_minigame.setStyleSheet("color: #FFFFFF; font-weight: bold; background-color: #00A2FF;")
        self.btn_minigame.clicked.connect(self.mo_minigame_giua_gio)

        self.btn_nop_bai = QPushButton("Nộp bài & Chấm điểm")
        self.btn_nop_bai.setProperty("class", "btn-success")
        self.btn_nop_bai.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.btn_nop_bai.clicked.connect(self.nop_bai_thi)

        nav_layout.addWidget(self.btn_truoc)
        nav_layout.addWidget(self.btn_sau)
        nav_layout.addWidget(self.btn_giai_thich)
        nav_layout.addWidget(self.btn_minigame)
        nav_layout.addStretch()
        nav_layout.addWidget(self.btn_nop_bai)

        main_layout.addLayout(nav_layout)

        # Khởi tạo mặc định tải phân môn Từ vựng
        self.chuyen_phan_mon("KT Từ Vựng")

    def thay_doi_band(self, text):
        """Khi thay đổi Band điểm mục tiêu Target."""
        self.chuyen_phan_mon(self.phan_mon_hien_tai)

    def chuyen_phan_mon(self, ten_mon):
        """Chuyển đổi phân môn trong Tập Thi IELTS theo Band điểm."""
        QuanLyAmThanh.get_instance().dung_giong_noi_ai()
        self.phan_mon_hien_tai = ten_mon
        self.cac_cau_da_choi_minigame.clear()
        band = self.cbo_band_ielts.currentText()

        # Cập nhật style nút chọn
        all_btns = [
            (self.btn_tu_vung, "KT Từ Vựng"),
            (self.btn_ngu_phap, "Ngữ Pháp & Các Thì"),
            (self.btn_doc, "Đọc Hiểu Reading"),
            (self.btn_nghe, "Luyện Nghe Listening"),
            (self.btn_tong_hop, "Đề Thi IELTS Tổng Hợp")
        ]
        for btn, name in all_btns:
            if name == ten_mon:
                btn.setProperty("class", "btn-primary")
                btn.setStyleSheet("font-size: 13px; font-weight: bold; color: #FFFFFF; padding: 8px 14px; background-color: #00A2FF;")
            else:
                btn.setProperty("class", "btn-secondary")
                btn.setStyleSheet("font-size: 13px; font-weight: bold; color: #FFFFFF; padding: 8px 14px;")

        if ten_mon == "KT Từ Vựng":
            self.de_thi = lay_danh_sach_tu_vung_ielts(band)
        elif ten_mon == "Ngữ Pháp & Các Thì":
            self.de_thi = lay_danh_sach_ngu_phap_va_thi(band)
        elif ten_mon == "Đọc Hiểu Reading":
            self.de_thi = lay_bai_doc_ielts_reading(band)
        elif ten_mon == "Luyện Nghe Listening":
            self.de_thi = lay_bai_nghe_ielts_listening(band)
        else:
            self.de_thi = lay_de_thi_ielts_tong_hop(band)

        self.cau_hoi_idx = 0
        self.dap_an_user = {}
        self.da_nop_bai = False
        self.lbl_giai_thich.hide()
        self.thoi_gian_con_lai = 900

        self.lbl_de_info.setText(f"TẬP THI IELTS - PHÂN MÔN: {ten_mon.upper()} - {band.upper()} ({len(self.de_thi)} CÂU HỎI - 15 PHÚT)")
        self.timer.start(1000)
        self.hien_thi_cau_hoi()

    def cap_nhat_dong_ho(self):
        if self.thoi_gian_con_lai > 0:
            self.thoi_gian_con_lai -= 1
            phut = self.thoi_gian_con_lai // 60
            giay = self.thoi_gian_con_lai % 60
            self.lbl_dong_ho.setText(f"Thời gian: {phut:02d}:{giay:02d}")
        else:
            self.timer.stop()
            QMessageBox.warning(self, "Hết giờ", "Hết thời gian làm bài Tập Thi IELTS! Hệ thống tự động nộp bài.")
            self.nop_bai_thi()

    def hien_thi_cau_hoi(self):
        QuanLyAmThanh.get_instance().dung_giong_noi_ai()
        if not self.de_thi:
            return

        cau_current = self.de_thi[self.cau_hoi_idx]
        self.lbl_cau_so.setText(f"Câu {self.cau_hoi_idx + 1} / {len(self.de_thi)}")

        is_listening = cau_current.get("is_listening", False) or self.phan_mon_hien_tai == "Luyện Nghe Listening"
        if is_listening:
            self.btn_phat_am_thanh.show()
            self.btn_dung_am_thanh.show()
            self.lbl_noidung.setText(f"[BÀI NGHE IELTS LISTENING - Hãy bấm nút 'Phát Âm Thanh Nghe' để nghe máy đọc kịch bản bài nghe và chọn đáp án bên dưới]\n\n{cau_current['cau_hoi']}")
            # Tự động phát giọng đọc âm thanh kịch bản bài nghe
            script_audio = cau_current.get("script_audio", "")
            if script_audio:
                QuanLyAmThanh.get_instance().phat_giong_noi_ai(script_audio)
        else:
            self.btn_phat_am_thanh.hide()
            self.btn_dung_am_thanh.hide()
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

        if self.da_nop_bai or not self.lbl_giai_thich.isHidden():
            self.cap_nhat_lbl_giai_thich()

    def phat_am_thanh_nghe(self):
        """Phát âm thanh kịch bản bài nghe bằng TTS."""
        if not self.de_thi:
            return
        cau_current = self.de_thi[self.cau_hoi_idx]
        script_audio = cau_current.get("script_audio", "")
        if script_audio:
            QuanLyAmThanh.get_instance().phat_giong_noi_ai(script_audio)
        else:
            QuanLyAmThanh.get_instance().phat_giong_noi_ai(cau_current.get("cau_hoi", ""))

    def dung_am_thanh_nghe(self):
        """Dừng âm thanh bài nghe."""
        QuanLyAmThanh.get_instance().dung_giong_noi_ai()

    def cap_nhat_lbl_giai_thich(self):
        if not self.de_thi:
            return
        cau_current = self.de_thi[self.cau_hoi_idx]
        dap_an = cau_current.get('dap_an_dung', '')
        giai_thich = cau_current.get('giai_thich', '')
        band = self.cbo_band_ielts.currentText()
        script_text = f"\nKịch bản âm thanh bài nghe: {cau_current.get('script_audio', '')}" if cau_current.get('script_audio') else ""
        self.lbl_giai_thich.setText(f"[Tập Thi IELTS - {self.phan_mon_hien_tai} - {band}]\nĐáp án đúng của Câu {self.cau_hoi_idx + 1}: {dap_an}{script_text}\n\n{giai_thich}")
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
        QuanLyAmThanh.get_instance().dung_giong_noi_ai()
        self.timer.stop()
        if not self.de_thi:
            return

        self.da_nop_bai = True
        ket_qua = cham_bai_lam(self.de_thi, self.dap_an_user)
        xp_nhan, coin_nhan = cong_phan_thuong(ket_qua["diem_so"], ket_qua["so_cau_dung"])

        band = self.cbo_band_ielts.currentText()
        msg = f"""
KẾT QUẢ TẬP THI IELTS ({self.phan_mon_hien_tai.upper()} - {band.upper()}):
- Điểm số: {ket_qua['diem_so']} / 10 ({ket_qua['phan_tram']}%)
- Số câu đúng: {ket_qua['so_cau_dung']} / {ket_qua['tong_cau']}
- Xếp loại: {ket_qua['xep_loai']}
- Phần thưởng: +{xp_nhan} XP và +{coin_nhan} Coin!
        """
        QMessageBox.information(self, "Kết quả Tập Thi IELTS", msg)
        self.cap_nhat_lbl_giai_thich()

        # Mở minigame thư giãn sau khi hoàn thành
        self.mo_minigame_giua_gio()

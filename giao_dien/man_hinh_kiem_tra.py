# Thu muc: giao_dien
# File: man_hinh_kiem_tra.py
# Mo ta: Man hinh cac che do kiem tra tuong tac voi thoi gian lam bai Tat ca chu mau trang sang ro net

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QFrame, QComboBox, 
    QMessageBox, QScrollArea, QCheckBox
)

from PyQt6.QtCore import QTimer, Qt
from xu_ly_kiem_tra.dong_co_javascript import chay_javascript_sinh_de
from xu_ly_kiem_tra.bo_cham_diem import cham_bai_lam
from xu_ly_hoc_tap.quan_ly_tien_do import kiem_tra_mo_khoa_bai_hoc
from giao_dien.dap_an_tuong_tac import TheDapAnGroup
from giao_dien.hop_thoai_tao_de import HopThoaiTaoDeDialog
from giao_dien.hop_thoai_chung_nhan import HopThoaiChungNhan
from giao_dien.hop_thoai_minigame_giua_gio import HopThoaiMinigameGiuaGioDialog


class ManHinhKiemTra(QWidget):
    """Màn hình trung tâm kiểm tra và thi thử thông minh với TẤT CẢ CHỮ LÀ CHỮ TRẮNG SÁNG."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.de_thi = []
        self.cau_hoi_idx = 0
        self.dap_an_user = {}
        self.da_nop_bai = False
        self.thoi_gian_con_lai = 600
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.cap_nhat_dong_ho)
        
        self.lop_hien_tai = "Lớp 6"
        self.chu_de_hien_tai = "Số nguyên và Các phép tính"
        self.cac_cau_da_choi_minigame = set()

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Tiêu đề chữ trắng
        title_label = QLabel("HỆ THỐNG KIỂM TRA VÀ THI THỬ SIÊU CLUB HỌC TẬP")
        title_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #FFFFFF;")
        main_layout.addWidget(title_label)

        # Chọn loại kiểm tra & Nút Tạo đề mới
        mode_frame = QFrame()
        mode_frame.setProperty("class", "card-widget")
        mode_layout = QHBoxLayout(mode_frame)

        lbl_loai = QLabel("Chọn loại kiểm tra:")
        lbl_loai.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")
        self.cbo_loai_kt = QComboBox()
        self.cbo_loai_kt.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.cbo_loai_kt.addItems([
            "Kiểm tra nhanh (10 câu, 10 phút)",
            "Kiểm tra cuối bài (Mở khóa bài khi đạt >=80%)",
            "Kiểm tra cuối chương (25 câu, 25 phút)",
            "Kiểm tra giữa kỳ (Chương trình nhà trường)",
            "Kiểm tra cuối kỳ (Mô phỏng thi thật)",
            "Thi thử tốt nghiệp THPT / HSG"
        ])

        btn_tao_de_moi = QPushButton("Tạo đề mới")
        btn_tao_de_moi.setProperty("class", "btn-primary")
        btn_tao_de_moi.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        btn_tao_de_moi.clicked.connect(self.mo_hop_thoai_tao_de)

        self.chk_auto_minigame = QCheckBox("Chơi Minigame sau mỗi câu")
        self.chk_auto_minigame.setChecked(True)
        self.chk_auto_minigame.setStyleSheet("color: #00FFCC; font-weight: bold; font-size: 14px;")

        mode_layout.addWidget(lbl_loai)
        mode_layout.addWidget(self.cbo_loai_kt)
        mode_layout.addWidget(self.chk_auto_minigame)
        mode_layout.addWidget(btn_tao_de_moi)

        main_layout.addWidget(mode_frame)


        # Vùng bài thi hiện tại
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.exam_frame = QFrame()
        self.exam_frame.setProperty("class", "card-widget")
        exam_layout = QVBoxLayout(self.exam_frame)

        # Đồng hồ đếm ngược nổi bật và Tiến độ chữ trắng
        header_exam = QHBoxLayout()
        self.lbl_cau_so = QLabel("Câu 1 / 15")
        self.lbl_cau_so.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF;")

        self.lbl_dong_ho = QLabel("Thời gian còn lại: Chưa bắt đầu")
        self.lbl_dong_ho.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF; background-color: #002B4D; padding: 6px 16px; border-radius: 14px; border: 2px solid #00A2FF;")

        header_exam.addWidget(self.lbl_cau_so)
        header_exam.addStretch()
        header_exam.addWidget(self.lbl_dong_ho)
        exam_layout.addLayout(header_exam)

        # Câu hỏi chữ trắng
        self.lbl_noidung = QLabel("Nhấn 'Tạo đề mới' để chọn Lớp, Chủ đề và Thời gian làm bài.")
        self.lbl_noidung.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF;")
        self.lbl_noidung.setWordWrap(True)
        exam_layout.addWidget(self.lbl_noidung)

        # Phương án đáp án tương tác
        self.vung_options = QWidget()
        self.vung_options_layout = QVBoxLayout(self.vung_options)
        exam_layout.addWidget(self.vung_options)

        # Vùng hiển thị giải thích chi tiết chữ trắng
        self.lbl_giai_thich = QLabel("")
        self.lbl_giai_thich.setWordWrap(True)
        self.lbl_giai_thich.setStyleSheet("background-color: #002B4D; padding: 12px; border-radius: 10px; color: #FFFFFF; font-size: 15px; font-weight: bold; margin-top: 10px; border: 2px solid #0084FF;")
        self.lbl_giai_thich.hide()
        exam_layout.addWidget(self.lbl_giai_thich)

        self.scroll_area.setWidget(self.exam_frame)
        main_layout.addWidget(self.scroll_area)

        # Thanh điều hướng chữ trắng
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

        self.btn_nop_bai = QPushButton("Nộp bài thi")
        self.btn_nop_bai.setProperty("class", "btn-success")
        self.btn_nop_bai.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.btn_nop_bai.clicked.connect(self.nop_bai_thi)

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


    def mo_hop_thoai_tao_de(self):
        """Mở Hộp thoại Dialog chọn Lớp 1-12, Chủ đề và Thời gian làm bài."""
        dialog = HopThoaiTaoDeDialog(self)
        dialog.de_thi_duoc_tao.connect(self.tao_de_tu_dialog)
        dialog.exec()

    def tao_de_tu_dialog(self, cauhinh):
        """Tải đề thi mới từ JavaScript & Internet API theo Lớp, Chủ đề và Thời gian chọn."""
        self.lop_hien_tai = cauhinh.get("ten_lop", "Lớp 6")
        self.chu_de_hien_tai = cauhinh.get("ten_chuong", "Số nguyên và Các phép tính")
        self.de_thi = chay_javascript_sinh_de(cauhinh["ten_lop"], cauhinh["ten_mon"], cauhinh["ten_chuong"], cauhinh["so_cau"])
        self.cau_hoi_idx = 0
        self.dap_an_user = {}
        self.da_nop_bai = False
        self.lbl_giai_thich.hide()

        thoi_gian_phut = cauhinh.get("thoi_gian_phut", 10)
        self.thoi_gian_con_lai = thoi_gian_phut * 60
        
        self.timer.start(1000)
        self.hien_thi_cau_hoi()
        QMessageBox.information(self, "Tạo đề thành công", f"Đã tạo thành công đề kiểm tra cho {cauhinh['ten_lop']} - Chủ đề: {cauhinh['ten_chuong']} (Thời gian: {thoi_gian_phut} phút)!")

    def cap_nhat_dong_ho(self):
        """Cập nhật thời gian đếm ngược."""
        if self.thoi_gian_con_lai > 0:
            self.thoi_gian_con_lai -= 1
            phut = self.thoi_gian_con_lai // 60
            giay = self.thoi_gian_con_lai % 60
            self.lbl_dong_ho.setText(f"Thời gian còn lại: {phut:02d}:{giay:02d}")
        else:
            self.timer.stop()
            QMessageBox.warning(self, "Hết thời gian", "Hết thời gian làm bài! Hệ thống tự động nộp bài.")
            self.nop_bai_thi()

    def hien_thi_cau_hoi(self):
        """Cập nhật giao diện câu hỏi với các thẻ bấm đáp án trực quan chữ trắng."""
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
        """Nộp bài, chấm điểm, hiển thị Giấy chứng nhận và mở khóa bài tiếp theo nếu đạt >=80%."""
        self.timer.stop()
        if not self.de_thi:
            return

        self.da_nop_bai = True
        ket_qua = cham_bai_lam(self.de_thi, self.dap_an_user)
        mo_khoa = kiem_tra_mo_khoa_bai_hoc(self.chu_de_hien_tai, ket_qua["phan_tram"])

        thong_bao_mo_khoa = "\nCHÚC MỪNG: Em đã đạt trên 80% và MỞ KHÓA bài học tiếp theo!" if mo_khoa else "\nEm cần đạt từ 80% trở lên để mở khóa bài tiếp theo."

        msg = f"""
KẾT QUẢ KIỂM TRA:
- Điểm số: {ket_qua['diem_so']} / 10
- Tỷ lệ đúng: {ket_qua['phan_tram']}%
- Số câu đúng: {ket_qua['so_cau_dung']} / {ket_qua['tong_cau']}
- Xếp loại: {ket_qua['xep_loai']}
- Nội dung còn yếu: {', '.join(ket_qua['noi_dung_yeu']) if ket_qua['noi_dung_yeu'] else 'Không có'}{thong_bao_mo_khoa}
        """
        QMessageBox.information(self, "Kết quả kiểm tra", msg)
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

        # Mở minigame thư giãn giữa giờ sau bài kiểm tra
        self.mo_minigame_giua_gio()


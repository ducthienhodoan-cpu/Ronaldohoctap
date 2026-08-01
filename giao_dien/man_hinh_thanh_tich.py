# Thu muc: giao_dien
# File: man_hinh_thanh_tich.py
# Mo ta: Man hinh hien thi danh hieu, phan thuong va bo suu tap Giay chung nhan cua Sieu Club Hoc Tap sang Tieng Viet co dau

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QFrame, QListWidget, QListWidgetItem, QProgressBar, QPushButton
)
from PyQt6.QtCore import Qt
from xu_ly_hoc_tap.he_thong_thuong import lay_thong_tin_thuong
from xu_ly_hoc_tap.quan_ly_tien_do import cap_nhat_streak
from xu_ly_hoc_tap.quan_ly_chung_nhan import lay_danh_sach_chung_nhan
from giao_dien.hop_thoai_chung_nhan import HopThoaiChungNhan

class ManHinhThanhTich(QWidget):
    """Màn hình hiển thị danh hiệu, XP, Coin, Huy hiệu và Bộ sưu tập Giấy chứng nhận bài tập chủ đề."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Tiêu đề
        title_label = QLabel("THÀNH TÍCH & BỘ SƯU TẬP GIẤY CHỨNG NHẬN")
        title_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #1E1B4B;")
        main_layout.addWidget(title_label)

        # Card tổng quan XP & Coin & Level
        info_frame = QFrame()
        info_frame.setProperty("class", "card-widget")
        info_layout = QHBoxLayout(info_frame)

        self.lbl_xp = QLabel("XP: 1200")
        self.lbl_xp.setStyleSheet("font-size: 16px; font-weight: bold; color: #4F46E5;")
        
        self.lbl_coin = QLabel("Coin: 350")
        self.lbl_coin.setStyleSheet("font-size: 16px; font-weight: bold; color: #D97706;")

        self.lbl_level = QLabel("Cấp độ: 2 (Tân binh Siêu Club)")
        self.lbl_level.setStyleSheet("font-size: 16px; font-weight: bold; color: #059669;")

        self.lbl_streak = QLabel("Chuỗi học: 3 ngày liên tiếp")
        self.lbl_streak.setStyleSheet("font-size: 16px; font-weight: bold; color: #DC2626;")

        info_layout.addWidget(self.lbl_xp)
        info_layout.addWidget(self.lbl_coin)
        info_layout.addWidget(self.lbl_level)
        info_layout.addWidget(self.lbl_streak)

        main_layout.addWidget(info_frame)

        # Danh sách Giấy chứng nhận bài tập chủ đề đã đạt được
        cert_frame = QFrame()
        cert_frame.setProperty("class", "card-widget")
        cert_layout = QVBoxLayout(cert_frame)

        lbl_cert_title = QLabel("Bộ sưu tập Giấy chứng nhận hoàn thành Bài tập chủ đề:")
        lbl_cert_title.setStyleSheet("font-size: 16px; font-weight: bold; color: #B45309;")
        cert_layout.addWidget(lbl_cert_title)

        self.list_chung_nhan = QListWidget()
        self.list_chung_nhan.itemDoubleClicked.connect(self.xem_chi_tiet_chung_nhan)
        cert_layout.addWidget(self.list_chung_nhan)

        main_layout.addWidget(cert_frame)

        # Danh sách Huy hiệu & Bộ sưu tập danh hiệu
        list_frame = QFrame()
        list_frame.setProperty("class", "card-widget")
        list_layout = QVBoxLayout(list_frame)

        lbl_badge_title = QLabel("Bộ sưu tập Huy hiệu & Danh hiệu đạt được:")
        lbl_badge_title.setStyleSheet("font-size: 16px; font-weight: bold; color: #1E1B4B;")
        list_layout.addWidget(lbl_badge_title)

        self.list_badges = QListWidget()
        list_layout.addWidget(self.list_badges)

        main_layout.addWidget(list_frame)

        # Cập nhật thông tin ban đầu
        self.tai_du_lieu_thanh_tich()

    def xem_chi_tiet_chung_nhan(self, item):
        """Mở hộp thoại Giấy chứng nhận khi học sinh nhấp đúp vào item."""
        data_cert = item.data(Qt.ItemDataRole.UserRole)
        if data_cert:
            dlg = HopThoaiChungNhan(
                parent=self, 
                lop=data_cert.get("lop", "Lớp 6"), 
                chu_de=data_cert.get("chu_de", "Bài tập chủ đề"), 
                phan_tram_diem=data_cert.get("phan_tram", 100.0), 
                diem_so=data_cert.get("diem_so", 10.0)
            )
            dlg.exec()

    def tai_du_lieu_thanh_tich(self):
        """Tải dữ liệu thưởng, huy hiệu và danh sách Giấy chứng nhận."""
        data = lay_thong_tin_thuong()
        streak = cap_nhat_streak()

        self.lbl_xp.setText(f"XP tích lũy: {data.get('xp', 0)}")
        self.lbl_coin.setText(f"Coin thưởng: {data.get('coin', 0)}")
        self.lbl_level.setText(f"Cấp độ: {data.get('cap_do', 1)} ({data.get('danh_hieu', 'Tân binh')})")
        self.lbl_streak.setText(f"Chuỗi học: {streak} ngày liên tiếp")

        # Tải danh sách chứng nhận
        self.list_chung_nhan.clear()
        ds_cert = lay_danh_sach_chung_nhan()
        
        if not ds_cert:
            # Tạo 1 mẫu chứng nhận khởi đầu nếu chưa có
            item_sample = QListWidgetItem("Chưa có giấy chứng nhận. Hãy hoàn thành 1 bài tập chủ đề để nhận ngay chứng nhận đầu tiên!")
            item_sample.setFlags(item_sample.flags() & ~Qt.ItemFlag.ItemIsSelectable)
            self.list_chung_nhan.addItem(item_sample)
        else:
            for c in ds_cert:
                text_item = f"[CHỨNG NHẬN HOÀN THÀNH] - Tên: {c['ten']} | Lớp: {c['lop']} | Chủ đề: {c['chu_de']} | Mức đạt: {c['muc_dat']} ({c['ngay_cap']})"
                item = QListWidgetItem(text_item)
                item.setData(Qt.ItemDataRole.UserRole, c)
                self.list_chung_nhan.addItem(item)

        # Tải danh sách huy hiệu
        self.list_badges.clear()
        huy_hieu_list = data.get("huy_hieu", [])
        if not huy_hieu_list:
            huy_hieu_list = [
                "Huy hiệu Tân binh Siêu Club: Hoàn thành bài học đầu tiên",
                "Huy hiệu Chăm chỉ: Học liên tiếp 3 ngày",
                "Huy hiệu Thông thái: Đạt điểm 10 ở bài kiểm tra nhanh",
                "Huy hiệu Nhà toán học: Giải đúng 50 câu hỏi Toán",
                "Huy hiệu Lập trình viên: Hoàn thành chủ đề Python"
            ]

        for hh in huy_hieu_list:
            item = QListWidgetItem(f"   [Đã đạt] {hh}")
            self.list_badges.addItem(item)

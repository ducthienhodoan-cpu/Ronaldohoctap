# Thu muc: giao_dien
# File: man_hinh_ke_hoach_hoc.py
# Mo ta: Man hinh Lich Hoc Tap va Muc Tieu Roblox Streak bang PyQt6

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QCheckBox, QFrame, QScrollArea, QMessageBox
)
from PyQt6.QtCore import Qt

from xu_ly_so_tay.quan_ly_ke_hoach_hoc import doc_ke_hoach_hoc, cap_nhat_trang_thai_muc_tieu
from xu_ly_am_thanh.quan_ly_am_thanh import QuanLyAmThanh

class ManHinhKeHoachHoc(QWidget):
    """Màn hình Lịch học tập hàng ngày và chuỗi Roblox Streak."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(12)

        # Tiêu đề chữ trắng
        title_label = QLabel("LỊCH HỌC TẬP HÀNG NGÀY & CHUỖI ROBLOX STREAK")
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #FFFFFF;")
        main_layout.addWidget(title_label)

        # Khung chuỗi Streak
        streak_frame = QFrame()
        streak_frame.setProperty("class", "card-widget")
        streak_frame.setStyleSheet("background-color: #002B4D; border: 3px solid #00A2FF; border-radius: 15px; padding: 15px;")
        streak_layout = QHBoxLayout(streak_frame)

        self.lbl_streak = QLabel("Chuỗi ngày học liên tục: 5 ngày Streak")
        self.lbl_streak.setStyleSheet("font-size: 18px; font-weight: bold; color: #FFFFFF;")

        lbl_xp = QLabel("Phần thưởng hoàn thành: +100 Roblox XP mỗi ngày")
        lbl_xp.setStyleSheet("font-size: 15px; font-weight: bold; color: #2ECC71;")

        streak_layout.addWidget(self.lbl_streak)
        streak_layout.addStretch()
        streak_layout.addWidget(lbl_xp)

        main_layout.addWidget(streak_frame)

        # Vùng cuộn danh sách mục tiêu
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("QScrollArea { border: none; background-color: transparent; }")

        self.list_widget = QWidget()
        self.list_layout = QVBoxLayout(self.list_widget)
        self.list_layout.setContentsMargins(0, 5, 0, 5)
        self.list_layout.setSpacing(10)

        self.scroll_area.setWidget(self.list_widget)
        main_layout.addWidget(self.scroll_area)

        # Tải danh sách ban đầu
        self.tai_ke_hoach()

    def tai_ke_hoach(self):
        """Tải danh sách mục tiêu và chuỗi Streak."""
        for i in reversed(range(self.list_layout.count())):
            item = self.list_layout.itemAt(i)
            if item.widget():
                item.widget().setParent(None)

        data = doc_ke_hoach_hoc()
        streak = data.get("streak_ngay", 0)
        self.lbl_streak.setText(f"Chuỗi ngày học liên tục: {streak} ngày Streak")

        danh_sach = data.get("danh_sach_muc_tieu", [])

        for item in danh_sach:
            m_id = item.get("id")
            noi_dung = item.get("noi_dung", "")
            hoan_thanh = item.get("hoan_thanh", False)
            xp = item.get("xp", 50)

            card = QFrame()
            card.setProperty("class", "card-widget")
            card.setStyleSheet("background-color: #001F3F; border: 2px solid #00A2FF; border-radius: 10px; padding: 12px;")
            card_layout = QHBoxLayout(card)

            chk = QCheckBox(f"{noi_dung} (+{xp} Roblox XP)")
            chk.setChecked(hoan_thanh)
            chk.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px;")
            chk.setCursor(Qt.CursorShape.PointingHandCursor)
            chk.stateChanged.connect(lambda state, idx=m_id: self.thay_doi_muc_tieu(idx, state == 2))

            card_layout.addWidget(chk)
            self.list_layout.addWidget(card)

        self.list_layout.addStretch()

    def thay_doi_muc_tieu(self, m_id, checked):
        """Cập nhật trạng thái mục tiêu học tập."""
        QuanLyAmThanh.get_instance().phat_hieu_ung_dap_an()
        data = cap_nhat_trang_thai_muc_tieu(m_id, checked)
        streak = data.get("streak_ngay", 0)
        self.lbl_streak.setText(f"Chuỗi ngày học liên tục: {streak} ngày Streak")

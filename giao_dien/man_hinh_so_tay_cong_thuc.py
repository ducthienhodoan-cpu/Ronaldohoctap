# Thu muc: giao_dien
# File: man_hinh_so_tay_cong_thuc.py
# Mo ta: Man hinh So tay Cong thuc va Khai niem Trong tam THCS bang PyQt6

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QFrame, QComboBox, QLineEdit, QScrollArea
)
from PyQt6.QtCore import Qt

from du_lieu_giao_duc.kho_cong_thuc import lay_danh_sach_cong_thuc

class ManHinhSoTayCongThuc(QWidget):
    """Màn hình tra cứu Sổ tay công thức và khái niệm trọng tâm THCS."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(12)

        # Tiêu đề chữ trắng
        title_label = QLabel("SỔ TAY CÔNG THỨC VÀ KHÁI NIỆM TRỌNG TÂM SGK THCS")
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #FFFFFF;")
        main_layout.addWidget(title_label)

        # Thanh lọc Lớp, Môn và Tìm kiếm
        filter_frame = QFrame()
        filter_frame.setProperty("class", "card-widget")
        filter_layout = QHBoxLayout(filter_frame)

        lbl_lop = QLabel("Khối Lớp:")
        lbl_lop.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")
        self.cbo_lop = QComboBox()
        self.cbo_lop.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px;")
        self.cbo_lop.addItems(["Lớp 6", "Lớp 7", "Lớp 8", "Lớp 9"])
        self.cbo_lop.currentTextChanged.connect(self.tai_danh_sach_cong_thuc)

        lbl_mon = QLabel("Môn học:")
        lbl_mon.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")
        self.cbo_mon = QComboBox()
        self.cbo_mon.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px;")
        self.cbo_mon.addItems(["Tất cả", "Toán", "Khoa học tự nhiên", "Tin học", "Tiếng Anh"])
        self.cbo_mon.currentTextChanged.connect(self.tai_danh_sach_cong_thuc)

        self.txt_search = QLineEdit()
        self.txt_search.setPlaceholderText("Nhập từ khóa tìm kiếm công thức...")
        self.txt_search.setStyleSheet("background-color: #001F3F; color: #FFFFFF; font-size: 14px; border: 1px solid #00A2FF; border-radius: 6px; padding: 6px 12px;")
        self.txt_search.textChanged.connect(self.tai_danh_sach_cong_thuc)

        filter_layout.addWidget(lbl_lop)
        filter_layout.addWidget(self.cbo_lop)
        filter_layout.addWidget(lbl_mon)
        filter_layout.addWidget(self.cbo_mon)
        filter_layout.addWidget(self.txt_search, 2)

        main_layout.addWidget(filter_frame)

        # Vùng cuộn danh sách công thức
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
        self.tai_danh_sach_cong_thuc()

    def tai_danh_sach_cong_thuc(self):
        """Tải và hiển thị thẻ công thức theo bộ lọc."""
        # Xóa danh sách cũ
        for i in reversed(range(self.list_layout.count())):
            item = self.list_layout.itemAt(i)
            if item.widget():
                item.widget().setParent(None)

        lop = self.cbo_lop.currentText()
        mon = self.cbo_mon.currentText()
        tu_khoa = self.txt_search.text().strip().lower()

        danh_sach = lay_danh_sach_cong_thuc(lop, mon)

        for item in danh_sach:
            ten = item.get("ten", "")
            ct = item.get("cong_thuc", "")
            vi_du = item.get("vi_du", "")
            m_item = item.get("mon", "")

            # Kiểm tra từ khóa tìm kiếm
            if tu_khoa and (tu_khoa not in ten.lower() and tu_khoa not in ct.lower()):
                continue

            card = QFrame()
            card.setProperty("class", "card-widget")
            card.setStyleSheet("background-color: #002B4D; border: 2px solid #00A2FF; border-radius: 10px; padding: 12px;")
            card_layout = QVBoxLayout(card)

            lbl_ten = QLabel(f"[{m_item} - {lop}] {ten}")
            lbl_ten.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF;")
            card_layout.addWidget(lbl_ten)

            lbl_ct = QLabel(f"Công thức: {ct}")
            lbl_ct.setStyleSheet("font-size: 15px; color: #FFFFFF; font-weight: bold; background-color: #001F3F; padding: 8px; border-radius: 6px;")
            lbl_ct.setWordWrap(True)
            card_layout.addWidget(lbl_ct)

            if vi_du:
                lbl_vd = QLabel(f"Ví dụ áp dụng: {vi_du}")
                lbl_vd.setStyleSheet("font-size: 14px; color: #FFFFFF;")
                lbl_vd.setWordWrap(True)
                card_layout.addWidget(lbl_vd)

            self.list_layout.addWidget(card)

        self.list_layout.addStretch()

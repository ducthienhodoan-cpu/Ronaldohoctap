# Thu muc: giao_dien
# File: man_hinh_so_loi_sai.py
# Mo ta: Man hinh So Loi Sai va On Lai Bai Kho bang PyQt6

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QFrame, QScrollArea, QMessageBox
)
from PyQt6.QtCore import Qt

from xu_ly_so_tay.quan_ly_so_loi_sai import doc_so_loi_sai, xoa_cau_loi_sai
from xu_ly_am_thanh.quan_ly_am_thanh import QuanLyAmThanh

class ManHinhSoLoiSai(QWidget):
    """Màn hình Sổ lỗi sai tập hợp các câu hỏi làm sai để học sinh ôn lại."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(12)

        # Tiêu đề chữ trắng
        title_label = QLabel("SỔ LỖI SAI VÀ ÔN LẠI BÀI KHÓ (MISTAKE NOTEBOOK)")
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #FFFFFF;")
        main_layout.addWidget(title_label)

        # Khung trạng thái & Tải lại
        status_frame = QFrame()
        status_frame.setProperty("class", "card-widget")
        status_layout = QHBoxLayout(status_frame)

        self.lbl_status = QLabel("Tổng số câu cần ôn lại: 0 câu hỏi")
        self.lbl_status.setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF;")

        btn_refresh = QPushButton("Tải lại Sổ lỗi sai")
        btn_refresh.setProperty("class", "btn-secondary")
        btn_refresh.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 14px; padding: 6px 16px;")
        btn_refresh.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_refresh.clicked.connect(self.tai_danh_sach_loi_sai)

        status_layout.addWidget(self.lbl_status)
        status_layout.addStretch()
        status_layout.addWidget(btn_refresh)

        main_layout.addWidget(status_frame)

        # Vùng cuộn danh sách các câu làm sai
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
        self.tai_danh_sach_loi_sai()

    def tai_danh_sach_loi_sai(self):
        """Tải lại danh sách câu hỏi trong Sổ lỗi sai."""
        for i in reversed(range(self.list_layout.count())):
            item = self.list_layout.itemAt(i)
            if item.widget():
                item.widget().setParent(None)

        danh_sach = doc_so_loi_sai()
        self.lbl_status.setText(f"Tổng số câu cần ôn lại: {len(danh_sach)} câu hỏi làm sai")

        if not danh_sach:
            lbl_empty = QLabel("Tuyệt vời! Bạn không có câu hỏi nào bị làm sai trong Sổ lỗi sai.")
            lbl_empty.setStyleSheet("font-size: 16px; font-weight: bold; color: #2ECC71; padding: 30px;")
            lbl_empty.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.list_layout.addWidget(lbl_empty)
            return

        for idx, item in enumerate(danh_sach):
            cau_text = item.get("cau_hoi", "")
            dap_an_dung = item.get("dap_an_dung", "")
            giai_thich = item.get("giai_thich", "")

            card = QFrame()
            card.setProperty("class", "card-widget")
            card.setStyleSheet("background-color: #002B4D; border: 2px solid #E74C3C; border-radius: 10px; padding: 12px;")
            card_layout = QVBoxLayout(card)

            lbl_cau = QLabel(f"Câu {idx + 1}: {cau_text}")
            lbl_cau.setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF;")
            lbl_cau.setWordWrap(True)
            card_layout.addWidget(lbl_cau)

            lbl_da = QLabel(f"Đáp án đúng chính xác: {dap_an_dung}")
            lbl_da.setStyleSheet("font-size: 14px; font-weight: bold; color: #2ECC71; background-color: #001F3F; padding: 6px 10px; border-radius: 6px;")
            card_layout.addWidget(lbl_da)

            if giai_thich:
                lbl_gt = QLabel(f"Lời giải chi tiết: {giai_thich}")
                lbl_gt.setStyleSheet("font-size: 14px; color: #FFFFFF;")
                lbl_gt.setWordWrap(True)
                card_layout.addWidget(lbl_gt)

            btn_da_hieu = QPushButton("Đã hiểu bài - Xóa khỏi sổ lỗi sai")
            btn_da_hieu.setProperty("class", "btn-primary")
            btn_da_hieu.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 13px; background-color: #2ECC71; padding: 6px 12px;")
            btn_da_hieu.setCursor(Qt.CursorShape.PointingHandCursor)
            btn_da_hieu.clicked.connect(lambda checked, text=cau_text: self.xoa_khoi_so(text))

            row_act = QHBoxLayout()
            row_act.addStretch()
            row_act.addWidget(btn_da_hieu)
            card_layout.addLayout(row_act)

            self.list_layout.addWidget(card)

        self.list_layout.addStretch()

    def xoa_khoi_so(self, cau_text):
        """Xóa câu hỏi khỏi Sổ lỗi sai khi học sinh đã hiểu bài."""
        xoa_cau_loi_sai(cau_text)
        QuanLyAmThanh.get_instance().phat_hieu_ung_dap_an()
        QMessageBox.information(self, "Sổ lỗi sai", "Đã xóa câu hỏi khỏi Sổ lỗi sai thành công!")
        self.tai_danh_sach_loi_sai()

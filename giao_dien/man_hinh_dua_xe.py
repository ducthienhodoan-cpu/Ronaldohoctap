# Thu muc: giao_dien
# File: man_hinh_dua_xe.py
# Mo ta: Man hinh Giai Dua Xe Sieu Cap Roblox 3D tang toc do va tan suat 3 muc do nhanh ngau kich tinh sang Tieng Viet co dau

import os
import random
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QFrame, QMessageBox, QDialog,
    QProgressBar, QComboBox, QScrollArea, QStackedWidget
)
from PyQt6.QtCore import QTimer, Qt, QRectF, QPointF
from PyQt6.QtGui import QPainter, QColor, QFont, QPen, QBrush, QPixmap, QPolygonF, QLinearGradient

from du_lieu.kho_noi_dung_hoc import lay_danh_sach_lop, lay_danh_sach_mon_hoc
from xu_ly_tro_choi.quan_ly_dua_xe import khoi_tao_duong_dua_xe, sinh_vat_the_duong_dua
from xu_ly_hoc_tap.he_thong_thuong import cong_phan_thuong
from giao_dien.dap_an_tuong_tac import TheDapAnGroup
from giao_dien.hop_thoai_chung_nhan import HopThoaiChungNhan

class HopThoaiCauHoiMayMan(QDialog):
    """Hộp thoại câu hỏi may mắn khi ăn Hộp Quà 3D trên đường đua."""

    def __init__(self, parent, cau_hoi_dict):
        super().__init__(parent)
        self.setWindowTitle("HỘP QUÀ MAY MẮN TRÊN ĐƯỜNG ĐUA 3D")
        self.setFixedSize(560, 390)
        self.setStyleSheet("QDialog { background-color: #191B1D; color: #FFFFFF; font-size: 15px; }")
        self.cau_hoi_dict = cau_hoi_dict
        self.tra_loi_dung = False
        self.dap_an_user = ""

        self.init_ui()

    def init_ui(self):
        l = QVBoxLayout(self)
        l.setContentsMargins(20, 20, 20, 20)
        l.setSpacing(15)

        title = QLabel("BẠN VỪA ĂN HỘP QUÀ MAY MẮN 3D!")
        title.setStyleSheet("font-size: 19px; font-weight: bold; color: #FFC107;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        l.addWidget(title)

        lbl_desc = QLabel("Trả lời ĐÚNG để nhận quà thưởng +50 XP và +20 Robux Coin! Trả lời SAI không sao cả!")
        lbl_desc.setStyleSheet("font-size: 14px; color: #FFFFFF; font-weight: bold;")
        lbl_desc.setWordWrap(True)
        l.addWidget(lbl_desc)

        card_q = QFrame()
        card_q.setStyleSheet("background-color: #232527; border: 2px solid #00A2FF; border-radius: 10px; padding: 12px;")
        ql = QVBoxLayout(card_q)

        q_text = self.cau_hoi_dict.get("cau_hoi", "Phép tính ngẫu nhiên?")
        lbl_q = QLabel(q_text)
        lbl_q.setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF;")
        lbl_q.setWordWrap(True)
        ql.addWidget(lbl_q)

        opts = self.cau_hoi_dict.get("dap_an", ["A", "B", "C", "D"])
        self.widget_opts = TheDapAnGroup(opts)
        self.widget_opts.dap_an_thay_doi.connect(self.luu_dap_an)
        ql.addWidget(self.widget_opts)

        l.addWidget(card_q)

        btn_confirm = QPushButton("Xác Nhận Đáp Án Hộp Quà")
        btn_confirm.setProperty("class", "btn-primary")
        btn_confirm.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px; padding: 10px 20px;")
        btn_confirm.clicked.connect(self.xac_nhan_dap_an)
        l.addWidget(btn_confirm)

    def luu_dap_an(self, text):
        self.dap_an_user = text

    def xac_nhan_dap_an(self):
        correct = str(self.cau_hoi_dict.get("dap_an_dung", "")).strip()
        user = str(self.dap_an_user).strip()

        if user == correct:
            self.tra_loi_dung = True
            QMessageBox.information(self, "Trả Lời Đúng", "CHÚC MỪNG! Đáp án chính xác! Em nhận được +50 XP và +20 Robux Coin!")
        else:
            self.tra_loi_dung = False
            QMessageBox.information(self, "Chưa Đúng", f"Chưa chính xác! Đáp án đúng là {correct}. Đừng lo, hãy tiếp tục tăng tốc về đích!")
        self.accept()


class CanvasDuongDua3D(QWidget):
    """Vùng vẽ Canvas đường đua 3D Pseudo-Perspective 60 FPS hỗ trợ 3 Mức độ Dễ, Bình thường, Khó với tốc độ lướt siêu nhanh."""

    def __init__(self, parent_screen):
        super().__init__()
        self.screen = parent_screen
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        
        self.game_timer = QTimer(self)
        self.game_timer.timeout.connect(self.update_game_frame)
        self.road_anim_step = 0

        # Sprite paths 3D
        self.path_car_3d = r"C:\Users\Admin\.gemini\antigravity-ide\brain\fcb0a507-c860-48bb-bc03-3398a0afb7bf\3d_super_car_sprite_1785127768574.png"
        self.path_gift_3d = r"C:\Users\Admin\.gemini\antigravity-ide\brain\fcb0a507-c860-48bb-bc03-3398a0afb7bf\3d_gift_box_sprite_1785127757441.png"

        self.pix_car = QPixmap(self.path_car_3d) if os.path.exists(self.path_car_3d) else None
        self.pix_gift = QPixmap(self.path_gift_3d) if os.path.exists(self.path_gift_3d) else None

    def start_race(self):
        self.setFocus()
        self.game_timer.start(16)

    def stop_race(self):
        self.game_timer.stop()

    def keyPressEvent(self, event):
        key = event.key()
        if key in [Qt.Key.Key_A, Qt.Key.Key_Left]:
            self.screen.dieu_khien_sang_trai()
        elif key in [Qt.Key.Key_D, Qt.Key.Key_Right]:
            self.screen.dieu_khien_sang_phai()
        elif key in [Qt.Key.Key_W, Qt.Key.Key_Up]:
            self.screen.dieu_khien_nhay()
        elif key in [Qt.Key.Key_S, Qt.Key.Key_Down]:
            self.screen.dieu_khien_chom_nguoi()

    def keyReleaseEvent(self, event):
        key = event.key()
        if key in [Qt.Key.Key_W, Qt.Key.Key_Up, Qt.Key.Key_S, Qt.Key.Key_Down]:
            self.screen.giai_phong_trang_thai_y()

    def update_game_frame(self):
        if not self.screen.state["tro_choi_ket_thuc"]:
            self.road_anim_step = (self.road_anim_step + 18) % 80
            self.screen.cap_nhat_game_loop()
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        w = float(self.width())
        h = float(self.height())
        horizon_y = h * 0.32

        # 1. Bầu trời đêm 3D Roblox
        sky_grad = QLinearGradient(0, 0, 0, horizon_y)
        sky_grad.setColorAt(0.0, QColor("#08090C"))
        sky_grad.setColorAt(1.0, QColor("#1A233A"))
        painter.fillRect(0, 0, int(w), int(horizon_y), QBrush(sky_grad))

        # Ngôi sao phát sáng 3D
        painter.setPen(QColor("#00E676"))
        for star_x, star_y in [(w*0.15, h*0.1), (w*0.4, h*0.08), (w*0.7, h*0.12), (w*0.88, h*0.06)]:
            painter.drawPoint(int(star_x), int(star_y))

        # 2. Mặt đất hai bên đường 3D
        ground_grad = QLinearGradient(0, horizon_y, 0, h)
        ground_grad.setColorAt(0.0, QColor("#0D1620"))
        ground_grad.setColorAt(1.0, QColor("#05080E"))
        painter.fillRect(0, int(horizon_y), int(w), int(h - horizon_y), QBrush(ground_grad))

        # 3. Đường đua 3D Perspective
        vp_x = w * 0.5
        top_left = QPointF(vp_x - w * 0.12, horizon_y)
        top_right = QPointF(vp_x + w * 0.12, horizon_y)
        bot_left = QPointF(w * 0.05, h)
        bot_right = QPointF(w * 0.95, h)

        road_poly = QPolygonF([top_left, top_right, bot_right, bot_left])
        road_grad = QLinearGradient(0, horizon_y, 0, h)
        road_grad.setColorAt(0.0, QColor("#1B222A"))
        road_grad.setColorAt(1.0, QColor("#2A3545"))
        painter.setBrush(QBrush(road_grad))
        painter.setPen(QPen(QColor("#00E676"), 3))
        painter.drawPolygon(road_poly)

        # 2 vạch phân làn 3D
        for t_ratio in [0.333, 0.666]:
            top_px = top_left.x() + (top_right.x() - top_left.x()) * t_ratio
            bot_px = bot_left.x() + (bot_right.x() - bot_left.x()) * t_ratio
            pen_lane = QPen(QColor("#00E676"), 3, Qt.PenStyle.DashLine)
            painter.setPen(pen_lane)
            painter.drawLine(QPointF(top_px, horizon_y), QPointF(bot_px, h))

        # 4. Vạch Đích 3D (khi > 850m)
        qd = self.screen.state["quang_duong"]
        if qd >= 850:
            scale_dich = (qd - 850) / 150.0
            y_dich = horizon_y + scale_dich * (h - horizon_y) * 0.7
            painter.fillRect(int(w * 0.15), int(y_dich), int(w * 0.7), 28, QColor("#FFD700"))
            painter.setPen(QColor("#191B1D"))
            painter.setFont(QFont("Segoe UI", 13, QFont.Weight.Bold))
            painter.drawText(int(w * 0.15), int(y_dich), int(w * 0.7), 28, Qt.AlignmentFlag.AlignCenter, "VẠCH ĐÍCH WORLD GRAND PRIX")

        # 5. Vẽ vật thể 3D (Hộp Quà May Mắn 3D, Hộp Rào Thấp Nhảy W, Cây Cầu Núp S)
        for obj in self.screen.danh_sach_vat_the:
            y_obj = float(obj["y"])
            if y_obj < horizon_y or y_obj > h:
                continue

            t_scale = (y_obj - horizon_y) / (h - horizon_y)
            t_scale = max(0.1, min(1.0, t_scale))

            lan_idx = obj["lan"]
            left_x = top_left.x() + (bot_left.x() - top_left.x()) * t_scale
            right_x = top_right.x() + (bot_right.x() - top_right.x()) * t_scale
            lane_w_3d = (right_x - left_x) / 3.0
            cx_3d = left_x + lan_idx * lane_w_3d + lane_w_3d / 2.0
            cy_3d = y_obj

            kieu = obj["kieu"]

            if kieu == "hop_qua_may_man":
                box_sz = int(46 * t_scale)
                if self.pix_gift:
                    pix_scaled = self.pix_gift.scaled(box_sz, box_sz, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                    painter.drawPixmap(int(cx_3d - box_sz / 2.0), int(cy_3d - box_sz / 2.0), pix_scaled)
                else:
                    painter.setBrush(QBrush(QColor("#FFC107")))
                    painter.setPen(QPen(QColor("#FFFFFF"), 2))
                    painter.drawRect(int(cx_3d - box_sz / 2.0), int(cy_3d - box_sz / 2.0), box_sz, box_sz)

                painter.setPen(QColor("#FFEA00"))
                painter.setFont(QFont("Segoe UI", max(9, int(11 * t_scale)), QFont.Weight.Bold))
                painter.drawText(int(cx_3d - 40), int(cy_3d - box_sz / 2.0 - 18), 80, 20, Qt.AlignmentFlag.AlignCenter, "HỘP QUÀ")

            elif kieu == "chong_ngai_thap":
                bw = int(lane_w_3d * 0.8)
                bh = int(25 * t_scale)
                bx = int(cx_3d - bw / 2.0)
                by = int(cy_3d - bh)

                painter.setBrush(QBrush(QColor("#FF9100")))
                painter.setPen(QPen(QColor("#FFFFFF"), 2))
                painter.drawRect(bx, by, bw, bh)

                painter.setPen(QColor("#FFFFFF"))
                painter.setFont(QFont("Segoe UI", max(9, int(11 * t_scale)), QFont.Weight.Bold))
                painter.drawText(bx, by - 20, bw, 20, Qt.AlignmentFlag.AlignCenter, "^ NHẢY (W) ^")

            elif kieu == "chong_ngai_cao":
                bw = int(lane_w_3d * 0.9)
                bh = int(30 * t_scale)
                bx = int(cx_3d - bw / 2.0)
                by = int(cy_3d - 50 * t_scale)

                painter.setBrush(QBrush(QColor("#FF1744")))
                painter.setPen(QPen(QColor("#FFFFFF"), 2))
                painter.drawRect(bx, int(by), int(10 * t_scale), int(50 * t_scale))
                painter.drawRect(int(bx + bw - 10 * t_scale), int(by), int(10 * t_scale), int(50 * t_scale))
                painter.drawRect(bx, by, bw, bh)

                painter.setPen(QColor("#FFFFFF"))
                painter.setFont(QFont("Segoe UI", max(9, int(11 * t_scale)), QFont.Weight.Bold))
                painter.drawText(bx, int(by + bh + 4), bw, 20, Qt.AlignmentFlag.AlignCenter, "v NÚP CHỒM (S) v")

            else:
                bw = int(lane_w_3d * 0.75)
                bh = int(35 * t_scale)
                bx = int(cx_3d - bw / 2.0)
                by = int(cy_3d - bh)
                painter.setBrush(QBrush(QColor("#D500F9")))
                painter.setPen(QPen(QColor("#FFFFFF"), 2))
                painter.drawRect(bx, by, bw, bh)

        # 6. Xe Đua 3D Của Học Sinh
        lan_user = self.screen.state["vi_tri_lan"]
        st_y = self.screen.state["trang_thai_y"]

        user_cy = h * 0.80
        left_u = top_left.x() + (bot_left.x() - top_left.x()) * 0.8
        right_u = top_right.x() + (bot_right.x() - top_right.x()) * 0.8
        lane_w_u = (right_u - left_u) / 3.0
        car_cx = left_u + lan_user * lane_w_u + lane_w_u / 2.0

        if st_y == 1:
            user_cy -= 55
        elif st_y == 2:
            user_cy += 18

        car_w = 75
        car_h = 100
        if self.pix_car:
            pix_c_scaled = self.pix_car.scaled(car_w, car_h, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            painter.drawPixmap(int(car_cx - car_w / 2.0), int(user_cy - car_h / 2.0), pix_c_scaled)
        else:
            painter.setBrush(QBrush(QColor("#00E676")))
            painter.setPen(QPen(QColor("#FFFFFF"), 3))
            painter.drawRoundedRect(int(car_cx - 32), int(user_cy - 45), 64, 90, 12, 12)

        painter.setPen(QColor("#FFFFFF"))
        painter.setFont(QFont("Segoe UI", 11, QFont.Weight.Bold))
        if st_y == 1:
            painter.drawText(int(car_cx - 50), int(user_cy - car_h / 2.0 - 20), 100, 20, Qt.AlignmentFlag.AlignCenter, "ĐANG NHẢY (W)")
        elif st_y == 2:
            painter.drawText(int(car_cx - 50), int(user_cy + car_h / 2.0 + 4), 100, 20, Qt.AlignmentFlag.AlignCenter, "ĐANG NÚP (S)")


class ManHinhDuaXe(QWidget):
    """Màn hình Giải Đua Xe Siêu Cấp Roblox với 3 Mức độ Dễ, Bình thường, Khó và phím A/D/W/S."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.state = khoi_tao_duong_dua_xe("Bình thường")
        self.danh_sach_vat_the = []
        self.spawning_cooldown = 0
        self.path_cover_3d = r"C:\Users\Admin\.gemini\antigravity-ide\brain\fcb0a507-c860-48bb-bc03-3398a0afb7bf\roblox_racing_cover_3d_1785127533504.png"

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(10)

        # Tiêu đề chính chữ trắng
        title = QLabel("GIẢI ĐUA XE SIÊU CẤP ROBLOX GRAND PRIX (3 MỨC ĐỘ TỐC ĐỘ CAO KỊCH TÍNH)")
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: #FFFFFF;")
        main_layout.addWidget(title)

        # StackedWidget chứa 2 màn hình: 0 - Màn hình Chờ / Hướng dẫn đồ họa 3D, 1 - Màn hình Đua xe 3D 60 FPS
        self.stack_racing = QStackedWidget()

        # --- INTRO SCREEN 0: MÀN HÌNH CHỜ CHỌN MỨC ĐỘ VÀ HƯỚNG DẪN 3D ---
        self.screen_intro = QWidget()
        intro_layout = QVBoxLayout(self.screen_intro)
        intro_layout.setContentsMargins(10, 10, 10, 10)
        intro_layout.setSpacing(12)

        card_intro = QFrame()
        card_intro.setProperty("class", "card-widget")
        card_intro_layout = QHBoxLayout(card_intro)
        card_intro_layout.setSpacing(20)

        # Trái: Đồ họa Banner Xe Đua 3D
        self.lbl_img_cover = QLabel()
        self.lbl_img_cover.setFixedSize(220, 220)
        self.lbl_img_cover.setScaledContents(True)
        if os.path.exists(self.path_cover_3d):
            self.lbl_img_cover.setPixmap(QPixmap(self.path_cover_3d))
        card_intro_layout.addWidget(self.lbl_img_cover)

        # Phải: Thông tin & Hướng dẫn 3 Mức độ chơi Dễ (70% Quà - 30% Vật cản), Bình thường (50/50), Khó (70% Vật cản - 30% Quà)
        info_vbox = QVBoxLayout()
        info_vbox.setSpacing(8)

        lbl_game_name = QLabel("HỆ THỐNG 3 MỨC ĐỘ TỐC ĐỘ VÀ VẬT CẢN DỒN DẬP 3D")
        lbl_game_name.setStyleSheet("font-size: 18px; font-weight: bold; color: #00E676;")
        info_vbox.addWidget(lbl_game_name)

        desc_rules = QLabel(
            "Em hãy lựa chọn Mức độ chơi phù hợp với phản xạ tay lái:\n"
            "- DỄ: 70% Hộp Quà - 30% Vật cản (Tốc độ mượt nhanh, chướng ngại vật sinh động xuất hiện liên tục).\n"
            "- BÌNH THƯỜNG: 50% Hộp Quà - 50% Vật cản (Tốc độ siêu tốc lướt nhanh, dồn dập rào nhảy W & cầu núp S).\n"
            "- KHÓ: 70% Vật cản - 30% Hộp Quà (Tốc độ cực hạn kịch tính dồn dập).\n"
            "Điều khiển phím: A/D (Rẽ trái/phải) | W (Nhảy qua rào thấp) | S (Núp chổm qua cây cầu cao)."
        )
        desc_rules.setStyleSheet("font-size: 14px; color: #FFFFFF; font-weight: bold; line-height: 1.5;")
        desc_rules.setWordWrap(True)
        info_vbox.addWidget(desc_rules)

        # Bộ lọc Chọn Mức độ, Chọn Lớp & Môn học
        row_sel = QHBoxLayout()
        lbl_md = QLabel("Mức độ:")
        lbl_md.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.cbo_muc_do_intro = QComboBox()
        self.cbo_muc_do_intro.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 14px;")
        self.cbo_muc_do_intro.addItems([
            "Dễ (70% Quà - 30% Vật cản - Tốc độ Nhanh)", 
            "Bình thường (50% Quà - 50% Vật cản - Tốc độ Siêu tốc)", 
            "Khó (70% Vật cản - 30% Quà - Tốc độ Cực hạn)"
        ])
        self.cbo_muc_do_intro.setCurrentIndex(0)

        lbl_lop = QLabel("Lớp:")
        lbl_lop.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.cbo_lop = QComboBox()
        self.cbo_lop.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.cbo_lop.addItems(lay_danh_sach_lop())
        self.cbo_lop.setCurrentText("Lớp 6")

        lbl_mon = QLabel("Môn:")
        lbl_mon.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.cbo_mon = QComboBox()
        self.cbo_mon.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.cbo_mon.addItems(lay_danh_sach_mon_hoc("Lớp 6"))

        row_sel.addWidget(lbl_md)
        row_sel.addWidget(self.cbo_muc_do_intro)
        row_sel.addWidget(lbl_lop)
        row_sel.addWidget(self.cbo_lop)
        row_sel.addWidget(lbl_mon)
        row_sel.addWidget(self.cbo_mon)
        info_vbox.addLayout(row_sel)

        btn_play_now = QPushButton("BẮT ĐẦU CHƠI GIẢI ĐUA XE NGAY")
        btn_play_now.setProperty("class", "btn-primary")
        btn_play_now.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 16px; padding: 12px 24px; background-color: #00E676;")
        btn_play_now.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_play_now.clicked.connect(self.chuyen_sang_man_hinh_dua)

        info_vbox.addWidget(btn_play_now)
        card_intro_layout.addLayout(info_vbox, 1)
        intro_layout.addWidget(card_intro)

        # --- GAMEPLAY SCREEN 1: MÀN HÌNH ĐUA XE TRỰC TIẾP 3D ---
        self.screen_gameplay = QWidget()
        gameplay_layout = QVBoxLayout(self.screen_gameplay)
        gameplay_layout.setContentsMargins(0, 0, 0, 0)
        gameplay_layout.setSpacing(8)

        # Thanh trạng thái HUD
        status_frame = QFrame()
        status_frame.setProperty("class", "card-widget")
        status_layout = QHBoxLayout(status_frame)

        self.lbl_muc_do_hud = QLabel("MỨC ĐỘ: DỄ (70% QUÀ - 30% VẬT CẢN)")
        self.lbl_muc_do_hud.setStyleSheet("font-size: 15px; font-weight: bold; color: #FFEA00; background-color: #002B4D; padding: 6px 14px; border-radius: 10px; border: 2px solid #FFEA00;")

        self.lbl_mang_song = QLabel("MẠNG SỐNG: 3 / 3 TIM")
        self.lbl_mang_song.setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF; background-color: #002B4D; padding: 6px 14px; border-radius: 10px; border: 2px solid #00E676;")

        self.lbl_quang_duong = QLabel("TIẾN ĐỘ VẠCH ĐÍCH: 0m / 1000m")
        self.lbl_quang_duong.setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF; background-color: #002B4D; padding: 6px 14px; border-radius: 10px; border: 2px solid #00A2FF;")

        btn_back_to_intro = QPushButton("Đổi Mức Độ & Hướng Dẫn")
        btn_back_to_intro.setProperty("class", "btn-secondary")
        btn_back_to_intro.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 13px;")
        btn_back_to_intro.clicked.connect(self.chuyen_sang_man_hinh_intro)

        status_layout.addWidget(self.lbl_muc_do_hud)
        status_layout.addWidget(self.lbl_mang_song)
        status_layout.addWidget(self.lbl_quang_duong)
        status_layout.addStretch()
        status_layout.addWidget(btn_back_to_intro)
        gameplay_layout.addWidget(status_frame)

        # Canvas đua xe 3D 60 FPS
        self.canvas = CanvasDuongDua3D(self)
        self.canvas.setMinimumHeight(420)
        gameplay_layout.addWidget(self.canvas)

        self.stack_racing.addWidget(self.screen_intro)      # 0
        self.stack_racing.addWidget(self.screen_gameplay)   # 1

        main_layout.addWidget(self.stack_racing)

    def chuyen_sang_man_hinh_intro(self):
        self.canvas.stop_race()
        self.stack_racing.setCurrentIndex(0)

    def chuyen_sang_man_hinh_dua(self):
        self.stack_racing.setCurrentIndex(1)
        self.bat_dau_lai_dua_xe()

    def bat_dau_lai_dua_xe(self):
        muc_do_text = self.cbo_muc_do_intro.currentText()
        if "Dễ" in muc_do_text:
            ten_muc_do = "Dễ"
            desc_hud = "DỄ (70% QUÀ - 30% VẬT CẢN)"
        elif "Khó" in muc_do_text:
            ten_muc_do = "Khó"
            desc_hud = "KHÓ (70% VẬT CẢN - 30% QUÀ)"
        else:
            ten_muc_do = "Bình thường"
            desc_hud = "BÌNH THƯỜNG (50/50)"

        self.state = khoi_tao_duong_dua_xe(ten_muc_do)
        self.danh_sach_vat_the = []
        self.spawning_cooldown = 0
        
        self.lbl_muc_do_hud.setText(f"MỨC ĐỘ: {desc_hud}")
        self.lbl_mang_song.setText(f"MẠNG SỐNG: {self.state['so_mang']} / 3 TIM")
        self.lbl_quang_duong.setText("TIẾN ĐỘ VẠCH ĐÍCH: 0m / 1000m")
        self.canvas.start_race()

    def dieu_khien_sang_trai(self):
        if self.state["vi_tri_lan"] > 0:
            self.state["vi_tri_lan"] -= 1

    def dieu_khien_sang_phai(self):
        if self.state["vi_tri_lan"] < 2:
            self.state["vi_tri_lan"] += 1

    def dieu_khien_nhay(self):
        self.state["trang_thai_y"] = 1

    def dieu_khien_chom_nguoi(self):
        self.state["trang_thai_y"] = 2

    def giai_phong_trang_thai_y(self):
        self.state["trang_thai_y"] = 0

    def cap_nhat_game_loop(self):
        if self.state["tro_choi_ket_thuc"]:
            return

        # Tăng quãng đường
        self.state["quang_duong"] += 3
        qd = self.state["quang_duong"]
        self.lbl_quang_duong.setText(f"TIẾN ĐỘ VẠCH ĐÍCH: {qd}m / 1000m")

        # Tốc độ di chuyển vật thể nhanh sinh động theo Mức độ
        muc_do = self.state.get("muc_do", "Bình thường")
        if muc_do == "Dễ":
            speed_step = 10  # Dễ: Tốc độ 10 mượt nhanh sinh động
            cd_range = (18, 28)
        elif muc_do == "Khó":
            speed_step = 18  # Khó: Tốc độ 18 siêu tốc kịch tính
            cd_range = (10, 16)
        else:
            speed_step = 14  # Bình thường: Tốc độ 14 rất nhanh dồn dập
            cd_range = (14, 22)

        # Sinh vật thể ngẫu nhiên theo tỷ lệ Dễ / Bình thường / Khó
        self.spawning_cooldown -= 1
        if self.spawning_cooldown <= 0:
            self.spawning_cooldown = random.randint(cd_range[0], cd_range[1])
            vt = sinh_vat_the_duong_dua(self.cbo_mon.currentText(), self.cbo_lop.currentText(), muc_do)
            vt["y"] = self.canvas.height() * 0.32
            self.danh_sach_vat_the.append(vt)

        # Di chuyển vật thể xuống dưới
        to_remove = []
        h_canvas = float(self.canvas.height())
        for obj in self.danh_sach_vat_the:
            obj["y"] += speed_step
            
            # Xử lý va chạm
            y_user_min = h_canvas * 0.72
            y_user_max = h_canvas * 0.85
            if y_user_min <= obj["y"] <= y_user_max:
                if obj["lan"] == self.state["vi_tri_lan"]:
                    kieu = obj["kieu"]
                    st_y = self.state["trang_thai_y"]

                    if kieu == "hop_qua_may_man":
                        to_remove.append(obj)
                        self.an_hop_qua_may_man(obj)
                        break

                    elif kieu == "chong_ngai_thap":
                        if st_y != 1:
                            to_remove.append(obj)
                            self.xu_ly_va_cham("Hộp Rào Thấp dưới đất (Bấm W để NHẢY qua)!")
                            break

                    elif kieu == "chong_ngai_cao":
                        if st_y != 2:
                            to_remove.append(obj)
                            self.xu_ly_va_cham("Cây Cầu Bắc Ngang trên cao (Bấm S để NÚP CHỒM bên dưới)!")
                            break

                    else:
                        to_remove.append(obj)
                        self.xu_ly_va_cham("Rào chắn trên đường!")
                        break

            if obj["y"] > h_canvas:
                to_remove.append(obj)

        for r in to_remove:
            if r in self.danh_sach_vat_the:
                self.danh_sach_vat_the.remove(r)

        # Kiểm tra Thắng giải đua xe (1000m)
        if qd >= 1000:
            self.state["tro_choi_ket_thuc"] = True
            self.canvas.stop_race()
            cong_phan_thuong(10.0, 10)
            QMessageBox.information(
                self, 
                "VÔ ĐỊCH GIẢI ĐUA XE ROBLOX", 
                f"XUẤT SẮC! Em đã điều khiển xe đua vượt qua Mức độ {muc_do.upper()} và VỀ ĐÍCH ĐẦU TIÊN!\n"
                "Thưởng: +100 XP và Cúp Vô Địch Giải Đua Xe Roblox!"
            )
            dlg_cert = HopThoaiChungNhan(
                parent=self, 
                lop=self.cbo_lop.currentText(), 
                chu_de=f"NHÀ VÔ ĐỊCH GIẢI ĐUA XE ROBLOX (MỨC ĐỘ {muc_do.upper()})", 
                phan_tram_diem=100, 
                diem_so=10.0
            )
            dlg_cert.exec()
            self.chuyen_sang_man_hinh_intro()

    def an_hop_qua_may_man(self, obj):
        """Tạm dừng xe và hiển thị câu hỏi may mắn khi ăn Hộp Quà 3D."""
        self.canvas.stop_race()
        cau_hoi = obj.get("cau_hoi")
        if not cau_hoi:
            cau_hoi = {
                "cau_hoi": "Số liền sau của số 99 trong bài học là số nào?",
                "dap_an": ["100", "98", "101", "90"],
                "dap_an_dung": "100"
            }
        
        dlg = HopThoaiCauHoiMayMan(self, cau_hoi)
        dlg.exec()
        
        if dlg.tra_loi_dung:
            cong_phan_thuong(10.0, 2)
            self.state["diem_so"] += 50
        
        if not self.state["tro_choi_ket_thuc"]:
            self.canvas.start_race()

    def xu_ly_va_cham(self, ten_chong_ngai="Chướng ngại vật"):
        """Xử lý va chạm chướng ngại vật: trừ 1 mạng sống. Đụng 3 lần = THUA."""
        self.state["so_mang"] -= 1
        self.lbl_mang_song.setText(f"MẠNG SỐNG: {self.state['so_mang']} / 3 TIM")

        if self.state["so_mang"] <= 0:
            self.state["tro_choi_ket_thuc"] = True
            self.canvas.stop_race()
            QMessageBox.warning(
                self, 
                "Kết Quả Giải Đua Xe 3D", 
                "Rất tiếc! Xe đua đã đụng chướng ngại vật 3 lần!\n"
                "Bấm 'BẮT ĐẦU CHƠI GIẢI ĐUA XE NGAY' để thử sức lại nhé!"
            )
            self.chuyen_sang_man_hinh_intro()
        else:
            QMessageBox.warning(
                self, 
                "Va Chạm Chướng Ngại Vật 3D", 
                f"CẢNH BÁO: Xe đua bị đụng {ten_chong_ngai}!\n"
                f"Mạng sống còn lại: {self.state['so_mang']} Tim.\n"
                f"Gợi ý: Bấm W để Nhảy qua rào thấp, bấm S để Núp chổm qua cây cầu cao!"
            )

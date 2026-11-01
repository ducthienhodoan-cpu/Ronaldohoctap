# Thu muc: giao_dien
# File: hop_thoai_video_penalty.py
# Mo ta: Hop thoai phat hoat hoa Video 3D mo phong cu sut Penalty 60 FPS (Ghi ban ngau nhien goc, Sut len troi 50%, Thu mon can pha 50%)

import math
import random
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QFrame, QWidget
)
from PyQt6.QtCore import QTimer, Qt, QRectF, QPointF
from PyQt6.QtGui import (
    QPainter, QColor, QFont, QPen, QBrush, 
    QLinearGradient, QRadialGradient, QPolygonF
)
from xu_ly_am_thanh.quan_ly_am_thanh import QuanLyAmThanh

class CanvasVideoPenalty(QWidget):
    """Vung ve hoat canh Video 3D cu sut Penalty 60 FPS voi do hoa ruc ro."""

    def __init__(self, ket_qua_dict, parent_dialog=None):
        super().__init__()
        self.ket_qua = ket_qua_dict
        self.dialog = parent_dialog
        self.setMinimumSize(640, 420)

        # Cac tham so vat ly va hoat hoa
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.cap_nhat_frame)
        self.progress = 0.0          # Tien trinh 0.0 -> 1.0 (sut bong) -> 1.5 (an mung/ket thuc)
        self.anim_speed = 0.022      # Toc do hoat hoa
        self.net_shake = 0.0         # Do rung cua luoi
        self.particles = []          # Cac hat tia sang bieu dien ban thang hoac va cham
        self.stars = []              # Cac vi sao bau troi dem

        # Khoi tao cac vi sao nen
        for _ in range(40):
            self.stars.append((random.random(), random.random() * 0.45, random.randint(1, 3)))

        # Khoi tao vi tri dich den cua qua bong
        self.init_goc_sut()

    def init_goc_sut(self):
        goc = self.ket_qua.get("goc_id", "chinh_giua")
        if goc == "cao_trai":
            self.target_dx = -0.32
            self.target_dy = -0.16
        elif goc == "thap_trai":
            self.target_dx = -0.30
            self.target_dy = 0.05
        elif goc == "cao_phai":
            self.target_dx = 0.32
            self.target_dy = -0.16
        elif goc == "thap_phai":
            self.target_dx = 0.30
            self.target_dy = 0.05
        elif goc == "len_troi":
            self.target_dx = random.uniform(-0.15, 0.15)
            self.target_dy = -0.65  # Bay vuot xa ngang len troi
        else:
            self.target_dx = 0.0
            self.target_dy = -0.05

    def bat_dau_video(self):
        self.progress = 0.0
        self.net_shake = 0.0
        self.particles.clear()
        self.timer.start(16)

    def dung_video(self):
        self.timer.stop()

    def cap_nhat_frame(self):
        self.progress += self.anim_speed
        
        # Tao hieu ung hat sau khi bong toi dich
        if self.progress >= 0.85 and len(self.particles) < 35:
            w = float(self.width())
            h = float(self.height())
            cx = w * 0.5 + self.target_dx * w * 0.5
            cy = h * 0.55 + self.target_dy * h * 0.5
            
            mau_sac = ["#00E676", "#FFEA00", "#00A2FF", "#FFFFFF", "#FF1744"]
            for _ in range(4):
                self.particles.append({
                    "x": cx,
                    "y": cy,
                    "vx": random.uniform(-4.0, 4.0),
                    "vy": random.uniform(-5.0, 3.0),
                    "color": random.choice(mau_sac),
                    "life": 1.0,
                    "size": random.randint(3, 7)
                })

        # Cap nhat hat
        for p in self.particles:
            p["x"] += p["vx"]
            p["y"] += p["vy"]
            p["life"] -= 0.02

        # Hieu ung rung luoi
        if self.ket_qua.get("la_ban_thang") and self.progress >= 0.85:
            self.net_shake = math.sin(self.progress * 25.0) * max(0.0, 1.0 - (self.progress - 0.85))

        if self.progress >= 1.6:
            self.timer.stop()

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        w = float(self.width())
        h = float(self.height())

        # 1. Bau troi dem san van dong
        horizon_y = h * 0.45
        sky_grad = QLinearGradient(0, 0, 0, horizon_y)
        sky_grad.setColorAt(0.0, QColor("#020B14"))
        sky_grad.setColorAt(0.6, QColor("#0A192F"))
        sky_grad.setColorAt(1.0, QColor("#112240"))
        painter.fillRect(0, 0, int(w), int(horizon_y), QBrush(sky_grad))

        # Ve cac vi sao
        painter.setPen(Qt.PenStyle.NoPen)
        for sx, sy, sz in self.stars:
            painter.setBrush(QBrush(QColor(255, 255, 255, 180)))
            painter.drawEllipse(QPointF(sx * w, sy * horizon_y), float(sz), float(sz))

        # Den chieu sang san van dong
        for lx in [w * 0.12, w * 0.88]:
            light_grad = QRadialGradient(lx, horizon_y * 0.25, w * 0.35)
            light_grad.setColorAt(0.0, QColor(255, 255, 255, 130))
            light_grad.setColorAt(0.5, QColor(0, 162, 255, 40))
            light_grad.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setBrush(QBrush(light_grad))
            painter.drawEllipse(QPointF(lx, horizon_y * 0.25), w * 0.35, horizon_y * 0.35)

        # 2. Mat co San bong 3D Perspective
        pitch_poly = QPolygonF([
            QPointF(0, horizon_y),
            QPointF(w, horizon_y),
            QPointF(w, h),
            QPointF(0, h)
        ])
        pitch_grad = QLinearGradient(0, horizon_y, 0, h)
        pitch_grad.setColorAt(0.0, QColor("#14532D"))
        pitch_grad.setColorAt(0.5, QColor("#166534"))
        pitch_grad.setColorAt(1.0, QColor("#15803D"))
        painter.setBrush(QBrush(pitch_grad))
        painter.drawPolygon(pitch_poly)

        # Cac duong ke soc co
        painter.setPen(QPen(QColor(255, 255, 255, 40), 2))
        for i in range(1, 6):
            y_stripe = horizon_y + (h - horizon_y) * (i / 6.0)
            painter.drawLine(0, int(y_stripe), int(w), int(y_stripe))

        # Vong tron diem phat den 11m
        spot_x = w * 0.5
        spot_y = h * 0.88
        painter.setBrush(QBrush(QColor("#FFFFFF")))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(QPointF(spot_x, spot_y), 7.0, 4.0)

        # 3. Khung Thanh 3D va Luoi
        gw = w * 0.52
        gh = h * 0.32
        gx1 = (w - gw) / 2.0
        gx2 = gx1 + gw
        gy_top = horizon_y - gh * 0.55
        gy_bot = horizon_y + gh * 0.45

        # Ve phan Luoi khung thanh
        net_offset = self.net_shake * 8.0
        painter.setPen(QPen(QColor(255, 255, 255, 80), 1))
        # Luoi doc
        for col in range(16):
            nx = gx1 + (gw / 15.0) * col
            painter.drawLine(int(nx + net_offset * 0.5), int(gy_top), int(nx), int(gy_bot))
        # Luoi ngang
        for row in range(8):
            ny = gy_top + ((gy_bot - gy_top) / 7.0) * row
            painter.drawLine(int(gx1), int(ny + net_offset * 0.3), int(gx2), int(ny + net_offset * 0.3))

        # Khung cot doc va xa ngang
        post_pen = QPen(QColor("#FFFFFF"), 7, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap)
        painter.setPen(post_pen)
        painter.drawLine(int(gx1), int(gy_bot), int(gx1), int(gy_top))  # Cot trai
        painter.drawLine(int(gx2), int(gy_bot), int(gx2), int(gy_top))  # Cot phai
        painter.drawLine(int(gx1), int(gy_top), int(gx2), int(gy_top))  # Xa ngang

        # 4. Thu Mon 3D
        goalie_progress = min(1.0, self.progress / 0.85)
        goalie_center_x = w * 0.5
        goalie_center_y = gy_bot - 20

        goc_id = self.ket_qua.get("goc_id", "chinh_giua")
        ket_qua_loai = self.ket_qua.get("ket_qua", "ghi_ban")

        # Vi tri thu mon di chuyen
        if ket_qua_loai == "thu_mon_can_pha":
            # Thu mon bay dung huong de can pha
            target_goalie_x = goalie_center_x + (self.target_dx * w * 0.42)
            target_goalie_y = gy_top + (gy_bot - gy_top) * 0.5 + (self.target_dy * h * 0.3)
            current_gx = goalie_center_x + (target_goalie_x - goalie_center_x) * goalie_progress
            current_gy = goalie_center_y + (target_goalie_y - goalie_center_y) * goalie_progress
        elif ket_qua_loai == "ghi_ban":
            # Thu mon bay nguoc huong hoac cham hon bong
            target_goalie_x = goalie_center_x - (self.target_dx * w * 0.25)
            target_goalie_y = goalie_center_y - 15
            current_gx = goalie_center_x + (target_goalie_x - goalie_center_x) * (goalie_progress * 0.7)
            current_gy = goalie_center_y + (target_goalie_y - goalie_center_y) * (goalie_progress * 0.7)
        else: # sut_len_troi
            # Thu mon dung nhin bong bay len troi
            current_gx = goalie_center_x
            current_gy = goalie_center_y

        # Ve than Thu Mon
        painter.setPen(QPen(QColor("#00E5FF"), 3))
        painter.setBrush(QBrush(QColor("#00B0FF")))
        painter.drawRoundedRect(QRectF(current_gx - 18, current_gy - 42, 36, 45), 8, 8)
        # Dau Thu Mon
        painter.setPen(QPen(QColor("#FFFFFF"), 2))
        painter.setBrush(QBrush(QColor("#FFD54F")))
        painter.drawEllipse(QPointF(current_gx, current_gy - 55), 14.0, 14.0)
        # Gang tay Thu Mon
        painter.setBrush(QBrush(QColor("#FF1744")))
        painter.drawEllipse(QPointF(current_gx - 26, current_gy - 25), 8.0, 8.0)
        painter.drawEllipse(QPointF(current_gx + 26, current_gy - 25), 8.0, 8.0)

        # 5. Qua Bong Penalty & Quy dao bay 3D
        p_clamped = min(1.0, self.progress / 0.85)
        # Toa do qua bong bay tu cham 11m den dich
        ball_start_x = spot_x
        ball_start_y = spot_y
        
        if ket_qua_loai == "len_troi":
            ball_dest_x = w * 0.5 + self.target_dx * w * 0.6
            ball_dest_y = -60.0  # Bay mat len troi
        else:
            ball_dest_x = w * 0.5 + self.target_dx * w * 0.46
            ball_dest_y = gy_top + (gy_bot - gy_top) * 0.5 + (self.target_dy * h * 0.35)

        # Do cong parabol nhe
        arc = math.sin(p_clamped * math.pi) * -35.0
        ball_x = ball_start_x + (ball_dest_x - ball_start_x) * p_clamped
        ball_y = ball_start_y + (ball_dest_y - ball_start_y) * p_clamped + arc

        # Kich thuoc bong nho dan theo khoang cach 3D
        ball_radius = 24.0 - (p_clamped * 13.0)

        # Bong do cua qua bong tren san co
        shadow_y = ball_start_y + (gy_bot - ball_start_y) * p_clamped
        painter.setBrush(QBrush(QColor(0, 0, 0, int(100 * (1.0 - p_clamped * 0.5)))))
        painter.drawEllipse(QPointF(ball_x, shadow_y), ball_radius * 1.1, ball_radius * 0.4)

        # Ve Qua Bong Tron 3D Lục Giác
        ball_grad = QRadialGradient(ball_x - ball_radius * 0.3, ball_y - ball_radius * 0.3, ball_radius * 1.2)
        ball_grad.setColorAt(0.0, QColor("#FFFFFF"))
        ball_grad.setColorAt(0.7, QColor("#E2E8F0"))
        ball_grad.setColorAt(1.0, QColor("#64748B"))
        painter.setBrush(QBrush(ball_grad))
        painter.setPen(QPen(QColor("#0F172A"), 2))
        painter.drawEllipse(QPointF(ball_x, ball_y), ball_radius, ball_radius)

        # Hoa tiet den cua bong
        painter.setBrush(QBrush(QColor("#1E293B")))
        painter.drawEllipse(QPointF(ball_x, ball_y), ball_radius * 0.35, ball_radius * 0.35)

        # 6. Ve cac hat tia sang / phao hoa
        for p in self.particles:
            if p["life"] > 0:
                c = QColor(p["color"])
                c.setAlpha(int(max(0, min(255, p["life"] * 255))))
                painter.setBrush(QBrush(c))
                painter.drawEllipse(QPointF(p["x"], p["y"]), float(p["size"]), float(p["size"]))

        # 7. Banner Thong Bao Ket Qua Lon
        if self.progress >= 0.85:
            banner_rect = QRectF(w * 0.08, h * 0.08, w * 0.84, 80)
            if ket_qua_loai == "ghi_ban":
                bg_color = QColor(0, 230, 118, 230)
                text_color = "#002B18"
                tieu_de = "VAO OOO! BAN THANG TUYET DEP!"
                sub_text = self.ket_qua.get("mo_ta", "Ghi ban thanh cong vao goc!")
            elif ket_qua_loai == "sut_len_troi":
                bg_color = QColor(255, 107, 0, 230)
                text_color = "#FFFFFF"
                tieu_de = "SUT LEN TROI! BONG BAY VOT XA NGANG!"
                sub_text = "Cu sut qua manh, bong bay vuot qua xa len khan dai!"
            else:
                bg_color = QColor(239, 68, 68, 230)
                text_color = "#FFFFFF"
                tieu_de = "THU MON CAN PHA XUAT SAC!"
                sub_text = "Thu mon doi phuong da phan doan dung huong va day bong!"

            painter.setBrush(QBrush(bg_color))
            painter.setPen(QPen(QColor("#FFFFFF"), 3))
            painter.drawRoundedRect(banner_rect, 14, 14)

            painter.setPen(QColor(text_color))
            painter.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
            painter.drawText(banner_rect.adjusted(0, 8, 0, -35), Qt.AlignmentFlag.AlignCenter, tieu_de)

            painter.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
            painter.drawText(banner_rect.adjusted(10, 42, -10, -8), Qt.AlignmentFlag.AlignCenter, sub_text)


class HopThoaiVideoPenalty(QDialog):
    """Hop thoai trinh chieu Video 3D mo phong cu sut Penalty."""

    def __init__(self, ket_qua_dict, parent=None):
        super().__init__(parent)
        self.ket_qua = ket_qua_dict
        self.setWindowTitle("VIDEO TRUC TIEP PENALTY")
        self.setFixedSize(680, 530)
        self.setStyleSheet("QDialog { background-color: #0B0F19; border: 3px solid #00E676; border-radius: 16px; }")
        
        self.init_ui()
        self.canvas.bat_dau_video()

        # Phat am thanh hieu ung tuong ung
        am_thanh = QuanLyAmThanh.get_instance()
        if self.ket_qua.get("la_ban_thang"):
            am_thanh.phat_hieu_ung_tra_loi_dung()
        else:
            am_thanh.phat_hieu_ung_dap_an()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(12)

        # Header Title
        title_label = QLabel("KHOANH KHAC SUT PHAT PENALTY")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #FFFFFF;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)

        # Video Canvas 3D
        self.canvas = CanvasVideoPenalty(self.ket_qua, self)
        main_layout.addWidget(self.canvas)

        # Bottom Bar
        btn_layout = QHBoxLayout()
        lbl_info = QLabel(f"Ket qua: {self.ket_qua.get('goc_ten', 'Sut Penalty')}")
        lbl_info.setStyleSheet("color: #94A3B8; font-weight: bold; font-size: 14px;")
        btn_layout.addWidget(lbl_info)

        btn_layout.addStretch()

        self.lbl_countdown = QLabel("Tự động tiếp tục sau: 6 giây")
        self.lbl_countdown.setStyleSheet("color: #00FFCC; font-weight: bold; font-size: 13px; margin-right: 8px;")
        btn_layout.addWidget(self.lbl_countdown)

        self.btn_replay = QPushButton("Xem Lại Pha Sút")
        self.btn_replay.setStyleSheet("background-color: #1E293B; color: #FFFFFF; font-weight: bold; font-size: 13px; padding: 8px 16px; border: 2px solid #334155; border-radius: 8px;")
        self.btn_replay.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_replay.clicked.connect(self.xem_lai_video)
        btn_layout.addWidget(self.btn_replay)

        self.btn_close = QPushButton("Tiếp Tục Trận Đấu")
        self.btn_close.setStyleSheet("background-color: #00E676; color: #021C13; font-weight: bold; font-size: 14px; padding: 8px 20px; border-radius: 8px;")
        self.btn_close.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_close.clicked.connect(self.xac_nhan_dong)
        btn_layout.addWidget(self.btn_close)

        main_layout.addLayout(btn_layout)

        # Khoi tao bo dem nguoc 6 giay (tam 5 - 10 giay) de chuyen tiep muot ma
        self.countdown_giay = 6
        self.timer_countdown = QTimer(self)
        self.timer_countdown.timeout.connect(self.cap_nhat_countdown)
        self.timer_countdown.start(1000)

    def cap_nhat_countdown(self):
        self.countdown_giay -= 1
        if self.countdown_giay > 0:
            self.lbl_countdown.setText(f"Tự động tiếp tục sau: {self.countdown_giay} giây")
        else:
            self.dung_hoat_dong()
            self.accept()

    def xem_lai_video(self):
        self.countdown_giay = 6
        self.lbl_countdown.setText("Tự động tiếp tục sau: 6 giây")
        self.canvas.bat_dau_video()

    def dung_hoat_dong(self):
        """Dừng đồng hồ đếm ngược và hoạt cảnh video 3D penalty khi thoát ra."""
        if hasattr(self, 'timer_countdown') and self.timer_countdown.isActive():
            self.timer_countdown.stop()
        if hasattr(self, 'canvas'):
            self.canvas.dung_video()

    def xac_nhan_dong(self):
        self.dung_hoat_dong()
        self.accept()

    def reject(self):
        """Dừng đồng hồ và hoạt động khi bấm ESC hoặc đóng cửa sổ."""
        self.dung_hoat_dong()
        super().reject()

    def closeEvent(self, event):
        """Dừng tất cả đồng hồ và hoạt ảnh khi đóng hộp thoại."""
        self.dung_hoat_dong()
        event.accept()

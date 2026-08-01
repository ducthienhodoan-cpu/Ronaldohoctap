# Thu muc: thong_ke
# File: bieu_do_hoc_tap.py
# Mo ta: Ve bieu do thong ke tien do hoc tap su dung Matplotlib va PyQt6 sang Tieng Viet co dau

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class BieuDoHocTapCanvas(FigureCanvas):
    """Component vẽ biểu đồ điểm số và tiến độ học tập cho EduVerse AI sang Tiếng Việt có dấu."""
    
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi, facecolor='#FFFFFF')
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.setParent(parent)
        self.ve_bieu_do_mac_dinh()

    def ve_bieu_do_mac_dinh(self):
        """Vẽ biểu đồ xu hướng điểm số theo thời gian (Ngày/Tuần/Tháng)."""
        self.axes.clear()
        
        ngay = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ Nhật"]
        diem = [8.5, 9.0, 7.5, 8.8, 9.5, 10.0, 9.2]
        
        self.axes.plot(ngay, diem, marker='o', color='#4A90E2', linewidth=2.5, label='Điểm trung bình')
        self.axes.set_title("Biểu đồ điểm số theo ngày trong tuần", fontsize=12, color='#2C3E50', fontweight='bold')
        self.axes.set_ylabel("Điểm số (Thang 10)", fontsize=10)
        self.axes.set_ylim(0, 10.5)
        self.axes.grid(True, linestyle='--', alpha=0.5)
        self.axes.legend(loc='lower right')
        self.fig.tight_layout()
        self.draw()

    def ve_bieu_do_mon_hoc(self, danh_sach_mon, diem_mon):
        """Vẽ biểu đồ cột so sánh kết quả giữa các môn học."""
        self.axes.clear()
        
        mau_sac = ['#4A90E2', '#2ECC71', '#F1C40F', '#E74C3C', '#9B59B6']
        bars = self.axes.bar(danh_sach_mon, diem_mon, color=mau_sac[:len(danh_sach_mon)])
        
        self.axes.set_title("So sánh kết quả giữa các môn học", fontsize=12, color='#2C3E50', fontweight='bold')
        self.axes.set_ylabel("Điểm số trung bình", fontsize=10)
        self.axes.set_ylim(0, 10.5)
        self.axes.grid(axis='y', linestyle='--', alpha=0.5)
        
        for bar in bars:
            yval = bar.get_height()
            self.axes.text(bar.get_x() + bar.get_width()/2, yval + 0.2, str(yval), ha='center', va='bottom', fontsize=9)
            
        self.fig.tight_layout()
        self.draw()

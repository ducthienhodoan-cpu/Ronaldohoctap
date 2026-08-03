# Thu muc: giao_dien
# File: phoi_mau_qss.py
# Mo ta: Cung cap bang phoi mau QSS phong cach Roblox Dark Gaming Theme chu sang, ro net, tuong phan cao de doc

def lay_qss_giao_dien():
    """Trả về chuỗi QSS giao diện phong cách Roblox Dark Gaming chữ sáng, rõ nét, dễ nhìn."""
    return """
    /* Tong the ung dung phong cach Roblox Dark Theme voi chu sang ro net */
    QWidget {
        background-color: #191B1D;
        font-family: 'Be Vietnam Pro', 'Segoe UI', 'Roboto', 'Arial', sans-serif;
        font-size: 15px;
        color: #FFFFFF;
        font-weight: 500;
    }

    QLabel {
        color: #FFFFFF;
        font-size: 15px;
    }

    /* Thanh dieu huong Sidebar phong cach Roblox Navigation */
    QFrame#sidebarFrame {
        background-color: #232527;
        border-right: 2px solid #393B3D;
        border-top-left-radius: 12px;
        border-bottom-left-radius: 12px;
    }

    /* Nut dieu huong Sidebar khoi Roblox 3D */
    QPushButton.btn-nav {
        background-color: transparent;
        color: #FFFFFF;
        font-size: 15px;
        font-weight: bold;
        text-align: left;
        padding: 12px 18px;
        border: none;
        border-radius: 8px;
        margin: 3px 8px;
    }

    QPushButton.btn-nav:hover {
        background-color: #393B3D;
        color: #00E676;
    }

    QPushButton.btn-nav:checked {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0084FF, stop:1 #00A2FF);
        color: #FFFFFF;
        font-weight: bold;
        border-bottom: 3px solid #0052A3;
    }

    /* Header thanh thong tin Roblox */
    QFrame#headerFrame {
        background-color: #232527;
        border-bottom: 2px solid #393B3D;
        padding: 10px;
    }

    QLabel.text-header-title {
        font-family: 'Montserrat', 'Segoe UI', 'Roboto', sans-serif;
        font-size: 21px;
        font-weight: bold;
        color: #00A2FF;
    }

    QLabel.text-badge-info {
        background-color: #002B4D;
        color: #00E676;
        border: 2px solid #00E676;
        padding: 6px 16px;
        border-radius: 14px;
        font-weight: bold;
        font-size: 14px;
    }

    /* Roblox Game Tile Card container */
    QFrame.card-widget {
        background-color: #232527;
        border: 2px solid #393B3D;
        border-bottom: 4px solid #111214;
        border-radius: 12px;
        padding: 16px;
    }

    QFrame.card-widget:hover {
        border: 2px solid #00A2FF;
    }

    /* Tieu de Card Roblox chu sang */
    QLabel.card-title {
        font-family: 'Montserrat', 'Segoe UI', 'Roboto', sans-serif;
        font-size: 18px;
        font-weight: bold;
        color: #00E676;
        margin-bottom: 8px;
    }

    /* Nut lua chon dap an card Roblox 3D chu sang */
    QPushButton.card-option {
        background-color: #1E2022;
        border: 2px solid #393B3D;
        border-bottom: 3px solid #111214;
        border-radius: 10px;
        padding: 12px 18px;
        text-align: left;
        font-size: 15px;
        font-weight: bold;
        color: #FFFFFF;
    }

    QPushButton.card-option:hover {
        background-color: #2B2D31;
        border: 2px solid #00A2FF;
        color: #00E676;
    }

    QPushButton.card-option-selected {
        background-color: #002B4D;
        border: 2px solid #00A2FF;
        border-bottom: 3px solid #0052A3;
        color: #FFC107;
        font-weight: bold;
    }

    /* Nut bam hanh dong chinh (Roblox Green 3D Button) */
    QPushButton.btn-primary {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #00E676, stop:1 #00B259);
        color: #FFFFFF;
        font-size: 15px;
        font-weight: bold;
        padding: 10px 22px;
        border: none;
        border-bottom: 4px solid #007E3E;
        border-radius: 8px;
    }

    QPushButton.btn-primary:hover {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #10F484, stop:1 #00C864);
    }

    QPushButton.btn-primary:pressed {
        border-bottom: 0px;
        margin-top: 4px;
    }

    /* Nut bam phu 1 (Roblox Gold 3D Button) */
    QPushButton.btn-success {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFC107, stop:1 #FFA000);
        color: #191B1D;
        font-size: 15px;
        font-weight: bold;
        padding: 10px 22px;
        border: none;
        border-bottom: 4px solid #C77C00;
        border-radius: 8px;
    }

    QPushButton.btn-success:hover {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFD54F, stop:1 #FFB300);
    }

    QPushButton.btn-success:pressed {
        border-bottom: 0px;
        margin-top: 4px;
    }

    /* Nut bam phu 2 (Roblox Blue 3D Button) */
    QPushButton.btn-secondary {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #00A2FF, stop:1 #0077D9);
        color: #FFFFFF;
        font-size: 15px;
        font-weight: bold;
        padding: 10px 20px;
        border: none;
        border-bottom: 4px solid #0052A3;
        border-radius: 8px;
    }

    QPushButton.btn-secondary:hover {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #1AB0FF, stop:1 #0088F0);
    }

    QPushButton.btn-secondary:pressed {
        border-bottom: 0px;
        margin-top: 4px;
    }

    /* ComboBox, QLineEdit & QTextEdit phong cach Roblox Dark voi chu sang trang tinh */
    QComboBox, QLineEdit, QSpinBox, QTextEdit, QPlainTextEdit {
        background-color: #111214;
        border: 2px solid #393B3D;
        border-radius: 8px;
        padding: 8px 14px;
        color: #FFFFFF;
        font-size: 15px;
        font-weight: 500;
        selection-background-color: #0084FF;
        selection-color: #FFFFFF;
    }

    QComboBox:focus, QLineEdit:focus, QSpinBox:focus, QTextEdit:focus {
        border: 2px solid #00A2FF;
    }

    QComboBox QAbstractItemView {
        background-color: #232527;
        color: #FFFFFF;
        selection-background-color: #0084FF;
    }

    /* List Widget Roblox chu sang ro net */
    QListWidget {
        background-color: #111214;
        border: 2px solid #393B3D;
        border-radius: 10px;
        padding: 6px;
        color: #FFFFFF;
        font-size: 15px;
    }

    QListWidget::item {
        padding: 10px 14px;
        border-bottom: 1px solid #232527;
        border-radius: 6px;
        color: #FFFFFF;
    }

    QListWidget::item:hover {
        background-color: #2B2D31;
        color: #00E676;
    }

    QListWidget::item:selected {
        background-color: #0084FF;
        color: #FFFFFF;
        font-weight: bold;
    }

    /* Progress Bar phong cach Roblox */
    QProgressBar {
        background-color: #111214;
        border: 2px solid #393B3D;
        border-radius: 10px;
        text-align: center;
        color: #FFFFFF;
        font-weight: bold;
    }

    QProgressBar::chunk {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #00E676, stop:1 #00A2FF);
        border-radius: 8px;
    }

    /* ScrollBar Roblox */
    QScrollBar:vertical {
        background-color: #191B1D;
        width: 10px;
        margin: 0px;
    }

    QScrollBar::handle:vertical {
        background-color: #393B3D;
        border-radius: 5px;
        min-height: 20px;
    }

    QScrollBar::handle:vertical:hover {
        background-color: #00A2FF;
    }

    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        height: 0px;
    }
    """

# Thu muc: xu_ly_bao_ve
# File: ngan_sao_chep.py
# Mo ta: Xu ly ngan chan boi den, sao chep va cat chu tren trang web va cac khung hien thi van ban

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget

def tao_trang_web_chong_copy(duong_dan_youtube_iframe):
    """
    Tao ma HTML cho trang web voi day du cac lop bao ve chong sao chep chu:
    - CSS: vo hieu hoa chon chu (user-select: none)
    - HTML: chan cac su kien copy, cut, contextmenu, selectstart
    - JavaScript: bat va ngan chan phim tat Ctrl+C, Ctrl+X, Ctrl+A, mouse right-click
    """
    html_chong_copy = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Trang Web Nhac Thu Gian</title>
    <style>
        * {{
            -webkit-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
            user-select: none;
        }}
        body {{
            margin: 0;
            padding: 0;
            background-color: #0F172A;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            font-family: 'Segoe UI', sans-serif;
            overflow: hidden;
        }}
        .container {{
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        iframe {{
            width: 100%;
            height: 100%;
            border: none;
            border-radius: 8px;
            box-shadow: none;
        }}
    </style>
</head>
<body oncopy="return false;" oncut="return false;" onpaste="return false;" oncontextmenu="return false;" onselectstart="return false;">
    <div class="container">
        {duong_dan_youtube_iframe}
    </div>
    <script>
        // Ngan chan su kien sao chep va boi den van ban
        document.addEventListener('copy', function(e) {{
            e.preventDefault();
            return false;
        }});
        document.addEventListener('cut', function(e) {{
            e.preventDefault();
            return false;
        }});
        document.addEventListener('selectstart', function(e) {{
            e.preventDefault();
            return false;
        }});
        document.addEventListener('contextmenu', function(e) {{
            e.preventDefault();
            return false;
        }});
        document.addEventListener('keydown', function(e) {{
            if ((e.ctrlKey || e.metaKey) && (e.key === 'c' || e.key === 'C' || e.key === 'x' || e.key === 'X' || e.key === 'a' || e.key === 'A' || e.key === 'u' || e.key === 'U')) {{
                e.preventDefault();
                return false;
            }}
            if (e.key === 'F12') {{
                e.preventDefault();
                return false;
            }}
        }});
    </script>
</body>
</html>"""
    return html_chong_copy

def thiet_lap_ngan_copy_web_view(web_view):
    """Vo hieu hoa menu chuot phai Context Menu tren QWebEngineView."""
    if web_view:
        web_view.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)

def thiet_lap_ngan_copy_text_edit(text_widget):
    """
    Vo hieu hoa kha nang boi den va sao chep chu tren QWidget text.
    Ngan chan menu chuot phai va tuong tac chon van ban.
    """
    if text_widget:
        text_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        text_widget.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

# Thu muc: du_lieu_giao_duc
# File: co_so_du_lieu_cau_hoi.py
# Mo ta: Quan ly Co so du lieu SQLite luu tru 10.000 cau hoi da dang tat ca cac mon va khoi lop

import os
import sqlite3
import json
from du_lieu_giao_duc.sinh_10000_cau_hoi import sinh_toan_bo_10000_cau_hoi

DUONG_DAN_DB = os.path.join("du_lieu", "ngan_hang_10000_cau_hoi.db")

def ket_noi_db():
    """Ket noi hoac tao moi file co so du lieu SQLite voi toc do doc ghi turbo sieu toc."""
    thu_muc = os.path.dirname(DUONG_DAN_DB)
    if not os.path.exists(thu_muc):
        os.makedirs(thu_muc)
    conn = sqlite3.connect(DUONG_DAN_DB, timeout=10.0, check_same_thread=False)
    conn.execute("PRAGMA journal_mode = WAL;")
    conn.execute("PRAGMA synchronous = NORMAL;")
    conn.execute("PRAGMA cache_size = 10000;")
    conn.execute("PRAGMA temp_store = MEMORY;")
    conn.row_factory = sqlite3.Row
    return conn

def khoi_tao_co_so_du_lieu_10000_cau_hoi():
    """Khoi tao bang cau hoi va nap 10.000 cau hoi neu chua co du lieu."""
    conn = ket_noi_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cau_hoi (
            id INTEGER PRIMARY KEY,
            mon TEXT NOT NULL,
            lop TEXT NOT NULL,
            chu_de TEXT NOT NULL,
            do_kho TEXT NOT NULL,
            loai TEXT NOT NULL,
            cau_hoi TEXT NOT NULL,
            luat_dap_an TEXT NOT NULL,
            dap_an_dung TEXT NOT NULL,
            giai_thich TEXT NOT NULL
        )
    """)
    
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_mon_lop ON cau_hoi(mon, lop);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_do_kho ON cau_hoi(do_kho);")
    
    # Kiem tra so luong cau hoi hien tai
    cursor.execute("SELECT COUNT(*) FROM cau_hoi")
    count = cursor.fetchone()[0]
    
    if count < 10000:
        # Xoa va nap lai day du 10.000 cau hoi
        cursor.execute("DELETE FROM cau_hoi")
        ds_10000 = sinh_toan_bo_10000_cau_hoi()
        
        insert_data = []
        for q in ds_10000:
            insert_data.append((
                q["id"],
                q["mon"],
                q["lop"],
                q["chu_de"],
                q["do_kho"],
                q["loai"],
                q["cau_hoi"],
                json.dumps(q["luat_dap_an"], ensure_ascii=False),
                q["dap_an_dung"],
                q["giai_thich"]
            ))
            
        cursor.executemany("""
            INSERT INTO cau_hoi (id, mon, lop, chu_de, do_kho, loai, cau_hoi, luat_dap_an, dap_an_dung, giai_thich)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, insert_data)
        conn.commit()
        
    conn.close()

def truy_van_cau_hoi(mon=None, lop=None, chu_de=None, so_cau=10, do_kho=None):
    """Truy van danh sach cau hoi tu database 10.000 cau hoi theo bo loc."""
    khoi_tao_co_so_du_lieu_10000_cau_hoi()
    conn = ket_noi_db()
    cursor = conn.cursor()
    
    query = "SELECT * FROM cau_hoi WHERE 1=1"
    params = []
    
    if mon and mon != "Tất cả":
        query += " AND mon = ?"
        params.append(mon)
        
    if lop and lop != "Tất cả":
        query += " AND lop = ?"
        params.append(lop)
        
    if chu_de and chu_de != "Tất cả" and chu_de != "Chủ đề bài học":
        query += " AND chu_de LIKE ?"
        params.append(f"%{chu_de}%")
        
    if do_kho and do_kho != "Tất cả":
        query += " AND do_kho = ?"
        params.append(do_kho)
        
    query += " ORDER BY RANDOM() LIMIT ?"
    params.append(so_cau)
    
    cursor.execute(query, params)
    rows = cursor.fetchall()
    
    danh_sach_ket_qua = []
    for r in rows:
        try:
            opts = json.loads(r["luat_dap_an"])
        except Exception:
            opts = ["A", "B", "C", "D"]
            
        danh_sach_ket_qua.append({
            "id": r["id"],
            "mon": r["mon"],
            "lop": r["lop"],
            "chu_de": r["chu_de"],
            "do_kho": r["do_kho"],
            "loai": r["loai"],
            "cau_hoi": r["cau_hoi"],
            "luat_dap_an": opts,
            "dap_an_dung": r["dap_an_dung"],
            "giai_thich": r["giai_thich"],
            "nguon": "Ngân Hàng 10.000 Câu Hỏi SQLite Database"
        })
        
    conn.close()
    return danh_sach_ket_qua

def lay_thong_ke_database():
    """Lay tong quan thong ke 10.000 cau hoi phan loai theo mon va lop."""
    khoi_tao_co_so_du_lieu_10000_cau_hoi()
    conn = ket_noi_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM cau_hoi")
    tong_cau = cursor.fetchone()[0]
    
    cursor.execute("SELECT mon, COUNT(*) as sl FROM cau_hoi GROUP BY mon ORDER BY sl DESC")
    theo_mon = {r["mon"]: r["sl"] for r in cursor.fetchall()}
    
    cursor.execute("SELECT lop, COUNT(*) as sl FROM cau_hoi GROUP BY lop")
    theo_lop = {r["lop"]: r["sl"] for r in cursor.fetchall()}
    
    cursor.execute("SELECT do_kho, COUNT(*) as sl FROM cau_hoi GROUP BY do_kho")
    theo_do_kho = {r["do_kho"]: r["sl"] for r in cursor.fetchall()}
    
    conn.close()
    
    return {
        "tong_so_cau": tong_cau,
        "theo_mon": theo_mon,
        "theo_lop": theo_lop,
        "theo_do_kho": theo_do_kho
    }

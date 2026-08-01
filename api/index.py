# Thu muc: api
# File: index.py
# Mo ta: Entry point Python Serverless Functions tich hop 100% tat ca 16 man hinh va tinh nang cua ban goc Desktop sang Tieng Viet co dau

from flask import Flask, jsonify, request
import sys
import os

# Them thu muc goc vao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from du_lieu.kho_noi_dung_hoc import lay_danh_sach_lop, lay_danh_sach_mon_hoc, lay_chu_de_theo_lop_va_mon
from du_lieu.noi_dung_chi_tiet import lay_noi_dung_bai_hoc_chi_tiet
from du_lieu.ngan_hang_cau_hoi import lay_cau_hoi_luyen_tap
from du_lieu_giao_duc.kho_cong_thuc import lay_danh_sach_cong_thuc
from du_lieu_giao_duc.ngan_hang_giai_toan import lay_danh_sach_cau_hoi_toan_giai_chi_tiet
from xu_ly_ielts.du_lieu_ielts import (
    lay_danh_sach_tu_vung_ielts, lay_danh_sach_ngu_phap_va_thi,
    lay_bai_doc_ielts_reading, lay_bai_nghe_ielts_listening,
    lay_de_thi_ielts_tong_hop
)
from xu_ly_gemini.dong_co_gemini import tao_de_thi_gemini_api
from xu_ly_kiem_tra.bo_cham_diem import cham_bai_lam
from xu_ly_kiem_tra.cham_bai_anh_ai import phan_tich_anh_bai_lam
from xu_ly_hoc_tap.he_thong_thuong import lay_thong_tin_thuong, cong_phan_thuong
from xu_ly_hoc_tap.quan_ly_nguoi_dung import lay_ten_nguoi_dung, cap_nhat_ten_nguoi_dung
from xu_ly_hoc_tap.quan_ly_tien_do import lay_du_lieu_tien_do, cap_nhat_streak, kiem_tra_mo_khoa_bai_hoc
from xu_ly_hoc_tap.quan_ly_chung_nhan import lay_danh_sach_chung_nhan, tao_chung_nhan_moi
from xu_ly_so_tay.quan_ly_so_loi_sai import doc_so_loi_sai, xoa_cau_loi_sai, them_cau_loi_sai
from xu_ly_so_tay.quan_ly_ke_hoach_hoc import doc_ke_hoach_hoc, ghi_ke_hoach_hoc, cap_nhat_trang_thai_muc_tieu
from xu_ly_tro_choi.quan_ly_world_cup import lay_danh_sach_doi_tuyen, lay_vong_dau_world_cup, sinh_tran_dau_world_cup
from xu_ly_tro_choi.quan_ly_champions_league import lay_danh_sach_clb_champions_league, lay_vong_dau_champions_league, sinh_tran_dau_champions_league
from xu_ly_tro_choi.quan_ly_dua_xe import khoi_tao_duong_dua_xe, sinh_vat_the_duong_dua
from xu_ly_tro_choi.minigame_giua_gio import tao_danh_sach_the_lat_tri_nho, quay_vong_quay_may_man, xu_ly_sut_phat_penalty
from xu_ly_cai_dat.quan_ly_diem_mong_muon import lay_cai_dat_diem_mong_muon, luu_cai_dat_diem_mong_muon
# Thong ke module ready

app = Flask(__name__)

# Function 1: Health & System Metadata
@app.route('/', methods=['GET'])
@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        "status": "ok",
        "app_name": "Sieu Club Hoc Tap & Tap Thi IELTS All-In-One",
        "version": "5.0.0",
        "total_screens": 16,
        "platform": "Vercel Hobby Free Limits Compliant"
    })

# Function 2: Questions Provider (Classes 1-12, Topics, Lessons, IELTS & Formulas)
@app.route('/api/questions', methods=['GET'])
def get_questions():
    skill = request.args.get('skill', 'tu_vung')
    band = request.args.get('band', 'Band 5.5 - 6.0')
    ten_lop = request.args.get('lop', 'Lớp 6')
    ten_mon = request.args.get('mon', 'Toán')
    ten_bai = request.args.get('bai', 'Chủ đề 1')

    if skill == 'tu_vung':
        data = lay_danh_sach_tu_vung_ielts(band)
    elif skill == 'ngu_phap':
        data = lay_danh_sach_ngu_phap_va_thi(band)
    elif skill == 'doc':
        data = lay_bai_doc_ielts_reading(band)
    elif skill == 'nghe':
        data = lay_bai_nghe_ielts_listening(band)
    elif skill == 'ielts_tong_hop':
        data = lay_de_thi_ielts_tong_hop(band)
    elif skill == 'formula':
        data = lay_danh_sach_cong_thuc(ten_lop, ten_mon)
    elif skill == 'math_step_by_step':
        data = lay_danh_sach_cau_hoi_toan_giai_chi_tiet(ten_lop)
    elif skill == 'lesson_detail':
        data = lay_noi_dung_bai_hoc_chi_tiet(ten_lop, ten_mon, ten_bai)
        return jsonify({"status": "success", "detail": data})
    elif skill == 'topics':
        data = lay_chu_de_theo_lop_va_mon(ten_lop, ten_mon)
        return jsonify({"status": "success", "topics": data})
    else:
        data = lay_cau_hoi_luyen_tap(ten_mon, ten_lop, ten_bai)

    return jsonify({
        "status": "success",
        "skill": skill,
        "band": band,
        "lop": ten_lop,
        "mon": ten_mon,
        "total": len(data),
        "questions": data
    })

# Function 3: Automated Grading, Mistake Auto-Logger & Certificates
@app.route('/api/submit', methods=['POST'])
def submit_exam():
    req = request.get_json() or {}
    questions = req.get('questions', [])
    answers = req.get('answers', {})
    exam_title = req.get('title', 'Bài Luyện Tập Tổng Hợp')

    formatted_answers = {int(k): v for k, v in answers.items()}
    result = cham_bai_lam(questions, formatted_answers)
    xp_nhan, coin_nhan = cong_phan_thuong(result["diem_so"], result["so_cau_dung"])

    # Tự động ghi nhận các câu làm sai vào Sổ Lỗi Sai
    for idx, q in enumerate(questions):
        user_ans = formatted_answers.get(idx)
        if user_ans and user_ans != q.get("dap_an_dung"):
            them_cau_loi_sai(q.get("cau_hoi", ""), user_ans, q.get("dap_an_dung", ""), q.get("giai_thich", ""))

    # Cấp Giấy chứng nhận nếu điểm >= 8.0
    certificate = None
    if result["diem_so"] >= 8.0:
        certificate = tao_chung_nhan_moi(exam_title, result["diem_so"])

    # Cập nhật chuỗi Streak
    cap_nhat_streak()

    return jsonify({
        "status": "success",
        "score": result["diem_so"],
        "percentage": result["phan_tram"],
        "correct": result["so_cau_dung"],
        "total": result["tong_cau"],
        "rating": result["xep_loai"],
        "xp_reward": xp_nhan,
        "coin_reward": coin_nhan,
        "certificate": certificate
    })

# Function 4: Gemini AI Generation & OCR Essay Evaluation
@app.route('/api/ai-generate', methods=['POST'])
def ai_engine():
    req = request.get_json() or {}
    mode = req.get('mode', 'quiz')

    if mode == 'essay_grading':
        bai_lam_text = req.get('bai_lam', '')
        res_grading = phan_tich_anh_bai_lam(bai_lam_text)
        return jsonify({"status": "success", "grading": res_grading})
    else:
        ten_lop = req.get('lop', 'Lớp 6')
        ten_mon = req.get('mon', 'Toán')
        muc_do = req.get('muc_do', 'Trung bình')
        chu_de = req.get('chu_de', 'Kiến thức tổng hợp')
        so_cau = req.get('so_cau', 5)
        questions = tao_de_thi_gemini_api(ten_lop, ten_mon, muc_do, chu_de, so_cau)
        return jsonify({"status": "success", "total": len(questions), "questions": questions})

# Function 5: All Sports & Racing Tournaments & Minigames
@app.route('/api/games', methods=['GET', 'POST'])
def games_engine():
    if request.method == 'POST':
        req = request.get_json() or {}
        game_type = req.get('type', 'wheel')
        if game_type == 'wheel':
            res = quay_vong_quay_may_man()
            return jsonify({"status": "success", "reward": res})
        elif game_type == 'penalty':
            huong = req.get('direction', 'Giữa')
            res = xu_ly_sut_phat_penalty(huong)
            return jsonify({"status": "success", "result": res})
        elif game_type == 'memory_cards':
            cards = tao_danh_sach_the_lat_tri_nho()
            return jsonify({"status": "success", "cards": cards})
        elif game_type == 'world_cup':
            vong_idx = req.get('vong', 0)
            match_res = sinh_tran_dau_world_cup(vong_idx, req.get('lop', 'Lớp 6'), req.get('mon', 'Toán'), req.get('doi_user', 'Việt Nam'))
            return jsonify({"status": "success", "match": match_res})
        elif game_type == 'champions_league':
            vong_idx = req.get('vong', 0)
            match_res = sinh_tran_dau_champions_league(vong_idx, req.get('lop', 'Lớp 6'), req.get('mon', 'Toán'), 'Chủ đề 1', req.get('clb_user', 'Real Madrid'))
            return jsonify({"status": "success", "match": match_res})
        elif game_type == 'racing_obstacle':
            obstacle = sinh_vat_the_duong_dua(req.get('mon', 'Toán'), req.get('lop', 'Lớp 6'), req.get('muc_do', 'Bình thường'))
            return jsonify({"status": "success", "obstacle": obstacle})

    return jsonify({
        "status": "success",
        "world_cup": {
            "teams": lay_danh_sach_doi_tuyen(),
            "rounds": lay_vong_dau_world_cup("Việt Nam")
        },
        "champions_league": {
            "clubs": lay_danh_sach_clb_champions_league(),
            "rounds": lay_vong_dau_champions_league("Real Madrid")
        },
        "racing": khoi_tao_duong_dua_xe()
    })

# Function 6: User Profile, Settings, Roblox XP & Analytics
@app.route('/api/settings', methods=['GET', 'POST'])
def handle_settings():
    if request.method == 'POST':
        req = request.get_json() or {}
        if req.get('ten_moi'):
            cap_nhat_ten_nguoi_dung(req['ten_moi'])
        if req.get('diem_mong_muon'):
            luu_cai_dat_diem_mong_muon(req)
        return jsonify({"status": "success", "message": "Đã cập nhật hồ sơ và cài đặt thành công!"})
    else:
        settings = lay_cai_dat_diem_mong_muon()
        user_name = lay_ten_nguoi_dung()
        rewards = lay_thong_tin_thuong()
        progress = lay_du_lieu_tien_do()
        certs = lay_danh_sach_chung_nhan()
        charts = {"ngay": ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ Nhật"], "diem": [8.5, 9.0, 7.5, 8.8, 9.5, 10.0, 9.2]}
        return jsonify({
            "status": "success",
            "user_name": user_name,
            "settings": settings,
            "rewards": rewards,
            "progress": progress,
            "certificates": certs,
            "analytics": charts
        })

# Function 7: Notebooks (Mistake Notebook & Study Plan)
@app.route('/api/notebook', methods=['GET', 'POST'])
def notebook_engine():
    if request.method == 'POST':
        req = request.get_json() or {}
        action = req.get('action', 'delete_mistake')
        if action == 'delete_mistake':
            xoa_cau_loi_sai(req.get('cau_hoi', ''))
            return jsonify({"status": "success", "message": "Đã xóa câu hỏi khỏi Sổ Lỗi Sai!"})
        elif action == 'update_target':
            target_id = req.get('target_id')
            status = req.get('status', False)
            res_plan = cap_nhat_trang_thai_muc_tieu(target_id, status)
            return jsonify({"status": "success", "plan": res_plan})

    so_sai = doc_so_loi_sai()
    plan = doc_ke_hoach_hoc()
    return jsonify({
        "status": "success",
        "total_mistakes": len(so_sai),
        "mistakes": so_sai,
        "study_plan": plan
    })

if __name__ == '__main__':
    app.run(debug=True)

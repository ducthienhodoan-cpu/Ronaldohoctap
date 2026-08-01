# Thu muc: api
# File: index.py
# Mo ta: Entry point Python Serverless Functions tong hop 7 endpoints cho Vercel Free Plan limits sang Tieng Viet co dau

from flask import Flask, jsonify, request
import sys
import os

# Them thu muc goc vao sys.path de import cac module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from xu_ly_ielts.du_lieu_ielts import (
    lay_danh_sach_tu_vung_ielts, lay_danh_sach_ngu_phap_va_thi,
    lay_bai_doc_ielts_reading, lay_bai_nghe_ielts_listening,
    lay_de_thi_ielts_tong_hop
)
from xu_ly_kiem_tra.bo_cham_diem import cham_bai_lam
from xu_ly_cai_dat.quan_ly_diem_mong_muon import lay_cai_dat_diem_mong_muon, luu_cai_dat_diem_mong_muon
from xu_ly_gemini.dong_co_gemini import tao_de_thi_gemini_api
from xu_ly_tro_choi.minigame_giua_gio import quay_vong_quay_may_man, xu_ly_sut_phat_penalty
from xu_ly_so_tay.quan_ly_so_loi_sai import doc_so_loi_sai, xoa_cau_loi_sai

app = Flask(__name__)

# Function 1: Health & System Status
@app.route('/', methods=['GET'])
@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        "status": "ok",
        "app_name": "Sieu Club Hoc Tap & Tap Thi IELTS",
        "version": "5.0.0",
        "serverless_functions_count": 7,
        "platform": "Vercel Hobby Free Limits Compliant"
    })

# Function 2: Questions Provider (IELTS, Lop 1-12, 5 Chu de, Kiem tra)
@app.route('/api/questions', methods=['GET'])
def get_questions():
    skill = request.args.get('skill', 'tu_vung')
    band = request.args.get('band', 'Band 5.5 - 6.0')
    ten_lop = request.args.get('lop', 'Lớp 6')
    ten_mon = request.args.get('mon', 'Toán')

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
    else:
        # Defaults to sample questions for practice
        data = lay_de_thi_ielts_tong_hop(band)

    return jsonify({
        "status": "success",
        "skill": skill,
        "band": band,
        "lop": ten_lop,
        "mon": ten_mon,
        "total": len(data),
        "questions": data
    })

# Function 3: Grading & XP Calculation
@app.route('/api/submit', methods=['POST'])
def submit_exam():
    req = request.get_json() or {}
    questions = req.get('questions', [])
    answers = req.get('answers', {})

    formatted_answers = {int(k): v for k, v in answers.items()}
    result = cham_bai_lam(questions, formatted_answers)

    return jsonify({
        "status": "success",
        "score": result["diem_so"],
        "percentage": result["phan_tram"],
        "correct": result["so_cau_dung"],
        "total": result["tong_cau"],
        "rating": result["xep_loai"],
        "xp_reward": result["so_cau_dung"] * 10
    })

# Function 4: Gemini AI Exercise Generator
@app.route('/api/ai-generate', methods=['POST'])
def ai_generate():
    req = request.get_json() or {}
    ten_lop = req.get('lop', 'Lớp 6')
    ten_mon = req.get('mon', 'Toán')
    muc_do = req.get('muc_do', 'Trung bình')
    chu_de = req.get('chu_de', 'Kiến thức tổng hợp')
    so_cau = req.get('so_cau', 5)

    questions = tao_de_thi_gemini_api(ten_lop, ten_mon, muc_do, chu_de, so_cau)
    return jsonify({
        "status": "success",
        "generator": "Gemini AI API Engine",
        "total": len(questions),
        "questions": questions
    })

# Function 5: Games Engine (World Cup, Champions League, Racing, Minigames)
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

    return jsonify({
        "status": "success",
        "available_games": ["World Cup", "Champions League", "Racing Grand Prix", "Lucky Wheel", "Penalty Blitz", "Memory Flip"]
    })

# Function 6: Target Settings & Avatar Profile
@app.route('/api/settings', methods=['GET', 'POST'])
def handle_settings():
    if request.method == 'POST':
        req = request.get_json() or {}
        luu_cai_dat_diem_mong_muon(req)
        return jsonify({"status": "success", "message": "Đã lưu cài đặt điểm mong muốn!"})
    else:
        settings = lay_cai_dat_diem_mong_muon()
        return jsonify({"status": "success", "settings": settings})

# Function 7: Notebooks (Mistake Notebook & Formula Notebook)
@app.route('/api/notebook', methods=['GET', 'POST'])
def notebook_engine():
    if request.method == 'POST':
        req = request.get_json() or {}
        cau_text = req.get('cau_hoi', '')
        if cau_text:
            xoa_cau_loi_sai(cau_text)
            return jsonify({"status": "success", "message": "Đã xóa câu hỏi khỏi Sổ Lỗi Sai!"})
    
    so_sai = doc_so_loi_sai()
    return jsonify({
        "status": "success",
        "total_mistakes": len(so_sai),
        "mistakes": so_sai
    })

if __name__ == '__main__':
    app.run(debug=True)

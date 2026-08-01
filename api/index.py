# Thu muc: api
# File: index.py
# Mo ta: Entry point Python Serverless Function cho Vercel Cloud Deployment ho tro API Questions, Submit & Settings sang Tieng Viet co dau

from flask import Flask, jsonify, request
import sys
import os

# Them thu muc goc vao sys.path de import cac xu ly du lieu
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from xu_ly_ielts.du_lieu_ielts import (
    lay_danh_sach_tu_vung_ielts, lay_danh_sach_ngu_phap_va_thi,
    lay_bai_doc_ielts_reading, lay_bai_nghe_ielts_listening,
    lay_de_thi_ielts_tong_hop
)
from xu_ly_kiem_tra.bo_cham_diem import cham_bai_lam
from xu_ly_cai_dat.quan_ly_diem_mong_muon import lay_cai_dat_diem_mong_muon, luu_cai_dat_diem_mong_muon

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "success",
        "app_name": "Sieu Club Hoc Tap & Tap Thi IELTS",
        "description": "Nen tang Hoc tap, Kiem tra tu dong, Gemini AI Sinh de va Tap thi IELTS",
        "version": "5.0.0",
        "platform": "Vercel Cloud Deployment"
    })

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        "status": "ok",
        "message": "He thong Sieu Club Hoc Tap Vercel API hoat dong binh thuong!"
    })

@app.route('/api/questions', methods=['GET'])
def get_questions():
    skill = request.args.get('skill', 'tu_vung')
    band = request.args.get('band', 'Band 5.5 - 6.0')
    
    if skill == 'tu_vung':
        data = lay_danh_sach_tu_vung_ielts(band)
    elif skill == 'ngu_phap':
        data = lay_danh_sach_ngu_phap_va_thi(band)
    elif skill == 'doc':
        data = lay_bai_doc_ielts_reading(band)
    elif skill == 'nghe':
        data = lay_bai_nghe_ielts_listening(band)
    else:
        data = lay_de_thi_ielts_tong_hop(band)
        
    return jsonify({"status": "success", "skill": skill, "band": band, "total": len(data), "questions": data})

@app.route('/api/submit', methods=['POST'])
def submit_exam():
    req = request.get_json() or {}
    questions = req.get('questions', [])
    answers = req.get('answers', {})
    
    # Format answers dict keys to integers
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

@app.route('/api/settings', methods=['GET', 'POST'])
def handle_settings():
    if request.method == 'POST':
        req = request.get_json() or {}
        luu_cai_dat_diem_mong_muon(req)
        return jsonify({"status": "success", "message": "Da luu cai dat diem mong muon!"})
    else:
        settings = lay_cai_dat_diem_mong_muon()
        return jsonify({"status": "success", "settings": settings})

if __name__ == '__main__':
    app.run(debug=True)

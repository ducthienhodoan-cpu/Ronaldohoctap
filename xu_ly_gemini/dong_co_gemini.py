# Thu muc: xu_ly_gemini
# File: dong_co_gemini.py
# Mo ta: Dong co sinh de kiem tra bang Gemini API Key va bo sinh de du phong sang Tieng Viet co dau

import json
import ssl
import urllib.request
import urllib.parse
from xu_ly_gemini.quan_ly_api_key import lay_gemini_api_key, lay_model_gemini
from xu_ly_mang.kiem_tra_ket_noi import kiem_tra_ket_noi_internet

# Danh sach cac phien ban mo hinh Gemini hoat dong tot nhat
DANH_SACH_MODEL_GEMINI = [
    "gemini-3.6-flash",
    "gemini-3.5-flash",
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-1.5-flash",
    "gemini-1.5-pro",
    "gemini-flash-latest"
]

def tao_de_thi_gemini_fallback(ten_lop, ten_mon, muc_do="Trung bình", ten_chuong="Kiến thức tổng hợp", so_cau=5):
    """Tạo danh sách câu hỏi dự phòng chất lượng cao khi Gemini API chưa có Key hoặc bị giới hạn mạng."""
    from du_lieu.ngan_hang_cau_hoi import lay_cau_hoi_luyen_tap
    raw_qs = lay_cau_hoi_luyen_tap(ten_mon, ten_lop, ten_chuong, so_cau)
    danh_sach = []
    
    for idx, q in enumerate(raw_qs):
        dap_an_list = q.get("dap_an") or q.get("luat_dap_an") or ["Phương án A", "Phương án B", "Phương án C", "Phương án D"]
        if len(dap_an_list) < 4:
            dap_an_list = (dap_an_list + ["Phương án bổ sung 1", "Phương án bổ sung 2", "Phương án bổ sung 3"])[:4]
        
        dap_an_dung = q.get("dap_an_dung", dap_an_list[0])
        danh_sach.append({
            "id": idx + 1,
            "cau_so": idx + 1,
            "cau_hoi": f"Câu {idx + 1} [{ten_lop} - {ten_mon} - {muc_do}]: " + q.get("cau_hoi", f"Kiến thức trọng tâm môn {ten_mon}"),
            "dap_an": dap_an_list,
            "dap_an_dung": dap_an_dung,
            "giai_thich": q.get("giai_thich", f"Đáp án đúng chính xác là: {dap_an_dung}"),
            "chuong": ten_chuong,
            "muc_do": muc_do,
            "mon_hoc": ten_mon,
            "nguon": "Động Cơ AI Ngoại Tuyến"
        })
    return danh_sach

def tao_de_thi_gemini_api(ten_lop="Lớp 7", ten_mon="Toán", ten_chuong="Biểu thức đại số", so_cau=5, muc_do="Trung bình", api_key=""):
    """Tạo danh sách câu hỏi trắc nghiệm tự động từ Gemini API hoặc Động cơ dự phòng ngoại tuyến."""
    # Neu ngat ket noi internet, chuyen ngay sang Dong co Ngoai tuyen khong lam treo thoi gian
    if not kiem_tra_ket_noi_internet():
        return tao_de_thi_gemini_fallback(ten_lop, ten_mon, muc_do, ten_chuong, so_cau)

    key_su_dung = api_key.strip() if api_key else lay_gemini_api_key()
    
    if key_su_dung:
        prompt = f"""Hãy đóng vai giáo viên chuyên nghiệp tạo {so_cau} câu hỏi trắc nghiệm bằng tiếng Việt có dấu.
Thông tin bài tập:
- Lớp học: {ten_lop}
- Môn học: {ten_mon}
- Chủ đề: {ten_chuong}
- Mức độ khó: {muc_do}

Yêu cầu định dạng đầu ra:
Trả về DUY NHẤT một chuỗi JSON array nguyên bản, không dùng block code markdown, không thêm bất kỳ câu giải thích nào trước hoặc sau JSON.
Cấu trúc mỗi object trong array như sau:
[
  {{
    "cau_hoi": "Nội dung câu hỏi chi tiết rõ ràng?",
    "dap_an": ["Đáp án A", "Đáp án B", "Đáp án C", "Đáp án D"],
    "dap_an_dung": "Đáp án A",
    "giai_thich": "Lời giải chi tiết ngắn gọn dễ hiểu cho học sinh."
  }}
]
Mỗi câu hỏi phải có đúng 4 phương án đáp án, và 'dap_an_dung' phải trùng khớp chính xác với 1 trong 4 phương án đó.
"""

        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }

        # Cau hinh SSL cho Windows
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        json_data = json.dumps(payload).encode("utf-8")

        # Tạo danh sách model thử nghiệm ưu tiên model người dùng chọn
        user_model = lay_model_gemini()
        models_to_try = [user_model] + [m for m in DANH_SACH_MODEL_GEMINI if m != user_model]

        for model in models_to_try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key_su_dung}"
            try:
                req = urllib.request.Request(
                    url, 
                    data=json_data, 
                    headers={"Content-Type": "application/json"},
                    method="POST"
                )

                with urllib.request.urlopen(req, context=ctx, timeout=12) as response:
                    res_body = response.read().decode("utf-8")
                    res_json = json.loads(res_body)

                    candidates = res_json.get("candidates", [])
                    if not candidates:
                        continue

                    text_response = candidates[0]["content"]["parts"][0]["text"].strip()
                    
                    # Xử lý làm sạch chuỗi JSON nếu Gemini trả về mã Markdown ```json ... ```
                    if text_response.startswith("```"):
                        text_response = text_response.replace("```json", "").replace("```", "").strip()

                    danh_sach_raw = json.loads(text_response)
                    
                    danh_sach_cau_hoi = []
                    for idx, item in enumerate(danh_sach_raw):
                        cau_hoi_text = item.get("cau_hoi", f"Câu hỏi {idx+1}")
                        dap_an_list = item.get("dap_an", ["A", "B", "C", "D"])
                        dap_an_dung = item.get("dap_an_dung", dap_an_list[0] if dap_an_list else "A")
                        giai_thich = item.get("giai_thich", "Lời giải chi tiết từ Gemini AI.")

                        danh_sach_cau_hoi.append({
                            "id": idx + 1,
                            "cau_so": idx + 1,
                            "cau_hoi": f"Câu {idx + 1} [{ten_lop} - {ten_mon} - {muc_do}]: {cau_hoi_text}",
                            "dap_an": dap_an_list,
                            "dap_an_dung": dap_an_dung,
                            "giai_thich": giai_thich,
                            "chuong": ten_chuong,
                            "muc_do": muc_do,
                            "mon_hoc": ten_mon,
                            "nguon": f"Gemini AI ({model})"
                        })

                    if danh_sach_cau_hoi:
                        return danh_sach_cau_hoi

            except Exception:
                continue

    # Neu nhap Key rong hoac Gemini API bi loi mang, su dung Dong Co Du Phong sinh de dam bao tao de 100% thanh cong
    return tao_de_thi_gemini_fallback(ten_lop, ten_mon, muc_do, ten_chuong, so_cau)

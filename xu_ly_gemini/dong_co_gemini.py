# Thu muc: xu_ly_gemini
# File: dong_co_gemini.py
# Mo ta: Dong co sinh de kiem tra bang Gemini API Key theo Lop, Mon, Chu de va Do kho sang Tieng Viet co dau

import json
import ssl
import urllib.request
import urllib.parse
from xu_ly_gemini.quan_ly_api_key import lay_gemini_api_key

# Danh sach cac phien ban mo hinh Gemini hoat dong tot nhat
DANH_SACH_MODEL_GEMINI = [
    "gemini-3.6-flash",
    "gemini-3.5-flash",
    "gemini-flash-latest",
    "gemini-flash-lite-latest",
    "gemini-2.0-flash-lite"
]

def tao_de_thi_gemini_api(ten_lop="Lớp 7", ten_mon="Toán", ten_chuong="Biểu thức đại số", so_cau=10, muc_do="Trung bình", api_key=""):
    """Tạo danh sách câu hỏi trắc nghiệm tự động từ Gemini API."""
    key_su_dung = api_key.strip() if api_key else lay_gemini_api_key()
    if not key_su_dung:
        return []

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

    # Thu lan luot cac model gemini cho den khi thanh cong
    for model in DANH_SACH_MODEL_GEMINI:
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

    return []

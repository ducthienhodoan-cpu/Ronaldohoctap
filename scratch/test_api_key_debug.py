import urllib.request
import urllib.parse
import json
import ssl

api_key = "AIzaSyD0HG29MxPEv2XAjIEPnEhkQqHwmOm_Ujk"

# Thử các model endpoint khác nhau
models = [
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-1.5-flash",
    "gemini-1.5-pro",
    "gemini-pro"
]

prompt = "Hãy tạo 1 câu hỏi trắc nghiệm tiếng Việt về Toán lớp 6. Trả về JSON."

for model in models:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    
    print(f"\n--- Testing model: {model} ---")
    try:
        json_data = json.dumps(payload).encode("utf-8")
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        
        req = urllib.request.Request(
            url, 
            data=json_data, 
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
            res = response.read().decode("utf-8")
            print(f"SUCCESS with {model}!")
            print(res[:200])
            break
    except urllib.error.HTTPError as e:
        print(f"HTTPError with {model}: {e.code} {e.reason}")
        print(e.read().decode("utf-8", errors="ignore")[:300])
    except Exception as e:
        print(f"Error with {model}: {e}")

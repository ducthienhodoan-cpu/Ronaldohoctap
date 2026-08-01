import urllib.request
import json
import ssl

api_key = "AIzaSyD0HG29MxPEv2XAjIEPnEhkQqHwmOm_Ujk"

test_models = [
    "gemini-2.0-flash-lite",
    "gemini-2.5-flash-lite",
    "gemini-flash-latest",
    "gemini-flash-lite-latest",
    "gemini-3.6-flash",
    "gemini-3.5-flash",
    "gemini-2.0-flash-001"
]

prompt = "Hãy trả về một JSON array gồm 1 câu hỏi trắc nghiệm Toán 6 dạng [{\"cau_hoi\":\"1+1=?\", \"dap_an\":[\"1\",\"2\",\"3\",\"4\"], \"dap_an_dung\":\"2\", \"giai_thich\":\"1+1=2\"}]"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for model in test_models:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    
    print(f"\n--- Testing model: {model} ---")
    try:
        json_data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            url, 
            data=json_data, 
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
            res_body = response.read().decode("utf-8")
            res_json = json.loads(res_body)
            print(f"SUCCESS with {model}!")
            text = res_json["candidates"][0]["content"]["parts"][0]["text"]
            print("Response:", text[:200])
            break
    except urllib.error.HTTPError as e:
        print(f"HTTPError with {model}: {e.code}")
        print(e.read().decode("utf-8", errors="ignore")[:250])
    except Exception as e:
        print(f"Error with {model}: {e}")

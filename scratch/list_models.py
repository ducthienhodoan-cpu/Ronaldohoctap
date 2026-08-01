import urllib.request
import json
import ssl

api_key = "AIzaSyD0HG29MxPEv2XAjIEPnEhkQqHwmOm_Ujk"
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    req = urllib.request.Request(url, method="GET")
    with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
        res = json.loads(response.read().decode("utf-8"))
        print("Available models:")
        for m in res.get("models", []):
            name = m.get("name")
            supported = m.get("supportedGenerationMethods", [])
            if "generateContent" in supported:
                print(f" - {name}")
except Exception as e:
    print(f"Error fetching models: {e}")

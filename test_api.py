import requests
import time

backend_url = "http://13.201.187.70"
target = "google.com"

endpoints = [
    ("/api/portscan", {"target": target, "start": 1, "end": 100}),
    ("/api/subdomain", {"domain": target}),
    ("/api/whois", {"target": target}),
    ("/api/dirbrute", {"url": f"http://{target}"})
]

for endpoint, payload in endpoints:
    url = f"{backend_url}{endpoint}"
    print(f"Testing {url}...")
    start_time = time.time()
    try:
        response = requests.post(url, json=payload, timeout=30)
        duration = time.time() - start_time
        print(f"Status: {response.status_code}, Time: {duration:.2f}s")
        if response.status_code != 200:
            print(f"Response: {response.text[:200]}")
    except Exception as e:
        print(f"Error: {e}")
    print("-" * 20)

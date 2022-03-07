import requests
from pyfiglet import Figlet

def get_info_by_ip(ip = "127.0.0.1"):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        save = {
            '[IP]': response.get('query'),
            '[INTERNET PROVIDER]': response.get('isp'),
            '[ORG]': response.get("org"),
            '[COUNTRY]': response.get("country"),
            '[REGION]': response.get("region"),
            "[CITY]": response.get("city"),
            "[LAT]": response.get("lat"),
            "[LON]": response.get("lon"),
        }

        for k, v in save.items():
            print(f"{k}:{v}")

    except requests.exceptions.ConnectionError:
        print("[!] Пожалуйста проверте ваше подключение к интернету...")

text = Figlet(font="slant", width=150)
print(text.renderText("IP SCANER BY GEF3DX"))
ip = input("Введите пожалуйста IP или нажмите [ENTER] чтоб узнать иформацию о своем IP\n")

get_info_by_ip(ip)

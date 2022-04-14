import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.netflix.com/browse")
if r.statude_code == 200:
    print(f"請求成功:{r.statude_code}")

else:
    print(f"請求失敗:{r.statude_code}")
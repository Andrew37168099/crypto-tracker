
# static.py - 抓取 CoinDesk 新聞
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.coindesk.com/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.select("a.card-title")
news = []

for article in articles:
    title = article.text.strip()
    link = "https://www.coindesk.com" + article.get("href")
    news.append({"title": title, "url": link})

df = pd.DataFrame(news)
df.to_csv("static.csv", index=False, encoding="utf-8-sig")

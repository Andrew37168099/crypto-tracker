
# api.py - 查詢加密貨幣即時價格
import requests
import pandas as pd

coin_ids = ["bitcoin", "ethereum", "solana", "dogecoin"]

url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": ",".join(coin_ids),
    "vs_currencies": "usd",
    "include_24hr_change": "true"
}

response = requests.get(url, params=params)
data = response.json()

coin_data = []
for coin_id in coin_ids:
    info = data[coin_id]
    coin_data.append({
        "coin": coin_id,
        "price_usd": info["usd"],
        "change_24h_%": round(info["usd_24h_change"], 2)
    })

df = pd.DataFrame(coin_data)
df.to_csv("api.csv", index=False, encoding="utf-8-sig")

import requests
import json

response = requests.get(
    "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo")

IBM_intra_day_5min = response.json()

with open("IBM.json", "w") as f:
    json.dump(IBM_intra_day_5min, f, indent=2)
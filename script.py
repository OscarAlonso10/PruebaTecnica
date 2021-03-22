import requests
from pymongo import MongoClient

client = MongoClient('localhost')
db = client['prueba']
transactions_col = db["transactions"]

url = "https://mainnet-fullnode1.coti.io/transaction/addressTransactions"

payload = "{\"address\":\"51dbd2feecb8c9e3b5c88129da88156d738d00d57bf4524cc780221c4e414ffc9372b00ad7d75679032d928776b044d40d5febb783d8ac9b241b7c0b1cad77de9b699c23\"}"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ca,en-US;q=0.7,en;q=0.3',
    'Content-Type': 'application/json',
    'cache-control': 'no-cache',
    'Origin': 'https://explorer.coti.io',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://explorer.coti.io/'
}

response = requests.request("POST", url, headers=headers, data=payload)
response = response.json()

for i in response["transactionsData"]:
    try:
        i["_id"] = i.pop("hash")
        x = transactions_col.insert_one(i)
    except:
        continue

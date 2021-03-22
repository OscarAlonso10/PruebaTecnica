import uvicorn
from pymongo import MongoClient
from fastapi import FastAPI

client = MongoClient('localhost')

db = client['prueba']
transactions_col = db["transactions"]


app = FastAPI()

"""GET http://localhost:8000/transactions
Api Documentation

Request Headers
Accept  application/json, text/plain, */*
Accept-Language  ca,en-US;q=0.7,en;q=0.3
Content-Type  application/json
Origin  https://explorer.coti.io
Referer https://explorer.coti.io/
"""

@app.get("/transactions")

def transactions():
    transactions = []
    for transaction in transactions_col.find():
        transactions.append(transaction)
    return {'transactions': transactions}


"""GET http://localhost:8000/especified_transactions
Api Documentation

Request Headers
Accept  application/json, text/plain, */*
Accept-Language  ca,en-US;q=0.7,en;q=0.3
Content-Type  application/json
Origin  https://explorer.coti.io
Referer https://explorer.coti.io/
"""

@app.get("/especified_transactions")

def transactions():
    transactions = []
    for esp_transaction in transactions_col.find():
        esp_transactions = {"id": esp_transaction["_id"], "amount": esp_transaction["amount"],
                            "type": esp_transaction["type"]}
        transactions.append(esp_transactions)
    return {'especified_transactions': transactions}

if __name__ == "__main__":
    uvicorn.run(app)

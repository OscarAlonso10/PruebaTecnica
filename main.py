import uvicorn
from pymongo import MongoClient
from fastapi import FastAPI

client = MongoClient('localhost')

db = client['prueba']
mycol = db["transactions"]


app = FastAPI()

@app.get("/transactions")
def transactions():
    transactions = []
    for transaction in mycol.find():
        transactions.append(transaction)
    return {'transactions': transactions}

if __name__ == "__main__":
    uvicorn.run(app)



import requests
import pymongo

COINS_URL = "https://api.coingecko.com/api/v3/coins/list?include_platform=true"
MONGO_URL = "mongodb://localhost:27017/"
DB_NAME = "tokentools"
COINS_COLLECTION_NAME = "coins"

client = pymongo.MongoClient(MONGO_URL)
db = client[DB_NAME]
collection = db[COINS_COLLECTION_NAME]

def get_coins_json() -> str:
    return requests.get(COINS_URL).json()

def clear_coins_collection():
    collection.delete_many({})

def save_coins(coins_json: str):
    collection.insert_many(coins_json)
    
clear_coins_collection()
save_coins(get_coins_json())
print('Coins database updated')
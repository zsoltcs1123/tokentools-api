import pymongo
from coin import Coin
from etherscan_scraper import get_creation_block_timestamp
from time_util import hex_to_datetime

MONGO_URL = "mongodb://localhost:27017/"
DB_NAME = "tokentools"
COINS_COLLECTION_NAME = "coins"

    
client = pymongo.MongoClient(MONGO_URL)
db = client[DB_NAME]
collection = db[COINS_COLLECTION_NAME]

def get_first_10_coins():
    return collection.find().limit(10)

def print_coin_count():
    return collection.count_documents({})

def query_coins_by_symbol(symbol):
    return [Coin(coin) for coin in collection.find({'symbol': symbol})]

res = query_coins_by_symbol('eth')[0]
ts_hex = get_creation_block_timestamp(res.platforms['ethereum'])

print(hex_to_datetime(ts_hex))
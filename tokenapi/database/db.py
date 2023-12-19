import os
import pymongo


COINS_RAW_COLLECTION_NAME = "coins"
COINS_METADATA_COLLECTION_NAME = "coins_metadata"


# Initialize MongoDB client
mongo_client = pymongo.MongoClient(os.getenv("MONGO_URL"))

# Define database
mongo_db = mongo_client[os.getenv("DB_NAME")]


# Coin collections
mongo_db.coins = mongo_db[COINS_RAW_COLLECTION_NAME]
mongo_db.coins_metadata = mongo_db[COINS_METADATA_COLLECTION_NAME]

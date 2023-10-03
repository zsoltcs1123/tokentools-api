import pymongo


MONGO_URL = "mongodb://localhost:27017/"
DB_NAME = "tokentools"
COINS_RAW_COLLECTION_NAME = "coins"
COINS_METADATA_COLLECTION_NAME = "coins_metadata"


# Initialize MongoDB client
mongo_client = pymongo.MongoClient(MONGO_URL)

# Define database 
mongo_db = mongo_client[DB_NAME] 

# Coin collections
mongo_db.coins = mongo_db[COINS_RAW_COLLECTION_NAME]
mongo_db.coins_metadata = mongo_db[COINS_METADATA_COLLECTION_NAME]
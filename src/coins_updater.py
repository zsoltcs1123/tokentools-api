import requests
from coin_dao import CoinDAO

COINS_URL = "https://api.coingecko.com/api/v3/coins/list?include_platform=true"

def get_coins_json() -> str:
    return requests.get(COINS_URL).json()

dao = CoinDAO()
    
dao.clear_coins_collection()
dao.save_coins(get_coins_json())
print('Coins database updated')
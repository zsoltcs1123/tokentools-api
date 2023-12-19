from typing import List, Optional

from tokenapi.database.db import mongo_db
from tokenapi.database.coin import Coin
from tokenapi.database.coin_metadata import CoinMetadata


class CoinDAO:
    def clear_coins_collection(self) -> None:
        mongo_db.coins.delete_many({})

    def save_coins(self, coins_json: str) -> None:
        mongo_db.coins.insert_many(coins_json)

    def get_first_10_coins(self) -> list:
        return [Coin(coin) for coin in mongo_db.coins.find().limit(10)]

    def query_coins_by_symbol(self, symbol: str) -> List[Coin]:
        return [Coin(coin) for coin in mongo_db.coins.find({"symbol": symbol.lower()})]

    def query_coin_by_symbol(self, symbol: str) -> Optional[Coin]:
        coin_data = mongo_db.coins.find_one({"symbol": symbol.lower()})
        return Coin(coin_data) if coin_data else None

    def query_coin_by_name(self, name: str) -> List[Coin]:
        return [Coin(coin) for coin in mongo_db.coins.find({"name": name})]

    def save_coin_metadata(self, coin_metadata: CoinMetadata) -> None:
        doc = {
            "coin_id": coin_metadata.coin_id,
            "symbol": coin_metadata.symbol,
            "birth_date": coin_metadata.birth_date,
            "birth_card": coin_metadata.birth_card,
        }
        mongo_db.coins_metadata.insert_one(doc)


coin_dao = CoinDAO()


def get_coin_dao():
    return coin_dao

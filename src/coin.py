from dataclasses import dataclass
from typing import Dict
from bson.objectid import ObjectId


@dataclass
class Coin:
    object_id: ObjectId
    id: str
    name: str
    symbol: str
    platforms: Dict[str, str]
    
    def __init__(self, coin_json: Dict[str, str]):
        self.object_id = coin_json['_id']
        self.id = coin_json['id']
        self.name = coin_json['name']
        self.symbol = coin_json['symbol']
        self.platforms = coin_json['platforms']
        
    def __repr__(self):
        return f"Coin(id='{self.id}', name='{self.name}', symbol='{self.symbol}', platforms={self.platforms})"

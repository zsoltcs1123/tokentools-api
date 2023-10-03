from dataclasses import dataclass
from datetime import datetime
from bson.objectid import ObjectId

@dataclass
class CoinMetadata:
    coin_id: ObjectId
    symbol: str
    birth_date: datetime
    birth_card: str
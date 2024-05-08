from dataclasses import dataclass
from datetime import datetime


@dataclass
class TokenData:
    contract_address: str
    birth_date: datetime

from datetime import datetime
from typing import Optional
from tokenapi.database.coin_dao import CoinDAO
from tokenapi.services.etherscan_scraper import get_creation_block_timestamp
from tokenapi.util.time_util import hex_to_datetime_utc


def get_birth_date(symbol: str, coin_dao: CoinDAO) -> Optional[datetime]:
    coin = coin_dao.query_coin_by_symbol(symbol)

    if not "ethereum" in coin.platforms:
        return None

    ts_hex = get_creation_block_timestamp(coin.platforms["ethereum"])
    return hex_to_datetime_utc(ts_hex)

from datetime import datetime

from tokenapi.services.etherscan_scraper import get_creation_block_timestamp
from tokenapi.util.time_util import hex_to_datetime_utc


def get_birth_date(contract_address: str) -> datetime:
    ts_hex = get_creation_block_timestamp(contract_address)
    return hex_to_datetime_utc(ts_hex)

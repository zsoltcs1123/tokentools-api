from web3 import Web3
from datetime import datetime


def hex_to_unix(hex_ts: str) -> int:
    return int(hex_ts, 16) 


def unix_to_datetime(unix_ts: int) -> datetime:
    return datetime.fromtimestamp(unix_ts)


def hex_to_datetime(hex_ts: str) -> datetime:
    return unix_to_datetime(hex_to_unix(hex_ts))

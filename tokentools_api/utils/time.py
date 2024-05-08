from datetime import datetime

import pytz


def hex_to_unix(hex_ts: str) -> int:
    return int(hex_ts, 16)


def unix_to_datetime(unix_ts: int) -> datetime:
    return datetime.fromtimestamp(unix_ts)


def hex_to_datetime(hex_ts: str) -> datetime:
    return unix_to_datetime(hex_to_unix(hex_ts))


def hex_to_datetime_utc(hex_ts: str) -> datetime:
    return hex_to_datetime(hex_ts).astimezone(pytz.UTC)

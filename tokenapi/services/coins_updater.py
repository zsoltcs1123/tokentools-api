import os
import requests
import logging
from fastapi import Depends
from tokenapi.database.coin_dao import CoinDAO
from tokenapi.database.coin_dao import get_coin_dao

logger = logging.getLogger(__name__)


def get_coins_json() -> str:
    return requests.get(os.getenv("COINS_URL")).json()


def update_coins(coin_dao: CoinDAO = Depends(get_coin_dao)):
    coin_dao.clear_coins_collection()
    logger.info("Coins database cleared")

    coins_json = get_coins_json()
    # logger.debug(coins_json)

    coin_dao.save_coins(coins_json)
    logger.info("Coins database updated")

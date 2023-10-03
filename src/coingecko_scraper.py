from coin_dao import CoinDAO
from time_util import hex_to_datetime
from birth_card_calculator import get_birth_card
from etherscan_scraper import get_creation_block_timestamp
from coin_metadata import CoinMetadata

coins = [
    "RIO"
]


dao = CoinDAO()

for symbol in coins:
    
    matching_coins = dao.query_coins_by_symbol(symbol)
    
    for coin in matching_coins:
        
        if not 'ethereum' in coin.platforms:
            continue        
    
        ts_hex = get_creation_block_timestamp(coin.platforms['ethereum'])

        birth_date = hex_to_datetime(ts_hex)
        birth_card = get_birth_card(birth_date.date())
        birth_card_str = f'{birth_card[0]}/{birth_card[1]} - {birth_card[2]}'

        print(birth_date)
        print(birth_card_str)

        metadata = CoinMetadata(coin.object_id, coin.symbol, birth_date, birth_card_str)
        dao.save_coin_metadata(metadata)
        print(f'{symbol} metadata saved.')


from fastapi import Depends, FastAPI
import uvicorn
from dotenv import load_dotenv
from tokenapi.database.coin_dao import CoinDAO, get_coin_dao
from tokenapi.services import birth_date_service
from tokenapi.services.coins_updater import update_coins

load_dotenv()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/birthdate")
async def get_birth_date(symbol: str, coin_dao: CoinDAO = Depends(get_coin_dao)):
    birth_date_value = birth_date_service.get_birth_date(symbol, coin_dao)
    return {"birth_date": birth_date_value}


@app.on_event("startup")
async def startup_event():
    coin_dao = get_coin_dao()
    update_coins(coin_dao)


# if __name__ == "__main__":
#     uvicorn.run(
#         app,
#         host="0.0.0.0",
#         port=8001,
#         log_config="tokenapi/app/logger_conf.yaml",
#     )

import logging

from fastapi import APIRouter, HTTPException

from tokentools_api.models.token_data import TokenData
from tokentools_api.services import birth_date_service

router = APIRouter(prefix="/tokenData", tags=["tokenData"])

logging.basicConfig(level=logging.DEBUG)


@router.get("/ethereum/{contract_address}")
async def get_token_data(contract_address: str) -> TokenData:
    try:
        birth_date_value = birth_date_service.get_birth_date(contract_address)
        return TokenData(contract_address, birth_date_value)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

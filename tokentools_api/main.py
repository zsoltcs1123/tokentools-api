import logging

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from tokentools_api.services import birth_date_service

load_dotenv()

app = FastAPI()

logging.basicConfig(level=logging.DEBUG)

# Define a list of allowed origins for CORS
# For development, you might allow all origins. For production, list your frontend's origin.
origins = [
    "http://localhost:3000",  # Assuming your React app runs on this origin
    "https://yourproductionfrontend.com",
]

# Add CORSMiddleware to the application instance
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows specified origins (use ["*"] for all origins)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/birthdate")
async def get_birth_date(contract_address: str):
    try:
        birth_date_value = birth_date_service.get_birth_date(contract_address)
        return {"contract_address": contract_address, "birth_date": birth_date_value}
    except Exception as e:
        logging.error(
            f"Error getting birth date for contract address {contract_address}: {e}"
        )
        raise HTTPException(status_code=500, detail=str(e))


# if __name__ == "__main__":
#     uvicorn.run(
#         app,
#         host="0.0.0.0",
#         port=8001,
#         log_config="tokenapi/app/logger_conf.yaml",
#     )

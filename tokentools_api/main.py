import logging

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.exception_handlers import http_exception_handler
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException

from tokentools_api.routes import token_data

load_dotenv()

app = FastAPI(root_path="/api/v1")

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


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    logging.error(f"Error handling request: {request.method} {request.url} {exc}")
    return await http_exception_handler(request, exc)


app.include_router(token_data.router)

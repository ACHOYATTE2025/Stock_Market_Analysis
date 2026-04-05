from pydantic import BaseModel
from dotenv import load_dotenv
from datetime import timedelta
import os

load_dotenv()

class Settings(BaseModel):
    authjwt_secret_key: str = os.getenv("JWT_SECRET_KEY")
    authjwt_access_token_expires: timedelta = timedelta(minutes=30)
    authjwt_refresh_token_expires: timedelta = timedelta(days=7)

def get_jwt_settings():
    return Settings()
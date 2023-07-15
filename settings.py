from pydantic import BaseSettings
from typing import Optional
class MongoSettings(BaseSettings):
    
    connection_string: Optional[str]=None
    collection: str = "puzzles_dev"
    class Config:
        env_prefix = "MONGO_"
        env_file = ".env"
        env_file_encoding = "utf-8"
        



class AuthSettings(BaseSettings):
    connection_uri: str = "http://localhost:3567"
    api_key: str

    api_domain: str = "http://localhost:3001"
    api_base_path: str = "/api/v1/auth"
    website_domain: str = "http://localhost:3390"

    class Config:
        env_prefix = "LEMODI_AUTH_"
        env_file = ".env"
        env_file_encoding = "utf-8"
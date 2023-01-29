from pydantic import BaseSettings
from typing import Optional
class MongoSettings(BaseSettings):
    
    connection_string: Optional[str]=None
    
    class Config:
        env_prefix = "MONGO_"
        env_file = ".env"
        env_file_encoding = "utf-8"
        
        
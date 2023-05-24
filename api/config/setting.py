from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str = "mongodb+srv://avijitsenme:8P9hYd5TMa4VbzaT@fastfck.4upl604.mongodb.net/?retryWrites=true&w=majority"
    MONGO_DB: str = "fastapi"

  
    
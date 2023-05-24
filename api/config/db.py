from pymongo import MongoClient
from api.config.setting import Settings

settings = Settings()
MongoClient = MongoClient(settings.MONGO_URI)
db = MongoClient[settings.MONGO_DB]
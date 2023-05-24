from api.config.setting import Settings
from fastapi import APIRouter, Depends, HTTPException

baseRouter = APIRouter()

@baseRouter.get("/")
async def root():
    settings = Settings()
    return {"message": "Hello World"}
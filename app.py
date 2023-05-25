from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles

from api.routes.base import baseRouter
from api.routes.user import userRoutes as userRouter

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(baseRouter)
app.include_router(userRouter, tags=["User"], prefix="/user")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
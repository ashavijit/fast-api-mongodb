from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles

from api.routes.base import baseRouter

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(baseRouter)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
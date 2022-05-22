import logging

import uvicorn
from fastapi import FastAPI

from src.api.routers import station_router

logging.basicConfig(level=logging.INFO)

app = FastAPI()

app.include_router(station_router)


if __name__ == "__main__":
    uvicorn.run("src.__main__:app", port=3000, reload=True)

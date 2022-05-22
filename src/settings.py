import os
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    WEBSOCKETS_SERVER_HOST: str
    WEBSOCKETS_SERVER_PORT: int
    WEBSOCKETS_SUBPROTOCOL = "ocpp2.0.1"

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        case_sensitive = True


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()

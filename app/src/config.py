from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    DB_PORT: int
    DB_HOST: str
    DB_NAME: str
    DB_USER: str
    DB_PASS: str

    @property
    def database_url_psycopg(self):
        """Подключение асинхронной базы"""
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def database_url_asyncpg(self):
        """Подключение синхронной базы"""
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=os.getenv(".env"))


settings = Settings()

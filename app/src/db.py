from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.src.config import settings


sync_engine = create_engine(
    url=settings.database_url_psycopg,
    echo=False,
)

async_engine = create_async_engine(
    url=settings.database_url_asyncpg,
    echo=False,
)

"""Создаём сессии"""
sync_session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)

import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text
from app.src.config import settings


sync_engine = create_engine(
    url=settings.database_url_psycopg,
    echo=True,
)

async_engine = create_async_engine(
    url=settings.database_url_asyncpg,
    echo=False,
)

"""Создаём сессии"""
sync_session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)

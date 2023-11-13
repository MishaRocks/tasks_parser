from typing import Optional

from sqlalchemy import Table, Column, String, Integer, Text, MetaData
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    ...


class Tasks(Base):
    __tablename__: str = "tasks"

    category: Mapped[str]
    topics: Mapped[str] = mapped_column(String(255))
    title: Mapped[str] = mapped_column(String(255), primary_key=True)
    contestId: Mapped[Optional[int]]
    index: Mapped[Optional[int]]
    solutions: Mapped[Optional[int]]
    complexity: Mapped[Optional[int]]

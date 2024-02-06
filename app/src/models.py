from typing import Optional

from sqlalchemy import String
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
    index: Mapped[Optional[str]]
    solutions: Mapped[Optional[int]]
    complexity: Mapped[Optional[int]]

    # def __repr__(self):
    #
    #     return (f'\nЗадача: {self.title} \n'
    #             f'Темы: {self.topics} \n'
    #             f'Количество решений: {self.solutions} '
    #             f'\nСложность: {self.complexity} \n ')

    def __repr__(self):
        result = []
        for col in self.__table__.columns.keys():
            result.append(f"{col}:{getattr(self, col)}")

        return f"{','.join(result)}"

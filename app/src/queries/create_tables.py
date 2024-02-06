from app.src.db import sync_engine
from app.src.models import Base


def create_tables():
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)


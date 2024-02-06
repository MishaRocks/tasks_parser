from sqlalchemy import select, and_

from app.src.db import sync_session_factory
from app.src.models import Tasks


def get_tasks_set(category, rating):
    with sync_session_factory() as session:
        query = (
            select(Tasks)
            .select_from(Tasks)
            .where(and_(
                Tasks.category == category,
                Tasks.complexity == rating
            ))
            .limit(10)
        )
        result = session.execute(query)
        return result.fetchall()


print(get_tasks_set("constructive algorithms", 1600))

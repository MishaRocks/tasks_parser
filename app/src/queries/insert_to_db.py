from timeloop import Timeloop
from datetime import timedelta
from sqlalchemy.exc import IntegrityError

from app.src.api.connector_api import ConnectApi
from app.src.db import async_session_factory, sync_session_factory
from app.src.models import Tasks

tl = Timeloop()


@tl.job(interval=timedelta(hours=1))
def insert_to_db() -> None:
    tasks = ConnectApi().get_tasks_by_api()
    for task in tasks:

        with sync_session_factory() as session:
            task_to_db = Tasks(
                category=task['category'],
                topics=task['topics'],
                title=task['title'],
                contestId=task['contestId'],
                index=task['index'],
                solutions=task['solutions'],
                complexity=task['complexity']
            )
            session.add(task_to_db)
            try:
                session.commit()
            except IntegrityError as e:
                continue

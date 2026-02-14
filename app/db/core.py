from typing import Any, Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

DATABASE_URL = "sqlite+pysqlite:///blogs.db"

engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
)

# session
session_local = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    bind=engine,
)


def init_db() -> None:
    from app.db.models import Base
    Base.metadata.create_all(bind=engine)
    

# dependency to get the database session
def get_db() -> Generator[Session, Any, None]:
    database = session_local()
    try:
        yield database
    finally:
        database.close()

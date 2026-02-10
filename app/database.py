from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABSE_URL = "sqlite+pysqlite:///blogs.db"

engine = create_engine(DATABSE_URL, echo=True) # echo = true prints the SQL

#session 
SessionLocal = sessionmaker(bind=engine)

#base class for ORM models
Base = declarative_base()



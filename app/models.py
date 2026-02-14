from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import DateTime, func


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"

    id : Mapped[str] = mapped_column(primary_key=True, nullable=False)
    email : Mapped[str] = mapped_column(nullable=False, unique=True)
    password_hash : Mapped[str] = mapped_column(nullable=False)
    created_at = mapped_column(DateTime,server_default=func.now(), nullable=False)
    





    
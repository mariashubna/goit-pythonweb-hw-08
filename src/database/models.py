from datetime import date

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = "contacts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = Column(String(25), nullable=False)
    last_name: Mapped[str] = Column(String(25), nullable=False)
    email: Mapped[str] = Column(String(100), nullable=False, unique=True)
    phone: Mapped[str] = Column(String(20), nullable=False, unique=True)
    birthday: Mapped[date] = Column(Date, nullable=False)
    additional_info: Mapped[str] = Column(String(255), nullable=True)

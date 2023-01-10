# import atexit
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from config import PG_DSN

Base = declarative_base()


class UserModel(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)


class AdModel(Base):
    __tablename__ = 'ad'

    id = Column(Integer, primary_key=True, autoincrement=True)
    header = Column(String(100), unique=True, nullable=False)
    description = Column(String(500), unique=True, nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.now)
    owner = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)

    user = relationship(UserModel, backref='ads')


def get_engine():
    return create_engine(PG_DSN)


def get_session_maker():
    return sessionmaker(bind=get_engine())


def init_db():
    Base.metadata.create_all(bind=get_engine())


init_db()

# atexit.register(lambda: engine.dispose())

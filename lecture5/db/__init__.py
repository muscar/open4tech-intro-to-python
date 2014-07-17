from contextlib import contextmanager

from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import sessionmaker


import config

engine = create_engine(config.DB_NAME, echo=True)
Session = sessionmaker(bind=engine)


# Base = declarative_base()


# class ModelMixin(object):
#     @declared_attr
#     def __tablename__(cls):
#         return cls.__name__.lower()

#     id =  Column(Integer, primary_key=True)


class Base(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id =  Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""

    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def init():
    Base.metadata.create_all(engine)

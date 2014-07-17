from db import Base#, ModelMixin

from sqlalchemy import Column, DateTime, Integer, String


class User(Base):#, ModelMixin):
    name = Column(String(100))
    fullname = Column(String(100))
    password = Column(String(100))
    created = Column(DateTime)

    def __repr__(self):
        return '<User(name="{0}", fullname="{1}", password="{2}", crated="{3}")>'.format(
            self.name, self.fullname, self.password, self.created)

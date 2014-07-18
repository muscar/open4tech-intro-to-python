from db import Base

from sqlalchemy import Column, DateTime, String


class LogEntry(Base):
    level = Column(String(100))
    created = Column(DateTime)
    message = Column(String(255))

    def __repr__(self):
        return '<LogEntry(level="{0}", created="{1}", message="{2}")>'.format(
            self.level, self.created, self.message)

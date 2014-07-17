import db

from db import session_scope
from db.models import User

from datetime import datetime as dt


def insert():
    with session_scope() as session:
        ed_user = User(name='foo', fullname='Foo Meta', password='foometa', created=dt.now())
        session.add(ed_user)
        session.commit()


def retrieve():
    with session_scope() as session:
        for instance in session.query(User).order_by(User.id): 
            print(instance.name, instance.fullname, instance.created)


def main():
    db.init()
    insert()
    retrieve()


if __name__ == '__main__':
    main()

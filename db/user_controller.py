import datetime

from sqlalchemy import Column, Integer, Sequence, DateTime, String

from db import SESSION, BASE


class Users(BASE):
    __tablename__ = "users"
    id = Column(Integer, Sequence('some_id_seq'))
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    user_status = Column(Integer, default=1)
    user_lang = Column(String, default="ru")
    reg_date = Column(DateTime, default=datetime.datetime.utcnow())

    def __init__(self, user_id, user_name, first_name, last_name):
        self.user_id = user_id
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "<User info %d> " % self.user_id


Users.__table__.create(checkfirst=True)


def get_all_users():
    users = SESSION.query(Users).all()
    SESSION.commit()
    return users


def add_user(user_id, user_name, first_name, last_name):
    users = SESSION.query(Users).get(user_id)
    if users:
        return False
    else:
        users = Users(user_id, user_name, first_name, last_name)
    SESSION.add(users)
    SESSION.commit()
    return True

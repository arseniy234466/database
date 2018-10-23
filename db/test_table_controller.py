from sqlalchemy import Column, Integer, Sequence, DateTime, String

from db import SESSION, BASE


class TestTabe(BASE):
    __tablename__ = "test_table"
    city = Column(String)
    user_id = Column(Integer, primary_key=True)
    country = Column(String, default="Россия")

    def __init__(self, user_id, city):
        self.user_id = user_id
        self.city = city

    def __repr__(self):
        return "<User info %d> " % self.user_id


TestTabe.__table__.create(checkfirst=True)


def get_locate_all_user():
    users = SESSION.query(TestTabe).all()
    return users


def add_locate_user(val1, val2):
    user = SESSION.query(TestTabe).get(val1)
    if user:
        return False
    else:
        user = TestTabe(user_id=val1, city=val2)
    SESSION.add(user)
    SESSION.commit()
    return True


def get_locate_curent_user(user_id):
    user_2 = SESSION.query(TestTabe).get(user_id)
    return user_2


# sess.query(User).filter(User.age == 25)

def get_locate_by_city(city):
    user = SESSION.query(TestTabe).filter(TestTabe.city == city)
    return user

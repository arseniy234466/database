from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import Development as Config


def start():
    db_url = Config.SQLALCHEMY_DATABASE_URL
    engine = create_engine(db_url)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    session_maker = sessionmaker(autoflush=False)
    return session_maker(bind=engine)


BASE = declarative_base()
SESSION = start()
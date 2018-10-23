class Config(object):
    LOGGER = True
    url = 'sqlite:///test.db'
    SQLALCHEMY_DATABASE_URL = url


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True

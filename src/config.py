class Development(object):

    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_DATABASE_URI = 'postgres://root:insected#3@localhost:5432/cities_db'

class Production(object):

    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI = 'postgres://root:insected#3@localhost:5432/cities_db'

app_config = {
    'development': Development,
    'production': Production
}
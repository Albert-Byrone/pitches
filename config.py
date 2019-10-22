import os
class Config:

    DATABASE_URL = 'postgresql+psycopg2://byrone:Albert254@localhost/pitcher'
    SECRET_KEY = 'albertbyrone'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'stmp.googleemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
from datetime import timedelta

class LocalConfig:
    HOST = '127.0.0.1'
    PORT = 80
    DEBUG = True

    SECRET_KEY = 'S3CRE7_K3YS'

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=365)

    RUN_SETTINGS = {
        'host': HOST,
        'port': PORT,
        'debug': DEBUG,
    }
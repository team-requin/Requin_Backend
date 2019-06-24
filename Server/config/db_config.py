import os

class LocalDBConfig:
    SERVICE_NAME = 'Database_Name'

    HOST = '127.0.0.1'
    PORT = '12345'
    USERNAME = os.getenv('DB_ID')
    PASSWORD = os.getenv('DB_PW')

    DB_SETTINGS = {
        'db': SERVICE_NAME,
        'host': HOST,
        'port': PORT,
        'username': USERNAME,
        'password': PASSWORD,
    }
import os

DB_NAME = os.getenv('DB_NAME', 'fbng_db')
DB_USER = os.getenv('DB_USER', 'db_user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'db_pwd')
DB_HOST = os.getenv('DB_HOST', 'fbng_db')

try:
    from settings_local import *
except ModuleNotFoundError:
    pass

JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 20

DB_CONNECTION_YOYO = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

# Frontend
FURL_ACCOUNT = '/api/account'
FURL_LOGIN = '/api/auth/login'

# Backend
ACCOUNT_ROUTE = '/account'
LOGIN_ROUTE = '/auth/login'

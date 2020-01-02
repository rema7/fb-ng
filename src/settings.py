import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(PROJECT_ROOT, 'logs')
LOG_LEVEL = 'ERROR'

DB_NAME = os.getenv('DB_NAME', 'fbng_db')
DB_USER = os.getenv('DB_USER', 'db_user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'db_pwd')
DB_HOST = os.getenv('DB_HOST', 'fbng_db')

try:
    from settings_local import *
except ModuleNotFoundError:
    pass

JWT_SECRET = 'eyJ0eXAiOi'
JWT_ALGORITHM = 'HS256'
JWT_EXP_SECONDS = 600

DB_CONNECTION_YOYO = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

# Frontend
FURL_ACCOUNT = '/api/account'
FURL_REGISTER = '/api/register'
FURL_LOGIN = '/api/auth/login'
FURL_SETTINGS = '/api/settings'

# Backend
ACCOUNT_ROUTE = '/account'
REGISTER_ROUTE = '/register'
LOGIN_ROUTE = '/auth/login'
SETTINGS_ROUTE = '/settings'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': LOG_LEVEL,
        'handlers': ['debug_file'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
        },
    },
    'handlers': {
        'stream': {
            'level': LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'debug_file': {
            'level': LOG_LEVEL,
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(LOG_DIR, 'debug.logs'),
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(LOG_DIR, 'error.logs'),
        },
        'access_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'access.logs'),
        }
    },
    'loggers': {
        'worker': {
            'level': LOG_LEVEL,
            'handlers': ['stream'],
        },
        'fbng': {
            'level': LOG_LEVEL,
            'handlers': ['error_file', 'debug_file'],
            'propagate': False,
        },
        'gunicorn.error': {
            'level': 'INFO',
            'handlers': ['error_file', 'stream'],
            'propagate': True,
        },
        'gunicorn.access': {
            'level': 'INFO',
            'handlers': ['access_file', 'stream'],
            'propagate': False,
        },
    },
}

from contextlib import contextmanager

import pymysql

import settings as app_settings

connection = pymysql.connect(
    host=app_settings.DB_HOST,
    user=app_settings.DB_USER,
    password=app_settings.DB_PASSWORD,
    db=app_settings.DB_NAME,
    cursorclass=pymysql.cursors.DictCursor
)


@contextmanager
def open_db_session():
    try:
        yield connection
    except:
        connection.rollback()
        raise


from contextlib import contextmanager

import pymysql

import settings as app_settings


def open_connection():
    return pymysql.connect(
        host=app_settings.DB_HOST,
        user=app_settings.DB_USER,
        password=app_settings.DB_PASSWORD,
        db=app_settings.DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )


@contextmanager
def open_db_session():
    connection = open_connection()
    try:
        yield connection
    except:
        connection.rollback()
    connection.close()

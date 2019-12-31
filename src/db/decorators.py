from functools import wraps

from db.session import open_db_session


def with_db_session(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get('db_session') is None:
            with open_db_session() as db_session:
                kwargs['db_session'] = db_session
                return fn(*args, **kwargs)

        return fn(*args, **kwargs)

    return wrapper

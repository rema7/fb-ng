from functools import wraps

from db.session import open_db_session


def with_db_session(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get('cursor') is None:
            with open_db_session() as connection:
                kwargs['connection'] = connection
                return fn(*args, **kwargs)

        return fn(*args, **kwargs)

    return wrapper

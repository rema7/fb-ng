from datetime import datetime

import falcon
import jsonschema
import jwt

import settings as app_settings
from db.decorators import with_db_session


def validate_schema(json, schema, raise_exception=True):
    try:
        jsonschema.validate(json, schema)
    except jsonschema.ValidationError as e:
        if raise_exception:
            raise falcon.HTTPBadRequest(
                'Failed data validation',
                e.message
            )


def validate_request(schema):
    def decor(func):
        def wrapper(self, req, resp, *args, **kwargs):
            json = req.context.get('body', None)
            validate_schema(json, schema)
            return func(self, req, resp, *args, **kwargs)
        return wrapper
    return decor


@with_db_session
def validate_auth(req, resp, resource, params, connection):
    encoded_jwt = req.context.get('Token', None)
    if not encoded_jwt:
        raise falcon.HTTPUnauthorized(
            description='Not authorized'
        )

    decoded_token = jwt.decode(
        encoded_jwt,
        app_settings.JWT_SECRET,
        algorithm=app_settings.JWT_ALGORITHM
    )
    expire_at = decoded_token['expire_at']
    if datetime.utcnow() >= datetime.fromisoformat(expire_at):
        raise falcon.HTTPUnauthorized(
            description='Not authorized'
        )

    req.context['account'] = decoded_token

import falcon
import jsonschema
import jwt

import settings as app_settings


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


def validate_auth(req, resp, resource, params):
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
    req.context['account'] = decoded_token

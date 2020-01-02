from datetime import datetime, timedelta

import falcon
import jwt
from passlib.handlers.pbkdf2 import pbkdf2_sha256
from validate_email import validate_email

import settings as app_settings


def is_email_valid(email):
    if not validate_email(email):
        msg = 'Invalid email {}'.format(email)
        raise falcon.HTTPInvalidParam(
            msg=msg,
            param_name='email'
        )


def generate_password_hash(password):
    return pbkdf2_sha256.using(rounds=200000, salt_size=16).hash(password)


def verify_password(password, password_hash):
    return pbkdf2_sha256.verify(password, password_hash)


def generate_token(uuid, email):
    expire_at = datetime.utcnow() + timedelta(app_settings.JWT_EXP_SECONDS)
    return jwt.encode(
        {
            'uuid': uuid,
            'email': email,
            'expire_at': str(expire_at.isoformat())
        },
        app_settings.JWT_SECRET,
        algorithm=app_settings.JWT_ALGORITHM
    )

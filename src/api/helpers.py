import falcon
from validate_email import validate_email


def is_email_valid(email):
    if not validate_email(email):
        msg = 'Invalid email {}'.format(email)
        raise falcon.HTTPInvalidParam(
            msg=msg,
            param_name='email'
        )


def generate_token():
    pass

from uuid import uuid4

import falcon

from api.auth.helpers import generate_token, generate_password_hash, is_email_valid, verify_password
from api.auth.schemas import register_request_schema, auth_request_schema
from api.decorators import validate_request
from db.decorators import with_db_session


class LoginResource:
    @staticmethod
    @with_db_session
    def handle_post(email, password, connection=None):
        is_email_valid(email)
        cursor = connection.cursor()
        query = f"""
                SELECT
                    uuid,
                    password
                FROM
                    account
                where account.email = '{email}'
                """
        cursor.execute(query)
        account_db = cursor.fetchone()
        if account_db is None:
            raise falcon.HTTPNotFound(
                description='Wrong email or password'
            )
        cursor.close()

        uuid = account_db['uuid']
        password_hash = account_db['password']
        if not verify_password(password, password_hash):
            raise falcon.HTTPNotFound(
                description='Wrong email or password'
            )
        return {
            'token': generate_token(uuid, email)
        }

    @validate_request(auth_request_schema)
    def on_post(self, req, resp):
        body = req.context['body']

        resp.body = self.handle_post(
            email=body['email'],
            password=body['password']
        )


class RegisterResource:
    @staticmethod
    @with_db_session
    def handle_post(
            email, password, name, last_name, age, sex, country, connection=None
    ):
        is_email_valid(email)
        with connection.cursor() as cursor:
            sql = "SELECT `email` FROM `account` where `email` = %s"
            cursor.execute(sql, email)
            account_db = cursor.fetchone()
            if account_db is not None:
                raise falcon.HTTPConflict(
                    description='Already exists'
                )

        with connection.cursor() as cursor:
            uuid = str(uuid4())
            sql = "INSERT INTO `account`" \
                  " (`uuid`, `email`, `password`, `name`, `last_name`, `age`, `sex`, `country`)" \
                  " VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (
                uuid, email, generate_password_hash(password),
                name, last_name, age, sex, country
            ))
        cursor.close()
        connection.commit()
        return {
            'token': generate_token(uuid, email)
        }

    @validate_request(register_request_schema)
    def on_post(self, req, resp):
        body = req.context['body']

        resp.body = self.handle_post(
            email=body['email'],
            password=body['password'],
            name=body['name'],
            last_name=body['last_name'],
            age=body['age'],
            sex=body['sex'],
            country=body['country']
        )

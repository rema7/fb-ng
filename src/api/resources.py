from api.helpers import is_email_valid
from db.decorators import with_db_session


class LoginResource:
    @staticmethod
    @with_db_session
    def handle_post(email, password, db_session=None):
        is_email_valid(email)
        return

    def on_post(self, req, resp):
        body = req.context['body']

        resp.body = self.handle_post(
            email=body['email'],
            password=body['password']
        )

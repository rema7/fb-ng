import falcon

import settings as app_settings
from api.decorators import validate_auth
from db.decorators import with_db_session


@falcon.before(validate_auth)
class AccountResource:
    def on_get(self, req, resp):
        account = req.context['account']

        resp.body = account


class SettingsResource:
    @staticmethod
    def on_get(_, resp):
        frontend_urls_prefix = 'FURL_'
        business_logic_keys = ()
        resp.body = {
            key: getattr(app_settings, key.upper()) for key in business_logic_keys
        }
        resp.body.update({
            'urls': {
                key[len(frontend_urls_prefix):].lower(): getattr(app_settings, key.upper())
                for key in dir(app_settings) if key.startswith(frontend_urls_prefix)
            }
        })


class HobbiesResource:
    @staticmethod
    @with_db_session
    def handle_get(connection=None):
        with connection.cursor() as cursor:
            sql = "SELECT `name` FROM `hobby`"
            cursor.execute(sql)
        return [hobby['name'] for hobby in cursor.fetchall()]

    def on_get(self, req, resp):
        resp.body = self.handle_get()


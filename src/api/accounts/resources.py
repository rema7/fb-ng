import falcon

import settings as app_settings
from api.decorators import validate_auth
from db.decorators import with_db_session


@falcon.before(validate_auth)
class AccountsResource:
    @staticmethod
    @with_db_session
    def handle_get(account_id, connection=None):
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `account`"
            cursor.execute(sql)
            result = []
            for account_db in cursor.fetchall():
                del account_db['password']
                result.append(account_db)
            cursor.close()
            return result

    def on_get(self, req, resp):
        account = req.context['account']

        resp.body = self.handle_get(
            account_id=account['uuid']
        )


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

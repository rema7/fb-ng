import settings as app_settings
from api.decorators import validate_auth


@validate_auth
class AccountResource:
    def on_get(self, req, resp):
        # body = req.context['body']

        resp.body = {}


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
import logging
from logging.config import dictConfig

import falcon

from api.resources import SettingsResource, AccountResource
from api.auth.resources import LoginResource, RegisterResource
from middlewares import SecureMiddleware, ContentEncodingMiddleware
import settings as app_settings

dictConfig(app_settings.LOGGING)
logger = logging.getLogger('fbng.' + __name__)

app = falcon.API(middleware=[
    SecureMiddleware(),
    ContentEncodingMiddleware(),
])

app.add_route(app_settings.ACCOUNT_ROUTE, AccountResource())
app.add_route(app_settings.REGISTER_ROUTE, RegisterResource())
app.add_route(app_settings.LOGIN_ROUTE, LoginResource())
app.add_route(app_settings.SETTINGS_ROUTE, SettingsResource())

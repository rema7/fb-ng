import falcon

from api.resources import LoginResource
from middlewares import SecureMiddleware, ContentEncodingMiddleware
import settings as app_settings

app = falcon.API(middleware=[
    SecureMiddleware(),
    ContentEncodingMiddleware(),
])

app.add_route(app_settings.LOGIN_ROUTE, LoginResource())

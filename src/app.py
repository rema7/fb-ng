import falcon

from src.middlewares import SecureMiddleware, ContentEncodingMiddleware

app = falcon.API(middleware=[
    SecureMiddleware(),
    ContentEncodingMiddleware(),
])

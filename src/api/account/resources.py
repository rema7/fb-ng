# pylint: disable=R0201
import falcon

from api.logic import validate_auth


@falcon.before(validate_auth)
class AccountResource:
    def on_get(self, req, resp):
        account = req.context['account']
        resp.body = account.as_dict()

import falcon

@with_db_session
def validate_auth(req, resp, resource, params, db_session=None):
    token = req.context.get('Token', None)
    if not token:
        raise falcon.HTTPUnauthorized(
            description='Not authorized'
        )

    # token = db_session.query(AccountToken).filter(
    #     AccountToken.token == token
    # ).first()
    # if token is None:
    #     raise falcon.HTTPUnauthorized(
    #         description='Not authorized'
    #     )
    # account = db_session.query(Account).filter(
    #     Account.id == token.account_id
    # ).first()
    # req.context['account'] = account

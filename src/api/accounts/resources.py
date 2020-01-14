import falcon
from webargs import fields
from webargs.falconparser import use_args

import settings as app_settings
from api.decorators import validate_auth
from db.decorators import with_db_session

cmp = {
    'lt': '<',
    'lte': '<=',
    'gt': '>',
    'gte': '>=',
    'eq': '=',
}


@falcon.before(validate_auth)
class AccountsResource:
    @staticmethod
    @with_db_session
    def handle_get(
            account_id, search, limit,
            age, age_cmp, sex, country,
            connection=None
    ):
        fields = (account_id,)
        with connection.cursor() as cursor:
            sql = 'select' \
                  ' a.uuid, a.email, a.name, a.last_name, a.age, a.country, a.sex,' \
                  ' GROUP_CONCAT(h.name) as hobby' \
                  ' from account as a' \
                  ' left join account_hobby ah on a.uuid = ah.account_id' \
                  ' left join hobby h on ah.hobby_id = h.id' \
                  ' where a.uuid != %s'
            if search is not None and len(search) > 0:
                search = search.lower()
                sql += f' and ((lower(a.name) like %s or lower(a.last_name) like %s))'
                fields += (f'{search}%', f'{search}%')
            if age is not None:
                sql += f' and age {cmp.get(age_cmp)} %s'
                fields += (age,)
            if sex is not None:
                sql += f' and sex is %s'
                fields += (sex,)
            fields += (limit,)
            sql += ' group by a.uuid limit %s'

            cursor.execute(sql, fields)
            result = cursor.fetchall()
            cursor.close()
            return result

    @use_args({
        'search': fields.Str(required=False, missing=None),
        'limit': fields.Str(required=False, missing=100),
        'age': fields.Int(required=False, missing=None),
        'age_cmp': fields.Str(
            required=False, missing='eq',
            validate=lambda c: c in ['lt', 'lte', 'eq', 'gt', 'gte']
        ),
        'sex': fields.Int(required=False, missing=None),
        'country': fields.Int(required=False, missing=None)
    })
    def on_get(self, req, resp, args):
        account = req.context['account']

        resp.body = self.handle_get(
            account_id=account['uuid'],
            search=args['search'],
            limit=args['limit'],
            age=args['age'],
            age_cmp=args['age_cmp'],
            sex=args['sex'],
            country=args['country']
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

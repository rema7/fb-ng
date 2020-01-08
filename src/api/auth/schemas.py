auth_request_schema = {
    '$schema': 'http://json-schema.org/draft-07/schema',
    'type': 'object',
    'additionalProperties': False,
    'properties': {
        'email': {
            'type': 'string'
        },
        'password': {
            'type': 'string'
        },
    },
    'required': [
        'email',
        'password',
    ]
}
register_request_schema = {
    '$schema': 'http://json-schema.org/draft-07/schema',
    'type': 'object',
    'additionalProperties': False,
    'properties': {
        'email': {
            'type': 'string'
        },
        'password': {
            'type': 'string'
        },
        'name': {
            'type': 'string'
        },
        'last_name': {
            'type': 'string'
        },
        'age': {
            'type': 'integer'
        },
        'sex': {
            'type': 'string',
            'enum': ['male', 'female', 'other']
        },
        'country': {
            'type': 'string'
        },
        'hobbies': {
            'type': 'array',
            'items': {
                'type': 'string'
            }
        },
    },
    'required': [
        'email',
        'password',
        'name',
        'last_name',
        'age',
        'sex',
        'country'
    ]
}

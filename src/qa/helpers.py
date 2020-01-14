from random import randrange
from uuid import uuid4

from faker import Faker
from faker.providers import person, address

from api.auth.helpers import generate_password_hash
from db.decorators import with_db_session

sex = ['male', 'female', 'other']

hobbies = [
    'Hiking', 'Backpacking', 'Camping', 'Hunting', 'Fishing',
    'Archery', 'Canoeing', 'Kayaking', 'Running', 'Geocaching'
]


def generate_accounts(cursor, number=5):
    fake = Faker()
    fake.add_provider(person)
    fake.add_provider(address)

    uuids = []
    for i in range(number):
        uuid = str(uuid4())
        uuids.append(uuid)
        sql = "INSERT INTO `account`" \
              " (`uuid`, `email`, `password`, `name`, `last_name`, `age`, `sex`, `country`)" \
              " VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (
            uuid,
            f'user{i}@mail.ru',
            generate_password_hash('123'),
            fake.first_name(),
            fake.last_name(),
            randrange(18, 70),
            sex[randrange(0, 2)],
            fake.country()
        ))

    return uuids


def get_hobby(hobby, cursor, connection):
        sql = "select id from `hobby` as h where h.name = %s"
        cursor.execute(sql, hobby)
        hobby_db = cursor.fetchone()
        if hobby_db is None:
            sql = "INSERT INTO `hobby`" \
                  " (`name`)" \
                  " VALUES (%s)"
            cursor.execute(sql, (
                hobby,
            ))
            connection.commit()
            return connection.insert_id()
        return hobby_db['id']


@with_db_session
def qa_generate_data(number=5, connection=None):
    with connection.cursor() as cursor:
        print('Creating accounts...', flush=True)
        uuids = generate_accounts(cursor, number)
        print('Accounts created', flush=True)
        print('Filling hobbies...', flush=True)
        for uuid in uuids:
            hobbies_ids = set(
                [
                    get_hobby(hobbies[randrange(0, 10)], cursor, connection) for _ in range(3)
                ]
            )
            print(hobbies_ids, flush=True)

            for hobby_id in hobbies_ids:
                sql = "INSERT INTO `account_hobby`" \
                      " (`account_id`, `hobby_id`)" \
                      " VALUES (%s, %s)"
                cursor.execute(sql, (
                    uuid,
                    hobby_id
                ))
    print('Hobbies filled', flush=True)
    cursor.close()
    connection.commit()

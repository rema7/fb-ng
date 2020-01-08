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


def generate_hobby(connection=None):
    for hobby in hobbies:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `hobby`" \
                  " (`name`)" \
                  " VALUES (%s)"
            cursor.execute(sql, (
                hobby,
            ))
        cursor.close()
        connection.commit()


def generate_accounts(connection=None):
    fake = Faker()
    fake.add_provider(person)
    fake.add_provider(address)

    uuids = []
    for i in range(50):
        with connection.cursor() as cursor:
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
        cursor.close()
        connection.commit()
    return uuids


@with_db_session
def qa_generate_data(connection=None):
    generate_hobby(connection)
    uuids = generate_accounts(connection)
    for uuid in uuids:
        with connection.cursor() as cursor:
            hobbies_ids = set([randrange(1, 10) for _ in range(3)])
            for hobby_id in hobbies_ids:
                sql = "INSERT INTO `account_hobby`" \
                      " (`account_id`, `hobby_id`)" \
                      " VALUES (%s, %s)"
                cursor.execute(sql, (
                    uuid,
                    hobby_id
                ))
        cursor.close()
        connection.commit()




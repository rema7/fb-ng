from invoke import task

from db.tasks import reapply_migrations
from qa.helpers import qa_generate_data


@task
def generate_data(ctx):
    """
    Fill data in DataBase
    """
    print('Start filling...')

    qa_generate_data()

    print('Success')


@task
def reset_all(ctx):
    """
    Reapply migrations and fill data
    """
    print('Start reseting...')

    reapply_migrations(ctx)

    generate_data(ctx)

from invoke import task

import settings as app_settings


@task
def apply_migrations(ctx):
    print('Start migration apply...')
    command = 'yoyo apply --database {db_connection} migrations --no-config-file --batch'
    ctx.run(command.format(db_connection=app_settings.DB_CONNECTION_YOYO))
    print('Success')


@task
def reapply_migrations(ctx):
    print('Start reapply migrations...')
    command = 'yoyo reapply --database {db_connection} migrations --no-config-file --batch'
    ctx.run(command.format(db_connection=app_settings.DB_CONNECTION_YOYO))
    print('Success')


@task
def rollback_migrations(ctx, revision):
    print('Start rollback migrations...')
    command = 'yoyo rollback --database {db_connection} migrations --no-config-file --batch --revision {revision}'
    ctx.run(command.format(db_connection=app_settings.DB_CONNECTION_YOYO, revision=revision))
    print('Success')


@task
def break_lock(ctx):
    print('Start breaking lock...')
    command = 'yoyo break-lock --database {db_connection}'
    ctx.run(command.format(db_connection=app_settings.DB_CONNECTION_YOYO))
    print('Success')

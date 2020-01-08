
from invoke import Collection

from db import tasks as db_tasks
from qa import tasks as qa_tasks

LOCAL_SETTINGS = 'settings_local.py'

ns = Collection()
ns.add_collection(Collection.from_module(db_tasks), name='db')
ns.add_collection(Collection.from_module(qa_tasks), name='qa')

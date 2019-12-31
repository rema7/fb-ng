#!/bin/bash

#mkdir -p logs
#
pip install --pre -U -r /app/.meta/packages.dev

gunicorn app:app -c gunicorn.conf.py --reload --error-logfile $LOGS_PATH/vrways-error.log --access-logfile $LOGS_PATH/vrways-access.log --log-file $LOGS_PATH/vrways.log

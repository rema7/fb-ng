FROM python:3.8.1

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]
RUN ["apt-get", "install", "-y", "mc"]

RUN mkdir -p /app
WORKDIR /app
COPY . /app

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.6.0/wait /wait
RUN chmod +x /wait

RUN mkdir -p logs
RUN pip install --pre -U -r /app/.meta/packages

CMD /wait

CMD invoke init-config --db-connection="$DB_CONNECTION" --silent

CMD gunicorn app:app -c gunicorn.conf.py --reload --error-logfile $LOGS_PATH/error.log --access-logfile $LOGS_PATH/access.log --log-file $LOGS_PATH/main.log

FROM python:3.8.1

VOLUME ["/app"]
COPY start.sh /scripts/start.sh
WORKDIR /app

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.6.0/wait /wait
RUN chmod +x /wait

CMD /wait && /scripts/start.sh
#CMD /scripts/start.sh

#ENTRYPOINT [""]

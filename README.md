# Run

```bash
$ cd ./docker
$ docker-compose up
```

# Initializing 
```bash
$ docker exec -it fbng_backend bash
$ inv db.apply-migrations
```

# Fill test data 
```bash
$ docker exec -it fbng_backend bash
$ inv qa.generate-data
```
```
STOP SLAVE;
CHANGE MASTER TO MASTER_HOST='fbng_db', MASTER_USER='slave_user', MASTER_PASSWORD='db_pwd', MASTER_AUTO_POSITION=1;
START SLAVE;
```

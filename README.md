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

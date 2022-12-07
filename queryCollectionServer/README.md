# QueryCollection
This folder means to collect queries for VSCode text2command plugin development

# How to develop locally?

The query collection server and the plug-in itself can and should be developed separately,
so this README file will focus on how to set up and develop the query collection server locally.

1. Download and install the latest docker desktop from [the docker website](https://www.docker.com/products/docker-desktop/)

2. Then, you have to comment out the envionment variables that are used on production in the `backend/entrypoint.sh` file:

```
export USE_REMOTE_POSTGRESQL=1

export AZURE_POSTGRESQL_HOST=querycollectiondb.postgres.database.azure.com
export AZURE_POSTGRESQL_DATABASE=database
export AZURE_POSTGRESQL_USERNAME=service
export AZURE_POSTGRESQL_PASSWORD=PASSword123
export RUNNING_IN_PRODUCTION=1
```

3. Then, you have to uncomment the environment variables that are used in development in the same file:

```
# export LOCAL_HOST=pgsql
# export LOCAL_DATABASE=database
# export LOCAL_USERNAME=service
# export LOCAL_PASSWORD=password
```

4. Finally, open the docker desktop, in this folder, run `docker compose up`

5. After the server is up, you can go to http://127.0.0.1:8000/docs to test your API. If you need more details about this API,
please refer to [FastAPI](https://fastapi.tiangolo.com/)

6. To access the database, you can use your favorite DB managment system and connect to the `Postgres SQL` using the following info:

```
HOST: pgsql
DB: database
USERNAME: service
PASSWORD: password
PORT: 54320
```

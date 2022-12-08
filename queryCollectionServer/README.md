# QueryCollection
This folder means to collect queries for VSCode smart/fuzzy command search plugin

# How to develop locally?

The query collection server and the plug-in can and should be developed separately,
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

4. Finally, start the docker desktop, in this folder, run `docker compose up`

5. After the server is up, go to http://127.0.0.1:8000/docs to test the API. If you need more details about the API,
please refer to [FastAPI](https://fastapi.tiangolo.com/)

6. To access the database, open your favorite DB managment system and connect to the `Postgres SQL` using the following info:

```
HOST: localhost
DB: database
USERNAME: service
PASSWORD: password
PORT: 54320
```

P.S. You don't need the plugin to test the API. But if you want
to test whether the plugin works correctly or not, you need to change the API address to:

```
Create query: http://127.0.0.1:8000/createquery/
Update query: http://127.0.0.1:8000/updatequery/
```
Please refer to the `API_doc.docx` for more details.
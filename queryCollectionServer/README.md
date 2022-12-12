# QueryCollection
This folder means to collect queries for VSCode smart/fuzzy command search plugin

# How to develop locally?

The query collection server and the plug-in can and should be developed separately,
so this README file will focus on how to set up and develop the query collection server locally.

1. Download and install the latest docker desktop from [the docker website](https://www.docker.com/products/docker-desktop/)

2. Start the docker desktop, in this folder, run `docker compose up`

3. After the server is up, go to http://127.0.0.1:8000/docs to test the API. If you need more details about the API,
please refer to [FastAPI](https://fastapi.tiangolo.com/)

4. To access the database, open your favorite DB managment system and connect to the `Postgres SQL` using the following info:

```
HOST: localhost
DB: database
USERNAME: service
PASSWORD: password
PORT: 54320
```

P.S. You don't need the plugin to test the API. But if you want
to test whether the plugin works correctly or not locally, you need to change the API address in the plugin as follows:

Replace the Micrsoft Azure [createURL](https://github.com/SigmaWe/text2command/blob/f71fc51bc3b4105fbb02c3abb7ba5de2e6ac98f7/Plugin/text2command/src/basicInput.ts#L83) with the localhost one `http://127.0.0.1:8000/createquery/`

Replace the Micrsoft Azure [updateURL](https://github.com/SigmaWe/text2command/blob/main/Plugin/text2command/src/basicInput.ts#L32) with the localhost one `http://127.0.0.1:8000/updatequery/`

For how those two URL works, please refer to the `API_doc.docx` for more details.
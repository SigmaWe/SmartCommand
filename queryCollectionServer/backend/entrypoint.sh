#!/bin/bash

# export LOCAL_HOST=pgsql
# export LOCAL_DATABASE=database
# export LOCAL_USERNAME=service
# export LOCAL_PASSWORD=password

export USE_REMOTE_POSTGRESQL=1

export AZURE_POSTGRESQL_HOST=querycollectiondb.postgres.database.azure.com
export AZURE_POSTGRESQL_DATABASE=database
export AZURE_POSTGRESQL_USERNAME=service
export AZURE_POSTGRESQL_PASSWORD=PASSword123
export RUNNING_IN_PRODUCTION=1

exec "$@"
#!/usr/bin/env bash

set -ex

echo "$PWD"

readonly TAG_NAME=electiify-db
readonly CONTAINER_NAME=electiify-db-container

docker build -t $TAG_NAME .
docker rm -f $CONTAINER_NAME
docker run --name $CONTAINER_NAME -d -p 5432:5432 $TAG_NAME

sleep 2

export PGSERVICEFILE=.pg_service.conf
export PGPASSFILE=.pgpass
./manage.py makemigrations poll
./manage.py migrate
./manage.py runserver

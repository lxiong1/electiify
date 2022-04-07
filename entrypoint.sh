#!/usr/bin/env bash

set -ex

readonly TAG_NAME=electiify-db
readonly CONTAINER_NAME=electiify-db-container

docker build -t $TAG_NAME .

if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ];
then
  echo "Container $CONTAINER_NAME is already running"
else
  docker build -t $TAG_NAME .
  docker run --name $CONTAINER_NAME -d -p 5432:5432 $TAG_NAME
  sleep 1.5
fi

export PGSERVICEFILE=.pg_service.conf
export PGPASSFILE=.pgpass
./manage.py makemigrations polls
./manage.py migrate
./manage.py runserver

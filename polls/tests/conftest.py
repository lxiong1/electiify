from time import sleep
import docker
import pytest
from faker import Faker
from rest_framework.test import APIClient

import path


CONTAINER_NAME = "electiify-db-container"
TAG_NAME = "electiify-db"
PORT = "5432"


# TODO: Find better solution instead of hard-timed sleep to
#  give time for container to be in running state
@pytest.fixture(scope="session", autouse=True)
def db_container():
    client = docker.from_env()

    containers = client.containers.list(filters={"name": CONTAINER_NAME})
    if not containers:
        image = client.images.build(path=path.PROJECT_DIRECTORY, tag=TAG_NAME)
        client.containers.run(
            image[0],
            name=CONTAINER_NAME,
            detach=True,
            ports={f"{PORT}/tcp": PORT},
        )

        sleep(1.5)


@pytest.fixture
def faker():
    return Faker()


@pytest.fixture
def api_client():
    return APIClient()

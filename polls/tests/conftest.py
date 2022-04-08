import pytest
from faker import Faker
from rest_framework.test import APIClient


@pytest.fixture
def faker():
    return Faker()


@pytest.fixture
def api_client():
    return APIClient()

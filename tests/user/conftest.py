import pytest


@pytest.fixture
def base_url():
    return 'https://petstore.swagger.io'


@pytest.fixture
def headers():
    headers = \
        {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
    return headers

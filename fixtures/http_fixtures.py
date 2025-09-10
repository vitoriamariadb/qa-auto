import pytest
import requests


@pytest.fixture
def http_session():
    session = requests.Session()
    session.headers.update({"User-Agent": "qa-auto/1.0"})
    yield session
    session.close()


@pytest.fixture
def api_base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def api_timeout():
    return 30


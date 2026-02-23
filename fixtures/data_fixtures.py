import pytest
import json
from pathlib import Path


@pytest.fixture
def test_data_dir():
    path = Path(__file__).parent.parent / "data"
    path.mkdir(exist_ok=True)
    return path


@pytest.fixture
def sample_user():
    return {"id": 1, "name": "João Silva", "email": "joao@example.com", "active": True}


@pytest.fixture
def sample_users():
    return [
        {"id": 1, "name": "João Silva", "email": "joao@example.com"},
        {"id": 2, "name": "Maria Santos", "email": "maria@example.com"},
        {"id": 3, "name": "Pedro Costa", "email": "pedro@example.com"},
    ]

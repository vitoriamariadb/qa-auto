import pytest
import requests


@pytest.mark.api
def test_get_users(http_session, api_base_url):
    response = http_session.get(f"{api_base_url}/users")
    assert response.status_code == 200
    users = response.json()
    assert len(users) > 0
    assert "name" in users[0]
    assert "email" in users[0]


@pytest.mark.api
def test_get_user_by_id(http_session, api_base_url):
    user_id = 1
    response = http_session.get(f"{api_base_url}/users/{user_id}")
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == user_id


@pytest.mark.api
def test_create_user(http_session, api_base_url):
    new_user = {"name": "Novo Usuário", "email": "novo@example.com"}
    response = http_session.post(f"{api_base_url}/users", json=new_user)
    assert response.status_code == 201
    created_user = response.json()
    assert created_user["name"] == new_user["name"]
    assert created_user["email"] == new_user["email"]


@pytest.mark.api
def test_update_user(http_session, api_base_url):
    user_id = 1
    updated_data = {"name": "Nome Atualizado", "email": "atualizado@example.com"}
    response = http_session.put(f"{api_base_url}/users/{user_id}", json=updated_data)
    assert response.status_code == 200


@pytest.mark.api
def test_delete_user(http_session, api_base_url):
    user_id = 1
    response = http_session.delete(f"{api_base_url}/users/{user_id}")
    assert response.status_code == 200

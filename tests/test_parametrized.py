import pytest


@pytest.mark.parametrize(
    "num1,num2,resultado",
    [
        (1, 1, 2),
        (2, 3, 5),
        (10, 5, 15),
        (100, 200, 300),
    ],
)
def test_soma(num1, num2, resultado):
    assert num1 + num2 == resultado


@pytest.mark.parametrize(
    "texto,esperado",
    [
        ("hello", "HELLO"),
        ("world", "WORLD"),
        ("python", "PYTHON"),
        ("testing", "TESTING"),
    ],
)
def test_uppercase(texto, esperado):
    assert texto.upper() == esperado


@pytest.mark.parametrize(
    "lista,tamanho",
    [
        ([1, 2, 3], 3),
        ([1, 2, 3, 4, 5], 5),
        ([], 0),
        ([1], 1),
    ],
)
def test_tamanho_lista(lista, tamanho):
    assert len(lista) == tamanho


@pytest.mark.api
@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_get_multiple_users(http_session, api_base_url, user_id):
    response = http_session.get(f"{api_base_url}/users/{user_id}")
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == user_id


@pytest.mark.parametrize(
    "status_code,is_success",
    [
        (200, True),
        (201, True),
        (400, False),
        (404, False),
        (500, False),
    ],
)
def test_status_code_validation(status_code, is_success):
    assert (200 <= status_code < 300) == is_success

# Exemplos Práticos

## Exemplo 1: Teste de API Simples

```python
import pytest

@pytest.mark.api
def test_get_users(http_session, api_base_url):
    response = http_session.get(f"{api_base_url}/users")
    assert response.status_code == 200
    users = response.json()
    assert len(users) > 0
```

## Exemplo 2: Teste de UI com Page Object

```python
from pages.home_page import HomePage

@pytest.mark.ui
def test_home_page(browser, base_url):
    page = HomePage(browser, base_url)
    page.open()
    assert page.is_loaded()
    heading = page.get_heading_text()
    assert heading != ""
```

## Exemplo 3: Teste Parametrizado

```python
@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_get_user_by_id(http_session, api_base_url, user_id):
    response = http_session.get(f"{api_base_url}/users/{user_id}")
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == user_id
```

## Exemplo 4: Teste Data-Driven

```python
from utils.data_loader import load_users

@pytest.mark.parametrize("user", load_users())
def test_user_validation(user):
    assert "name" in user
    assert "email" in user
    assert "@" in user["email"]
```

## Exemplo 5: Teste Assíncrono

```python
import aiohttp

@pytest.mark.asyncio
async def test_async_api():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/users/1") as response:
            assert response.status == 200
            data = await response.json()
            assert "name" in data
```

## Exemplo 6: Fixture Customizada

```python
@pytest.fixture
def authenticated_session(http_session):
    http_session.headers.update({
        'Authorization': 'Bearer token123'
    })
    return http_session

@pytest.mark.api
def test_with_auth(authenticated_session, api_base_url):
    response = authenticated_session.get(f"{api_base_url}/protected")
    assert response.status_code == 200
```

## Exemplo 7: Teste com Setup e Teardown

```python
@pytest.fixture
def test_user(http_session, api_base_url):
    # Setup: criar usuário
    new_user = {"name": "Test User", "email": "test@example.com"}
    response = http_session.post(f"{api_base_url}/users", json=new_user)
    user = response.json()

    yield user

    # Teardown: deletar usuário
    http_session.delete(f"{api_base_url}/users/{user['id']}")

def test_user_operations(test_user):
    assert test_user["name"] == "Test User"
```

## Exemplo 8: Teste com Múltiplas Assertivas

```python
@pytest.mark.api
def test_user_complete_validation(http_session, api_base_url):
    response = http_session.get(f"{api_base_url}/users/1")

    # Status code
    assert response.status_code == 200

    # Response data
    user = response.json()

    # User structure
    assert "id" in user
    assert "name" in user
    assert "email" in user

    # Data types
    assert isinstance(user["id"], int)
    assert isinstance(user["name"], str)
    assert isinstance(user["email"], str)

    # Data validation
    assert user["id"] > 0
    assert len(user["name"]) > 0
    assert "@" in user["email"]
```

## Exemplo 9: Teste com Waits Customizados

```python
from selenium.webdriver.common.by import By
from utils.selenium_helpers import wait_for_element

@pytest.mark.ui
def test_dynamic_content(browser, base_url):
    browser.get(base_url)

    # Espera elemento aparecer
    element = wait_for_element(browser, (By.ID, "dynamic-element"), timeout=15)
    assert element is not None
    assert element.is_displayed()
```

## Exemplo 10: Teste de Performance Básico

```python
import time

@pytest.mark.slow
@pytest.mark.api
def test_api_response_time(http_session, api_base_url):
    start = time.time()
    response = http_session.get(f"{api_base_url}/users")
    end = time.time()

    duration = end - start

    assert response.status_code == 200
    assert duration < 2.0  # resposta em menos de 2 segundos
```

## Exemplo 11: Teste com Retry

```python
import time

@pytest.mark.api
def test_with_retry(http_session, api_base_url):
    max_retries = 3
    retry_count = 0

    while retry_count < max_retries:
        response = http_session.get(f"{api_base_url}/users")
        if response.status_code == 200:
            break
        retry_count += 1
        time.sleep(1)

    assert response.status_code == 200
```

## Exemplo 12: Geração de Relatório

```python
from utils.report_generator import ReportGenerator

def test_generate_report():
    generator = ReportGenerator()

    results = {
        "total": 50,
        "passed": 45,
        "failed": 5,
        "duration": 120.5
    }

    html_file = generator.generate_html(results)
    json_file = generator.generate_json(results)

    assert html_file.exists()
    assert json_file.exists()
```

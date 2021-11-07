# Guia de Uso - qa-auto

## Instalação

```bash
pip install -r requirements.txt
```

## Execução de Testes

### Todos os testes

```bash
pytest tests/ -v
```

### Apenas testes de API

```bash
pytest tests/ -m api -v
```

### Apenas testes de UI

```bash
pytest tests/ -m ui -v
```

### Com relatório HTML

```bash
pytest tests/ -v --html=reports/report.html --self-contained-html
```

ou use o script:

```bash
./run_tests.sh
```

## Interface TUI

Execute a interface interativa:

```bash
python tui.py
```

## Menu Principal

Execute o menu de opções:

```bash
python main.py
```

## Estrutura de Testes

### Testes de API

Localizados em `tests/test_api.py` e `tests/test_posts_api.py`.

Usam a fixture `http_session` para fazer requisições HTTP.

Exemplo:

```python
@pytest.mark.api
def test_get_users(http_session, api_base_url):
    response = http_session.get(f"{api_base_url}/users")
    assert response.status_code == 200
```

### Testes de UI

Localizados em `tests/test_ui.py`.

Usam a fixture `browser` que inicializa um WebDriver do Selenium.

Exemplo:

```python
@pytest.mark.ui
def test_page_title(browser, base_url):
    browser.get(base_url)
    assert "Example" in browser.title
```

### Testes Parametrizados

Testes com múltiplos valores de entrada.

Exemplo:

```python
@pytest.mark.parametrize("num1,num2,resultado", [
    (1, 1, 2),
    (2, 3, 5),
])
def test_soma(num1, num2, resultado):
    assert num1 + num2 == resultado
```

### Testes Data-Driven

Testes que carregam dados de arquivos JSON.

Os dados ficam em `data/users.json` e `data/api_endpoints.json`.

Exemplo:

```python
@pytest.mark.parametrize("user", load_users())
def test_user_data(user):
    assert "name" in user
```

### Testes Assíncronos

Testes que usam `async/await` para execução paralela.

Exemplo:

```python
@pytest.mark.asyncio
async def test_async_request():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            assert response.status == 200
```

## Fixtures

Fixtures reutilizáveis estão em `fixtures/`:

- `http_fixtures.py`: fixtures para testes de API
- `browser_fixtures.py`: fixtures para testes de UI
- `data_fixtures.py`: fixtures para dados de teste

## Page Object Model

Classes Page Object estão em `pages/`:

- `base_page.py`: classe base com métodos comuns
- `home_page.py`: exemplo de página específica

Exemplo de uso:

```python
page = HomePage(browser, base_url)
page.open()
heading = page.get_heading_text()
```

## Utilitários

Helpers e utilitários em `utils/`:

- `selenium_helpers.py`: funções auxiliares do Selenium
- `data_loader.py`: carregamento de dados JSON
- `report_generator.py`: geração de relatórios
- `async_runner.py`: execução assíncrona

## Relatórios

Relatórios são gerados em `reports/`:

- HTML: `pytest --html=reports/report.html`
- JSON: via `ReportGenerator`

## Markers

Markers disponíveis:

- `@pytest.mark.api`: testes de API
- `@pytest.mark.ui`: testes de UI
- `@pytest.mark.slow`: testes lentos
- `@pytest.mark.smoke`: testes de fumaça
- `@pytest.mark.asyncio`: testes assíncronos

## Configuração

Configurações em `pytest.ini`:

- Diretório de testes: `tests/`
- Padrão de arquivos: `test_*.py`
- Opções padrão: verbose, traceback curto

## Exemplos Práticos

Veja `docs/EXEMPLOS.md` para exemplos detalhados.

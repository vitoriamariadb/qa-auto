# FAQ - Perguntas Frequentes

## Como executar apenas testes rápidos?

```bash
pytest tests/ -m "not slow" -v
```

## Como executar testes em paralelo?

Instale pytest-xdist:

```bash
pip install pytest-xdist
pytest tests/ -n auto
```

## Como aumentar o timeout do Selenium?

Edite `fixtures/browser_fixtures.py` e altere o `implicitly_wait`:

```python
driver.implicitly_wait(30)  # 30 segundos
```

## Como usar um browser visível ao invés de headless?

Remova a opção `--headless` em `fixtures/browser_fixtures.py`:

```python
# options.add_argument('--headless')  # comentar esta linha
```

## Como adicionar novos dados de teste?

Crie ou edite arquivos JSON em `data/`:

```json
{
    "name": "Novo Teste",
    "value": "valor"
}
```

## Como criar uma nova fixture?

Adicione em `fixtures/` ou em `conftest.py`:

```python
@pytest.fixture
def minha_fixture():
    return "valor"
```

## Como debugar um teste?

Use `pytest --pdb` para abrir debugger em falhas:

```bash
pytest tests/test_api.py --pdb
```

## Como executar um teste específico?

```bash
pytest tests/test_api.py::test_get_users -v
```

## Como ver print statements durante testes?

```bash
pytest tests/ -v -s
```

## Como gerar coverage report?

Instale pytest-cov:

```bash
pip install pytest-cov
pytest tests/ --cov=. --cov-report=html
```

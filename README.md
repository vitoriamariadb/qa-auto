# qa-auto

Framework de automação de testes integrado com interface TUI.

## Descrição

Sistema de testes automatizados com suporte para:
- Testes de API REST
- Testes de interface UI (Selenium)
- Execução paralela e assíncrona
- Interface TUI interativa
- Relatórios HTML

## Requisitos

- Python 3.9+
- pip

## Instalação

```bash
pip install -r requirements.txt
```

## Uso

```bash
python main.py
```

## Estrutura

```
qa-auto/
├── tests/          # Testes automatizados
├── pages/          # Page Object Model
├── fixtures/       # Fixtures reutilizáveis
├── utils/          # Utilitários
└── reports/        # Relatórios gerados
```

## Licença

MIT

## Documentação

Para instruções detalhadas, consulte o [Guia de Uso](GUIA.md).

## Recursos

- Testes de API REST
- Testes de UI com Selenium
- Page Object Model
- Testes parametrizados
- Testes data-driven
- Execução assíncrona
- Interface TUI
- Relatórios HTML e JSON
- Fixtures reutilizáveis

## Comandos Rápidos

```bash
# Executar todos os testes
pytest tests/ -v

# Testes de API apenas
pytest tests/ -m api -v

# Testes de UI apenas
pytest tests/ -m ui -v

# Com relatório HTML
./run_tests.sh

# Interface TUI
python tui.py
```

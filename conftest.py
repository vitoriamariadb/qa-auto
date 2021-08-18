import pytest

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "api: testes de API REST"
    )
    config.addinivalue_line(
        "markers", "ui: testes de interface UI"
    )
    config.addinivalue_line(
        "markers", "slow: testes lentos"
    )
    config.addinivalue_line(
        "markers", "smoke: testes de fumaça"
    )

pytest_plugins = [
    "fixtures.http_fixtures",
    "fixtures.browser_fixtures",
    "fixtures.data_fixtures",
]

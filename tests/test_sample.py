import pytest


@pytest.mark.smoke
def test_exemplo():
    assert 1 + 1 == 2


def test_string():
    assert "qa-auto".upper() == "QA-AUTO"


def test_lista():
    dados = [1, 2, 3]
    assert len(dados) == 3
    assert 2 in dados

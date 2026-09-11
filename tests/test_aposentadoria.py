import pytest

from fincalc import calcular_aposentadoria


def test_aposentadoria_tempo_zero():
    # Arrange & Act
    resultado = calcular_aposentadoria(1000.0, 500.0, 0, 10.0)

    # Assert
    assert round(resultado, 2) == 1000.00


def test_aposentadoria_aporte_zero():
    # Arrange & Act
    resultado = calcular_aposentadoria(1000.0, 0.0, 2, 10.0)

    # Assert
    assert round(resultado, 2) == 1220.39


def test_aposentadoria_patrimonio_negativo():
    # Arrange, Act & Assert
    with pytest.raises(ValueError):
        calcular_aposentadoria(-1000.0, 500.0, 2, 10.0)


def test_aposentadoria_tempo_negativo():
    # Arrange, Act & Assert
    with pytest.raises(ValueError):
        calcular_aposentadoria(1000.0, 500.0, -1, 10.0)

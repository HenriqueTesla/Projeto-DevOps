import pytest

from fincalc import calcular_juros_simples


def test_juros_simples_valido():
    # Arrange & Act
    resultado = calcular_juros_simples(1000.0, 5.0, 2)

    # Assert
    assert round(resultado, 2) == 1100.00


def test_juros_simples_tempo_zero():
    # Arrange & Act
    resultado = calcular_juros_simples(1000.0, 5.0, 0)

    # Assert
    assert round(resultado, 2) == 1000.00


def test_juros_simples_capital_negativo():
    # Arrange, Act & Assert
    with pytest.raises(ValueError):
        calcular_juros_simples(-500.0, 5.0, 2)


def test_juros_simples_tempo_negativo():
    # Arrange, Act & Assert
    with pytest.raises(ValueError):
        calcular_juros_simples(1000.0, 5.0, -1)

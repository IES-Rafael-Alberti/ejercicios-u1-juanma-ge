import pytest
from src.ej05_def2 import calcular_precio

def test_calcular_precio():
    assert calcular_precio(12, 16) == 13.92
    assert calcular_precio(23, 21) == 27.83
    assert calcular_precio(14, 15) == 16.1
    assert calcular_precio(18, 20) == 21.6
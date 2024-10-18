

from src.ej02_def import calcular_importe

def test_calcular_importe():
    assert calcular_importe(1, 1) == 1
    assert calcular_importe(10, 5) == 50
    assert calcular_importe(0, 555) == 0
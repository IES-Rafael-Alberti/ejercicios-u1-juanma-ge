
import sys
import os
from src.prueba1 import comprobar_numero

# Agregar el directorio raíz del proyecto (practica6) al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_comprobar_numero():
    assert comprobar_numero(5, 3) == 5
    assert comprobar_numero(3, 5) == 5
    assert comprobar_numero(4, 4) == 0
    assert comprobar_numero(-1, -2) == -1
    assert comprobar_numero(-5, -5) == 0
    assert comprobar_numero(0, 0) == 0

import sys
import os
from src.ej01_def import saludar

# Agregar el directorio raíz del proyecto (practica6) al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_saludar():
    assert saludar("Diego") == "Hola, Diego."

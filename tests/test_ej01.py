import pytest
from src.ej01_def import saludar

def test_saludar():
    assert saludar("Juan") == "Hola, Juan."
    assert saludar("Luis") == "Hola, Luis."
    assert saludar("Mario") == "Hola, Mario."
    assert saludar("Diego") == "Hola, Diego."

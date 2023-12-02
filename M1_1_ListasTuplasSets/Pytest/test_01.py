
from M1_1_ListasTuplasSets.Programa_01 import duplicados
import pytest

# test_duplicados.py

def test_duplicados():
    assert duplicados(c=[1, 2, 3, 4, 5]) == False
    assert duplicados(c=[1, 2, 3, 4]) == True



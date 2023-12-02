from M1_1_ListasTuplasSets.Programa_05 import *
def test_media():
    pensionista = Grupo_Pensionista(1, 40, "100,200,300")
    assert pensionista.calcular_media_pagos() == 200.0

def test_edad():
    pensionista1 = Grupo_Pensionista(1, 40, "100,200,300")
    pensionista2 = Grupo_Pensionista(2, 50, "150,250,350")
    pensionistas = [pensionista1, pensionista2]
    assert pensionista1.calcular_media_edad_total(pensionistas) == 45.0

def test_pension():
    pensionista = Grupo_Pensionista(1, 40, "100,200,300")
    expected = "Identificador: 1, Edad: 40, Pagos: 100,200,300"
    assert str(pensionista) == expected

import pytest
from M1_2_RecoleccionDatos.Programa_10 import titanic

@pytest.mark.parametrize("test_input", ["https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/titanic.csv"])
def test_titanic(test_input, capsys):
    titanic()
    captured = capsys.readouterr()
    assert "Las dimensiones son" in captured.out
    assert "El numero de datos son" in captured.out
    assert "Nombres de columnas" in captured.out
    assert "Las primeras 10 filas son" in captured.out
    assert "Las ultimas 10 filas son" in captured.out
    assert "Porcentaje de personas vivas" in captured.out
    assert "Porcentaje de personas muertas" in captured.out
    assert "Porcentaje de personas vivas en cada clase" in captured.out

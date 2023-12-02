import pandas as pp
from M1_2_RecoleccionDatos import Programa_08


def test_balance():
    D1 = {
        "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
        "Ventas": [30500, 35600, 28300, 33900],
        "Gastos": [22000, 23400, 18100, 20700],
        "Balance": [8500, 12200, 10200, 13200],
    }
    df_al = pp.DataFrame(D1)

    res = Programa_08.balance()

    assert res.equals(df_al)


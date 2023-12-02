from M1_2_RecoleccionDatos import Programa_07

import pandas as pd



def test_ventas():
    D1 = {
        "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
        "Ventas": [30500, 35600, 28300, 33900],
        "Gastos": [22000, 23400, 18100, 20700],
    }
    df_al = pd.DataFrame(D1)
    res= Programa_07.ventas()

    assert res.equals(df_al)



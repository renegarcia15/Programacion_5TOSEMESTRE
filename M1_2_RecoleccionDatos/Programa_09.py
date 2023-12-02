""""Nombre: Rene Garcia Soto
    Grupo:951
    Fecha:26/08/23
    Descripcion:El archivo cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas:
    nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), Máximo (precio máximo de la acción durante la jornada),
    Mínimo (precio mínimo de la acción durante la jornada), volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros).
     Construir una función que construya un DataFrame a partir del archivo con el formato anterior y devuelve otro DataFrame con el mínimo,
     el máximo y la media de cada columna."""

import pandas as pd

def cotizacion():
    df_coti= pd.read_csv("https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/cotizacion.csv",sep=";", decimal=",")

    solo_numeros = df_coti.select_dtypes(include=['int64', 'float64'])

    mini = solo_numeros.min()
    maxi = solo_numeros.max()
    media = solo_numeros.mean()

    df_cotii = pd.DataFrame({
            'Minimo': mini,
            'Maximo': maxi,
            'Media': media
        })
    return print(df_cotii)

cotizacion()


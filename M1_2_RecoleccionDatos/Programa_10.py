""""Nombre: Rene Garcia Soto
    Grupo:951
    Fecha:26/08/23
    Descripcion:El archivo titanic.csv contiene información sobre los pasajeros del Titanic. Escribir un programa con los siguientes requisitos:
Generar un DataFrame con los datos del archivo.
Mostrar por pantalla las dimensiones del DataFrame.
Mostrar el número de datos que contiene, los nombres de sus columnas.
Mostrar las 10 primeras filas y las 10 últimas filas.
Mostrar por pantalla el porcentaje de personas que vivos y murieron.
Mostrar por pantalla el porcentaje de personas que vivos en cada clase.
"""


import pandas as pd

def titanic():
    james_cameron = pd.read_csv("https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/titanic.csv")

    print(james_cameron)

    print("Las dimensiones son ---> \n", james_cameron.shape)

    print("El numero de datos son ---> \n", james_cameron.size)

    print("Nombres de columnas ---> \n", james_cameron.columns)

    print("Las primeras 10 filas son ---> \n", james_cameron.head(10), "Las ultimas 10 filas son ---> \n", james_cameron.tail(10))

    pasajeros = len(james_cameron)
    vivos = james_cameron['Survived'].sum()
    muertos = pasajeros - vivos

    porcentaje_vivos = (vivos / pasajeros) * 100
    porcentaje_muertos = (muertos / pasajeros) * 100

    print(f"Porcentaje de personas vivas ---> {porcentaje_vivos:.2f}%")
    print(f"Porcentaje de personas muertas ---> {porcentaje_muertos:.2f}%")

    porcentaje_vivos_clase = james_cameron.groupby('Pclass')['Survived'].mean() * 100
    print("Porcentaje de personas vivas en cada clase ---> \n", porcentaje_vivos_clase)

titanic()


"""Alumno: Garcia Soto Rene Grupo: 951
Fecha:24/09/23
Descripcion: Escribir una función que reciba como parámetro una lista de números, y retorne una tupla.
El primer elemento de la tupla es la cantidad de números sin repetir de la lista, el segundo elemento de la tupla es la cantidad de números repetidos.
 Ejemplo: [1, 3, 1, 4, 5, 3, 7], resultado (3, 4). Ejemplo dos: [1, 3, 1, 1, 3, 4] , resultado (1, 5).
 Nota: Puede usar el método Count de las listas. Recibe de parámetro  el elemento que se desea contar.
"""


def repetidos(lista_01):
    elementos_unicos = set()
    repetidos = set()
    for elemento in lista_01:
        if elemento in elementos_unicos:
            repetidos.add(elemento)
        else:
            elementos_unicos.add(elemento)
    return (len(elementos_unicos), len(repetidos))

lista1 = [1, 3, 1, 4, 5, 3, 7]
resultado1 = repetidos(lista1)
print(resultado1)





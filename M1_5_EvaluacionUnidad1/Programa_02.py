"""Alumno: Garcia Soto Rene Grupo: 951
Fecha:24/09/23
Descripcion:Escribir una función que reciba como parámetro una lista de números. 
El método debe retornar una lista de booleanos, True si el número es divisible entre 5, False si es no es divisible. 
Ejemplo: [10, 3, 5, 9, 15, 1] retorna [True, False, True, False, True, False]. 
"""
def division_cinco(lista_01):
    res = []
    for numero in lista_01:
        if numero % 5 == 0:
            res.append(True)
        else:
            res.append(False)
    return res
ejemplo = [10,3,5,9,15,1]
res = division_cinco(ejemplo)
print(res)


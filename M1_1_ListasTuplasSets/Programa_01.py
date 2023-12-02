""""Nombre: Rene Garcia Soto
    Grupo:951
    Fecha:15/08/23
    Descripcion:Duplicados. Dada una lista de números enteros, retorna True si al menos un valor
    aparece dos veces, y Falso si todos los elementos son distintos.
"""
def duplicados(c):
    return len(c) != len(nums)
c = [1, 2, 3, 4, 5]
nums=set(c)

if duplicados(c):
    print("True")
else:
    print("False")
""""Nombre: Rene Garcia Soto
    Grupo:951
    Fecha:16/08/23
    Descripcion:Dado una lista de números enteros y un valor entero (target), retorna el
    índice de los dos números que sumados sean igual al target. Debe asumir que existe siempre
    una única solución, y que los elementos no se pueden usar dos veces. Debes retorna una tupla con los índices.
"""
def suma(nums, target):
    cont= len(nums)
    for i in range(cont):
        for x in range(i + 1, cont):
            if nums[i] + nums[x] == target:
                return (i, x)

t= [2, 7, 11, 15]
target= 9
indice= suma(t,target)

if indice:
    print(indice)


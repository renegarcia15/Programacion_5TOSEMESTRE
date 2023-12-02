import numpy as np

l1=[1,2,3,4,5]
n1=np.array(l1)#Tranforma cualquier lista en array
print(n1)

"""Principales atributos"""

print(n1.ndim) #Cantidad de dimensiones
print(n1.shape) #Dimensiones del arreglo, cuantas columnas y renglones tiene
print(n1.size) #Cantidad de elementos
print(n1.dtype) #Tipo de dato
"""DOS DIMENSI0NES"""
l2=[[1,2,3,4,5],[6,7,8,9,10]]
n2=np.array(l2)
print(n2)
print(n2.ndim) #Cantidad de dimensiones
print(n2.shape) #Dimensiones del arreglo, cuantas columnas y renglones tiene
print(n2.size) #Cantidad de elementos
print(n2.dtype) #Tipo de datos
#Acceso a los elementos
print(n2[1,2]) #El primer numero es el renglon y el segundo numero es la columna
print(n2*2)
print(n2+2)
print(n2-2)
print(np.linalg.norm(n2))#LINALG ES ALGEBRA LINEAL, SOLVE PUEDE RESOLVER ECUACIONES DE MUCHAS INCOGNITAS
print(n2.T)#T GRANDOTA es para transponer es decir de columna a renglon o de renglon a columna
print(n2[0,:].mean())
"""Ecuaciones
x-2y=1
3x+5y=2
"""
ecuaciones=[[1,2],[3,5]]

np_ec=np.array(ecuaciones)

res_ec=np.array([1,2])

print(np.linalg.solve(np_ec,res_ec))




import pandas as pd


D1={
   "nombres":["Maria","Luis","Carmen"],
   "materias":["matematicas","programacion","mercadotecnia"],
   "promedios":[80,90,100],
}

df_al=pd.DataFrame(D1)
print(df_al)
df_colesterol= pd.read_csv("https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesteroles.csv",sep=";", decimal=",")
print(df_colesterol)
print(df_colesterol.info())
print(df_colesterol.describe())

print(df_colesterol.shape)
print(df_colesterol.size)
print(df_colesterol.columns)
print(df_colesterol.dtypes)
print(df_colesterol.index)
print(df_colesterol.nombre) #Si ocupas mas de una columna serai ejemplo ([["nombre","edad"]])

print("THE END")

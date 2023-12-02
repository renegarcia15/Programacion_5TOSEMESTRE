import pandas as pd

datos = pd.read_csv("../DATA/surveys.csv")

nulos=datos.isnull() #Ver si hay nulos en los renglones
#print(nulos.any()) Sirve para ver si hay nulos en las columnas
#print(nulos.sum()) #Sirve para ver la cantidad de valores nulos en cada columna
#print(nulos.sum().sum()) #Valor total de los valores nulos (CONCATENACION)
#print(nulos.sum()/len(nulos)) #Porcentaje de valores nulos, si hay alto porcentaje en una columna de valores nulos es mejor darle cuello a esa columna

#Eliminar columnas
datos_eliminados=datos.drop(["day","month"],axis="columns",inplace=True)#Eliminar columnas, el inplace en True es para eliminarlo en el archivo original y NO EN UNA COPIA
print(datos.columns)

#Eliminar renglones
datos_row_eliminado=datos.drop([2,3,4],axis="index")

#print(datos_row_eliminado.head(10))

#Eliminar nulos
datos_noNA=datos.dropna(axis="index",subset=["hindfoot_length","sex"])
print(len(datos_noNA))
print(len(datos))

#Llenar valores nul0s
"""promedios=datos.mean()
print(promedios)"""
"""datos_llenos=datos.fillna("SIN DATA")
print(datos_llenos)"""
columnas=["hindfoot_length","weight"]
promedio=datos[columnas].mean
print(promedio)
datos_llenos=datos.fillna(promedio)
print(datos_llenos)

#llenar valores nulos usando mix
datos_bfill=datos.bfill().ffill()
print(datos_bfill)

#VERIFISRT FUPLIVSFPODS
datos.duplicated()
print(datos.duplicated())
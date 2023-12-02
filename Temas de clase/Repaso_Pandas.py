import pandas as pd

d={"articulo":["COCA","TOSTITOS","CHEETOS","JUGO"],
   "precio":[16,20,14,20],
   "costo":[8,10,7,10],
   "categoria":["Bebida","Snacks","Snacks","Bebida"]}

DATA= pd.DataFrame(d)
#print(DATA)

art=[
    ["Tostitos",20,10,"Snacks"],
    ["COCA",16,8,"Bebida"],
    ["CHEETOS",14,7,"Snacks"],
    ["JUGO",20,10,"Bebida"]
]
DATA_2=pd.DataFrame(art,columns=["articulo","precio","costo","categoria"])
#print(DATA.articulo)#Seleccionar columna
#print(DATA_2)
seleccionar_Varias_columnas=["articulo","precio"]
#print(DATA[seleccionar_Varias_columnas])

#Calcular las utilidades de cada producto(precio-costo)
utilidad=DATA.precio-DATA.costo
DATA["U T I L I D A D"]=utilidad
#print(DATA)

#Calcular el precio maximo de los articulos
"""precio_maximo=max(DATA.precio)
precio_filtrado=(DATA[DATA.precio==precio_maximo])
print(precio_filtrado)"""

#Calcular el precio mayor de la categoria bebidas
DATA_filtrado=DATA[DATA.categoria=="Bebida"]
precio_maximo=DATA_filtrado.precio.max()
precio_filtrado=(DATA.precio==precio_maximo) & (DATA.categoria=="Bebida")
print(DATA[precio_filtrado][seleccionar_Varias_columnas])

#Calcular max, min, mean de las columnas precio y costo, devolvervo en un Distrito Federal (DF)
columnas=["precio","costo"]
maxi=DATA[columnas].max()
mini=DATA[columnas].min()
promedio=DATA[columnas].mean()
res=pd.DataFrame([maxi,mini,promedio],index=["MAXIMO","MINIMO","PROMEDIO"])
print(res)
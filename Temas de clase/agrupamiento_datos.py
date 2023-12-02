import pandas as pd

data=pd.read_csv("../DATA/DATA_oliimpiadas.csv",
                 index_col=0)
datos_agrupados=data.groupby(["gender","country"])
#print(datos_agrupados.get_group("male"))
columnas=["gold","silver","bronze"]
"""res=datos_agrupados[columnas].sum()
res1=data.country.value_counts()"""
#res=data.sort_values("year",ascending=False)
#print(data.mean(numeric_only=True))
#print(data.describe().transpose())
gruposgender=data.groupby("gender")
print(gruposgender.sample(6))
#Galletas marias con yoghurt natural y fruta
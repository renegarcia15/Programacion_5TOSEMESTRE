import pandas as pd

def eliminar_porcentaje(df, maxi):
    if 0 <= maxi<= 1:
        porcentaje_nulo= df.isnull().mean()
        col= porcentaje_nulo[porcentaje_nulo >= maxi].index.tolist()
        df = df.drop(columns=col)
        return col
prueba=pd.read_csv("weekly_stocks.csv")

res=eliminar_porcentaje(prueba,0.5)
print(res)
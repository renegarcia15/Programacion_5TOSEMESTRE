import pandas as pd

def sustitucion(df, columnas, cadena):
    if cadena not in ["mean", "bfill", "ffill"]:
        raise ValueError("El método debe ser mean, bfill o ffill.")
    df[columnas] = df[columnas].fillna(method=cadena)
    return df

prueba=pd.read_csv("weekly_stocks.csv")

res=sustitucion(prueba,["MSFT","FB"],"ffill")
print(res)
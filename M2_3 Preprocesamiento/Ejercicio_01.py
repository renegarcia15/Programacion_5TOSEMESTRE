import pandas as pd
def porcentaje_nulos(df):
    porcentaje_nulo= df.isnull().mean() * 100
    return porcentaje_nulo

prueba=pd.read_csv("weekly_stocks.csv")

res=porcentaje_nulos(prueba)
print(res)
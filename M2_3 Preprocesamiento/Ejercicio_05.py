import pandas as pd

def eliminar_renglones(df):
    no_renglones = len(df)
    df = df.drop_duplicates()
    renglones_eliminados= no_renglones - len(df)
    return renglones_eliminados

prueba=pd.read_csv("weekly_stocks.csv")

res=eliminar_renglones(prueba)
print(res)
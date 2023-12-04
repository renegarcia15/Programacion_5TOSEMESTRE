import pandas as pd
def escalado_simple(df, columnas):
    for col in columnas:
        max_val = df[col].max()
        df[col] = df[col] / max_val
    return df

prueba=pd.read_csv("weekly_stocks.csv")
col=["MSFT","FB","AAPL"]
res=escalado_simple(prueba,col)
print(res)
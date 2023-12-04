import pandas as pd

def min_max(df, columnas):
    for col in columnas:
        min_val = df[col].min()
        max_val = df[col].max()
        df[col] = (df[col] - min_val) / (max_val - min_val)
    return df



prueba=pd.read_csv("weekly_stocks.csv")
col=["MSFT","FB","AAPL"]
res=min_max(prueba,col)
print(res)



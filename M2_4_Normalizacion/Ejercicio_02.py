import pandas as pd

def zscore(df, columnas):
    for col in columnas:
        mean_val = df[col].mean()
        std_val = df[col].std()
        df[col] = (df[col] - mean_val) / std_val
    return df

prueba=pd.read_csv("weekly_stocks.csv")
col=["MSFT","FB","AAPL"]
res=zscore(prueba,col)
print(res)



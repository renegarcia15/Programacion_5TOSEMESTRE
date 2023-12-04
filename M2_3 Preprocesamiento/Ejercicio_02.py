import pandas as pd

def no_renglones(df):
    clon= df[df.duplicated()]
    return len(clon)

prueba=pd.read_csv("weekly_stocks.csv")
res=no_renglones(prueba)
print(res)
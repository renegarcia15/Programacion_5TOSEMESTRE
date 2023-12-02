import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

data=pd.read_csv("../DATA/weekly_stocks.csv", parse_dates=True)

columnas=["MSFT","AAPL","FB"]

grafica_linea=px.line(data,x="Date",y=["MSFT","AAPL"],title="MICROSOFT STOCKS")

grafica_box=px.box(data,y=["MSFT","AAPL"],title="MICROSOFT CAJA Y BIGOTES")

grafica_Area=px.area(data,x="Date",y=["MSFT","AAPL","FB"],title="Grafica de area")

data["Date"]=pd.to_datetime(data["Date"])

data2=data.set_index("Date")
data_3months=data2.resample(rule="M").mean()[-3:]
data_3months=data_3months.reset_index()

grafica_barras=px.bar(data_3months,x="Date",y=columnas,title="Grafica de barras")

nbins_formula=int(len(data)**(1/2))
histograma=px.histogram(data,x="Date",y="MSFT",nbins=nbins_formula)

grafica_dispersion=px.scatter(data,x="Date",y=columnas,size="AAPL")


#DATAFRAME QUE YA ESTA AQUI
df_iris=px.data.iris()
fig_iris=px.scatter(df_iris,x="species",y="petal_length",size="petal_length",color="species")

df_tips=px.data.tips()
grafica_circulas=px.pie(df_tips,values="total_bill",names="day")
#Mostrar graficas
grafica_circulas.show()
"""fig_iris.show()"""
"""grafica_dispersion.show()"""
"""histograma.show()
grafica_barras.update_layout(xaxis_title="Mes",yaxis_title="DLLS")#ES ANTES DE GRAFICAR Y UDS LE PUEDEN HACER MODIFICACIONES A LA GRAFICA
grafica_barras.show()"""
"""grafica_Area.show()
grafica_linea.show()
grafica_box.show()"""
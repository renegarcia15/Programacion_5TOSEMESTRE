import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("../DATA/weekly_stocks.csv", parse_dates=True, index_col="Date")
#print(data.sample(5))


#grafica=data.plot(y="MSFT",figsize=(9,6))
#data.plot.line(y="MSFT",title="Microsoft Stocks",ylabel="USD",xlabel="Week",color="red")
#data.plot(kind="box",vert=False)
#data.plot(kind="area",y="MSFT")



"""data2=data.reset_index()
data2.plot(kind="scatter",x="Date",y="MSFT")
plt.show()"""

#10 DE NOVIEMBRE DEL 2023


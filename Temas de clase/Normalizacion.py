import pandas as pd

personas={"Salario":[20000,10000,40000,25000,60000],
          "Edad":[20,18,35,40,45]}

DATA=pd.DataFrame(personas)

#Calculo Z-SCORE=X=(xi-promedio)/std
prom_salario=DATA.Salario.mean()
std_salario=DATA.Salario.std()
DATA["zscore_salario"]=(DATA.Salario - prom_salario)/std_salario

prom_edad=DATA.Edad.mean()
std_edad=DATA.Edad.std()
DATA["zscore_edad"]=(DATA.Edad - prom_edad)/std_edad

#CALCULO MIN-MAX X=(xi-min)/(max-min)
min_salario=DATA.Salario.min()
max_salario=DATA.Salario.max()
DATA["Min-MAX_SALARIO"]=(DATA.Salario-min_salario)/(max_salario-min_salario)
min_edad=DATA.Edad.min()
max_edad=DATA.Edad.max()
DATA["Min-MAX_EDAD"]=(DATA.Edad-min_edad)/(max_edad-min_edad)
#ESCALADO SIMPLE X=Xi/Xmax
DATA["Escalado Salario"]=DATA.Salario/max_salario
DATA["Escalado Edad"]=DATA.Edad/max_edad
print(DATA)
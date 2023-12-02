import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

alumnos = {"nombre": ["            Octavio        ","       Josue          ","      Maria","     Selene"],
           "genero": ["IN","M","F","F"],
           "nivel escolar": ["Universidad","Universidad","Prepa","Secundaria"]
           }
data=pd.DataFrame(alumnos)
data["nombre"]=data.nombre.str.strip()
data["nom_min"]=data.nombre.str.lower()
data["nom_miy"]=data.nombre.str.upper()
data["X"]=data.nombre.str.replace("a","X")
#Metodos de filtros
start_m=data.nombre.str.startswith("M")
#print(start_m)
#print(data(start_m))
end_e=data.nombre.str.endswith("E")
#print(data[end_e])

#print(data)
one_hot_encoder=pd.get_dummies(data.genero)
encoder=OrdinalEncoder(categories=[["Secundaria","Prepa","Universidad"]])
encoder.fit(data[["nivel escolar"]])
data["educacion_encoder"]=encoder.transform(data[["nivel escolar"]])

print(data)
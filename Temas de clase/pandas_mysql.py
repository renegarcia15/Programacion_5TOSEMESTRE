import pandas as pd
from sqlalchemy import create_engine
from enum import Enum


class DATAbd(Enum):
    USER = "root"
    PASSWORD = "12345"
    NAME_BD = "olimpiadas"
    SERVER = "localhost"


cadena_conexion = f"mysql+mysqlconnector://{DATAbd.USER.value}:{DATAbd.PASSWORD.value}@{DATAbd.SERVER.value}/{DATAbd.NAME_BD.value}"
print(cadena_conexion)
engine = create_engine(cadena_conexion)
conexion = engine.connect()
print(conexion)

data_olimpiadas = pd.read_csv("../DATA/DATA_OLIMPIADAS.csv", index_col=0)
# print(data_olimpiadas.sample(5))
genders = data_olimpiadas.gender.unique()
print(genders)
df_genders = pd.DataFrame(genders, columns=["nombre"])
df_genders.to_sql("genero", conexion, if_exists="append", index=False)

query="select nombre from genero where nombre=%s"
parametros=("male",)
resultados=pd.read_sql(query,conexion,params=parametros)

print(resultados)
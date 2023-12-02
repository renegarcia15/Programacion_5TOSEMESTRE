import pandas as pd

alumnos={
    "nombre":["Juan","Maria","Pedro","Miguel"],
    "edad":[20,19,22,18],
    "carrera":["IN","C","NI","IN"],
    "promedio":[90,85,70,100]
}

df_alumnos=pd.DataFrame(alumnos)

#Tecnica 1: Filtrado de datos
c1=df_alumnos.promedio>80
data_c1=df_alumnos[c1]
#print(data_c1)

#And &, or | neg~

c2=(df_alumnos.promedio>80) & (df_alumnos.carrera=="IN")
data_c2=df_alumnos[c2]
data_c22=df_alumnos[c2][["nombre","carrera"]]
#print(data_c2)

#Tecnica 02: Busqueda por query
query1_c1=df_alumnos.query("promedio>80")
print(query1_c1)

condicion="promedio>80 and carrera=='IN'"
query2_c2=df_alumnos.query(condicion)
print(query2_c2)
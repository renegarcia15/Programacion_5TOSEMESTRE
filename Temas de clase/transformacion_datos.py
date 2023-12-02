
import pandas as pd

alumnos={
    "nombre":["Juan","Maria","Pedro","Miguel","tEST"],
    "edad":[20,19,22,18,20],
    "carrera":["IN","C","NI","IN",""],
    "promedio":[90,85,70,100,90]
}

df_alumnos=pd.DataFrame(alumnos)

carrera={
    "nombre":["IN","C","NI","A","I"],
    "alumnos":[190,1000,300,2000,60],
    "creditos":[352,350,360,326,340]
}

df_carrera=pd.DataFrame(carrera)

#MERGE INNER, LEFT, RIGHT, OUTER

DATA=pd.merge(df_alumnos,df_carrera,how="outer",left_on="carrera",right_on="nombre")



#C O N C A T E N A T I O N
alumnos2={
    "nombre":["Marcos","Efrain","Pedro","Miguel","tEST"],
    "edad":[20,19,22,18,20],
    "carrera":["IN","C","NI","IN",""],
    "promedio":[90,85,70,100,90]
}

df_alumnos2=pd.DataFrame(alumnos)

concat=pd.concat([df_alumnos2,df_alumnos],axis="columns")
print(concat)
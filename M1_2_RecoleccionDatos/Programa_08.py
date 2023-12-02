""""Nombre: Rene Garcia Soto
    Grupo:951
    Fecha:26/08/23
    Descripcion:Escribir una funcion que reciba un Dataframe con el formato del ejercicio anterior,
    una lista de meses y devuelva el balance (ventas-gastos) total en los meses indicados."""
import pandas as pp
import numpy as np
def balance():
   D1={
      "Mes":["Enero","Febrero","Marzo","Abril"],
      "Ventas":[30500,35600,28300,33900],
      "Gastos":[22000,23400,18100,20700],
   }
   df_al=pp.DataFrame(D1)
   df_al['Balance']=df_al["Ventas"]-df_al["Gastos"]
   return df_al
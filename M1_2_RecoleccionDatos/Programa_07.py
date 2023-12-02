""""Nombre: Rene Garcia Soto
    Grupo:951
    Fecha:26/08/23
    Descripcion:Escribir un programa que genere y muestre por pantalla un DataFrame."""

import pandas as pp

def ventas():
   D1={
      "Mes":["Enero","Febrero","Marzo","Abril"],
      "Ventas":[30500,35600,28300,33900],
      "Gastos":[22000,23400,18100,20700],
   }
   df_al=pp.DataFrame(D1)
   return df_al
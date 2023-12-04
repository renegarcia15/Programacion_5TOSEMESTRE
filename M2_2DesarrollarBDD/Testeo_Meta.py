from Ejercicio_01 import Mysqlconnect
from Ejercicio_02 import Paismysql
from Ejercicio_03 import OlimpiadasmySQL
from Ejercicio_04 import *

conexion= Mysqlconnect(host="localhost", user="root", password="12345", database="olimpiadas")
conexion.conectar()

pais = Paismysql(host="localhost", user="root", password="12345", database="olimpiadas")
insertar_pais = pais.insertar(1, "Mexico")
editar_pais=pais.editar("Puerto Rico")
eliminar_pais=pais.eliminar(1)
consultar_pais=pais.consultar("id=1")

genero=Genero(host="localhost", user="root", password="12345", database="olimpiadas")
insertar_genero=genero.insertar("Masculino")
editar_genero=genero.editar(1,"Femenino")
eliminar_genero=genero.eliminar(1,"Femenino")
consultar_genero=genero.consultar("id=1")

olimpiada=OlimpiadasmySQL(host="localhost", user="root", password="12345", database="olimpiadas")
insertar_olimpiada=olimpiada.insertar(1,2016)
editar_olimpiada=olimpiada.editar(2017)
eliminar_olimpiada=olimpiada.eliminar(1)
consultar_olimpiada=olimpiada.consultar("id=1")

resultado=ResultadosmySQL(host="localhost", user="root", password="12345", database="olimpiadas")
insertar_resultado=resultado.insertar(1,1,1,4,3,2)
editar_resultado=resultado.editar(2,2,2,2,5,3)
eliminar_resultado=resultado.eliminar(2,2,2)
consultar_resultado=pais.consultar("id=1")


conexion.desconectar()
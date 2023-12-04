import mysql.connector
from Ejercicio_01 import Mysqlconnect
from Ejercicio_02 import Paismysql
from Ejercicio_03 import OlimpiadasmySQL
class ResultadosmySQL(Mysqlconnect):
    def insertar(self, idOlimpiada, idPais, idGenero, oro, plata, bronce):
        try:
            conexion = self.conectar()
            if conexion:
                cursor = conexion.cursor()
                cursor.execute("select * from Olimpiada where id = %s", (idOlimpiada,))
                if not cursor.fetchone():
                    print("No existen las olimpiadas")
                    return False
                query = "insert into Resultados (idOlimpiada, idPais, idGenero, oro, plata, bronce) values (%s, %s, %s, %s, %s, %s)"
                values = (idOlimpiada, idPais, idGenero, oro, plata, bronce)
                cursor.execute(query, values)
                conexion.commit()
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print(f"no se inserto el resultado de las olimpiadas: {err}")
            return False
        finally:
            self.desconectar()

    def editar(self, idOlimpiada, idPais, idGenero, oro, plata, bronce):
        try:
            conexion = self.conectar()
            if conexion:
                cursor = conexion.cursor()
                if not all(isinstance(valor, int) and valor >= 0 for valor in [oro, plata, bronce]):
                    print("Las medallas deben de ser enteros!!!")
                    return False
                query = "update Resultados set oro = %s, plata = %s, bronce = %s where idOlimpiada = %s and idPais = %s and idGenero = %s"
                values = (oro, plata, bronce, idOlimpiada, idPais, idGenero)
                cursor.execute(query, values)
                conexion.commit()
                cursor.close()
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print(f"No se puede editar {err}")
            return False
        finally:
            self.desconectar()

    def eliminar(self, idOlimpiada, idPais, idGenero):
        try:
            conexion = self.conectar()
            if conexion:
                cursor = conexion.cursor()
                query = "delete from Resultados where idOlimpiada = %s and idPais = %s and idGenero = %s"
                values = (idOlimpiada, idPais, idGenero)
                cursor.execute(query, values)
                conexion.commit()
                cursor.close()
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print(f"NO se puede eliminar: {err}")
            return False
        finally:
            self.desconectar()

    def consultar(self, filtro):
        try:
            conexion = self.conectar()
            if conexion:
                cursor = conexion.cursor()
                query = f"select * from Resultados where {filtro}"
                cursor.execute(query)
                res = cursor.fetchall()
                return res
            else:
                return None
        except mysql.connector.Error as err:
            print(f"No hay nada para consultar por que: {err}")
            return []
        finally:
            self.desconectar()



class Genero(Mysqlconnect):
    def insertar(self, nombre):
        try:
            conexion = self.conectar()
            if conexion:
                cursor = conexion.cursor()
                query = "insert into Genero (nombre) values (%s)"
                values = (nombre,)
                cursor.execute(query, values)
                conexion.commit()
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print(f"No se insertó el género: {err}")
            return False
        finally:
            self.desconectar()

    def editar(self, id,nombre):
        try:
            conexion = self.conectar()
            if conexion:
                cursor = conexion.cursor()
                query = "update Genero set id = %s, nombre = %s where id = %s and nombre = %s "
                values = (id,nombre)
                cursor.execute(query, values)
                conexion.commit()
                cursor.close()
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print(f"No se puede editar {err}")
            return False
        finally:
            self.desconectar()

    def eliminar(self, id,nombre):
        try:
            conexion = self.conectar()
            if conexion:
                cursor = conexion.cursor()
                query = "delete from Genero where id = %s and nombre = %s"
                values = (id,nombre)
                cursor.execute(query, values)
                conexion.commit()
                cursor.close()
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print(f"NO se puede eliminar: {err}")
            return False
        finally:
            self.desconectar()

    def consultar(self, filtro):
        try:
            conexion = self.conectar()
            if conexion:
                cursor = conexion.cursor()
                query = f"select * from Genero where {filtro}"
                cursor.execute(query)
                res = cursor.fetchall()
                return res
            else:
                return None
        except mysql.connector.Error as err:
            print(f"No hay nada para consultar por que: {err}")
            return []
        finally:
            self.desconectar()

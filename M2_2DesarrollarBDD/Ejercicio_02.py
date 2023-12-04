import mysql.connector
from Ejercicio_01 import Mysqlconnect

class Paismysql(Mysqlconnect):
    def insertar(self, id, nombre):
        try:
            conexion = self.conectar()
            if conexion:
                cursor = conexion.cursor()
                cursor.execute("select * from Pais where id = %s", (id,))
                if cursor.fetchone():
                    print("Este pais ya existe:(")
                    return False

                query = "insert into Pais (id, nombre) values (%s, %s)"
                values = (id, nombre)
                cursor.execute(query, values)
                conexion.commit()
                cursor.close()
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print(f"No se pudo insertar el pais: {err}")
            return False
        finally:
            self.desconectar()

    def editar(self, nombre):
        try:
            conexion = self.conectar()
            if conexion:
                cursor = conexion.cursor()
                query = "update Pais set nombre = %s where nombre = %s"
                new_values = ("newname", nombre)
                cursor.execute(query, new_values)
                conexion.commit()
                cursor.close()
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print(f"Este pais no se puede editar: {err}")
            return False
        finally:
            self.desconectar()

    def eliminar(self, id):
        try:
            conexion = self.conectar()
            if conexion:
                cursor = conexion.cursor()
                query = "delete from pais where id = %s"
                value = (id,)
                cursor.execute(query, value)
                conexion.commit()
                cursor.close()
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print(f"este pais no se puede eliminar: {err}")
            return False
        finally:
            self.desconectar()

    def consultar(self, filtro):
        try:
            conexion = self.conectar()
            if conexion:
                cursor = conexion.cursor()
                query = f"select * from Pais where {filtro}"
                cursor.execute(query)
                res = cursor.fetchall()
                cursor.close()
                return res
            else:
                return None
        except mysql.connector.Error as err:
            print(f"No consultas del pais: {err}")
            return None
        finally:
            self.desconectar()

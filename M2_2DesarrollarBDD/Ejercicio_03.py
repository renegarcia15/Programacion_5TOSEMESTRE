import mysql.connector
from Ejercicio_01 import Mysqlconnect

class OlimpiadasmySQL(Mysqlconnect):
    def insertar(self, id, year):
        try:
            conexion = self.conectar()
            cursor = conexion.cursor()

            cursor.execute(f"select * from Olimpiada where year_olimpiada = {year}")
            res = cursor.fetchone()
            if res:
                return False

            cursor.execute(f"insert into Olimpiada (id, year_olimpiada) values ({id}, {year})")
            conexion.commit()
            return True
        except Exception as e:
            print(f"El año de esta olimpiada no se puede insertar: {e}")
            return False
        finally:
            self.desconectar()

    def editar(self, year):
        try:
            conexion = self.conectar()
            cursor = conexion.cursor()

            cursor.execute(f"select * from Olimpiada where year_olimpiada = {year}")
            res = cursor.fetchone()
            if res:
                return False
            cursor.execute(f"update Olimpiada set year_olimpiada = {year}")
            conexion.commit()
            return True
        except Exception as e:
            print(f"No puedes editar este año: {e}")
            return False
        finally:
            self.desconectar()

    def eliminar(self, id):
        try:
            conexion = self.conectar()
            cursor = conexion.cursor()

            cursor.execute(f"delete from Olimpiada where id = {id}")
            conexion.commit()
            return True
        except Exception as e:
            print(f"No puedes eliminar aqui: {e}")
            return False
        finally:
            self.desconectar()

    def consultar(self, filter):
        try:
            conexion = self.conectar()
            cursor = conexion.cursor()

            cursor.execute(f"select * from Olimpiada where {filter}")
            res = cursor.fetchall()
            return res
        except Exception as e:
            print(f"No se pueden consultar las olimpiadas: {e}")
            return []
        finally:
            self.desconectar()


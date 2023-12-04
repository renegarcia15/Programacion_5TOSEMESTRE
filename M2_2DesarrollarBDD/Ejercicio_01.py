import mysql.connector

class Mysqlconnect:
    def __init__(self, host, user, password, database):
        self._host = host
        self._user = user
        self._password = password
        self._database = database
        self._connection = None

    @property
    def host(self):
        return self._host

    @property
    def user(self):
        return self._user

    @property
    def password(self):
        return self._password

    @property
    def database(self):
        return self._database

    @property
    def connection(self):
        return self._connection

    @host.setter
    def host(self, value):
        self._host = value

    @user.setter
    def user(self, value):
        self._user = value

    @password.setter
    def password(self, value):
        self._password = value

    @database.setter
    def database(self, value):
        self._database = value

    def conectar(self):
        self._connection = mysql.connector.connect(
            host=self._host,
            user=self._user,
            password=self._password,
            database=self._database)
        return self._connection

    def desconectar(self):
        if self._connection:
            self._connection.close()
            self._connection = None

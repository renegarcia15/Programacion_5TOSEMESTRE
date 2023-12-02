from mysql.connector import connect, Error

try:
    db_conexion = connect(host="localhost", user="root", password="12345", database="olimpiadas")
    cursor = db_conexion.cursor()
    """
    sql="show databases"
    cursor.execute(sql)
    lista=cursor.fetchall()
    for i in lista:
        print (i)
    """
    # sql="insert into genero(nombre) values(%s)"
    sql = "update genero set nombre=%s where id=%s"
    val = [("FEMENINO", 2), ("Masculino",)]
    # val=[("Femenino",),("Masculino",)]
    cursor.execute(sql, val[0])  # SOOO EXECUTE ES PARA UNA VEZ OSEA UN SOLO DATO, MANY YA ES PARA VARIOS DATOS
    db_conexion.commit()  # SOLO SE USA CON INSERT, UPDATE Y DELETE
    print(cursor.lastrowid)
except Error as e:
    print(e)




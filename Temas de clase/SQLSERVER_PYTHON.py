#Instalen la libreria pywin32
import win32com.client
def insertar_datos():
    # Conexión a la base de datos con usuario y contraseña
    conn_str = "Provider=SQLOLEDB;Data Source=NOMBREDELSERVIDOR;Initial Catalog=Alumnoss;User ID=sa;Password=12345678;"
    conn = win32com.client.Dispatch("ADODB.Connection")
    conn.Open(conn_str)
    # Crear un objeto de comando
    cmd = win32com.client.Dispatch("ADODB.Command")
    cmd.ActiveConnection = conn
    sql = "INSERT INTO Estudiantes (nombre, carrera) VALUES (?, ?)"
    valor1 = "Marco"
    valor2 = "LIN"
    adVarChar = 200 # Este valor corresponde a adVarChar en ADO.NET
    adParamInput = 1 # Este valor corresponde a adParamInput en ADO.NET
    cmd.Parameters.Append(
        cmd.CreateParameter("@param1", adVarChar, adParamInput, len(valor1), valor1))
    cmd.Parameters.Append(
        cmd.CreateParameter("@param2", adVarChar, adParamInput, len(valor2), valor2))
    cmd.CommandText = sql
    cmd.Execute()
    conn.Close()
if __name__ == "__main__":
    insertar_datos()


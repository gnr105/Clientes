# pip install mysql-connector-python
import mysql.connector

class CConexion:

    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="clientesdb",
                port = "3306"
            )
            print("Conectado a la base de datos MySQL")
            return conexion
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos MySQL: {}".format(error))
            return None
    ConexionBaseDeDatos()
        
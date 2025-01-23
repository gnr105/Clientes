from Conexion import *

class CClientes:

    def mostrarClientes():
        try:

            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from usuarios;")

            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado
        
        except mysql.connector.Error as error:
            print("Error de Mostrar datos, error: {}".format(error))



    def ingresarClientes(nombre, apellido, sexo):

        try:

            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "insert into usuarios values(null, %s, %s, %s)"
            #La variable valores tiene que ser una tupla
            #Como minima expresion es:(valor,) La coma hace que sea una tupla
            #Las tuplas son listas inmutables, no se pueden modificar

            valores = (nombre, apellido, sexo)
            #Cursor execute va a unir la consulta sql con valores
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Cliente ingresado correctamente")
            cone.close()

        except mysql.connector.Error as error:
            print("Error al ingresar los clientes, error: {}".format(error))


    def modificarClientes(idUsuario, nombre, apellido, sexo):

        try:

            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "UPDATE usuarios SET usuarios.nombre = %s, usuarios.apellido = %s, usuarios.sexo = %s Where usuarios.id = %s;"
            valores = (nombre, apellido, sexo, idUsuario)
            #Cursor execute va a unir la consulta sql con valores
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro actualizado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de actualizacion de datos, error: {}".format(error))

    def eliminarClientes(idUsuario):

        try:

            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "DELETE from usuarios WHERE usuarios.id = %s;"
            valores = (idUsuario,)
            #Cursor execute va a unir la consulta sql con valores
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro Eliminado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de eliminacion de datos, error: {}".format(error))
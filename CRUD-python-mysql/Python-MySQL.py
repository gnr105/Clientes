import tkinter as tk

#Importar modulos restantes de tkinter
from tkinter import *

from tkinter import ttk
from tkinter import messagebox

from Clientes import *

from Conexion import *

class FormularioClientes: 

    global base
    base = None

    global texBoxId
    texBoxId = None

    global texBoxNombre
    texBoxNombre = None

    global texBoxApellido
    texBoxApellido = None

    global combo
    combo = None

    global groupBox
    groupBox = None

    global tree
    tree = None

def Formulario():

        global texBoxId
        global texBoxNombre
        global texBoxApellido
        global combo
        global base
        global tree
        global groupBox





        try:
            base = Tk()
            base.geometry("1200x300")
            base.title("Formulario Python")

            groupBox = LabelFrame(base, text="Datos del personal", padx=5, pady=5)
            groupBox.grid(row=0, column=0, padx=10, pady=10)

            labelId= Label(groupBox, text="Id:", width=13, font=("arial", 12)).grid(row=0, column=0)
            texBoxId = Entry(groupBox)
            texBoxId.grid(row=0, column=1)

            labelNombre= Label(groupBox, text="Nombre:", width=13, font=("arial", 12)).grid(row=1, column=0)
            texBoxNombre = Entry(groupBox)
            texBoxNombre.grid(row=1, column=1)

            labelApellido= Label(groupBox, text="Apellido:", width=13, font=("arial", 12)).grid(row=2, column=0)
            texBoxApellido = Entry(groupBox)
            texBoxApellido.grid(row=2, column=1)

            labelSexo= Label(groupBox, text="Sexo:", width=13, font=("arial", 12)).grid(row=3, column=0)
            seleccionSexo = tk.StringVar()
            combo = ttk.Combobox(groupBox,values=["Masculino", "Femenino"], textvariable=seleccionSexo)
            combo.grid(row=3, column=1)
            seleccionSexo.set("Masculino")

            Button(groupBox,text="Guardar", width=10, command=guardarRegistros).grid(row=4, column=0)
            Button(groupBox,text="Modificar", width=10, command= modificarRegistros).grid(row=4, column=1)
            Button(groupBox, text="Eliminar", width=10, command= eliminarRegistros).grid(row=4, column=2)

            groupBox = LabelFrame(base, text="Lista de Personal", padx=5, pady=5,)
            groupBox.grid(row=0, column=1, padx=5, pady=5)
            #Crear un TreeView

            #Configurar las columnas

            tree = ttk.Treeview(groupBox, columns=("Id", "Nombre", "Apellido", "Sexo"), show='headings', height=5,)
            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="Id")

            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2", text="Nombre")

            tree.column("# 3", anchor=CENTER)
            tree.heading("# 3", text="Apellido")

            tree.column("# 4", anchor=CENTER)
            tree.heading("# 4", text="Sexo")

            for row in CClientes.mostrarClientes():
                 tree.insert("", "end", values=row)

            #Ejecutar la funcion de hacer click y mostrar el resultado
            tree.bind("<<TreeviewSelect>>", seleccionarRegistro)

            tree.pack()

            base.mainloop()


        except ValueError as error:
            print ("Error al mostrar la interfaz, error: {}".format(error))

def guardarRegistros():
        global texBoxNombre, texBoxApellido, combo, groupBox

        try:
            #Verificar si los widgets estan inicializados
            if texBoxNombre is None or texBoxApellido is None or combo is None:
                print("Los widgets no estan inicializados")
                return

            nombres = texBoxNombre.get()
            apellidos = texBoxApellido.get()
            sexo = combo.get()

            CClientes.ingresarClientes(nombres, apellidos, sexo)
            messagebox.showinfo("Registro", "Registro exitoso")
            
            actualizarTreeView()
            #Limpiamos los campos

            texBoxNombre.delete(0, END)
            texBoxApellido.delete(0, END)

        except ValueError as error:
            print("Error ingresar los datos, error: {}".format(error))
def actualizarTreeView():
    global tree

    try:
          #Borrar todos los elementos actuales de los treeView
          tree.delete(*tree.get_children())
          #Mostrar los nuevos datos
          datos = CClientes.mostrarClientes()

          #Insertar los datos en el treeView
          for row in datos:
              tree.insert("", "end", values=row)

    except ValueError as error:
          print("Error al actualizar la tabla {}".format(error))
def seleccionarRegistro(event):
    try:
         itemSeleccionado = tree.focus()

         if itemSeleccionado:
            #Obtener el Id del elemento seleccionado
            values = tree.item(itemSeleccionado)['values']

            #Establecer los valores en los widgets Entry

            texBoxId.delete(0, END)
            texBoxId.insert(0, values[0])
            texBoxNombre.delete(0, END)
            texBoxNombre.insert(0, values[1])
            texBoxApellido.delete(0, END)
            texBoxApellido.insert(0, values[2])
            combo.set(values[3])

    except ValueError as error:
          print("Error al seleccionar el elemento, error: {}".format(error))

def modificarRegistros():
        global texBoxId, texBoxNombre, texBoxApellido, combo, groupBox

        try:
            #Verificar si los widgets estan inicializados
            if texBoxId is None or texBoxNombre is None or texBoxApellido is None or combo is None:
                print("Los widgets no estan inicializados")
                return

            idUsuario = texBoxId.get()
            nombres = texBoxNombre.get()
            apellidos = texBoxApellido.get()
            sexo = combo.get()

            CClientes.modificarClientes(idUsuario, nombres, apellidos, sexo)
            messagebox.showinfo("Modificar", "Actualizacion Exitosa")
            
            actualizarTreeView()
            #Limpiamos los campos

            texBoxId.delete(0, END)
            texBoxNombre.delete(0, END)
            texBoxApellido.delete(0, END)

        except ValueError as error:
            print("Error al modificar los datos, error: {}".format(error))

def eliminarRegistros():
        global texBoxId, texBoxNombre, texBoxApellido

        try:
            #Verificar si los widgets estan inicializados
            if texBoxId is None:
                print("Los widgets no estan inicializados")
                return

            idUsuario = texBoxId.get()

            CClientes.eliminarClientes(idUsuario)
            messagebox.showinfo("Eliminar", "Eliminacion Exitosa")
            
            actualizarTreeView()
            #Limpiamos los campos

            texBoxId.delete(0, END)
            texBoxNombre.delete(0, END)
            texBoxApellido.delete(0, END)

        except ValueError as error:
            print("Error ingresar los datos, error: {}".format(error))
Formulario()
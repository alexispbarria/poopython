import mysql.connector
conexion = mysql.connector.connect (host = "localhost", user = "root", passwd = "", database = "entrenamiento")
cursor1 = conexion.cursor()

class Agenda:

    def __init__(self):
        self.menuEleccion()

    def menuEleccion (self):
        print ("BIENVENIDOS A LA AGENDA DEL SISTEMA")
        print ("1)Nuevo Contacto\n 2)Ver Agenda\n 3)Actualizar Contacto\n 4)Borrar contacto\n 5)Salir")
        self.op = int(input("Seleccione la opción que desee: "))
        if self.op == 1:
            self.insertarDatos()
        elif self.op == 2:
            self.mostrarDatos()
        elif self.op ==3:
            self.actualizarDatos()
        elif self.op == 4:
            self.borrarDatos()
        elif self.op == 5:
            print ("ADIOS!")
            conexion.close()
    


    def insertarDatos (self):
        self.nombre = input("Ingrese el nombre de la persona que desea agendar: ")
        self.alias = input ("Ingrese el alias de la persona: ")
        self.telefono = int(input("Ingrese el teléfono de la persona: "))
        sql = "insert into agenda (nombre, alias, telefono) values (%s, %s, %s)"
        datos = (self.nombre, self.alias, self.telefono)
        cursor1.execute(sql, datos)
        cursor1.execute ("select * from agenda")
        for fila in cursor1:
            print (fila)
        conexion.commit()


    def mostrarDatos(self):
        cursor1.execute ("select * from agenda")
        for fila in cursor1:
            print (fila)

    def actualizarDatos(self):
        self.modificar = input ("Ingrese el nombre de la persona que desea modificar datos: ")
        self.nuevoalias = input("Ingrese el nuevo alias de la persona: ")
        self.nuevotel = input ("Ingrese el nuevo teléfono de la persona: ")

        cursor1.execute (f"UPDATE agenda set alias = '{self.nuevoalias}', telefono = '{self.nuevotel}' where nombre = '{self.modificar}'")
        cursor1.execute ("select * from agenda")
        for fila in cursor1:
            print (fila)
        conexion.commit()

    def borrarDatos(self):
        self.borrar = input("Ingrese el nombre de la persona que deseas eliminar de la agenda: ")
        cursor1.execute (f"delete from agenda where nombre = '{self.borrar}'")
        cursor1.execute ("select * from agenda")
        for fila in cursor1:
            print (fila)
        conexion.commit()








objeto1 = Agenda()

conexion.close()
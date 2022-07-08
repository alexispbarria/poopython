import mysql.connector
conexion = mysql.connector.connect (host = "localhost", user="root", passwd="", database= "last")
cursor1 = conexion.cursor()

class Agenda:

    def __init__(self):
        self.menuEleccion()

    def menuEleccion (self):
        print ("Bienvenido a la agenda")
        print ("1)Ingresar un contacto\n 2)Mostrar Agenda\n 3)Modificar un contacto\n 4)Eliminar un contacto\n 5)Buscar un contacto específico\n 6)SALIR")
        self.op = int(input("Ingrese una opción válida: "))
        while True:
            if self.op == 1:
                self.insertarAgenda()
                self.que = input("Desea otra operación?")
                if self.que == 's' or self.que == 'S':
                    self.menuEleccion()
                else:
                    break
            elif self.op == 2:
                self.mostrarDatos()
                self.que = input("Desea otra operación?")
                if self.que == 's' or self.que == 'S':
                    self.menuEleccion()
                else:
                    break
            elif self.op == 3:
                self.modificarDatos()
                self.que = input("Desea otra operación?")
                if self.que == 's' or self.que == 'S':
                    self.menuEleccion()
                else:
                    break
            elif self.op ==4:
                self.eliminarDatos()
                self.que = input("Desea otra operación?")
                if self.que == 's' or self.que == 'S':
                    self.menuEleccion()
                else:
                    break
            elif self.op ==5:
                self.buscarContacto()
                self.que = input("Desea otra operación?")
                if self.que == 's' or self.que == 'S':
                    self.menuEleccion()
                else:
                    break
            else:
                print("ADIOS")
                break
            break    
            


    def insertarAgenda(self):
        self.nombre = input("Ingrese el nombre de la persona que desea agendar: ")
        self.telefono = int(input("Ingrese el número telefónico: "))
        sql = "insert into agenda (nombre, telefono) values (%s, %s)"
        datos = (self.nombre, self.telefono)
        cursor1.execute (sql, datos)      
        conexion.commit()
    
    def mostrarDatos(self):
        cursor1.execute("select * from agenda")
        for fila in cursor1:
            print(fila)

    def modificarDatos(self):
        self.mod = input("Ingrese el nombre del contacto que desea modificar: ")
        self.nuevotel = int(input("Ingrese el nuevo número telefónico: "))
        cursor1.execute(f"update agenda set telefono = '{self.nuevotel}' where nombre = '{self.mod}'")
        conexion.commit()

    def eliminarDatos(self):
        self.borrar = input("Ingrese el nombre de la persona que desee eliminar: ")
        cursor1.execute(f"delete from agenda where nombre = '{self.borrar}'")
        conexion.commit()

    def buscarContacto (self):
        self.buscar = input("Ingrese el nombre de la persona que desee buscar: ")
        cursor1.execute(f"select * from agenda where nombre = '{self.buscar}'")
        for fila in cursor1:
            print(fila)
    


    

objeto1 = Agenda()
conexion.close()

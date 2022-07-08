#CRUD PASO A PASO

#1 DEFINIR CLASE

class Clientes: #crear clase clientes, para almacenar y mostrar datos (metodos)
    def __init__(self): 
        print ("BiENVENIDO AL SISTEMA DE GESTIÓN DE CLIENTES")
        self.guardarDatos() #ejecutar el metodo guardarDatos al iniciar el programa, sin llamarlo en el main.
    
    def guardarDatos(self):        
        self.rut = input("Ingrese rut: ")
        self.nombre = input ("Ingrese nombre: ")
        self.edad = int(input("Ingrese edad: "))
        self.categoria = input ("Ingrese categoría (PREFERENCIAL/ESTANDAR): ")

    def mostrarDatos (self):
        print ("*****DATOS CLIENTE*****")
        print ("RUT\tNOMBRE\tEDAD\tCATEGORÍA")
        print (f"{self.rut}\t{self.nombre}\t{self.edad}\t{self.categoria}")

    def modificarDatos (self):
        print ("DESEA MODIFICAR DATOS?")
        self.opcion = input("Ingrese si/no")
        if self.opcion == 'si':
            self.cambio = input("Ingrese el RUT de la persona a modificar: ")
            if self.cambio == self.rut:
                self.rut = input("Ingrese rut: ")
                self.nombre = input ("Ingrese nombre: ")
                self.edad = int(input("Ingrese edad: "))
                self.categoria = input ("Ingrese categoría (PREFERENCIAL/ESTANDAR): ")
        else:
            print ("NINGÚN DATO DE CLIENTE FUE MODIFICADO")
        self.mostrarDatos()
    
    def eliminarDatos (self):
        print ("DESEA ELIMINAR DATOS?")
        self.eliminar = input ("Ingrese si/no")
        if self.eliminar == 'si':
            self.eliminado = input("Ingrese el RUT de la persona a eliminar: ")
            if self.eliminado == self.rut:
                self.rut = " "
                self.nombre = " "
                self.edad = " "
                self.categoria = " "
        else:
            print ("NINGÚN DATO DE CLIENTE FUE ELIMINADO")
        self.mostrarDatos()



#main
objeto1 = Clientes()
objeto1.mostrarDatos()
objeto1.modificarDatos()
objeto1.eliminarDatos()
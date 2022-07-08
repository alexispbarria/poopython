class Clientes: #crear clase clientes, para almacenar y mostrar datos (metodos)
    
    def __init__(self): 
        print ("BiENVENIDO AL SISTEMA DE GESTIÓN DE CLIENTES")
        print ("Por favor, seleccione la opción que desea ejecutar")       
        self.listaRut = []
        self.listaNombre = []
        self.listaEdad = []
        self.listaCategoria = []
        self.menuEleccion()          

    def menuEleccion (self):
        print ("***************")
        print (" 1)GUARDAR DATOS\n 2)MODIFICAR DATOS\n 3)ELIMINAR DATOS\n 4)MOSTRAR DATOS\n 5)SALIR")
        self.eleccion = int(input("Ingrese una opción válida: "))
        while True:
            if self.eleccion == 1:
                self.guardarDatos()
                self.op = input("Desea realizar otra acción? si/no:  ")
                if self.op == 'si':
                    self.menuEleccion()
                else:
                    print ("¡HASTA LUEGO!")
                    break
            elif self.eleccion == 2:
                self.modificarDatos()
                self.op = input("Desea realizar otra acción? si/no:  ")
                if self.op == 'si':
                    self.menuEleccion()
                else:
                    print ("¡HASTA LUEGO!")
                    break           
            elif self.eleccion == 3:
                self.eliminarDatos()
                self.op = input("Desea realizar otra acción? si/no:  ")
                if self.op == 'si':
                    self.menuEleccion()
                else:
                    print ("¡HASTA LUEGO!")
                    break               
            elif self.eleccion == 4:
                self.mostrarDatos()
                self.op = input("Desea realizar otra acción? si/no:  ")
                if self.op == 'si':
                    self.menuEleccion()
                else:
                    print ("¡HASTA LUEGO!")
                    break
            else:
            
                break
    
    def guardarDatos(self):
        self.cantidad = int(input("Ingrese cantidad de registros: "))
        for i in range(self.cantidad):
            self.rut = input("Ingrese rut: ")
            self.listaRut.append(self.rut)
            self.nombre = input ("Ingrese nombre: ")
            self.listaNombre.append(self.nombre)
            self.edad = int(input("Ingrese edad: "))
            self.listaEdad.append(self.edad)
            self.categoria = input ("Ingrese categoría (PREFERENCIAL/ESTANDAR): ")
            self.listaCategoria.append(self.categoria)        
        
    def mostrarDatos (self):
        print ("*****DATOS CLIENTE*****")
        print ("RUT\tNOMBRE\tEDAD\tCATEGORÍA")
        for i in range (len(self.listaRut)): #Mostrar listas según su cantidad de elementos con len()
            print (f"{self.listaRut[i]}\t{self.listaNombre[i]}\t{self.listaEdad[i]}\t{self.listaCategoria[i]}")
    
    def modificarDatos (self):
        self.rutModificar = input("Ingrese rut del registro a modificar: ")
        if self.rutModificar in self.listaRut:
            print ("El registro existe")
            self.posicion = self.listaRut.index(self.rutModificar) #index muestra el indice de posicion en la lista
            print (f"el valor está en la posicion {self.posicion}") 
            self.listaRut[self.posicion] = self.rut = input("ingrese nuevo rut: ") #modificar la lista, según la posición dentro de ella.
            self.listaNombre[self.posicion] = self.nombre = input("Ingrese nuevo nombre: ")
            self.listaEdad[self.posicion] = self.edad = int(input("Ingrese nueva edad: "))
            self.listaCategoria[self.posicion] = self.categoria = input("Ingrese categoría (PREFERENCIAL/ESTANDAR): ")
        else:
            print ("No existe dicho registro")

    def eliminarDatos(self):
        self.borrar = input ("DESEA BORRAR TODOS LOS DATOS? SI/NO: ")
        if self.borrar == "si":
            self.listaRut.clear() #vaciar listas sin eliminarlas, del elimina la lista completa
            self.listaNombre.clear()
            self.listaEdad.clear()
            self.listaCategoria.clear()
        

#main
objeto1 = Clientes()

#AGREGAR MENU DE NAVEGACION, para que el usuario pueda elegir que quiera hacer.
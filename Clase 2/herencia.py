class Persona: #Clase Padre (da herencia)
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))
    def imprimir (self):
        print ("Nombre ",self.nombre)
        print ("Edad ",self.edad)

class Empleado(Persona): #Clase Hijo (recibe herencia)
    def __init__ (self):
        super().__init__() #llamar __init__ de la clase Padre -Persona-
        self.sueldo = float (input("Ingrese el sueldo: "))
    def imprimir (self):
        super().imprimir() #llamar imprimir de la clase Padre -Persona-
        print (f"Sueldo: {self.sueldo}")
    def pagaImpuestos(self):
        if self.sueldo > 3000:
            print ("El empleado paga impuestos")
        else:
            print ("No paga impuestos")

#MAIN

print("****************************")
empleado1 = Empleado()
empleado1.imprimir()
empleado1.pagaImpuestos()
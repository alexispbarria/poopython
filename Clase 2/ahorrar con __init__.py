class Persona: #class define el nombre de la clase
 
    def __init__(self): #AUTOMATIZAR PROCESOS
        self.nombre = input ("Ingrese nombre: ")
        self.edad = int(input ("Ingrese edad: "))
        self.imprimir()
        self.mayorEdad()

    def imprimir (self):
        print ("Nombre: ",self.nombre)
        print ("Edad: ",self.edad)
        
    def mayorEdad (self): #definir si es mayor de edad
        if self.edad > 17:
            print ("Es mayor de edad")
#main

persona1 = Persona()
persona2 = Persona()


class Persona: #class define el nombre de la clase
    def inicializar(self, nom, edad): #metodo
        self.nombre = nom
        self.edad =edad

    def imprimir (self):
        print ("Nombre: ",self.nombre)
        print ("Edad: ",self.edad)


#main

persona1 = Persona()
persona1.inicializar("Belen", "24")
persona1.imprimir()


persona2 = Persona()
persona2.inicializar("Juan", "25")
persona2.imprimir()

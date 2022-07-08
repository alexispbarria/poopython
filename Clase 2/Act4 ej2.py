#Plantear una clase llamada Jugador. 
#Definir en la clase Jugador los atributos nombre y puntaje, y los métodos __init__, imprimir 
#y pasar_tiempo (que debe reducir en uno la variable de clase). 
#Declarar dentro de la clase Jugador una variable de clase que indique cuantos minutos falta 
#para el fin de juego (iniciarla con el valor 30) 
#Definir en el bloque principal dos objetos de la clase Jugador. 
#Reducir dicha variable hasta llegar a cero. 

class Jugador:
    finJuego = 30
    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje
    
    def imprimir (self):
        print ("Nombre: ",self.nombre)
        print ("Puntaje: ",self.puntaje)
       
    
    def pasar_tiempo ():
        while Jugador.finJuego >= 0:
            print ("Tiempo Restante: ",Jugador.finJuego)
            Jugador.finJuego -= 1

jugador1 = Jugador("Alexis", 30)
jugador1.imprimir()



jugador2 = Jugador ("Andres", 20)
jugador2.imprimir()

Jugador.pasar_tiempo()




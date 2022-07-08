#Declarar  una  clase  Cuenta  y  dos  subclases  CajaAhorra  y  PlazoFijo.  Definir  los  atributos  y 
#métodos comunes entre una caja de ahorro y un plazo fijo y agruparlos en la clase Cuenta. 
#Una  caja de ahorro y un plazo fijo  tienen un nombre de titular y un monto. Un plazo fijo 
#añade un plazo de imposición en días y una tasa de interés. Hacer que la caja de ahorro no 
#genera intereses. 
#En  el  bloque  principal  del  programa  definir  un  objeto  de  la  clase  CajaAhorro  y  otro  de  la 
#clase PlazoFijo.

class Cuenta:
    def __init__(self):
        self.ntitular = input ("Ingrese el nombre del titular de cuenta: ")
        self.monto = int(input ("Ingrese monto: "))
        self.banco = input ("Ingrese un banco: ")
        self.edad = int(input("Ingrese edad: "))
        self.imprimir()
        self.mayorEdad()
    def mayorEdad (self):
        if self.edad >= 18:
            print ("Cuenta con mayoría de edad")
        else:
            print ("No puede acceder, debido a su menoría de edad.")
            exit
            
    def imprimir(self):
        print ("Nombre del titular: ",self.ntitular)
        print ("Monto ahorrado: ",self.monto)
        print ("Banco al que pertenece: ",self.banco)


class CajaAhorra:
    def __init__(self):
        super().__init__()
    def saldoAhorro(self):
        c = Cuenta()
        print ("El saldo ahorrado es de: ",c.monto)

class PlazoFijo:
    def __init__(self):
        super().__init__()
    
    def plazoImposicion (self):
        c = Cuenta()
        self.dias = int (input("Ingrese la cantidad de días para su plazo: "))
        if self.dias < 7:
            print ("El mínimo de días es de 7.")
        elif self.dias >= 7 and self.dias <= 125:
            self.calculo = c.monto * 0.008
            print ("Tu interés por los días seleccionado sería de: ",self.calculo)
        elif self.dias > 125 and self.dias <= 365:
            self.calculo = c.monto * 0.022
            print ("Tu interés por los días seleccionado sería de: ",self.calculo)
        else:
            print ("El máximo de días es 365.")

    

    

    

#MAIN 
print ("********** PLAZO FIJO ***********")
plazo1 = PlazoFijo()
plazo1.plazoImposicion()


print("*********** CAJA DE AHORRO ***********")
caja1 = CajaAhorra()
caja1.saldoAhorro()
class Operar ():
    def __init__ (self):
        self.valor1 = int(input("Ingrese un número: "))
        self.valor2 = int(input("Ingrese el segundo número"))
    def carga1 (self):
        self.carga1 = self.valor1
    def carga2 (self):
        self.carga2 = self.valor2

class Suma (Operar):
    
    def __init__(self):
        super ().__init__()
    def operar (self):
        op = Operar()
        self.sumar = op.valor1 + op.valor2
    def mostrar_resultado (self):
        print ("el resultado de la suma es: ",self.sumar)

class Resta (Operar):
    def __init__(self):
        super ().__init__()
    def operar (self):
        op = Operar()
        self.restar = op.valor1 - op.valor2
    def mostrar_resultado (self):
        print ("el resultado de la resta es: ",self.restar)

class Multiplicacion (Operar):
    def __init__(self):
        super ().__init__()
    def operar (self):
        op = Operar()
        self.multiplicar = op.valor1 * op.valor2
    def mostrar_resultado (self):
        print ("el resultado de la multiplicacion es: ",self.multiplicar)

class Division (Operar):
    def __init__(self):
        super ().__init__()
    def operar (self):
        op = Operar()
        self.dividir = op.valor1 / op.valor2
    def mostrar_resultado (self):
        print ("el resultado de la división es: ",self.dividir)

sum1 = Suma()
sum1.operar()
sum1.mostrar_resultado()

rest1 = Resta()
rest1.operar()
rest1.mostrar_resultado()

mul1 = Multiplicacion()
mul1.operar()
mul1.mostrar_resultado()

div1 = Division()
div1.operar()
div1.mostrar_resultado()


    

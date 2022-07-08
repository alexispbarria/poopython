class Cliente:
    suspendidos = []

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
    def imprimir (self):
        print ("codigo: ",self.codigo)
        print ("nombre: ",self.nombre)
        self.estaSuspendido()
    def estaSuspendido(self):
        if self.codigo in Cliente.suspendidos:
            print ("Está suspendido")
        else: 
            print ("No está suspendido")
    def suspender(self):
        Cliente.suspendidos.append(self.codigo)

#MAIN O BLOQUE PRINCIPAL #T ODO LO Q NO ESTA DENTRO DE UNA FUNCION O METODO

cliente1 = Cliente(1, "Juan")
cliente2 = Cliente(2, "Carlos")
cliente3 = Cliente(3, "Diego")
cliente4 = Cliente(4, "Pedro")

cliente1.suspender()

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

print (Cliente.suspendidos)

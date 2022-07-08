#Calcular e imprimir la tabla de multiplicar, 
# del 1 al 20 para un valor x ingresado por un usuario, 
# debe realizar el algoritmo mediante un ciclo FOR.

num = int(input("Ingrese un número: "))

for i in range (1, 20+1):
    multi= (num * i)
    print (num, "X", i, "=", multi)    

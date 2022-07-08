#Construya una función que muestre el digito menor de una decena ingresada, 
# en caso de que el número no sea de 2 dígitos o si son dígitos iguales como el 22 el programa dirá “Número no permitido” como mensaje.

def min ():
    for i in range (1, 9+1):
        num = int(input("Ingrese un número: "))
        if num < 10 or num == 11 or num == 22 or num == 33 or num == 44 or num == 55 or num == 66 or num == 77 or num == 88 or num == 99 or num >= 100:
            print ("Número no permitido")

#INCOMPLETO
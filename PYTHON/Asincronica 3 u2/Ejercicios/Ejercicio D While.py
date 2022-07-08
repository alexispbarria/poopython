#Diseñe un programa en python que cuente los números 
#pares e impares ingreasdos por un usuario de forma no definida, 
# (se pueden ingresar n cantidad de numeros para evaluar). 
# para finalizar el programa y obtener el resultado deberá 
# presionar la letra n, para seguir ingresando números 
# debe presionar cualquier tecla



pares=0
impares=0
while True:
    num = int (input("Ingrese números enteros \n"))
    if num%2==0: #evaluar si el numero es par
        pares=pares+1 #contabiliza pares
    else:
        impares=impares+1 #contabiliza impares
    op=input("""Desea continuar?
    presione: cualquier tecla, presione 'n' para salir \n""")
    if op == "n" or op =="N":
        break
print ("La cantidad de pares ingresados es: ", impares)
print ("La cantidad de impares ingresados es: ", impares)



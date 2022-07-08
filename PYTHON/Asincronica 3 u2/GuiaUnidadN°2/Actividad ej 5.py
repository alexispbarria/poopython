#Utilizando ciclo for, escriba un programa que 
# ingresado el nombre de una persona, 
#entregue las letras del nombre ordenadas de manera vertical (linea a linea). 
# Además el algoritmo entregará el número de letras del nombre, 
# en caso de que el nombre sea compuesto ej. Juan Carlos, no se contará 
# el espacio como letra por tanto el total de letras del nombre será 10.

nombre = input("Ingrese un nombre: ")
c=0
for i in (nombre):
    print (i)
    c=c+1
    if i == " ":
        c=c-1

print (c)

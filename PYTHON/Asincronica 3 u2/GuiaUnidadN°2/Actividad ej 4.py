#Utilizando ciclo for, escriba un programa que ingresado el 
# nombre de una persona 
#entregue como respuesta las letras del nombre tabuladas de forma horizontal

nombre = input("Ingresa el nombre \n ")


for i in (nombre):
    print (i, end="\t")
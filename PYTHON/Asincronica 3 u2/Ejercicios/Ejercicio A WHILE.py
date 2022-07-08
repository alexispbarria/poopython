#Disena un programa en Python que reciba un número mayor que 10
#e imprima todos los números pares entre 0 y el número

num=int(input("Ingrese un número mayor que 10 \n"))
if num <=10:
    print("El número debe ser mayor que 10")
    num=int(input("Ingrese un número mayor que 10 \n"))
cont=0
while cont <= num:
    print (cont)
    cont = cont+2
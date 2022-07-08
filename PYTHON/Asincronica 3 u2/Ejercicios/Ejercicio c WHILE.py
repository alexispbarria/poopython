#Programa que reciba dos números a y b, para saber cuál es mayor.
#Los números deben ser mayores a 0, el prog sabrá cuando es menor a 0.

num1=int(input("Ingrese el primer número: \n"))
num2=int(input("Ingrese el segundo número: \n"))
if num1 <= 0 or num2 <= 0:
    print ("el número ingresado debe ser mayor a 0, vuelva a ingresar")
elif num1 > num2:
    print("El número mayor es: ",num1)
else:
    print("El número mayor es: ",num2)
#Programa que pida 3 numeros
num1=float(input("Ingrese el primer número: "))
num2=float(input("Ingrese el segundo número: "))
num3=float(input("Ingrese el tercer número: "))

if num1 == num2 and num1 ==num3 and num2 == num3:
    print ("Los tres números son iguales")
elif num1 != num2 and num1 !=num3 and num2 !=num3:
    print ("Los tres son distintos")
else:
    print ("hay dos números iguales")

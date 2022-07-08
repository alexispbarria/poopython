#programa que pida al usuario dos numeros y muestre por pantalla su division, si div = 0 el programa muestra error
num1 = int(input("Ingrese el primer número: \n"))
num2 = int(input("Ingrese el divisor: \n"))

if num2 == 0:
    div=num1/num2
    print ("error")
else:
    print ("La división de los números corresponde a: ",div)

#numeros deben ser multiplos de 10

num= int(input("Ingrese un número: "))
if num % 10 == 0:
    print ("Acepta")
else:
    print ("Rechaza")
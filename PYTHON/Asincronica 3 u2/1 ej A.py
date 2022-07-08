# Mensaje de validación, numero natural y letra vocal

num = int(input("Escribir un número: "))
letra = input("Escribir una letra: ")
if num > 0 and letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print ("Acepta")
else:
    print ("Rechaza")

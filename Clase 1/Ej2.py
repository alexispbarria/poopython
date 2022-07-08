lista = []

repetido = []
for i in range (5):
    numero = int(input("Ingrese un numero: "))
    lista.append(numero)




norepe = []
repe = []
for x in lista:
    if x not in norepe:
        norepe.append(x)
    else:
        if x not in repe:
            repe.append(x)
print (f"los valores no repetidos son {norepe[:]}")
print (f"El número mayor de la lista es: {max(lista[:])}")
print (f"los números que se repiten son {repe[:]}")
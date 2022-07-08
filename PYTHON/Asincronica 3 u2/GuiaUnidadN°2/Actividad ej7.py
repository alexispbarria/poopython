#Sumar los números impares que existen entre 10 y 60.
acum = 0
for i in range (10, 60+1):
    if i%2!=0:
        acum=acum+i
        print (i)
print ("la suma de los numeros impares es: ", acum)
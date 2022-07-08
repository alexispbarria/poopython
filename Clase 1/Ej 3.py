paises = []
habitantes = []


for i in range (5):
    ingreso_paises = input ("Ingrese países para ingresar en la lista: ")
    paises.append (ingreso_paises)
for x in range (5):
    ingreso_habitantes = input("Ingrese la cantidad de habitantes por país: ")
    habitantes.append (ingreso_habitantes)

paises.sort()
habitantes.sort()

print (f"La lista ordenada alfabeticamente por países es {paises}, mientras que la lista ordenada de mayor a menor de habitantes es {habitantes}")

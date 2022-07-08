#Utilizando ciclo for, escriba un programa que muestre 
# la serie de exponentes  correspondiente a un byte (2^n). 
# El algoritmo mostrará el resultado de la suma de todos los exponentes.
sumatoria = 0
for i in range (0, 8):
    elevado= (2**i)
    sumatoria=sumatoria+elevado
    print (elevado)
    
print ("El resultado de la suma de los exponentes es: ",sumatoria)
    
    
    
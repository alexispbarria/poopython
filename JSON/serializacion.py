#Serialización
import json 


cadena1 = """
    [
        {
            "codigo" : "1",
            "descripcion" : "kiwi",
            "precio" : "1000"
        },
        {
            "codigo" : "2",
            "descripcion" : "palta",
            "precio" : "9000"
        }
    ]
"""    
print (type(cadena1)) #mostrar que tipo de dato es el codigo, en este caso el resultado arroja string 'str'
print (cadena1)
print ("_"*80)

lista = json.loads(cadena1) #cambio el tipo de dato de str a lista.
print (type(lista)) 
print (lista) #muestra el resultado como lista

#Lo anterior hecho es serializar, partimos con string y terminamos con list.

print ("_"*80)

#desserializar
cadena2 = json.dumps(lista) #dumps vuelve el tipo de codigo transformado de lista (primeramente era str luego list), por lo que la invierte volviendo a su inicio, manteniendo el orden visual
print (type(cadena2))
print (cadena2)

#realizar estos  2 puntos genera ventajas tanto estructural como visualmente.
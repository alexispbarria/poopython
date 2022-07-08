import json
cadena = """
[    
    {
        "codigo":"1", 
        "descripcion": "platano",
        "precio": "50"
    },
    {
        "codigo":"2", 
        "descripcion": "naranja",
        "precio": "60"
    },
    {
        "codigo":"3", 
        "descripcion": "guinda",
        "precio": "70"
    },
    {
        "codigo":"4", 
        "descripcion": "frutilla",
        "precio": "80"
    },
    {
        "codigo":"5", 
        "descripcion": "manzana",
        "precio": "90"
    },
    {
        "codigo":"6", 
        "descripcion": "kiwi",
        "precio": "40"
    }

]
"""
print (cadena)
lista = json.loads(cadena)
print (lista)
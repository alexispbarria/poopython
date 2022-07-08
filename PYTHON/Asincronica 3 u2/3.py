#Validad categoria del participante segun si año de nacimiento

nac=int(input("Ingrese el año de nacimiento: "))
edad=2021-nac

if edad < 18:
    print ("Participa en la categoría A")
elif edad >= 18 and edad <= 40:
        print("Participa en la categoría B")
else:
    print ("Participa en la categoria C")
   
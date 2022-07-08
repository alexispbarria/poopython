
while True:
    try:
        print ("ingrese notas del alumno 1")
        nota1=int(input("Ingrese la nota 1: "))
        nota2=int(input("Ingrese la nota 2: "))
        nota3=int(input("Ingrese la nota 3: "))
        while nota1 < 10 or nota1 > 70 or nota2 < 10 or nota2 > 70 or nota3 < 10 or nota3 >70:
            print ("Ingrese valores en el rango entre 10 y 70")
            nota1=int(input("Ingrese la nota 1: "))
            nota2=int(input("Ingrese la nota 2: "))
            nota3=int(input("Ingrese la nota 3: "))
        promedio1= nota1*0.5 + nota2*0.3 + nota3*0.2
        print ("el primedio final del primer alumno es: ",promedio1)
        break
    except ValueError:
        print ("ingrese valores enteros")

while True:
    try:
        print ("ingrese notas del alumno 2")
        nota1=int(input("Ingrese la nota 1: "))
        nota2=int(input("Ingrese la nota 2: "))
        nota3=int(input("Ingrese la nota 3: "))
        while nota1 < 10 or nota1 > 70 or nota2 < 10 or nota2 > 70 or nota3 < 10 or nota3 >70:
            print ("Ingrese valores en el rango entre 10 y 70")
            nota1=int(input("Ingrese la nota 1: "))
            nota2=int(input("Ingrese la nota 2: "))
            nota3=int(input("Ingrese la nota 3: "))
        promedio2= nota1*0.5 + nota2*0.3 + nota3*0.2
        print ("el primedio final del segundo alumno es: ",promedio2)
        break
    except ValueError:
        print ("ingrese valores enteros")

while True:
    try:
        print ("ingrese notas del alumno 3")
        nota1=int(input("Ingrese la nota 1: "))
        nota2=int(input("Ingrese la nota 2: "))
        nota3=int(input("Ingrese la nota 3: "))
        while nota1 < 10 or nota1 > 70 or nota2 < 10 or nota2 > 70 or nota3 < 10 or nota3 >70:
            print ("Ingrese valores en el rango entre 10 y 70")
            nota1=int(input("Ingrese la nota 1: "))
            nota2=int(input("Ingrese la nota 2: "))
            nota3=int(input("Ingrese la nota 3: "))
        promedio3= nota1*0.5 + nota2*0.3 + nota3*0.2
        print ("el primedio final del tercer alumno es: ",promedio3)
        break
    except ValueError:
        print ("ingrese valores enteros")

while True:
    try:
        print ("ingrese notas del alumno 4")
        nota1=int(input("Ingrese la nota 1: "))
        nota2=int(input("Ingrese la nota 2: "))
        nota3=int(input("Ingrese la nota 3: "))
        while nota1 < 10 or nota1 > 70 or nota2 < 10 or nota2 > 70 or nota3 < 10 or nota3 >70:
            print ("Ingrese valores en el rango entre 10 y 70")
            nota1=int(input("Ingrese la nota 1: "))
            nota2=int(input("Ingrese la nota 2: "))
            nota3=int(input("Ingrese la nota 3: "))
        promedio4= nota1*0.5 + nota2*0.3 + nota3*0.2
        print ("el primedio final del cuarto alumno es: ",promedio4)
        break
    except ValueError:
        print ("ingrese valores enteros")

while True:
    try:
        print ("ingrese notas del alumno 5")
        nota1=int(input("Ingrese la nota 1: "))
        nota2=int(input("Ingrese la nota 2: "))
        nota3=int(input("Ingrese la nota 3: "))
        while nota1 < 10 or nota1 > 70 or nota2 < 10 or nota2 > 70 or nota3 < 10 or nota3 >70:
            print ("Ingrese valores en el rango entre 10 y 70")
            nota1=int(input("Ingrese la nota 1: "))
            nota2=int(input("Ingrese la nota 2: "))
            nota3=int(input("Ingrese la nota 3: "))
        promedio5= nota1*0.5 + nota2*0.3 + nota3*0.2
        print ("el primedio final del quinto alumno es: ",promedio5)
        break
    except ValueError:
        print ("ingrese valores enteros")
promediocurso = (promedio1 + promedio2 + promedio3 + promedio4 + promedio5) /5
print ("el promedio final del curso es de: ",promediocurso)
mejorpromedio = (max (promedio1, promedio2, promedio3, promedio4, promedio5))
print ("el mejor promedio de los 5 alumnos es de: ",mejorpromedio)
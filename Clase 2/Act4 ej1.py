# Confeccionar una clase que administre una agenda personal. Se debe almacenar el nombre de la persona, teléfono y mail 
#Debe mostrar un menú con las siguientes opciones: 
#1- Carga de un contacto en la agenda.
#2- Listado completo de la agenda.
#3- Consulta ingresando el nombre de la persona.
#4- Modificación de su teléfono y mail
#5- Finalizar programa. 
class Contacto:
    def __init__(self, nombre, telefono, mail):
        self.nombre = nombre
        self.telefono = telefono
        self.mail = mail

class Agenda:
    def __init__(self):
        self.contactos = []

    def menu(self):
        print ("1- Carga de un contacto en la agenda.")
        print ("2- Listado completo de la agenda.")
        print ("3- Consulta ingresando el nombre de la persona.")
        print ("4- Modificación de su teléfono y mail")
        print ("5- Finalizar programa.")
        opcion = int(input("Escoja su opción: "))
        if opcion == 1:
            self.cargar()
        elif opcion == 2: 
            self.listado()
        elif opcion == 3:
            self.consultar()
        elif opcion == 4:
            self.modificar()
        else:
            print ("Hasta pronto")
    
    def cargar(self):
            nombreC = input ("Ingrese el nombre: ")
            telefonoC = int(input("Ingrese el número de teléfono: "))
            mailC = input("Ingrese el correo: ")
            c = Contacto(nombreC, telefonoC, mailC)
            self.contactos.append(c)
            self.menu()
    def listado(self):
        i = 0
        print ("| N°  |  Nombre  |  Teléfono  |  Mail|")
        for c in self.contactos:
            print (f"|{i+1}  |  {c.nombre}  |  {c.telefono}  |  {c.mail}|")
            i+=1
        self.menu()
    def consultar(self):
        op = input("Ingrese nombre a buscar: ")
        for c in self.contactos:
            if c.nombre == op:
                print (f"  |  {c.nombre}  |  {c.telefono}  |  {c.mail}|")
        self.menu()
    
    def modificar(self):
        self.listado()
        num = int(input("ingrese el número del contacto a editar: "))
        contacto = self.contactos[num-1]
        print ("2. Teléfono 3. Mail 4. Salir")
        op = int(input("Seleccione la opción que desea"))
        if op == 2:
            nuevotel = (int(input("Modifique el teléfono: ")))
            contacto.nombre = nuevotel
        elif op == 3:
            nuevomail = input("Modifique el nuevo correo: ")
            contacto.mail = nuevomail
        else:
            pass
        self.menu()

agenda1 = Agenda()
agenda1.menu()

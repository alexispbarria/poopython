import mysql.connector

conexion1 = mysql.connector.connect(host = "localhost",user="root",passwd="", database="basedatospython")
cursor1=conexion1.cursor()
cursor1.execute("show tables") #MOSTRAR TABLAS DE LA BD
for tabla in cursor1:
    print(tabla)
conexion1.close()

#DEMOSTRAR QUE ESTOY CONECTADO A UNA  BASE DE DATOS.
import mysql.connector #SIEMPRE DEBE ESTAR

conexion1 = mysql.connector.connect(host = "localhost",user="root",passwd="", database="basedatospython") #SIEMPRE DEBE ESTAR
cursor1=conexion1.cursor() #SIEMPRE DEBE ESTAR

cursor1.execute ("select * from articulos")

for fila in cursor1:
    print(fila)
conexion1.close() #SIEMPRE DEBE ESTAR
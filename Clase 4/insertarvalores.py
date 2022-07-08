import mysql.connector #SIEMPRE DEBE ESTAR

conexion1 = mysql.connector.connect(host = "localhost",user="root",passwd="", database="basedatospython") #SIEMPRE DEBE ESTAR
cursor1=conexion1.cursor() #SIEMPRE DEBE ESTAR
#INSERTAR FILAS
sql = "insert into articulos (descripcion, precio)values(%s, %s)" #EN QUE COLUMNA INSERTAR
datos =("naranja", 23.50) #QUÉ VALORES INSERTAR
cursor1.execute(sql, datos)
datos =("platano", 55.50)
cursor1.execute(sql, datos)
datos =("peras", 77.50)
cursor1.execute(sql, datos) #EJECUTAR INSERT INTO + datos
conexion1.commit() #SIEMPRE DEBE ESTAR CUANDO SE EJECUTA UN CRUD (INSERT,DELETE, UPDATE ETC.)

cursor1.execute("show tables")
for tabla in cursor1:
    print(tabla)
conexion1.close() #SIEMPRE DEBE ESTAR

#una vez ejecutado, revisar BD para corroborar que se agregaaron los datos ingresados.
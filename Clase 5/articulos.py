import mysql.connector

class Articulos:
    def abrir(self): #abrir bd
        conexion = mysql.connector.connect(host ="localhost",user="root",passwd="", database="basedatospython")
        return conexion

    def alta (self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into articulos(descripcion, precio) values (%s, %s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
    
    def consulta (self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql ="select descripcion, precio from articulos where codigo = %s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()
    
    def recuperar_todos (self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql ="select codigo, descripcion, precio from articulos"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall() #permite devolver componentes que estamos buscando
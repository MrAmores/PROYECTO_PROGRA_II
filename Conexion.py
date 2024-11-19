import mysql.connector
def conexionDB():
    conexion = mysql.connector.connect(
        host= '127.0.0.1',
        user ='root',
        password = '2006',
        port= '3306',
        database= 'crucero'
    ) 
    return conexion
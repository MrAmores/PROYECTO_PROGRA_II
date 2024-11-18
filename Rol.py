from Conexion import conexionDB
from Validaciones import validaString, validaFloatPositivo

class Rol():
    conexion = conexionDB()  # Se establece una única conexión para toda la clase
    miconexion = conexion.cursor()
    
    def __init__(self, idRol, nombre, descripcion, departamento, salario):
        self.idRol = idRol
        self.nombre = nombre
        self.descripcion = descripcion
        self.departamento = departamento
        self.salario = salario

    #We capture data to insert it
    def capturaNuevoR(self):
        self.idRol = validaString("Digite el ID del rol: ")
        self.nombre = validaString("Digite el nombre del rol: ")
        self.descripcion = validaString("Digite la descripción del rol: ")
        self.departamento = validaString("Digite el departamento del rol: ")
        self.salario = validaFloatPositivo("Digite el salario:")

    #Query to insert new data into the database
    def ingresaRol(self):
        ingreso = "INSERT INTO rol (idRol, nombre, descripcion, departamento, salario) VALUES (%s, %s, %s, %s, %s)"
        datos = (self.idRol, self.nombre, self.descripcion, self.departamento, self.salario)
        Rol.miconexion.execute(ingreso, datos)
        Rol.conexion.commit()
        print("Se ha ingresado el rol exitosamente.")

    # We capture data to do modifications
    def capturaModR(self, id):
        # We get the current data of the worker with the given ID
        Rol.miconexion.execute("SELECT * FROM rol WHERE idRol = '%s'" % id)
        datos = Rol.miconexion.fetchone()

        # Prints the current data
        print(f"Datos actuales del rol: {datos}")

        # New data validation
        nombre = validaString("Digite el nombre del rol: ")
        descripcion = validaString("Digite la descripción del rol: ")
        departamento = validaString("Digite el departamento del rol: ")
        salario = validaFloatPositivo("El salario debe ser un número positivo.")

        # We call the method to update data
        self.modificaRol(nombre, descripcion, departamento, salario, id)

    # Query to uptade existing data in the database
    def modificaRol(self, nombre, descripcion, departamento, salario, id):
        modificar = ("update rol set nombre = %s, "
                     "descripcion = %s, "
                     "departamento = %s,"
                     "salario = %s"
                     "where idRol = %s")
        datos = (nombre, descripcion, departamento, salario, id)
        Rol.miconexion.execute(modificar, datos)
        Rol.conexion.commit()
        print("Se han modificado los datos del rol exitosamente.")

    #Prints all information in the database
    def listaRol(self):
        print("Listado de roles en el sistema:")
        print("ID, NOMBRE, DESCRIPCIÓN, DEPARTAMENTO, SALARIO")
        Rol.miconexion.execute("select * from rol")
        datos = Rol.miconexion.fetchall()
        for i in datos:
            print(i)

    #Query to "delete" data from the database
    def BorraRol(self, id):
        Rol.miconexion.execute("DELETE FROM rol where idRol =  '%s'" % id)
        Rol.conexion.commit()
        print("Se ha borrado el rol exitosamente.")

    # Prints and returns all the information in the database
    def returnListaRol(self):
        print("Listado de roles en el sistema:")
        print("ID, NOMBRE")
        Rol.miconexion.execute("SELECT idRol, nombre FROM rol;")
        datos = Rol.miconexion.fetchall()
        for i in datos:
            print(i)
        return datos
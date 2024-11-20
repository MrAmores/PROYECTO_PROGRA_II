from Conexion import conexionDB
from Validaciones import validaString, validaFloatPositivo, validaIntPositivo

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
        while True:
            self.idRol = validaIntPositivo("Digite el ID del rol: ")
            Rol.miconexion.execute("SELECT COUNT(*) FROM rol WHERE idRol = %s", (self.idRol,))
            if Rol.miconexion.fetchone()[0] > 0:
                print("\n----El ID del rol ya existe. Por favor, ingrese un ID único----\n")
            else:
                break
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
        salario = validaFloatPositivo("Digite el salario: ")

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
        if not datos:  # If the list is empty
            print("No se encuentran roles en el sistema.")
        else:
            for i in datos:
                print(i)

    # Prints and returns all the information in the database
    @staticmethod
    def returnListaRol():
        # Captures data
        Rol.miconexion.execute("SELECT * FROM rol;")
        datos = Rol.miconexion.fetchall()
        return datos

    def obtenerTrabajadoresActivos(self, idRol):
        try:
            # Ejecuta la consulta para contar las personas activas con el idRol recibido como parámetro
            consulta = ("SELECT COUNT(*) FROM trabajador WHERE idRol = %s AND activo = %s")
            Rol.miconexion.execute(consulta, (idRol, True))  # Cambiado para pasar como tupla
            datos = Rol.miconexion.fetchone()
            print(f"cantidad activos ahora es {datos[0]}")  # Cambiado para acceder al primer elemento

            if datos[0] > 0:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error en obtenerTrabajadoresActivos: {e}")
            return False

    def BorraRol(self, id):
        try:
            # Verificar si hay trabajadores activos con el idRol que se desea borrar
            trabajadoresActivos = self.obtenerTrabajadoresActivos(id)

            if trabajadoresActivos:
                print("No se puede borrar el rol. Hay trabajadores activos asociados a este rol.")
            else:
                # Proceder a borrar el rol si no hay trabajadores activos
                consulta = "DELETE FROM rol WHERE idRol = %s"
                Rol.miconexion.execute(consulta, (id,))  # Esto está correcto
                Rol.miconexion.commit()
                print("Se ha borrado el rol exitosamente.")
        except Exception as e:
            print("Ocurrió un error al intentar borrar el rol:", e)



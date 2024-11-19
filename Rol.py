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
        self.idRol = validaIntPositivo("Digite el ID del rol: ")
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

    """def BorraRol(self, id):
        try:
            # Verificar si hay trabajadores activos con el idRol que se desea borrar
            consulta = "SELECT COUNT(*) FROM trabajador WHERE idRol = %s AND activo = 1"
            datos = (id, 1)  # 1 representa True en MySQL
            Rol.miconexion.execute(consulta, datos)
            trabajadoresActivos = Rol.miconexion.fetchone()[0]  # Recuperar el conteo

            if trabajadoresActivos > 0:
                print("No se puede borrar el rol. Hay trabajadores activos asociados a este rol.")
            else:
                # Proceder a borrar el rol si no hay trabajadores activos
                Rol.miconexion.execute("DELETE FROM rol WHERE idRol = %s", (id,))
                Rol.conexion.commit()
                print("Se ha borrado el rol exitosamente.")
        except Exception as e:
            print("Ocurrió un error al intentar borrar el rol:", e)
    """

    def BorraRol(self, id):
        cursor = None  # Inicializamos cursor fuera del bloque try
        try:
            # Crear un cursor explícito
            cursor = Rol.miconexion.cursor()

            # Validar que el rol existe
            consulta_verificar_rol = "SELECT COUNT(*) FROM rol WHERE idRol = %s"
            cursor.execute(consulta_verificar_rol, (id,))
            existe_rol = cursor.fetchone()[0]

            if existe_rol == 0:
                print(f"No se puede borrar el rol con idRol {id} porque no existe en la base de datos.")
                return

            # Verificar si hay trabajadores activos con el idRol que se desea borrar
            consulta = "SELECT COUNT(*) FROM trabajador WHERE idRol = %s AND activo = %s"
            datos = (id, 1)  # 1 representa True en MySQL
            cursor.execute(consulta, datos)
            trabajadoresActivos = cursor.fetchone()[0]  # Recuperar el conteo

            # Depuración: Mostrar conteo de trabajadores activos
            print(f"Trabajadores activos encontrados con idRol {id}: {trabajadoresActivos}")

            if trabajadoresActivos > 0:
                print("No se puede borrar el rol. Hay trabajadores activos asociados a este rol.")
            else:
                # Proceder a borrar el rol si no hay trabajadores activos
                cursor.execute("DELETE FROM rol WHERE idRol = %s", (id,))
                Rol.conexion.commit()
                print("Se ha borrado el rol exitosamente.")
        except Exception as e:
            print("Ocurrió un error al intentar borrar el rol:", e)
        finally:
            # Cerrar el cursor solo si se creó correctamente
            if cursor:
                cursor.close()

    # Prints and returns all the information in the database
    @staticmethod
    def returnListaRol():
        # Captures data
        Rol.miconexion.execute("SELECT * FROM rol;")
        datos = Rol.miconexion.fetchall()
        return datos
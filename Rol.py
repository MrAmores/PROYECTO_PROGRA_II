from Conexion import conexionDB
from Validaciones import validaString, validaFloatPositivo, validaIntPositivo

class Rol:
    conexion = conexionDB()  # Establish a single database connection for the class
    miconexion = conexion.cursor()

    def __init__(self, idRol, nombre, descripcion, departamento, salario):
        # Initializes a Rol object with ID, name, description, department, and salary
        self.idRol = idRol
        self.nombre = nombre
        self.descripcion = descripcion
        self.departamento = departamento
        self.salario = salario

    def capturaNuevoR(self):
        # Captures data for a new role and validates each field
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
        self.salario = validaFloatPositivo("Digite el salario: ")

    def ingresaRol(self):
        # Inserts a new role into the database
        ingreso = "INSERT INTO rol (idRol, nombre, descripcion, departamento, salario) VALUES (%s, %s, %s, %s, %s)"
        datos = (self.idRol, self.nombre, self.descripcion, self.departamento, self.salario)
        Rol.miconexion.execute(ingreso, datos)
        Rol.conexion.commit()
        print("\n==================================")
        print("Se ha ingresado el rol exitosamente.")
        print("==================================\n")

    def capturaModR(self, id):
        # Captures new data to modify an existing role
        Rol.miconexion.execute("SELECT * FROM rol WHERE idRol = %s" % id)
        dato = Rol.miconexion.fetchone()
        print("")
        print(f"Datos actuales del rol: ")  # Displays current data for the role
        print(f"{"ID":<15} {"Nombre":<20} {"Descripción 1":<20} {"Departamento 2":<20} {"Salario":<15}")
        print(f"{dato[0]:<15} {dato[1]:<20} {dato[2]:<20} {dato[3]:<20} {dato[4]:<15}")
        print("")

        # Captures new data
        nombre = validaString("Digite el nombre del rol: ")
        descripcion = validaString("Digite la descripción del rol: ")
        departamento = validaString("Digite el departamento del rol: ")
        salario = validaFloatPositivo("Digite el salario: ")

        # Calls the method to update the role
        self.modificaRol(nombre, descripcion, departamento, salario, id)

    def modificaRol(self, nombre, descripcion, departamento, salario, id):
        # Updates an existing role in the database
        modificar = ("UPDATE rol SET nombre = %s, "
                     "descripcion = %s, "
                     "departamento = %s,"
                     "salario = %s"
                     "where idRol = %s")
        datos = (nombre, descripcion, departamento, salario, id)
        Rol.miconexion.execute(modificar, datos)
        Rol.conexion.commit()
        print("\n===============================================")
        print("Se han modificado los datos del rol exitosamente.")
        print("===============================================\n")

    def listaRol(self):
        # Lists all roles in the database
        Rol.miconexion.execute("SELECT * FROM rol")
        datos = Rol.miconexion.fetchall()
        if not datos:  # Checks if no roles are found
            print("\n----No se encuentran roles en el sistema.----\n")
        else:
            print("Listado de roles en el sistema:")
            print(f"{"ID":<10} {"Nombre":<20} {"Descripción":<30} {"Departamento":<20} {"Salario":<10}")
            for rol in datos:
                print(f"{rol[0]:<10} {rol[1]:<20} {rol[2]:<30} {rol[3]:<20} {rol[4]:<10.2f}")

    @staticmethod
    def returnListaRol():
        # Retrieves all roles from the database
        Rol.miconexion.execute("SELECT * FROM rol;")
        datos = Rol.miconexion.fetchall()
        return datos

    @staticmethod
    def select_trabajadores():
        # Retrieves active workers from the database
        Rol.miconexion.execute("SELECT idTrabajador, nombre, idRol FROM trabajador WHERE activo = True")
        datos = Rol.miconexion.fetchall()
        return datos

    @staticmethod
    def BorraRol_prueba(id):
        # Deletes a role from the database
        consulta = "DELETE FROM rol WHERE idRol = %s"
        Rol.miconexion.execute(consulta, (id,))
        Rol.conexion.commit()
        print("\n===============================")
        print("Se ha borrado el rol exitosamente")
        print("===============================\n")
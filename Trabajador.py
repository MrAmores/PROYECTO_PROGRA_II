from Conexion import conexionDB
from Persona import Persona
from Rol import Rol
from Validaciones import (
    validaString,
    validaGenero,
    validaAnhoNacimiento
)

class Trabajador(Persona):
    conexion = conexionDB()
    miconexion = conexion.cursor()

    def __init__(self, identificacion, nombre, apellido1, apellido2, anhoNacimiento, genero, activo, idRol):
        super().__init__(identificacion, nombre, apellido1, apellido2, anhoNacimiento, genero, activo)
        self.idRol=idRol

    #We capture data to insert it
    def capturaDatosNuevos(self):
        # Recursive method to capture a new worker's data
        self.identificacion = validaString("Digite el número de identificación del trabajador: ").upper()
        Trabajador.miconexion.execute("SELECT COUNT(*) FROM trabajador WHERE idTrabajador = %s", (self.identificacion,))
        # Check if the ID already exists
        if Trabajador.miconexion.fetchone()[0] > 0:
            print("\n----El ID del trabajador ya existe. Por favor, ingrese un ID único----\n")
            return self.capturaDatosNuevos()  # Recursive call if ID is not unique
        # Capture additional data after a valid ID is entered
        self.nombre = validaString("Digite el nombre del trabajador: ")
        self.apellido1 = validaString("Digite el primer apellido del trabajador: ")
        self.apellido2 = validaString("Digite el segundo apellido del trabajador: ")
        self.anhoNacimiento = validaAnhoNacimiento("Digite el año de nacimiento del trabajador: ")
        self.genero = validaGenero()


        # Gets the current roles
        listRoles = Rol.returnListaRol()
        if not listRoles:  # If the list is empty
            print("\n----No se encuentran roles en el sistema----\n")
        else:
            print("Listado de roles en el sistema:")
            print(f"{"ID":<10} {"Nombre":<20} {"Descripción":<30} {"Departamento":<20} {"Salario":<10}")
            for rol in listRoles:
                print(f"{rol[0]:<10} {rol[1]:<20} {rol[2]:<30} {rol[3]:<20} {rol[4]:<10.2f}")
        print("")        
        # In the next lines the role is selected and this selection is validated
        while True:
            try:
                idSeleccionado = int(input("Digite el ID del rol al que pertenece: ").strip())
                # Checks if the ID is in the list of available roles
                if any(rol[0] == idSeleccionado for rol in listRoles):
                    self.idRol = idSeleccionado
                    break
                else:
                    print("\n----El ID del rol no se encontró en el sistema. Por favor, intente nuevamente----\n")
            except ValueError:
                print("\n----Entrada inválida. Por favor, ingrese un número entero----\n")
        self.activo = True

    #Query to insert new data into the database
    def ingresaDatos(self):
        ingreso = "INSERT INTO trabajador (idTrabajador, nombre, apell_1, apell_2, anho_nacimiento, genero, activo, idRol) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (self.identificacion, self.nombre, self.apellido1, self.apellido2, self.anhoNacimiento,self.genero,self.activo,self.idRol)
        Trabajador.miconexion.execute(ingreso, datos)
        Trabajador.conexion.commit()
        print("\n==========================================\n")
        print("Se ha ingresado al trabajador exitosamente.")
        print("\n==========================================\n")

    #We capture data to do modifications
    def capturaDatosMod(self, id):
       # We get the current data of the worker with the given ID
        Trabajador.miconexion.execute("""
            SELECT 
                t.idTrabajador,
                t.nombre,
                t.apell_1,
                t.apell_2,
                t.anho_nacimiento,
                t.genero,
                r.nombre AS Nombre_Rol
            FROM trabajador t
            INNER JOIN rol r ON r.idRol = t.idRol
            WHERE t.idTrabajador = %s
        """, (id,))
        dato = Trabajador.miconexion.fetchone()

        # Prints the current data
        print(f"Datos actuales del trabajador:")
        print(f"{"ID":<15} {"Nombre":<20} {"Apellido 1":<20} {"Apellido 2":<20} {"Año nacimiento":<15} {"Genero":<10} {"Rol":<20}")
        print(f"{dato[0]:<15} {dato[1]:<20} {dato[2]:<20} {dato[3]:<20} {dato[4]:<15} {dato[5]:<10} {dato[6]:<20}")
        print()
        # New data validation
        nombre = validaString("Digite el nombre del trabajador: ")
        apell_1 = validaString("Digite el primer apellido del trabajador: ")
        apell_2 = validaString("Digite el segundo apellido del trabajador: ")
        anho_nacimiento = validaAnhoNacimiento("Digite el año de nacimiento del trabajador: ")
        genero = validaGenero()
        print()

        # Gets the current roles
        listRoles = Rol.returnListaRol()
        if not listRoles:  # If the list is empty
            print("\n----No se encuentran roles en el sistema.----\n")
        else:
            print("Listado de roles en el sistema:")
            print(f"{"ID":<15} {"Nombre":<20} {"Descripción":<15} {"Departamento":<15} {"Salario":<10}")
            for i in listRoles:
                print(f"{i[0]:<15} {i[1]:<20} {i[2]:<15} {i[2]:<15} {i[3]:<10}")
        # In the next lines the role is selected and this selection is validated
        while True:
            try:
                idSeleccionado = int(input("\nDigite el ID del rol al que pertenece: ").strip())
                # Checks if the ID is in the list of available roles
                if any(rol[0] == idSeleccionado for rol in listRoles):
                    idRol = idSeleccionado
                    break
                else:
                    print("\n----El ID del rol no se encontró en el sistema. Por favor, intente nuevamente----\n")
            except ValueError:
                print("\n----Entrada inválida. Por favor, ingrese un número entero----\n")

        #We call the method to update data
        self.modificaDatos(nombre, apell_1, apell_2, anho_nacimiento, genero, idRol, id)

    #Query to uptade existing data in the database
    def modificaDatos(self, nombre, apell_1, apell_2, anho_nacimiento, genero, idRol, id):
        modificar = ("UPDATE trabajador SET nombre = %s, "
                     "apell_1 = %s, "
                     "apell_2 = %s, "
                     "anho_nacimiento = %s, "
                     "genero = %s, "
                     "idRol = %s "
                     "WHERE idTrabajador = %s")
        datos = (nombre, apell_1, apell_2, anho_nacimiento, genero, idRol, id)
        Trabajador.miconexion.execute(modificar, datos)
        Trabajador.conexion.commit()
        print("\n====================================================\n")
        print("Se han modificado los datos del trabajador exitosamente.")
        print("\n====================================================\n")

    #Prints all information in the database
    def listaDatos(self):
        Trabajador.miconexion.execute("""
            SELECT
                t.idTrabajador,
                t.nombre,
                t.apell_1,
                t.apell_2,
                t.anho_nacimiento,
                t.genero,
                r.nombre AS Nombre_Rol
                FROM trabajador t
                INNER JOIN rol r ON r.idRol = t.idRol   
        """)
        datos = Trabajador.miconexion.fetchall()
        if not datos:  # If the list is empty
            print("\n----No se encuentran trabajadores activos en el sistema----\n")
        # Encabezado de la tabla
        else:
            print("Listado de trabajadores en el sistema:")
            print(f"{"ID":<15} {"Nombre":<20} {"Apellido 1":<20} {"Apellido 2":<20} {"Año nacimiento":<15} {"Genero":<10} {"Rol":<20}")
            # Imprimir cada fila de datos
            for i in datos:
                print(f"{i[0]:<15} {i[1]:<20} {i[2]:<20} {i[3]:<20} {i[4]:<15} {i[5]:<10} {i[6]:<20}")

                
    #Query to "delete" data from the database
    def desactiva(self, id):
        modificar = "UPDATE trabajador SET activo = %s, idRol = %s WHERE idTrabajador = %s"
        datos = (False, None, id)
        Trabajador.miconexion.execute(modificar, datos)
        Trabajador.conexion.commit()
        print("\n========================================\n")
        print("Se ha borrado el trabajador exitosamente.")
        print("\n========================================\n")

    #Prints currently active workers
    @staticmethod
    def trabajadoresActivos():
        # Captures data
        Trabajador.miconexion.execute("""
            SELECT 
                t.idTrabajador,
                t.nombre,
                t.apell_1,
                t.apell_2,
                t.anho_nacimiento,
                t.genero,
                r.nombre AS Nombre_Rol
                FROM trabajador t
                INNER JOIN rol r ON r.idRol = t.idRol
                WHERE t.activo = True
            """)
        datos = Trabajador.miconexion.fetchall()
        return datos
    
    
    
    

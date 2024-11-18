from Conexion import conexionDB
from Persona import Persona
from Rol import Rol
from Validaciones import (
    validaString,
    validaIntPositivo,
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
        self.identificacion = validaString("Digite el número de identificación del trabajador: ").upper()
        self.nombre = validaString("Digite el nombre del trabajador: ")
        self.apellido1 = validaString("Digite el primer apellido del trabajador: ")
        self.apellido2 = validaString("Digite el segundo apellido del trabajador: ")
        self.anhoNacimiento = validaAnhoNacimiento("Digite el año de nacimiento del trabajador: ")
        self.genero = validaGenero()

        # Gets the current roles
        listRoles = Rol.returnListaRol()
        print("Listado de roles en el sistema:")
        print("ID, NOMBRE")
        for i in listRoles:
            print(i)
        # In the next lines the role is selected and this selection is validated
        while True:
            try:
                idSeleccionado = int(input("Digite el ID del rol al que pertenece: ").strip())

                # Checks if the ID is in the list of available roles
                if any(rol[0] == idSeleccionado for rol in listRoles):
                    self.idRol = idSeleccionado
                    break
                else:
                    print("ID no encontrado. Intente nuevamente.")
            except ValueError:
                print("Ingrese un número entero válido para el ID del rol")
        self.activo = True

    #Query to insert new data into the database
    def ingresaDatos(self):
        ingreso = "INSERT INTO trabajador (idTrabajador, nombre, apell_1, apell_2, anho_nacimiento, genero, activo, idRol) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (self.identificacion, self.nombre, self.apellido1, self.apellido2, self.anhoNacimiento,self.genero,self.activo,self.idRol)
        Trabajador.miconexion.execute(ingreso, datos)
        Trabajador.conexion.commit()
        print("Se ha ingresado al trabajador exitosamente.")

    #We capture data to do modifications
    def capturaDatosMod(self, id):
        # We get the current data of the worker with the given ID
        Trabajador.miconexion.execute("SELECT * FROM trabajador WHERE idTrabajador = '%s'" % id)
        datos = Trabajador.miconexion.fetchone()

        # Prints the current data
        print(f"Datos actuales del trabajador: {datos}")

        # New data validation
        nombre = validaString("Digite el nombre del trabajador: ")
        apell_1 = validaString("Digite el primer apellido del trabajador: ")
        apell_2 = validaString("Digite el segundo apellido del trabajador: ")
        anho_nacimiento = validaAnhoNacimiento("Digite el año de nacimiento del trabajador: ")
        genero = validaGenero()

        # Gets the current roles
        listRoles = Rol.returnListaRol()
        print("Listado de roles en el sistema:")
        print("ID, NOMBRE")
        for i in listRoles:
            print(i)
        # In the next lines the role is selected and this selection is validated
        while True:
            try:
                idSeleccionado = int(input("Digite el ID del rol al que pertenece: ").strip())

                # Checks if the ID is in the list of available roles
                if any(rol[0] == idSeleccionado for rol in listRoles):
                    idRol = idSeleccionado
                    break
                else:
                    print("ID no encontrado. Intente nuevamente.")
            except ValueError:
                print("Ingrese un número entero válido para el ID del rol.")

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
        print("Se han modificado los datos del trabajador exitosamente.")

    #Prints all information in the database
    def listaDatos(self):
        print("Listado de trabajadores en el sistema:")
        print("IDENTIFICACIÓN, NOMBRE, APELLIDO_1, APELLIDO_2, AÑO_NACIMIENTO, GÉNERO, ACTIVO, ID_ROL")
        Trabajador.miconexion.execute("select * from trabajador")
        datos = Trabajador.miconexion.fetchall()
        if not datos:  # If the list is empty
            print("No se encuentran trabajadores activos en el sistema.")
        else:
            for i in datos:
                print(i)

    #Query to "delete" data from the database
    def desactiva(self, id):
        modificar = "UPDATE trabajador SET activo = %s WHERE idTrabajador = %s"
        datos = (False, id)
        Trabajador.miconexion.execute(modificar, datos)
        Trabajador.conexion.commit()
        print("Se ha borrado el trabajador exitosamente.")

    #Prints currently active workers
    def trabajadoresActivos(self):
        # Captures data
        Trabajador.miconexion.execute( "SELECT idTrabajador, nombre, apell_1, apell_2, anho_nacimiento, genero, idRol FROM trabajador WHERE activo = True")
        datos = Trabajador.miconexion.fetchall()
        return datos

from Conexion import conexionDB
from Persona import Persona
from Rol import Rol
from Validaciones import (
    validaString,
    validaIntPositivo,
    validaGenero,
    validaIdRol
)

class Trabajador(Persona):
    conexion = conexionDB()
    miconexion = conexion.cursor()

    def __init__(self, identificacion, nombre, apellido1, apellido2, anhoNacimiento, genero, activo, idRol):
        super().__init__(identificacion, nombre, apellido1, apellido2, anhoNacimiento, genero, activo)
        self.idRol=idRol

    #We capture data to insert it
    def capturaDatosNuevos(self):
        self.identificacion = validaString("Digite el número de identificación del trabajador: ")
        self.nombre =  validaString("Digite el nombre del trabajador: ")
        self.apellido1 =  validaString("Digite el primer apellido del trabajador: ")
        self.apellido2 = validaString("Digite el segundo apellido del trabajador: ")
        self.anhoNacimiento = validaIntPositivo("Digite el año de nacimiento del trabajador: ")
        self.genero = validaGenero()
        #Gets the active roles
        rolesActuales = Rol.returnListaRol()
        #In the next line the role is selected and this selection is validated
        self.idRol = validaIdRol(rolesActuales)
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
        #We get the current data of the worker with the given ID
        Trabajador.miconexion.execute("SELECT * FROM trabajador WHERE idPasajero = '%s'" % id)
        datos = Trabajador.miconexion.fetchone()

        #Prints the current data
        print(f"Datos actuales del trabajador: {datos}")

        #New data validation
        nombre = validaString("Digite el nombre del trabajador: ")
        apell_1 = validaString("Digite el primer apellido del trabajador: ")
        apell_2 = validaString("Digite el segundo apellido del trabajador: ")
        anho_nacimiento = validaIntPositivo("Digite el año de nacimiento del trabajador: ")
        genero = validaGenero()
        idRol = validaIdRol()

        #We call the method to update data
        self.modificaDatos(nombre, apell_1, apell_2, anho_nacimiento, genero, idRol, id)

    #Query to uptade existing data in the database
    def modificaDatos(self, nombre, apell_1, apell_2, anho_nacimiento, genero, idRol, id):
        modificar = ("update trabajador set nombre = %s, "
                     "apell_1 = %s, "
                     "apell_2 = %s,"
                     "anho_nacimiento = %s,"
                     "genero = %s,"
                     "idRol = %s"
                     "where idPasajero = %s")
        datos = (nombre, apell_1, apell_2, anho_nacimiento, genero, idRol, id)
        Trabajador.miconexion.execute(modificar, datos)
        Trabajador.conexion.commit()
        print("Se han modificado los datos del trabajador exitosamente.")

    #Prints all information in the database
    def listaDatos(self):
        print("Listado de trabajadores en el sistema:")
        Trabajador.miconexion.execute("select * from trabajador")
        datos = Trabajador.miconexion.fetchall()
        for i in datos:
            print(i)

    #Query to "delete" data from the database
    def desactiva(self, id):
        modificar = "UPDATE trabajador SET activo = %s WHERE idRol = %s"
        datos = (False, id)
        Trabajador.miconexion.execute(modificar, datos)
        Trabajador.conexion.commit()
        print("Se ha borrado el trabajador exitosamente.")

    #Prints currently active workers
    def trabajadoresActivos(self):
        #Captures data
        Trabajador.miconexion.execute("SELECT idTrabajador, nombre, apell_1, apell_2 FROM trabajador WHERE activo = True")
        datos = Trabajador.miconexion.fetchall()

        print("Listado de trabajadores activos en el sistema:")
        #Prints workers with an index to facilitate selection
        for i, trabajador in enumerate(datos, start=1):
            print(f"{i}. {trabajador[1]} {trabajador[2]} {trabajador[3]} (ID: {trabajador[0]})")
        return datos

from Persona import Persona
from Conexion import conexionDB
from Cabina import Cabina

from Validaciones import (
    validaString,
    validaAnhoNacimiento,
    validaGenero,
    validaIntPositivo
)

class Pasajero(Persona):
    conexion = conexionDB()
    miconexion = conexion.cursor()
    
    def __init__(self, identificacion, nombre, apellido1, apellido2, anhoNacimiento, genero, activo, idCabina):
        super().__init__(identificacion, nombre, apellido1, apellido2, anhoNacimiento, genero, activo)
        self.idCabina = idCabina

    def capturaDatosNuevos(self): # ABSTRACT METHOD 
        while True:
            self.identificacion = validaString("Digite el número de identificación del pasajero: ")
            Pasajero.miconexion.execute("SELECT COUNT(*) FROM pasajero WHERE idPasajero = %s", (self.identificacion,))
            if Pasajero.miconexion.fetchone()[0] > 0:
                print("\n----El ID del pasajero ya existe. Por favor, ingrese un ID único----\n")
            elif self.identificacion:
                self.activo = True
                break
        while True:
            acompañantes = input("""
            Usted viene con acompañantes?
            1 - Si
            2 - No
            """
            )
            if acompañantes == "1":
                cantidad_pasajeros = validaIntPositivo("Digite la cantidad de acompañantes que vienen con usted: ")
                break
            elif acompañantes == "2":
                cantidad_pasajeros = 0
                break
            else:
                print("\n ---- Opción invalida selecione 1 o 2 ----\n")        
        ids_disponibles = Cabina.obtener_cabinas_disponibles(cantidad_pasajeros)
        if not ids_disponibles:
            print("\n----No se puedo ingresar al pasajero ya que no hay cabinas disponibles para esa cantidad de personas----\n")
        else:
             while True:
                try:
                    cabina = int(input("Seleccione el ID de la cabina: ").strip())
                    if cabina in ids_disponibles:  # Verificar si el ID existe en la lista de IDs disponibles
                        self.idCabina = cabina
                        self.nombre = validaString("Digite el nombre del pasajero: ")
                        self.apellido1 = validaString("Digite el primer apellido del pasajero: ")
                        self.apellido2 = validaString("Digite el segundo apellido del pasajero: ")
                        self.anhoNacimiento = validaAnhoNacimiento("Digite el año de nacimiento del pasajero: ")
                        self.genero = validaGenero()
                        Cabina.pasar_cabina_a_ocupada(self.idCabina)
                        Pasajero.ingresaDatos()
                        break
                    else:
                        print("\n----El ID de la cabina ingresado no está disponible. Por favor, seleccione un ID válido de la lista----\n")
                except ValueError:
                    print("\n----Entrada inválida. Por favor, ingrese un número entero----\n")
                            
    def ingresaDatos(self): # ABSTRACT METHOD 
        # Consulta SQL de inserción
        ingreso = "INSERT INTO pasajero (idPasajero, nombre, apell_1, apell_2, anho_nacimiento, genero, activo, idCabina) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (self.identificacion, self.nombre, self.apellido1, self.apellido2, self.anhoNacimiento,self.genero,self.activo,self.idCabina)
        # Ejecutar la consulta e ingresar datos
        Pasajero.miconexion.execute(ingreso, datos)
        Pasajero.conexion.commit()
        print("Se ha ingresado al pasajero exitosamente.")
        
    def capturaDatosMod(self, id): # ABSTRACT METHOD 
        # We get the current data of the worker with the given ID
        Pasajero.miconexion.execute("SELECT * FROM pasajero WHERE idPasajero = '%s'" % id)
        datos = Pasajero.miconexion.fetchone()
        # Prints the current data
        print(f"Datos actuales del pasajero: {datos}")
        # New data validation
        nombre = validaString("Digite el nombre del pasajero: ")
        apell_1 = validaString("Digite el primer apellido del pasajero: ")
        apell_2 = validaString("Digite el segundo apellido del pasajero: ")
        anho_nacimiento = validaAnhoNacimiento("Digite el año de nacimiento del pasajero: ")
        genero = validaGenero()
        #We call the method to update data
        self.modificaDatos(nombre, apell_1, apell_2, anho_nacimiento, genero, id)         
                                 
    def modificaDatos(self, nombre, apell_1, apell_2, anho_nacimiento, genero, id):# ABSTRACT METHOD 
         # Consulta SQL de modificación
        modificar = ("update pasajero set nombre = %s, "
                     "apell_1 = %s, "
                     "apell_2 = %s,"
                     "anho_nacimiento = %s,"
                     "genero = %s"
                     "where idPasajero = %s")
        datos = (nombre, apell_1, apell_2, anho_nacimiento, genero, id)
        # Execute the query and modify data
        Pasajero.miconexion.execute(modificar, datos)
        Pasajero.conexion.commit()
        print("Se han modificado los datos del pasajero exitosamente.")
    
    def listaDatos(self):# ABSTRACT METHOD 
        print("Listado de pasajeros en el sistema")
        # Execute query and list data
        Pasajero.miconexion.execute("SELECT * FROM pasajero WHERE activo != 0")
        datos = Pasajero.miconexion.fetchall()
        for i in datos:
            print(f"Identificación: {i[0]}, Nombre: {i[1]}, Apellido 1: {i[2]}, Apellido 2: {i[3]}, Año de Nacimiento: {i[4]}, Género: {i[5]}, Activo: {i[6]}, ID Cabina: {i[7]}")
            
    def desactiva(self, id):# ABSTRACT METHOD 
        modificar = "UPDATE pasajero SET activo = %s WHERE idPasajero = %s"
        datos = (False, id)
        # Ejecutar la consulta y inactivar datos
        Pasajero.miconexion.execute(modificar, datos)
        Pasajero.conexion.commit()
        print("\n=======================================")
        print("Se ha borrado el pasajero exitosamente.")
        print("\n=====================================\n")
               
        
    @staticmethod
    def select_pasajero():
        # Query para obtener las cabinas
        consulta = "SELECT idPasajero,nombre,CONCAT(apell_1, ' ', apell_2), anho_nacimiento,genero FROM pasajero WHERE activo != 0 "
        Pasajero.miconexion.execute(consulta)
        pasajeros = Pasajero.miconexion.fetchall()  # Retorna lista de tuplas
        return pasajeros
    
           
    
    

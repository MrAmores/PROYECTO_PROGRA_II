from Persona import Persona
from Conexion import conexionDB
from Cabina import Cabina
from Validaciones import (
    validaString,
    validaIntPositivo,
    validaGenero
)
class Pasajero(Persona):
    conexion = conexionDB()
    miconexion = conexion.cursor()
    
    def __init__(self, identificacion, nombre, apellido1, apellido2, anhoNacimiento, genero, activo, idCabina):
        super().__init__(identificacion, nombre, apellido1, apellido2, anhoNacimiento, genero, activo)
        self.idCabina = idCabina

    def capturaDatosNuevos(self):
        self.identificacion = validaString("Digite el número de identificación del pasajero: ")
        self.nombre = validaString("Digite el nombre del pasajero: ")
        self.apellido1 = validaString("Digite el primer apellido del pasajero: ")
        self.apellido2 = validaString("Digite el segundo apellido del pasajero: ")
        self.anhoNacimiento = validaIntPositivo("Digite el año de nacimiento del pasajero: ")
        self.genero = validaGenero()
        while True:
            try:
                cantidad_pasajeros = int(input("Digite la cantidad de acompañantes que vienen con usted: "))
                if cantidad_pasajeros >= 0:  # Cambié el operador de comparación
                    Cabina.obtener_cabinas_disponibles(cantidad_pasajeros)
                    while True:
                        try:
                            cabina = int(input("Seleccione el id de la cabina: ").strip())
                            if cabina > 0:
                                self.idCabina = cabina
                                break
                            else:
                                print("Entrada inválida. Por favor, ingrese un número entero positivo.")
                        except ValueError:
                            print("Entrada inválida. Por favor, ingrese un número entero.")
                    break
                else:
                    print("No se permite ingresar números negativos.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")
        self.activo = True
        #self.ingresaPasajero()
    
    def ingresaDatos(self):
        # Consulta SQL de inserción
        ingreso = "INSERT INTO pasajero (idPasajero, nombre, apell_1, apell_2, anho_nacimiento, genero, activo, idCabina) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (self.identificacion, self.nombre, self.apellido1, self.apellido2, self.anhoNacimiento,self.genero,self.activo,self.idCabina)
        # Ejecutar la consulta e ingresar datos
        Pasajero.miconexion.execute(ingreso, datos)
        Pasajero.conexion.commit()
        print("Se ha ingresado al pasajero exitosamente.")

    def capturaDatosMod(self):
        pass

    def modificaDatos(self, nombre, apell_1, apell_2, anho_nacimiento, genero, id):
         # Consulta SQL de modificación
        modificar = ("update pasajero set nombre = %s, "
                     "apell_1 = %s, "
                     "apell_2 = %s,"
                     "anho_nacimiento = %s,"
                     "genero = %s,"
                     "where idPasajero = %s")
        datos = (nombre, apell_1, apell_2, anho_nacimiento, genero, id)
        # Ejecutar la consulta y modificar datos
        Pasajero.miconexion.execute(modificar, datos)
        Pasajero.conexion.commit()
        print("Se han modificado los datos del pasajero exitosamente.")
    
    def listaDatos(self):
        print("Listado de pasajeros en el sistema:")
        # Ejecutar la consulta y listar datos
        Pasajero.miconexion.execute("select * from pasajero")
        datos = Pasajero.miconexion.fetchall()
        for i in datos:
            print(i)
    
    def desactiva(self, id):
        modificar = "UPDATE pasajero SET activo = %s WHERE idRol = %s"
        datos = (False, id)
        # Ejecutar la consulta y inactivar datos
        Pasajero.miconexion.execute(modificar, datos)
        Pasajero.conexion.commit()
        print("Se ha borrado el pasajero exitosamente.")
    
           
    
    

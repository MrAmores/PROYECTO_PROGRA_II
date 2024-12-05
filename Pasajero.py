from Persona import Persona
from Conexion import conexionDB

from Validaciones import (
    validaString,
    validaAnhoNacimiento,
    validaGenero
)

class Pasajero(Persona):
    conexion = conexionDB()
    miconexion = conexion.cursor()
    def __init__(self, identificacion, nombre, apellido1, apellido2, anhoNacimiento, genero, activo):
        super().__init__(identificacion, nombre, apellido1, apellido2, anhoNacimiento, genero, activo)
   
    #Recursivo
    def capturaDatosNuevos(self): 
        # Recursive method to capture a new passenger's data
        self.identificacion = validaString("Digite el número de identificación del pasajero: ").upper()
        Pasajero.miconexion.execute("SELECT COUNT(*) FROM pasajero WHERE idPasajero = %s", (self.identificacion,))
        if Pasajero.miconexion.fetchone()[0] > 0: #The user doesn't exists in the bd
            print("\n----El ID del pasajero ya existe. Por favor, ingrese un ID único----\n")
            return self.capturaDatosNuevos()  # Recursive call if ID is not unique
        
        self.activo = True
        self.nombre = validaString("Digite el nombre del pasajero: ")
        self.apellido1 = validaString("Digite el primer apellido del pasajero: ")
        self.apellido2 = validaString("Digite el segundo apellido del pasajero: ")
        self.anhoNacimiento = validaAnhoNacimiento("Digite el año de nacimiento del pasajero: ")
        self.genero = validaGenero()
        self.ingresaDatos()

                            
    def ingresaDatos(self): # ABSTRACT METHOD 
        # Insert SQL query
        ingreso = "INSERT INTO pasajero (idPasajero, nombre, apell_1, apell_2, anho_nacimiento, genero, activo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        datos = (self.identificacion, self.nombre, self.apellido1, self.apellido2, self.anhoNacimiento,self.genero,self.activo)
        Pasajero.miconexion.execute(ingreso, datos)  # Execute the query and enter data
        Pasajero.conexion.commit()
        print("\n=====================================")
        print("Se ha ingresado al pasajero exitosamente.")
        print("=====================================\n")
        

    def capturaDatosMod(self, id): # ABSTRACT METHOD 
        # We get the current data of the worker with the given ID
        Pasajero.miconexion.execute("SELECT * FROM pasajero WHERE idPasajero = '%s'" % id)
        dato = Pasajero.miconexion.fetchone()
        # Prints the current data
        print(f"Datos actuales del pasajero:")
        print(f"{"ID":<15} {"Nombre":<20} {"Apellido 1":<20} {"Apellido 2":<20} {"Año nacimiento":<15} {"Genero":<10}")
        print(f"{dato[0]:<15} {dato[1]:<20} {dato[2]:<20} {dato[3]:<20} {dato[4]:<15} {dato[5]:<10}")
        print("")
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
        print("\n====================================================")
        print("Se han modificado los datos del pasajero exitosamente.")
        print("====================================================\n")
    
    def listaDatos(self):  # ABSTRACT METHOD
        print("\nListado de pasajeros en el sistema:\n")
        # Execute query to list data
        Pasajero.miconexion.execute("SELECT * FROM pasajero WHERE activo != 0")
        datos = Pasajero.miconexion.fetchall()

        if not datos:  # If there are no active passengers
            print("\n----No se encuentran pasajeros activos en el sistema----\n")
        else:
            # Table header
            print(f"{"Identificación":<15} {"Nombre":<20} {"Apellido 1":<15} {"Apellido 2":<15} {"Año Nac":<10} {"Género":<10} {"Activo":<10}")

            # Data rows
            for i in datos:  
                #idCabina = i[7] if i[7] is not None else "N/A"  # Manejo de None
                print(f"{i[0]:<15} {i[1]:<20} {i[2]:<15} {i[3]:<15} {i[4]:<10} {i[5]:<10} {i[6]:<10}")
                

    def desactiva(self, id):# ABSTRACT METHOD 
        modificar = "UPDATE pasajero SET activo = %s WHERE idPasajero = %s"
        datos = (False, id)
        Pasajero.miconexion.execute(modificar, datos)  # Execute the query and enter data
        Pasajero.conexion.commit()
        print("\n=======================================")
        print("Se ha borrado el pasajero exitosamente.")
        print("=======================================\n")

                 
    @staticmethod
    def select_pasajero():
        # Query to obtain the booths
        consulta = "SELECT idPasajero,nombre,CONCAT(apell_1, ' ', apell_2), anho_nacimiento,genero FROM pasajero WHERE activo != 0 "
        Pasajero.miconexion.execute(consulta)
        pasajeros = Pasajero.miconexion.fetchall()  
        return pasajeros  # Return list of tuples
    
    @staticmethod
    def listaPasajerosConCabinas():  # Method for listing passengers and cabins
        print("\nListado de pasajeros y sus cabinas:\n")
        # Consult to get data
        consulta = """
            SELECT 
                CONCAT(p.nombre, ' ', p.apell_1, ' ', p.apell_2) AS "Nombre del pasajero",
                p.idPasajero AS "Identificación del pasajero",
                c.idCabina AS "Número de cabina",
                c.tamanho AS "Tamaño de la cabina",
                reg.fechaEntrada AS "Fecha de entrada",
                reg.fechaSalida AS "Fecha de salida"
            FROM 
                Registro reg
            JOIN 
                Pasajero p ON reg.idPasajero = p.idPasajero
            JOIN 
                Cabina c ON reg.idCabina = c.idCabina
            ORDER BY 
                p.nombre, p.apell_1, p.apell_2;
        """
        # Execute the consult
        Pasajero.miconexion.execute(consulta)
        datos = Pasajero.miconexion.fetchall()

        if not datos:  # There's not results
            print("\n----No se encontraron registros de pasajeros hospedados----\n")
        else:
            # Table header
            print(f"{'Nombre completo':<30} {'Identificación':<20} {'N°Cabina':<15} {'Tamaño':<15} {'Fecha entrada':<20} {'Fecha salida':<15}")
            # Row in data
            for fila in datos:
                fecha_entrada = fila[4].strftime("%Y-%m-%d")  # Date format for entry
                fecha_salida = fila[5].strftime("%Y-%m-%d")   # Date format for exit
                print(f"{fila[0]:<30} {fila[1]:<20} {fila[2]:<15} {fila[3]:<15} {fecha_entrada:<20} {fecha_salida:<15}")
        
    
           
    
    

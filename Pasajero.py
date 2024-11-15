from Persona import Persona
from Conexion import conexionDB
from Cabina import Cabina
class Pasajero(Persona):
    conexion = conexionDB()
    miconexion = conexion.cursor()
    
    def __init__(self, identificacion, nombre, apellido1, apellido2, fechaNacimiento, genero, activo, idCabina):
        super().__init__(identificacion, nombre, apellido1, apellido2, fechaNacimiento, genero, activo)
        self.idCabina = idCabina

    

    def capturaDatos(self): # ABSTRACT METHOD 
         # Validation of identification
        while True:
            self.identificacion = input("Digite la identificación del pasajero: ").strip()
            # Check if the identificacion already exists in the database
            Pasajero.miconexion.execute("SELECT COUNT(*) FROM pasajero WHERE idPasajero = %s", (self.identificacion,))
            if Pasajero.miconexion.fetchone()[0] > 0:
                print("El ID del pasajero ya existe. Por favor, ingrese un ID único.")
            elif self.identificacion:
                self.activo = True
                break
            else:
                print("El número de identificación no puede estar vacío o contener solo espacios.")
                
        # Validation of name
        while True:
            self.nombre = input("Digite el nombre del pasajero: ").strip()
            if self.nombre:
                break
            else:
                print("El nombre no puede estar vacío o contener solo espacios.")
                
        # Validation of the first last name
        while True:
            self.apellido1 = input("Digite el primer apellido del pasajero: ").strip()
            if self.apellido1:
                break
            else:
                print("El primer apellido no puede estar vacío o contener solo espacios.")
                
        # Validation of the second last name
        while True:
            self.apellido2 = input("Digite el segundo apellido del pasajero: ").strip()
            if self.apellido2:
                break
            else:
                print("El segundo apellido no puede estar vacío o contener solo espacios.")
                
        # Validation of date of birtg year
        while True:
            try:
                anhoNacimiento = int(input("Digite el año de nacimiento del pasajero: ").strip())
                if anhoNacimiento > 0:
                    self.fechaNacimiento = anhoNacimiento
                    break
                else:
                    print("El año de nacimiento debe de ser una numero positivo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")
                     
        # Gender validation
        while True:
            gen = input("""
            Seleccione el género:
            F - Femenino
            M - Masculino
            """).strip().upper()

            if gen == "F":
                self.genero = "Femenino"
                break
            elif gen == "M":
                self.genero = "Masculino"
                break
            else:
                print("Opción no válida. Ingrese 'F' para Femenino o 'M' para Masculino.")
                
        while True:
            try:
                cantidad_pasajeros = int(input("Digite la cantidad de acompañantes que vienen con usted: "))
                if cantidad_pasajeros >= 0:  
                    ids_disponibles = Cabina.obtener_cabinas_disponibles(cantidad_pasajeros)  # Obtener y almacenar IDs disponibles
                    #print(f"IDs disponibles: {ids_disponibles}")
                    if not ids_disponibles:
                        print("No hay cabinas disponibles para la cantidad de acompañantes especificada.")
                        self.idCabina=None
                        break
                    while True:
                        try:
                            cabina = int(input("Seleccione el ID de la cabina: ").strip())
                            if cabina in ids_disponibles:  # Verificar si el ID existe en la lista de IDs disponibles
                                self.idCabina = cabina
                                Cabina.pasar_cabina_a_ocupada(self.idCabina)
                                #print(f"Cabina seleccionada: {self.idCabina}")
                                break
                            else:
                                print("El ID ingresado no está disponible. Por favor, seleccione un ID válido de la lista.")
                        except ValueError:
                            print("Entrada inválida. Por favor, ingrese un número entero.")
                    break        
                else:
                    print("No se permite ingresar números negativos.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")
        if self.idCabina:  # Solo si se ha seleccionado una cabina
            self.ingresaPasajero()
        else:
            print("No se puede ingresar al pasajero ya que no hay cabinas disponibles.")       
               
    def modificar(self, nombre, apell_1, apell_2, anho_nacimiento, genero, id):# ABSTRACT METHOD 
         # Consulta SQL de modificación
        modificar = ("update pasajero set nombre = %s, "
                     "apell_1 = %s, "
                     "apell_2 = %s,"
                     "anho_nacimiento = %s,"
                     "genero = %s,"
        
                     "where idPasajero = %s")
        datos = (nombre, apell_1, apell_2, anho_nacimiento, genero, id)
        
        # Execute the query and modify data
        Pasajero.miconexion.execute(modificar, datos)
        Pasajero.conexion.commit()
        print("Se han modificado los datos del pasajero exitosamente.")
    
    def listar(self):# ABSTRACT METHOD 
        print("Listado de pasajeros en el sistema")
        # Execute query and list data
        Pasajero.miconexion.execute("SELECT * FROM pasajero WHERE activo != 0")
        datos = Pasajero.miconexion.fetchall()
        for i in datos:
            print(f"Identificación: {i[0]}, Nombre: {i[1]}, Apellido 1: {i[2]}, Apellido 2: {i[3]}, Año de Nacimiento: {i[4]}, Género: {i[5]}, Activo: {i[6]}, ID Cabina: {i[7]}")
    
    def desactivar(self, id):# ABSTRACT METHOD 
        modificar = "UPDATE pasajero SET activo = %s WHERE idPasajero = %s"
        datos = (False, id)
        # Ejecutar la consulta y inactivar datos
        Pasajero.miconexion.execute(modificar, datos)
        Pasajero.conexion.commit()
        print("Se ha borrado el pasajero exitosamente.")
        
    def ingresaPasajero(self):
        # Consulta SQL de inserción
        ingreso = "INSERT INTO pasajero (idPasajero, nombre, apell_1, apell_2, anho_nacimiento, genero, activo, idCabina) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (self.identificacion, self.nombre, self.apellido1, self.apellido2, self.fechaNacimiento,self.genero,self.activo,self.idCabina)
        # Ejecutar la consulta e ingresar datos
        Pasajero.miconexion.execute(ingreso, datos)
        Pasajero.conexion.commit()
        print("Se ha ingresado al pasajero exitosamente.")
    
    @staticmethod
    def select_pasajero():
        print("Listado de pasajeros en el sistema")
        # Execute query and list data
        Pasajero.miconexion.execute("SELECT idPasajero,nombre,apell_1 FROM pasajero ")
        datos = Pasajero.miconexion.fetchall()
        for i in datos:
            print(f"Identificación: {i[0]}, Nombre: {i[1]}, Apellido 1: {i[2]}")
    
           
    
    

from Conexion import conexionDB
from Validaciones import validaIntPositivo, validar_fecha
from Cabina import Cabina
from Pasajero import Pasajero

class RegistroEstadia:
    conexion = conexionDB()  # Establish a single database connection for the class
    miconexion = conexion.cursor()
    
    def __init__(self, idRegistro, idCabina, idPasajero, fechaDeIngreso, fechaDeSalida):
        # Initializes a Registro object
        self.idRegistro = idRegistro
        self.idCabina = idCabina
        self.idPasajero = idPasajero
        self.fechaDeIngreso = fechaDeIngreso
        self.fechaDeSalida = fechaDeSalida

    def capturaDatos(self):
    # Modify an existing passenger
        listapasajeros = Pasajero.select_pasajero()  # Fetches all passengers
        if not listapasajeros:
            print("\n----No hay pasajeros registrados----\n")  # No passengers message
        else:
            ids_validos = [pasajero[0] for pasajero in listapasajeros]  # Collect valid IDs
            # Displays the list of passengers
            print("")
            print(f"{"ID":<10} {"Nombre":<20} {"Apellidos":<30}")
            for pasajero in listapasajeros:
                print(f"{pasajero[0]:<10} {pasajero[1]:<20} {pasajero[2]:<30}")
            while True:
                id_pasajero = input("\nDigite el ID del pasajero que desea registrar a una cabina: ").strip().upper()
                if id_pasajero in ids_validos:
                    self.idPasajero = id_pasajero   # Captures new data for the passenger
                    break
                else:
                    print("\n----ID no válido. Intente nuevamente.----\n")
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
                print("\n----No hay cabinas disponibles----\n")
            else:
                while True:
                    try:
                        cabina = int(input("Seleccione el ID de la cabina: ").strip())
                        if cabina in ids_disponibles: # Check if the ID exists in the list of available IDs
                            self.idCabina = cabina
                            self.fechaDeIngreso = validar_fecha("Digite la fecha de ingreso en formato YYYY-MM-DD: ")
                            self.fechaDeSalida = validar_fecha("Digite la fecha de salida en formato YYYY-MM-DD: ")
                            Cabina.pasar_cabina_a_ocupada(self.idCabina)
                            self.ingresaRegistroEstadia(self.idCabina, self.idPasajero, self.fechaDeIngreso, self.fechaDeSalida)
                            break
                        else:
                            print("\n----El ID de la cabina ingresado no está disponible. Por favor, seleccione un ID válido de la lista----\n")
                    except ValueError:
                        print("\n----Entrada inválida. Por favor, ingrese un número entero----\n")      
            
        
    def ingresaRegistroEstadia(self, idCabina, idPasajero, fechaEntrada, fechaSalida):
        consulta = ("INSERT INTO Registro (idCabina, idPasajero, fechaEntrada, fechaSalida) VALUES (%s,%s,%s,%s)")
        datos=(idCabina, idPasajero, fechaEntrada, fechaSalida)
        RegistroEstadia.miconexion.execute(consulta, datos)
        RegistroEstadia.conexion.commit()
        print("\n====================================================\n")
        print("Se ha registrado la estadía exitosamente.")
        print("\n====================================================\n")
        
    # Methood to print the passager information
    def listar(self):
        consulta = """
        SELECT 
        p.idPasajero AS id_pasajero, 
        p.nombre, 
        CONCAT(p.apell_1, ' ', p.apell_2) AS apellidos_completos,
        c.idCabina AS numero_cabina, 
        r.fechaEntrada AS fecha_entrada, 
        r.fechaSalida AS fecha_salida
        FROM 
            Registro r
        JOIN 
            Pasajero p ON r.idPasajero = p.idPasajero
        JOIN 
            Cabina c ON r.idCabina = c.idCabina;
        """
        print("\nListado:\n")
        # Execute query to list data
        RegistroEstadia.miconexion.execute(consulta)
        datos = RegistroEstadia.miconexion.fetchall()
        if not datos:  # If there are no active passengers
            print("\n----No se encuentran pasajeros activos en el sistema----\n")
        else:
            # Table header
            print(f"{"ID Pasajero":<15} {"Nombre":<20} {"Apellidos":<30} {"Número Cabina":<15} {"Fecha Entrada":<15} {"Fecha Salida":<15}")
            for i in datos:  
                fecha_entrada = i[4].strftime("%Y-%m-%d")  # Date format for entry
                fecha_salida = i[5].strftime("%Y-%m-%d")   # Date format for exit
                print(f"{i[0]:<15} {i[1]:<20} {i[2]:<30} {i[3]:<15} {fecha_entrada:<15} {fecha_salida:<15}")

    @staticmethod # Execute the query to obtain information from the passenger and booth number
    def returnEstadias():
        # Captures data
        RegistroEstadia.miconexion.execute("""
            SELECT 
                p.idPasajero AS id_pasajero, 
                p.nombre, 
                CONCAT(p.apell_1, ' ', p.apell_2) AS apellidos_completos,
                c.idCabina AS numero_cabina 
                FROM 
                    Registro r
                JOIN 
                    Pasajero p ON r.idPasajero = p.idPasajero
                JOIN 
                    Cabina c ON r.idCabina = c.idCabina;
        """)
        print("\nListado:\n")
        datos = RegistroEstadia.miconexion.fetchall()
        return datos


        
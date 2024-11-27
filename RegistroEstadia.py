from Conexion import conexionDB
from Validaciones import validaString, validaFloatPositivo, validaIntPositivo, validar_fecha
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
            print(f"{'ID':<10} {'Nombre':<20} {'Apellidos':<30}")
            for pasajero in listapasajeros:
                print(f"{pasajero[0]:<10} {pasajero[1]:<20} {pasajero[2]:<30}")
            while True:
                id_pasajero = input("\nDigite el ID del pasajero que desea registrar: ").strip()
                if id_pasajero in ids_validos:
                    self.idPasajero = id_pasajero   # Captures new data for the passenger
                    break
                else:
                    print("\n----ID no válido. Intente nuevamente.----\n")
        while True:
            acompañantes = input("""
            El pasajero viene con acompañantes?
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
            print("\n---- No hay cabinas disponibles ----\n")
        else:
            cabina = int(input("Seleccione el ID de la cabina: ").strip())
            if cabina in ids_disponibles: # Check if the ID exists in the list of available IDs
                self.idCabina = cabina
                self.fechaDeIngreso = validar_fecha("Digite la fecha de ingreso en formato YYYY-MM-DD: ")
    
        self.ingresaRegistroEstadia(self.idCabina, self.idPasajero, self.fechaDeIngreso, self.fechaDeSalida)


    def ingresaRegistroEstadia(self, idCabina, idPasajero, fechaEntrada, fechaSalida):
        consulta = ("INSERT INTO Registro (idCabina, idPasajero, fechaEntrada, fechaSalida) VALUES (%s,%s,%s,%s)")
        datos=(idCabina, idPasajero, fechaEntrada, fechaSalida)
        RegistroEstadia.miconexion.execute(consulta, datos)
        
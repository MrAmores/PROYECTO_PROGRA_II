from Conexion import conexionDB
from RegistroEstadia import RegistroEstadia
from Servicio import Servicio
from Trabajador import Trabajador
from Validaciones import *

class SoliServicio():
    conexion = conexionDB()
    miconexion = conexion.cursor()
    def __init__(self, idSolicitud, idRegistro, idServicio, idTrabajador, fecha, hora):
        self.idSolicitud=idSolicitud
        self.idRegistro=idRegistro
        self.idServicio=idServicio
        self.idTrabajador=idTrabajador
        self.fecha=fecha
        self.hora=hora
        
    def capturaDatos(self):
        listaEstadias = RegistroEstadia.returnEstadias()  # Fetches all passengers
        if not listaEstadias:
            print("\n----No hay pasajeros alojados en el crucero----\n")  # No passengers message
        else:
            print("")
            print(f"{"ID":<10} {"Nombre":<20} {"Apellidos":<30} {"ID Cabina":<20}")
            for estadia in listaEstadias:
                print(f"{estadia[0]:<10} {estadia[1]:<20} {estadia[2]:<30} {estadia[2]:20}")
            while True:
                try:
                    idSeleccionado =input("\nDigite el ID del pasajero que solicita el servicio: \n").strip().upper()
                    # Checks if the ID is in the list of available roles
                    if any(estadia[0] == idSeleccionado for estadia in listaEstadias): # Verifies if the id exitis in the "listaEstadias"
                        self.idRegistro = self.obtener_id_registro(idSeleccionado)
                        break
                    else:
                        print("\n----El ID del pasajero no existe. Por favor, intente nuevamente----\n")
                except ValueError:
                    print("\n----Entrada inválida. Por favor, ingrese un número entero----\n") 
            print("")      
            listServicios = Servicio.select_servicio() # print services if there are
            if not listServicios:
                print("\n----No hay servicios----\n")
            else:
                print(f"{"ID":<10} {"Tipo":<15} {"Descripción":<30} {"Precio":<10}") # Header
                for servicio in listServicios: # Print information if there exists
                    print(f"{servicio[0]:<10} {servicio[1]:<15} {servicio[2]:<30} {servicio[3]:<10.2f}")
                while True:    
                    idServicio = validaIntPositivo("\nDigite el id del servicio que desea: \n")
                    if any(servicio[0] == idServicio for servicio in listServicios): # Verifies if the id exitis
                        self.idServicio = idServicio
                        break
                    else:
                        print("\n----El id no se encuentra en la lista. Intente de nuevo----\n")
                listTrabajadores = Trabajador.trabajadoresActivos()
                if not listTrabajadores:
                    print("\n----No se encuentran trabajadores activos en el sistema----\n")
                else:
                    print("") 
                    print("\nListado de trabajadores activos en el sistema:\n")
                    # Display table header for worker data
                    print(f"{"Identificación":<15} {"Nombre":<15} {"Primer apellido":<20} {"Segundo apellido":<20} {"Año de nacimiento":<18} {"Género":<10} {"N°Rol":<10}")
                    # Display each worker"s data
                    for trabajador in listTrabajadores:
                        print(f"{trabajador[0]:<15} {trabajador[1]:<15} {trabajador[2]:<20} {trabajador[3]:<20} {trabajador[4]:<18} {trabajador[5]:<10} {trabajador[6]:<10}")
                    while True:
                        try:
                            idSeleccionado = input("Digite el ID del trabajador que brindará el servicio: \n").strip().upper()
                            # Check if the ID is valid
                            if any(trabajador[0] == idSeleccionado for trabajador in listTrabajadores):
                                self.idTrabajador = idSeleccionado
                                break
                            else:
                                print("\n----ID no encontrado. Intente nuevamente----\n")
                        except ValueError:
                            print("\n----Ingrese un número válido para el ID----\n")       
                print("")  
                self.fecha = validar_fecha("Digite la fecha de ingreso en formato YYYY-MM-DD: ") # Validate that the date is valid
                self.hora = validar_hora("Digite la hora en formato HH:MM:SS: " ) # Validate that the time is valid
                self.ingresaSolicitudServicio() 
                                                
    # Add a request service
    def ingresaSolicitudServicio(self):
        consulta = ("INSERT INTO solicitudServicio (idRegistro, idServicio, idTrabajador, fecha, hora) VALUES(%s, %s, %s, %s, %s)")
        datos = (self.idRegistro, self.idServicio, self.idTrabajador, self.fecha, self.hora)
        SoliServicio.miconexion.execute(consulta, datos)
        SoliServicio.conexion.commit()
        print("\n=====================================================\n")
        print("Se ha ingresado la solicitud de servicio exitosamente.")
        print("\n=====================================================\n")
    
    # Print the information about passager, worker and services
    def listar(self):
        SoliServicio.miconexion.execute( """
        SELECT 
        ss.idSolicitud AS "Número de servicio",
        CONCAT(p.nombre, ' ', p.apell_1, ' ', p.apell_2) AS "Nombre del cliente",
        p.idPasajero AS "Identificación del cliente",
        c.idCabina AS "Número de Cabina",
        CONCAT(t.nombre, ' ', t.apell_1, ' ', t.apell_2) AS "Nombre del funcionario",
        r.nombre AS "Rol del funcionario",
        ss.fecha AS "Fecha de la solicitud",
        ss.hora AS "Hora de la solicitud",
        se.tipo AS "Servicio",
        se.precio AS "Monto"
            FROM 
                SolicitudServicio ss
            JOIN 
                Registro reg ON ss.idRegistro = reg.idRegistro
            JOIN 
                Pasajero p ON reg.idPasajero = p.idPasajero
            JOIN 
                Cabina c ON reg.idCabina = c.idCabina
            LEFT JOIN 
                Trabajador t ON ss.idTrabajador = t.idTrabajador
            LEFT JOIN 
                Rol r ON t.idRol = r.idRol
            JOIN 
                Servicio se ON ss.idServicio = se.idServicio;
        """)
        # Print about request services
        listado_soli_servicio = SoliServicio.miconexion.fetchall()
        # Print the information of service
        print(f"{"Número de servicio":<20} {"Nombre del cliente":<30} {"Identificación":<25} "
        f"{"Cabina":<20} {"Funcionario":<30} {"Rol":<25} "
        f"{"Fecha":<20} {"Hora":<15} {"Servicio":<20} {"Monto":<10}")
        for servicio in listado_soli_servicio:
            fecha = servicio[6].strftime("%Y-%m-%d")  
            hora = str(servicio[7])  
            print(f"{str(servicio[0]):<20} {str(servicio[1]):<30} {str(servicio[2]):<25} "
          f"{str(servicio[3]):<20} {str(servicio[4]):<30} {str(servicio[5]):<25} "
          f"{fecha:<20} {hora:<15} {str(servicio[8]):<20} {servicio[9]:<10.2f}")
        
    def obtener_id_registro(self, idPasajero):
            """Método para obtener el idRegistro del pasajero"""
            try:
                SoliServicio.miconexion.execute("SELECT idRegistro FROM Registro WHERE idPasajero = %s", (idPasajero,)) # Get the id register
                resultado = SoliServicio.miconexion.fetchone()
                if resultado:
                    return resultado[0]  # Return if the id exists
                else:
                    print("\n----No se encontró un registro para el pasajero seleccionado----\n")
                    return None  # Return None if the id not exists
            except Exception as e:
                print(f"Error al obtener el idRegistro: {e}")
                return None
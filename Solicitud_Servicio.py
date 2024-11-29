from Conexion import conexionDB
class SoliServicio():
    conexion = conexionDB()
    miconexion = conexion.cursor()
    def __init__(self, idSolicitud, idPasajero, idCabina, idServicio, idTrabajador, fecha, hora):
        self.idSolicitud=idSolicitud
        self.idPasajero=idPasajero
        self.idCabina=idCabina
        self.idServicio=idServicio
        self.idTrabajador=idTrabajador
        self.fecha=fecha
        self.hora=hora
        
    def capturaDatos(self):
        pass
    
    def ingresaSolicitudServicio(self):
        pass
    
    
    def listar(self):
        consulta = """
        SELECT 
            ss.idSolicitud AS "Número de servicio",
            CONCAT(p.nombre,' ',p.apell_1, ' ', p.apell_2) AS "Nombre del cliente",
            p.idPasajero AS "Identificación del cliente",
            c.idCabina AS "Número de Cabina",
            concat(t.nombre, ' ',t.apell_1, ' ',t.apell_2)AS "Nombre del funcionario",
            r.nombre AS "Rol del funcionario",
            ss.fecha AS "Fecha de la solicitud",
            ss.hora AS "Hora de la solicitud",
            se.tipo AS "Servicio",
            se.precio AS "Monto"
        FROM 
            SolicitudServicio ss
        JOIN 
            Pasajero p ON ss.idPasajero = p.idPasajero
        JOIN 
            Cabina c ON ss.idCabina = c.idCabina
        JOIN 
            Trabajador t ON ss.idTrabajador = t.idTrabajador
        JOIN 
            Rol r ON t.idRol = r.idRol
        JOIN 
            Servicio se ON ss.idServicio = se.idServicio;
        """
        
        SoliServicio.miconexion.execute(consulta)
        listado_soli_servicio = SoliServicio.miconexion.fetchall()
        # Imprimir los resultados con formato
        print(f"{"Número de servicio":<20} {"Nombre del cliente":<30} {"Identificación":<25} "
        f"{"Cabina":<20} {"Funcionario":<30} {"Rol":<25} "
        f"{"Fecha":<20} {"Hora":<15} {"Servicio":<20} {"Monto":<10}")
        for servicio in listado_soli_servicio:
            fecha = servicio[6].strftime("%Y-%m-%d")  
            hora = str(servicio[7])  
            print(f"{str(servicio[0]):<20} {str(servicio[1]):<30} {str(servicio[2]):<25} "
          f"{str(servicio[3]):<20} {str(servicio[4]):<30} {str(servicio[5]):<25} "
          f"{fecha:<20} {hora:<15} {str(servicio[8]):<20} {servicio[9]:<10.2f}")
            
#obj = SoliServicio("","","","","","","")
#obj.listar()            
     


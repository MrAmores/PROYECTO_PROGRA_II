from Conexion import conexionDB
from Validaciones import *

class Cabina:
    conexion = conexionDB()
    miconexion = conexion.cursor()

    def __init__(self, idCabina, capacidad, disponibilidad, tamanho, precio):
        # Initializes a Cabina object with ID, capacity, availability, size, and price
        self.idCabina = idCabina
        self.capacidad = capacidad
        self.disponibilidad = disponibilidad
        self.tamanho = tamanho
        self.precio = precio

    def capturaDatos(self):
        # Captures and validates data for a new cabin
        while True:
            self.idCabina = validaIntPositivo("Digite el ID de la cabina: ")
            # Check if the idCabina already exists in the database
            Cabina.miconexion.execute("SELECT COUNT(*) FROM cabina WHERE idCabina = %s", (self.idCabina,))
            if Cabina.miconexion.fetchone()[0] > 0:
                print("\n----El ID de la cabina ya existe. Por favor, ingrese un ID único----\n")
            else:
                self.disponibilidad = True
                break
        
        # Validation of capacity
        print("")
        self.capacidad = validaIntPositivo("Digite la capacidad de personas que permite la cabina: ")
        
        # Validation of size
        while True:
            print("""
            Seleccione el tamaño de la cabina:
            1 - Pequeña
            2 - Mediana
            3 - Grande
            """)
            print("")
            opcion = input("Digite el número correspondiente al tamaño de la cabina: ").strip()
            if opcion == "1":
                self.tamanho = "Pequeña"
                break
            elif opcion == "2":
                self.tamanho = "Mediana"
                break
            elif opcion == "3":
                self.tamanho = "Grande"
                break
            else:
                print("\n----Opción inválida. Por favor, seleccione 1, 2 o 3----\n")         

        # Validation of price
        print("")
        self.precio = validaFloatPositivo("Digite el precio de la cabina: ")
           
    def ingresaCabina(self):
        # Inserts a new cabin into the database
        ingreso = "INSERT INTO cabina (idCabina, capacidad, disponibilidad, tamanho, precio) VALUES (%s, %s, %s, %s, %s)"
        datos = (self.idCabina, self.capacidad, self.disponibilidad, self.tamanho, self.precio)
        Cabina.miconexion.execute(ingreso, datos)  # Execute the query and enter data
        Cabina.conexion.commit()
        print("\n=======================================")
        print("Se ha ingresado la cabina exitosamente.")
        print("=======================================\n")

    def modificar(self, capacidad, disponibilidad, tamanho, precio, id):
        # Modifies an existing cabin in the database
        modificar = ( 
            "UPDATE cabina SET capacidad = %s, "
            "disponibilidad = %s, "
            "tamanho = %s,"
            "precio = %s "
            "WHERE idCabina = %s")
        datos = (capacidad, disponibilidad, tamanho, precio, id)
        Cabina.miconexion.execute(modificar, datos)  # Execute the query and modify data
        Cabina.conexion.commit()
        print("\n======================================================")
        print("Se han modificado los datos de la cabina exitosamente.")
        print("======================================================\n")
        
    def listar(self):
        # Lists all cabins in the system
        print("\nListado de cabinas en el sistema:\n")
        Cabina.miconexion.execute("SELECT * FROM cabina")  # Execute query and list data
        datos = Cabina.miconexion.fetchall()
        print(f"{"ID Cabina":<10} {"Capacidad":<15} {"Disponibilidad":<15} {"Tamaño":<15} {"Precio":<10}")
        for dato in datos:
            # Interpretar disponibilidad basada en 1 o 0
            disponibilidad = "Disponible" if dato[2] == 1 else "No Disponible"
            print(f"{dato[0]:<10} {dato[1]:<15} {disponibilidad:<15} {dato[3]:<15} {dato[4]:<10.2f}")

            
    def desactivar(self, id):
        # Marks a cabin as unavailable in the database
        modificar = "UPDATE cabina SET disponibilidad = %s WHERE idCabina = %s"
        datos = (False, id)
        Cabina.miconexion.execute(modificar, datos)  # Execute the query and inactivate data
        Cabina.conexion.commit()
        print("\n=====================================")
        print("Se ha borrado la cabina exitosamente.")
        print("=====================================\n")
        
    @staticmethod
    def obtener_cabinas_disponibles(acompanantes):
        # Retrieves available cabins based on the required capacity
        capacidad_cabina = acompanantes + 1
        consulta = """
        SELECT idCabina, capacidad, tamanho, precio FROM cabina
        WHERE disponibilidad = TRUE AND capacidad = %s
        ORDER BY capacidad;
        """
        Cabina.miconexion.execute(consulta, (capacidad_cabina,))
        cabinas_disponibles = Cabina.miconexion.fetchall()

        # Collects and displays available cabins
        ids_disponibles = [cabina[0] for cabina in cabinas_disponibles]
        if cabinas_disponibles:
            print(f"\nCabinas disponibles para {capacidad_cabina} personas:\n")
            print(f"{"ID":<10} {"Capacidad":<15} {"Tamaño":<15} {"Precio":<10}")
            for cabina in cabinas_disponibles:
                print(f"{cabina[0]:<10} {cabina[1]:<15} {cabina[2]:<15} {cabina[3]:<10.2f}")
        return ids_disponibles

    @staticmethod
    def pasar_cabina_a_ocupada(id_Cabina):
        # Marks a cabin as occupied in the database
        update = "UPDATE cabina SET disponibilidad = FALSE WHERE idCabina = %s"
        Cabina.miconexion.execute(update, (id_Cabina,))
        Cabina.conexion.commit()

    @staticmethod
    def select_cabina():
        # Retrieves all cabins from the database
        consulta = "SELECT idCabina, capacidad, tamanho, disponibilidad, precio FROM cabina"
        Cabina.miconexion.execute(consulta)
        cabinas = Cabina.miconexion.fetchall()
        return cabinas  # Return list of tuples

    def cabinas4personas(self):
        Cabina.miconexion.execute("SELECT * FROM cabina WHERE capacidad = 4")  # Execute query and list data
        datos = Cabina.miconexion.fetchall()
        if not datos:
            print("\n----No hay cabinas para cuatro persoans en el sistema----\n")
        else:
            print(f"{"ID Cabina":<10} {"Capacidad":<15} {"Disponibilidad":<15} {"Tamaño":<15} {"Precio":<10}")
            for dato in datos:
                # Interpretar disponibilidad basada en 1 o 0
                disponibilidad = "Disponible" if dato[2] == 1 else "No Disponible"
                print(f"{dato[0]:<10} {dato[1]:<15} {disponibilidad:<15} {dato[3]:<15} {dato[4]:<10.2f}")
from Conexion import conexionDB
class Cabina():
    conexion = conexionDB()
    miconexion = conexion.cursor()

    def __init__(self, idCabina, capacidad, disponibilidad, tamanho, precio):
        self.idCabina = idCabina
        self.capacidad = capacidad
        self.disponibilidad = disponibilidad
        self.tamanho = tamanho
        self.precio = precio

    def capturaDatos(self):
    # Validation of idCabina
        while True:
            try:
                self.idCabina = int(input("Digite el ID de la cabina: ").strip())
                # Check if the idCabina already exists in the database
                Cabina.miconexion.execute("SELECT COUNT(*) FROM cabina WHERE idCabina = %s", (self.idCabina,))
                if Cabina.miconexion.fetchone()[0] > 0:
                    print("El ID de la cabina ya existe. Por favor, ingrese un ID único.")
                elif self.idCabina < 0:
                    print("No se permiten números negativos.")
                else:
                    self.disponibilidad = True
                    break
            except ValueError:
                print("Entrada inválida. El ID de la cabina debe de ser un número entero.")
                        
        # Validation of capacity
        while True:
            try:
                self.capacidad = int(input("Digite la capacidad de personas que permite la cabina: ").strip())
                if self.capacidad <= 0:
                    print("La cabina por lo menos debe tener capacidad para un pasajero.")
                else:
                    break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
        
        # Validation of size
        while True:
            print("Seleccione el tamaño de la cabina:")
            print("1 - Pequeña")
            print("2 - Mediana")
            print("3 - Grande")
            
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
                print("Opción inválida. Por favor, seleccione 1, 2 o 3.")
                    
        # Validation of price
        while True:
            try:
                entrada_precio = input("Digite el precio de la cabina: ").strip()
                precio = float(entrada_precio)
                if precio > 0:
                    self.precio = precio
                    break
                else:
                    print("El precio debe ser un número positivo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")

    def ingresaCabina(self):
        # Consulta SQL de inserción
        ingreso = "INSERT INTO cabina (idCabina, capacidad, disponibilidad, tamanho, precio) VALUES (%s, %s, %s, %s, %s)"
        datos = (self.idCabina, self.capacidad, self.disponibilidad, self.tamanho, self.precio)
        # Ejecutar la consulta e ingresar datos
        Cabina.miconexion.execute(ingreso, datos)
        Cabina.conexion.commit()
        print("Se ha ingresado la cabina exitosamente.")

    def modificar(self,capacidad, disponibilidad, tamanho, precio, id):
        # Consulta SQL de modificación
        modificar = ("update cabina set capacidad = %s, "
         "disponibilidad = %s, "
         "tamanho = %s,"
         "precio = %s"
         "where idCabina = %s")
        datos = (capacidad, disponibilidad, tamanho, precio, id)
        # Ejecutar la consulta y modificar datos
        Cabina.miconexion.execute(modificar, datos)
        Cabina.conexion.commit()
        print("Se han modificado los datos de la cabina exitosamente.")
    
    def listar(self):
        print("Listado de cabinas en el sistema:")
        # Execute query and list data
        Cabina.miconexion.execute("select * from cabina")
        datos = Cabina.miconexion.fetchall()
        for i in datos:
            print(f"ID Cabina: {i[0]}, Capacidad: {i[1]}, Disponibilidad: {i[2]}, Tamaño: {i[3]}, Precio: {i[4]}")

    def desactivar(self,id):
        modificar = "UPDATE cabina SET disponibilidad = %s WHERE idCabina = %s"
        datos = (False, id)
        # Ejecutar la consulta y inactivar datos
        Cabina.miconexion.execute(modificar, datos)
        Cabina.conexion.commit()
        print("Se ha borrado la cabina exitosamente.")
        
    @staticmethod
    def obtener_cabinas_disponibles(acompanantes):
            capacidad_cabina = acompanantes + 1
            # Query to filter available cabins according to required capacity
            consulta = """
            SELECT idCabina,capacidad,tamanho,precio FROM cabina
            WHERE disponibilidad = TRUE AND capacidad = %s
            ORDER BY capacidad;
            """
            Cabina.miconexion.execute(consulta, (capacidad_cabina,))
            cabinas_disponibles = Cabina.miconexion.fetchall()
            
            # Collect the IDs of the available booths in a list
            ids_disponibles = [cabina[0] for cabina in cabinas_disponibles]
            
            # Display the results to the user
            if cabinas_disponibles:
                print(f"\nCabinas disponibles para {capacidad_cabina} personas:")
                for cabina in cabinas_disponibles:
                    print(f"ID: {cabina[0]}, Capacidad: {cabina[1]}, Disponibilidad: {cabina[2]}, Tamaño: {cabina[3]}, Precio: {cabina[4]}")
                    
            return ids_disponibles
        
    @staticmethod
    def pasar_cabina_a_ocupada(id_Cabina):
        update = ("UPDATE cabina SET disponibilidad = FALSE WHERE idCabina = %s  ")
        Cabina.miconexion.execute(update,(id_Cabina,))
        Cabina.conexion.commit()
        
    @staticmethod
    def select_cabina():
        # Query para obtener las cabinas
        consulta = "SELECT idCabina, capacidad, tamanho, disponibilidad, precio FROM cabina"
        Cabina.miconexion.execute(consulta)
        cabinas = Cabina.miconexion.fetchall()  # Retorna lista de tuplas
        return cabinas
    

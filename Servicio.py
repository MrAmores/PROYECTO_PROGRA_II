from Conexion import conexionDB
from Validaciones import *

class Servicio:
    conexion = conexionDB()
    miconexion = conexion.cursor()

    def __init__(self, idServicio, tipo, descripcion, precio):
        # Initializes a Servicio object with ID, type, description, and price
        self.idServicio = idServicio
        self.tipo = tipo
        self.descripcion = descripcion
        self.precio = precio

    def capturaDatos(self):
        # Captures and validates the data for a new service
        while True:
            try:
                self.idServicio = validaIntPositivo("Digite el número de identificación del servicio: ")
                # Check if the service ID already exists in the database
                verificar_id = "SELECT COUNT(*) FROM servicio WHERE idServicio = %s"
                Servicio.miconexion.execute(verificar_id, (self.idServicio,))
                resultado = Servicio.miconexion.fetchone()
                if resultado[0] > 0:
                    print(f"\n----El ID {self.idServicio} ya existe. Por favor, ingrese un ID distinto---\n")
                else:
                    break
            except ValueError:
                print("\n----Entrada inválida. Por favor, intente nuevamente----\n")
        
        # Validates the service type
        try:
            while True:
                self.tipo = input("Digite el tipo del servicio: ").strip()
                if self.tipo:
                    break
                else:
                    print("\n----El tipo no puede estar vacío o contener solo espacios----\n")
        except ValueError as e:
            print(f"----\n{e} Entrada inválida. Por favor, intente nuevamente----\n")
        
        # Validates the service description
        try:
            while True:
                self.descripcion = input("Digite la descripción del servicio: ").strip()
                if self.descripcion:
                    break
                else:
                    print("\n----La descripción no puede estar vacía o contener solo espacios----\n")
        except ValueError as e:
            print(f"\n----{e} Entrada inválida. Por favor, intente nuevamente----\n")
        
        # Validates the service price
        try:
            while True:
                try:
                    precio = float(input("Digite el precio del servicio: ").strip())
                    if precio > 0:
                        self.precio = precio
                        break
                    else:
                        print("\n----El precio debe ser un número positivo----\n")
                except ValueError:
                    print("\nEntrada inválida. Por favor, ingrese un número----\n")
        except ValueError as e:
            print(f"\n----{e} Entrada inválida. Por favor, intente nuevamente----\n")

    # Inserts a new service into the database
    def ingresaServicio(self):
        try:
            ingreso = "INSERT INTO servicio (idServicio, tipo, descripcion, precio) VALUES (%s, %s, %s, %s)"
            datos = (self.idServicio, self.tipo, self.descripcion, self.precio)
            Servicio.miconexion.execute(ingreso, datos)
            Servicio.conexion.commit()
            print("\n=========================================")
            print("Se ha ingresado el servicio exitosamente.")
            print("=========================================\n")
        except Exception as e:
            print(f"\n----Error inesperado: {e}. Por favor, intente nuevamente----\n")
    
    # Modifies an existing service in the database
    def modificaServicio(self):

        try:
            while True:
                id = validaIntPositivo("Digite un ID del servicio que desea modificar: ")
                verificar_id = "SELECT COUNT(*) FROM servicio WHERE idServicio = %s"
                Servicio.miconexion.execute(verificar_id, (id,))
                resultado = Servicio.miconexion.fetchone()
                if resultado[0] == 0:
                    print(f"\n----El ID {id} no existe en la base de datos----\n")
                else:
                    break
            tipo=validaString("Digite el tipo: ")
            descripcion=validaString("Digite la descripción: ")
            precio=float(validaFloatPositivo("Digite el precio: "))    
            modificar = "UPDATE servicio SET tipo = %s, descripcion = %s, precio = %s WHERE idServicio = %s"
            datos = (tipo, descripcion, precio,id)
            Servicio.miconexion.execute(modificar, datos)
            Servicio.conexion.commit()
            print("\n=====================================================")
            print("Se han modificado los datos del servicio exitosamente")
            print("=====================================================\n")
        except Exception as e:
            print(f"\n----Error al modificar el servicio: {e}----\n")
    
    # Lists all services in the database
    def listar(self):
        
        print("Listado de servicios:")
        Servicio.miconexion.execute("SELECT idServicio, tipo, descripcion, precio FROM servicio")
        servicios = Servicio.miconexion.fetchall()
        print(f"{"ID":<10} {"Tipo":<15} {"Descripción":<30} {"Precio":<10}")
        for servicio in servicios:
            print(f"{servicio[0]:<10} {servicio[1]:<15} {servicio[2]:<30} {servicio[3]:<10.2f}")
    
    # Deletes a service from the database
    def borraServicio(self, id):
        
        try:
            if id <= 0:
                print("\n----El número de identificación debe ser un valor positivo----\n")
                return  False
            verificar_id = "SELECT COUNT(*) FROM servicio WHERE idServicio = %s"
            Servicio.miconexion.execute(verificar_id, (id,))
            resultado = Servicio.miconexion.fetchone()
            if resultado[0] == 0:
                print(f"\n----El ID {id} no existe en la base de datos. No se puede eliminar----\n")
                return False
            eliminar = "DELETE FROM servicio WHERE idServicio = %s"
            datos = (id,)
            Servicio.miconexion.execute(eliminar, datos)
            Servicio.conexion.commit()
            print("\n----Se ha borrado el servicio exitosamente----\n")
            return True
        except Exception as e:
            print(f"\n----Error inesperado: {e}----\n")
    
    @staticmethod            
    def select_servicio():
        print("Listado de servicios:")
        Servicio.miconexion.execute("SELECT idServicio, tipo, descripcion, precio FROM servicio")
        servicios = Servicio.miconexion.fetchall()
        return servicios
                
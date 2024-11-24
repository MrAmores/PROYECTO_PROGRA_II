from Conexion import conexionDB
from Validaciones import *

class Servicio():
    conexion = conexionDB()
    miconexion = conexion.cursor()

    def __init__(self, idServicio, tipo, descripcion, precio):
        self.idServicio = idServicio
        self.tipo = tipo
        self.idServicio = idServicio
        self.descripcion = descripcion
        self.precio = precio
        

    def capturaDatos(self):
    # Validación del número de identificación del servicio, evitando duplicados
        while True:
            try:
                self.idServicio = validaIntPositivo("Digite el número de identificación del servicio: ")

                if self.idServicio <= 0:
                    print("El número de identificación debe ser un valor positivo.")
                    continue

                # Verificar si el ID ya existe en la base de datos
                verificar_id = "SELECT COUNT(*) FROM servicio WHERE idServicio = %s"
                Servicio.miconexion.execute(verificar_id, (self.idServicio,))
                resultado = Servicio.miconexion.fetchone()

                if resultado[0] > 0:
                    print(f"El ID '{self.idServicio}' ya existe. Por favor, ingrese un ID distinto.")
                else:
                    # Si el ID es válido y no existe en la base de datos, romper el ciclo
                    break

            except ValueError:
                print("Entrada inválida. Por favor, intente nuevamente.")

            
            # Validación del tipo de servicio
        try:
            while True:
                self.tipo = input("Digite el tipo del servicio: ").strip()
                if self.tipo:
                    break
                else:
                    print("El tipo no puede estar vacío o contener solo espacios.")
        
        except ValueError as e:
            print(f"{e} Entrada inválida. Por favor, intente nuevamente")

            # Validación de la descripción del servicio
            
        try:    
            while True:
                self.descripcion = input("Digite la descripción del servicio: ").strip()
                if self.descripcion:
                    break
                else:
                    print("La descripción no puede estar vacía o contener solo espacios.")

        except ValueError as e:
            print(f"{e} Entrada inválida. Por favor, intente nuevamente")

        try:        
            # Validación del precio del servicio
            while True:
                try:
                    precio = float(input("Digite el precio del servicio: ").strip())
                    if precio > 0:
                        self.precio = precio
                        break
                    else:
                        print("El precio debe ser un número positivo.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
        except ValueError as e:
            print(f"{e} Entrada inválida. Por favor, intente nuevamente")
    
    def ingresaServicio(self):
        try:
    # Consulta SQL de inserción
            ingreso = "INSERT INTO servicio (idServicio, tipo, descripcion, precio) VALUES (%s, %s, %s, %s)"
            datos = (self.idServicio, self.tipo, self.descripcion, self.precio)
            # Ejecutar la consulta e ingresar datos
            try:
                Servicio.miconexion.execute(ingreso, datos)
                Servicio.conexion.commit()
                print("Se ha ingresado el servicio exitosamente.")
            except ValueError as e:
                print(f"{e} Error inesperado. Por favor, intente nuevamente")

        except ValueError as e:
            print(f"{e} Entrada inválida. Por favor, intente nuevamente")
    
    
    
    def modificaServicio(self, tipo, descripcion, precio, id):
        try:
            while True:
                # Verificar si el ID existe en la base de datos
                verificar_id = "SELECT COUNT(*) FROM servicio WHERE idServicio = %s"
                Servicio.miconexion.execute(verificar_id, (id,))
                resultado = Servicio.miconexion.fetchone()

                if resultado[0] == 0:
                    print(f"El ID '{id}' no existe en la base de datos.")
                    id = validaIntPositivo("Digite un ID válido del servicio que desea modificar: ")
                else:
                    break  # Sale del bucle si el ID existe

            # Actualizar los datos en la base de datos
            modificar = "UPDATE servicio SET tipo = %s, descripcion = %s, precio = %s WHERE idServicio = %s"
            datos = (tipo, descripcion, precio, id)

            Servicio.miconexion.execute(modificar, datos)
            Servicio.conexion.commit()
            print("Se han modificado los datos del servicio exitosamente.")

        except Exception as e:
            print(f"Error al modificar el servicio: {e}")


    def listar(self):
        print("Listado de servicios:")
        Servicio.miconexion.execute("SELECT idServicio, tipo, descripcion, precio FROM servicio")
        servicios = Servicio.miconexion.fetchall()
        print(f"{'ID':<10} {'Tipo':<15} {'Descripción':<30} {'Precio':<10}")
        for servicio in servicios:
            print(f"{servicio[0]:<10} {servicio[1]:<15} {servicio[2]:<30} {servicio[3]:<10.2f}")

    def borraServicio(self, id):
        try:
        # Validar que el ID sea un número entero positivo
            if id <= 0:
                print("El número de identificación debe ser un valor positivo.")
                return

            # Verificar si el ID existe en la base de datos
            verificar_id = "SELECT COUNT(*) FROM servicio WHERE idServicio = %s"
            Servicio.miconexion.execute(verificar_id, (id,))
            resultado = Servicio.miconexion.fetchone()

            if resultado[0] == 0:
                print(f"El ID '{id}' no existe en la base de datos. No se puede eliminar.")
                return

            # Si el ID existe, procedemos a eliminarlo
            eliminar = "DELETE FROM servicio WHERE idServicio = %s"
            datos = (id,)
            Servicio.miconexion.execute(eliminar, datos)
            Servicio.conexion.commit()
            print("Se ha borrado el servicio exitosamente.")

        except ValueError as e:
            print(f"Error: {e}. Entrada inválida. Por favor, intente nuevamente.")
        except Exception as e:
            print(f"Error inesperado: {e}.")

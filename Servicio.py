from Conexion import conexionDB
from Validaciones import validaIntPositivo

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
            Servicio.miconexion.execute(ingreso, datos)
            Servicio.conexion.commit()
            print("Se ha ingresado el servicio exitosamente.")
        except ValueError as e:
            print(f"{e} Entrada inválida. Por favor, intente nuevamente")
    
    def modificaServicio(self, tipo, descripcion, precio, id):
        try:

    # Validar que el ID exista en la base de datos antes de proceder con la modificación
            while True:
                if id <= 0:
                    verificar_id = "SELECT COUNT(*) FROM servicio WHERE idServicio = %s"
                    Servicio.miconexion.execute(verificar_id, (id,))
                    resultado = Servicio.miconexion.fetchone()

                if resultado[0] == 0:
                    print(f"El ID '{id}' no existe en la base de datos. Por favor, ingrese un ID válido para modificar.")
                    id = input("Digite un ID válido del servicio que desea modificar: ").strip()
                else:
                    break

            # Consulta SQL de modificación
            modificar = ("UPDATE Servicio SET tipo = %s, "
                        "descripcion = %s, "
                        "precio = %s "
                        "WHERE idServicio = %s")
            datos = (tipo, descripcion, precio, id)

            # Ejecutar la consulta y modificar datos
            Servicio.miconexion.execute(modificar, datos)
            Servicio.conexion.commit()
            print("Se han modificado los datos del servicio exitosamente.")
        except ValueError as e:
            print(f"{e} Entrada inválida. Por favor, intente nuevamente")


    def listar(self):
        print("Listado de servicios en el sistema:")
        # Ejecutar la consulta y listar datos
        Servicio.miconexion.execute("select * from Servicio")
        datos = Servicio.miconexion.fetchall()
        for i in datos:
            print(i)
    
    def borraServicio(self, id):
        try:

            while True:
                if id <= 0:
                    verificar_id = "SELECT COUNT(*) FROM servicio WHERE idServicio = %s"
                    Servicio.miconexion.execute(verificar_id, (id,))
                    resultado = Servicio.miconexion.fetchone()
                else: 
                    print(f"El número de identificación [{id}]debe ser un número positivo ")
                    id = input("Digite un ID válido del servicio que desea eliminar: ").strip()

                if resultado[0] == 0:
                    print(f"El ID '{id}' no existe en la base de datos. Por favor, ingrese un ID válido para modificar.")
                    id = input("Digite un ID válido del servicio que desea eliminar: ").strip()
                else:
                    break

            eliminar = "DELETE FROM Servicio WHERE idServicio = %s"
            datos = (id,)
            # Ejecutar la consulta y eliminar el servicio
            Servicio.miconexion.execute(eliminar, datos)
            Servicio.conexion.commit()
            print("Se ha borrado el servicio exitosamente.")

        except ValueError as e:
            print(f"{e} Entrada inválida. Por favor, intente nuevamente")
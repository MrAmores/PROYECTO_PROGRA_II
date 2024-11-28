from Pasajero import Pasajero
from Trabajador import Trabajador
from Rol import Rol
from Cabina import Cabina
from Servicio import Servicio
from RegistroEstadia import RegistroEstadia
from Validaciones import *

# Displays the main menu and directs to the corresponding submenu based on user input
def mostrar_menu_principal():
    opc = 0
    while True:
        print("""
        --------------------------------------
        ---       Sistema de Gestión       ---
        --------------------------------------
        1 - Gestión Pasajeros
        2 - Gestión Trabajadores
        3 - Gestión Cabinas
        4 - Gestión de Roles
        5 - Gestión Servicios
        6 - Gestión de Solicitud de Servicios
        7 - Gestión de registro de pasajero a cabina
        8 - Salir
        --------------------------------------
        """)
        try:
            opc = int(input("Seleccione una opción: "))  # Prompts the user to select an option
            if opc == 1:
                mostrar_menu_pasajero()  # Calls the passenger management menu
            elif opc == 2:
                mostrar_menu_trabajador()  # Calls the worker management menu
            elif opc == 3:
                mostrar_menu_cabina()  # Calls the cabin management menu
            elif opc == 4:
                mostrar_menu_rol()  # Calls the role management menu
            elif opc == 5:
                mostrar_menu_servicio()  # Calls the service management menu
            elif opc == 6:
                mostrar_menu_solicitud_servicio()  # Calls the service request menu
            elif opc == 7:
                mostrar_menu_registro_pasajero_a_cabina()  # Calls the client register to room  menu    
            elif opc == 8:
                print("SALIENDO DEL SISTEMA")  # Exits the system
                break
            else:
                print("\n----Opción no valida. Intente de nuevo----\n")  # Invalid option message
        except ValueError as e:
            print(f"\n----Error: {e}. Intente ingresar un número válido----\n")  # Error message for invalid input

# Displays the passenger management menu and performs actions based on the user's choice
def mostrar_menu_pasajero():
    objPasajero = Pasajero(
        identificacion=None, nombre=None, apellido1=None, apellido2=None,
        anhoNacimiento=None, genero=None, activo=None)

    while True:
        print("""
        ------------------------------
        ---  Gestión de Pasajeros  ---   
        ------------------------------
        1 - Registrar Pasajero
        2 - Modificar Pasajero
        3 - Eliminar Pasajero
        4 - Listar Pasajeros
        5 - Volver al Menú Principal
        ------------------------------
        """)
        try:
            opcion = int(input("Seleccione una opción: "))  # Prompts the user to select an option

            if opcion == 1:
                objPasajero.capturaDatosNuevos()  # Registers a new passenger

            elif opcion == 2:
                # Modify an existing passenger
                listapasajeros = Pasajero.select_pasajero()  # Fetches all passengers
                if not listapasajeros:
                    print("\n----No hay pasajeros registrados para modificar----\n")  # No passengers message
                else:
                    ids_validos = [pasajero[0] for pasajero in listapasajeros]  # Collect valid IDs

                    # Displays the list of passengers
                    print("")
                    print(f"{'ID':<10} {'Nombre':<20} {'Apellidos':<30}")
                    for pasajero in listapasajeros:
                        print(f"{pasajero[0]:<10} {pasajero[1]:<20} {pasajero[2]:<30}")

                    while True:
                        id_pasajero = input("\nDigite el ID del pasajero que desea modificar: ").strip().upper()
                        if id_pasajero in ids_validos:
                            objPasajero.capturaDatosMod(id_pasajero)  # Captures new data for the passenger
                            break
                        else:
                            print("\n----ID no válido. Intente nuevamente.----\n")  # Invalid ID message

            elif opcion == 3:
                # Deletes a passenger
                listapasajeros = Pasajero.select_pasajero()  # Fetches all passengers
                
                if not listapasajeros:
                    print("\n----No hay pasajeros registrados para eliminar----\n")  # No passengers message
                    
                else:
                    ids_validos = [pas[0] for pas in listapasajeros]  # Collect valid IDs

                    # Displays the list of passengers
                    print("")
                    print(f"{'ID':<10} {'Nombre':<20} {'Apellidos':<30}")
                    for pasajero in listapasajeros: 
                        print(f"{pasajero[0]:<10} {pasajero[1]:<20} {pasajero[2]:<30}")

                    while True:
                        idPasajero = input("\nDigite el ID del pasajero a eliminar: ").strip()
                        if idPasajero in ids_validos:
                            objPasajero.desactiva(idPasajero)  # Deactivates the passenger
                            break
                        print("\n----ID no válido. Intente nuevamente.----\n")  # Invalid ID message

            elif opcion == 4:
                objPasajero.listaDatos()  # Lists all active passengers

            elif opcion == 5:
                print("\n----Volviendo al menú principal.----\n")  # Returns to the main menu
                break

            else:
                print("\n----Opción no válida. Intente de nuevo.----\n")  # Invalid option message

        except ValueError:
            print("\n----Entrada inválida. Por favor, ingrese un número válido.----\n")  # Invalid input message

def mostrar_menu_trabajador():
    # Display and handle options for worker management
    objTrabajador = Trabajador(identificacion=None, nombre=None, apellido1=None, apellido2=None, anhoNacimiento=None, genero=None, activo=None, idRol=None)
    while True:
        print("""
        ------------------------------
        --  Gestión de Trabajadores --   
        ------------------------------
        1 - Registrar Trabajador
        2 - Modificar Trabajador
        3 - Eliminar Trabajador
        4 - Listar Trabajador
        5 - Volver al Menú Principal
        ------------------------------
        """)
        try:
            opcion = int(input("Selecione una opción: "))
            print("")
            if opcion == 1:
                # Validate if there are roles before registering a worker
                listRoles = Rol.returnListaRol()
                if not listRoles:
                    print("\n---No hay roles en el sistema. Debe ingresar primero un rol---\n")
                else:    
                    objTrabajador.capturaDatosNuevos()
                    objTrabajador.ingresaDatos()
                
            elif opcion == 2:
                # Modify a worker's information
                listTrabajadores = objTrabajador.trabajadoresActivos()
                if not listTrabajadores:
                    print("\n----No se encuentran trabajadores activos en el sistema----\n")
                else:
                    print("Listado de trabajadores activos en el sistema:")
                    # Display table header for worker data
                    print(f"{'Identificación':<15} {'Nombre':<15} {'Primer apellido':<20} {'Segundo apellido':<20} {'Año de nacimiento':<18} {'Género':<10} {'N°Rol':<10}")
                    # Display each worker's data
                    for trabajador in listTrabajadores:
                        print(f"{trabajador[0]:<15} {trabajador[1]:<15} {trabajador[2]:<20} {trabajador[3]:<20} {trabajador[4]:<18} {trabajador[5]:<10} {trabajador[6]:<10}")

                    while True:
                        try:
                            idSeleccionado = input("Digite el ID del trabajador que desea modificar: ").strip().upper()
                            # Check if the ID is valid
                            if any(trabajador[0] == idSeleccionado for trabajador in listTrabajadores):
                                objTrabajador.capturaDatosMod(idSeleccionado)
                                break
                            else:
                                print("\n----ID no encontrado. Intente nuevamente----\n")
                        except ValueError:
                            print("\n----Ingrese un número válido para el ID----\n")
            elif opcion == 3:
                # Deactivate a worker
                listTrabajadores = objTrabajador.trabajadoresActivos()
                if not listTrabajadores:  # If no workers are active
                    print("\n----No se encuentran trabajadores activos en el sistema----\n")
                else:
                    print("Listado de trabajadores activos en el sistema:")
                    # Display table header
                    print(f"{'Identificación':<15} {'Nombre':<15} {'Apellido 1':<20} {'Apellido 2':<20} {'Año nacimiento':<15} {'Género':<10} {'Id rol':<10}")
                    # Display each worker's data
                    for trabajador in listTrabajadores:
                        print(f"{trabajador[0]:<15} {trabajador[1]:<15} {trabajador[2]:<20} {trabajador[3]:<20} {trabajador[4]:<15} {trabajador[5]:<10} {trabajador[6]:<10}")

                    while True:
                        try:
                            idSeleccionado = input("\nDigite el ID del trabajador que desea desactivar: ").strip().upper()
                            # Check if the ID is valid
                            if any(trabajador[0] == idSeleccionado for trabajador in listTrabajadores):
                                objTrabajador.desactiva(idSeleccionado)
                                break
                            else:
                                print("\n----ID no encontrado. Intente nuevamente----\n")
                        except ValueError:
                            print("\n----Ingrese un número válido para el ID----\n")
            elif opcion == 4:
                # List all workers
                objTrabajador.listaDatos()
            elif opcion == 5:
                # Exit to main menu
                break
            else:
                print("\n----Opción no válida. Intente de nuevo----\n")
        except ValueError as e: 
            print(f"\n----Error: {e}. Intente ingresar un número válido---\n")

def mostrar_menu_cabina():
    # Display and handle options for cabin management
    objCabina = Cabina(idCabina=None, capacidad=None, disponibilidad=None, tamanho=None, precio=None)
    while True:
        print("""
        ------------------------------
        ---  Gestión de Cabinas  ---   
        ------------------------------
        1 - Registrar Cabina
        2 - Modificar Cabina
        3 - Eliminar Cabina
        4 - Listar Cabina
        5 - Listar Cabinas para 4 personas
        6 - Volver al Menú Principal
        ------------------------------
        """)
        try:
            opcion = int(input("Selecione una opción: ")) 
            if opcion == 1:
                # Register a new cabin
                objCabina.capturaDatos()
                objCabina.ingresaCabina()
                
            elif opcion == 2:
                # Modify an existing cabin
                cabinas = Cabina.select_cabina()
                if not cabinas:
                    print("\n----No hay cabinas registradas en el sistema para modificar----\n")
                    break
                
                ids_validos = [cabina[0] for cabina in cabinas]
                if not cabinas:
                    print("\n----No se encuentran cabinas registradas en el sistema----\n")
                else:
                    print("Listado de cabinas en el sistema:")
                    # Display table header
                    print(f"{'ID Cabina':<10} {'Capacidad':<10} {'Tamaño':<15} {'Disponibilidad':<15} {'Precio':<10}")
                    # Display each cabin's data
                    for cabina in cabinas:
                        disponibilidad = "Disponible" if cabina[3] else "No Disponible"
                        print(f"{cabina[0]:<10} {cabina[1]:<10} {cabina[2]:<15} {disponibilidad:<15} {cabina[4]:<10.2f}")

                # Validate cabin ID
                while True:
                        idCabina = validaIntPositivo("Digite ID de la cabina que desea modificar: ")
                        if idCabina in ids_validos:
                            break        
                capacidad = validaIntPositivo("Digite la nueva capacidad de la cabina: ")
                        
                while True:
                    # Select cabin size
                    print("Seleccione el nuevo tamaño de la cabina")
                    print("1 - Pequeña")
                    print("2 - Mediana")
                    print("3 - Grande")
                    opcion = input("Digite el número correspondiente al tamaño de la cabina: ").strip()
                    if opcion == "1":
                        tamanho = "Pequeña"
                        break
                    elif opcion == "2":
                        tamanho = "Mediana"
                        break
                    elif opcion == "3":
                        tamanho = "Grande"
                        break
                    else:
                        print("\n----Opción inválida. Por favor, seleccione 1, 2 o 3----\n")
           
                while True:
                    # Select cabin availability
                    print("Seleccione el nuevo estado de la cabina")
                    print("1 - Disponible")
                    print("2 - Indisponible")
                    opcion = input("Digite el número correspondiente al estado de la cabina: ").strip()
                    if opcion == "1":
                        estado = True
                        break
                    elif opcion == "2":
                        estado = False
                        break
                    else:
                        print("\n----Opción inválida. Por favor, seleccione 1 o 2----\n")  
                precio = validaFloatPositivo("Digtite el precio: ")
                objCabina.modificar(capacidad, estado, tamanho, precio, idCabina)
                                        
            elif opcion == 3:
                # Delete a cabin
                cabinas = Cabina.select_cabina()
                if not cabinas:
                    print("\n----No hay cabinas registradas en el sistema para borrar----\n")
                    break
                ids_validos = [cabina[0] for cabina in cabinas]
                # Display table header
                print(f"{'ID Cabina':<10} {'Capacidad':<10} {'Tamaño':<15} {'Disponibilidad':<15} {'Precio':<10}")
                # Display each cabin's data
                for cabina in cabinas:
                    disponibilidad = "Disponible" if cabina[3] else "No Disponible"
                    print(f"{cabina[0]:<10} {cabina[1]:<10} {cabina[2]:<15} {disponibilidad:<15} {cabina[4]:<10.2f}")
                # Validate cabin ID
                while True:
                    try:
                        idCabina = int(input("Digite el ID de la cabina que desea borrar: ").strip())
                        if idCabina > 0 and idCabina in ids_validos:
                            objCabina.desactivar(idCabina)
                            break
                        else:
                            print("\n----El ID ingresado no es válido. Debe ser un número positivo y pertenecer a la lista mostrada----\n")
                    except ValueError:
                        print("\n----Entrada inválida. Por favor, ingrese un número----\n")
                        
            elif opcion == 4:
                # List all cabins
                objCabina.listar()
            elif opcion==5:
                objCabina.cabinas4personas()
            elif opcion == 6:
                # Exit to main menu
                break  
            else:
                print("\n----Opción no válida. Intente de nuevo----\n")
        except ValueError as e: 
            print(f"\n----Error: {e}. Intente ingresar un número válido----\n")  
   
                              
def mostrar_menu_rol():
    # Display and handle options for role management
    objRol = Rol(idRol=None, nombre=None, descripcion=None, departamento=None, salario=None)
    while True:
        print("""
        ------------------------------
        ---    Gestión de Roles    ---   
        ------------------------------
        1 - Registrar Rol
        2 - Modificar Rol
        3 - Eliminar Rol
        4 - Listar Rol
        5 - Volver al Menú Principal
        ------------------------------
        """)
        try:
            opcion = int(input("Selecione una opción: "))
            if opcion == 1:
                # Register a new role
                objRol.capturaNuevoR()
                objRol.ingresaRol()
            elif opcion == 2:
                # Modify an existing role
                listRoles = objRol.returnListaRol()
                if not listRoles:  # Check if roles exist
                    print("\n----No se encuentran roles registrados en el sistema----\n")
                else:
                    print("Listado de roles en el sistema:")
                    
                    # Table header for roles
                    print(f"{'ID':<10} {'Rol':<20} {'Descripción':<30} {'Departamento':<20} {'Salario':<10}")
                    # Display formatted role data
                    for rol in listRoles:
                        print(f"{rol[0]:<10} {rol[1]:<20} {rol[2]:<30} {rol[3]:<20} {rol[4]:<10.2f}")

                while True:
                    try:
                        idSeleccionado = int(input("Digite el ID del rol que desea modificar: ").strip())
                        # Check if the role ID is valid
                        if any(rol[0] == idSeleccionado for rol in listRoles):
                            objRol.capturaModR(idSeleccionado)
                            break
                        else:
                            print("\n----ID no encontrado. Intente nuevamente----\n")
                    except ValueError:
                        print("\n----Ingrese un número entero válido para el ID----\n")
            elif opcion == 3:
                # Delete a role
                listRoles = objRol.returnListaRol()
                listaTrabajadores = objRol.select_trabajadores()
                idRolesOcupados = [rol[2] for rol in listaTrabajadores]  # Extract IDs of occupied roles
                if not listRoles:  # Check if roles exist
                    print("\n----No se encuentran roles en el sistema----\n")
                else:
                    print("Listado de roles en el sistema:")
                    # Table header for roles
                    print(f"{'ID':<5} {'Nombre':<20} {'Descripción':<30} {'Departamento':<20} {'Salario':<10}")
                    # Display formatted role data
                    for rol in listRoles:
                        print(f"{rol[0]:<5} {rol[1]:<20} {rol[2]:<30} {rol[3]:<20} {rol[4]:<10.2f}")

                while True:
                    try:
                        idSeleccionado = int(input("Digite el ID del rol que desea borrar: ").strip())
                        # Check if the role ID is occupied or valid
                        if idSeleccionado in idRolesOcupados:
                            print("\n----No se puede borrar este rol porque esta ocupado por un trabajador----\n")
                            break
                        elif any(rol[0] == idSeleccionado for rol in listRoles):
                            objRol.BorraRol_prueba(idSeleccionado)
                            break
                        else:
                            print("\n----ID no encontrado. Intente nuevamente----\n")
                    except ValueError:
                        print("\n----Ingrese un número válido para el ID----\n")
            elif opcion == 4:
                # List all roles
                objRol.listaRol()
            elif opcion == 5:
                # Exit to main menu
                break  
            else:
                print("\n----Opción no válida. Intente de nuevo----\n")
        except ValueError as e: 
            print(f"\n----Error: {e}. Intente ingresar un número válido----\n")

def mostrar_menu_servicio():
    # Display and handle options for service management
    objServicio = Servicio(idServicio=None, tipo=None, descripcion=None, precio=None)
    while True:
        print("""
        ------------------------------
        ---  Gestión de Servicios  ---   
        ------------------------------
        1 - Registrar Servicio
        2 - Modificar Servicio
        3 - Eliminar Servicio
        4 - Listar Servicio
        5 - Volver al Menú Principal
        ------------------------------
        """)
        try:
            opcion = int(input("Selecione una opción: ")) 
            
            if opcion == 1:
                # Register a new service
                objServicio.capturaDatos()
                objServicio.ingresaServicio()
                pass
                
            elif opcion == 2:
                # Modify an existing service
                objServicio.listar()
                objServicio.modificaServicio()
            elif opcion == 3:
                while True:
                    objServicio.listar()  # Muestra el listado de servicios
                    try:
                        id_servicio = int(input("Digite el número del servicio que desea eliminar: "))
                        if objServicio.borraServicio(id=id_servicio):
                            break  # Si la eliminación fue exitosa, sale del ciclo
                    except ValueError:
                        print("\n----Error: Debe ingresar un número válido----\n")
                    
            elif opcion == 4:
                # List all services
                objServicio.listar()
                pass
            elif opcion == 5:
                # Exit to main menu
                break  
            else:
                print("\n----Opción no válida. Intente de nuevo----\n")
        except ValueError as e:
            print(f"\n----Error: {e}. Intente ingresar un número válido----\n")  


def mostrar_menu_solicitud_servicio():
    while True:
        print("""
        -------------------------------------------
        ---  Gestión de Solicitud de Servicios  ---   
        -------------------------------------------
        1 - Registrar Solicitud de Servicio
        2 - Modificar Solicitud de Servicio
        3 - Listar Solicitudes de Servicio
        4 - Volver al Menú Principal
        -------------------------------------------
        """)
        try:
            opcion = int(input("Seleccione una opción: ")) 
            if opcion == 1:
                pass
            elif opcion == 2:
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                break 
            else:
                print("\n----Opción no válida. Intente de nuevo.----\n")
        except ValueError as e: 
            print(f"\n----Error: {e}. Intente ingresar un número válido.----\n")
            
def mostrar_menu_registro_pasajero_a_cabina():
    objRegistro = RegistroEstadia(idRegistro=None, idCabina=None, idPasajero=None, fechaDeIngreso=None,fechaDeSalida=None)
    while True:
        print("""
        --------------------------------------------------
        ---  Gestión de registro de pasajero a cabina  ---   
        --------------------------------------------------
        1 - Registrar pasajero a cabina
        2 - Listar
        3 - Volver al Menú Principal
        -------------------------------------------
        """)
        try:
            opcion = int(input("Seleccione una opción: ")) 
            if opcion == 1:
                objRegistro.capturaDatos()
            elif opcion == 2:
                objRegistro.listar()
            elif opcion == 3:
                # Exit to main menu
                break
            else:
                print("\n----Opción no válida. Intente de nuevo.----\n")
        except ValueError as e: 
            print(f"\n----Error: {e}. Intente ingresar un número válido.----\n")
            
# Ejecutar el programa
if __name__ == "__main__":
    mostrar_menu_principal()
                                      


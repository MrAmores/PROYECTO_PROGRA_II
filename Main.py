from Pasajero import Pasajero
from Trabajador import Trabajador
from Rol import Rol
from Cabina import Cabina
from Servicio import Servicio
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
        7 - Salir
        --------------------------------------
        """)
        try:
            opc = int(input("Seleccione una opción: "))
            if opc == 1:
                mostrar_menu_pasajero()
            elif opc == 2:
                mostrar_menu_trabajador()
            elif opc == 3:
                mostrar_menu_cabina()
            elif opc == 4:
                mostrar_menu_rol()
            elif opc == 5:
                mostrar_menu_servicio()
            elif opc == 6:
                mostrar_menu_solicitud_servicio()
            elif opc == 7:
                print("SALIENDO DEL SISTEMA")
                break
            else:
                print("Opción no valida. Intente de nuevo.")
        except ValueError as e:
            print(f"Error: {e}. Intente ingresar un número válido.")
def mostrar_menu_pasajero():
    objPasajero = Pasajero(identificacion=None, nombre=None, apellido1=None, apellido2=None, anhoNacimiento=None, genero=None, activo=None, idCabina=None)
    objPasajero = Pasajero(identificacion=None, nombre=None, apellido1=None, apellido2=None, fechaNacimiento=None, genero=None, activo=None, idCabina=None)
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
            opcion = int(input("Seleccione una opción: "))
            elif opcion == 2:
                # Option to modify a passenger
                pasajeros = Pasajero.select_pasajero()  # Get the list of passengers as tuples
                if not pasajeros:
                    print("\n----No hay pasajeros registrados en el sistema para modificar----\n")
                else:
                    ids_validos = [pasajero[0] for pasajero in pasajeros]  # Extract valid IDs from the tuples
                    print("Listado de pasajeros en el sistema:")
                    for pasajero in pasajeros:
                        print(f"ID Pasajero: {pasajero[0]}, Nombre: {pasajero[1]}, Apellidos: {pasajero[2]}, Año de nacimiento: {pasajero[3]}, Genero: {pasajero[4]}")

                    # Validate the entered passenger ID
                    while True:
                        try:
                            id_pasajero = input("Digite el ID del pasajero que desea modificar: ").strip()
                            if id_pasajero in ids_validos:
                                break
                            else:
                                print("\n----El ID ingresado no es válido. Debe pertenecer a la lista mostrada----\n")
                        except ValueError:
                            print("\n----Entrada inválida. Por favor, ingrese un ID válido----\n")

                    # Validate the new first name
                    while True:
                        nuevo_nombre = input("Digite el nuevo nombre del pasajero: ").strip()
                        if nuevo_nombre:
                            break
                        else:
                            print("\n----El nombre no puede estar vacío o contener solo espacios----\n")

                    # Validate the new first last name
                    while True:
                        nuevo_apellido1 = input("Digite el nuevo primer apellido del pasajero: ").strip()
                        if nuevo_apellido1:
                            break
                        else:
                            print("\n----El primer apellido no puede estar vacío o contener solo espacios----\n")

                    # Validate the new second last name
                    while True:
                        nuevo_apellido2 = input("Digite el nuevo segundo apellido del pasajero: ").strip()
                        if nuevo_apellido2:
                            break
                        else:
                            print("\n----El segundo apellido no puede estar vacío o contener solo espacios----\n")

                    # Validate the new birth year
                    while True:
                        try:
                            nuevo_anho_nacimiento = int(input("Digite el nuevo año de nacimiento del pasajero: ").strip())
                            if nuevo_anho_nacimiento > 0:
                                break
                            else:
                                print("\n----El año de nacimiento debe ser un número positivo----\n")
                        except ValueError:
                            print("\n----Entrada inválida. Por favor, ingrese un número entero----\n")

                    # Validate the new gender
                    while True:
                        print("Seleccione el nuevo género del pasajero:")
                        print("F - Femenino")
                        print("M - Masculino")
                        nuevo_genero = input("Digite 'F' para Femenino o 'M' para Masculino: ").strip().upper()
                        if nuevo_genero == "F":
                            nuevo_genero = "Femenino"
                            break
                        elif nuevo_genero == "M":
                            nuevo_genero = "Masculino"
                            break
                        else:
                            print("\n----Opción inválida. Por favor, ingrese 'F' o 'M'----\n")
                    objPasajero.modificar(nuevo_nombre, nuevo_apellido1, nuevo_apellido2, nuevo_anho_nacimiento, nuevo_genero, id_pasajero)


            elif opcion == 3:
                pasajeros = Pasajero.select_pasajero()  # Obtener lista de cabinas como tuplas
                if not pasajeros:
                    print("\n----No hay pasajeros registrados en el sistema para borrar----\n")
                else:
                    ids_validos = [pas[0] for pas in pasajeros]  # Extraer IDs válidos de las tuplas
                    print("\n----Listado de pasajeros en el sistema----")
                    for pasajero in pasajeros:
                        print(f"ID Pasajero: {pasajero[0]}, Nombre: {pasajero[1]}, Apellidos: {pasajero[2]}, Año de nacimiento: {pasajero[3]}, Genero: {pasajero[4]}")
                    print("-------------------------------------------------\n")
                    # Validar el ID de cabina ingresado
                    while True:
                        idPasajero = input("Digite la identificación del pasajero que desea borrar: ").strip()
                        if idPasajero in ids_validos and idPasajero:
                            objPasajero.desactivar(idPasajero)
                            print("\n----El pasajero ha sido desactivado correctamente----\n")
                            break
                        else:
                            print("\n----La identificación ingresada no es válida. Debe pertenecer a la lista mostrada----\n")
            elif opcion == 4:
                objPasajero.listaDatos()
                objPasajero.listar()
            elif opcion == 5:
                print("\n----Saliendo del sistema----\n")
                break
            else:
                print("\n----Opción no válida. Intente de nuevo----\n")
        except ValueError as e:
            print(f"\n----Error: {e}. Intente ingresar un número válido----\n")
def mostrar_menu_trabajador():
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
            if opcion == 1:
                # We check if there are roles before proceeding with option 1 or 2
                listRoles = Rol.returnListaRol()

                if not listRoles:
                    print("No hay roles en el sistema. Debe ingresar primero un rol.")
                    continue
                objTrabajador.capturaDatosNuevos()
                objTrabajador.ingresaDatos()
            elif opcion == 2:
                listTrabajadores = objTrabajador.trabajadoresActivos()
                # Validate if there are active workers
                if not listTrabajadores:  # If the list is empty
                    print("No se encuentran trabajadores activos en el sistema.")
                else:
                    print("Listado de trabajadores activos en el sistema: ")
                    print("IDENTIFICACIÓN, NOMBRE, APELLIDO_1, APELLIDO_2, AÑO_NACIMIENTO, GÉNERO, ID_ROL")
                    for i in listTrabajadores:
                        print(i)
                    while True:
                        try:
                            idSeleccionado = input("Digite el ID del trabajador que desea modificar: ").strip().upper()

                            #Checks if the ID is in the list of available workers
                            if any(trabajador[0] == idSeleccionado for trabajador in listTrabajadores):
                                objTrabajador.capturaDatosMod(idSeleccionado)
                                break
                            else:
                                print("ID no encontrado. Intente nuevamente.")
                        except ValueError:
                            print("Ingrese un número válido para el ID.")
            elif opcion == 3:
                listTrabajadores = objTrabajador.trabajadoresActivos()
                # Validate if there are active workers
                if not listTrabajadores:  # If the list is empty
                    print("No se encuentran trabajadores activos en el sistema.")
                else:
                    print("Listado de trabajadores activos en el sistema: ")
                    print("IDENTIFICACIÓN, NOMBRE, APELLIDO_1, APELLIDO_2, AÑO_NACIMIENTO, GÉNERO, ID_ROL")
                    for i in listTrabajadores:
                        print(i)
                    while True:
                        try:
                            idSeleccionado = input("Digite el ID del trabajador que desea desactivar: ").strip().upper()

                            #Checks if the ID is in the list of available workers
                            if any(trabajador[0] == idSeleccionado for trabajador in listTrabajadores):
                                objTrabajador.desactiva(idSeleccionado)
                                break
                            else:
                                print("ID no encontrado. Intente nuevamente.")
                        except ValueError:
                            print("Ingrese un número válido para el ID.")
            elif opcion == 4:
                objTrabajador.listaDatos()
            elif opcion == 5:
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError as e: 
            print(f"Error: {e}. Intente ingresar un número válido.")
def mostrar_menu_cabina():
    objCabina = Cabina(idCabina=None,capacidad=None,disponibilidad=None,tamanho=None,precio=None)
    while True:
        print("""
        ------------------------------
        ---  Gestión de Cabinas  ---   
        ------------------------------
        1 - Registrar Cabina
        2 - Modificar Cabina
        3 - Eliminar Cabina
        4 - Listar Cabina
        5 - Volver al Menú Principal
        ------------------------------
        """)
        try:
            opcion = int(input("Selecione una opción: ")) 
            if opcion == 1:
                objCabina.capturaDatos()
                objCabina.ingresaCabina()
                
            elif opcion == 2:
                cabinas = Cabina.select_cabina()  # Obtener lista de cabinas como tuplas
                if not cabinas:
                    print("\n----No hay cabinas registradas en el sistema para modificar----\n")
                    break
                
                ids_validos = [cabina[0] for cabina in cabinas]  # Extraer IDs válidos de las tuplas
                print("Listado de cabinas en el sistema:")
                for cabina in cabinas:
                    print(f"ID Cabina: {cabina[0]}, Capacidad: {cabina[1]}, "
                    f"Tamaño: {cabina[2]}, Disponibilidad: {cabina[3]}, Precio: {cabina[4]}")

                # Validar el ID de cabina ingresado
                while True:
                    try:
                        idCabina = int(input("Digite el ID de la cabina que desea modificar: ").strip())
                        if idCabina > 0 and idCabina in ids_validos:
                            break
                        else:
                            print("\n----El ID ingresado no es válido. Debe ser un número positivo y pertenecer a la lista mostrada----\n")
                    except ValueError:
                        print("\n----Entrada inválida. Por favor, ingrese un número----\n")
                        
                while True:
                    try:
                        capacidad = int(input("Digite la nueva capacidad de personas que permite la cabina: ").strip())
                        if capacidad <= 0:
                            print("\n----La cabina por lo menos debe tener capacidad para un pasajero----\n")
                        else:
                            break
                    except ValueError:
                        print("\n----Entrada inválida. Por favor, ingrese un número----\n")
                        
                while True:
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
                           
                while True:
                        try:
                            precio = float(input("Digite el precio de la cabina: ").strip())
                            if precio > 0:
                                break
                            else:
                                print("\n----El precio debe ser un número positivo----\n")
                        except ValueError:
                            print("\n----Entrada inválida. Por favor, ingrese un número----\n")
                objCabina.modificar(capacidad, estado, tamanho, precio, idCabina)
                                        
            elif opcion == 3:
                cabinas = Cabina.select_cabina()  # Obtener lista de cabinas como tuplas
                if not cabinas:
                    print("\n----No hay cabinas registradas en el sistema para borrar----\n")
                    break
                ids_validos = [cabina[0] for cabina in cabinas]  # Extraer IDs válidos de las tuplas
                print("Listado de cabinas en el sistema:")
                for cabina in cabinas:
                    print(f"ID Cabina: {cabina[0]}, Capacidad: {cabina[1]}, "
                          f"Tamaño: {cabina[2]}, Disponibilidad: {cabina[3]}, Precio: {cabina[4]}")
                # Validar el ID de cabina ingresado
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
                objCabina.listar()
                
            elif opcion == 5:
                break  
            else:
                print("\n----Opción no válida. Intente de nuevo----\n")
        except ValueError as e: 
            print(f"Error: {e}. Intente ingresar un número válido.")

            print(f"\n----Error: {e}. Intente ingresar un número válido----\n")                       
def mostrar_menu_rol():
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
                objRol.capturaNuevoR()
                objRol.ingresaRol()
            elif opcion == 2:
                listRoles = objRol.returnListaRol()
                # Validate if there are active workers
                if not listRoles:  # If the list is empty
                    print("No se encuentran roles en el sistema.")
                else:
                    print("Listado de roles en el sistema: ")
                    print("ID, NOMBRE, DESCRIPCIÓN, DEPARTAMENTO, SALARIO")
                    for i in listRoles:
                        print(i)
                while True:
                    try:
                        idSeleccionado = int(input("Digite el ID del rol que desea modificar: ").strip())

                        # Checks if the ID is in the list of available roles
                        if any(rol[0] == idSeleccionado for rol in listRoles):
                            objRol.capturaModR(idSeleccionado)
                            break
                        else:
                            print("ID no encontrado. Intente nuevamente.")
                    except ValueError:
                        print("Ingrese un número entero válido para el ID.")
            elif opcion == 3:
                listRoles = objRol.returnListaRol()
                # Validate if there are active workers
                if not listRoles:  # If the list is empty
                    print("No se encuentran roles en el sistema.")
                else:
                    print("Listado de roles en el sistema: ")
                    print("ID, NOMBRE, DESCRIPCIÓN, DEPARTAMENTO, SALARIO")
                    for i in listRoles:
                        print(i)
                while True:
                    try:
                        idSeleccionado = int(input("Digite el ID del rol que desea borrar: ").strip())

                        # Checks if the ID is in the list of available roles
                        if any(rol[0] == idSeleccionado for rol in listRoles):
                            objRol.BorraRol(idSeleccionado)
                            break
                        else:
                            print("ID no encontrado. Intente nuevamente.")
                    except ValueError:
                        print("Ingrese un número válido para el ID.")
            elif opcion == 4:
                objRol.listaRol()
            elif opcion == 5:
                break  
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError as e: 
            print(f"Error: {e}. Intente ingresar un número válido.")

def mostrar_menu_servicio():
    objServicio = Servicio(idServicio = None, tipo = None, descripcion = None, precio = None)
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
                objServicio.capturaDatos()
                objServicio.ingresaServicio()
                pass
                
            elif opcion == 2:
                objServicio.listar()
                objServicio.modificaServicio(tipo= input("Digite el tipo: "), descripcion= input("Digite la descripción: "), precio= float(input("Digite el precio: ")), id= int(input("Digite el id: ")))
                pass
            elif opcion == 3:
                pass
                objServicio.listar()
                objServicio.borraServicio(id= int(input("Digite el número del servicio que desea eliminar: ")))
            elif opcion == 4:
                objServicio.listar()
                pass
            elif opcion == 5:
                break  
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError as e:  

def mostrar_menu_solicitud_servicio():
    while True:
        print("""
        -------------------------------------------
        ---  Gestión de Solicitud de Servicios  ---   
        -------------------------------------------
        1 - Registrar Solicitud de Servicio
        2 - Modificar Solicitud de Servicio
        3 - Listar Solicitud de Servicio
        4 - Volver al Menú Principal
        -------------------------------------------
        """)
        try:
            opcion = int(input("Selecione una opción: ")) 
            
            if opcion == 1:
                pass
                # registrar()
            elif opcion == 2:
                pass
                # modificar()
            elif opcion == 3:
                # listar()
                pass
            elif opcion == 4:
                break 
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError as e: 
            print(f"Error: {e}. Intente ingresar un número válido.")


if __name__=="__main__":
    mostrar_menu_principal()    
mostrar_menu_principal()                                      


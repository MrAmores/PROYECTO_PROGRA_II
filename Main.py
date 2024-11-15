
from Pasajero import Pasajero
from Cabina import Cabina
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
                pass
            elif opc == 2:
                mostrar_menu_trabajador()
                pass
            elif opc == 3:
                mostrar_menu_cabina()
                pass
            elif opc == 4:
                mostrar_menu_rol()
                pass
            elif opc == 5:
                mostrar_menu_servicio
                pass
            elif opc == 6:
                mostrar_menu_solicitud_servicio
                pass
            elif opc == 7:
                print("SALIENDO DEL SISTEMA")
                break
            else:
                print("Opción no valida. Intente de nuevo.")
        except ValueError as e:
            print(f"Error: {e}. Intente ingresar un número válido.")
def mostrar_menu_pasajero():
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
            opcion = int(input("Selecione una opción: ")) 
            if opcion == 1:
                objPasajero.capturaDatos()
            elif opcion == 2:
                # modificar()
                pass
            elif opcion == 3:
                Pasajero.select_pasajero()
                objPasajero.desactivar(input("Ingrese la identificación del usaurio que desea desactivar: "))
            elif opcion == 4:
                objPasajero.listar()
            elif opcion == 5:
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError as e: 
            print(f"Error: {e}. Intente ingresar un número válido.")   
def mostrar_menu_trabajador():
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
                pass
                # registrar()
            elif opcion == 2:
                pass
                # modificar()
            elif opcion == 3:
                pass
                # desactivar()
            elif opcion == 4:
                # listar()
                pass
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
                    print("No hay cabinas registradas en el sistema para modificar.")
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
                            print("El ID ingresado no es válido. Debe ser un número positivo y pertenecer a la lista mostrada.")
                    except ValueError:
                        print("Entrada inválida. Por favor, ingrese un número.")
                        
                while True:
                    try:
                        capacidad = int(input("Digite la nueva capacidad de personas que permite la cabina: ").strip())
                        if capacidad <= 0:
                            print("La cabina por lo menos debe tener capacidad para un pasajero.")
                        else:
                            break
                    except ValueError:
                        print("Entrada inválida. Por favor, ingrese un número.")
                        
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
                        print("Opción inválida. Por favor, seleccione 1, 2 o 3.")
                        
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
                        print("Opción inválida. Por favor, seleccione 1 o 2")
                           
                while True:
                        try:
                            precio = float(input("Digite el precio de la cabina: ").strip())
                            if precio > 0:
                                break
                            else:
                                print("El precio debe ser un número positivo.")
                        except ValueError:
                            print("Entrada inválida. Por favor, ingrese un número.")
                objCabina.modificar(capacidad, estado, tamanho, precio, idCabina)
                                        
            elif opcion == 3:
                cabinas = Cabina.select_cabina()  # Obtener lista de cabinas como tuplas
                if not cabinas:
                    print("No hay cabinas registradas en el sistema para borrar.")
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
                            objCabina.desactivar(idCabina)
                            break
                        else:
                            print("El ID ingresado no es válido. Debe ser un número positivo y pertenecer a la lista mostrada.")
                    except ValueError:
                        print("Entrada inválida. Por favor, ingrese un número.")
                        
            elif opcion == 4:
                objCabina.listar()
                
            elif opcion == 5:
                break  
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError as e: 
            print(f"Error: {e}. Intente ingresar un número válido.")                       
def mostrar_menu_rol():
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
                pass
                # registrar()
            elif opcion == 2:
                pass
                # modificar()
            elif opcion == 3:
                pass
                # desactivar()
            elif opcion == 4:
                # listar()
                pass
            elif opcion == 5:
                break  
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError as e: 
            print(f"Error: {e}. Intente ingresar un número válido.")         
def mostrar_menu_servicio():
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
                pass
                # registrar()
            elif opcion == 2:
                pass
                # modificar()
            elif opcion == 3:
                pass
                # desactivar()
            elif opcion == 4:
                # listar()
                pass
            elif opcion == 5:
                break  
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError as e: 
            print(f"Error: {e}. Intente ingresar un número válido.")           
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
            
mostrar_menu_principal()                                     
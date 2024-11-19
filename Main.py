from Pasajero import Pasajero
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
                mostrar_menu_servicio()
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
                objPasajero.ingresaPasajero()
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
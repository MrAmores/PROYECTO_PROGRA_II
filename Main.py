from Pasajero import Pasajero
from Trabajador import Trabajador
from Rol import Rol

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
                objPasajero.capturaDatosNuevos()
                objPasajero.ingresaDatos()
            elif opcion == 2:
                pass
                # modificar()
            elif opcion == 3:
                pass
                # desactivar()
            elif opcion == 4:
                objPasajero.listaDatos()
            elif opcion == 5:
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError as e: 
            print(f"Error: {e}. Intente ingresar un número válido.")
    
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
                objTrabajador.capturaDatosNuevos()
                objTrabajador.ingresaDatos()
            elif opcion == 2:
                listTrabajadores = objTrabajador.trabajadoresActivos()
                while True:
                    try:
                        idSeleccionado = int(input("Digite el ID del trabajador que desea modificar: ").strip())

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
                while True:
                    try:
                        idSeleccionado = int(input("Digite el ID del trabajador que desea desactivar: ").strip())

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
                        print("Ingrese un número entero válido para la posición.")
            elif opcion == 3:
                listRoles = objRol.returnListaRol()
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

if __name__=="__main__":
    mostrar_menu_principal()
#Validates that a string data type is not empty
def validaString(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato:
            return dato
        else:
            print("El dato no puede estar vacío o contener solo espacios")

#Validates the entry of a positive float type number
def validaFloatPositivo(mensaje,):
    while True:
        try:
            dato = float(input(mensaje).strip())
            if dato > 0:
                return dato
            else:
                print("El valor debe ser un número positivo")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

#Validates the entry of a positive int type number
def validaIntPositivo(mensaje):
    while True:
        try:
            dato = int(input(mensaje).strip())
            if dato > 0:
                return dato
            else:
                print("El valor debe ser un número positivo")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

#Validates the gender
def validaGenero():
    while True:
        gen = input("""
            Seleccione el género:
            F - Femenino
            M - Masculino
            """).strip().upper()

        if gen == "F":
            return "Femenino"
        elif gen == "M":
            return "Masculino"
        else:
            print("Opción no válida. Ingrese 'F' para Femenino o 'M' para Masculino.")

# Validates the idRol
def validaIdRol(rolesActuales):
    while True:
        try:
            # Muestra los roles disponibles
            for i, rol in enumerate(rolesActuales, start=1):
                print(f"{i}. {rol[1]}")  # rol[1] es el nombre del rol

            # Solicita al usuario seleccionar un rol por su índice
            seleccion = int(input("\nSeleccione el número del rol: ").strip())

            # Verifica que la selección sea válida
            if 1 <= seleccion <= len(rolesActuales):
                idRolSeleccionado, nombreRolSeleccionado = rolesActuales[seleccion - 1]
                print(f"Has seleccionado el rol: {nombreRolSeleccionado} (ID: {idRolSeleccionado})")
                return idRolSeleccionado
            else:
                print("Opción inválida. Elige un número dentro del rango.")
        except ValueError:
            print("Entrada no válida. Debes seleccionar un número.")
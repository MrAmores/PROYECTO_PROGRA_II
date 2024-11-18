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

#Validates the year of birth
def validaAnhoNacimiento(mensaje):
    while True:
        try:
            dato = int(input(mensaje).strip())
            if 1901 <= dato <= 2155:
                return dato
            else:
                print("El año debe estar entre 1901 y 2155.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido para el año.")
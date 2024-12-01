from datetime import datetime

# Validates that a string is not empty or contains only spaces
def validaString(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato:
            return dato
        else:
            print("\nEl dato no puede estar vacío o contener solo espacios\n")

# Validates the entry of a positive float number
def validaFloatPositivo(mensaje):
    while True:
        try:
            dato = float(input(mensaje).strip())  # Converts the input to a float
            if dato > 0:
                return dato
            else:
                print("\nEl valor debe ser un número positivo\n")  # Ensures the value is positive
        except ValueError:
            print("\nEntrada inválida. Por favor, ingrese un número válido.\n")  # Handles invalid input

# Validates the entry of a positive integer number
def validaIntPositivo(mensaje):
    while True:
        try:
            dato = int(input(mensaje).strip())  # Converts the input to an integer
            if dato > 0:
                return dato
            else:
                print("\nEl valor debe ser un número positivo\n")  # Ensures the value is positive
        except ValueError:
            print("\nEntrada inválida. Por favor, ingrese un número válido.\n")  # Handles invalid input

# Validates the input for gender selection
def validaGenero():
    while True:
        gen = input("""
            Seleccione el género:
            F - Femenino
            M - Masculino
            """).strip().upper()  # Converts input to uppercase for consistency

        if gen == "F":
            return "Femenino"  # Returns "Femenino" if input is "F"
        elif gen == "M":
            return "Masculino"  # Returns "Masculino" if input is "M"
        else:
            print("\nOpción no válida. Ingrese F para Femenino o M para Masculino.\n")  # Invalid input message

# Validates the year of birth to be between 1901 and 2155
def validaAnhoNacimiento(mensaje):
    while True:
        try:
            dato = int(input(mensaje).strip())  # Converts the input to an integer
            if 1901 <= dato <= 2155:
                return dato  # Ensures the year is within the valid range
            else:
                print("\nEl año debe estar entre 1901 y 2155.\n")  # Range validation message
        except ValueError:
            print("\nEntrada inválida. Por favor, ingrese un número válido para el año.\n")  # Handles invalid input

def validar_fecha(mensaje):
    while True:
        try:
            entrada = input(mensaje).strip()
            fecha = datetime.strptime(entrada, "%Y-%m-%d")  # Convert text to a date
            if 1901 <= fecha.year <= 2155:  # Validates that the year is within the range
                return fecha
            else:
                print("\nEl año debe estar entre 1901 y 2155.\n")
        except ValueError:
            print("\nEntrada inválida. Por favor, ingrese una fecha válida en formato YYYY-MM-DD.\n")
            
def validar_hora(mensaje):
    while True:
        try:
            entrada = input(mensaje).strip()
            hora = datetime.strptime(entrada, "%H:%M:%S")  # Convert text to a time
            return hora.time()  # Returns only the time part
        except ValueError:
            print("\nEntrada inválida. Por favor, ingrese una hora válida en formato HH:MM:SS.\n")            

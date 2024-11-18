from abc import ABC, abstractmethod
class Persona(ABC):
    def __init__(self, identificacion, nombre, apellido1, apellido2, anhoNacimiento, genero, activo):
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.anhoNacimiento = anhoNacimiento
        self.genero = genero
        self.activo = activo

    @abstractmethod
    def capturaDatosNuevos(self):
        pass

    @abstractmethod
    def ingresaDatos(self):
        pass

    @abstractmethod
    def capturaDatosMod(self):
        pass

    @abstractmethod
    def modificaDatos(self, nombre, apell_1, apell_2, anho_nacimiento, genero, id):
        pass

    @abstractmethod
    def listaDatos(self):
        pass

    @abstractmethod
    def desactiva(self, id):
        pass

        
        

        
        
    
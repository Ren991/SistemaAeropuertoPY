
from vuelo import Vuelo

class Aeropuerto():
    
    def __init__(self,nombre: str, ciudad:str) -> None:
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__vuelos = []

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def ciudad(self):
        return self.__ciudad

    @ciudad.setter
    def ciudad(self, nueva_ciudad):
        self.__ciudad = nueva_ciudad

    @property
    def vuelos(self):
        return self.__vuelos
    
    @vuelos.setter
    def vuelos(self, nuevos_vuelos):
        self.__vuelos = nuevos_vuelos
    
    def añadir_vuelo(self, vuelo: Vuelo):
        self.__vuelos.append(vuelo)

    def __str__(self) -> str:
        return f"Aeropuerto {self.nombre} de la ciudad de {self.ciudad}"
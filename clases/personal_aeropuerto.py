
from .aeropuerto import Aeropuerto

class Personal_Aeropuerto():
    def __init__(self, nombre: str, password: str, aeropuerto: Aeropuerto) -> None:
        self.__nombre = nombre
        self.__password = password
        self.__aeropuerto = aeropuerto

        

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, nueva_password):
        self.__password = nueva_password

    @property
    def aeropuerto(self):
        return self.__aeropuerto
    
    @aeropuerto.setter
    def aeropuerto(self, nuevo_aeropuerto):
        self.__aeropuerto = nuevo_aeropuerto

    

    
    def __str__(self) -> str:
        return f"Nombre personal: {self.nombre}"
        

from .personal_aeropuerto import *


class Aeropuerto():
    
    def __init__(self,nombre: str, ciudad:str) -> None:
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__status_aterrizaje = False
        self.__status_despegue = False
        self.__despegues = []
        self.__aterrizajes = []
        self.__empleados = []
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
    def status_despegue(self):
        return self.__status_despegue
    
    @status_despegue.setter
    def status_despegue(self,nuevo_status):
        self.__status_despegue = nuevo_status
    
    @property
    def status_aterrizaje(self):
        return self.__status_aterrizaje
    
    @status_aterrizaje.setter
    def status_aterrizaje(self,nuevo_status):
        self.__status_aterrizaje = nuevo_status
    
    @property
    def despegues(self):
        return self.__despegues
    
    @despegues.setter
    def despegues(self,nuevos_despegues):
        self.__despegues = nuevos_despegues

    @property
    def aterrizajes(self):
        return self.__aterrizajes
    
    @aterrizajes.setter
    def aterrizajes(self,nuevos_aterrizajes):
        self.__aterrizajes = nuevos_aterrizajes
    
    @property
    def empleados(self):
        return self.__empleados
    
    @empleados.setter
    def empleados(self, nuevos_empleados):
        self.__empleados = nuevos_empleados
    
    @property
    def vuelos(self):
        return self.__vuelos
    
    @vuelos.setter
    def vuelos(self, nuevos_vuelos):
        self.__vuelos = nuevos_vuelos
    

    def añadir_vuelo(self, vuelo):
        self.__vuelos.append(vuelo)

    
    def solicitar_despegue(self):
        self.__status_despegue = True
    
    def solicitar_aterrizaje(self):
        self.__status_aterrizaje = True

    def resetear_status_despegue(self): #=> Invierte valor propiedad status_despegue
        self.__status_despegue = False
    
    def resetear_status_aterrizaje(self): #=> Invierte valor propiedad status_aterrizaje
        self.__status_aterrizaje = False

    def añadir_despegue(self,vuelo_nuevo):
        self.__despegues.append(vuelo_nuevo)

    def añadir_aterrizaje(self,vuelo):
        self.__aterrizajes.append(vuelo)

    def añadir_empleado(self, empleado):
        self.__empleados.append(empleado)

    def eliminar_empleado(self, empleado):
        self.__empleados.remove(empleado)
    
        
    def __str__(self) -> str:
        return f"Aeropuerto {self.nombre} de la ciudad de {self.ciudad}"
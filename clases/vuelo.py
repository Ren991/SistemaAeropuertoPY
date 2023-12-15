from aeropuerto import Aeropuerto
from avion import Avion
from pasajero import Pasajero
from comisario import Comisario
from datetime import *
from code_generator import *
from torre_control import *

class Vuelo():
    __numeros_vuelos = set()
    def __init__(self, origen: Aeropuerto , destino: Aeropuerto, modelo_avion: Avion, aerolinea: str) -> None:
        self.__origen = origen
        self.__destino = destino
        self.__modelo_avion = modelo_avion
        self.__pasajeros = []
        self.__aerolinea = aerolinea
        self.__numero_vuelo = Vuelo.__crear_num_vuelo()
        

    @property
    def origen(self):
        return self.__origen
    
    @origen.setter
    def origen(self, nuevo_origen):
        self.__origen = nuevo_origen
    
    @property
    def destino(self):
        return self.__destino
    
    @destino.setter
    def destino(self, nuevo_destino):
        self.__destino = nuevo_destino

    @property
    def modelo_avion(self):
        return self.__modelo_avion
    
    @modelo_avion.setter
    def modelo_avion(self, nuevo_modelo_avion):
        self.__modelo_avion = nuevo_modelo_avion

    @property
    def pasajeros(self):
        return self.__pasajeros
    
    @pasajeros.setter
    def pasajeros(self, nuevos_pasajeros):
        self.__pasajeros = nuevos_pasajeros
    
    @property
    def aerolinea(self):
        return self.__aerolinea
    
    @aerolinea.setter
    def aerolinea(self, nueva_aerolinea):
        self.__aerolinea = nueva_aerolinea

    @property
    def numero_vuelo(self):
        return self.__numero_vuelo
    
    @numero_vuelo.setter
    def numero_vuelo(self, nuevo_num):
        self.__numero_vuelo = nuevo_num

    @property
    def status_despegue(self):
        return Torre_Control.status_despegue
    
    @property
    def status_aterrizaje(self):
        return Torre_Control.status_aterrizaje

    
    def despegar(self):
        if self.status_despegue:
            return f"Despegando vuelo: {self.numero_vuelo} con destino a {self.destino}"

    def aterrizar(self):
        if self.status_aterrizaje:
            return f"Aterrizando vuelo: {self.numero_vuelo} con origen en {self.origen}"

    @classmethod
    def __crear_num_vuelo(cls):
        codigo = CodGenerator.generar_codigo()

        if codigo in cls.__numeros_vuelos:
            raise Exception("Error")
        else:
            cls.__numeros_vuelos.add(codigo)
            return codigo
        
    

from .aeropuerto import Aeropuerto
from .avion import Avion
from .comisario import Comisario
from .pasajero import Pasajero
from .code_generator import CodGenerator
from datetime import datetime, timedelta
from random import randint


class Vuelo():
    __numeros_vuelos = set()
    def __init__(self, origen: Aeropuerto , destino:Aeropuerto ,modelo_avion: Avion, aerolinea: str, comisario_vuelo: Comisario) -> None:
        self.__origen = origen
        self.__destino = destino
        self.__modelo_avion = modelo_avion
        self.__pasajeros = []
        self.__aerolinea = aerolinea
        self.__numero_vuelo = Vuelo.__crear_num_vuelo()
        self.__comisario_vuelo = comisario_vuelo
        self.__despegue_solicidado = False
        self.__aterrizaje_solicitado = False

        

        

    @property
    def origen(self):
        return self.__origen.ciudad
    
    @origen.setter
    def origen(self, nuevo_origen):
        self.__origen = nuevo_origen
    
    @property
    def destino(self):
        return self.__destino.ciudad
    
    @destino.setter
    def destino(self, nuevo_destino):
        self.__destino = nuevo_destino

    @property
    def modelo_avion(self):
        return self.__modelo_avion.modelo
    
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
        return self.__origen.status_despegue
    
    @property
    def status_aterrizaje(self):
        return self.__destino.status_aterrizaje
    
    
   
    
    @property
    def horario_salida(self):
        return datetime.today()
    
    @property
    def horario_llegada(self):
        horas_adicionales = randint(1, 6)
        minutos_adicionales = randint(0, 59)

        return self.horario_salida + timedelta(hours=horas_adicionales, minutes=minutos_adicionales)

    @property
    def duracion_vuelo(self):
        duracion_en_horas = (self.horario_llegada - self.horario_salida).total_seconds() / 3600.0
        return round(duracion_en_horas, 1)
    
    @property
    def comisario_vuelo(self):
        return self.__comisario_vuelo
    
    @comisario_vuelo.setter
    def comisario_vuelo(self, nuevo_comisario):
        self.__comisario_vuelo = nuevo_comisario

    @property
    def despegue_solicitado(self):
        return self.__despegue_solicidado
    
    @despegue_solicitado.setter
    def despegue_solicitado(self, nuevo_status):
        self.__despegue_solicidado = nuevo_status

    @property
    def aterrizaje_solicitado(self):
        return self.__aterrizaje_solicitado
    
    @aterrizaje_solicitado.setter
    def aterrizaje_solicitado(self, nuevo_status):
        self.__aterrizaje_solicitado = nuevo_status

    def solicitar_aterrizaje(self):
        self.__aterrizaje_solicitado = True

    def solicitar_despegue(self):
        self.__despegue_solicidado = True


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
        
    def añadir_pasajero(self, pasajero: Pasajero):
        self.pasajeros.append(pasajero)

    
    
    def __str__(self):
        return f"Aerolinea: {self.aerolinea} || Código vuelo: {self.numero_vuelo} || Origen: {self.origen} || Destino: {self.destino} || Duración: {self.duracion_vuelo}Hs || Modelo avión: {self.modelo_avion}"
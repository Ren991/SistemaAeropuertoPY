class Avion():
    def __init__(self,modelo:str, capacidad_pasaj: int) -> None:
        self.__modelo = modelo
        self.__capacidad_pasaj = capacidad_pasaj 

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, nuevo_modelo):
        self.__modelo = nuevo_modelo

    @property
    def capacidad_pasaj(self):
        return self.__capacidad_pasaj

    @capacidad_pasaj.setter
    def capacidad_pasaj(self, nueva_capacidad):
        self.__capacidad_pasaj = nueva_capacidad    

    def __str__(self) -> str:
        return f"Modelo: {self.modelo} || Capacidad de pasajeros: {self.capacidad_pasaj}"   
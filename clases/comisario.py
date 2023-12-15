class Comisario():
    def __init__(self,nombre:str, edad:int) -> None:
        self.__nombre = nombre
        self.__edad= edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nuevo_edad):
        self.__edad = nuevo_edad

    def __str__(self) -> str:
        return f"Nombre Comisario: {self.nombre} || Edad: {self.edad}"
           
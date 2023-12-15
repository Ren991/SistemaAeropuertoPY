class Pasajero():
    def __init__(self, nombre: str, dni: str, es_adulto : bool) -> None:
        self.__nombre = nombre
        self.__dni = dni
        self.__es_adulto = es_adulto

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self, nuevo_dni):
        self.__dni = nuevo_dni
    
    @property
    def es_adulto(self):
        return "Si" if self.__es_adulto else "No"
    
    @es_adulto.setter
    def es_adulto(self, nuevo_status):
        self.__es_adulto = nuevo_status

    def __str__(self) -> str:
        return f"Nombre: {self.nombre} || DNI: {self.dni} || Es Adulto: {self.es_adulto}"


        
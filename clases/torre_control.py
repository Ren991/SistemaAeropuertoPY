from aeropuerto import Aeropuerto

class Torre_Control():
    def __init__(self, aeropuerto = Aeropuerto) -> None:
        self.__aeropuerto = aeropuerto
        self.__status_despegue = None
        self.__status_aterrizaje = None

    @property
    def aeropuerto(self):
        return self.__aeropuerto
    
    @aeropuerto.setter
    def aeropuerto(self, nuevo_aeropuerto):
        self.__aeropuerto = nuevo_aeropuerto

    @property
    def status_aterrizaje(self):
        return self.__status_aterrizaje
    
    @status_aterrizaje.setters
    def status_aterrizaje(self, nuevo_status):
        self.__status_aterrizaje = nuevo_status
    
    @property
    def status_despegue(self):
        return self.__status_despegue
    
    @status_despegue.setter
    def status_despegue(self, nuevo_status):
        self.__status_despegue = nuevo_status

    
        
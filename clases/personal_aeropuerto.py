

class Personal_Aeropuerto():
    def __init__(self, nombre: str, password: str) -> None:
        self.__nombre = nombre
        self.__password = password        

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

   
    
  

    

    
    def __str__(self) -> str:
        return f"Nombre personal: {self.nombre}"
        
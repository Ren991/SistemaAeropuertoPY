#Aeropuerto(nombre:str,ciudad:str)
#Torre_Control(aeropuerto:str)
#Vuelo(origen,destino,modelo_avion)
#Comisario(nombre,edad)
#Pasajero(nombre:str,dni: str, es_adulto: bool)
#Avion(modelo: str, capacidad:str)


from aeropuerto import Aeropuerto
from avion import Avion
from pasajero import Pasajero
from comisario import Comisario

from vuelo import Vuelo
from code_generator import CodGenerator

# Crear instancias de otras clases
aeropuerto_origen = Aeropuerto("Aeropuerto Origen", "Ciudad Origen")
aeropuerto_destino = Aeropuerto("Aeropuerto Destino", "Ciudad Destino")
avion = Avion("Boeing 747", 300)
comisario = Comisario("Nombre del Comisario",33)



vuelo = Vuelo(aeropuerto_origen, aeropuerto_destino,avion, "Aerolinea X", comisario)
print(vuelo)

aeropuerto_origen.solicitar_despegue()

print(vuelo.despegar())

aeropuerto_destino.solicitar_aterrizaje()
print(vuelo.aterrizar())

pasajero1 = Pasajero("Nombre Pasajero 1","62222222",False)
vuelo.añadir_pasajero(pasajero1)

print(f"Pasajeros en el vuelo: {len(vuelo.pasajeros)}")

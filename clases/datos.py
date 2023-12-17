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
from torre_control import Torre_Control
from vuelo import Vuelo
from code_generator import CodGenerator

# Crear instancias de otras clases
aeropuerto_origen = Aeropuerto("Aeropuerto Origen", "Ciudad Origen")
aeropuerto_destino = Aeropuerto("Aeropuerto Destino", "Ciudad Destino")
avion = Avion("Boeing 747", 300)
comisario = Comisario("Nombre del Comisario",33)

# Crear una instancia de Torre_Control
torre_control = Torre_Control(aeropuerto_origen)

# Crear una instancia de Vuelo con una referencia a Torre_Control
vuelo = Vuelo(aeropuerto_origen, aeropuerto_destino, torre_control, avion, "Aerolinea X", comisario)

# Acceder a las propiedades y métodos de la instancia de Vuelo
print(f"Origen: {vuelo.origen}")
print(f"Destino: {vuelo.destino}")
print(f"Modelo avión: {vuelo.modelo_avion}")
print(f"Número de vuelo: {vuelo.numero_vuelo}")
print(f"Status de despegue: {vuelo.status_despegue}")
print(f"Status de aterrizaje: {vuelo.status_aterrizaje}")
print(f"Comisario de vuelo: {vuelo.comisario_vuelo}")

# Intentar despegar el vuelo
print(vuelo.despegar())

# Intentar aterrizar el vuelo
print(vuelo.aterrizar())

# Añadir un pasajero al vuelo
pasajero1 = Pasajero("Nombre Pasajero 1","62222222",False)
vuelo.añadir_pasajero(pasajero1)

# Verificar la lista de pasajeros después de añadir uno
print(f"Pasajeros en el vuelo: {len(vuelo.pasajeros)}")

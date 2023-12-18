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
aeropuertos = [
    Aeropuerto("Ministro Pistarini", "Ezeiza"),
    Aeropuerto("Jorge Chávez", "Lima"),
    Aeropuerto("Heathrow", "Londres"),
    Aeropuerto("Charles de Gaulle", "París"),
    Aeropuerto("Los Angeles International", "Los Ángeles"),
    Aeropuerto("Dubai International", "Dubái"),
    Aeropuerto("Hong Kong International", "Hong Kong"),
    Aeropuerto("O'Hare International", "Chicago"),
    Aeropuerto("Sydney Kingsford Smith", "Sídney"),
    Aeropuerto("Incheon International", "Seúl"),
    Aeropuerto("El Dorado International", "Bogotá"),
    Aeropuerto("Narita International", "Tokio"),
    Aeropuerto("Munich Airport", "Múnich"),
    Aeropuerto("Singapore Changi", "Singapur"),
    Aeropuerto("Barajas Adolfo Suárez", "Madrid"),
    Aeropuerto("Copenhagen Airport", "Copenhague"),
    Aeropuerto("Benito Juárez", "Ciudad de México"),
    Aeropuerto("Kuala Lumpur International", "Kuala Lumpur"),
    Aeropuerto("Auckland Airport", "Auckland"),
    Aeropuerto("Zurich Airport", "Zúrich"),
]

aviones = [
    Avion("Boeing 747", 300),
    Avion("Airbus A380", 500),
    Avion("Boeing 777", 350),
    Avion("Airbus A320", 180),
    Avion("Embraer E190", 100),
    Avion("Bombardier CRJ900", 90),
    Avion("Boeing 737", 200),
    Avion("Airbus A350", 400),
    Avion("Boeing 787", 250),
    Avion("McDonnell Douglas MD-11", 280),
    Avion("Airbus A330", 300),
    Avion("Embraer E175", 80),
    Avion("Bombardier Q400", 70),
    Avion("Airbus A321", 220),
    Avion("Boeing 767", 280),
]

aerolineas = [
    "Aerolíneas Argentinas",
    "Emirates",
    "Delta Air Lines",
    "British Airways",
    "Lufthansa",
    "Qatar Airways",
    "Singapore Airlines",
    "American Airlines",
    "Air France",
    "Cathay Pacific",
    "KLM Royal Dutch Airlines",
    "Turkish Airlines",
    "ANA All Nippon Airways",
    "Southwest Airlines",
    "Etihad Airways",
    "Alitalia",
    "JetBlue Airways",
    "Air Canada",
    "LATAM Airlines",
    "Qantas",
]

aeropuerto_origen = aeropuertos[2]
aeropuerto_destino = aeropuertos[7]
avion = aviones[8]
comisario = Comisario("Nombre del Comisario",33)

aerolinea = aerolineas[5]

vuelo = Vuelo(aeropuerto_origen, aeropuerto_destino,avion, aerolinea , comisario)
print(vuelo)

aeropuerto_origen.solicitar_despegue()

vuelo.despegar()
aeropuerto_origen.resetear_status_despegue()


aeropuerto_destino.solicitar_aterrizaje()
vuelo.aterrizar()
aeropuerto_destino.resetear_status_aterrizaje()


pasajero1 = Pasajero("Nombre Pasajero 1","62222222",False)
vuelo.añadir_pasajero(pasajero1)

print(f"Pasajeros en el vuelo: {len(vuelo.pasajeros)}")

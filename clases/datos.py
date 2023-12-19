from .aeropuerto import Aeropuerto
from .vuelo import Vuelo
from .avion import Avion
from .comisario import Comisario
from .pasajero import Pasajero


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
avion1 = aviones[8]
comisario1 = Comisario("Nombre del Comisario",33)

aerolinea = aerolineas[5]

vuelo1 = Vuelo(aeropuerto_origen, aeropuerto_destino,avion1, aerolinea , comisario1)
#print(vuelo1)

aeropuerto_origen.solicitar_despegue()

vuelo1.despegar()

aeropuerto_origen.resetear_status_despegue()
aeropuerto_origen.añadir_despegue(vuelo1)

for vuelos in aeropuerto_origen.despegues:
    print(vuelos)


aeropuerto_destino.solicitar_aterrizaje()
vuelo1.aterrizar()
aeropuerto_destino.resetear_status_aterrizaje()


pasajero1 = Pasajero("Nombre Pasajero 1","62222222",False)
vuelo1.añadir_pasajero(pasajero1)

print(f"Pasajeros en el vuelo: {len(vuelo1.pasajeros)}")



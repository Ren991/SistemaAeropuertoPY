
from .aeropuerto import Aeropuerto
from .personal_aeropuerto import Personal_Aeropuerto
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
    Aeropuerto("Barajas", "Madrid"),  
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

comisarios = [
    Comisario("Pedro Perez", 33),
    Comisario("María García", 40),
    Comisario("Juan López", 35),
    Comisario("Laura Martínez", 38),
    Comisario("Carlos Rodríguez", 42),
    Comisario("Ana Díaz", 37),
    Comisario("Javier Sánchez", 45),
    Comisario("Elena Gómez", 39),
    Comisario("Luis Vázquez", 44),
    Comisario("Lucía Torres", 41),
    Comisario("Roberto Ramírez", 36),
    Comisario("Isabel Herrera", 43),
    Comisario("Pedro Molina", 46),
    Comisario("Silvia Navarro", 48),
    Comisario("Miguel Castro", 50),
    Comisario("Carmen Ortega", 49),
    Comisario("Alejandro Jiménez", 52),
    Comisario("Beatriz Ruiz", 47),
    Comisario("Francisco Morales", 51),
    Comisario("Patricia Torres", 53),
]

aeropuertos[0].añadir_empleado(Personal_Aeropuerto("Pepito1", "password123"))
aeropuertos[0].añadir_empleado(Personal_Aeropuerto("Pepito2", "password123"))
aeropuertos[0].añadir_empleado(Personal_Aeropuerto("Pepito3", "password123"))

aeropuertos[1].añadir_empleado(Personal_Aeropuerto("Fulanito1", "password123"))
aeropuertos[1].añadir_empleado(Personal_Aeropuerto("Fulanito2", "password123"))
aeropuertos[1].añadir_empleado(Personal_Aeropuerto("Fulanito3", "password123"))

aeropuertos[2].añadir_empleado(Personal_Aeropuerto("Marito1", "password123"))
aeropuertos[2].añadir_empleado(Personal_Aeropuerto("Marito2", "password123"))
aeropuertos[2].añadir_empleado(Personal_Aeropuerto("Marito3", "password123"))

aeropuertos[3].añadir_empleado(Personal_Aeropuerto("User1", "password123"))
aeropuertos[3].añadir_empleado(Personal_Aeropuerto("User2", "password123"))
aeropuertos[3].añadir_empleado(Personal_Aeropuerto("User3", "password123"))

aeropuertos[4].añadir_empleado(Personal_Aeropuerto("Luisito1", "password123"))
aeropuertos[4].añadir_empleado(Personal_Aeropuerto("Luisito1", "password123"))
aeropuertos[4].añadir_empleado(Personal_Aeropuerto("Luisito1", "password123"))



aeropuerto_origen = aeropuertos[0]
aeropuerto_destino = aeropuertos[3]
avion1 = aviones[8]
comisario1 = comisarios[0]

aerolinea = aerolineas[5]

vuelo1 = Vuelo(aeropuerto_origen, aeropuerto_destino,avion1, aerolinea , comisario1)
aeropuerto_origen.añadir_vuelo(vuelo1)
#print(vuelo1)

aeropuerto_origen.conceder_despegue()

vuelo1.despegar()

aeropuerto_origen.resetear_status_despegue()
aeropuerto_origen.añadir_despegue(vuelo1)

for vuelos in aeropuerto_origen.despegues:
    print(vuelos)


aeropuerto_destino.conceder_aterrizaje()
vuelo1.aterrizar()
aeropuerto_destino.resetear_status_aterrizaje()


pasajero1 = Pasajero("Nombre Pasajero 1","62222222",False)
vuelo1.añadir_pasajero(pasajero1)

print(f"Pasajeros en el vuelo: {len(vuelo1.pasajeros)}")



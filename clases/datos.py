from .aeropuerto import Aeropuerto
from .vuelo import Vuelo
from .avion import Avion
from .comisario import Comisario
from .pasajero import Pasajero
from .personal_aeropuerto import Personal_Aeropuerto


# Crear instancias de otras clases
aeropuertos = [
    Aeropuerto("Ministro Pistarini", "Ezeiza"),
    Aeropuerto("Jorge Chávez", "Lima"),
    Aeropuerto("Heathrow", "Londres"),
    Aeropuerto("Charles de Gaulle", "París"),
    Aeropuerto("Los Angeles International", "Los Ángeles"),  
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
    Comisario("Pedro Pérez", 33),
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

empleados_aeropuerto_1 = [
    Personal_Aeropuerto("Pepito1", "password123"),
    Personal_Aeropuerto("Pepito2", "password123"),
    Personal_Aeropuerto("Pepito3", "password123"),
]

empleados_aeropuerto_2 = [
    Personal_Aeropuerto("Juanito1", "password123"),
    Personal_Aeropuerto("Juanito2", "password123"),
    Personal_Aeropuerto("Juanito3", "password123"),
]

empleados_aeropuerto_3 = [
    Personal_Aeropuerto("Luisito1", "password123"),
    Personal_Aeropuerto("Luisito2", "password123"),
    Personal_Aeropuerto("Luisito3", "password123"),
]

empleados_aeropuerto_4 = [
    Personal_Aeropuerto("Marito1", "password123"),
    Personal_Aeropuerto("Marito2", "password123"),
    Personal_Aeropuerto("Marito3", "password123"),
]

empleados_aeropuerto_5 = [
    Personal_Aeropuerto("Ana1", "password123"),
    Personal_Aeropuerto("Ana2", "password123"),
    Personal_Aeropuerto("Ana3", "password123"),
]

# Agregar empleados a cada aeropuerto utilizando el método añadir_empleado
for i, aeropuerto in enumerate(aeropuertos):
    for empleado in globals()[f"empleados_aeropuerto_{i + 1}"]:
        aeropuerto.añadir_empleado(empleado)

# Mostrar los empleados de cada aeropuerto
for aeropuerto in aeropuertos:
    print(f"\nEmpleados en el aeropuerto {aeropuerto.nombre} ({aeropuerto.ciudad}):")
    for empleado in aeropuerto.empleados:
        print(f"Nombre: {empleado.nombre}, Contraseña: {empleado.password}")






aeropuerto_origen = aeropuertos[2]
aeropuerto_destino = aeropuertos[3]
avion1 = aviones[8]
comisario1 = comisarios[9]

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



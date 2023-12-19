from clases.datos import *

for aero in aerolineas:
    print(aero)

for comis in comisarios:
    print(comis)

for emp in empleados_aeropuerto_1:
    print(emp.nombre)
# Menú principal

""" 
MENU PRINCIPAL.

Se muestra listado de aeropuerto y se le pide al usuario seleccionarlo.


2 tipo usuario => 1 personal aeropuerto ; 2 comisario vuelo

-El personal de aeropuerto pertenece a un aeropuerto
-El comisario_vuelo pertenece a una aerolinea

*Personal aeropuerto => Puede habilitar despegue/aterrizaje y añadir vuelos

*Comisario vuelo => Puede solicitar despegue/aterrizaje y despegar/aterrizar

*HASTA QUE EL USUARIO NO SELECCIONE OPCION "SALIR" NO SE SALE DEL PROGRAMA.

"""
#

# aeropuerto1 = aeropuerto.Aeropuerto("Ministro Pistarini","Ezeiza") Manera de instanciar las clases.


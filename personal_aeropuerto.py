from clases.datos import *
def listado_vuelos(aeropuerto_actual):
    if len(aeropuerto_actual.vuelos) != 0:
        for vuelo in aeropuerto_actual.vuelos:
            print(vuelo)
    else:
        print("No hay vuelos disponibles para mostrar en el aeropuerto seleccionado . ")


def añadir_vuelo(aeropuerto_actual):
    tipo_vuelo = int(input("Ingrese 1- Salida , 2-Desepegue"))

    if tipo_vuelo == 1:
        aeropuerto_origen = aeropuerto_actual

        print("Lista de aeropuertos:")
        for i, aeropuerto in enumerate(aeropuertos):
            print(f"{i + 1}. {aeropuerto.nombre}")

        # Inicializar la opción fuera del rango para que entre en el bucle while
        opcion = 0

        while not (1 <= opcion <= len(aeropuertos)):
            # Pedir al usuario que elija un número
            opcion = input("Ingrese el número de aeropuerto destino: ")

            try:
                opcion = int(opcion)  
            except ValueError:
                print("Por favor, ingrese un número entero.")
                continue  # Reiniciar el bucle si no se ingresó un número

            if not (1 <= opcion <= len(aeropuertos)):
                print("Número fuera de rango. Por favor, ingrese un número válido.")

        # aeropuerto_destino contiene el aeropuerto seleccionado
        aeropuerto_destino = aeropuertos[opcion - 1]        

        flag_aerolinea = False

        while not flag_aerolinea:
            aerolinea_vuelo = input("Ingrese aerolinea .")

            for aerolinea in aerolineas:
                if aerolinea_vuelo == aerolinea:
                    flag_aerolinea = True
                    break
            if not flag_aerolinea:
                print("Aerolinea no encontrada. Inténtelo de nuevo. ")
        
        
        flag_modelo = False

        while not flag_modelo:
            modelo_avion = input("Ingrese modelo de avion .")

            for avion in aviones:
                if modelo_avion == avion.modelo:
                    flag_modelo = True
                    modelo_avion = avion
                    break
            if not flag_modelo:
                print("Modelo de avion no encontrado. Inténtelo de nuevo")        

        flag_comisario = False

        while not flag_comisario:
            comisario_vuelo = input("Ingrese el nombre del comisario: ")
            
            for comisario in comisarios:
                if comisario_vuelo == comisario.nombre:
                    flag_comisario = True
                    comisario_vuelo = comisario
                    break  # Rompe el bucle for cuando encuentra el comisario

            if not flag_comisario:
                print("Comisario no encontrado. Inténtelo de nuevo.")
    
        nuevo_despegue =  Vuelo(aeropuerto_origen, aeropuerto_destino,modelo_avion, aerolinea_vuelo , comisario_vuelo)

        aeropuerto_actual.añadir_vuelo(nuevo_despegue)

    elif tipo_vuelo == 2:
        aeropuerto_destino = aeropuerto_actual

        print("Lista de aeropuertos:")
        for i, aeropuerto in enumerate(aeropuertos):
            print(f"{i + 1}. {aeropuerto.nombre}")

        # Inicializar la opción fuera del rango para que entre en el bucle while
        opcion = 0

        while not (1 <= opcion <= len(aeropuertos)):
            # Pedir al usuario que elija un número
            opcion = input("Ingrese el número de aeropuerto destino: ")

            try:
                opcion = int(opcion)  
            except ValueError:
                print("Por favor, ingrese un número entero.")
                continue  # Reiniciar el bucle si no se ingresó un número

            if not (1 <= opcion <= len(aeropuertos)):
                print("Número fuera de rango. Por favor, ingrese un número válido.")

        # aeropuerto_destino contiene el aeropuerto seleccionado
        aeropuerto_origen = aeropuertos[opcion - 1]        

        flag_aerolinea = False

        while not flag_aerolinea:
            aerolinea_vuelo = input("Ingrese aerolinea .")

            for aerolinea in aerolineas:
                if aerolinea_vuelo == aerolinea:
                    flag_aerolinea = True
                    break
            if not flag_aerolinea:
                print("Aerolinea no encontrada. Inténtelo de nuevo. ")
        
        
        flag_modelo = False

        while not flag_modelo:
            modelo_avion = input("Ingrese modelo de avion .")

            for avion in aviones:
                if modelo_avion == avion.modelo:
                    flag_modelo = True
                    modelo_avion = avion
                    break
            if not flag_modelo:
                print("Modelo de avion no encontrado. Inténtelo de nuevo. ")        

        flag_comisario = False

        while not flag_comisario:
            comisario_vuelo = input("Ingrese el nombre del comisario: ")
            
            for comisario in comisarios:
                if comisario_vuelo == comisario.nombre:
                    flag_comisario = True
                    comisario_vuelo = comisario
                    break  # Rompe el bucle for cuando encuentra el comisario

            if not flag_comisario:
                print("Comisario no encontrado. Inténtelo de nuevo. ")

        nuevo_aterrizaje =  Vuelo(aeropuerto_origen, aeropuerto_destino,modelo_avion, aerolinea_vuelo , comisario_vuelo)

        aeropuerto_actual.añadir_vuelo(nuevo_aterrizaje)
    else:
        print("Opcion inválida. Por favor inténtelo nuevamente. ")
        

def menu_personal_aeropuerto(aeropuerto_actual):
    
    while True:  
        print("1- Habilitar despegue ")
        print("2- Habilitar aterrizaje ")
        print("3-Añadir vuelo")
        print("4- Ver vuelos")
        print("5-volver a la pantalla anterior ")
        opt = int(input("Ingrese una opcion : "))

        if opt == 1:
            print("Despegue habilitado")
        elif opt == 2:
            print("Aterrizaje habilitado")
        elif opt == 3:
            añadir_vuelo(aeropuerto_actual)
            print("Vuelo añadido")
        elif opt ==4:
            print("Listado de vuelos")
            listado_vuelos(aeropuerto_actual)
        elif opt ==5:
            print("Volviendo al menú principal")
        else:
            print("Numero inválido por favor ingrese otro numero")    


def personal_aeropuerto(aeropuerto_actual):
    
    print(aeropuerto_actual.ciudad)
    nombre_usuario = input("ingrese nombre de  usuario: ")
    contrasenia_usuario = input("Ingrese contrasenia: ")

    flag = False
    for empleado in aeropuerto_actual.empleados:
        if empleado.nombre == nombre_usuario and empleado.password == contrasenia_usuario:
            
            flag = True
            break
    if flag == True:
        menu_personal_aeropuerto(aeropuerto_actual)
    else:
        print("Credenciales inválidas")
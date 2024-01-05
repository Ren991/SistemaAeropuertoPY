vuelos_comisario = []
def solicitar_despegue(comisario,aeropuerto_actual):
    
    
    if len(aeropuerto_actual.vuelos) == 0:
        print("No hay vuelos registrados para despegar")
    else:
        print("Elija Vuelo que desea solicitar despegue")

        for vuelo in aeropuerto_actual.vuelos:
            if vuelo.comisario_vuelo.nombre == comisario.nombre:
                vuelos_comisario.append(vuelo)
        
        for i, vuelo in enumerate(vuelos_comisario):
            print(f"{i + 1}. {vuelo}")

        # Pedir al usuario que elija un vuelo
        while True:
            opcion = input("Ingrese el número del vuelo que desea solicitar despegue: ")

            try:
                opcion = int(opcion)
                if 1 <= opcion <= len(vuelos_comisario):
                    vuelo_seleccionado = vuelos_comisario[opcion - 1]
                    print(f"Ha seleccionado el vuelo: {vuelo_seleccionado.numero_vuelo}")
                    vuelo_seleccionado.solicitar_despegue()
                    break  # Salir del bucle while después de una selección válida
                else:
                    print("Número fuera de rango. Por favor, ingrese un número válido.")
            except ValueError:
                print("Por favor, ingrese un número entero válido.")



def solicitar_aterrizaje(comisario,aeropuerto_actual):
    
    if len(aeropuerto_actual.vuelos) == 0:
        print("No hay vuelos registrados para Aterrizar")
    else:
        print("Elija Vuelo que desea solicitar aterrizar")

        for vuelo in aeropuerto_actual.vuelos:
            if vuelo.comisario_vuelo.nombre == comisario.nombre:
                vuelos_comisario.append(vuelo)
        
        for i, vuelo in enumerate(vuelos_comisario):
            print(f"{i + 1}. {vuelo}")

        # Pedir al usuario que elija un vuelo
        while True:
            opcion = input("Ingrese el número del vuelo que desea solicitar aterrizaje: ")

            try:
                opcion = int(opcion)
                if 1 <= opcion <= len(vuelos_comisario):
                    vuelo_seleccionado = vuelos_comisario[opcion - 1]
                    print(f"Ha seleccionado el vuelo: {vuelo_seleccionado.numero_vuelo}")
                    vuelo_seleccionado.solicitar_aterrizaje()
                    break  # Salir del bucle while después de una selección válida
                else:
                    print("Número fuera de rango. Por favor, ingrese un número válido.")
            except ValueError:
                print("Por favor, ingrese un número entero válido.")


def despegar(aeropuerto_actual):
    vuelos_habilitados = []
    if len(vuelos_comisario) == 0:
        print("No hay vuelos disponibles para despegar")
    else:
        if aeropuerto_actual.status_despegue == True:
            for vuelo in vuelos_comisario:
                if vuelo.despegue_solicitado == True:
                    vuelos_habilitados.append(vuelo)
            
            if len(vuelos_habilitados) > 0:
                for i, vuelo in enumerate(vuelos_habilitados):
                    print(f"{i + 1}. {vuelo}")
                while True:
                    opcion = input("Ingrese el número del vuelo que desea Despegar: ")
                    try:
                        opcion = int(opcion)
                        if 1 <= opcion <= len(vuelos_habilitados):
                            vuelo_seleccionado = vuelos_habilitados[opcion - 1]                            
                            vuelo_seleccionado.despegar()
                            print("Vuelo despegado con éxito")
                            break  # Salir del bucle while después de una selección válida
                        else:
                            print("Número fuera de rango. Por favor, ingrese un número válido.")
                    except ValueError:
                        print("Por favor, ingrese un número entero válido.")
                
        else:
            print("El aeropuerto no habilitó el despegue aún.")


def aterrizar(aeropuerto_actual):

    vuelos_habilitados = []
    if len(vuelos_comisario) == 0:
        print("No hay vuelos disponibles para aterrizar")
    else:
        if aeropuerto_actual.status_aterrizaje == True:
            for vuelo in vuelos_comisario:
                if vuelo.aterrizaje_solicitado == True:
                    vuelos_habilitados.append(vuelo)
            
            if len(vuelos_habilitados) > 0:
                for i, vuelo in enumerate(vuelos_habilitados):
                    print(f"{i + 1}. {vuelo}")
                while True:
                    opcion = input("Ingrese el número del vuelo que desea Aterrizar: ")
                    try:
                        opcion = int(opcion)
                        if 1 <= opcion <= len(vuelos_habilitados):
                            vuelo_seleccionado = vuelos_habilitados[opcion - 1]                            
                            vuelo_seleccionado.aterrizar()
                            break  # Salir del bucle while después de una selección válida
                        else:
                            print("Número fuera de rango. Por favor, ingrese un número válido.")
                    except ValueError:
                        print("Por favor, ingrese un número entero válido.")
                
        else:
            print("El aeropuerto no habilitó el despegue aún.")


def menu_comisario(comisario,aeropuerto_actual):
    print(f"Bienvenido comisari@ {comisario.nombre}")
    while True:
        print("\nMenú de Comisario de Vuelo:")
        print("1. Solicitar despegue")
        print("2. Solicitar aterrizaje")
        print("3. Despegar")
        print("4. Aterrizar")
        print("5. Volver al menú principal")

        opcion_comisario = input("Seleccione una opción: ")

        if opcion_comisario == "1": 
            solicitar_despegue(comisario,aeropuerto_actual)                 
            
        elif opcion_comisario == "2":
            solicitar_aterrizaje(comisario,aeropuerto_actual)
            print("Aterrizaje solicitado.")
        elif opcion_comisario == "3":
            despegar(aeropuerto_actual)
            
        elif opcion_comisario == "4":
            aterrizar(aeropuerto_actual)
            
        elif opcion_comisario == "5":
            print("Volviendo al menú principal ... ")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

def comisarios_vuelo(comisarios, aeropuerto_actual):
    nombre_comisario = input("Ingrese nombre de comisario/a : ")
    flag = False
    for comisario in comisarios:
        if nombre_comisario == comisario.nombre:            
            flag = True            
            menu_comisario(comisario, aeropuerto_actual)
            break
    
    if flag == False:
        print("Nombre no encontrado. ")

        
    

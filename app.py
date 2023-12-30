from clases.datos import *




# Menú principal
def menu_personal_aeropuerto(aeropuerto_actual):
    
    while True:
        
        print("1- Habilitar despegue ")
        print("2- Habilitar aterrizaje ")
        print("3-Añadir vuelo")
        print("4-volver a la pantalla anterior ")
        opt = int(input("Ingrese una opcion : "))

        if opt == 1:
            print("Despegue habilitado")
        elif opt == 2:
            print("Aterrizaje habilitado")
        elif opt == 3:
            print("Vuelo añadido")
        elif opt ==4:
            print("volviendo al menú principal")
            break
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

def comisarios_vuelo():
    print("Bienvenido comisari@")
    
def menu():
    while True:
        print("\nMenú Principal:")
        print("Lista de aeropuertos:")
        for i, aeropuerto in enumerate(aeropuertos):
            print(f"{i + 1}. {aeropuerto.nombre}")

        # Pedir al usuario que elija un número
        opcion = input("Ingrese el número correspondiente al aeropuerto que desea seleccionar: ")

        # Validar la entrada del usuario
        try:
            opcion = int(opcion)
            if 1 <= opcion <= len(aeropuertos):
                aeropuerto_actual = aeropuertos[opcion - 1]
                print(f"Ha seleccionado el aeropuerto: {aeropuerto_actual.nombre}")
            else:
                print("Número fuera de rango. Por favor, ingrese un número válido.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
        
        if aeropuerto_actual:
            print(f"Bienvenido al aeropuerto {aeropuerto_actual.nombre} ({aeropuerto_actual.ciudad})!")

            while True:
                print("\nSeleccione una opción:")
                print("1. Personal de Aeropuerto")
                print("2. Comisario de Vuelo")
                print("3. Salir")

                opcion = input("Ingrese el número de la opción: ")

                # En la sección donde el usuario selecciona el aeropuerto y la opción 1
                if opcion == "1":
                    personal_aeropuerto(aeropuerto_actual)

                elif opcion == "2":
                    print("\nMenú de Comisario de Vuelo:")
                    print("1. Solicitar despegue")
                    print("2. Solicitar aterrizaje")
                    print("3. Despegar")
                    print("4. Aterrizar")
                    print("5. Volver al menú principal")

                    opcion_comisario = input("Seleccione una opción: ")

                    if opcion_comisario == "1":                  
                        print("Despegue solicitado.")
                    elif opcion_comisario == "2":
                        print("Aterrizaje solicitado.")
                    elif opcion_comisario == "3":
                        print("Despegue realizado.")
                    elif opcion_comisario == "4":
                        print("Aterrizaje realizado.")
                    elif opcion_comisario == "5":
                        continue
                    else:
                        print("Opción no válida. Inténtelo de nuevo.")

                elif opcion == "3":
                    print("Saliendo del programa.")
                    break

        else:
            print("Opción no válida. Inténtelo de nuevo.")
    

# Ejecutar el menú
menu()



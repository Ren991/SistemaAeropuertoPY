from clases.datos import *

for empleado in empleados:
    print(empleado.aeropuerto.ciudad)


# Menú principal
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

            print("\nSeleccione una opción:")
            print("1. Personal de Aeropuerto")
            print("2. Comisario de Vuelo")
            print("3. Salir")

            opcion = input("Ingrese el número de la opción: ")

            # En la sección donde el usuario selecciona el aeropuerto y la opción 1
            if opcion == "1" and opcion:
                
                print("hola")
            else:
                print("Número de aeropuerto fuera de rango.")

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
                # Lógica para solicitar aterrizaje (puedes implementarla según tus necesidades)
                print("Aterrizaje solicitado.")
            elif opcion_comisario == "3":
                # Lógica para despegar (puedes implementarla según tus necesidades)
                print("Despegue realizado.")
            elif opcion_comisario == "4":
                # Lógica para aterrizar (puedes implementarla según tus necesidades)
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
    else:
        print("Nombre de aeropuerto no válido. Inténtelo de nuevo.")

# Ejecutar el menú
menu()



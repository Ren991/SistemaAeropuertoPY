from clases.datos import *
from comisarios_vuelos import *
from personal_aeropuerto import *

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
                    comisarios_vuelo(comisarios)                   

                elif opcion == "3":
                    print("Saliendo del programa.")
                    break
        else:
            print("Opción no válida. Inténtelo de nuevo.") 
# Ejecutar el menú
menu()



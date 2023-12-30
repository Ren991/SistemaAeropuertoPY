

def menu_comisario(comisario):
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
            print("Despegue solicitado.")
        elif opcion_comisario == "2":
            print("Aterrizaje solicitado.")
        elif opcion_comisario == "3":
            print("Despegue realizado.")
        elif opcion_comisario == "4":
            print("Aterrizaje realizado.")
        elif opcion_comisario == "5":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

def comisarios_vuelo(comisarios):
    nombre_comisario = input("Ingrese nombre de comisario/a : ")
    flag = False
    for comisario in comisarios:
        if nombre_comisario == comisario.nombre:
            
            flag = True
            
            menu_comisario(comisario)
            break
    
    if flag == False:
        print("Nombre no encontrado. ")

        
    

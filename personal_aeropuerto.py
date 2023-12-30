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
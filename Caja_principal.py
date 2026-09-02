import Caja_de_herramientas
import Caja_de_policia

activo=True
while activo:
    print("MENU PRINCIPAL")
    print("===============")
    print("1.Registrar materia o actividad:")
    print("2.Ver el horario semanal")
    print("3.Modificar una materia o actividad:")
    print("4.Eliminar una materia o actividad:")
    print("5.Generar reporte del horario")
    print("6.Salir")

    opcion=int(input("Ingrese una opción: "))
    if opcion == 1:
        nombremateriaoactividad = input("Ingrese el nombre de la materia o actividad: ")
        print(f"Nombre de la materia o actividad '{nombremateriaoactividad}' agregada.")
        diadelasemana = input("Ingrese el día de la semana: ")
        print(f"Día de la semana '{diadelasemana}' agregado.")
        horadeinicio = input("Ingrese la hora de inicio: ")
        print(f"Hora de inicio '{horadeinicio}' agregada.")
        horadefin = input("Ingrese la hora de fin: ")
        print(f"Hora de fin '{horadefin}' agregada.")
        decirubicacion = input("Ingrese la ubicación de la actividad: ")
        print(f"Ubicación '{decirubicacion}' agregada.")
        
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    elif opcion == 6:
        print("Saliendo del programa...")
        activo = False
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")
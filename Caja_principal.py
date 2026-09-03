import caja_de_herramientas
import caja_de_policia
from caja_de_herramientas import ver_horario_semanal
from caja_de_policia import datoscorrectos
lista_materias = caja_de_herramientas.cargar_datos()

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
        decirubicacion = input("Ingrese la ubicación de la actividad(si no presionar enter): ")
        print(f"Ubicación '{decirubicacion}' agregada.")
        if caja_de_policia.datoscorrectos(nombremateriaoactividad, diadelasemana, horadeinicio, horadefin, decirubicacion, lista_materias):

            nueva_materia = {
            "materia": nombremateriaoactividad,
            "dia": diadelasemana,
            "hora_inicio": horadeinicio,
            "hora_fin": horadefin,
            "ubicacion": decirubicacion
        }
            lista_materias.append(nueva_materia)
            caja_de_herramientas.guardar_datos(lista_materias)
            print(f"¡Éxito! La materia '{nombremateriaoactividad}' fue agregada.")
        else:
            print("Los datos no son correctos. No se puede registrar la materia.")
    elif opcion == 2:
        caja_de_herramientas.ver_horario_semanal(lista_materias)
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
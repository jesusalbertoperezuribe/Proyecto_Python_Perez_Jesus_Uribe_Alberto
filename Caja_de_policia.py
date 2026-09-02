def datoscorrectos(nombremateriaoactividad, diadelasemana, horadeinicio, horadefin, decirubicacion, lista_materias):
    if horadeinicio >= horadefin:
        print("Error: La hora de inicio no puede ser mayor o igual a la hora de fin.")
        return False

    for materia_guardada in lista_materias:
        if materia_guardada["materia"].lower() == nombremateriaoactividad.lower() and materia_guardada["dia"].lower() == diadelasemana.lower():
            print(f"Error: La materia '{nombremateriaoactividad}' ya está registrada el día {diadelasemana}.")
            return False

        if materia_guardada["dia"].lower() == diadelasemana.lower():
            if horadeinicio < materia_guardada["hora_fin"] and horadefin > materia_guardada["hora_inicio"]:
                print(f"Error: El horario {horadeinicio} - {horadefin} choca con {materia_guardada['materia']} ({materia_guardada['hora_inicio']} - {materia_guardada['hora_fin']}).")
                return False

    return True

    
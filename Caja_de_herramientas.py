import json

def cargar_datos():
    try:
        with open("horario.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return []

def guardar_datos(lista_materias):
    try:
        with open("horario.json", "w", encoding="utf-8") as archivo:
            datos_json = json.dumps(lista_materias, indent=4, ensure_ascii=False)
            archivo.write(datos_json)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def ver_horario_semanal(lista_materias):
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    horas_set = set()
    for m in lista_materias:
        horas_set.add(m["hora_inicio"])
    horas = sorted(list(horas_set))

    if not horas:
        print("\nEl horario está vacío. Registre materias primero.")
        return

    print("\n========================================================================================================")
    print(f"| {'Hora':<10} | {'Lunes':<15} | {'Martes':<15} | {'Miércoles':<15} | {'Jueves':<15} | {'Viernes':<15} |")
    print("========================================================================================================")

    for hora in horas:
        fila = f"| {hora:<10} |"
        for dia in dias:
            encontrado = False
            for m in lista_materias:
                if m["dia"].lower() in [dia.lower(), dia.lower().replace('é', 'e')] and m["hora_inicio"].upper() == hora.upper():
                    fila += f" {m['materia'][:14]:<15} |"
                    encontrado = True
                    break
            if not encontrado:
                fila += f" {'Libre':<15} |"
        print(fila)

    print("========================================================================================================\n")

def generar_reporte(lista_materias):
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    reporte = []

    print("\n==========================================")
    print("REPORTE DEL HORARIO SEMANAL")
    print("==========================================")

    for dia in dias:
        eventos_dia = []
        for m in lista_materias:
            if m["dia"].lower() in [dia.lower(), dia.lower().replace('é', 'e')]:
                eventos_dia.append({
                    "materia": m["materia"],
                    "hora_inicio": m["hora_inicio"],
                    "hora_fin": m["hora_fin"],
                    "ubicacion": m["ubicacion"]
                })
        
        if eventos_dia:
            eventos_dia = sorted(eventos_dia, key=lambda x: x["hora_inicio"])
            reporte.append({
                "dia": dia,
                "eventos": eventos_dia
            })

            print(f"{dia}:")
            for e in eventos_dia:
                print(f" - {e['materia']} ({e['hora_inicio']}-{e['hora_fin']}) en {e['ubicacion']}")
            
            input("Presione ENTER para continuar...")

    try:
        with open("reporte_horario.json", "w", encoding="utf-8") as archivo:
            archivo.write(json.dumps(reporte, indent=4, ensure_ascii=False))
        print("\n¡Reporte JSON generado exitosamente como 'reporte_horario.json'!")
    except Exception as e:
        print(f"Error al guardar el reporte: {e}")
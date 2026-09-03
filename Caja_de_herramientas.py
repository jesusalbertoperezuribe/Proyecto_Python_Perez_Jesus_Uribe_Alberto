import json

def cargar_datos():
    try:
        with open("horario.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo) 
    except FileNotFoundError:
        return []

def ver_horario_semanal(lista_materias):
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    horas = ["08:00 AM", "10:00 AM", "12:00 PM", "02:00 PM"]

    print("\n=================================================================")
    print(f"| {'Hora':<10} | {'Lunes':<11} | {'Martes':<11} | {'Miércoles':<11} | {'Jueves':<11} | {'Viernes':<11} |")
    print("=================================================================")

    for hora in horas:
        fila = f"| {hora:<10} |"
        for dia in dias:
            encontrado = False
            for m in lista_materias:
                if m["dia"].lower() == dia.lower() and m["hora_inicio"].upper() == hora:
                    fila += f" {m['materia']:<11} |"
                    encontrado = True
                    break
            if not encontrado:
                fila += f" {'Libre':<11} |"
        print(fila)

    print("=================================================================\n")


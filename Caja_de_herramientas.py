import json
def importar_datos():
    try:
        with open("datos.json", "r") as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        return {}

def verhorariosemanal():


    return "Horario semanal: Lunes a Viernes de 8:00 a 18:00"
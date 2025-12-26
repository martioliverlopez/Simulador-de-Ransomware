import os
from datetime import datetime

RUTA_LOGS = os.path.join("logs", "activity.log")

def llistar_fitxers(ruta):
    llista_final = []
    if os.path.exists(ruta):
        for arrel, directoris, fitxers in os.walk(ruta):
            for nom in fitxers:
                llista_final.append(os.path.join(arrel, nom))
        return llista_final
    return []

def registrar_log(missatge, nivell):
    carpeta_logs = os.path.dirname(RUTA_LOGS)
    if not os.path.exists(carpeta_logs):
        os.makedirs(carpeta_logs)
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linia = f"[{data}] [{nivell}] {missatge}\n"
    with open(RUTA_LOGS, "a", encoding="utf-8") as f:
        f.write(linia)

def llegir_logs():
    if os.path.exists(RUTA_LOGS):
        with open(RUTA_LOGS, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("No hi ha logs disponibles.")

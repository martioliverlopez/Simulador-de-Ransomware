import os
from datetime import datetime

def llistar_fitxers(ruta: str):
    
    if os.path.exists(ruta):
        arxius = os.listdir(ruta)
        print(f"--- Arxius trobats a {ruta} ---")
        
        for arxiu in arxius:
            ruta_completa = os.path.join(ruta, arxiu)
            if os.path.isfile(ruta_completa):
                print(arxiu)      
        return arxius
    else:
        print("[ERROR]: No s'ha trobat l'arxiu")
        return []

#print(llistar_fitxers("ruta_que_no_existeix"))        #Aquesta linea serveix de prova per a veure que el programa funciona

RUTA_LOGS = os.path.join("logs", "activity.log")

def registrar_log(missatge: str, nivell: str):
    #La funció registra els logs amb [DATA] [NIVELL] I MISSATGE
    #nivells: INFO,WARNING,ERROR,CRITICAL
    carpeta_logs = os.path.dirname(RUTA_LOGS)

    if not os.path.exists(carpeta_logs):
        os.makedirs(carpeta_logs)

    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    linia_log = f"[{data}] [{nivell}] {missatge}\n"

    try:
        with open(RUTA_LOGS, "a", encoding="utf-8") as file:
            file.write(linia_log)
    except Exception as error:
        print(f"[X] ERROR AL ESCRIURE ELS LOGS")

def llegir_logs():

    if not os.path.exists(RUTA_LOGS):
        print("[INFO] NO EXISTEIX EL REGISTRE D'ACTIVITAT PRÈVIA")
        return None
    print("="*10)
    print("HISTORIAL DE LOGS")
    print("="*10)

    try:
        with open(RUTA_LOGS, "r", encoding="utf-8") as file:
                contingut = file.read()
                if contingut:
                    print(contingut)
                else:
                    print("[INFO] EL FITXER DE LOGS ESTÀ BUIT")
    except Exception as error:
        print(f"[ERROR] ERROR LLEGINT ELS LOGS: {error}")
    
    print("="*30)
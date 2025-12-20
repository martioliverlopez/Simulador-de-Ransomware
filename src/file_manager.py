import os
from datetime import datetime

def llistar_fitxers(ruta):
    # 1. Creem la llista buida
    llista_final = []
    
    # 2. Comprovem si la carpeta existeix
    if os.path.exists(ruta):
        # 3. Busquem a totes les subcarpetes
        for arrel, directoris, fitxers in os.walk(ruta):
            for nom in fitxers:
                # 4. Creem el cami sencer i el guardem
                cami_sencer = os.path.join(arrel, nom)
                llista_final.append(cami_sencer)
        
        # 5. Registrem quants n'hem trobat i retornem la llista
        registrar_log("Fitxers trobats: " + str(len(llista_final)), "INFO")
        return llista_final
    else:
        registrar_log("Error: No s'ha trobat la carpeta", "ERROR")
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
        print("[INFO] NO EXISTEIX EL REGISTRE D'ACTIVITAT PREVIA")
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
                    print("[INFO] EL FITXER DE LOGS ESTA BUIT")
    except Exception as error:
        print(f"[ERROR] ERROR LLEGINT ELS LOGS: {error}")
    
    print("="*30)

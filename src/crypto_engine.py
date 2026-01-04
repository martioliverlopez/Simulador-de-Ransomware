# -*- coding: utf-8 -*-
import os
from cryptography.fernet import Fernet, InvalidToken
import file_manager

def generar_i_guardar_clau(ruta):
    # Genera una nova clau de xifratge Fernet i la desa en un fitxer
    if os.path.exists(ruta) and os.path.getsize(ruta) > 0:
        print(f"[INFO] La clau ja existeix a {ruta}, s'ha abortat la generacio d'una nova")
        file_manager.registrar_log("CLAU_NO_GENERADA", ruta)
        return

    clau = Fernet.generate_key()
    try:
        with open(ruta, "wb") as clau_file:
            clau_file.write(clau)
        file_manager.registrar_log("CLAU_GENERADA", ruta)
    except Exception as error:
        print(f"[X] ERROR GENERANT CLAU: {error}")

def carregar_clau(ruta):
    # Carrega la clau de xifratge des d'un fitxer
    if not os.path.exists(ruta):
        return None
    try:
        with open(ruta, "rb") as file:
            return file.read()
    except Exception as e:
        print(f"[X] Error carregant clau: {e}")
        return None

def xifrar_arxiu(ruta, clau):
    # Xifra un fitxer utilitzant l'algoritme Fernet i el reanomena
    try:
        f = Fernet(clau)
        with open(ruta, "rb") as file:
            dades = file.read()
        encriptat = f.encrypt(dades)
        with open(ruta, "wb") as file:
            file.write(encriptat)
        locked_nom = ruta + ".locked"
        os.rename(ruta, locked_nom)
        return True
    except Exception as e:
        print(f"[X] Error xifrant {ruta}: {e}")
        return False

def desxifrar_arxiu(ruta, clau):
    # Desxifra un fitxer .locked i restaura el nom original
    try:
        f = Fernet(clau)
        with open(ruta, "rb") as file:
            dades = file.read()
        desencriptat = f.decrypt(dades)
        original = ruta.replace(".locked", "")
        with open(ruta, "wb") as file:
            file.write(desencriptat)
        os.rename(ruta, original)
        return True
    except InvalidToken:
        print(f"[!] ERROR CRITIC: La clau no es valida per a desxifrar {ruta}")
        return False
    except Exception as e:
        print(f"Error desxifrant {ruta}: {e}")
        return False

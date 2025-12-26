import os
from cryptography.fernet import Fernet, InvalidToken
import file_manager

def generar_i_guardar_clau(ruta):
    clau = Fernet.generate_key()
    try:
        with open(ruta, "wb") as clau_file:
            clau_file.write(clau)
        file_manager.registrar_log(f"CLAU GENERADA A {ruta}", "INFO")
    except Exception as e:
        print(f"[X] ERROR GENERANT CLAU: {e}")

def carregar_clau(ruta):
    if not os.path.exists(ruta):
        return None
    try:
        with open(ruta, "rb") as file:
            return file.read()
    except Exception:
        return None

def xifrar_arxiu(ruta, clau):
    try:
        f = Fernet(clau)
        with open(ruta, "rb") as file:
            dades = file.read()
        encriptat = f.encrypt(dades)
        with open(ruta, "wb") as file:
            file.write(encriptat)
        os.rename(ruta, ruta + ".locked")
    except Exception as e:
        print(f"Error xifrant {ruta}: {e}")

def desxifrar_arxiu(ruta, clau):
    try:
        f = Fernet(clau)
        with open(ruta, "rb") as file:
            dades = file.read()
        desencriptat = f.decrypt(dades)
        original = ruta.replace(".locked", "")
        with open(ruta, "wb") as file:
            file.write(desencriptat)
        os.rename(ruta, original)
    except Exception as e:
        print(f"Error desxifrant {ruta}: {e}")

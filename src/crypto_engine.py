import os
from cryptography.fernet import Fernet


def administrar_clau():
    clau = Fernet.generate_key()
    print(f"[✔] CLAU GENERADA")
    return clau

def guardar_clau(ruta,clau):

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

def encriptar_arxiu(ruta,clau):

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
            print(f"[✔] ARXIU XIFRAT CORRECTAMENT")

    except IOError as error:
        print(f"[X] ERROR AL GUARDAR: {error}")
    except TypeError as error:
        print(f"[X] ERROR: DADES EN FORMAT INCORRECTE")
    except Exception as error:
        print(f"[X] ERROR INESPERAT: {error}")
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
        print(f"[INFO] Carpeta creada: {directori}")
    try:
        with open(ruta, "wb") as clau_file:
            clau_file.write(clau)
            print(f"[✔] CLAU GUARDADA A {ruta}")
    except IOError as error:
        print(f"[X] ERROR AL GUARDAR: {error}")

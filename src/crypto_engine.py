# -*- coding: utf-8 -*-
import os
import file_manager

# Clau mestra per al simulacre de pagament
CLAU_MESTRA = b'uX9-03X-uS6uQ1_uR6uS6uQ1_uR6uS6uQ1_uR6uS6='

def generar_i_guardar_clau(ruta):
    try:
        # Creem la carpeta system si no existeix
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, "wb") as f:
            f.write(CLAU_MESTRA)
        file_manager.registrar_log("CLAU_GENERADA", ruta)
        return True
    except:
        return False

def carregar_clau(ruta):
    if not os.path.exists(ruta): return None
    try:
        with open(ruta, "rb") as f:
            return f.read()
    except:
        return None

def xifrar_arxiu(ruta, clau):
    try:
        # Llegim dades originals
        with open(ruta, "rb") as f:
            dades = f.read()
        
        # Xifratge XOR manual: robust per a qualsevol tipus de fitxer
        dades_xifrades = bytes([b ^ clau[i % len(clau)] for i, b in enumerate(dades)])
        
        # Escrivim dades xifrades
        with open(ruta, "wb") as f:
            f.write(dades_xifrades)
        
        # Reanomenem el fitxer real al disc
        os.rename(ruta, ruta + ".locked")
        return True
    except Exception as e:
        print(f"DEBUG ERROR MOTOR: {e}")
        return False

def desxifrar_arxiu(ruta, clau):
    try:
        with open(ruta, "rb") as f:
            dades = f.read()
            
        # El mateix proces XOR desxifra les dades
        dades_originals = bytes([b ^ clau[i % len(clau)] for i, b in enumerate(dades)])
        
        with open(ruta, "wb") as f:
            f.write(dades_originals)
            
        # Restaurem el nom original
        os.rename(ruta, ruta.replace(".locked", ""))
        return True
    except:
        return False

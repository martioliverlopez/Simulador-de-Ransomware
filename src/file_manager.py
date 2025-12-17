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
        return ""

print(llistar_fitxers("ruta_que_no_existeix"))

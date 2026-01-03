import os

#Directori actual
CURR_DIR = os.path.dirname(os.path.abspath(__file__))
#Directori del simulador de ransomware
ROOT_DIR = os.path.dirname(CURR_DIR)

#Directori Data
DATA_DIR = os.path.join(ROOT_DIR, "data")
#Subcarpetes del projecte
LOGS_DIR = os.path.join(DATA_DIR, "logs")
SAND_DIR = os.path.join(DATA_DIR, "sandbox")
SYST_DIR = os.path.join(DATA_DIR, "system") 
ASST_DIR = os.path.join(DATA_DIR, "assets") 

#--Fitxers especifics--
#Arxiu de la clau criptografica
FILE_KEY = os.path.join(SYST_DIR, "config_sys_04.dat")
#Arxiu dels logs
FILE_LOGS = os.path.join(LOGS_DIR, "activity.jsonl")
#Arxiu de la imatge per al fons de pantalla de la GUI
FILE_LOGO = os.path.join(ASST_DIR, "logo_virus.png")
#Nota de rescat (es crea dins de la sandbox)
FILE_RANSOM_NOTE = os.path.join(SAND_DIR, "INSTRUCCIONS_RECUPERACIO.txt")

#Llogica de creacio de carpetes si s'esborren per equivocacio
dirs_to_create = [LOGS_DIR, SAND_DIR, SYST_DIR, ASST_DIR]

for directory in dirs_to_create:
    os.makedirs(directory, exist_ok=True)
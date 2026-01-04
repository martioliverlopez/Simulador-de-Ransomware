# config.py
import os

# Directori base: on es troba aquest fitxer config.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Tota la informacio a la subcarpeta 'data' que acabes de moure
DATA_DIR = os.path.join(BASE_DIR, "data")

LOGS_DIR = os.path.join(DATA_DIR, "logs")
SAND_DIR = os.path.join(DATA_DIR, "sandbox")
SYST_DIR = os.path.join(DATA_DIR, "system") 
ASST_DIR = os.path.join(DATA_DIR, "assets") 

# Fitxers especifics
FILE_KEY = os.path.join(SYST_DIR, "config_sys_04.dat")
FILE_LOGS = os.path.join(LOGS_DIR, "activity.jsonl")
FILE_LOGO = os.path.join(ASST_DIR, "logo_virus.png")

# Creacio automatica de subcarpetes
for directory in [LOGS_DIR, SAND_DIR, SYST_DIR, ASST_DIR]:
    os.makedirs(directory, exist_ok=True)

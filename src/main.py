import os
import file_manager                 
import crypto_engine

RUTA_SANDBOX = "sandbox"
RUTA_CLAU = "gestor_claus.key"
PROHIBITED_WHITELIST = [".py", ".key", ".exe", ".dll", ".sys", ".locked", ".ini", ".lnk", ".bat"]                    #Creem una llista clara de tot el que NO volem xifrar mai i afegim les extensions del sistema per seguretat

def mostrar_menu():             
    file_manager.registrar_log("SESSIO INICIADA AL SIMULADOR DE RANSOMWARE", "INFO")                   
    while True:
        print("\n" + "=" * 32)
        print("   SIMULADOR DE RANSOMWARE")    
        print("  Marti Oliver - Marc Fernandez")     
        print("        ENTI - UB")             
        print("=" * 32)
        print("1. Infectar (Xifrar)")          
        print("2. Recuperar (Desxifrar)")       
        print("3. Veure historial (Logs)")      
        print("4. Sortir")                      
        
        opcio = input("\nTria una opcio (1-4): ")        
        
        if opcio == "1":
            file_manager.registrar_log("LA OPCIO 'INFECTAR' HA ESTAT SELECCIONADA", "INFO")
            print("\n[INICIANT XIFRATGE...]")
            
            if not os.path.exists(RUTA_SANDBOX):
                print("[X] ERROR: NO EXISTEIX EL FOLDER SANDBOX")
                file_manager.registrar_log("INTENT D'INFECCIO FALLIT, FOLDER SANDBOX INEXISTENT", "WARNING")
                continue
                
            if os.path.exists(RUTA_CLAU):
                print("\n[EXTRAIENT LA CLAU...]")
                clau = crypto_engine.carregar_clau(RUTA_CLAU)
            else:
                print("\n CREANT LA CLAU...")
                crypto_engine.generar_i_guardar_clau(RUTA_CLAU)
                clau = crypto_engine.carregar_clau(RUTA_CLAU)

            # Aqui fem servir la nova funcio recursiva de la SDR-14
            llista_arxius = file_manager.llistar_fitxers(RUTA_SANDBOX)

            for ruta_completa in llista_arxius:
                # Agafem el nom del fitxer per comprovar l'extensio
                nom_arxiu, extensio = os.path.splitext(ruta_completa)

                # Filtres de seguretat (Llista blanca)
                if extensio.lower() in PROHIBITED_WHITELIST or nom_arxiu.startswith("."):
                    print("[SEGURETAT] Ignorant fitxer protegit: " + ruta_completa)
                    continue

                crypto_engine.xifrar_arxiu(ruta_completa, clau)
            
            print("ARXIUS XIFRATS CORRECTAMENT A " + RUTA_SANDBOX)

        elif opcio == "2":
            file_manager.registrar_log("LA OPCIO 'RECUPERAR' HA ESTAT SELECCIONADA", "INFO")
            print("\n[INICIANT RECUPERACIO...]")
            
            clau = crypto_engine.carregar_clau(RUTA_CLAU)
            if not clau:
                print("[X] ERROR: LA CLAU NO S'HA TROBAT")
                file_manager.registrar_log("ERROR DE RECUPERACIO, CLAU INEXISTENT", "ERROR")
                continue

            llista_arxius = file_manager.llistar_fitxers(RUTA_SANDBOX)
            
            for ruta_completa in llista_arxius:
                if ruta_completa.endswith(".locked"):
                    crypto_engine.desxifrar_arxiu(ruta_completa, clau)

            print("ARXIUS RECUPERATS CORRECTAMENT A " + RUTA_SANDBOX)

        elif opcio == "3":
            print("\n[MOSTRANT HISTORIAL DE LOGS]")
            file_manager.llegir_logs()
            input("\n PREM ENTER PER A CONTINUAR")
            
        elif opcio == "4":
            file_manager.registrar_log("SESSIO TANCADA AL SIMULADOR DE RANSOMWARE", "INFO")
            print("\n[INFO]: Simulacio finalitzada amb seguretat.")
            break
        else:
            print("[ERROR]: Opcio no valida.")

if __name__ == "__main__":
    mostrar_menu()

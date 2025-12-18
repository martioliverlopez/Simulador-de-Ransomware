import os
import file_manager                 
import crypto_engine

RUTA_SANDBOX = "sandbox"
RUTA_CLAU = "gestor_claus.key"

def mostrar_menu():                                
    while True:
        print("\n" + "=" * 32)
        print("   SIMULADOR DE RANSOMWARE")    
        print("  Marti Oliver - Marc Fernandez")     
        print("           ENTI - UB")             
        print("=" * 32)
        print("1. Infectar (Xifrar)")          # Tasca SDR-9 
        print("2. Recuperar (Desxifrar)")       # Tasca SDR-12 
        print("3. Veure historial (Logs)")      # Tasca SDR-10 
        print("4. Sortir")                      
        
        opcio = input("\nTria una opcio (1-4): ")        
        
        if opcio == "1":
            print("\n[INICIANT XIFRATGE...]")
            if not os.path.exists(RUTA_SANDBOX):
                print("[X] ERROR: NO EXISTEIX EL FOLDER SANDBOX, ENCRIPTACIÓ ATURADA")
                continue
            if os.path.exists(RUTA_CLAU) and RUTA_CLAU:
                print("\n[EXTRAIENT LA CLAU...]")
                clau = crypto_engine.carregar_clau(RUTA_CLAU)
            else:
                print("\n CREANT LA CLAU...")
                crypto_engine.generar_i_guardar_clau(RUTA_CLAU)
                clau = crypto_engine.carregar_clau(RUTA_CLAU)

            llista_arxius = file_manager.llistar_fitxers(RUTA_SANDBOX)

            for arxiu in llista_arxius:

                ruta_completa = os.path.join(RUTA_SANDBOX, arxiu)

                if arxiu.startswith(".") or arxiu.endswith(".py") or arxiu.endswith(".key") or arxiu.endswith(".exe") or arxiu.endswith(".dll") or arxiu.endswith(".sys") or arxiu.endswith(".locked"):
                    continue

                crypto_engine.xifrar_arxiu(ruta_completa, clau)
            print(f"ARXIUS XIFRATS CORRECTAMENT A {RUTA_SANDBOX}")

        elif opcio == "2":
            print("\n[INICIANT RECUPERACIO...]")
            clau = crypto_engine.carregar_clau(RUTA_CLAU)
            if not clau:
                print(f"[X] ERROR: LA CLAU NO S'HA TROBAT A {RUTA_CLAU}")
                continue

            llista_arxius = file_manager.llistar_fitxers(RUTA_SANDBOX)
            
            for arxiu in llista_arxius:
                ruta_completa = os.path.join(RUTA_SANDBOX, arxiu)
                if arxiu.endswith(".locked"):
                    crypto_engine.desxifrar_arxiu(ruta_completa, clau)

            print(f"ARXIUS DESXIFRATS CORRECTAMENT A {RUTA_SANDBOX}")
        elif opcio == "3":
            print("\n[MOSTRANT HISTORIAL DE LOGS]")
            
        elif opcio == "4":
            print("\n[INFO]: Simulacio finalitzada amb seguretat.")
            print("[INFO]: Revisa la carpeta 'logs' per veure l'activitat.")
            break
        else:
            print(f"[ERROR]: '{opcio}' no es valid. Tria del 1 al 4.")

mostrar_menu()

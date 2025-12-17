import file_manager                 
import crypto_engine



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
            print("\n[INICIANT INFECTACIO...]")
            file_manager.llistar_fitxers("Sandbox")
            
        elif opcio == "2":
            print("\n[INICIANT RECUPERACIO...]")
            
        elif opcio == "3":
            print("\n[MOSTRANT HISTORIAL DE LOGS]")
            
        elif opcio == "4":
            print("\n[INFO]: Simulacio finalitzada amb seguretat.")
            print("[INFO]: Revisa la carpeta 'logs' per veure l'activitat.")
            break
        else:
            print(f"[ERROR]: '{opcio}' no es valid. Tria del 1 al 4.")

mostrar_menu()

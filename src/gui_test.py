import customtkinter as ctk

def provar_interfac():

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("500x300")
    app.title("SDR - PROVA DE CONFIGURACIO GRAFICA")


    titol = ctk.CTkLabel(
        app, 
        text="TASCA FINALITZADA AMB EXIT", 
        font=("Arial", 24, "bold")
    )
    titol.pack(pady=30)

    subtitol = ctk.CTkLabel(
        app, 
        text="Llibreria CustomTkinter instal-lada i configurada per Marc.",
        font=("Arial", 14)
    )
    subtitol.pack(pady=10)


    boto_tancar = ctk.CTkButton(
        app, 
        text="TANCAR I FER COMMIT", 
        command=app.destroy
    )
    boto_tancar.pack(pady=40)


    print("[V] La finestra de prova s ha obert correctament.")
    app.mainloop()

if __name__ == "__main__":
    provar_interfac()

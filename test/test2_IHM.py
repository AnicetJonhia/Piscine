import tkinter as tk
from tkinter import ttk
import csv

def charger_fichier():
    chemin_fichier = chemin_fichier_entry.get()
    
    try:
        with open(chemin_fichier, newline='') as fichier:
            lecteur_csv = csv.reader(fichier)
            
            for item in treeview.get_children():
                treeview.delete(item)

            for ligne in lecteur_csv:
                if len(ligne) > 0:
                    treeview.insert("", "end", values=(ligne[0],))
    except Exception as e:
        print("Une erreur s'est produite :", str(e))

app = tk.Tk()
app.title("Liste d'adresses")

frame = ttk.Frame(app)
frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

chemin_fichier_label = ttk.Label(frame, text="Chemin du fichier CSV :")
chemin_fichier_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

chemin_fichier_entry = ttk.Entry(frame)
chemin_fichier_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

charger_button = ttk.Button(frame, text="Charger un fichier d'adresses", command=charger_fichier)
charger_button.grid(row=0, column=2, padx=10, pady=5, sticky="w")

treeview = ttk.Treeview(app, columns=("Adresse e-mail",), show="headings")
treeview.heading("Adresse e-mail", text="Adresse e-mail")
treeview.grid(row=1, column=0, padx=10, pady=5, sticky="w")

app.mainloop()


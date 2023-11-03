import tkinter as tk
from tkinter import ttk
import csv
import sendMail

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

def rafraichir():
    # Simulation de récupération de données depuis une base de données
    # Dans cet exemple, nous utilisons des données de démonstration
    donnees_bdd = [
        ("john@example.com", True, False, "2023-11-02", "john_doe", "motdepasse123"),
        ("jane@example.com", False, True, "2023-11-01", "jane_doe", "password456"),
        ("bob@example.com", True, True, "2023-10-31", "bob_smith", "secret789")
    ]
    
    for item in treeview.get_children():
        treeview.delete(item)
    
    for ligne in donnees_bdd:
        treeview.insert("", "end", values=(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4], ligne[5]))

def envoyer_mail():
    # Ici, vous pouvez ajouter le code pour préparer et envoyer un e-mail aux adresses de la liste
    sendMail()
    pass

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

rafraichir_button = ttk.Button(frame, text="Rafraîchir", command=rafraichir)
rafraichir_button.grid(row=0, column=3, padx=10, pady=5, sticky="w")

treeview = ttk.Treeview(app, columns=("Adresse e-mail", "Mail lu", "Lien cliqué", "Date d'affichage", "Login", "Mot de passe"), show="headings")
treeview.heading("Adresse e-mail", text="Adresse e-mail")
treeview.heading("Mail lu", text="Mail lu")
treeview.heading("Lien cliqué", text="Lien cliqué")
treeview.heading("Date d'affichage", text="Date d'affichage")
treeview.heading("Login", text="Login")
treeview.heading("Mot de passe", text="Mot de passe")
treeview.grid(row=1, column=0, padx=10, pady=5, sticky="w")

envoyer_button = ttk.Button(app, text="Envoyer un mail", command=envoyer_mail)
envoyer_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

app.mainloop()

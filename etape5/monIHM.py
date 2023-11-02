import tkinter as tk
from tkinter import ttk

def charger_fichier():
    # Ici, vous pouvez ajouter le code pour charger un fichier d'adresses
    # Par exemple, vous pouvez utiliser la bibliothèque tkinter pour demander à l'utilisateur de sélectionner un fichier

    # Exemple de données d'adresses sous forme de liste de tuples (pour la démonstration)
    adresses = [
        (True, False, "2023-11-02", "user1", "motdepasse1"),
        (False, True, "2023-11-01", "user2", "motdepasse12"),
        (True, True, "2023-10-31", "user3", "motdepasse123")
    ]


    afficher_adresses(adresses)

# def afficher_adresses(adresses):
#     for i, (lu, clic, date, login, mot_de_passe) in enumerate(adresses):
#         treeview.insert("", i, values=(lu, clic, date, login, mot_de_passe))


def afficher_adresses(adresses):
    for i, (lu, clic, date, login, mot_de_passe) in enumerate(adresses):
        treeview.insert("", i, values=(lu, clic, date, login, mot_de_passe))

app = tk.Tk()
app.title("Liste d'adresses")

frame = ttk.Frame(app)
frame.pack(padx=10, pady=10)

treeview = ttk.Treeview(frame, columns=("Mail lu", "Lien cliqué", "Date d'affichage", "Login", "Mot de passe"), show="headings")
treeview.heading("Mail lu", text="Mail lu")
treeview.heading("Lien cliqué", text="Lien cliqué")
treeview.heading("Date d'affichage", text="Date d'affichage")
treeview.heading("Login", text="Login")
treeview.heading("Mot de passe", text="Mot de passe")

treeview.pack()

charger_button = ttk.Button(app, text="Charger un fichier d'adresses", command=charger_fichier)
charger_button.pack()

app.mainloop()

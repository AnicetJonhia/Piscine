import csv

# Chemin vers le fichier CSV
fichier_csv = "mailAdress.csv"

# Ouvrez le fichier CSV en mode lecture
with open(fichier_csv, newline='') as fichier:
    lecteur_csv = csv.reader(fichier)

    # Parcourez chaque ligne du fichier CSV
    for ligne in lecteur_csv:
        # Assurez-vous que la ligne contient au moins une colonne
        if len(ligne) > 0:
            # Affichez la première colonne (supposée contenir les adresses email)
            adresse_email = ligne[0]
            print(adresse_email)

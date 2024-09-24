import os
# Parcourir un dossier donné
directory = '/chemin/du/dossier'
for root, dirs, files in os.walk(directory):
    print(f"Dans le dossier : {root}")
for file in files:
    print(f"Fichier trouvé : {file}")
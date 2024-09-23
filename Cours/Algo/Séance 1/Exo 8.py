prix = float(input("Entrez le prix : "))
quantite = int(input("Entrez la quantité : "))
remise = 0.85
tva = float(input("Saisissez le montant de la TVA sous forme décimale : "))
total = ((prix * quantite) * remise) * tva 
print("Le coût TTC de votre commande est de : ", total)
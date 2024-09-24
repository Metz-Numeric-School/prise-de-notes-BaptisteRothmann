montant_ttc = float(input("Entrez un montant TTC : "))
if 500 < montant_ttc < 1000:
    new_montant = montant_ttc * 0.98
elif 1000 < montant_ttc < 2000:
    new_montant = montant_ttc * 0.95
elif montant_ttc > 2000:
    new_montant = montant_ttc * 0.9
else:
    new_montant = montant_ttc

print(f"Le nouveau montant après remise est de {new_montant}€.")
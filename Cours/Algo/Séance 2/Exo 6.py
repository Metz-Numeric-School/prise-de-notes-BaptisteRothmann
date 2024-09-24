prix_ht = float(input("Saisissez le prix de l'objet : "))
print("Veuillez choisir le taux de TVA : ")
print("1 - La TVA est de 5,5%")
print("2 - La TVA est de 19,6%")
print("3 - La TVA est de 33")

code_tva = int(input("Saisissez le code TVA (1, 2 ou 3) : "))

if code_tva == 1:
    tva = 5.5
elif code_tva == 2:
    tva = 19.6
elif code_tva == 3:
    tva = 33

prix_ttc = prix_ht * (1 + tva / 100)
print(f"Le prix HT est de {prix_ht}€, la TVA est de {tva}% et le prix TTC est de {prix_ttc}€.")


a = float(input("Saisissez un nombre : "))
b = float(input("Saisissez un nombre : "))

somme = a + b
print(f"La somme (a + b) est égale à {somme}")

difference = a - b
print(f"La différence (a - b) est égale à {difference}")

produit = a * b 
print(f"Le produit (a * b) est égal à {produit}")

if b != 0:
    quotient = a / b 
    print(f"Le quotient (a / b) est égal à {quotient} ")
else:
    print("Erreur : divison par zéro")

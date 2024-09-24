chaine = input("Saisissez une chaîne de caractères : ")

l = len(chaine)
print(f"Il y a {l} caractères dans la chaîne.")

p = chaine[0]
print(f"Le premier caractère de la chaîne est {p}.")

d = chaine[-1]
print(f"Le dernier caractère de la chaîne est {d}.")

ma = chaine.upper()
print(f"La chaîne en majuscule donne : {ma}.")

mi = chaine.lower()
print(f"La chaîne en minuscule donne : {mi}.")

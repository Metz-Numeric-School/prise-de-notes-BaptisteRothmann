nombre = int(input("Entrez un nombre pour définir sa table de multiplication : "))
print(f"Table de multiplication de {nombre} :")
for i in range(1, 10):
    resultat = nombre * i
    print(f"{nombre} x {i} = {resultat}")
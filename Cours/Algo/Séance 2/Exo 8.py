a = float(input("Entrez la valeur de a : "))
b = float(input("Entrez la valeur de b : "))

if a == 0 and b == 0:
    print("L'ensemble des solutions est l'ensemble R.")
elif a == 0 and b != 0:
    print("L'ensemble des solutions est l'ensemble vide.")
else:
    solution = ((-b) / a)
    print(f"La solution de l'équation est {solution}.")

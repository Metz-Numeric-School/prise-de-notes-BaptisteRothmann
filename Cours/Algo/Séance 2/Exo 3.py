birth_year = int(input("Saisissez l'année de naissance du bébé : "))
year = int(input("Entrez l'année en cours : "))
age = year - birth_year
if age < 3:
    print("Le bébé a gagné une palette")
else:
    print("Le bébé n'a pas gagné de palette")
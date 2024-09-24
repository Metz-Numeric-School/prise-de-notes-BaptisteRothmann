note_francais = float(input("Saisissez la note de français : "))
note_maths = float(input("Saisissez la note de maths : "))
note_geometrie = float(input("Saisissez la note de géométrie : "))
note_informatique = float(input("Saisissez la note d'informatique : "))

coefficient_francais = int(input("Saissez le coefficient du français : "))
coefficient_maths = int(input("Saissez le coefficient des maths : "))
coefficient_geometrie = int(input("Saissez le coefficient de la géométrie : "))
coefficient_informatique = int(input("Saissez le coefficient de l'informatique : "))

coefficient_total = coefficient_maths + coefficient_informatique + coefficient_francais + coefficient_geometrie

moyenne = (((note_francais * coefficient_francais) + (note_maths * coefficient_maths) + (note_geometrie * coefficient_geometrie) + (note_informatique * coefficient_informatique)) / (coefficient_total))

print(f"Votre moyenne est de {moyenne}")

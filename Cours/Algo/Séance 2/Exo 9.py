note_francais = float(input("Saissiez la note de français : "))
note_maths = float(input("Saissiez la note de maths : "))
note_geographie = float(input("Saissiez la note de géographie : "))
note_informatique = float(input("Saissiez la note d'informatique : "))

moyenne = ((note_francais + note_geographie + note_maths + note_informatique) / 4)
print(f"Votre moyenne est de {moyenne}")

if 16 < moyenne < 20:
    print("Très bien")
elif 12 < moyenne < 16:
    print("Bien")
elif 8 < moyenne < 12:
    print("Assez bien")
elif 4 < moyenne < 8:
    print("Insuffisant")
elif 0 < moyenne < 4:
    print("Nul")
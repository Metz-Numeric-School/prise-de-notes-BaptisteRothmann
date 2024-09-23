note_francais = float(input("Note de français : "))
note_maths = float(input("Note de maths : "))
note_geometrie = float(input("Note de géométrie : "))
note_informatique = float(input("Note d'informatique : "))

moyenne = (note_francais + note_maths + note_geometrie + note_informatique) / 4
print(f"Vous avez {moyenne} de moyenne")
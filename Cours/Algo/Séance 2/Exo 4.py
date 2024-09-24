doigts_a = int(input("Combien de doigts le joueur A a montré : ")) 
doigts_b = int(input("Combien de doigts le joueur B a montré : ")) 
somme = doigts_a + doigts_b 
if (somme % 2) == 0:
    print("Le joueur A a gagné")
else:
    print("Le joueur B a gagné")


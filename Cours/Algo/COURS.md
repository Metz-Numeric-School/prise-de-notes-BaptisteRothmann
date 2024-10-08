# Installation et commandes de base de GIT

Créer un dossier « GIT »
clic droit puis « Afficher d’autres options » puis « Open git here » 

  
Récupérer le projet -> « Code » puis copier l’URL 
Dans GIT, taper « git clone (URL) »

git status (voir les modifications faites)
git add .
git commit -a -m " msg " (enregistrer une snapshot)
git push (envoyer les modifications sur la version cloud)

# Qu'est ce que l'algorithmique 

Séquences d'instructions obtenant un résultat

Utilisé en maths (théorèmes, algèbre) / informatique (programmes, scripts etc...) / vie quotidienne (recette de cuisine)

## Représentation 

Logigramme --> chemin menant à un résultat avec des conditions (oui ou non)

## Python 

Variables : un nom (pas de caractères spéciaux, pas d'espace, ne pas commencer par un chiffre) ET une valeur (types de variables)

Exemple : prenom = " John " 
prenom représente la variable
" John " représente une chaîne de caractères (encadrée par des "")
(le = est une déclaration / affectation / initialisation)

#### Noms de variables 

dateJour = "23-09-2024"
anneeNaissance = 1988

#### Conventions de nommage

camelCase : lecture plus facile 
ex : jeSuisResponsableDeFormationAlaMetzNumericSchool

PascalCase

propre à Python : snake_case (ex : birth_year)

kebab-case (non utilisé en programmation, utilisé pour les noms de fichiers ou les URL)

#### Types de données 

Entier (integer / int) de -∞ à +∞
Décimaux (float) de -∞ à +∞ -> ATTENTION, on utilise le "." à la place de "," ex : 3.14
Chaîne de caractères (string / str) ""
Booléen (Boolean / Bool) true / false, 1 / 0

#### Opérations 

Entiers / Décimaux :
	" + " addition
	" - " soustraction
	" * " multiplication 
	" // " division entière
	" / " division
	" ** " puissance

String : 
" + " concaténation 
ex : " Salut " + " Ca va "
		" Salut ca va "

" * " multiplication en PYTHON uniquement 
" A " * 4 = " AAAA "

Bool :
and -> et 
or -> ou
not -> non
--> Opérateurs logiques 

#### Algèbre de Boole


| a   | b   | a ET b |
| --- | --- | ------ |
| F   | F   | F      |
| F   | V   | F      |
| V   | F   | F      |
| V   | V   | V      |

| a   | b   | a ET b |
| --- | --- | ------ |
| 0   | 0   | 0      |
| 0   | 1   | 0      |
| 1   | 0   | 0      |
| 1   | 1   | 1      |

| a   | b   | a OU b |
| --- | --- | ------ |
| F   | F   | F      |
| F   | V   | V      |
| V   | F   | V      |
| V   | V   | V      |

| a   | b   | a OU b |
| --- | --- | ------ |
| 0   | 0   | 0      |
| 0   | 1   | 1      |
| 1   | 0   | 1      |
| 1   | 1   | 1      |

| a   | NON a |
| --- | ----- |
| F   | V     |
| V   | F     |

V et F et F ou V et V et F ou F  = F

Algo 
DEBUT
a = 2 
b = 3
c = 6

a = c + 1  
b = a + b  
c = a - b + 1 
a = b 
c = b * 2 

a = 10
b = 10
c = 20
FIN

DEBUT
a = 7 
b = 5 
c = 2 

a = b * c 
c = a + a 
b = c * 3 - c 
a = a + b + c 
c = a - b + c 

a = 70
b = 40
c = 50
FIN

#### Opérateurs de comparaison 

Ils donnent des résultats booléens :

a == b si a est STRICTEMENT égal à b
a != b si a est DIFFERENT de b 
a > b si a STRICTEMENT supérieur à b
a < b si a STRICTEMENT inférieur à b
a <= b si a est inférieur OU égal à b (a < b or a == b)
a >= b si a est supérieur OU égal à b (a > b or a == b)

if *condition* : 
-> instruction 
(indentation)

ex : 
```python 
light = 1
if light == 1 :
	print("J'ouvre les volets")
else :
	print("Je ferme les volets")
```

```python
first_name = input("Votre nom : ")
if first_name == "John" :
	print("Bonjour")
else : 
	print("Au revoir")
```

#### Boucles

- for (pour)
-> boucle comptée (utilisation d'une variable de comptage)
Elle permet de répéter n fois une ou plusieurs instructions 

for i in range(start, end):
	instruction
la boucle d'arrête lorsque i == end

```python
for i in range(0, 5):
	print("Hello")
```
(incrémentation) i = i + 1

- while (tant que)
-> boucle conditionnelle 
Elle répète l'instruction tant qu'elle est vérifiée 

while c:
	instruction

```python
n = 1
while n != 100:
	print(n)
	n = n + 1
```

mot = "Hello"
mot.lower() ----> "hello"
mot.upper() ----> "HELLO"
h = mot[0] ----> "h"
l = len(mot) ----> 5
d = mot[-1] ----> "o"

jour = "mardi"
message = f"Nous sommes {jour}"

#### Listes

Permet de contenir plusieurs valeurs 
chats = ["bibou", "tartuffe, "frimousse"]
divers = ["a", 12, True, 3.14]
l = [1, 2, 3, 4]
0  1   2  3 (indice)
Pour accéder à la valeur 3 de la liste, il faut utiliser l'indice 2 
ex : 
print(l[2]) # affiche 3 
print(len(l)) # affiche 4 

dernier indice (last index) : len(l) - 1

##### Parcours d'un liste 

```python
fruits = ["pomme", "fraise", "banane"]
for i in range(0, len(fruits))
	print(fruits[i])
```

```python
vegetables = ["aubergine", "brocolis", "haricot"]
for vegetable in vegetables:
	print(vegetable)
```

#### Functions

def somme(a, b) :
	print(f"La somme de {a} + {b} = {a + b}")

somme(5, 2)
somme (3, 3)

--> Procédure

def somme(a, b) :
	return a + b

resultat = somme(5, 2)

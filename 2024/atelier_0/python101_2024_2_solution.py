#####################################################################################
# Thème: Les triplets pythagoriciens
#####################################################################################

# Introduction de base au Input / Output et aux variables.

## Les lignes précédées dièses sont des lignes de commentaires en Python et ne seront pas évaluées
### Vous devriez être généreux dans vos commentaires pour vous aider à réviser votre code

## Exemple: obtenir le rayon de l'usagé du programme et imprimer le diamètre+circonférence
##   et répondre avec une belle phrase réponse
# r= int(input())
r=5
print("Le diamètre est: "+ str(2*r))    #str() transforme le nombre en chaîne de caractère


## Exercice: Obtenir le rayon de l'utilisateur et approximer l'aire du cercle
pi = 3.1416  # à peu près
print(pi*r**2)


#####################################################################################

# Les conditionels

## Exemple: Vérifions si trois nombres (a,b,r) forment un triplet pythagoricien, soit a^2 + b^2 = r^2
a=3
b=4
r=6
if a**2+b**2 == r**2:
    print("triplet pyth")
else:
    print("Oh oh!")

## Exemple: Étant données des coordonées (a,b), imprimez le quadrant dans lequel se trouve le point
a=3
b=-5

if a>0 and b>0:
    print("quadrant 1")
elif a<0 and b>0:
    print("quadrant 2")
elif a<0 and b<0:
    print("quadrant 3")
else:
    print("quadrant 4")


## Exercice: Vérifiez si les coordonnées (a,b) sont à l'intérieur d'un cercle de rayon 6,
    # à l'extérieur d'un cercle de rayon 6, ou sur le périmètre d'un cercle de rayon 6.
a=3
b=5

if a**2+b**2 < 6**2:
    print("a l'intérieur")

### Exercice maison: Imprimez la plus grande valeur entre a,b,c
a, b, c = 1, 3, -7

if a >= b and a >= c:
    print(a)
elif b>=a and b >= c:
    print(b)
else:
    print(c)

    # ou

print(max(a,b,c))

#####################################################################################

# Les boucles

## Boucle While
### Exemple: Trouvons les dimensions de trois triangles rectangles à côtés entiers qui ont une cathète de longueur 12
a=12
b=0
counter=0
r= (a**2+b**2)**0.5
while counter<3:
    b = b+1
    r = (a**2+b**2)**0.5
    if r == int(r):
        counter += 1
        print(f"a: {a}, b: {b}, r: {r}")


## For loop avec range()
### Exemple: Imprimons les 10 premiers carrés parfaits
for i in range(10):
    n = i+1
    print(n**2)


### Exercice: Imprimez les 5 premiers carrés parfaits qui terminent avec un 1.
# x % 10

i=0
counter=0

while counter < 5 :
    i+=1
    i_carre = i**2
    if i_carre % 10 == 1:
        counter += 1
        print(i_carre)


#####################################################################################
print()
print("Les listes")

# Les listes

x = [1,3,6,7,9,10]
y = [4,4,8,5,1,10]

## Exemple: 5 différentes manières de manipuler les éléments d'une liste

# Imprimer la liste de x
print(x)

# Accédez aux éléments par position
x_3 = x[2]  # La variable x_2 prends la 2e valeur de la liste x en comptant à partir de 0
print(x_3)  # x_3 = 6


# Ajoutez des éléments à une liste (calculons les valeurs de r)
coords = []  # une liste vide contenant les valeurs de r
for i in range(6):
    a = x[i]
    b = y[i]
    coord = (a,b)
    coords.append(coord)

print(coord)

coord_3 = coords[3]
print(f"x: {coord_3[0]}, y: {coord_3[1]}")


# vérifier si un élément est dans une liste
coord = (7,5)
if coord in coords:
    print(f"{coord} est dans {coords}")

coord = (1,1)
if coord in coords:
    print(f"{coord} est dans {coords}")
else:
    print(f"{coord} n'est pas dans {coords}")

## Exercice: Pour chaque paire (x[i],y[i]) vérifiez si (x,y,r) forme un triplet pythagoricien
for i in range(6):
    r = (x[i]**2 + y[i]**2)**0.5
    if r == int(r):
        print(f"({x[i]}, {y[i]}, {r}) est un triplet pythagoricien")
    else:
        print(f"({x[i]}, {y[i]}, {r}) n'est pas un triplet pythagoricien")

#####################################################################################

# Approximons PI !!!

## Exemple final: Trouvons tous les points à coordonnées entières dans le carré circonscrit au cercle de rayon r.
r = 200
points_cercle = []

for x in range(-r,r+1):
    for y in range(-r,r+1):
        if x**2+y**2<= r**2:
            points_cercle.append((x,y))


## Calculons le nombre de points.
nb_points_cercle = len(points_cercle)
print(f"Le nombre de points à coordonnées entières dans le cercle: {nb_points_cercle}")



## Exercice: Approximez pi avec un cercle de rayon r.
    # nombre_pts_cercle / nombre_pts_carré ≈ pi/4

nb_cercle = 0
nb_carre = 0

for x in range(-r,r+1):
    for y in range(-r,r+1):
        nb_carre += 1
        if x**2+y**2<= r**2:
            nb_cercle +=1

PI = 4*nb_cercle/nb_carre

print(f"J'approxime PI: {PI}")
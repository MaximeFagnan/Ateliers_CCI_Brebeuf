#####################################################################################
# Thème: Les triplets pythagoriciens
#####################################################################################

# Introduction de base au Input / Output et aux variables.

## Les lignes précédées dièses sont des lignes de commentaires en Python et ne seront pas évaluées
### Vous devriez être généreux dans vos commentaires pour vous aider à réviser votre code

## Exemple: obtenir le rayon de l'usagé du programme et imprimer le diamètre+circonférence
##   et répondre avec une belle phrase réponse



## Exercice: Obtenir le rayon de l'utilisateur et approximer l'aire du cercle
pi = 3.1416  # à peu près



#####################################################################################

# Les conditionels

## Exemple: Vérifions si trois nombres (a,b,r) forment un triplet pythagoricien, soit a^2 + b^2 = r^2



## Exemple: Étant données des coordonées (a,b), imprimez le quadrant dans lequel se trouve le point



## Exercice: Vérifiez si les coordonnées (a,b) sont à l'intérieur d'un cercle de rayon 6,
    # à l'extérieur d'un cercle de rayon 6, ou sur le périmètre d'un cercle de rayon 6.



### Exercice maison: Imprimez la plus grande valeur entre a,b,c

#####################################################################################

# Les boucles

## Boucle While
### Exemple: Trouvons les dimensions de trois triangles rectangles à côtés entiers qui ont une cathète de longueur 12



## For loop avec range()
### Exemple: Imprimons les 10 premiers carrés parfaits



### Exercice: Imprimez les 5 premiers carrés parfaits qui terminent avec un 1.
# x, y = 101,1327
# print(x % 10)
# print(y % 10)




#####################################################################################

# Les listes

x = [1,3,6,7,9,10]
y = [4,4,8,5,1,10]

## Exemple: 5 différentes manières de manipuler les éléments d'une liste

# Imprimer la liste de valeurs de x



# Accédez aux éléments par position



# Ajoutez des éléments à une liste (calculons les valeurs de r)
r = []  # une liste vide contenant les valeurs de r



# vérifier si un élément est dans une liste



## Exercice: Pour chaque paire (x[i],y[i]) vérifiez si (x,y,z) forme un triplet pythagoricien



#####################################################################################

# Approximons PI !!!

## Exemple final: Trouvons tous les points à coordonnées entières dans le carré circonscrit au cercle de rayon r.
r = 4
points = []


## Calculons le nombre de points.



## Exercice: Approximez pi avec un cercle de rayon r.
    # nombre_pts_cercle / nombre_pts_carré ≈ pi/4
#etage(x, y_sol, couleur, niveau)
#x correspond au x du centre de l'étage
#y_sol -> self explanatory
#couleur -> self explanatory
#niveau correspond au nombre d'étage
from fenetre import *
from fenetre_b import *
from facade import *
from turtle import *
from random import randint

def etage(x, y_sol, couleur, niveau):
    facade(x,y_sol*niveau,couleur,niveau)
    xf = x - 57
    for i in range(3):
        r = randint(0,1)
        if r == 1 :
            fenetre(xf+15, y_sol*niveau+60)
        else :
            fenetre_b(xf+15, y_sol*niveau+60)
        xf += 42

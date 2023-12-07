# Fonction rdc(x, y sol, c facade, c porte) :
# x : (int) abscisse du centre
# y sol : ordonn´ee du sol du la rue
# c facade : couleur de la fa¸cade
# c porte : couleur de la porte
from facade import *
from random import *
from porte import *
from fenetre import *
from turtle import *
from couleur_aleatoire import *

def rdc(x,y_sol,c_facade,c_porte):
    facade(x,y_sol,c_facade,0)
    r = randint(0,1)
    p = randint(1,3)
    if p == 1:
        po = -42
    elif p == 2:
        po = 0
    elif p == 3:
        po = 42
    if r == 0:
        porte1(x+po,y_sol,c_porte)
        if po == -42:
            fenetre(x+42,y_sol)
            fenetre(x,y_sol)
        elif po == 42:
            fenetre(x-42,y_sol)
            fenetre(x,y_sol)
        elif po == 0:
            fenetre(x+42,y_sol)
            fenetre(x-42,y_sol)

    else :
        porte2(x+po,y_sol,c_porte)
        if po == -42:
            fenetre(x+42,y_sol)
            fenetre(x,y_sol)
        elif po == 42:
            fenetre(x-42,y_sol)
            fenetre(x,y_sol)
        elif po == 0:
            fenetre(x+42,y_sol)
            fenetre(x-42,y_sol)
    

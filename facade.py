# Fonction facade(x, y sol, couleur, niveau) :
# x : abscisse du centre de la facade
# y sol : ordonn´ee du sol du la rue
# couleur : couleur de la fa¸cade
# niveau : num du niveau (0 pour les rdc, ...)
from turtle import *
from rectangle import rectangle

def facade(x, y_sol, couleur, niveau) :
    colormode(255)
    fillcolor(couleur)
    begin_fill()
    rectangle(x,y_sol+60*niveau,140,60)
    end_fill()

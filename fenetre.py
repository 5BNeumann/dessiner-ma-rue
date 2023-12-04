from rectangle import *
from turtle import *
'''
Paramètres :
    x est l'abcisse du centre de la fenêtre
    y est l'ordonnée du sol du niveau de la fenetre
Remarque:
    dessine une fenetre de 30 pixels sur 30 pixels
'''

def fenetre(x,y):
    up()
    colormode(255)
    fillcolor(196,214,215)
    begin_fill()
    down()
    rectangle(x,y+25,30,30)
    end_fill()

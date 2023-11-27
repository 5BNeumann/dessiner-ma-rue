# Fonction porte(x,y,couleur) :
# x est l’abscisse du centre de la porte
# y est l’ordonn´ee du sol du niveau de la porte
# w est la largeur de la porte
# h est la hauteur de la portefrom turtle import *
from turtle import *
from trait import *

def porte(x,y,w,h,couleur) :
    color("Black")
    fillcolor(couleur)
    begin_fill()
    setheading(90)
    trait(x+w/2,y,x+w/2,y+h,1)
    circle(w/2,180)
    trait(x-w/2,y+h,x-w/2,y,1)
    end_fill()

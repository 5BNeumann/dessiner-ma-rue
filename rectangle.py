# Fonction rectangle(x,y,w,h) :
# x, y : coordonn´ees du centre de la base de rectangle
# w : largeur du rectangle
# h : hauteur du rectangle
from turtle import *
from trait import *

def rectangle(x,y,w,h) :
    up()
    goto(x-w/2,y)
    down()
    trait(x-w/2,y,x+w/2,y,1)
    trait(x+w/2,y,x+w/2,y+h,1)
    trait(x+w/2,y+h,x-w/2,y+h,1)
    trait(x-w/2,y+h,x-w/2,y,1)

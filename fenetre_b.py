#fenetre_b(x, y_sol, niveau)
#x correspond au milieu de la porte-fenêtre-balcon
#y_sol -> self explanatory
#niveau correspond au nombre d'étage
from turtle import *
from trait import *
from rectangle import *

def fenetre_b(x, y_sol, niveau):
    colormode(255)
    fillcolor(196, 214, 215)
    begin_fill()
    rectangle(x,y_sol*niveau,30,50)
    end_fill()
    trait(x-20,y_sol*niveau,x+20,y_sol*niveau,2)
    trait(x-20,y_sol*niveau+30,x+20,y_sol*niveau+30,2)
    xa = x-20
    for i in range(9):
        trait(xa,y_sol*niveau,xa,y_sol*niveau+30,2)
        xa += 5
if __main__ :
    fenetre_b(0,0,0)

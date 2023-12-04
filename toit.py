#toit1(x, y_sol, niveau)
#x correspond au milieu du toit
#y_sol -> self explanatory
#niveau correspond au nombre d'étage
#toit2(x, y_sol, niveau)
#x correspond au milieu du toit
#y_sol -> self explanatory
#niveau correspond au nombre d'étage
from trait import *
from turtle import *

def toit1(x,y_sol,niveau):
    up()
    xd = x - 180
    xf = x + 180
    y = y_sol + (60 * niveau)
    down()
    trait(xd,y,xf,y, 10)
    trait(xd,y,x,(y+40),1)

def toit2(x,y_sol,niveau):
    up()
    xd = x - 180
    xf = x + 180
    y = y_sol + (60 * niveau)
    down()
    trait(xd,y,xf,y, 10)

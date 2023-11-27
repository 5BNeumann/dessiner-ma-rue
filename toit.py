#toit1(x, y_sol, niveau)
#
#
#
#toit2(x, y_sol, niveau)
#
#
#
from trait import *
from turtle import *

def toit2(x,y_sol,niveau):
    up()
    xd = x - 180
    xf = x + 180
    y = y_sol + (60 * niveau)
    trait(xd,y,xf,y, 10)

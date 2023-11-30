# Fonction couleur aleatoire() :
# Cette fonction retourne un triplet de 3 nombres entiers
# compris entre 0 et 255 correspondant `a du RGB
from random import *
R=0
V=0
B=0
def couleur_aleatoire():
    R = randint(0,255)
    V = randint(0,255)
    B = randint(0,255)
    return R,V,B

import pygame
from pygame.locals import *


# Changement de l'image du personnage
walk_left = [pygame.image.load("marche1.jpg"), pygame.image.load("marche4.jpg"), pygame.image.load("marche3.jpg"), pygame.image.load("marche2.jpg")]
walk_right = [pygame.image.load("marche1.jpg"), pygame.image.load("marche2.jpg"), pygame.image.load("marche3.jpg"), pygame.image.load("marche4.jpg")]
hurt = [pygame.image.load("marche1.jpg"), pygame.image.load("blessure.jpg")]
dead = [pygame.image.load("marche1.jpg"), pygame.image.load("mort1.jpg"), pygame.image.load("mort2.jpg"), pygame.image.load("mort3.jpg"), pygame.image.load("mort4.jpg")]
block = [pygame.image.load("marche1.jpg"), pygame.image.load("block.jpg")]
attack = [pygame.image.load("marche1.jpg"), pygame.image.load("attack1.jpg"), pygame.image.load("attack2.jpg")]


# Position inital du personnage
x = 500
y = 550
width = 64
height = 64
vel = 50

def redraw():
    global compteur
    fenetre.blit(fond, (0,0))
    if compteur + 1 >= 57:
        compteur = 0

    # Deplacement à gauche 
    if left:
        fenetre.blit(walk_left[compteur], (x, y))
        compteur += 1
        print("gauche")
        if compteur + 1 >= 4:
            compteur = 0

    # Deplacement à droite
    elif right:
        move = True
        fenetre.blit(walk_right[compteur], (x, y))
        compteur += 1
        print("droit")
        if compteur + 1 >= 4:
            compteur = 0

    elif mort:
        while compteur < 5:
            fenetre.blit(dead[compteur], (x, y))
            pygame.display.update() 
            pygame.display.flip()
            pygame.time.delay(500)
            compteur += 1
            pygame.display.update() 
            pygame.display.flip() 
        compteur = 0


    pygame.display.update() 
    pygame.display.flip() 

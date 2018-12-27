import pygame
import fenetre
from math import *
import sys


walk_left = [pygame.image.load("marche1.jpg"), pygame.image.load("marche4.jpg"), pygame.image.load("marche3.jpg"), pygame.image.load("marche2.jpg")]
walk_right = [pygame.image.load("marche1.jpg"), pygame.image.load("marche2.jpg"), pygame.image.load("marche3.jpg"), pygame.image.load("marche4.jpg")]
hurt = [pygame.image.load("marche1.jpg"), pygame.image.load("blessure.jpg")]
dead = [pygame.image.load("marche1.jpg"), pygame.image.load("mort1.jpg"), pygame.image.load("mort2.jpg"), pygame.image.load("mort3.jpg"), pygame.image.load("mort4.jpg")]
block = [pygame.image.load("marche1.jpg"), pygame.image.load("block.jpg")]
attack = [pygame.image.load("marche1.jpg"), pygame.image.load("attack1.jpg"), pygame.image.load("attack2.jpg")]


class Tools:

    def switch_tool (self, key):
        global compteur
        
        if (key == pygame.gauche):

            # Gestion du déplacement
            x -= vel

            # Blocker le personnage pour qu'il ne sorte pas de la fenêtre
            if x < 0 :
                x = 0

            # Actualiser l'image du personnage
            fenetre.blit(walk_left[compteur], (x, y))
            compteur += 1
            if compteur + 1 >= 4:
                compteur = 0

            print("gauche")

        if (key == pygame.droit):
            
            # Gestion du déplacement
            x += vel

            # Blocker le personnage pour qu'il ne sorte pas de la fenêtre
            if x > 1200 :
                x = 1200
                
            # Actualiser l'image du personnage
            fenetre.blit(walk_right[compteur], (x, y))
            compteur += 1
            if compteur + 1 >= 4:
                compteur = 0

            print("droit")
        

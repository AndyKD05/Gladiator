import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((1080,720))
pygame.display.set_caption('Gladiator')

fond = pygame.image.load("arene.jpg").convert()
fenetre.blit(fond, (0,0))
pygame.display.flip()
       

continuer = 1
while continuer:
        
    for event in pygame.event.get():
                # Arrêt du programme si l'on clique sur la croix de la fenêtre pour la fermer
        if event.type == pygame.QUIT:
            continuer = 0 
        pygame.display.flip()
        
pygame.quit()

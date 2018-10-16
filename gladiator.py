import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Gladiator')

fond = pygame.image.load("arene.jpg").convert()
fenetre.blit(fond, (0,0))

perso = pygame.image.load("marche1.jpg").convert()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)
walk_left = [pygame.image.load("marche1.jpg"), pygame.image.load("marche4.jpg"), pygame.image.load("marche3.jpg"), pygame.image.load("marche2.jpg")]
walk_right = [pygame.image.load("marche1.jpg"), pygame.image.load("marche2.jpg"), pygame.image.load("marche3.jpg"), pygame.image.load("marche4.jpg")]

# clock = pygame.time.clock()

x = 500
y = 425
width = 64
height = 64
vel = 5

left = False
right = False
compteur = 0

pygame.display.flip()

def redraw():
    global compteur
    fenetre.blit(fond, (0,0))
    if compteur + 1 >= 27:
        compteur = 0
    if left:
        fenetre.blit(walk_left[compteur//3], (x, y))
        compteur += 1
    elif right:
        fenetre.blit(walk_right[compteur//3], (x, y))
        compteur += 1
    
    # pygame.draw.rect(fenetre, (255, 0, 0), (x, y, width, height))
    pygame.display.update()     

continuer = 1
while continuer:
    pygame.time.delay(50)
    #clock.tick(27)    
    for event in pygame.event.get():
                # Arrêt du programme si l'on clique sur la croix de la fenêtre pour la fermer
        if event.type == pygame.QUIT:
            continuer = 0 
        
    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_LEFT]:
        x -= vel
        left = True
        right = False
    if keys[pygame.K_RIGHT]:
        x += vel
        left = False
        right = True
    else:
        right = False
        left = False
        compteur = 0
                # position_perso = position_perso.move(0.3)
    # fenetre.blit(fond, (0,0))
    # fenetre.blit(perso, position_perso)
    
    #pygame.display.flip()
    redraw   
pygame.quit()

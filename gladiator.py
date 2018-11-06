import pygame
from pygame.locals import *

# musique
pygame.mixer.init()
pygame.mixer.music.load('musique.mp3') 
pygame.mixer.music.play(loops=-1, start=0.0)

#Personnage 
pygame.init()

fenetre = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Gladiator')

fond = pygame.image.load("arene.jpg").convert()
fenetre.blit(fond, (0,0))

perso = pygame.image.load("marche1.jpg").convert()
position_perso = (500, 550)
fenetre.blit(perso, position_perso)
walk_left = [pygame.image.load("marche1.jpg"), pygame.image.load("marche4.jpg"), pygame.image.load("marche3.jpg"), pygame.image.load("marche2.jpg")]
walk_right = [pygame.image.load("marche1.jpg"), pygame.image.load("marche2.jpg"), pygame.image.load("marche3.jpg"), pygame.image.load("marche4.jpg")]

# clock = pygame.time.clock()

x = 500
y = 550
width = 64
height = 64
vel = 50

left = False
right = False
compteur = 0

pygame.display.flip()

def redraw():
    global compteur
    fenetre.blit(fond, (0,0))
    if compteur + 1 >= 57:
        compteur = 0
    if left:
        fenetre.blit(walk_left[compteur], (x, y))
        compteur += 1
        print("gauche")
        if compteur + 1 >= 4:
            compteur = 0
    elif right:
        move = True
       
        fenetre.blit(walk_right[compteur], (x, y))
        compteur += 1
        print("droit")
        if compteur + 1 >= 4:
            compteur = 0
        if event.type == KEYUP:
            move = False
            print("move")
        pygame.display.update() 
        pygame.display.flip() 

continuer = 1
while continuer:
    pygame.time.delay(50)
    #clock.tick(27)    
    for event in pygame.event.get():
                # Arrêt du programme si l'on clique sur la croix de la fenêtre pour la fermer
        if event.type == pygame.QUIT:
            continuer = 0 
        
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                tmp = x
                x -= vel
                if x < 0:
                    x = 0
                left = True
                right = False
                redraw()
                
                # ///////////////////////////////////////
                # pygame.draw.rect(fenetre, (255, 0, 0), (x, y, width, height)s
                #////////////////////////////////////////
            elif event.key == K_RIGHT:
                tmp = x
                x += vel
                if x > 1200:
                    x = 1200
                left = False
                right = True
                redraw() 
            else:
                right = False
                left = False
                compteur = 0
                
        pygame.display.flip()
                # position_perso = position_perso.move(0.3)
    # fenetre.blit(fond, (0,0))
    # fenetre.blit(perso, position_perso)
    
    #pygame.display.flip()
    
pygame.quit()

import pygame, sys
import move
from pygame.locals import *

# musique
pygame.mixer.init()
pygame.mixer.music.load('musique.mp3') 
pygame.mixer.music.play(loops=-1, start=0.0)

pygame.init()

fenetre = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Gladiator')

fond = pygame.image.load("arene.jpg").convert()
fenetre.blit(fond, (0,0))
fenetre.blit(pygame.image.load("score.png"), (0,0))
fenetre.blit(pygame.image.load("coeur.png"), (20,465))
pygame.draw.rect(fenetre, (255, 0, 0), (20, 200, 40, 250))
pygame.draw.rect(fenetre, (0, 0, 0), (20, 200, 40, 250), 3)

perso = pygame.image.load("marche1.jpg").convert_alpha()
position_perso = (250, 525)

fenetre.blit(perso, position_perso)


walk_left = [pygame.image.load("marche1.jpg"), pygame.image.load("marche4.jpg"), pygame.image.load("marche3.jpg"), pygame.image.load("marche2.jpg")]
walk_right = [pygame.image.load("marche1.jpg"), pygame.image.load("marche2.jpg"), pygame.image.load("marche3.jpg"), pygame.image.load("marche4.jpg")]
hurt = pygame.image.load("blessure.jpg")
dead = [pygame.image.load("mort1.jpg"), pygame.image.load("mort2.jpg"), pygame.image.load("mort3.jpg"), pygame.image.load("mort4.jpg")]
block = pygame.image.load("block.jpg")
attack = [pygame.image.load("attack1.jpg"), pygame.image.load("attack2.jpg")]
jump = [pygame.image.load("marche1.jpg"), pygame.image.load("jump1.jpg"), pygame.image.load("jump2.jpg"), pygame.image.load("jump3.jpg")]

clock = pygame.time.Clock()

x = 250
y = 525
width = 40
height = 250
vel = 50
a = 200

left = False
right = False
mort = False
defense = False
offens = False
Jump = False
bless = False
jumpCount = 12
compteur = 0

pygame.display.flip()

def redraw():
    global compteur
    fenetre.blit(fond, (0,0))
    if compteur + 1 >= 57:
        compteur = 0

    # Deplacement à gauche 
    if left:
        fenetre.blit(pygame.image.load("score.png"), (0,0))
        fenetre.blit(pygame.image.load("coeur.png"), (20,465))
        pygame.draw.rect(fenetre, (255, 0, 0), (20, 200, width, height))
        pygame.draw.rect(fenetre, (0, 0, 0), (20, 200, 40, 250), 3)
        
        fenetre.blit(walk_left[compteur], (x, y))
        compteur += 1
        print("gauche")
        if compteur + 1 >= 4:
            compteur = 0

    # Deplacement à droite
    elif right:
        fenetre.blit(pygame.image.load("score.png"), (0,0))
        fenetre.blit(pygame.image.load("coeur.png"), (20,465))
        pygame.draw.rect(fenetre, (255, 0, 0), (20, 200, width, height))
        pygame.draw.rect(fenetre, (0, 0, 0), (20, 200, 40, 250), 3)
        
        fenetre.blit(walk_right[compteur], (x, y))
        compteur += 1
        print("droit")
        if compteur + 1 >= 4:
            compteur = 0

    # Saut du personnage
    elif Jump:
        fenetre.blit(jump[compteur], (x, y))
        compteur += 1
        print("saut")
        if compteur + 1 >= 4:
            compteur = 0

    # Attaque du personnage
    elif offens:
        while compteur < 2:
            pygame.time.delay(50)
            fenetre.blit(attack[compteur], (x, y))
            pygame.display.update() 
            pygame.display.flip()
            pygame.time.delay(500)
            compteur += 1
        #pygame.display.flip() 
        #fenetre.blit(perso, (x, y))
        compteur = 0

    # Position défensie du personnage
    elif defense:
        fenetre.blit(block, (x, y))
        pygame.time.delay(500)
        fenetre.blit(perso, (x, y))

    #Personnage touché
    elif bless:

        fenetre.blit(pygame.image.load("score.png"), (0,0))
        fenetre.blit(pygame.image.load("coeur.png"), (20,465))
        pygame.draw.rect(fenetre, (255, 0, 0), (20, a, width, height))
        pygame.draw.rect(fenetre, (0, 0, 0), (20, 200, 40, 250), 3)
        
        fenetre.blit(hurt, ((x), y))
        pygame.time.delay(500)

        
    elif mort:
        while compteur < 4:
            fenetre.blit(dead[compteur], (x, y))
            #pygame.display.update() 
            pygame.display.flip()
            pygame.time.delay(350)
            compteur += 1
           
        compteur = 0


    pygame.display.update() 
    pygame.display.flip() 

continuer = 1
while continuer:
    clock.tick(50)
    fenetre.blit(pygame.image.load("score.png"), (0,0))
    fenetre.blit(pygame.image.load("coeur.png"), (20,465))
    pygame.draw.rect(fenetre, (255, 0, 0), (20, 200, width, height))
    pygame.draw.rect(fenetre, (0, 0, 0), (20, 200, 40, 250), 3)
    
    for event in pygame.event.get():
        

        # Arrêt du programme si l'on clique sur la croix de la fenêtre pour la fermer
        if event.type == pygame.QUIT:
            continuer = 0 
        
        if event.type == KEYDOWN:
            
            # Deplacement vers la gauche
            if event.key == K_LEFT:
                
                x -= vel
                if x < 0:
                    x = 0
                left = True
                redraw()
                left = False

            # Deplacement vers la droite
            elif event.key == K_RIGHT:
                tmp = x
                x += vel
                if x > 1200:
                    x = 1200
                right = True
                redraw()
                right = False

            # Saut du personage
            elif event.key == K_UP:
                if jumpCount >= -10:
                    neg = 1
                if jumpCount < 0:
                    neg = -1
                if y <= 550:
                    y -= (jumpCount ** 2) * 0.5 * neg
                else:
                    y = 0
                jumpCount -= 2
                Jump = True
                redraw()
                Jump = False

            # Attack du personnage    
            elif event.key == K_SPACE:
                offens = True
                redraw()
                offens = False

            # Position de défense du personnage
            elif event.key == K_d:
                defense = True
                redraw()
                defense = False

            # Blessure du personnage
            elif event.key == K_b:
                bless = True
                if height > 0:
                    height = height - 25
                redraw()
                bless = False
                
                
                

            # Simulation de la mort
            elif event.key == K_DOWN:
                mort = True
                x = x - 8
                redraw()
                mort = False

                

            
            else:
                right = False
                left = False
                mort = False
                compteur = 0
        
        pygame.display.flip()
    
pygame.quit()

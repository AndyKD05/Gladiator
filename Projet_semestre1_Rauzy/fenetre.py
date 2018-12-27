import pygame

# musique
pygame.mixer.init()
pygame.mixer.music.load('musique.mp3') 
pygame.mixer.music.play(loops=-1, start=0.0)

pygame.init()

ring = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Gladiator')

fond = pygame.image.load("arene.jpg").convert()
fenetre.blit(fond, (0,0))

pygame.display.flip()


continuer = 1
while continuer:
    pygame.time.delay(50)
    for event in pygame.event.get():

        # Arrêt du programme si l'on clique sur la croix de la fenêtre pour la fermer
        if event.type == pygame.QUIT:
            continuer = 0 

    pygame.display.flip()

pygame.quit()

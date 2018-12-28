import pygame
from pygame.locals import *
pygame.init()

# musique
#pygame.mixer.init()
#pygame.mixer.music.load('musique.mp3') 
#pygame.mixer.music.play(loops=-1, start=0.0)

ecran = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Gladiator")

walkLeft = [pygame.image.load("gauche1.jpg"), pygame.image.load("gauche2.jpg"), pygame.image.load("gauche3.jpg")]
walkRight = [pygame.image.load("droite1.jpg"), pygame.image.load("droite2.jpg"), pygame.image.load("droite3.jpg")]
fond = pygame.image.load("arene.jpg")
char = pygame.image.load("face.jpg")

clock = pygame.time.Clock()

score = 0

tour = 1

pause = False

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.X = 40
        self.Y = 250
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.face = True
        self.hitbox = (self.x , self.y +20, 80, 130)
        self.pause = False

    def draw(self, ecran):
        
        ecran.blit(pygame.image.load("coeur.png"), (20,465))
        pygame.draw.rect(ecran, (255, 0, 0), (20, 200, self.X, self.Y))
        pygame.draw.rect(ecran, (0, 0, 0), (20, 200, 40, 250), 3)
        
        if self.walkCount + 1 >= 9:
            self.walkCount = 0
            
        if not(self.face):
            if self.left:
                ecran.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
                
            elif self.right:
                ecran.blit(walkRight[self.walkCount//3], (self.x, self.y)) 
                self.walkCount += 1
                
        else:
             if self.right:
                 ecran.blit(walkRight[0], (self.x,self.y))
                 
             else:
                 ecran.blit(walkLeft[0], (self.x,self.y))

                 
        self.hitbox = (self.x , self.y +20 , 80, 130)

        
    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 1100
        self.y = 525
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        self.dommage = 4
        self.tour = tour
        self.dommage = self.tour + 5
        text = font1.render('-' + str(self.dommage), 1, (255,0,0))
        ecran.blit(text,(650 - (text.get_width()/2),245))
        pygame.display.update()
        i = 0

        if self.Y > 25:
            self.Y -= 25
        elif self.Y == 25:
            self.Y -= 20
        else:
            self.pause = True
            
            
        
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
                    


class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, ecran):
        pygame.draw.circle(ecran, self.color, (self.x,self.y), self.radius)


#enemy
class enemy(object):
    walkRight =[pygame.image.load("R1E.jpg"), pygame.image.load("R2E.jpg"), pygame.image.load("R3E.jpg"), pygame.image.load("R4E.jpg"), pygame.image.load("R5E.jpg"), pygame.image.load("R6E.jpg")]
    walkLeft = [pygame.image.load("L1E.jpg"), pygame.image.load("L2E.jpg"), pygame.image.load("L3E.jpg"), pygame.image.load("L4E.jpg"), pygame.image.load("L5E.jpg"), pygame.image.load("L6E.jpg")]
              
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x , self.y, 121, 55)
        self.vie = 10
        self.visible = True
        self.tour = tour

    def draw(self, ecran):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0
                
            if self.vel > 0:
                ecran.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            else:
                ecran.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            pygame.draw.rect(ecran, (255,0,0), (self.hitbox[0], self.hitbox[2] +450, 120, 10))
            pygame.draw.rect(ecran, (0,255,0), (self.hitbox[0], self.hitbox[2] +450, 120 - (12 * (10 - self.vie)), 10))
            self.hitbox = (self.x , self.y , 121, 55)
            #pygame.draw.rect(ecran, (255,0,0), self.hitbox,2)
    

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.vie > 0:
            self.vie -= 1
        else:
            self.visible = False
            self.vie = 10
        print('hit')
        

def redrawGameWindow():
    ecran.blit(fond, (0,0))
    text = font.render('Score:' + str(score), 1,(0,0,0,))
    Text = font.render('ROUND ' + str(tour), 1, (255, 0, 0))
    ecran.blit(Text, (550, 150))
    ecran.blit(text, (1100, 10))
    
    man.draw(ecran)
    for bullet in bullets:
        bullet.draw(ecran)
    tigre.draw(ecran)
    pygame.display.update()


    
#boucle principale
font = pygame.font.SysFont('comicsans', 50, True)
man = player(250, 525, 40, 250)
bullets =[]
tigre = enemy(1, 615, 107, 52, 1200)
run = True
while run:
    clock.tick(27)
    
    if tigre.visible == True:
        if man.hitbox[1] < tigre.hitbox[1] + tigre.hitbox[3] and man.hitbox[1] + man.hitbox[3] > tigre.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > tigre.hitbox [0] and man.hitbox [0] < tigre.hitbox[0] + tigre.hitbox[2]:    
                man.hit()
                score -= (tour + 5)
                if man.pause == True:
                    continuer = 1
                    while continuer:
                        man.Y = 250
                        man.x = 250
                        man.y = 525
                        tigre.y = 615
                        tigre.x = 1
                        score = 0
                        tour = 1
                        if keys[pygame.K_SPACE]:
                            continuer = 0
                        





                    
    if tigre.visible == False:
        tour += 1
        pygame.time.delay(5000)
        tigre.visible = True
                
                
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    for bullet in bullets:
        if bullet.y - bullet.radius < tigre.hitbox[1] + tigre.hitbox[3] and bullet.y + bullet.radius > tigre.hitbox[1]:
            if bullet.x + bullet.radius > tigre.hitbox [0] and bullet.x - bullet.radius < tigre.hitbox[0] + tigre.hitbox[2]:    
                tigre.hit()
                score += 1
                bullets.pop(bullets.index(bullet))
        if bullet.x < 1280 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 1:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

    
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.face = False
    elif keys[pygame.K_RIGHT] and man.x < 1280 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.face = False
    else:
        man.face = True
        man.walkCount = 0
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
             neg = 1
             if man.jumpCount < 0:
                neg = -1
             man.y -= (man.jumpCount ** 2) * 0.5 * neg
             man.jumpCount -= 1
        else:
                man.isJump = False
                man.jumpCount = 10
             
    redrawGameWindow()
        
         




            
pygame.quit()

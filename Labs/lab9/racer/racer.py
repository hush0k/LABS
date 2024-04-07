#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0
COIN_SPEED = 5
background_y = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(15, SCREEN_WIDTH - 15), 0)
    
    def move(self):
        global COIN_SCORE
        self.rect.move_ip(0, COIN_SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(15, SCREEN_WIDTH - 15), 0)


class Big_Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Coin.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(15, SCREEN_WIDTH - 15), 0)
    
    def move(self):
        global COIN_SCORE
        self.rect.move_ip(0, COIN_SPEED)
        if (self.rect.top > 2000):
            self.rect.top = 0
            self.rect.center = (random.randint(15, SCREEN_WIDTH - 15), 0)
    

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -SPEED)
        if self.rect.bottom < SCREEN_HEIGHT:        
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0,SPEED)
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-SPEED, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(SPEED, 0)
    


        
                  
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()
C2 = Big_Coin()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(C2)
coin = pygame.sprite.Group()
coin.add(C1)
big_coin = pygame.sprite.Group()
big_coin.add(C2)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:
      
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED and SPEED<=10:
              SPEED += 0.2     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    
    #Background scrolling
    background_y += SPEED - 2
    if background_y > 600:
        background_y = 0
    DISPLAYSURF.blit(background, (0,background_y))
    DISPLAYSURF.blit(background, (0,background_y-600))
        
    scores = font_small.render("Cars: " +str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    coin_score = font_small.render("Coins: "+str(COIN_SCORE), True, BLACK)
    speed = font_small.render("Speed: "+str(int(SPEED)), True, BLACK)
    DISPLAYSURF.blit(speed, (10, 60))
    DISPLAYSURF.blit(coin_score, (10, 35))  
    


    

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

        
    #Coin collision
    if pygame.sprite.spritecollideany(P1, coin):
        pygame.mixer.Sound('catch.mp3').play()
        COIN_SCORE += 1
        #BOOST OF SPEED
        if COIN_SCORE % 20 == 0 and SPEED > 10:
            SPEED += 2
        C1.rect.center = (random.randint(15, SCREEN_WIDTH - 15), -400)
    
    
    #Big Coin collision
    if pygame.sprite.spritecollideany(P1, big_coin):
        pygame.mixer.Sound('catch.mp3').play()
        COIN_SCORE += 3
        #BOOST OF SPEED
        if COIN_SCORE % 20 == 0 and SPEED > 10: 
            SPEED += 2
        C2.rect.center = (random.randint(15, SCREEN_WIDTH - 15), -1900)
        


        
          

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)
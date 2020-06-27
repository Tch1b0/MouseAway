import pygame
import sys

pygame.font.init()
pygame.init()                  
pygame.display.set_caption('MouseAway')                
screen = pygame.display.set_mode([600,600])
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 36)

RED = (200,0,0)
BLACK = (0,0,0)
BLUE = (0,0,250)

pos = [100,100]

Game = False
Start = True
Dead = False

Menuframes = 0
Level = 1
rawCounter = 0
counter = 10
speed = 2


def drawPlayer(mouse):
    pygame.draw.circle(screen, BLUE, mouse, 10)
    x = mouse[0]
    y = mouse[1]
    return x,y

def CheckHit():
    hitboxP = pygame.draw.circle(screen, BLUE, mouse, 10)
    hitboxE = pygame.draw.circle(screen, RED, pos, 20)
    if hitboxP.colliderect(hitboxE):
        Dead = True

def EnemyMovement(mouse,speed):       
    pygame.draw.circle(screen, RED, pos, 20)
    if pos[0] > mouse[0]:
        pos[0] -= speed
    if pos[0] < mouse[0]:
        pos[0] += speed
    if pos[1] > mouse[1]:
        pos[1] -= speed
    if pos[1] < mouse[1]:
        pos[1] += speed

def DisplayLevel():
    text_surface = font.render(('Level '+str(Level)), False, (255, 255, 255))
    screen.blit(text_surface, dest=(225,0))

def IfDead2():
    screen.fill((BLACK))
    text_surface = font.render(("You Died on Level "+str(Level)), False, (255, 255, 255))
    screen.blit(text_surface, dest=(200,250))


#mainloop
while Start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill((BLACK))

    counter = 10
    Menuframes = 0
    speed += 1
    Menu = True
    
    pygame.display.update()
    clock.tick(60)
    #second loop
    while Menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        
        pressed = pygame.key.get_pressed()
        text_surface = font.render(("Level ")+(str(Level)), False, (255, 255, 255))
        screen.blit(text_surface, dest=(235,200))

        text_surface = font.render(("Press space to continue"), False, (255, 255, 255))
        screen.blit(text_surface, dest=(100,400))

        if pressed[pygame.K_SPACE]:
            Game = True
        if Menuframes == 0:
            pygame.display.update()
            Menuframes = 1

        #third loop
        while Game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            screen.fill((BLACK))
            mouse = pygame.mouse.get_pos()
            x = mouse[0]
            y = mouse[1]
            drawPlayer(mouse)
            EnemyMovement(mouse,speed)
            CheckHit()
            DisplayLevel()

            # Timer
            rawCounter += 1
            if rawCounter >= 60: 
                counter -= 1
                rawCounter = 0
            text_surface = font.render((str(counter)), False, (255, 255, 255))
            screen.blit(text_surface, dest=(275,550))

                
            if counter == 0:
                Level += 1
                Game = False
                Menu = False
            #Timer
            while Dead:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: sys.exit()
                    screen.fill((BLACK))
                    text_surface = font.render(("You Died on Level "+str(Level)), False, (255, 255, 255))
                    screen.blit(text_surface, dest=(200,250))
                    pygame.display.update()
                    clock.tick(60)
            pygame.display.update()
            clock.tick(60)
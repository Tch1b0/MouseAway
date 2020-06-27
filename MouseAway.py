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

Menuframes = 0
Level = 1
rawCounter = 0
counter = 20
speed = 1
fps = 0




def drawPlayer(mouse):
    pygame.draw.circle(screen, BLUE, mouse, 10)
    x = mouse[0]
    y = mouse[1]
    return x,y

def CheckHit(x,y):
    hitboxUpLeft = [x-20,y-20]
    hitboxUpRight = [x+20,y-20]
    hitboxDownLeft = [x-20,y+20]
    hitboxDownRight = [x+20,y+20]
    if pos[0] > hitboxUpLeft[0] and pos[0] < hitboxUpRight[0] and pos[1] == hitboxUpRight[1]:
        quit()
    if pos[0] == hitboxUpLeft[0] and pos[1] > hitboxUpLeft[1] and pos[1] < hitboxDownLeft[1]:
        quit()
    if pos[0] > hitboxDownLeft[0] and pos[0] < hitboxDownRight[0] and pos[1] == hitboxDownRight[1]:
        quit()
    if pos[0] == hitboxUpLeft[0] and pos[1] > hitboxUpRight[1] and pos[1] < hitboxDownRight[1]:
       quit()
    if pos == mouse:
        quit()


class Enemy():
    def __init__(self,mouse,speed):       
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

    counter = 20
    Menuframes = 0
    fps += 120
    Menu = True
    
    pygame.display.update()
    clock.tick(fps)
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
            Enemy(mouse,speed)
            CheckHit(x,y)
            DisplayLevel()

            # Timer
            rawCounter += 1
            if rawCounter >= fps:
                counter -= 1
            text_surface = font.render((str(counter)), False, (255, 255, 255))
            screen.blit(text_surface, dest=(275,550))
            if rawCounter >= fps:
                rawCounter = 0
            if counter == 0:
                Level += 1
                Game = False
                Menu = False
            #Timer

            if CheckHit(x,y):
                counter = 0
            pygame.display.update()
            clock.tick(fps)
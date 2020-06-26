import pygame
import sys

pygame.init()                  
pygame.display.set_caption('MouseAway')                
screen = pygame.display.set_mode([600,600])
clock = pygame.time.Clock()

RED = (200,0,0)
BLACK = (0,0,0)
BLUE = (0,0,250)

pos = [100,100]

class Player():
    def __init__(self,mouse):
        pygame.draw.circle(screen, BLUE, mouse, 10)
        self.x = mouse[0]
        self.y = mouse[1]
        self.hitbox = (self.x + 1, self.y + 11, 29, 52)

class Enemy():
    def __init__(self,mouse):       
        pygame.draw.circle(screen, RED, pos, 20)
        speed = 2
        if pos[0] > mouse[0]:
            pos[0] -= speed
        if pos[0] < mouse[0]:
            pos[0] += speed
        if pos[1] > mouse[1]:
            pos[1] -= speed
        if pos[1] < mouse[1]:
            pos[1] += speed



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill((BLACK))
    mouse = pygame.mouse.get_pos()
    P = Player(mouse)
    E = Enemy(mouse)
    Player(mouse)
    Enemy(mouse)

    if pos == P.hitbox:
        quit()



    pygame.display.update()
    clock.tick(60)
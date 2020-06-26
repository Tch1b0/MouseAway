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
speed = 2

class Player():
    def __init__(self,mouse):
        pygame.draw.circle(screen, BLUE, mouse, 10)
        self.x = mouse[0]
        self.y = mouse[1]

    def CheckHit(self):
        hitboxUpLeft = [self.x-10,self.y-10]
        hitboxUpRight = [self.x+10,self.y-10]
        hitboxDownLeft = [self.x-10,self.y+10]
        hitboxDownRight = [self.x+10,self.y+10]
        if pos[0] > hitboxUpLeft[0] and pos[0] < hitboxUpRight[0] and pos[1] == hitboxUpRight[1]:
            quit()
        if pos[0] == hitboxUpLeft[0] and pos[1] > hitboxUpLeft[1] and pos[1] < hitboxDownLeft[1]:
            quit()
        if pos[0] > hitboxDownLeft[0] and pos[0] < hitboxDownRight[0] and pos[1] == hitboxDownRight[1]:
            quit()
        if pos[0] == hitboxUpLeft[0] and pos[1] > hitboxUpRight[1] and pos[1] < hitboxDownRight[1]:
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


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill((BLACK))
    mouse = pygame.mouse.get_pos()
    P = Player(mouse)
    E = Enemy(mouse,speed)
    Player(mouse)
    Enemy(mouse,speed)
    P.CheckHit()

    pygame.display.update()
    clock.tick(60)
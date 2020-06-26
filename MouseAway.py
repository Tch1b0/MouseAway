import pygame
import sys

pygame.init()                  
pygame.display.set_caption('MouseAway')                
screen = pygame.display.set_mode([600,600])
clock = pygame.time.Clock()

RED = (200,0,0)
BLACK = (0,0,0)
BLUE = (0,0,200)

pos = [100,100]

def Enemy():
    pygame.draw.circle(screen, RED, pos, 20)
    speed = 3
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
    pygame.draw.circle(screen, BLUE, mouse, 10)

    if pos[0] == mouse[0] and pos[1] == mouse[1]:
        quit()

    Enemy()

    pygame.display.update()
    clock.tick(60)
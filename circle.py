import pygame
pygame.init()
screen = pygame.display.set_mode((540,230))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.circle(screen,(0,255,0),(200,150),50) 
    pygame.draw.circle(screen,(0,255,0),(100,100),50,3)
    pygame.display.flip()
    

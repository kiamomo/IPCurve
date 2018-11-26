import pygame
import math
pygame.init()

win = pygame.display.set_mode((400,400))

pygame.display.set_caption("IPCurve")

print(math.cos(math.pi))
xStart = 200
yStart = 200

xEnd = 200
yEnd = 195


speed = 5



run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pygame.draw.line(win, (255, 0, 0), (xStart, yStart), (xEnd, yEnd), 3)
        xStart = xEnd
        yStart = yStart-speed
        xEnd = xEnd
        yEnd = yEnd-speed


    if keys[pygame.K_LEFT]:

        pass


    if keys[pygame.K_RIGHT]:
        pass



    pygame.display.update()

pygame.quit()
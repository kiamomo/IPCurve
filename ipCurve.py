import pygame
import math
import random

pygame.init()

pygame.display.set_caption("IPCurve")
basicfont = pygame.font.SysFont(None, 48)

height = 800
width = 800

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

winkel = 0
radius = 20

speed = 45 #niedriger ist schneller
size = 5

zufall1 = random.randint(20, height-20)
zufall2 = random.randint(20, width-20)

print(zufall1,zufall2)
win = pygame.display.set_mode((height,width))


xStart = zufall2
yStart = zufall1

xEnd = zufall2
yEnd = zufall1-size


run = True


while run:
    pygame.time.delay(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    keys = pygame.key.get_pressed()


    pygame.draw.line(win, red, (xStart, yStart), (xEnd, yEnd), size)
    xStart = xEnd-(size*math.sin(winkel))
    yStart = yStart-(size*math.cos(winkel))
    xEnd = xEnd-(size*math.sin(winkel))
    yEnd = yEnd-(size*math.cos(winkel))


    if keys[pygame.K_LEFT]:
        winkel = winkel + math.pi / radius



    if keys[pygame.K_RIGHT]:
        winkel = winkel - math.pi / radius

    if xEnd > width or xEnd < 0 or yEnd > height or yEnd < 0:
        text = basicfont.render('You lost!', True, (255, 0, 0), (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = win.get_rect().centerx
        textrect.centery = win.get_rect().centery
        win.fill((255, 255, 255))
        win.blit(text, textrect)



    pygame.display.update()

pygame.quit()
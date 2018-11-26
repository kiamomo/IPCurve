import pygame
import math
import random

pygame.init()

pygame.display.set_caption("IPCurve")
basicfont = pygame.font.SysFont(None, 48)

height = 800
width = 800

white = (255,255,255) #defining colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

winkel = 0
radius = 20

speed = 45 #niedriger ist schneller
size = 5

zufall1 = random.randint(20, height-20) #I need two random numbers for the x and y coordinate
zufall2 = random.randint(20, width-20)


win = pygame.display.set_mode((height,width))

xStart = zufall2
yStart = zufall1

xEnd = zufall2
yEnd = zufall1-size #A: we need to subttract the same value here as we do at the other point A (currently line 51)


run = True


while run:
    pygame.time.delay(speed) #with this parameter you essentially control how often the game runs the loop, therefore you control the speed of the drawing
    for event in pygame.event.get(): #for being able to close the game with the x in the top right corner
        if event.type == pygame.QUIT:
            run = False



    keys = pygame.key.get_pressed()

    #pygame.draw.line draws a line on our surface with chosen color(defined up top) from a start to an end position.
    pygame.draw.line(win, red, (xStart, yStart), (xEnd, yEnd), size) #A: here we need to put the same amount in size as we do in the other A (currently line 34),
    xStart = xEnd-(size*math.sin(winkel))                            # this way we ensure its a square that gets drawn from pygame. If you dont habe equal values here
    yStart = yStart-(size*math.cos(winkel))                          # you end up with a weird looking sideways movement.
    xEnd = xEnd-(size*math.sin(winkel))
    yEnd = yEnd-(size*math.cos(winkel))                              # https://imgur.com/ErTLFns You control with sin and cos how much we move in each (x,y) direction


    if keys[pygame.K_LEFT]:
        winkel = winkel + math.pi / radius       #Here we are able to control in which direction we draw a new square
                                                 #radius controls the slized of pi you add or subtract from our sin,cos function up top
    if keys[pygame.K_RIGHT]:
        winkel = winkel - math.pi / radius

    if xEnd > width or xEnd < 0 or yEnd > height or yEnd < 0:                       #checks if we hit the the edge of our screen
        text = basicfont.render('You lost!', True, (255, 0, 0), (255, 255, 255))        #random piece of code i found online to display text
        textrect = text.get_rect()
        textrect.centerx = win.get_rect().centerx
        textrect.centery = win.get_rect().centery
        win.fill((255, 255, 255))
        win.blit(text, textrect)



    pygame.display.update()

pygame.quit()
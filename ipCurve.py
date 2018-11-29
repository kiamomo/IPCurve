import pygame
import math
import random
import numpy

pygame.init()

pygame.display.set_caption("IPCurve")
basicfont = pygame.font.SysFont(None, 48)

height = 800
width = 800

# defining colors
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# the amount of times we divide pi, to get more or less slices
radius = 20

# niedriger ist schneller, 45 is best
gameSpeed = 45
size = 5
# size and speed need to be the same to draw a nice looking line
speed = size

# I need two random numbers for the x and y coordinate
zufall1 = random.randint(80, height-80)
zufall2 = random.randint(80, width-80)

# For the start angle
zufall3 = random.randint(0, 7)
winkel = zufall3

win = pygame.display.set_mode((height,width))

xStart = zufall2
yStart = zufall1
xEnd = zufall2
yEnd = zufall1-speed


#A: we need to subttract the same value here as we do at the other point A (currently line 51)







'''
# Didnt work. Ich erkenne eine collision direkt am start :D
# creates a matrix with (zeilen, spalten), to store were our little worm has been
collision = numpy.zeros((height, width), dtype=float)



a=1
b=1
c=1
d=1

#to add to the matrix you type
collision[a,b] = 1
#Zeile 1, Spalte 1 ist nun = 1
print(collision)
'''





run = True
draw = True

while run:
    pygame.time.delay(gameSpeed)
    # with this parameter you essentially control how often the game runs the loop, therefore you control the speed of the drawing
    # for being able to close the game with the x in the top right corner
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    keys = pygame.key.get_pressed()


    if draw:
        pygame.draw.line(win, red, (xStart, yStart), (xEnd, yEnd), size)
        # A: here we need to put the same amount in size as we do in the other A (currently line 34),
        # this way we ensure its a square that gets drawn from pygame. If you dont have equal values here
        # you end up with a weird looking sideways movement.
        xStart = xStart-(speed*math.sin(winkel))
        yStart = yStart-(speed*math.cos(winkel))
        xEnd = xEnd-(speed*math.sin(winkel))
        yEnd = yEnd-(speed*math.cos(winkel))
        # https://imgur.com/ErTLFns You control with sin and cos how much we move in each (x,y) direction
        # pygame.draw.line draws a line on our surface with chosen color(defined up top) from a start to an end position.

        '''
        xStart = int(xStart)
        yStart = int(yStart)
        xEnd = int(xEnd)
        yEnd = int(yEnd)

        a = xStart+5*math.sin(winkel)
        b = yStart+5*math.cos(winkel)
        c = xEnd+5*math.sin(winkel)
        d = yEnd+5*math.cos(winkel)

        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        
        '''

    '''
    print(xStart, yStart)
    print(xEnd, yEnd)
    print(a,b)
    
    
    collision[c,d] = 1

    if collision[c, d] == 1:
        draw = False

    '''










# Here we are able to control in which direction we draw a new square
    # radius controls the slized of pi you add or subtract from our sin,cos function up top
    if keys[pygame.K_LEFT]:
        winkel = winkel + math.pi / radius

    if keys[pygame.K_RIGHT]:
        winkel = winkel - math.pi / radius

    if xEnd > width or xEnd < 0 or yEnd > height or yEnd < 0:
        # checks if we hit the the edge of our screen
        # random piece of code i found online to display text
        text = basicfont.render('You lost!', True, (255, 0, 0), (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = win.get_rect().centerx
        textrect.centery = win.get_rect().centery
        win.fill((255, 255, 255))
        win.blit(text, textrect)
        draw = False



    pygame.display.update()

pygame.quit()
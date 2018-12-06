import pygame
import math
import random

pygame.init()
pygame.display.set_caption("IPCurve")
basicfont = pygame.font.SysFont(None, 48)


class Player:
    # defining colors
    __colors = {
        "pink": (255, 0, 255),
        "white": (255, 255, 255),
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255)
    }

    def __init__(self, name="", color="red", left=0, right=0):
        self.name = name
        self.color = self.__colors[color]
        self.left = left
        self.right = right

        self.setInitialPosition()

        self.score = 0
        # the amount of times we divide pi, to get more or less slices
        self.radius = 20


    def setInitialPosition(self, height=800, width=800, speed=5):
        x1 = random.randint(80, width - 80)
        y1 = random.randint(80, height - 80)
        x2 = x1
        y2 = y1 - speed
        winkel = random.randint(0, 7)
        self.position = [x1, y1, x2, y2, winkel]

    def setPosition(self, x1, y1, x2, y2, winkel):
        self.position = [x1, y1, x2, y2, winkel]

    def getPosition(self):
        return self.position

    def setColor(self, color):
        self.color = color

    def setRadius(self, radius):
        self.radius = radius

    def setName(self, name):
        self.name = name

    def setColor(self, color):
        self.color = color





class Game:

    def __init__(self, height: int = 800, width: int = 800) -> object:
        self.height = 800
        self.width = 800
        # niedriger ist schneller, 45 is best
        self.gameSpeed = 45
        self.win = pygame.display.set_mode((height, width))
        self.players = []
        self.pastPositions = []
        # size and speed need to be the same to draw a nice looking line
        self.size = 5
        self.speed = self.size



    def addPlayer(self, name="", color="", left=0, right=0):
        player = Player(name=name, color=color, left=left, right=right)
        self.players.append(player)

    def getPlayer(self):
        print(self.players)

    def setHeight(self, height):
        self.height = height

    def setWidth(self, width):
        self.width = width

    def setGameSpeed(self, gameSpeed):
        self.gameSpeed = gameSpeed

    def setSize(self, size):
        self.size = size

    def addPastPositions(self, x1, y1):
        self.pastPositions.append(x1)
        self.pastPositions.append(y1-2.5)

    def checkCollision(self, x1, y1):
        y1 = y1-2.5
        if x1 and y1 in self.pastPositions[:-2]:
            print("Collision?")
        #if x1-2 <= x1 <= x1+2 and y1-2 <= y1 <= y1+2 in self.pastPositions[:-2]:
        #    print("Collision?")

    #this doesnt seem to work, as tested in test
    #x1 and y1 kind of works

    def checkInRange(x, y, a):
        if x < y:
            Ausgabe1 = a - x

        if y < x:
            Ausgabe1 = a - y

        if Ausgabe1 >= 0:
            return True








# Jede Taste hat eine eigene Zahl
# print(pygame.K_LEFT) --> 276
# print(pygame.K_RIGHT) --> 275
# print(pygame.K_a) --> 97
# print(pygame.K_d) --> 100
# print(pygame.K_g) --> 103
# print(pygame.K_j) --> 106

game = Game()
game.addPlayer(name="Spieler_1", color="red", left=276, right=275)
#game.addPlayer(name="Spieler_2", color="white", left=97, right=100)
#game.addPlayer(name="Spieler_3", color="blue", left=103, right=106)

run = True


while run:


    pygame.time.delay(game.gameSpeed)
    # with this parameter you essentially control how often the game runs the loop, therefore you control the speed of the drawing
    # for being able to close the game with the x in the top right corner

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()


    for player in game.players:


        position = player.getPosition()

        xStart = position[0]
        yStart = position[1]
        xEnd = position[2]
        yEnd = position[3]
        winkel = position[4]

        #print("1")

        #print(player.getPosition())
        #print(game.pastPositions)


        game.checkCollision(xStart, yStart)

        pygame.draw.line(game.win, player.color, (xStart, yStart), (xEnd, yEnd), game.size)
        pygame.draw.line(game.win, (255,255,255), (xStart, yStart-2.5), (xStart, yStart-2.5), 4)
        pygame.draw.line(game.win, (255, 255, 255), (xStart, yStart-0.5), (xStart, yStart-4.5), 1)

        # Here we are able to control in which direction we draw a new square
        # radius controls the slized of pi you add or subtract from our sin,cos function up top

        left = player.left
        right = player.right

        if keys[left]:
            winkel = winkel + math.pi / player.radius

        if keys[right]:
            winkel = winkel - math.pi / player.radius

        xStart = xStart - (game.speed * math.sin(winkel))
        yStart = yStart - (game.speed * math.cos(winkel))
        xEnd = xEnd - (game.speed * math.sin(winkel))
        yEnd = yEnd - (game.speed * math.cos(winkel))

        # https://imgur.com/ErTLFns You control with sin and cos how much we move in each (x,y) direction


        #print("2")
        player.setPosition(xStart, yStart, xEnd, yEnd, winkel)

        #print("3")
        game.addPastPositions(xStart, yStart)
        #print(game.pastPositionsLenght)






    """

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
"""
    pygame.display.update()

pygame.quit()
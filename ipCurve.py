import pygame
import pygameMenu
from pygameMenu.locals import *
import math
import random

pygame.init()
pygame.display.set_caption("IPCurve")
font = pygame.font.SysFont(None, 48)
print(pygame.font.match_font('arial'))
background = (40,40,40)
height = 600
width = 600

class Player:
    # defining colors
    __colors = {
        "pink": (255, 0, 255),
        "white": (255, 255, 255),
        "red": (255, 0, 0),
        "green": (60, 255, 60),
        "blue": (100, 100, 255)
    }

    def __init__(self, name="", color="red", left=0, right=0):
        self.name = name
        self.color = self.__colors[color]
        self.left = left
        self.right = right

        self.setInitialPosition()

        self.score = 10
        self.scoreAccess = 0
        self.runScoreKeeper = True

        # the amount of times we divide pi, to get more or less slices
        self.radius = 20
        self.draw = True

        self.gapCounter = 0
        self.gapLength = 6
        self.randomGap = random.randint(60,90)
        self.gap = False

        self.runCollisionChecks = True



    def setInitialPosition(self, height=height, width=width, speed=5):
        x1 = random.randint(80, width - 80)
        y1 = random.randint(80, height - 80)
        x2 = x1
        y2 = y1 - speed
        winkel = random.randint(0, 50)
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

    def gapCreator(self):
        if self.gap == False:
            self.gapCounter = self.gapCounter + 1
            if self.gapCounter is self.randomGap:
                self.gap = True
                self.gapCounter = 0
        if self.gap == True:
            self.gapCounter = self.gapCounter + 1
            if self.gapCounter is self.gapLength:
                self.randomGap = random.randint(50,100)
                #Generates new random number for when the next gap should appear.
                self.gap = False
                self.gapCounter = 0

    # This function set gap True or False, depending on gapCounter.
    # While gap is
    # True: The game loop doesnt draw and doesnt append to pastPositionArray,
    # but it sets new positions for the now invisible line.
    # False: The gapCounter now counts to a random Number between 50 and 80 until it sets gap = True
    # Random number to ensure no two players have the same occurence

    def scoreKeeper(self):
        if self.scoreAccess is 1:
            self.score = self.score - 1
            self.scoreAccess = 0
            print(player.name, player.score)
        if player.score is 0:
            self.draw = False
            self.runScoreKeeper = False
            game.eliminatedPlayerCounter += 1


    # This function waits for scoreAccess to be 1.
    # scoreAccess turns 1 after a collision.
    # Then it decreases the score by one and locks the Access again.
    # Second if condition asks if a player has no points.
    # If so he isn't able to draw anymore.

    def lastPlayerCheck(self):
        if game.lastPlayerCounter is len(game.players) -1:
            self.draw = False
            a = 0
            for player in game.players:
                text = font.render(player.name + ": " + str(player.score), True, (background), (255, 255, 255))
                game.win.blit(text, (a, 0))
                a = a + 150
            text1 = font.render("Press Space for NEWROUND!", True, (background), (255, 255, 255))
            game.win.blit(text1, (0, game.height-50))


    def eliminatedPlayerCheck(self):
        if game.eliminatedPlayerCounter is len(game.players) - 1:
            self.draw = False
            for player in game.players:
                if player.score != 0:
                    game.winner = player.name
            text = font.render('The winner is: ' + game.winner, True, (background), (255, 255, 255))
            text2 = font.render("Press n for NEWGAME!", True, (background), (255, 255, 255))
            textrect = text.get_rect()
            textrect2 = text2.get_rect()
            textrect.centerx = game.win.get_rect().centerx
            textrect.centery = game.win.get_rect().centery
            game.win.blit(text, textrect)
            game.win.blit(text2, (0, game.height-50))

    # Here it checks if a player is the last player by letting it count up each time a player terminates.
    # It then checks if "number of players" - 1 already terminated. If so the current player is the last one.
    # After that we set draw = False to bypass the scoreKeeper function which triggers
    # when the collision functions trigger.
    # If we let the last player collide as usual, everyone would loose a point in each round.
    # (That would be pointless. Pun intended.)


class Game:

    def __init__(self, height: int = height, width: int = width) -> object:
        self.height = height
        self.width = width
        # niedriger ist schneller, 45 is best
        self.gameSpeed = 45
        self.win = pygame.display.set_mode((height, width))
        self.win.fill(background)

        self.players = []
        self.pastXpositions = []
        self.pastYpositions = []

        # size and speed need to be the same to draw a nice looking line
        self.size = 5
        self.speed = self.size

        self.lastPlayerCounter = 0
        self.eliminatedPlayerCounter = 0

        self.winner = ""

        self.runControls = True


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
        y1 = y1-2.5
        self.pastXpositions.append(x1)
        self.pastYpositions.append(y1)

    def checkCollision(self, x1, y1):
        interval = 3
        y1 = y1 - 2.5
        k = 0
        for i in self.pastYpositions[:-len(self.players)]:
            if y1-interval <= i <= y1+interval:
                if x1-interval <= self.pastXpositions[k] <= x1+interval:
                    player.draw = False
                    player.runCollisionChecks = False
                    player.scoreAccess = 1
                    self.lastPlayerCounter = self.lastPlayerCounter + 1
                    # Stops the if statement for drawing the line
                    # After detecting a collision stops further checks for a collision
                    # Allows the player.scoreKeeper to run. Subtracts one from start points.
                    # Adds one to the lastPlayerCounter
                    break
            k = k + 1

    def checkWallCollision(self, x1, y1):
        y1 = y1 - 2.5
        if x1 > self.height or x1 < 0 or y1 > self.width or y1 < 0:
            player.draw = False
            player.runCollisionChecks = False
            player.scoreAccess = 1
            self.lastPlayerCounter = self.lastPlayerCounter + 1
            # Stops the if statement for drawing the line
            # After detecting a collision stops further checks for a collision
            # Allows the player.scoreKeeper to run. Subtracts one from start points.
            # Adds one to the lastPlayerCounter


    def newRound(self):
        player.setInitialPosition()
        self.win.fill(background)
        self.pastYpositions = []
        self.pastXpositions = []

        if player.score != 0:
            player.draw = True
        player.runCollisionChecks = True

        self.lastPlayerCounter = game.eliminatedPlayerCounter

        pygame.time.delay(100)
        # Sets new positions and angle etc; Just like at the start of the game
        # Paints a black screen
        # Empties the pastPosition lists
        # Re-enables the ability to draw the line
        # Re-enables the ability to check for collision
        # Sets the lastPlayerCounter to zero
        # Slight delay for a cleaner looking start

    def newGame(self):
        for player in game.players:
            player.score = 10
        print(player.name, player.score)

        player.setInitialPosition()
        self.win.fill(background)
        self.pastYpositions = []
        self.pastXpositions = []
        del game.players[:]

        player.draw = True
        player.runCollisionChecks = True
        player.runScoreKeeper = True

        self.lastPlayerCounter = 0
        self.eliminatedPlayerCounter = 0

        events = pygame.event.get()
        startMenu.mainloop(events)
        startMenu._dopause = True
        startMenu.enable()





# Jede Taste hat eine eigene Zahl
# print(pygame.K_LEFT) --> 276
# print(pygame.K_RIGHT) --> 275

# print(pygame.K_a) --> 97
# print(pygame.K_s) --> 115

# print(pygame.K_g) --> 103
# print(pygame.K_h) --> 104

#print(pygame.K_k) --> 107
#print(pygame.K_l) --> 108

# print(pygame.K_SPACE) --> 32

game = Game()






#TODO Startmenu erstellen. Mithilfe von https://ppizarror.com/pygame-menu/
def bgfun():
    pass

def Start2():
    game.win.fill(background)
    startMenu._dopause = False
    game.addPlayer(name="Rot", color="red", left=276, right=275)
    game.addPlayer(name="Weiß", color="white", left=97, right=115)
    startMenu.disable()

def Start3():
    game.win.fill(background)
    startMenu._dopause = False
    game.addPlayer(name="Rot", color="red", left=276, right=275)
    game.addPlayer(name="Weiß", color="white", left=97, right=115)
    game.addPlayer(name="Blau", color="blue", left=103, right=104)
    startMenu.disable()

def Start4():
    game.win.fill(background)
    startMenu._dopause = False
    game.addPlayer(name="Rot", color="red", left=276, right=275)
    game.addPlayer(name="Weiß", color="white", left=97, right=115)
    game.addPlayer(name="Blau", color="blue", left=103, right=104)
    game.addPlayer(name="Grün", color="green", left=107, right=108)
    startMenu.disable()




startMenu = pygameMenu.Menu(game.win, game.width, game.height, font = pygameMenu.fonts.FONT_8BIT, title ="ipCurve", dopause=True, bgfun = bgfun)
startMenu.add_option("2 Spieler", Start2)
startMenu.add_option("3 Spieler", Start3)
startMenu.add_option("4 Spielern", Start4)



run = True
while run:

    keys = pygame.key.get_pressed()

    events = pygame.event.get()
    startMenu.mainloop(events)

    pygame.time.delay(game.gameSpeed)
    # with this parameter you essentially control how often the game runs the loop, therefore you control the speed of the drawing
    # for being able to close the game with the x in the top right corner

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    for player in game.players:
        if keys[pygame.K_SPACE]:
            game.newRound()
        if keys[pygame.K_n]:
            game.newGame()

        position = player.getPosition()
        xStart = position[0]
        yStart = position[1]
        xEnd = position[2]
        yEnd = position[3]
        winkel = position[4]


        if player.runCollisionChecks:
            game.checkCollision(xStart, yStart)
            game.checkWallCollision(xStart, yStart)

        if player.runScoreKeeper:
            player.scoreKeeper()

        player.eliminatedPlayerCheck()



        if player.draw:

            pygame.draw.line(game.win, (background), (xStart, yStart), (xEnd, yEnd), game.size)
            # 1.1 Always draws a line thats the background color.

            player.lastPlayerCheck()

            player.gapCreator()

            if player.gap == False:
                pygame.draw.line(game.win, player.color, (xStart, yStart), (xEnd, yEnd), game.size)
                #1.2 This draw function draws a line ontop of the background color with the player color


                #Collisions Rechtreck
                #pygame.draw.line(game.win, (255, 255, 255), (xStart, yStart-2.5), (xStart, yStart-2.5), 6)
                #pygame.draw.line(game.win, (255, 255, 255), (xStart, yStart+0.5), (xStart, yStart-5.5), 1)

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

            player.setPosition(xStart, yStart, xEnd, yEnd, winkel)

            if player.gap == False:
                game.addPastPositions(xStart, yStart)

            pygame.draw.line(game.win, (255,255,0), (xStart, yStart), (xEnd, yEnd), game.size)
            # 1.3 This draw function draws a yellow line at the newly modified xStart and yStart.
            # With the combination of 1.1,1.2,1.3 we are able to make it apear as to having a head.

        pygame.display.update()

pygame.quit()
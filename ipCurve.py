import pygame
import math
import random

pygame.init()
pygame.display.set_caption("IPCurve")
font = pygame.font.SysFont(None, 48)



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

        self.score = 10
        self.scoreAccess = 0

        # the amount of times we divide pi, to get more or less slices
        self.radius = 20
        self.draw = True

        self.gapCounter = 0
        self.randomGap = random.randint(50,80)
        self.gap = False

        self.runCollisionChecks = True

    def setInitialPosition(self, height=800, width=800, speed=5):
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

    def setColor(self, color):
        self.color = color

    def gapCreator(self):
        if self.gap == False:
            self.gapCounter = self.gapCounter + 1
            if self.gapCounter is self.randomGap:
                self.gap = True
                self.gapCounter = 0
        if self.gap == True:
            self.gapCounter = self.gapCounter + 1
            if self.gapCounter is 6:
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
            player.draw = False

    # This function waits for scoreAccess to be 1.
    # scoreAccess turns 1 after a collision.
    # Then it decreases the score by one and locks the Access again.
    # Second if condition asks if a player has no points.
    # If so he isn't able to draw anymore.

    def lastPlayerCheck(self):
        if game.lastPlayerCounter is len(game.players) - 1:
            self.draw = False

    # Here it checks if a player is the last player by letting it count up each time a player terminates.
    # It then checks if "number of players" - 1 already terminated. If so the current player is the last one.
    # After that we set draw = False to bypass the scoreKeeper function which triggers
    # when the collision functions trigger.
    # If we let the last player collide as usual, everyone would loose a point in each round.
    # (That would be pointless. Pun intended.)

class Game:

    def __init__(self, height: int = 800, width: int = 800) -> object:
        self.height = 800
        self.width = 800
        # niedriger ist schneller, 45 is best
        self.gameSpeed = 45
        self.win = pygame.display.set_mode((height, width))

        self.players = []
        self.pastXpositions = []
        self.pastYpositions = []

        # size and speed need to be the same to draw a nice looking line
        self.size = 5
        self.speed = self.size

        self.lastPlayerCounter = 0

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
        if x1 > game.width or x1 < 0 or y1 > game.height or y1 < 0:
            player.draw = False
            player.runCollisionChecks = False
            player.scoreAccess = 1
            self.lastPlayerCounter = self.lastPlayerCounter + 1
            # Stops the if statement for drawing the line
            # After detecting a collision stops further checks for a collision
            # Allows the player.scoreKeeper to run. Subtracts one from start points.
            # Adds one to the lastPlayerCounter

    def newGame(self):
        if keys[pygame.K_SPACE]:
            player.setInitialPosition()
            game.win.fill((0, 0, 0))
            self.pastYpositions = []
            self.pastXpositions = []

            player.draw = True
            player.runCollisionChecks = True

            self.lastPlayerCounter = 0

            pygame.time.delay(100)
            # Sets new positions and angle etc; Just like at the start of the game
            # Paints a black screen
            # Empties the pastPosition lists
            # Re-enables the ability to draw the line
            # Re-enables the ability to check for collision
            # Sets the lastPlayerCounter to zero
            # Slight delay for a cleaner looking start




# Jede Taste hat eine eigene Zahl
# print(pygame.K_LEFT) --> 276
# print(pygame.K_RIGHT) --> 275
# print(pygame.K_a) --> 97
# print(pygame.K_d) --> 100
# print(pygame.K_g) --> 103
# print(pygame.K_j) --> 106
# print(pygame.K_SPACE) --> 32

game = Game()
game.addPlayer(name="Spieler_1", color="red", left=276, right=275)
game.addPlayer(name="Spieler_2", color="white", left=97, right=100)
game.addPlayer(name="Spieler_3", color="blue", left=103, right=106)




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

        player.scoreKeeper()

        if player.draw:

            player.lastPlayerCheck()

            player.gapCreator()

            if player.gap == False:
                pygame.draw.line(game.win, player.color, (xStart, yStart), (xEnd, yEnd), game.size)
                #Collisions Rechtreck
                #pygame.draw.line(game.win, (255, 255, 255), (xStart, yStart-2.5), (xStart, yStart-2.5), 6)
                #pygame.draw.line(game.win, (255, 255, 255), (xStart, yStart+0.5), (xStart, yStart-5.5), 1)
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

            player.setPosition(xStart, yStart, xEnd, yEnd, winkel)

            if player.gap == False:
                game.addPastPositions(xStart, yStart)

        pygame.display.update()

pygame.quit()











"""
        if xEnd > width or xEnd < 0 or yEnd > height or yEnd < 0:
            text = basicfont.render('You lost!', True, (255, 0, 0), (255, 255, 255))
            textrect = text.get_rect()
            textrect.centerx = win.get_rect().centerx
            textrect.centery = win.get_rect().centery
    
            win.fill((255, 255, 255))
            win.blit(text, textrect)
            draw = False
"""





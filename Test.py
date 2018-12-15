import random
x = 100
y = 200
a = 150
b = 150


'''
def checkInRange(x,y,a,b):
    if x < y:
        Ausgabe1 = a-x
        Ausgabe2 = b-x

    if y < x:
        Ausgabe1 = a-y
        Ausgabe2 = b-y

    if Ausgabe1 >= 0 and Ausgabe2 >= 0:
        print("a and b are in between x and y")

checkInRange(x,y,a,b)
'''

list = []
list.append(a)
list.append(b)
lenge = len(list)



for i in list:




 def checkCollision(self, x1, y1):
        for i in self.pastXpositions:
            if x1-2 <= i <= x1+2:
                collisionX = True
            else:
                pass
        for j in self.pastYpositions:
            if y1-2 <= j <= y1+2:
                collisionY = True
            else:
                pass
        if collisionX and collisionY:
            print("Collision")




'''
list = []

list.append(x)
list.append(y)

print(list)
print(a - 2 <= a <= a + 2 in list)
print(b - 2 <= b <= b + 2 in list)

if a - 2 <= a <= a + 2 and b - 2 <= b <= b + 2 in list[:]:
    print("Collision!")

'''


a = 1
b = 2
c = 3
d = 4

list = []
player = []

player.append(a)
player.append(b)
list.append(a)
list.append(b)
list.append(c)
list.append(d)

print(list)
print(player)

if len(player) - 1 is 1:
    print("yay")

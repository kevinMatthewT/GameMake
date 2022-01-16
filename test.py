import pygame
import random
from threading import Timer
from pygame import mixer

#game running
pygame.init()
runningscreen= True
numArrows=1

#

#diplaying the screen
screen= pygame.display.set_mode((700,500))
pygame.display.set_caption("undyne battle simulator")
icon = pygame.image.load('pixel.png')
pygame.display.set_icon(icon)

#Making the player
playerImg=pygame.image.load("GreenHeart.png")
playerX=330
playerY=230

playerShield=pygame.image.load("shieldDown.png")
playerShieldX=307
playerShieldY=260

def player(x,y):
    screen.blit(playerImg,(playerX,playerY))
    screen.blit(playerShield,(x,y))

#random ones, store it to a new value of random= I

#void thing
emptyPICTURE=pygame.image.load("emptyPic.png")

#arrows
ArrowRight=pygame.image.load("ArrowRight.png")
ArrowRightX=700
ArrowRightY=230

ArrowDown=pygame.image.load("ArrowDown.png")
ArrowDownX=330
ArrowDownY=500

ArrowLeft=pygame.image.load("ArrowLeft.png")
ArrowLeftX=-10
ArrowLeftY=230

ArrowUp=pygame.image.load("Arrowup.png")
ArrowUpX=330
ArrowUpY=-10

#arrow key command
def Arrows(z,x,y):
    screen.blit(z,(x,y))
    Timer(7,Arrows).start()

#implement amount of arrows
ArrowIMG=[]
ArrowX=[]
ArrowY=[]
#randomizing arrow selection
DirectionOfArrow=["up","down","left","right"]
def chooseArrow():
    ListOfDirections=[]
    global numArrows
    i=0
    #choosing the direction
    while i<numArrows:
        DirectionsChoose=random.randint(0,3)
        ListOfDirections.append(DirectionOfArrow[DirectionsChoose])
        i+=1
    #putting the arrows
    for ArrowCount in ListOfDirections:
        if ArrowCount == "up":
            ArrowIMG.append(ArrowUp)
            ArrowX.append(ArrowUpX)
            ArrowY.append(ArrowUpY)
            
        elif ArrowCount =="down":
            ArrowIMG.append(ArrowDown)
            ArrowX.append(ArrowDownX)
            ArrowY.append(ArrowDownY)
            
            #Arrows(ArrowDown,ArrowDownX,ArrowDownY)
        elif ArrowCount =="left":
            ArrowIMG.append(ArrowLeft)
            ArrowX.append(ArrowLeftX)
            ArrowY.append(ArrowLeftY)
            
            #Arrows(ArrowLeft,ArrowLeftX,ArrowLeftY)
        elif ArrowCount =="right":
            ArrowIMG.append(ArrowRight)
            ArrowX.append(ArrowRightX)
            ArrowY.append(ArrowRightY)
            
            #Arrows(ArrowRight,ArrowRightX,ArrowRightY)
        else:
            pass

#shield blocking
def Blocked(shieldX,shieldY,ArrowX,ArrowY,ArrowType):
    if ArrowType==ArrowRight:
        if ArrowX == 360 and shieldX==360:
            return True
        else:
            return False
    elif ArrowType==ArrowLeft:
        if ArrowX == 300 and shieldX==300:
            return True
        else:
            return False
    elif ArrowType==ArrowLeft:
        if ArrowY == 209 and shieldY==209:
            return True
        else:
            return False
    elif ArrowType==ArrowLeft:
        if ArrowY == 260 and shieldY==260:
            return True
        else:
            return False
    else:
        return False

#screen running and looks

while runningscreen:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runningscreen=False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerShield=pygame.image.load("shield.png")
                playerShieldX=307
                playerShieldY=209
 
            if event.key == pygame.K_LEFT:
                playerShield=pygame.image.load("shieldLeft.png")
                playerShieldX=300
                playerShieldY=210
            
            if event.key == pygame.K_RIGHT:
                playerShield=pygame.image.load("shieldRight.png")
                playerShieldX=360
                playerShieldY=210

            if event.key == pygame.K_DOWN:
                playerShield=pygame.image.load("shieldDown.png")
                playerShieldX=307
                playerShieldY=260
    
    #moving the arrows
    
    for i in range(len(ArrowIMG)):
        if ArrowIMG[i]== ArrowRight:
            ArrowX[i] -= 1.5
        elif ArrowIMG[i]== ArrowDown:
            ArrowY[i] -= 1.5
        elif ArrowIMG[i]== ArrowLeft:
            ArrowX[i] += 1.5
        elif ArrowIMG[i]== ArrowUp:
            ArrowY[i] += 1.5
        elif ArrowIMG[i] == emptyPICTURE:
            pass

    screen.fill((0,0,0))

    player(playerShieldX,playerShieldY)
    
    pygame.display.update()



    #make it so that you call a random arrow, and when you enter this random arrow a new random arrow will exist
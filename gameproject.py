
import pygame
import random

#game running
pygame.init()
runningscreen= True

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

#player shield and heart icon
def player(z,x,y):
    screen.blit(playerImg,(playerX,playerY))
    screen.blit(z,(x,y))

#arrow direction
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

#implement amount of arrows
ArrowCount="right"
#randomizing arrow selection
DirectionOfArrow=["up","down","left","right"]

ArrowMovement=[]
def chooseArrow():
    global ArrowCount
    #choosing the direction
    DirectionsChoose=random.randint(0,3)
    print(DirectionsChoose)
    ArrowCount=DirectionOfArrow[DirectionsChoose]
    
    print(ArrowCount)
    #making sure the movement

    if ArrowCount == "up":
        Arrows(ArrowUp,ArrowUpX,ArrowUpY)
    elif ArrowCount =="down":
       Arrows(ArrowDown,ArrowDownX,ArrowDownY)
    elif ArrowCount =="left":
        Arrows(ArrowLeft,ArrowLeftX,ArrowLeftY)
    elif ArrowCount =="right":
        Arrows(ArrowRight,ArrowRightX,ArrowRightY)
    else:
        pass
    
    

#shield blocking and arrow hitting shield
def Blocked(ArrowType):
    if ArrowType=="right":
        if ArrowRightX == 360 and playerShieldX==360:
            return True
        else:
            return False
    elif ArrowType=="left":
        if ArrowLeftX == 300 and playerShieldX==300:
            return True
        else:
            return False
    elif ArrowType=="up":
        if ArrowUpY == 200 and playerShieldY==209:
            return True
        else:
            return False
    elif ArrowType=="down":
        if ArrowDownY == 260 and playerShieldY==260:
            return True
        else:
            return False
    else:
        return False

#screen running and looks
score=0

while runningscreen:
    #moving arrows
    ArrowRightX -= 0.5
    ArrowDownY -= 0.5
    ArrowLeftX += 0.5
    ArrowUpY += 0.5
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runningscreen=False
        #changing the shield position
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerShield=pygame.image.load("shield.png")
                playerShieldX=307
                playerShieldY=209
                player(playerShield,playerShieldX,playerShieldY)
 
            if event.key == pygame.K_LEFT:
                playerShield=pygame.image.load("shieldLeft.png")
                playerShieldX=300
                playerShieldY=210
                player(playerShield,playerShieldX,playerShieldY)
            
            if event.key == pygame.K_RIGHT:
                playerShield=pygame.image.load("shieldRight.png")
                playerShieldX=360
                playerShieldY=210
                player(playerShield,playerShieldX,playerShieldY)

            if event.key == pygame.K_DOWN:
                playerShield=pygame.image.load("shieldDown.png")
                playerShieldX=307
                playerShieldY=260
                player(playerShield,playerShieldX,playerShieldY)
        
    
    
    screen.fill((0,0,0))
    #starting the code
    player(playerShield,playerShieldX,playerShieldY)
    hit=Blocked(ArrowCount)
    #continue the code
    chooseArrow()
    #Arrows(ArrowRight,ArrowRightX,ArrowRightY)
    if hit==True:
        
        score +=1
        ArrowUpX=330
        ArrowUpY=-10
        ArrowLeftX=-10
        ArrowLeftY=230
        ArrowDownX=330
        ArrowDownY=500
        ArrowRightX=700
        ArrowRightY=230
        
        print(score)
    else:
        pass

    pygame.display.update()

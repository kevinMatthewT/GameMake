
import pygame
import random
from pygame import mixer
state="empty"
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

#song Battle Against a true hero by Toby Fox
mixer.music.load("BackgroundBATH.wav")
mixer.music.play(-1)

#implement amount of arrows
ArrowCount="up"
#randomizing arrow selection
DirectionOfArrow=["up","down","left","right"]

def chooseArrow():
    global ArrowCount
    global state
    #choosing the direction
    DirectionsChoose=random.randint(0,3)
    ArrowCount=DirectionOfArrow[DirectionsChoose]
    #making sure the movement
    #state active so that if it happens then it will activate
    if ArrowCount == "up":
        Arrows(ArrowUp,ArrowUpX,ArrowUpY)
        state="active"
    elif ArrowCount =="down":
        Arrows(ArrowDown,ArrowDownX,ArrowDownY)
        state="active"
    elif ArrowCount =="left":
        Arrows(ArrowLeft,ArrowLeftX,ArrowLeftY)
        state="active"
    elif ArrowCount =="right":
        Arrows(ArrowRight,ArrowRightX,ArrowRightY)
        state="active"
    else:
        pass

styleText= pygame.font.Font('freesansbold.ttf',16)
scoreX=3
scoreY=3
HitX=3
HitY=21

def ScoreAndHit(X1,Y1,X2,Y2):
    TotalScore=styleText.render("Score:" +str(score),True,(255,255,255))
    TotalHits= styleText.render("Hits:" +str(hits),True,(255,255,255))
    screen.blit(TotalScore,(X1,Y1))
    screen.blit(TotalHits,(X2,Y2))

    
hits=0
#shield blocking and arrow hitting shield
def Blocked(ArrowType):
    global hits
    global score
    if ArrowType=="right":
        if 350>ArrowRightX < 360 and playerShieldX==360:
            return True
        elif ArrowRightX==340:
            hits +=1
            score -=1
            print("Hits")
            print(hits)
            return True
        else:
            return False
    elif ArrowType=="left":
        if 290<ArrowLeftX< 300 and playerShieldX==300:
            return True
        elif ArrowLeftX==320:
            hits +=1
            score -=1
            print("Hits")
            print(hits)

            return True
        else:
            return False
    elif ArrowType=="up":
        if 190<ArrowUpY <200 and playerShieldY==209:
            return True
        elif ArrowUpY==220:
            hits +=1
            score -=1
            print("Hits")
            print(hits)
            return True
        else:
            return False
    elif ArrowType=="down":
        if 250<ArrowDownY<260 and playerShieldY==260:
            return True
        elif ArrowDownY==200:
            hits +=1
            score -=1
            print("Hits")
            print(hits)
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
    while state=="empty":
        chooseArrow()
    else :
        if ArrowCount=="up":
            Arrows(ArrowUp,ArrowUpX,ArrowUpY)
        elif ArrowCount=="down":
            Arrows(ArrowDown,ArrowDownX,ArrowDownY)
        elif ArrowCount=="right":
            Arrows(ArrowRight,ArrowRightX,ArrowRightY)
        elif ArrowCount=="left":
            Arrows(ArrowLeft,ArrowLeftX,ArrowLeftY)
        
    
        
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
        state="empty"
        print("Total Score")
        print(score)
    else:
        pass
    ScoreAndHit(scoreX,scoreY,HitX,HitY)
    pygame.display.update()

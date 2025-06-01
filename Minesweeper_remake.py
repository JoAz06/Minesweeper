import random
import pygame
pygame.init()
##########Colors##########
white=(255,255,255)
black=(0,0,0)
grey=(128,128,128)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
orange=(255,128,0)
pink=(255,0,191)
yellow=(255,255,0)
cyan=(0,255,255)
##########

##########Creating the board##########
size=5
NbBomb=1
NbCase=size*size
NbSafeCase=NbCase-NbBomb
Board=[]
BoardStatus=[]
x=1
y=1
while y<=size:
    while x<=size:
        Board=Board+[(x,y)]
        x=x+1
        BoardStatus=BoardStatus+[0]
    else:
        y=y+1
        x=1
##########

##########Generating Bombs##########
NbBombTest=NbBomb
RandomList=[]
while len(RandomList)<NbCase:
    while NbBombTest!=0:
        RandomList=RandomList+[1]
        NbBombTest=NbBombTest-1
    RandomList=RandomList+[0]
##########

##########Placing Bombs##########
BombList=[]
while len(BombList)<NbCase:
    RandomChoice=random.choice(RandomList)
    RandomList.remove(RandomChoice)
    BombList=BombList+[RandomChoice]
##########

##########Danger Number##########
DangerList=[]
DangerLevel=0
BoxIndex=0
while len(DangerList)<NbCase:
    if  Board[BoxIndex][0] !=size and BombList[BoxIndex+1]==1:
        DangerLevel=DangerLevel+1
    if  Board[BoxIndex][0] !=1 and BombList[BoxIndex-1]==1:
        DangerLevel=DangerLevel+1
    if  Board[BoxIndex][1] !=size and BombList[BoxIndex+size]==1:
        DangerLevel=DangerLevel+1
    if  Board[BoxIndex][1] !=1 and BombList[BoxIndex-size]==1:
        DangerLevel=DangerLevel+1
    if  Board[BoxIndex][0] !=size and Board[BoxIndex][1] !=size and BombList[BoxIndex+size+1]==1:
        DangerLevel=DangerLevel+1
    if  Board[BoxIndex][0] !=1 and Board[BoxIndex][1] != size and BombList[BoxIndex+size-1]==1:
        DangerLevel=DangerLevel+1
    if  Board[BoxIndex][0] !=1 and Board[BoxIndex][1] !=1 and BombList[BoxIndex-size-1]==1:
        DangerLevel=DangerLevel+1
    if  Board[BoxIndex][0] !=size and Board[BoxIndex][1] !=1 and BombList[BoxIndex-size+1]==1:
        DangerLevel=DangerLevel+1
    DangerList=DangerList+[DangerLevel]
    BoxIndex=BoxIndex+1
    DangerLevel=0
##########

##########Pygame Display##########
running=True
screen=pygame.display.set_mode((750,750))
pygame.display.set_caption('Minesweeper')
screen.fill(white)
BoxSize=750/size
x=BoxSize
y=BoxSize
ActiveBox=[]
myfont = pygame.font.SysFont("Comic Sans MS",int(BoxSize/1.5))  
Numbers=[myfont.render('0',1,black),myfont.render('1',1,black),myfont.render('2',1,black),myfont.render('3',1,black),myfont.render('4',1,black),myfont.render('5',1,black),myfont.render('6',1,black),myfont.render('7',1,black),myfont.render('8',1,black),myfont.render('9',1,black)]

while x<=(750-BoxSize):
    pygame.draw.line(screen,black,(x,0),(x,750))
    x=x+BoxSize
while y<=(750-BoxSize):
    pygame.draw.line(screen,black,(0,y),(750,y))
    y=y+BoxSize
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        key=pygame.key.get_pressed()
        mouse_pos=pygame.mouse.get_pos()
        if (pygame.mouse.get_pressed())[0]==1 and (BoardStatus[(Board.index((-((-(mouse_pos[0]))//BoxSize),-(((-mouse_pos[1]))//BoxSize))))])==0 and BombList[(Board.index((-((-(mouse_pos[0]))//BoxSize),-(((-mouse_pos[1]))//BoxSize))))]==0 and (DangerList[(Board.index((-((-(mouse_pos[0]))//BoxSize),-(((-mouse_pos[1]))//BoxSize))))]) !=0:
            ActiveBox=ActiveBox+[Board.index((-((-(mouse_pos[0]))//BoxSize),-(((-mouse_pos[1]))//BoxSize)))]
        if (pygame.mouse.get_pressed())[0]==1 and (BoardStatus[(Board.index((-((-(mouse_pos[0]))//BoxSize),-(((-mouse_pos[1]))//BoxSize))))])==0 and BombList[(Board.index((-((-(mouse_pos[0]))//BoxSize),-(((-mouse_pos[1]))//BoxSize))))]==1:
             ActiveBox=ActiveBox+[Board.index((-((-(mouse_pos[0]))//BoxSize),-(((-mouse_pos[1]))//BoxSize)))]
             screen.blit((myfont.render('*',1,red)),(((Board[ActiveBox[0]])[0])*150+BoxSize/4-BoxSize,((Board[ActiveBox[0]])[1])*150-BoxSize))
             running=False
        if (pygame.mouse.get_pressed())[0]==1 and (BoardStatus[(Board.index((-((-(mouse_pos[0]))//BoxSize),-(((-mouse_pos[1]))//BoxSize))))])==0 and BombList[(Board.index((-((-(mouse_pos[0]))//BoxSize),-(((-mouse_pos[1]))//BoxSize))))]==0 and (DangerList[(Board.index((-((-(mouse_pos[0]))//BoxSize),-(((-mouse_pos[1]))//BoxSize))))]) ==0:
            ActiveBox=ActiveBox+[Board.index((-((-(mouse_pos[0]))//BoxSize),-(((-mouse_pos[1]))//BoxSize)))]
            i=0
            while i+1<=len(ActiveBox):
                if Board[ActiveBox[i]][0]<size and BoardStatus[ActiveBox[i]+1] ==0 and DangerList[ActiveBox[i]]==0 and BombList[ActiveBox[i]+1]==0 and ActiveBox[i]+1 not in ActiveBox:
                    ActiveBox=ActiveBox+[ActiveBox[i]+1]
                if Board[ActiveBox[i]][0]>1 and BoardStatus[ActiveBox[i]-1] ==0 and DangerList[ActiveBox[i]]==0 and BombList[ActiveBox[i]-1]==0 and ActiveBox[i]-1 not in ActiveBox:
                    ActiveBox=ActiveBox+[ActiveBox[i]-1]
                if Board[ActiveBox[i]][1]<size and BoardStatus[ActiveBox[i]+size] ==0 and DangerList[ActiveBox[i]]==0 and BombList[ActiveBox[i]+size]==0 and ActiveBox[i]+size not in ActiveBox:
                    ActiveBox=ActiveBox+[ActiveBox[i]+size]
                if Board[ActiveBox[i]][1]>1 and BoardStatus[ActiveBox[i]-size] ==0 and DangerList[ActiveBox[i]]==0 and BombList[ActiveBox[i]-size]==0 and ActiveBox[i]-size not in ActiveBox:
                    ActiveBox=ActiveBox+[ActiveBox[i]-size]
                if Board[ActiveBox[i]][0]<size and  Board[ActiveBox[i]][1]>1 and BoardStatus[ActiveBox[i]-size+1] ==0 and DangerList[ActiveBox[i]]==0 and BombList[ActiveBox[i]-size+1]==0 and ActiveBox[i]-size+1 not in ActiveBox:
                    ActiveBox=ActiveBox+[ActiveBox[i]-size+1]
                if Board[ActiveBox[i]][0]<size and  Board[ActiveBox[i]][1]<size and BoardStatus[ActiveBox[i]+size+1] ==0 and DangerList[ActiveBox[i]]==0 and BombList[ActiveBox[i]+size+1]==0 and ActiveBox[i]+size+1 not in ActiveBox:
                    ActiveBox=ActiveBox+[ActiveBox[i]+size+1]
                if Board[ActiveBox[i]][0]>1 and  Board[ActiveBox[i]][1]>1 and BoardStatus[ActiveBox[i]-size-1] ==0 and DangerList[ActiveBox[i]]==0 and BombList[ActiveBox[i]-size-1]==0 and ActiveBox[i]-size-1 not in ActiveBox:
                    ActiveBox=ActiveBox+[ActiveBox[i]-size-1]
                if Board[ActiveBox[i]][0]<size and  Board[ActiveBox[i]][1]<size and BoardStatus[ActiveBox[i]+size-1] ==0 and DangerList[ActiveBox[i]]==0 and BombList[ActiveBox[i]+size-1]==0 and ActiveBox[i]+size-1 not in ActiveBox:
                    ActiveBox=ActiveBox+[ActiveBox[i]+size-1]
                i=i+1
        while len(ActiveBox)>=1 and running:
            BoardStatus=BoardStatus[:(ActiveBox[0])]+[1]+BoardStatus[(ActiveBox[0]+1):]
            screen.blit(Numbers[DangerList[ActiveBox[0]]],(((Board[ActiveBox[0]])[0])*BoxSize+BoxSize/4-BoxSize,((Board[ActiveBox[0]])[1])*BoxSize-BoxSize))
            ActiveBox.remove(ActiveBox[0])
    pygame.display.flip()
pygame.time.wait(1000)
pygame.QUIT
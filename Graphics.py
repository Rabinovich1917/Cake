def stickMan(X, Y, T):
    pygame.draw.circle(gameDisplay, green, [10+X, 10+Y], radiusLead)
    pygame.draw.line(gameDisplay, red, [10+X, 20+Y], [10+X, 50+Y], T)
    pygame.draw.line(gameDisplay, red, [10+X, 50+Y], [20+X, 65+Y], T)
    pygame.draw.line(gameDisplay, red, [10+X, 50+Y], [X, 65+Y], T)
    pygame.draw.line(gameDisplay, red, [10+X, 20+Y], [X, 35+Y], T)
    pygame.draw.line(gameDisplay, red, [10+X, 20+Y], [20+X, 35+Y], T)        
# -*-coding: utf-8 -*-
import pygame
import math
 
pygame.init()
 
winWidth=800
winHeight=600
size=[winWidth, winHeight]
gameDisplay=pygame.display.set_mode(size)
image1=pygame.image.load("1.jpg").convert()
image2=pygame.image.load("St.jpg").convert()
image3=pygame.image.load("Len.jpg").convert()
clicksound=pygame.mixer.music.load("Gunshots.wav")
# keysound=pygame.mixer.music.load("MachineGun.wav")
FPS=200
 
pygame.display.set_caption("My Game")
clock=pygame.time.Clock()
 
white=(0xFF, 0xFF, 0xFF)
black=(0, 0, 0)
red=(0xFF, 0, 0)
green=(0, 0xFF, 0)
blue=(0, 0, 0xFF)
 
# Инициализация
radiusLead=10
heightPartOfBody=5
X=100
Y=100
speedX=2
speedY=2
menR=False
menL=False
menU=False
menD=False

gameExit=False
 
while not gameExit:
    # Обработка нажатий
    for  event in pygame.event.get():
        # print(event)
        if event.type==pygame.QUIT:
            gameExit=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                menR=True
            if event.key==pygame.K_LEFT:
                menL=True
            if event.key==pygame.K_UP:
                menU=True
            if event.key==pygame.K_DOWN:
                menD=True

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                menR=False
            if event.key==pygame.K_LEFT:
                menL=False
            if event.key==pygame.K_UP:
                menU=False
            if event.key==pygame.K_DOWN:
                menD=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            pygame.mixer.music.play()
            
    # Обработка движения мыши
    pos=pygame.mouse.get_pos()
    pygame.mouse.set_visible(False)
           
    # Обработка логики
    if menR==True:
        X+=speedX
        pygame.mixer.music.play()
    if menL==True:
        X-=speedX
        pygame.mixer.music.play()        
    if menU==True:
        Y-=speedY
        pygame.mixer.music.play()        
    if menD==True:
        Y+=speedY
        pygame.mixer.music.play()        
    # Обработка изображений
    gameDisplay.blit(image1, [0, 0])
    #gameDisplay.blit(image2, [0, 0])
    #gameDisplay.blit(image3, [500, 0])    
    
    stickMan(X, Y, heightPartOfBody)
    stickMan(pos[0], pos[1], heightPartOfBody)
   
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
quit()
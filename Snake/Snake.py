import pygame
import math
import time
import random

pygame.init()

winWidth  = 800
winHeight = 600
FPS = 15
size = [winWidth, winHeight]
gameDisplay = pygame.display.set_mode(size)

pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
smallFont = pygame.font.SysFont('comicsansms', 20)
mediumFont = pygame.font.SysFont('comicsansms', 35)
largeFont = pygame.font.SysFont('comicsansms', 60)
img = pygame.image.load('snakehead.png')
imgApple = pygame.image.load('apple.png')
icon = pygame.image.load('ksnake.png')
pygame.display.set_icon(icon)


WHITE = (0xFF, 0xFF, 0xFF)
BLACK = (   0,    0,    0)
RED   = (0xFF,    0,    0)
GREEN = (   0, 0xAA,    0)
GREENA = (0, 0xFF, 0)
BLUE  = (   0,    0, 0xFF)

def text_object(text, color, size='small'):
    if size == 'small':
        textSerface = smallFont.render(text, True, color)    
    elif size == 'medium':
        textSerface = mediumFont.render(text, True, color)    
    elif size == 'large':
        textSerface = largeFont.render(text, True, color)
    return textSerface, textSerface.get_rect()

def message_to_screen(msg, color, xDisplace=0, yDisplace=0, size='small'):
    textSerf, textRect = text_object(msg, color, size)
    textRect.center = xDisplace, yDisplace
    gameDisplay.blit(textSerf, textRect)

def snake(snakeList, blockSize):
    if direction == 'right':
        head = pygame.transform.rotate(img, 270)    
    if direction == 'left':
        head = pygame.transform.rotate(img, 90)    
    if direction == 'up':
        head = img    
    if direction == 'down':
        head = pygame.transform.rotate(img, 180)

    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))

    for blk in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, GREEN, [blk[0], blk[1], blockSize, blockSize])

def apple_gen():
    appleX = random.randrange(0, winWidth - appleSize, 10)
    appleY = random.randrange(0, winHeight - appleSize, 10)

    return appleX, appleY

def score(score):
    message_to_screen("Score: " + str(score), BLACK, 50, 10)

blockSize = 20
appleSize = 30
introRectSizeLen = 100
introRectSizeWidth = 50

direction = 'right'

def game_intro():
    intro = True
    introRectColor1 = GREEN
    introRectColor2 = GREEN    
    
    while intro:
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    intro = False
            if event.type == pygame.MOUSEBUTTONDOWN and winWidth/2-200 < mousePos[0] < winWidth/2-100 and winHeight/2+100 < mousePos[1] < winHeight/2+150:
                intro = False
            if event.type == pygame.MOUSEBUTTONDOWN and winWidth/2+100 < mousePos[0] < winWidth/2+200 and winHeight/2+100 < mousePos[1] < winHeight/2+150:
                pygame.quit()
                quit()
                


        gameDisplay.fill(WHITE)
        message_to_screen("Welcome to snake game", GREEN, winWidth/2, winHeight/2-100, 'large')
        message_to_screen("The objective of the game is eat red apples", BLACK, winWidth/2, winHeight/2-30)
        message_to_screen("The more apples you eat, the longer you get", BLACK, winWidth/2, winHeight/2+10)
        message_to_screen("If you run into youself, or the edges, you die.", BLACK, winWidth/2, winHeight/2+50)
        message_to_screen("Press P to pause", BLACK, winWidth/2, winHeight/2+180)
        
        
        if winWidth/2-200 < mousePos[0] < winWidth/2-100 and winHeight/2+100 < mousePos[1] < winHeight/2+150:
            introRectColor1 = GREENA
        elif winWidth/2+100 < mousePos[0] < winWidth/2+200 and winHeight/2+100 < mousePos[1] < winHeight/2+150:
            introRectColor2 = GREENA
        else:
            introRectColor1, introRectColor2 = GREEN, GREEN
        rect(winWidth/2-200, winHeight/2+100, introRectColor1, introRectSizeLen, introRectSizeWidth)
        rect(winWidth/2+100, winHeight/2+100, introRectColor2, introRectSizeLen, introRectSizeWidth)
        message_to_screen("PLAY", BLACK, winWidth/2-150, winHeight/2+125, 'medium')
        message_to_screen("QUIT", BLACK, winWidth/2+150, winHeight/2+125, 'medium')
        
        
        pygame.display.update()
        clock.tick(5)

def game_pause():
    paused = True

    message_to_screen("PAUSED", BLACK, winWidth/2, winHeight/2-100, 'large')
    message_to_screen("Press C or P to play or Q to quit", BLACK, winWidth/2, winHeight/2+25)
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c or event.key == pygame.K_p:
                    paused = False
                    
def rect(introRectX, introRectY, introRectColor, lenRect, widthRect):
    pygame.draw.rect(gameDisplay, introRectColor, [introRectX, introRectY, lenRect, widthRect])


def game_loop():
    gameExit = False
    gameOver = False  

    global direction 
    direction = 'right'
    
    leadX = winWidth / 2
    leadY = winHeight / 2
    
    leadXChange = blockSize
    leadYChange = 0
    snakeList = []
    snakeLenght = 1

    appleX, appleY = apple_gen()


    while not gameExit:
        if gameOver == True:
            message_to_screen("GAME OVER", RED, winWidth/2, winHeight/2-50, 'large')
            message_to_screen("Press C to play again or Q to quit", BLACK, winWidth/2, winHeight/2+50)
            pygame.display.update()


        while gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        game_loop()


        for  event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    leadXChange = -blockSize
                    leadYChange = 0
                    direction = 'left'
                elif event.key == pygame.K_RIGHT:
                    leadXChange = blockSize
                    leadYChange = 0
                    direction = 'right'            
                elif event.key == pygame.K_UP:
                    leadYChange = -blockSize
                    leadXChange = 0    
                    direction = 'up'        
                elif event.key == pygame.K_DOWN:
                    leadYChange = blockSize
                    leadXChange = 0
                    direction = 'down'
                elif event.key == pygame.K_p:
                    game_pause()

                    
        leadX += leadXChange
        leadY += leadYChange

        if leadX >= winWidth or leadX < 0 or leadY >= winHeight or leadY < 0:
            gameOver = True



        
        gameDisplay.fill(WHITE)
        gameDisplay.blit(imgApple, (appleX, appleY))


        snakeHead = []
        snakeHead.append(leadX)
        snakeHead.append(leadY)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLenght:
            del snakeList[0]
        for block in snakeList[:-1]:
            if block == snakeHead:
                gameOver = True
        snake(snakeList, blockSize)

        score(snakeLenght - 1)
        pygame.display.update()

        # Обработка коллизий
        if leadX > appleX and leadX < appleX + appleSize or \
        leadX + blockSize > appleX and leadX + blockSize < appleX + appleSize:
            if leadY > appleY and leadY < appleY + appleSize or \
            leadY + blockSize > appleY and leadY + blockSize < appleY + appleSize:
                appleX, appleY = apple_gen()
                snakeLenght += 1

        clock.tick(FPS)
    
    pygame.quit()
    quit()


game_intro()
game_loop()
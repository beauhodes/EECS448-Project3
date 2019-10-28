# ALL IMPORTS AND ALL GLOBAL VARIABLES
#import math # NOT USED YET
#import random # NOT USED YET
import pygame
#import pygame.gfxdraw  # NOT USED YET
#from pygame.locals import * # NOT USED YET
from pikachu import Pikachu

# INITIALIZE PYGAME AND GLOBAL DISPLAY VARIABLES
pygame.init()
global displayWidth
displayWidth = 1080
global displayHeight
displayHeight = 720
global display
display = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('EECS448 Project 3: Pokemon Battle Simulator')

# GLOBAL TEXT OBJECT VARIABLES
global font
font = pygame.font.Font('freesansbold.ttf', 32)
global smallText
smallText = pygame.font.Font('freesansbold.ttf', 36)
global mediumText
mediumText = pygame.font.Font('freesansbold.ttf', 48)
global largeText
largeText = pygame.font.Font('freesansbold.ttf', 65)

# CREATES A TEXT OBJECT
def createTextObject(textToDisplay, fontToUse):
    textSurface = font.render(textToDisplay, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()

# DISPLAYS THE START SCREEN
def startScreen():
    textPlay, textPlay_RECT = createTextObject("PLAY!", largeText)
    textPlay_RECT.center = (displayWidth / 2, displayHeight / 1.2)

    playGame = True # MAIN GAME LOOP BOOLEAN VARIABLE
    while playGame == True: # MAIN GAME LOOP
        display.fill((192, 192, 192))
        display.blit(textPlay, textPlay_RECT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()

# MAIN
if __name__ == "__main__":
    startScreen() # Call startScreen to load the start screen

    #playerTest = Pikachu() # TESTER CODE
    #player1 = Pikachu() # Choose player1's Pokemon


#def fightScreen(playerTurn):

#def playerTurn():
    #will contain everything done in one turn, will call other functions such as attack, AI attack, checkForWin, etc.

# ALL IMPORTS AND ALL GLOBAL VARIABLES
import pygame
from pikachu import Pikachu
import random
#import math # NOT USED YET
#import random # NOT USED YET
#import pygame.gfxdraw  # NOT USED YET
#from pygame.locals import * # NOT USED YET

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
global BLACK
BLACK = pygame.Color(0, 0, 0)
global WHITE
WHITE = pygame.Color(255, 255, 255)
global RED
RED = pygame.Color(255, 0, 0)
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
    textSurface = font.render(textToDisplay, True, BLACK)
    return textSurface, textSurface.get_rect()

# CHECKS IF (x, y) IS INSIDE OF (rect.x, rect.y)
def isPointInRect(x, y, rect):
    if x < rect.x + rect.width and x > rect.x and y < rect.y + rect.height and y > rect.y:
        return True # (x, y) IS INSIDE OF (rect.x, rect.y)
    return False # (x, y) IS NOT INSIDE OF (rect.x, rect.y)

# (UNFINISHED) TRACKS IF THE PLAY BUTTON IS CLICKED
def trackPlayButton():
    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE
    #print("mouse(x, y): ", mouse[0], ",", mouse[1]) # TESTER CODE
    if displayWidth * 0.45 + 110 > mouse[0] > displayWidth * 0.45 and displayHeight * 0.805 + 40 > mouse[1] > displayHeight * 0.805: # VALID LOCATION OF PLAY BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.45, displayHeight * 0.805, 110, 40), 5) # BOX AROUND PLAY ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0): # MOUSE CLICK DETECTED
            # (UNFINISHED) IF PLAYER 1 AND PLAYER AI HAVE POKEMON SELECTED
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.45, displayHeight * 0.805, 110, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PLAY BUTTON
                # (UNFINISHED) THIS IS WHERE WINDOW SWITCH SHOULD OCCUR
                print("MOUSE CLICK DETECTED ON PLAY BUTTON")

# (UNFINISHED) TRACKS IF PLAYER 1'S PIKACHU BUTTON IS CLICKED
def trackPikachuButton_P1():
    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE
    #print("mouse(x, y): ", mouse[0], ",", mouse[1]) # TESTER CODE
    if displayWidth * 0.19 + 130 > mouse[0] > displayWidth * 0.19 and displayHeight * 0.17 + 40 > mouse[1] > displayHeight * 0.17: # VALID LOCATION OF PLAYER 1'S PIKACHU BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.19, displayHeight * 0.17, 130, 40), 5) # BOX AROUND PLAYER 1'S PIKACHU ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0): # MOUSE CLICK DETECTED
        # (UNFINISHED) IF PLAYER 1 AND PLAYER AI HAVE POKEMON SELECTED
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.19, displayHeight * 0.17, 130, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PLAYER 1'S PIKACHU BUTTON
                # (UNFINISHED) NEED TO SET VARIABLE - pokemonP1 - TO BE PIKACHU
                print("MOUSE CLICK DETECTED ON PLAYER 1'S PIKACHU BUTTON")

# (UNFINISHED) TRACKS IF PLAYER AI'S PIKACHU BUTTON IS CLICKED
def trackPikachuButton_AI():
    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE
    #print("mouse(x, y): ", mouse[0], ",", mouse[1]) # TESTER CODE
    if displayWidth * 0.71 + 130 > mouse[0] > displayWidth * 0.71 and displayHeight * 0.17 + 40 > mouse[1] > displayHeight * 0.17: # VALID LOCATION OF PLAYER AI'S PIKACHU BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.71, displayHeight * 0.17, 130, 40), 5) # BOX AROUND PLAYER AI'S PIKACHU ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0): # MOUSE CLICK DETECTED
        # (UNFINISHED) IF PLAYER 1 AND PLAYER AI HAVE POKEMON SELECTED
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.71, displayHeight * 0.17, 130, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PLAYER AI'S PIKACHU BUTTON
                # (UNFINISHED) NEED TO SET VARIABLE - pokemonAI - TO BE PIKACHU
                print("MOUSE CLICK DETECTED ON PLAYER AI'S PIKACHU BUTTON")

# (UNFINISHED) DISPLAYS THE START SCREEN
def startScreen():
    # PLAYER 1'S POKEMON OPTIONS
    textPlayer1, textPlayer1_RECT = createTextObject("Player 1's Pokemon", largeText)
    textPlayer1_RECT.center = (displayWidth / 4, displayHeight / 8)

    # PLAYER 1'S POKEMON BUTTONS
    textPikachu1, textPikachu1_RECT = createTextObject("Pikachu", mediumText)
    textPikachu1_RECT.center = (displayWidth / 4, displayHeight / 5)

    # PLAYER 2'S POKEMON OPTIONS
    textPlayer2, textPlayer2_RECT = createTextObject("Player 2's Pokemon", largeText)
    textPlayer2_RECT.center = (displayWidth / 1.3, displayHeight / 8)

    # PLAYER 2'S POKEMON BUTTONS
    textPikachu2, textPikachu2_RECT = createTextObject("Pikachu", mediumText)
    textPikachu2_RECT.center = (displayWidth / 1.3, displayHeight / 5)

    # PLAY BUTTON
    textPlay, textPlay_RECT = createTextObject("PLAY", largeText)
    textPlay_RECT.center = (displayWidth / 2, displayHeight / 1.2)

    playGame = True # MAIN GAME LOOP BOOLEAN VARIABLE
    while playGame == True: # MAIN GAME LOOP
        display.fill(WHITE) # MAKES BACKGROUND OF START SCREEN WHITE
        display.blit(textPlayer1, textPlayer1_RECT) # DISPLAYS PLAYER 1'S POKEMON
        display.blit(textPikachu1, textPikachu1_RECT) # DISPLAYS PIKACHU FOR PLAYER 1
        display.blit(textPlayer2, textPlayer2_RECT) # DISPLAYS PLAYER 2'S POKEMON
        display.blit(textPikachu2, textPikachu2_RECT) # DISPLAYS PIKACHU FOR PLAYER 2
        display.blit(textPlay, textPlay_RECT) # DISPLAYS PLAY
        for event in pygame.event.get(): # FOR-LOOP TO HANDLE ALL PYGAME EVENTS
            if event.type == pygame.QUIT: # IF PYGAME EVENT IS QUIT
                playGame = False # STOP RUNNING THE PROGRAM
                pygame.quit() # QUIT PYGAME
                quit() # QUIT PYTHON3
            trackPikachuButton_P1() # TRACKS IF PIKACHU BUTTON IS CLICKED BY PLAYER 1
            trackPikachuButton_AI() # TRACKS IF PIKACHU BUTTON IS CLICKED BY PLAYER AI
            trackPlayButton() # TRACKS IF PLAY BUTTON IS CLICKED
            pygame.display.update() # UPDATE THE PYGAME DISPLAY

#def fightScreen(playerTurn):
    #sets up graphics for fight screen

#def playerTurn():
    # WILL CONTAIN EVERYTHING DONE IN ONE TURN (WILL CALL OTHER FUNCTIONS SUCH AS attack, attack_AI, checkForWin, etc.)
    #has to begin by tracking "fight", "bag", "run", etc (needs to be a different function probably)
    #depending on choice, could call ThunderBoltAttack(player2) or usePotion() or whatever the choice is
    #if attack was chosen, pop up display showing success or failure AND update the UI to show lowered enemy health if hit
    #call AI turn

def AITurn():
    AIMove = random.randint(1,101)
    if (AIMove <= 90): #90% chance to attack
        #attack
        chosenAttack, result = playerAI.AIAttack() #chosenAttack will be the string of which attack was used, result was whether it worked or not
        #display 3 second popup window of which attack was chosen and whether it worked
        #checkForWin, if game over then exit this function and display victory screen
    else if (AIMove <= 98 and playerAI.hasItem()): #8% chance to use item
        #use item
    #add 2% chance to run, need a run function to end the game

# MAIN
if __name__ == "__main__":
    startScreen() # CALL startScreen TO LOAD THE START SCREEN

    #playerTest = Pikachu() # TESTER CODE
    #player1 = Pikachu() # CHOOSE PLAYER1'S POKEMON
    #playerAI = # CHOOSE AI POKEMON

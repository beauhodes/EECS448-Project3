# ALL IMPORTS AND ALL GLOBAL VARIABLES
import random
import pygame
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

# GLOBAL PLAYER POKEMON VARIABLES
global pokemonP1
pokemonP1 = ""
global pokemonAI
pokemonAI = ""

# GLOBAL GAME STATE VARIABLE
global gameState
gameState = ""

# CREATES A TEXT OBJECT
def createTextObject(textToDisplay, fontToUse):
    textSurface = font.render(textToDisplay, True, BLACK)
    return textSurface, textSurface.get_rect()

# CHECKS IF (x, y) IS INSIDE OF (rect.x, rect.y)
def isPointInRect(x, y, rect):
    if x < rect.x + rect.width and x > rect.x and y < rect.y + rect.height and y > rect.y:
        return True # (x, y) IS INSIDE OF (rect.x, rect.y)
    return False # (x, y) IS NOT INSIDE OF (rect.x, rect.y)

# TRACKS IF THE PLAY BUTTON IS CLICKED
def trackPlayButton():
    global pokemonP1
    global pokemonAI
    global gameState
    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE
    #print("mouse(x, y): ", mouse[0], ",", mouse[1]) # TESTER CODE
    if displayWidth * 0.45 + 110 > mouse[0] > displayWidth * 0.45 and displayHeight * 0.805 + 40 > mouse[1] > displayHeight * 0.805: # VALID LOCATION OF PLAY BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.45, displayHeight * 0.805, 110, 40), 5) # BOX AROUND PLAY ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0): # MOUSE CLICK DETECTED
            if pokemonP1 != "" and pokemonAI != "": # IF PLAYER 1 AND PLAYER AI HAVE POKEMON SELECTED
                if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.45, displayHeight * 0.805, 110, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PLAY BUTTON
                    print("MOUSE CLICK DETECTED ON PLAY BUTTON") # TESTER CODE
                    gameState = "fightScreen"
                    handleScreen(gameState) # "SWITCHES" THE PYGAME DISPLAY SCREEN
            else:
                if pokemonP1 == "":
                    print("ERROR: Player 1 needs to select a Pokemon to play with.")
                elif pokemonAI == "":
                    print("ERROR: Player AI needs to select a Pokemon to play with.")

# (UNFINISHED) TRACKS IF PLAYER 1'S POKEMON BUTTONS ARE CLICKED
def trackPokemonButtons_P1():
    global pokemonP1
    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE
    #print("mouse(x, y): ", mouse[0], ",", mouse[1]) # TESTER CODE
    if displayWidth * 0.19 + 130 > mouse[0] > displayWidth * 0.19 and displayHeight * 0.17 + 40 > mouse[1] > displayHeight * 0.17: # VALID LOCATION OF PLAYER 1'S PIKACHU BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.19, displayHeight * 0.17, 130, 40), 5) # BOX AROUND PLAYER 1'S PIKACHU ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0): # MOUSE CLICK DETECTED
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.19, displayHeight * 0.17, 130, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PLAYER 1'S PIKACHU BUTTON
                print("MOUSE CLICK DETECTED ON PLAYER 1'S PIKACHU BUTTON") # TESTER CODE
                pokemonP1 = "Pikachu" # GLOBAL pokemonP1 VARIABLE
                print("pokemonP1", pokemonP1) # TESTER CODE
    elif displayWidth * 0.173 + 170 > mouse[0] > displayWidth * 0.173 and displayHeight * 0.235 + 40 > mouse[1] > displayHeight * 0.235: # VALID LOCATION OF PLAYER 1'S CHARIZARD BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.173, displayHeight * 0.235, 170, 40), 5) # BOX AROUND PLAYER 1'S CHARIZARD ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0): # MOUSE CLICK DETECTED
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.173, displayHeight * 0.235, 170, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PLAYER 1'S CHARIZARD BUTTON
                print("MOUSE CLICK DETECTED ON PLAYER 1'S CHARIZARD BUTTON") # TESTER CODE
                pokemonP1 = "Charizard" # GLOBAL pokemonP1 VARIABLE
                print("pokemonP1", pokemonP1) # TESTER CODE

# (UNFINISHED) TRACKS IF PLAYER AI'S POKEMON BUTTONS ARE CLICKED
def trackPokemonButtons_AI():
    global pokemonAI
    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE
    #print("mouse(x, y): ", mouse[0], ",", mouse[1]) # TESTER CODE
    if displayWidth * 0.71 + 130 > mouse[0] > displayWidth * 0.71 and displayHeight * 0.17 + 40 > mouse[1] > displayHeight * 0.17: # VALID LOCATION OF PLAYER AI'S PIKACHU BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.71, displayHeight * 0.17, 130, 40), 5) # BOX AROUND PLAYER AI'S PIKACHU ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0): # MOUSE CLICK DETECTED
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.71, displayHeight * 0.17, 130, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PLAYER AI'S PIKACHU BUTTON
                print("MOUSE CLICK DETECTED ON PLAYER AI'S PIKACHU BUTTON") # TESTER CODE
                pokemonAI = "Pikachu" # GLOBAL pokemonAI VARIABLE
                print("pokemonAI", pokemonAI) # TESTER CODE
    elif displayWidth * 0.69 + 170 > mouse[0] > displayWidth * 0.69 and displayHeight * 0.235 + 40 > mouse[1] > displayHeight * 0.235: # VALID LOCATION OF PLAYER AI'S CHARIZARD BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.69, displayHeight * 0.235, 170, 40), 5) # BOX AROUND PLAYER AI'S CHARIZARD ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0): # MOUSE CLICK DETECTED
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.69, displayHeight * 0.235, 170, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PLAYER AI'S CHARIZARD BUTTON
                print("MOUSE CLICK DETECTED ON PLAYER AI'S CHARIZARD BUTTON") # TESTER CODE
                pokemonAI = "Charizard" # GLOBAL pokemonAI VARIABLE
                print("pokemonAI", pokemonAI) # TESTER CODE

# (UNFINISHED) HANDLES CONTROL OF GAMESTATE'S
def handleScreen(gameState):
    if gameState == "startScreen" or gameState == "fightScreen":
        while gameState == "startScreen":
            # PLAYER 1'S POKEMON OPTIONS
            textPlayer1, textPlayer1_RECT = createTextObject("Player 1's Pokemon", largeText)
            textPlayer1_RECT.center = (displayWidth / 4, displayHeight / 8)

            # PLAYER 1'S POKEMON BUTTONS
            textPikachu1, textPikachu1_RECT = createTextObject("Pikachu", mediumText)
            textPikachu1_RECT.center = (displayWidth / 4, displayHeight / 5)
            textCharizard1, textCharizard1_RECT = createTextObject("Charizard", mediumText)
            textCharizard1_RECT.center = (displayWidth / 4, displayHeight / 3.8)

            # (UNFINISHED) PLAYER 1'S POKEMON IMAGES
            # imagePikachu = pygame.image.load('Pikachu.jpg')
            # imagePikachu_RECT = imagePikachu.get_rect()
            # imagePikachu_RECT.center = (displayWidth / 6, displayHeight / 5.5)
            # imageChar = pygame.image.load('Charizard.jpg')
            # imageChar_RECT = imageChar.get_rect()
            # imageChar_RECT.center = (displayWidth / 7.5, displayHeight / 3.8)

            # PLAYER AI'S POKEMON OPTIONS
            textPlayerAI, textPlayerAI_RECT = createTextObject("Player AI's Pokemon", largeText)
            textPlayerAI_RECT.center = (displayWidth / 1.3, displayHeight / 8)

            # PLAYER AI'S POKEMON BUTTONS
            textPikachuAI, textPikachuAI_RECT = createTextObject("Pikachu", mediumText)
            textPikachuAI_RECT.center = (displayWidth / 1.3, displayHeight / 5)
            textCharizardAI, textCharizardAI_RECT = createTextObject("Charizard", mediumText)
            textCharizardAI_RECT.center = (displayWidth / 1.3, displayHeight / 3.8)

            # (UNFINISHED) PLAYER AI'S POKEMON IMAGES
            # imagePikachu2 = pygame.image.load('Pikachu.jpg')
            # imagePikachu2_RECT = imagePikachu2.get_rect()
            # imagePikachu2_RECT.center = (displayWidth / 1.45, displayHeight / 5.5)
            # imageChar2 = pygame.image.load('Charizard.jpg')
            # imageChar2_RECT = imageChar2.get_rect()
            # imageChar2_RECT.center = (displayWidth / 1.52, displayHeight / 3.8)

            # PLAY BUTTON
            textPlay, textPlay_RECT = createTextObject("PLAY", largeText)
            textPlay_RECT.center = (displayWidth / 2, displayHeight / 1.2)

            # (UNFINISHED) DISPLAY TEXT OBJECTS AND IMAGES
            display.fill(WHITE) # MAKES BACKGROUND OF START SCREEN WHITE
            # display.blit(imagePikachu, imagePikachu_RECT) # DISPLAYS PIKACHU IMAGE FOR PLAYER 1
            # display.blit(imageChar, imageChar_RECT) # DISPLAYS CHARIZARD IMAGE FOR PLAYER 1
            display.blit(textPlayer1, textPlayer1_RECT) # DISPLAYS PLAYER 1'S POKEMON
            display.blit(textPikachu1, textPikachu1_RECT) # DISPLAYS PIKACHU FOR PLAYER 1
            display.blit(textCharizard1, textCharizard1_RECT) # DISPLAYS CHARIZARD FOR PLAYER 1
            # display.blit(imagePikachu2, imagePikachu2_RECT) # DISPLAYS PIKACHU IMAGE FOR PLAYER AI
            # display.blit(imageChar2, imageChar2_RECT) # DISPLAYS CHARIZARD IMAGE FOR PLAYER AI
            display.blit(textPlayerAI, textPlayerAI_RECT) # DISPLAYS PLAYER AI'S POKEMON
            display.blit(textPikachuAI, textPikachuAI_RECT) # DISPLAYS PIKACHU FOR PLAYER AI
            display.blit(textCharizardAI, textCharizardAI_RECT) # DISPLAYS CHARIZARD FOR PLAYER AI
            display.blit(textPlay, textPlay_RECT) # DISPLAYS PLAY
            trackPokemonButtons_P1() # TRACKS IF PLAYER 1 HAS SELECTED A POKEMON
            trackPokemonButtons_AI() # TRACKS IF PLAYER AI HAS SELECTED A POKEMON
            trackPlayButton() # TRACKS IF PLAY BUTTON IS CLICKED
            for event in pygame.event.get(): # FOR-LOOP TO HANDLE ALL PYGAME EVENTS
                if event.type == pygame.QUIT: # IF PYGAME EVENT IS QUIT
                    playGame = False # STOP RUNNING THE PROGRAM
                    pygame.quit() # QUIT PYGAME
                    quit() # QUIT PYTHON3
                pygame.display.update() # UPDATE THE PYGAME DISPLAY
        while gameState == "fightScreen":
            display.fill(BLACK) # MAKES BACKGROUND OF FIGHT SCREEN WHITE

            for event in pygame.event.get(): # FOR-LOOP TO HANDLE ALL PYGAME EVENTS
                if event.type == pygame.QUIT: # IF PYGAME EVENT IS QUIT
                    playGame = False # STOP RUNNING THE PROGRAM
                    pygame.quit() # QUIT PYGAME
                    quit() # QUIT PYTHON3
                pygame.display.update() # UPDATE THE PYGAME DISPLAY

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
    #else if (AIMove <= 98 and playerAI.hasItem()): #8% chance to use item
        #use item
    #add 2% chance to run, need a run function to end the game

# MAIN
if __name__ == "__main__":
    gameState = "startScreen"
    handleScreen(gameState) # LOADS THE START SCREEN

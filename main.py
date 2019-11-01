# ALL IMPORTS AND ALL GLOBAL VARIABLES
import random
import pygame
from electricCat import ElectricCat

# INITIALIZE PYGAME AND GLOBAL DISPLAY VARIABLES
pygame.init()
global displayWidth
displayWidth = 1080
global displayHeight
displayHeight = 720
global display
display = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('EECS448 Project 3: Progmon Battle Simulator')

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

# GLOBAL PLAYER PROGMON VARIABLES
global progmonP1
progmonP1 = ""
global progmonAI
progmonAI = ""
global playerMove
playerMove = ""

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
        return True
    return False

# TRACKS IF THE PLAY BUTTON IS CLICKED
def trackPlayButton():
    global progmonP1
    global progmonAI
    global gameState
    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE
    #print("mouse(x, y): ", mouse[0], ",", mouse[1]) # TESTER CODE
    if displayWidth * 0.45 + 110 > mouse[0] > displayWidth * 0.45 and displayHeight * 0.805 + 40 > mouse[1] > displayHeight * 0.805: # VALID LOCATION OF PLAY BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.45, displayHeight * 0.805, 110, 40), 5) # BOX AROUND PLAY ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0): # MOUSE CLICK DETECTED
            if progmonP1 != "" and progmonAI != "": # IF PLAYER 1 AND PLAYER AI HAVE PROGMON SELECTED
                if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.45, displayHeight * 0.805, 110, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PLAY BUTTON
                    #print("MOUSE CLICK DETECTED ON PLAY BUTTON") # TESTER CODE
                    gameState = "fightScreen"
                    handleScreen(gameState) # "SWITCHES" THE PYGAME DISPLAY SCREEN
            else:
                if progmonP1 == "":
                    print("ERROR: Player 1 needs to select a Progmon to play with.")
                elif progmonAI == "":
                    print("ERROR: Player AI needs to select a Progmon to play with.")

# (UNFINISHED) TRACKS IF PLAYER 1'S PROGMON BUTTONS ARE CLICKED
def trackProgmonButtons_P1():
    global progmonP1
    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE
    #print("mouse(x, y): ", mouse[0], ",", mouse[1]) # TESTER CODE
    if displayWidth * 0.16 + 200 > mouse[0] > displayWidth * 0.16 and displayHeight * 0.1 + 40 > mouse[1] > displayHeight * 0.1: # VALID LOCATION OF PLAYER 1'S ELECTRICCAT BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.16, displayHeight * 0.1, 200, 40), 5) # BOX AROUND PLAYER 1'S ELECTRICCAT ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0): # MOUSE CLICK DETECTED
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.16, displayHeight * 0.1, 200, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PLAYER 1'S ELECTRICCAT BUTTON
                #print("MOUSE CLICK DETECTED ON PLAYER 1'S ELECTRICCAT BUTTON") # TESTER CODE
                progmonP1 = "ElectricCat"
                print("progmonP1", progmonP1) # TESTER CODE
    elif displayWidth * 0.16 + 190 > mouse[0] > displayWidth * 0.16 and displayHeight * 0.223 + 40 > mouse[1] > displayHeight * 0.223: # VALID LOCATION OF PLAYER 1'S FIREDRAGON BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.16, displayHeight * 0.223, 190, 40), 5) # BOX AROUND PLAYER 1'S FIREDRAGON ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0): # MOUSE CLICK DETECTED
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.16, displayHeight * 0.223, 190, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PLAYER 1'S FIREDRAGON BUTTON
                #print("MOUSE CLICK DETECTED ON PLAYER 1'S FIREDRAGON BUTTON") # TESTER CODE
                progmonP1 = "FireDragon"
                print("progmonP1", progmonP1) # TESTER CODE

# (UNFINISHED) TRACKS IF PLAYER AI'S PROGMON BUTTONS ARE CLICKED
def trackProgmonButtons_AI():
    global progmonAI
    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE
    #print("mouse(x, y): ", mouse[0], ",", mouse[1]) # TESTER CODE
    if displayWidth * 0.68 + 200 > mouse[0] > displayWidth * 0.68 and displayHeight * 0.1 + 40 > mouse[1] > displayHeight * 0.1: # VALID LOCATION OF PLAYER AI'S ELECTRICCAT BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.68, displayHeight * 0.1, 200, 40), 5) # BOX AROUND PLAYER AI'S ELECTRICCAT ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0): # MOUSE CLICK DETECTED
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.68, displayHeight * 0.1, 200, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PLAYER AI'S ELECTRICCAT BUTTON
                #print("MOUSE CLICK DETECTED ON PLAYER AI'S ELECTRICCAT BUTTON") # TESTER CODE
                progmonAI = "ElectricCat"
                print("progmonAI", progmonAI) # TESTER CODE
    elif displayWidth * 0.68 + 190 > mouse[0] > displayWidth * 0.68 and displayHeight * 0.223 + 40 > mouse[1] > displayHeight * 0.223: # VALID LOCATION OF PLAYER AI'S FIREDRAGON BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.68, displayHeight * 0.223, 190, 40), 5) # BOX AROUND PLAYER AI'S FIREDRAGON ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0): # MOUSE CLICK DETECTED
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.68, displayHeight * 0.223, 190, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PLAYER AI'S FIREDRAGON BUTTON
                #print("MOUSE CLICK DETECTED ON PLAYER AI'S FIREDRAGON BUTTON") # TESTER CODE
                progmonAI = "FireDragon"
                print("progmonAI", progmonAI) # TESTER CODE

# (UNFINISHED) TRACKS IF BATTLE MENU BUTTONS ARE CLICKED
def trackBattleMenuButtons():
    pygame.draw.rect(display, BLACK, (displayWidth * 0.62, displayHeight * 0.79, 370, 120), 5) # BOX AROUND BATTLE MENU OPTIONS
    pygame.draw.rect(display, BLACK, (displayWidth * 0.06, displayHeight * 0.065, 350, 100), 5) # BOX AROUND PLAYER 1'S PROGMON NAME AND HEALTH
    pygame.draw.rect(display, BLACK, (displayWidth * 0.6, displayHeight * 0.065, 350, 100), 5) # BOX AROUND PLAYER AI'S PROGMON NAME AND HEALTH

    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE
    #print("mouse(x, y): ", mouse[0], ",", mouse[1]) # TESTER CODE
    if displayWidth * 0.665 + 110 > mouse[0] > displayWidth * 0.665 and displayHeight * 0.805 + 40 > mouse[1] > displayHeight * 0.805: # VALID LOCATION OF FIGHT BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.665, displayHeight * 0.805, 110, 40), 5) # BOX AROUND FIGHT ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0): # MOUSE CLICK DETECTED
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.665, displayHeight * 0.805, 110, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR FIGHT BUTTON
                print("MOUSE CLICK DETECTED ON FIGHT BUTTON") # TESTER CODE
                playerMove = "FIGHT"
    elif displayWidth * 0.63 + 180 > mouse[0] > displayWidth * 0.63 and displayHeight * 0.88 + 40 > mouse[1] > displayHeight * 0.88: # VALID LOCATION OF PROGMON BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.63, displayHeight * 0.88, 180, 40), 5) # BOX AROUND PROGMON ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0): # MOUSE CLICK DETECTED
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.63, displayHeight * 0.88, 180, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PROGMON BUTTON
                print("MOUSE CLICK DETECTED ON PROGMON BUTTON") # TESTER CODE
                playerMove = "PROGMON"
    elif displayWidth * 0.87 + 80 > mouse[0] > displayWidth * 0.87 and displayHeight * 0.805 + 40 > mouse[1] > displayHeight * 0.805: # VALID LOCATION OF BAG BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.87, displayHeight * 0.805, 80, 40), 5) # BOX AROUND BAG ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0): # MOUSE CLICK DETECTED
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.87, displayHeight * 0.805, 80, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR BAG BUTTON
                print("MOUSE CLICK DETECTED ON BAG BUTTON") # TESTER CODE
                playerMove = "BAG"
    elif displayWidth * 0.865 + 95 > mouse[0] > displayWidth * 0.865 and displayHeight * 0.88 + 40 > mouse[1] > displayHeight * 0.88: # VALID LOCATION OF QUIT BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.865, displayHeight * 0.88, 95, 40), 5) # BOX AROUND QUIT ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0): # MOUSE CLICK DETECTED
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.865, displayHeight * 0.88, 95, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR QUIT BUTTON
                print("Quitting...")
                pygame.quit()
                quit()

# (UNFINISHED) HANDLES CONTROL OF GAMESTATE'S
def handleScreen(gameState):
    if gameState == "startScreen" or gameState == "fightScreen":
        while gameState == "startScreen":
            # PLAYER 1'S PROGMON OPTIONS
            textPlayer1, textPlayer1_RECT = createTextObject("Player 1's Progmon", largeText)
            textPlayer1_RECT.center = (displayWidth / 4, displayHeight / 19)

            # PLAYER 1'S PROGMON BUTTONS
            textElectricCatP1, textElectricCatP1_RECT = createTextObject("Electric Cat", mediumText)
            textElectricCatP1_RECT.center = (displayWidth / 4, displayHeight / 7.5)
            textFireDragonP1, textFireDragonP1_RECT = createTextObject("Fire Dragon", mediumText)
            textFireDragonP1_RECT.center = (displayWidth / 4, displayHeight / 4)

            # PLAYER 1'S PROGMON IMAGES
            imageSmallElectricCatP1 = pygame.image.load('smallElectricCat.png')
            imageSmallElectricCatP1_RECT = imageSmallElectricCatP1.get_rect()
            imageSmallElectricCatP1_RECT.center = (displayWidth / 9, displayHeight / 7.5)
            imageSmallFireDragonP1 = pygame.image.load('smallFireDragon.png')
            imageSmallFireDragonP1_RECT = imageSmallFireDragonP1.get_rect()
            imageSmallFireDragonP1_RECT.center = (displayWidth / 9, displayHeight / 4)

            # PLAYER AI'S PROGMON OPTIONS
            textPlayerAI, textPlayerAI_RECT = createTextObject("Player AI's Progmon", largeText)
            textPlayerAI_RECT.center = (displayWidth / 1.3, displayHeight / 19)

            # PLAYER AI'S PROGMON BUTTONS
            textElectricCatAI, textElectricCatAI_RECT = createTextObject("Electric Cat", mediumText)
            textElectricCatAI_RECT.center = (displayWidth / 1.3, displayHeight / 7.5)
            textFireDragonAI, textFireDragonAI_RECT = createTextObject("Fire Dragon", mediumText)
            textFireDragonAI_RECT.center = (displayWidth / 1.3, displayHeight / 4)

            # PLAYER AI'S PROGMON IMAGES
            imageSmallElectricCatAI = pygame.image.load('smallElectricCat.png')
            imageSmallElectricCatAI_RECT = imageSmallElectricCatAI.get_rect()
            imageSmallElectricCatAI_RECT.center = (displayWidth / 1.6, displayHeight / 7.5)
            imageSmallFireDragonAI = pygame.image.load('smallFireDragon.png')
            imageSmallFireDragonAI_RECT = imageSmallFireDragonAI.get_rect()
            imageSmallFireDragonAI_RECT.center = (displayWidth / 1.6, displayHeight / 4)

            # PLAY BUTTON
            textPlay, textPlay_RECT = createTextObject("PLAY", largeText)
            textPlay_RECT.center = (displayWidth / 2, displayHeight / 1.2)

            # (UNFINISHED) DISPLAY TEXT OBJECTS AND IMAGES
            display.fill(WHITE) # MAKES BACKGROUND OF START SCREEN WHITE
            display.blit(imageSmallElectricCatP1, imageSmallElectricCatP1_RECT) # DISPLAYS ElectricCat IMAGE FOR PLAYER 1
            display.blit(imageSmallFireDragonP1, imageSmallFireDragonP1_RECT) # DISPLAYS FireDragon IMAGE FOR PLAYER 1
            display.blit(textPlayer1, textPlayer1_RECT) # DISPLAYS PLAYER 1'S PROGMON
            display.blit(textElectricCatP1, textElectricCatP1_RECT) # DISPLAYS ElectricCat FOR PLAYER 1
            display.blit(textFireDragonP1, textFireDragonP1_RECT) # DISPLAYS FireDragon FOR PLAYER 1
            display.blit(imageSmallElectricCatAI, imageSmallElectricCatAI_RECT) # DISPLAYS ElectricCat IMAGE FOR PLAYER AI
            display.blit(imageSmallFireDragonAI, imageSmallFireDragonAI_RECT) # DISPLAYS FireDragon IMAGE FOR PLAYER AI
            display.blit(textPlayerAI, textPlayerAI_RECT) # DISPLAYS PLAYER AI'S PROGMON
            display.blit(textElectricCatAI, textElectricCatAI_RECT) # DISPLAYS ElectricCat FOR PLAYER AI
            display.blit(textFireDragonAI, textFireDragonAI_RECT) # DISPLAYS FireDragon FOR PLAYER AI
            display.blit(textPlay, textPlay_RECT) # DISPLAYS PLAY

            trackProgmonButtons_P1()
            trackProgmonButtons_AI()
            trackPlayButton()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                pygame.display.update()
        while gameState == "fightScreen":
            # PLAYER 1'S PROGMON
            if progmonP1 == "ElectricCat":
                progmonNameP1 = "Electric Cat"
                progmonImageP1 = pygame.image.load('largeElectricCat.png')
                progmonImageP1_RECT = progmonImageP1.get_rect()
                progmonImageP1_RECT.center = (displayWidth / 4.5, displayHeight / 2.5)
            elif progmonP1 == "FireDragon":
                progmonNameP1 = "Fire Dragon"
                progmonImageP1 = pygame.image.load('largeFireDragon.png')
                progmonImageP1_RECT = progmonImageP1.get_rect()
                progmonImageP1_RECT.center = (displayWidth / 4.5, displayHeight / 2.5)
            # CREATE NAME FOR PLAYER 1
            textNameP1, textNameP1_RECT = createTextObject("Player 1", largeText)
            textNameP1_RECT.center = (displayWidth / 4.5, displayHeight / 30)

            # CREATE NAME FOR PLAYER 1'S PROGMON
            textProgmonP1, textProgmonP1_RECT = createTextObject(progmonNameP1, largeText)
            textProgmonP1_RECT.center = (displayWidth / 4.5, displayHeight / 10)

            # (UNFINISHED) CREATE HEALTH BAR FOR PLAYER 1'S PROGMON
            textProgmonHealthP1, textProgmonHealthP1_RECT = createTextObject("HEALTH", largeText)
            textProgmonHealthP1_RECT.center = (displayWidth / 4.5, displayHeight / 6)

            # PLAYER AI'S PROGMON
            if progmonAI == "ElectricCat":
                progmonNameAI = "Electric Cat"
                progmonImageAI = pygame.image.load('largeElectricCat.png')
                progmonImageAI_RECT = progmonImageAI.get_rect()
                progmonImageAI_RECT.center = (displayWidth / 1.3, displayHeight / 2.5)
            elif progmonAI == "FireDragon":
                progmonNameAI = "Fire Dragon"
                progmonImageAI = pygame.image.load('largeFireDragon.png')
                progmonImageAI_RECT = progmonImageAI.get_rect()
                progmonImageAI_RECT.center = (displayWidth / 1.3, displayHeight / 2.5)
            # CREATE NAME FOR PLAYER AI
            textNameAI, textNameAI_RECT = createTextObject("Player AI", largeText)
            textNameAI_RECT.center = (displayWidth / 1.3, displayHeight / 30)

            # CREATE NAME FOR PLAYER AI'S PROGMON
            textProgmonAI, textProgmonAI_RECT = createTextObject(progmonNameAI, largeText)
            textProgmonAI_RECT.center = (displayWidth / 1.3, displayHeight / 10)

            # (UNFINISHED) CREATE HEALTH BAR FOR PLAYER AI'S PROGMON
            textProgmonHealthAI, textProgmonHealthAI_RECT = createTextObject("HEALTH", largeText)
            textProgmonHealthAI_RECT.center = (displayWidth / 1.3, displayHeight / 6)

            # CREATE BATTLE MENU OPTIONS
            textFight, textFight_RECT = createTextObject("FIGHT", largeText)
            textFight_RECT.center = (displayWidth / 1.4, displayHeight / 1.2)
            textBag, textBag_RECT = createTextObject("BAG", largeText)
            textBag_RECT.center = (displayWidth / 1.1, displayHeight / 1.2)
            textProgmon, textProgmon_RECT = createTextObject("PROGMON", largeText)
            textProgmon_RECT.center = (displayWidth / 1.4, displayHeight / 1.1)
            textQuit, textQuit_RECT = createTextObject("QUIT", largeText)
            textQuit_RECT.center = (displayWidth / 1.1, displayHeight / 1.1)

            display.fill(WHITE) # MAKES BACKGROUND OF FIGHT SCREEN WHITE
            display.blit(progmonImageP1, progmonImageP1_RECT) # DISPLAYS ElectricCat IMAGE FOR PLAYER 1
            display.blit(textNameP1, textNameP1_RECT) # DISPLAYS PLAYER 1'S NAME
            display.blit(textProgmonP1, textProgmonP1_RECT) # DISPLAYS PLAYER 1'S PROGMON NAME
            display.blit(textProgmonHealthP1, textProgmonHealthP1_RECT) # DISPLAYS PLAYER 1'S PROGMON HEALTH
            display.blit(progmonImageAI, progmonImageAI_RECT) # DISPLAYS ElectricCat IMAGE FOR PLAYER AI
            display.blit(textNameAI, textNameAI_RECT) # DISPLAYS PLAYER AI'S NAME
            display.blit(textProgmonAI, textProgmonAI_RECT) # DISPLAYS PLAYER AI'S PROGMON NAME
            display.blit(textProgmonHealthAI, textProgmonHealthAI_RECT) # DISPLAYS PLAYER AI'S PROGMON HEALTH
            display.blit(textFight, textFight_RECT) # DISPLAYS FIGHT BATTLE OPTION
            display.blit(textBag, textBag_RECT) # DISPLAYS BAG BATTLE OPTION
            display.blit(textProgmon, textProgmon_RECT) # DISPLAYS PROGMON BATTLE OPTION
            display.blit(textQuit, textQuit_RECT) # DISPLAYS QUIT BATTLE OPTION

            trackBattleMenuButtons()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                pygame.display.update()

def playerTurn():
    # WILL CONTAIN EVERYTHING DONE IN ONE TURN (WILL CALL OTHER FUNCTIONS SUCH AS attack, attack_AI, checkForWin, etc.)
    #has to begin by tracking "fight", "bag", "run", etc (needs to be a different function probably)
    
    if(playerMove == "ATTACK"): #or ----- if (FIGHT == True):
        progmonP1.ThunderBoltAttack(progmonP1, progmonAI);
        #now we should display some sort of window/message for the user saying if they hit or not
        #update AI's health in the UI

    elif(playerMove == "BAG"):
        if (progmonP1.bagEmpty()):
            print("This player has nothing in their bag")   #Display some message to the player "BAG IS EMPTY"
        else:
            progmonP1.useHealthPotion() #for this implementation, all we can use is health potions
            AIBagTrack += 1 #lets AI track how many items you've use from your bag so it can be more AI-ish

    elif(playerMove == "RUN"):
        # DISPLAY SOME SORT OF MESSAGE SAYING THE THIS PLAYER CHOSE TO RUN
        pygame.quit()

    elif(playerMove == "PROGMON"):  #nothing for this is done, just an example
        #progmonP1.switchProgmon()


    AITurn()    #after player's turn is over, let AI go



def AITurn():
    # AIMove = random.randint(1,101)
    # if (AIMove <= 90): #90% chance to attack
    #     #attack
    #     chosenAttack, result = playerAI.AIAttack() #chosenAttack will be the string of which attack was used, result was whether it worked or not
    #     #display 3 second popup window of which attack was chosen and whether it worked
    #     #checkForWin, if game over then exit this function and display victory screen
    # else if (AIMove <= 98 and playerAI.hasItem()): #8% chance to use item
    #     playerAI.useHealthPotion()
    #     #use item
    # #add 2% chance to run, need a run function to end the game

    # FOR BETA-VERSION (PROJECT 3 VERSION)
    # MAKE SOME VARIABLE/DEF THAT SAYS IF PROGMON IS IN CRITICAL CONDITION
    if(progmonP1.currentHealth == critical):    #if P1 currently set-up progmon is in critical condition - attack them
        progmonAI.AIAttack(progmonAI, progmonP1)
        #now we should display some sort of window/message for the user saying if they hit or not
        #update player's health in the UI
    elif(progmonAI.currentHealth == critical and progmonAI.bagEmpty):   #this should be the AI's last option - AI is going to die if it's hit again
        # DISPLAY SOME SORT OF MESSAGE SAYING THE THIS PLAYER CHOSE TO RUN
        pygame.quit()

    elif(progmonAI.currentHealth == critical):  #if AI is low, it will use potion
        progmonAI.useHealthPotion()

    else:   # if progmonP1 is not low and AI is not low, then all we can do is attack the other player
        progmonAI.AIAttack(progmonAI, progmonP1)
        #now we should display some sort of window/message for the user saying if they hit or not
        #update player's health in the UI

    playerTurn()    #after turn is over, let the player go

# MAIN
if __name__ == "__main__":
    gameState = "startScreen"
    handleScreen(gameState) # LOADS THE START SCREEN

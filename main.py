import random
import pygame
from fireDragon import FireDragon
from electricCat import ElectricCat

# INITIALIZE PYGAME AND GLOBAL DISPLAY VARIABLES
pygame.init()
displayWidth = 1080
displayHeight = 720
display = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('EECS448 Project 3: Progmon Battle Simulator')

# GLOBAL TEXT OBJECT VARIABLES
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
font = pygame.font.Font('freesansbold.ttf', 32)
smallText = pygame.font.Font('freesansbold.ttf', 36)
mediumText = pygame.font.Font('freesansbold.ttf', 48)
largeText = pygame.font.Font('freesansbold.ttf', 65)

# GLOBAL VARIABLES
gameState = ""
playerMove = ""
global myP1
progmonP1 = ""
progmonNameP1 = ""
global myAI
progmonAI = ""
progmonNameAI = ""

# HANDLES PYGAME EVENTS
def eventHandler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame()
        pygame.display.update()

# QUITS THE GAME
def quitGame():
    print("Quitting...")
    pygame.quit()
    quit()

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
    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE
    if displayWidth * 0.45 + 110 > mouse[0] > displayWidth * 0.45 and displayHeight * 0.805 + 40 > mouse[1] > displayHeight * 0.805: # VALID LOCATION OF PLAY BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.45, displayHeight * 0.805, 110, 40), 5) # BOX AROUND PLAY ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if progmonP1 != "" and progmonAI != "":
                if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.45, displayHeight * 0.805, 110, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PLAY BUTTON
                    handleScreen("fightScreen")
            else:
                if progmonP1 == "":
                    print("ERROR: Player 1 needs to select a Progmon to play with.")
                elif progmonAI == "":
                    print("ERROR: Player AI needs to select a Progmon to play with.")

# TRACKS IF PLAYER 1'S PROGMON BUTTONS ARE CLICKED
def trackProgmonButtons_P1():
    global progmonP1
    global myP1
    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE
    if displayWidth * 0.16 + 200 > mouse[0] > displayWidth * 0.16 and displayHeight * 0.1 + 40 > mouse[1] > displayHeight * 0.1: # VALID LOCATION OF PLAYER 1'S ELECTRICCAT BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.16, displayHeight * 0.1, 200, 40), 5) # BOX AROUND PLAYER 1'S ELECTRICCAT ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.16, displayHeight * 0.1, 200, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PLAYER 1'S ELECTRICCAT BUTTON
                myP1 = ElectricCat()
                progmonP1 = "ElectricCat"
                # print("progmonP1 =", progmonP1) # TESTER CODE
    elif displayWidth * 0.16 + 190 > mouse[0] > displayWidth * 0.16 and displayHeight * 0.223 + 40 > mouse[1] > displayHeight * 0.223: # VALID LOCATION OF PLAYER 1'S FIREDRAGON BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.16, displayHeight * 0.223, 190, 40), 5) # BOX AROUND PLAYER 1'S FIREDRAGON ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.16, displayHeight * 0.223, 190, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PLAYER 1'S FIREDRAGON BUTTON
                myP1 = FireDragon()
                progmonP1 = "FireDragon"
                # print("progmonP1 =", progmonP1) # TESTER CODE

# TRACKS IF PLAYER AI'S PROGMON BUTTONS ARE CLICKED
def trackProgmonButtons_AI():
    global progmonAI
    global myAI
    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE
    if displayWidth * 0.68 + 200 > mouse[0] > displayWidth * 0.68 and displayHeight * 0.1 + 40 > mouse[1] > displayHeight * 0.1: # VALID LOCATION OF PLAYER AI'S ELECTRICCAT BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.68, displayHeight * 0.1, 200, 40), 5) # BOX AROUND PLAYER AI'S ELECTRICCAT ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.68, displayHeight * 0.1, 200, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PLAYER AI'S ELECTRICCAT BUTTON
                myAI = ElectricCat()
                progmonAI = "ElectricCat"
                # print("progmonAI =", progmonAI) # TESTER CODE
    elif displayWidth * 0.68 + 190 > mouse[0] > displayWidth * 0.68 and displayHeight * 0.223 + 40 > mouse[1] > displayHeight * 0.223: # VALID LOCATION OF PLAYER AI'S FIREDRAGON BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.68, displayHeight * 0.223, 190, 40), 5) # BOX AROUND PLAYER AI'S FIREDRAGON ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.68, displayHeight * 0.223, 190, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PLAYER AI'S FIREDRAGON BUTTON
                myAI = FireDragon()
                progmonAI = "FireDragon"
                # print("progmonAI =", progmonAI) # TESTER CODE

# (UNFINISHED - PROJECT 4) TRACKS IF BATTLE MENU BUTTONS ARE CLICKED
def trackBattleMenuButtons():
    global playerMove
    pygame.draw.rect(display, BLACK, (displayWidth * 0.62, displayHeight * 0.79, 370, 120), 5) # BOX AROUND BATTLE MENU OPTIONS
    pygame.draw.rect(display, BLACK, (displayWidth * 0.06, displayHeight * 0.065, 350, 100), 5) # BOX AROUND PLAYER 1'S PROGMON NAME AND HEALTH
    pygame.draw.rect(display, BLACK, (displayWidth * 0.6, displayHeight * 0.065, 350, 100), 5) # BOX AROUND PLAYER AI'S PROGMON NAME AND HEALTH
    pygame.draw.rect(display, BLACK, (displayWidth * 0.06, displayHeight * 0.79, 450, 100), 5) # BOX AROUND USER INPUT PROMPT MESSAGE
    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE
    if displayWidth * 0.665 + 110 > mouse[0] > displayWidth * 0.665 and displayHeight * 0.805 + 40 > mouse[1] > displayHeight * 0.805: # VALID LOCATION OF FIGHT BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.665, displayHeight * 0.805, 110, 40), 5) # BOX AROUND FIGHT ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.665, displayHeight * 0.805, 110, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR FIGHT BUTTON
                playerMove = "FIGHT"
                # (UNFINISHED - PROJECT 4) CALL A FUNCTION TO DISPLAY ATTACK OPTIONS
    elif displayWidth * 0.63 + 180 > mouse[0] > displayWidth * 0.63 and displayHeight * 0.88 + 40 > mouse[1] > displayHeight * 0.88: # VALID LOCATION OF PROGMON BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.63, displayHeight * 0.88, 180, 40), 5) # BOX AROUND PROGMON ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.63, displayHeight * 0.88, 180, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PROGMON BUTTON
                playerMove = "PROGMON"
                # (UNFINISHED - PROJECT 4) CALL A FUNCTION TO DISPLAY PROGMON SWITCH OPTIONS
    elif displayWidth * 0.87 + 80 > mouse[0] > displayWidth * 0.87 and displayHeight * 0.805 + 40 > mouse[1] > displayHeight * 0.805: # VALID LOCATION OF BAG BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.87, displayHeight * 0.805, 80, 40), 5) # BOX AROUND BAG ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.87, displayHeight * 0.805, 80, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR BAG BUTTON
                playerMove = "BAG"
                # (UNFINISHED - PROJECT 4) CALL A FUNCTION TO DISPLAY BAG ITEM OPTIONS
    elif displayWidth * 0.865 + 95 > mouse[0] > displayWidth * 0.865 and displayHeight * 0.88 + 40 > mouse[1] > displayHeight * 0.88: # VALID LOCATION OF QUIT BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.865, displayHeight * 0.88, 95, 40), 5) # BOX AROUND QUIT ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.865, displayHeight * 0.88, 95, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR QUIT BUTTON
                quitGame()

# (UNFINISHED - PROJECT 4) HANDLES CONTROL OF THE GAMESTATE'S
def handleScreen(gameState):
    global myP1
    global progmonNameP1
    global myAI
    global progmonNameAI
    if gameState == "startScreen" or gameState == "fightScreen":
        while gameState == "startScreen":
            eventHandler()
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

            # DISPLAY TEXT OBJECTS AND IMAGES
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

        while gameState == "fightScreen":
            eventHandler()
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

            # (UNFINISHED - PROJECT 4) CREATE HEALTH BAR FOR PLAYER 1'S PROGMON
            progmonHealthP1 = myP1.getCurrentHealth()
            # print("progmonHealthP1 =", progmonHealthP1) # TESTER CODE
            textHealthP1 = font.render(str(progmonHealthP1), True, BLACK, None)
            textHealthP1_RECT = textHealthP1.get_rect()
            textHealthP1_RECT.center = (displayWidth / 4.5, displayHeight / 6)

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

            # (UNFINISHED - PROJECT 4) CREATE HEALTH BAR FOR PLAYER AI'S PROGMON
            progmonHealthAI = myAI.getCurrentHealth()
            # print("progmonHealthAI =", progmonHealthAI) # TESTER CODE
            textHealthAI = font.render(str(progmonHealthAI), True, BLACK, None)
            textHealthAI_RECT = textHealthAI.get_rect()
            textHealthAI_RECT.center = (displayWidth / 1.3, displayHeight / 6)

            # CREATE BATTLE MENU OPTIONS
            textFight, textFight_RECT = createTextObject("FIGHT", largeText)
            textFight_RECT.center = (displayWidth / 1.4, displayHeight / 1.2)
            textBag, textBag_RECT = createTextObject("BAG", largeText)
            textBag_RECT.center = (displayWidth / 1.1, displayHeight / 1.2)
            textProgmon, textProgmon_RECT = createTextObject("PROGMON", largeText)
            textProgmon_RECT.center = (displayWidth / 1.4, displayHeight / 1.1)
            textQuit, textQuit_RECT = createTextObject("QUIT", largeText)
            textQuit_RECT.center = (displayWidth / 1.1, displayHeight / 1.1)

            # CREATE USER INPUT PROMPT MESSAGE
            textUserPrompt, textUserPrompt_RECT = createTextObject("What would you like to do?", largeText)
            textUserPrompt_RECT.center = (displayWidth / 3.7, displayHeight / 1.2)

            display.fill(WHITE) # MAKES BACKGROUND OF FIGHT SCREEN WHITE
            display.blit(progmonImageP1, progmonImageP1_RECT) # DISPLAYS ElectricCat IMAGE FOR PLAYER 1
            display.blit(textNameP1, textNameP1_RECT) # DISPLAYS PLAYER 1'S NAME
            display.blit(textProgmonP1, textProgmonP1_RECT) # DISPLAYS PLAYER 1'S PROGMON NAME
            display.blit(textHealthP1, textHealthP1_RECT) # DISPLAYS PLAYER 1'S PROGMON HEALTH
            display.blit(progmonImageAI, progmonImageAI_RECT) # DISPLAYS ElectricCat IMAGE FOR PLAYER AI
            display.blit(textNameAI, textNameAI_RECT) # DISPLAYS PLAYER AI'S NAME
            display.blit(textProgmonAI, textProgmonAI_RECT) # DISPLAYS PLAYER AI'S PROGMON NAME
            display.blit(textHealthAI, textHealthAI_RECT) # DISPLAYS PLAYER AI'S PROGMON HEALTH
            display.blit(textFight, textFight_RECT) # DISPLAYS FIGHT BATTLE OPTION
            display.blit(textBag, textBag_RECT) # DISPLAYS BAG BATTLE OPTION
            display.blit(textProgmon, textProgmon_RECT) # DISPLAYS PROGMON BATTLE OPTION
            display.blit(textQuit, textQuit_RECT) # DISPLAYS QUIT BATTLE OPTION
            display.blit(textUserPrompt, textUserPrompt_RECT) # DISPLAYS USER PROMPT MESSAGE

            trackBattleMenuButtons()
            playerTurn()

# (UNFINISHED) HANDLES ALL FUNCTIONS THAT OCCUR DURING PLAYER 1'S TURN
def playerTurn():
    # WILL CONTAIN EVERYTHING DONE IN ONE TURN (WILL CALL OTHER FUNCTIONS SUCH AS attack, attack_AI, checkForWin, etc.)
    global playerMove
    global progmonNameP1
    global progmonNameAI
    # print("playerMove =", playerMove) # TESTER CODE
    if(playerMove == "FIGHT"):
        p1Attack = random.randint(0,5)
        # print("p1Attack =", p1Attack) # TESTER CODE
        if(progmonP1 == "FireDragon"):
            if(p1Attack == 1):
                print("Player 1's", progmonNameP1, "used Roar!")
                myP1.RoarAttack(myAI)
            elif(p1Attack == 2):
                print("Player 1's", progmonNameP1, "used Claw Swipe!")
                myP1.ClawSwipeAttack(myAI)
            elif(p1Attack == 3):
                print("Player 1's", progmonNameP1, "used Fire Breath!")
                myP1.FireBreathAttack(myAI)
            elif(p1Attack == 4):
                print("Player 1's", progmonNameP1, "used Tail Whip!")
                myP1.TailWhipAttack(myAI)
        elif(progmonP1 == "ElectricCat"):
            if(p1Attack == 1):
                print("Player 1's", progmonNameP1, "used Lightning Bolt!")
                myP1.LightningBoltAttack(myAI)
            elif(p1Attack == 2):
                print("Player 1's", progmonNameP1, "used Electric Scratch!")
                myP1.ElectricScratchAttack(myAI)
            elif(p1Attack == 3):
                print("Player 1's", progmonNameP1, "used Energy Beam!")
                myP1.EnergyBeamAttack(myAI)
            elif(p1Attack == 4):
                print("Player 1's", progmonNameP1, "used Bite!")
                myP1.BiteAttack(myAI)
        if(myAI.checkAlive() != True):
            print("Player AI's", progmonNameAI, "has fainted. You win!\n")
            quitGame()
    # (UNFINISHED - PROJECT 4) ADD MORE ITEMS TO THE BAG PLUS NEED ABILITY TO SELECT THE ITEM YOU WANT TO USE
    elif(playerMove == "BAG"):
        if (myP1.bagEmpty()):
            print("Player 1 has nothing in their Bag.\n")
        else:
            myP1.useHealthPotion()
            print("Player 1 has used a Health Potion!\n") # TESTER CODE
            # AIBagTrack += 1 #lets AI track how many items you've use from your bag so it can be more AI-ish
    # (UNFINISHED - PROJECT 4) ALLOW PLAYER 1 THE ABILITY TO CHANGE THEIR PROGMON DURING THE BATTLE
    elif(playerMove == "PROGMON"):
        # progmonP1.switchProgmon()
        print("PROGMON SWITCHING IS NOT AVAILABLE AT THIS TIME")

    # (UNFINISHED - PROJECT 3) AFTER PLAYER 1'S TURN IS OVER, LET PLAYER AI GO
    AITurn()

def AITurn():
    global myP1
    global myAI
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
    critical = 80
    if(myP1.currentHealth <= critical):    #if P1 currently set-up progmon is in critical condition - attack them
        myAI.AIAttack(myP1)
        #now we should display some sort of window/message for the user saying if they hit or not
        #update player's health in the UI
        if(myAI.checkAlive() != True):
            print("P1 progmon has died")
            quitGame()
    elif(myAI.currentHealth <= critical and myAI.bagEmpty):   #this should be the AI's last option - AI is going to die if it's hit again
        # DISPLAY SOME SORT OF MESSAGE SAYING THE THIS PLAYER CHOSE TO RUN
        quitGame()

    elif(myAI.currentHealth <= critical):  #if AI is low, it will use potion
        myAI.useHealthPotion()

    else:   # if progmonP1 is not low and AI is not low, then all we can do is attack the other player
        myAI.AIAttack(myP1)
        #now we should display some sort of window/message for the user saying if they hit or not
        #update player's health in the UI

    playerTurn()    #after turn is over, let the player go

# MAIN
if __name__ == "__main__":
    eventHandler()
    gameState = "startScreen"
    handleScreen(gameState) # LOADS THE START SCREEN

"""
BUG LIST:
    > (BEAU) When a Progmon faints, their Health and Health Bar does not update to display 0 HP
    > "Player 1's PROGMON has fainted. You win!" is not displaying before controlScreen("endScreen")
    > "Player AI's PROGMON has fainted. You win!" is not displaying before controlScreen("endScreen")
    > When Defense Boost is active for either Player, the amount of damage that is printed to Terminal is not taking into account the -10 damage from the Defense Boost

TODO LIST:
    > (QUI) Create End Screen
        --> Sprites on End Screen should be the large versions
    > (CAMERON) Add sound effects
    > (ROB) Adjust positioning of Hit Marker sprite for both Players
    > (ROB/BEAU) Create a Test Suite
        --> create testSuite.py (should be similar to EECS448 LAB06 - TESTING LAB)
            --> from main import *
                --> TO RUN: python3 testSuite.py
                    --> Output our tests to Terminal
        --> Update the Bug List
    > (ROB) Clean up code in main.py and progmon.py
    > (ROB) Document code in main.py and progmon.py
        --> Copy & Paste Progmon classes into their own files
    > (BEAU) Use Sphinx documentation generator to create HTML files
    > (COLE) User Manual
    > (COLE) Gantt Chart
    > (ROB) Meeting Logs
    > (QUI) UML Diagrams
    > (CAMERON) Product Backlog + Sprint Backlog
    > Deployment Plan
    > Maintenance Plan
"""
import random
import pygame
import pygame.gfxdraw
from progmon import Progmon, FireDragon, ElectricCat, WaterTurtle, FinalBoss

# INITIALIZE PYGAME AND GLOBAL DISPLAY/TEXT OBJECT VARIABLES
pygame.init()
pygame.display.set_caption('EECS448 Project 4: Progmon Battle Simulator')
WIDTH = 1080
HEIGHT = 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
MINI = pygame.font.Font('freesansbold.ttf', 24)
SMALL = pygame.font.Font('freesansbold.ttf', 32)
MEDIUM = pygame.font.Font('freesansbold.ttf', 36)
LARGE = pygame.font.Font('freesansbold.ttf', 42)
HUGE = pygame.font.Font('freesansbold.ttf', 50)
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(160, 219, 154)
LIGHT_GREEN = pygame.Color(0, 200, 0)

# GLOBAL VARIABLES
gameState = ""
global myP1
progmonP1 = ""
progmonNameP1 = ""
global myAI
progmonAI = ""
progmonNameAI = ""
winner = ""
totalAttackPlayerP1 = 0
totalAttackPlayerAI = 0
totalHitPlayerP1 = 0
totalHitPlayerAI = 0
totalMissedPlayerP1 = 0
totalMissedPlayerAI = 0

def eventHandler():
    """
    Handles Pygame events
    Args:
        None
    Returns:
        None
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame()
        pygame.display.update()

def quitGame():
    """
    Quits Pygame
    Args:
        None
    Returns:
        None
    """
    print("Quitting...\n")
    pygame.quit()
    quit()

def displayButton(textToDisplay, fontToUse, colorToUse, x, y):
    """
    Creates a button and displays it on the screen
    Args:
        textToDisplay (string) - text to be displayed
        fontToUse (string) - font of the text
        colorToUse (string) - color of the text
        x (int) - center x-coordinate
        y (int) - center y-coordinate
    Returns:
        buttonRectangle (pygame.Rect) - the created buttons rectangle
    """
    buttonSurface = fontToUse.render(textToDisplay, True, colorToUse)
    buttonRectangle = buttonSurface.get_rect()
    buttonRectangle.center = (x, y)
    SCREEN.blit(buttonSurface, buttonRectangle)
    return buttonRectangle

def displayImage(imageToDisplay, x, y):
    """
    Loads an image and displays it on the screen
    Args:
        imageToDisplay (string) - image to be displayed
        x (int) - center x-coordinate
        y (int) - center y-coordinate
    Returns:
        None
    """
    img = pygame.image.load(imageToDisplay)
    imgRectangle = img.get_rect()
    imgRectangle.center = (x, y)
    SCREEN.blit(img, imgRectangle)

def displayText(textToDisplay, fontToUse, colorToUse, x, y):
    """
    Creates a text object and displays it on the screen
    Args:
        textToDisplay (string) - text to be displayed
        fontToUse (string) - font of the text
        colorToUse (string) - color of the text
        x (int) - center x-coordinate
        y (int) - center y-coordinate
    Returns:
        None
    """
    textSurface = fontToUse.render(textToDisplay, True, colorToUse)
    textRectangle = textSurface.get_rect()
    textRectangle.center = (x, y)
    SCREEN.blit(textSurface, textRectangle)

def mouseClick(surfaceRect):
    """
    Checks if mouse-click is within the bounds of a surfaceRect
    Args:
        surfaceRect (Pygame.Rect) - surface object that is being checked
    Returns:
        (bool) - True if mouse-click is in surfaceRect, otherwise False
    """
    mousePosition = pygame.mouse.get_pos() # GETS (x, y) COORDINATE OF MOUSE
    if surfaceRect.collidepoint(mousePosition):
        pygame.draw.rect(SCREEN, RED, surfaceRect, 3) # UNFILLLED BOX AROUND surfaceRect
        if pygame.mouse.get_pressed() == (1, 0, 0):
            pygame.time.delay(500) # WAIT TO PREVENT MULTIPLE BUTTON CLICKS
            return True
    return False

def startScreen():
    """
    displays and tracks all objects on the Start Screen
    Args:
        None
    Returns:
        None
    """
    global gameState
    global myP1
    global progmonP1
    global progmonNameP1
    global myAI
    global progmonAI
    global progmonNameAI

    # DISPLAY IMAGES
    displayImage('Sprites/startScreen.png', WIDTH * .5, HEIGHT * .5) # BACKGROUND

    displayImage('Sprites/smallElectricCat.png', WIDTH / 9, HEIGHT / 7.5) # PLAYER 1
    displayImage('Sprites/smallFireDragon.png', WIDTH / 9, HEIGHT / 4) # PLAYER 1
    displayImage('Sprites/smallWaterTurtle.png', WIDTH / 9, HEIGHT / 2.7) # PLAYER 1
    displayImage('Sprites/smallFinalBoss.png', WIDTH / 8.6, HEIGHT / 2.08) # PLAYER 1

    displayImage('Sprites/smallElectricCat.png', WIDTH / 1.6, HEIGHT / 7.5) # PLAYER AI
    displayImage('Sprites/smallFireDragon.png', WIDTH / 1.6, HEIGHT / 4) # PLAYER AI
    displayImage('Sprites/smallWaterTurtle.png', WIDTH / 1.6, HEIGHT / 2.7) # PLAYER AI
    displayImage('Sprites/smallFinalBoss.png', WIDTH / 1.577, HEIGHT / 2.08) # PLAYER AI

    # DRAW TO SCREEN
    pygame.draw.rect(SCREEN, BLACK, (WIDTH * .15, HEIGHT * .1, 220, 320), 0) # FILLED BOX FOR PLAYER 1 PROGMON OPTIONS
    pygame.draw.rect(SCREEN, BLACK, (WIDTH * .67, HEIGHT * .1, 220, 320), 0) # FILLED BOX FOR PLAYER AI PROGMON OPTIONS

    # DISPLAY TEXT OBJECTS
    displayText("Player 1", LARGE, WHITE, WIDTH / 4, HEIGHT / 19)  # PLAYER 1
    displayText("Player AI", LARGE, WHITE, WIDTH / 1.3, HEIGHT / 19) # PLAYER AI

    # DISPLAY BUTTONS
    btnPlay = displayButton("PLAY", MEDIUM, WHITE, WIDTH * .5, HEIGHT * .9)

    btnProgmon1_P1 = displayButton("Electric Cat", SMALL, WHITE, WIDTH / 4, HEIGHT / 7.5) # PLAYER 1
    btnProgmon2_P1 = displayButton("Fire Dragon", SMALL, WHITE, WIDTH / 4, HEIGHT / 4) # PLAYER 1
    btnProgmon3_P1 = displayButton("Water Turtle", SMALL, WHITE, WIDTH / 4, HEIGHT / 2.7) # PLAYER 1
    btnProgmon4_P1 = displayButton("Final Boss", SMALL, WHITE, WIDTH / 4, HEIGHT / 2) # PLAYER 1

    btnProgmon1_AI = displayButton("Electric Cat", SMALL, WHITE, WIDTH / 1.3, HEIGHT / 7.5) # PLAYER AI
    btnProgmon2_AI = displayButton("Fire Dragon", SMALL, WHITE, WIDTH / 1.3, HEIGHT / 4) # PLAYER AI
    btnProgmon3_AI = displayButton("Water Turtle", SMALL, WHITE, WIDTH / 1.3, HEIGHT / 2.7) # PLAYER AI
    btnProgmon4_AI = displayButton("Final Boss", SMALL, WHITE, WIDTH / 1.3, HEIGHT / 2) # PLAYER AI

    # TRACK PLAYER 1 BUTTONS
    if mouseClick(btnProgmon1_P1):
        myP1 = ElectricCat()
        progmonP1 = "ElectricCat"
        progmonNameP1 = "Electric Cat"
    elif mouseClick(btnProgmon2_P1):
        myP1 = FireDragon()
        progmonP1 = "FireDragon"
        progmonNameP1 = "Fire Dragon"
    elif mouseClick(btnProgmon3_P1):
        myP1 = WaterTurtle()
        progmonP1 = "WaterTurtle"
        progmonNameP1 = "Water Turtle"
    elif mouseClick(btnProgmon4_P1):
        myP1 = FinalBoss()
        progmonP1 = "FinalBoss"
        progmonNameP1 = "Final Boss"

    # TRACK PLAYER AI BUTTONS
    if mouseClick(btnProgmon1_AI):
        myAI = ElectricCat()
        progmonAI = "ElectricCat"
        progmonNameAI = "Electric Cat"
    elif mouseClick(btnProgmon2_AI):
        myAI = FireDragon()
        progmonAI = "FireDragon"
        progmonNameAI = "Fire Dragon"
    elif mouseClick(btnProgmon3_AI):
        myAI = WaterTurtle()
        progmonAI = "WaterTurtle"
        progmonNameAI = "Water Turtle"
    elif mouseClick(btnProgmon4_AI):
        myAI = FinalBoss()
        progmonAI = "FinalBoss"
        progmonNameAI = "Final Boss"

    # TRACK PLAY BUTTON
    if mouseClick(btnPlay):
        if progmonP1 != "" and progmonAI != "":
            gameState = "fightScreen"
            controlScreen(gameState)
        else:
            if progmonP1 == "":
                print("ERROR: Player 1 needs to select a Progmon")
            elif progmonAI == "":
                print("ERROR: Player AI needs to select a Progmon")

def fightScreen():
    """
    Displays and tracks all objects on the Fight Screen
    Args:
        None
    Returns:
        None
    """
    global gameState
    global myP1
    global progmonNameP1
    global myAI
    global progmonNameAI

    # DISPLAY IMAGES
    displayImage('Sprites/fightScreen.png', WIDTH * .5, HEIGHT * .5) # BACKGROUND

    if progmonP1 == "ElectricCat":
        displayImage('Sprites/largeElectricCat.png', WIDTH * .2, HEIGHT * .45) # PLAYER 1
    elif progmonP1 == "FireDragon":
        displayImage('Sprites/largeFireDragon.png', WIDTH * .2, HEIGHT * .45) # PLAYER 1
    elif progmonP1 == "WaterTurtle":
        displayImage('Sprites/largeWaterTurtle.png', WIDTH * .2, HEIGHT * .45) # PLAYER 1
    elif progmonP1 == "FinalBoss":
        displayImage('Sprites/largeFinalBoss.png', WIDTH * .2, HEIGHT * .45) # PLAYER 1

    if myP1.getStunStatus():
        displayImage('Sprites/stunIcon.png', WIDTH * .06, HEIGHT * .25) # PLAYER 1
    if myP1.getStatBoost():
        displayImage('Sprites/boostIcon.png', WIDTH * .13, HEIGHT * .25) # PLAYER 1
    if myP1.getDefenseBoost():
        displayImage('Sprites/defenseIcon.png', WIDTH * .2, HEIGHT * .25) # PLAYER 1

    if progmonAI == "ElectricCat":
        displayImage('Sprites/largeElectricCat.png', WIDTH * .8, HEIGHT * .45) # PLAYER AI
    elif progmonAI == "FireDragon":
        displayImage('Sprites/largeFireDragon.png', WIDTH * .8, HEIGHT * .45) # PLAYER AI
    elif progmonAI == "WaterTurtle":
        displayImage('Sprites/largeWaterTurtle.png', WIDTH * .8, HEIGHT * .45) # PLAYER AI
    elif progmonAI == "FinalBoss":
        displayImage('Sprites/largeFinalBoss.png', WIDTH * .8, HEIGHT * .45) # PLAYER AI

    if myAI.getStunStatus():
        displayImage('Sprites/stunIcon.png', WIDTH * .72, HEIGHT * .25) # PLAYER AI
    if myAI.getStatBoost():
        displayImage('Sprites/boostIcon.png', WIDTH * .79, HEIGHT * .25) # PLAYER AI
    if myAI.getDefenseBoost():
        displayImage('Sprites/defenseIcon.png', WIDTH * .86, HEIGHT * .25) # PLAYER AI

    # DRAW TO SCREEN
    pygame.draw.rect(SCREEN, WHITE, (WIDTH * .037, HEIGHT * .92, 1000, 50), 0) # FILLED BOX FOR BATTLE MENU BUTTONS

    pygame.draw.rect(SCREEN, WHITE, (WIDTH * .05, HEIGHT * .14, 200, 40), 5) # UNFILLED BOX FOR PLAYER 1'S PROGMON HEALTH BAR
    pygame.draw.rect(SCREEN, RED, (WIDTH * .052, HEIGHT * .141, 196, 37), 0) # FILLED BOX FOR PLAYER 1'S PROGMON HEALTH BAR
    pygame.draw.rect(SCREEN, LIGHT_GREEN, (WIDTH * .052, HEIGHT * .141, 196 * (myP1.getCurrentHealth() / myP1.getHp()), 37), 0) # FILLED BOX FOR PLAYER 1'S PROGMON HEALTH BAR
    pygame.draw.rect(SCREEN, WHITE, (WIDTH * .037, HEIGHT * .71, 480, 140), 0) # FILLED BOX FOR PLAYER 1'S MESSAGES

    pygame.draw.rect(SCREEN, WHITE, (WIDTH * .699, HEIGHT * .14, 200, 40), 5) # UNFILLED BOX FOR PLAYER AI'S PROGMON HEALTH BAR
    pygame.draw.rect(SCREEN, RED, (WIDTH * .701, HEIGHT * .141, 196, 37), 0) # FILLED BOX FOR PLAYER AI'S PROGMON HEALTH BAR
    pygame.draw.rect(SCREEN, LIGHT_GREEN, (WIDTH * .701, HEIGHT * .141, 196 * (myAI.getCurrentHealth() / myAI.getHp()), 37), 0) # FILLED BOX FOR PLAYER AI'S PROGMON HEALTH BAR
    pygame.draw.rect(SCREEN, WHITE, (WIDTH * .518, HEIGHT * .71, 480, 140), 0) # FILLED BOX FOR PLAYER AI'S MESSAGES

    # DISPLAY TEXT OBJECTS
    displayText("Player 1", MEDIUM, WHITE, WIDTH * .175, HEIGHT * .035) # PLAYER 1
    displayText(progmonNameP1, MEDIUM, WHITE, WIDTH * .175, HEIGHT * .105) # PLAYER 1
    displayText(str(myP1.getCurrentHealth()), SMALL, WHITE, WIDTH * .28, HEIGHT * .168) # PLAYER 1

    displayText("Player AI", MEDIUM, WHITE, WIDTH * .825, HEIGHT * .035) # PLAYER AI
    displayText(progmonNameAI, MEDIUM, WHITE, WIDTH * .825, HEIGHT * .105) # PLAYER AI
    displayText(str(myAI.getCurrentHealth()), SMALL, WHITE, WIDTH * .925, HEIGHT * .168) # PLAYER AI

    # DISPLAY BUTTONS
    btnFight = displayButton("FIGHT", SMALL, BLACK, WIDTH * 0.2, HEIGHT * 0.955)
    btnBag = displayButton("BAG", SMALL, BLACK, WIDTH * 0.4, HEIGHT * 0.955)
    btnProgmon = displayButton("PROGMON", SMALL, BLACK, WIDTH * 0.6, HEIGHT * 0.955)
    btnQuit = displayButton("QUIT", SMALL, BLACK, WIDTH * 0.8, HEIGHT * 0.955)

    # HANDLE TURN FOR PLAYER 1
    if myP1.getStunStatus() == False:
        displayText("What will you do?", MINI, BLACK, WIDTH * .25, HEIGHT * .75)

        # TRACK BATTLE MENU BUTTONS
        if mouseClick(btnFight):
            gameState = "fightMenu"
            controlScreen(gameState)
        elif mouseClick(btnBag):
            if myP1.bagEmpty() == False:
                gameState = "bagMenu"
                controlScreen(gameState)
            else:
                print("Your Bag is empty!")
                displayText("Your Bag is empty!", MINI, BLACK, WIDTH * .25, HEIGHT * .8)
                pygame.time.wait(1600) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
                gameState = "fightScreen"
                controlScreen(gameState)
        elif mouseClick(btnProgmon):
            gameState = "progmonMenu"
            controlScreen(gameState)
        elif mouseClick(btnQuit):
            quitGame()
    elif myP1.getStunStatus() == True:
        displayText(("{} has stunned {}!".format(progmonNameAI, progmonNameP1)), MINI, BLACK, WIDTH * .25, HEIGHT * .75)
        myP1.stunned = False
        print("{} has stunned {}!".format(progmonNameAI, progmonNameP1))
        pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
        AITurn()

def fightMenu():
    """
    Displays and tracks the Fight Menu for Player 1 after "FIGHT" has been clicked
    Args:
        None
    Returns:
        None
    """
    global gameState
    global myP1
    global progmonP1
    global progmonNameP1
    global myAI
    global winner
    global totalAttackPlayerP1
    global totalHitPlayerP1
    global totalMissedPlayerP1

    # DRAW TO SCREEN
    pygame.draw.rect(SCREEN, WHITE, (WIDTH * .037, HEIGHT * .92, 1000, 50), 0) # FILLED BOX FOR FIGHT MENU BUTTONS
    pygame.draw.rect(SCREEN, WHITE, (WIDTH * .037, HEIGHT * .71, 480, 140), 0) # FILLED BOX FOR PLAYER 1 MESSAGES

    # DISPLAY TEXT OBJECTS
    displayText("Which attack would you like to use?", MINI, BLACK, WIDTH * .25, HEIGHT * .75)

    # HANDLE TURN FOR PLAYER 1
    if myAI.checkAlive() == False:
        winner = "Player 1"
        print("Player AI's {} has fainted. You win!".format(progmonNameAI))
        displayText(("Player AI's {} has fainted. You win!".format(progmonNameAI)), MINI, BLACK, WIDTH * .25, HEIGHT * .8)
        pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
        gameState = "endScreen"
        controlScreen(gameState)
    else:
        # DISPLAY FIGHT MENU BUTTONS
        attackList = myP1.getAttackList()
        if len(attackList) == 4:
            btnAttack1 = displayButton(str(attackList[0]), MINI, BLACK, WIDTH * .2, HEIGHT * .955)
            btnAttack2 = displayButton(str(attackList[1]), MINI, BLACK, WIDTH * .4, HEIGHT * .955)
            btnAttack3 = displayButton(str(attackList[2]), MINI, BLACK, WIDTH * .6, HEIGHT * .955)
            btnAttack4 = displayButton(str(attackList[3]), MINI, BLACK, WIDTH * .8, HEIGHT * .955)

        # TRACK FIGHT MENU BUTTONS
        if mouseClick(btnAttack1):
            print("Player 1's {} used {}!".format(progmonNameP1, attackList[0]))
            attackHit = myP1.attack1(myAI) # ATTACK HIT / MISS TRACKER
            displayText(("{} used {}!".format(progmonNameP1, attackList[0])), MINI, BLACK, WIDTH * .25, HEIGHT * .8)
            totalAttackPlayerP1 = totalAttackPlayerP1 + 1  # endScreen() total P1 attacked
            pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
            if attackHit[0] == True:
                displayImage('Sprites/hitMarker.png', WIDTH * .8, HEIGHT * .45) # HIT MARKER ON PLAYER AI PROGMON
                print("{}".format(attackHit[1]))
                displayText("{}".format(attackHit[1]), MINI, BLACK, WIDTH * .25, HEIGHT * .85)
                totalHitPlayerP1 = totalHitPlayerP1 + 1  # endScreen() total P1 hit
                pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
            else:
                print("{}".format(attackHit[1]))
                displayText("{}".format(attackHit[1]), MINI, BLACK, WIDTH * .25, HEIGHT * .85)
                totalMissedPlayerP1 = totalMissedPlayerP1 + 1  # endScreen() total P1 missed
                pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE

            if myAI.checkAlive():
                AITurn()
                gameState = "fightScreen"
                controlScreen(gameState)

        if mouseClick(btnAttack2):
            print("Player 1's {} used {}!".format(progmonNameP1, attackList[1]))
            attackHit = myP1.attack2(myAI) # ATTACK HIT / MISS TRACKER
            displayText(("{} used {}!".format(progmonNameP1, attackList[1])), MINI, BLACK, WIDTH * .25, HEIGHT * .8)
            totalAttackPlayerP1 = totalAttackPlayerP1 + 1  # endScreen() total P1 attacked
            pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
            if attackHit[0] == True:
                displayImage('Sprites/hitMarker.png', WIDTH * .8, HEIGHT * .45) # HIT MARKER ON PLAYER AI PROGMON
                print("{}".format(attackHit[1]))
                displayText("{}".format(attackHit[1]), MINI, BLACK, WIDTH * .25, HEIGHT * .85)
                totalHitPlayerP1 = totalHitPlayerP1 + 1  # endScreen() total P1 hit
                pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
            else:
                print("{}".format(attackHit[1]))
                displayText("{}".format(attackHit[1]), MINI, BLACK, WIDTH * .25, HEIGHT * .85)
                totalMissedPlayerP1 = totalMissedPlayerP1 + 1  # endScreen() total P1 missed
                pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE

            if myAI.checkAlive():
                AITurn()
                gameState = "fightScreen"
                controlScreen(gameState)

        if mouseClick(btnAttack3):
            print("Player 1's {} used {}!".format(progmonNameP1, attackList[2]))
            attackHit = myP1.attack3(myAI) # ATTACK HIT / MISS TRACKER
            displayText(("{} used {}!".format(progmonNameP1, attackList[2])), MINI, BLACK, WIDTH * .25, HEIGHT * .8)
            totalAttackPlayerP1 = totalAttackPlayerP1 + 1  # endScreen() total P1 attacked
            pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
            if attackHit[0] == True:
                displayImage('Sprites/hitMarker.png', WIDTH * .8, HEIGHT * .45) # HIT MARKER ON PLAYER AI PROGMON
                print("{}".format(attackHit[1]))
                displayText("{}".format(attackHit[1]), MINI, BLACK, WIDTH * .25, HEIGHT * .85)
                totalHitPlayerP1 = totalHitPlayerP1 + 1  # endScreen() total P1 hit
                pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
            else:
                print("{}".format(attackHit[1]))
                displayText("{}".format(attackHit[1]), MINI, BLACK, WIDTH * .25, HEIGHT * .85)
                totalMissedPlayerP1 = totalMissedPlayerP1 + 1  # endScreen() total P1 missed
                pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE

            if myAI.checkAlive():
                AITurn()
                gameState = "fightScreen"
                controlScreen(gameState)

        if mouseClick(btnAttack4):
            print("Player 1's {} used {}!".format(progmonNameP1, attackList[3]))
            attackHit = myP1.attack4(myAI) # ATTACK HIT / MISS TRACKER
            displayText(("{} used {}!".format(progmonNameP1, attackList[3])), MINI, BLACK, WIDTH * .25, HEIGHT * .8)
            totalAttackPlayerP1 = totalAttackPlayerP1 + 1  # endScreen() total P1 attacked
            pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
            if attackHit[0] == True:
                displayImage('Sprites/hitMarker.png', WIDTH * .8, HEIGHT * .45) # HIT MARKER ON PLAYER AI PROGMON
                print("{}".format(attackHit[1]))
                displayText("{}".format(attackHit[1]), MINI, BLACK, WIDTH * .25, HEIGHT * .85)
                totalHitPlayerP1 = totalHitPlayerP1 + 1  # endScreen() total P1 hit
                pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
            else:
                print("{}".format(attackHit[1]))
                displayText("{}".format(attackHit[1]), MINI, BLACK, WIDTH * .25, HEIGHT * .85)
                totalMissedPlayerP1 = totalMissedPlayerP1 + 1  # endScreen() total P1 missed
                pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE

            if myAI.checkAlive():
                AITurn()
                gameState = "fightScreen"
                controlScreen(gameState)

def bagMenu():
    """
    Displays and tracks the Bag Menu for Player 1 after "BAG" has been clicked
    Args:
        None
    Returns:
        None
    """
    global gameState

    # DRAW TO SCREEN
    pygame.draw.rect(SCREEN, WHITE, (WIDTH * .037, HEIGHT * .92, 1000, 50), 0) # FILLED BOX FOR BAG MENU BUTTONS
    pygame.draw.rect(SCREEN, WHITE, (WIDTH * .037, HEIGHT * .71, 480, 140), 0) # FILLED BOX FOR PLAYER 1 MESSAGES

    # DISPLAY TEXT OBJECTS
    displayText("Which item would you like to use?", MINI, BLACK, WIDTH * .25, HEIGHT * .75)

    # DISPLAY BAG MENU BUTTONS
    if "healthPotion" in myP1.getBag():
        btnItem1 = displayButton("Health Potion", MINI, BLACK, WIDTH * .2, HEIGHT * .955)
        if mouseClick(btnItem1):
            print("Player 1 used a Health Potion!")
            myP1.useHealthPotion()
            displayText("Player 1 used a Health Potion!", MINI, BLACK, WIDTH * .25, HEIGHT * .8)
            pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
            AITurn()
            gameState = "fightScreen"
            controlScreen(gameState)

    if "statBoost" in myP1.getBag():
        btnItem2 = displayButton("Stat Boost", MINI, BLACK, WIDTH * .4, HEIGHT * .955)
        if mouseClick(btnItem2):
            print("Player 1 used a Stat Boost!")
            myP1.useStatBoost()
            displayText("Player 1 used a Stat Boost!", MINI, BLACK, WIDTH * .25, HEIGHT * .8)
            pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
            AITurn()
            gameState = "fightScreen"
            controlScreen(gameState)

    if "defenseBoost" in myP1.getBag():
        btnItem3 = displayButton("Defense Boost", MINI, BLACK, WIDTH * .6, HEIGHT * .955)
        if mouseClick(btnItem3):
            print("Player 1 used a Defense Boost")
            myP1.useDefenseBoost()
            displayText("Player 1 used a Defense Boost!", MINI, BLACK, WIDTH * .25, HEIGHT * .8)
            pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
            AITurn()
            gameState = "fightScreen"
            controlScreen(gameState)

    if "restorePotion" in myP1.getBag():
        btnItem4 = displayButton("Restore Potion", MINI, BLACK, WIDTH * .8, HEIGHT * .955)
        if mouseClick(btnItem4):
            print("Player 1 used a Restore Potion!")
            myP1.useRestorePotion()
            myP1.setCurrentHealth(myP1.hp)
            displayText("Player 1 used a Restore Potion!", MINI, BLACK, WIDTH * .25, HEIGHT * .8)
            pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
            AITurn()
            gameState = "fightScreen"
            controlScreen(gameState)

def progmonMenu():
    """
    Displays and tracks the Progmon Menu for Player 1 after "PROGMON" has been clicked
    Args:
        None
    Returns:
        None
    """
    global myP1
    global progmonP1
    global progmonNameP1
    global myAI
    global winner

    # DRAW TO SCREEN
    pygame.draw.rect(SCREEN, WHITE, (WIDTH * .037, HEIGHT * .92, 1000, 50), 0) # FILLED BOX FOR PROGMON MENU BUTTONS
    pygame.draw.rect(SCREEN, WHITE, (WIDTH * .037, HEIGHT * .71, 480, 140), 0) # FILLED BOX FOR PLAYER 1 MESSAGES

    # DISPLAY TEXT OBJECTS
    displayText("Which Progmon will you switch to?", MINI, BLACK, WIDTH * .25, HEIGHT * .75)

    # DISPLAY PROGMON MENU BUTTONS
    btnProgmon1 = displayButton("Electric Cat", MINI, BLACK, WIDTH * .2, HEIGHT * .955)
    btnProgmon2 = displayButton("Fire Dragon", MINI, BLACK, WIDTH * .4, HEIGHT * .955)
    btnProgmon3 = displayButton("Water Turtle", MINI, BLACK, WIDTH * .6, HEIGHT * .955)
    btnProgmon4 = displayButton("Final Boss", MINI, BLACK, WIDTH * .8, HEIGHT * .955)

    # TRACK PROGMON MENU BUTTONS
    if mouseClick(btnProgmon1):
        print("Player 1 is switching to Electric Cat!")
        curHp = myP1.getCurrentHealth()
        curBag = myP1.getBag()
        curStatBoost = myP1.getStatBoost()
        curDefenseBoost = myP1.getDefenseBoost()
        myP1 = ElectricCat()
        progmonP1 = "ElectricCat"
        progmonNameP1 = "Electric Cat"
        myP1.setBag(curBag)
        myP1.setStatBoost(curStatBoost)
        myP1.setDefenseBoost(curDefenseBoost)
        if curHp < myP1.getHp(): # if player had less health than new progmon's max (before the switch), reduce health
            myP1.setCurrentHealth(curHp)
        AITurn()
        gameState = "fightScreen"
        controlScreen(gameState)

    if mouseClick(btnProgmon2):
        print("Player 1 is switching to Fire Dragon!")
        curHp = myP1.getCurrentHealth()
        curBag = myP1.getBag()
        curStatBoost = myP1.getStatBoost()
        curDefenseBoost = myP1.getDefenseBoost()
        myP1 = FireDragon()
        progmonP1 = "FireDragon"
        progmonNameP1 = "Fire Dragon"
        myP1.setBag(curBag)
        myP1.setStatBoost(curStatBoost)
        myP1.setDefenseBoost(curDefenseBoost)
        if curHp < myP1.getHp(): # if player had less health than new progmon's max (before the switch), reduce health
            myP1.setCurrentHealth(curHp)
        AITurn()
        gameState = "fightScreen"
        controlScreen(gameState)

    if mouseClick(btnProgmon3):
        print("Player 1 is switching to Water Turtle!")
        curHp = myP1.getCurrentHealth()
        curBag = myP1.getBag()
        curStatBoost = myP1.getStatBoost()
        curDefenseBoost = myP1.getDefenseBoost()
        myP1 = WaterTurtle()
        progmonP1 = "WaterTurtle"
        progmonNameP1 = "Water Turtle"
        myP1.setBag(curBag)
        myP1.setStatBoost(curStatBoost)
        myP1.setDefenseBoost(curDefenseBoost)
        if curHp < myP1.getHp(): # if player had less health than new progmon's max (before the switch), reduce health
            myP1.setCurrentHealth(curHp)
        AITurn()
        gameState = "fightScreen"
        controlScreen(gameState)

    if mouseClick(btnProgmon4):
        print("Player 1 is switching to Final Boss!")
        curHp = myP1.getCurrentHealth()
        curBag = myP1.getBag()
        curStatBoost = myP1.getStatBoost()
        curDefenseBoost = myP1.getDefenseBoost()
        myP1 = FinalBoss()
        progmonP1 = "FinalBoss"
        progmonNameP1 = "Final Boss"
        myP1.setBag(curBag)
        myP1.setStatBoost(curStatBoost)
        myP1.setDefenseBoost(curDefenseBoost)
        if curHp < myP1.getHp(): # if player had less health than new progmon's max (before the switch), reduce health
            myP1.setCurrentHealth(curHp)
        AITurn()
        gameState = "fightScreen"
        controlScreen(gameState)

def endScreen():            # unfinish , still need to add variables and statistic
    global winner
    global gameState
    global progmonNameP1
    global progmonNameAI
    global totalAttackPlayerP1
    global totalAttackPlayerAI
    global totalHitPlayerP1
    global totalHitPlayerAI
    global totalMissedPlayerP1
    global totalMissedPlayerAI

    SCREEN.fill(GREEN)

    # DISPLAY TEXT OBJECTS
    displayText("{} VS {}".format(progmonNameP1, progmonNameAI), MEDIUM, BLACK, WIDTH / 2, HEIGHT * .05)
    displayText((winner + " wins!"), HUGE, BLACK, WIDTH / 2, HEIGHT * .14)

    displayText("Player 1", LARGE, BLACK, WIDTH / 4.7, HEIGHT * .28) # PLAYER 1
    displayText("Player AI", LARGE, BLACK, WIDTH / 1.3, HEIGHT * .28) # PLAYER AI

    # DISPLAY IMAGES
    if progmonP1 == "ElectricCat":
        displayImage('Sprites/smallElectricCat.png', WIDTH / 4.65, HEIGHT * .06) # PLAYER 1
    elif progmonP1 == "FireDragon":
        displayImage('Sprites/smallFireDragon.png', WIDTH / 4.65, HEIGHT * .06) # PLAYER 1
    elif progmonP1 == "WaterTurtle":
        displayImage('Sprites/smallWaterTurtle.png', WIDTH / 4.65, HEIGHT * .06) # PLAYER 1
    elif progmonP1 == "FinalBoss":
        displayImage('Sprites/smallFinalBoss.png', WIDTH / 4.65, HEIGHT * .06) # PLAYER 1

    if progmonAI == "ElectricCat":
        displayImage('Sprites/smallElectricCat.png', WIDTH / 1.26, HEIGHT * .06) # PLAYER AI
    elif progmonAI == "FireDragon":
        displayImage('Sprites/smallFireDragon.png', WIDTH / 1.26, HEIGHT * .06) # PLAYER AI
    elif progmonAI == "WaterTurtle":
        displayImage('Sprites/smallWaterTurtle.png', WIDTH / 1.26, HEIGHT * .06) # PLAYER AI
    elif progmonAI == "FinalBoss":
        displayImage('Sprites/smallFinalBoss.png', WIDTH / 1.26, HEIGHT * .06) # PLAYER AI

    # DISPLAY END SCREEN STATISTICS
    displayText("Total Attacks:" + (str(totalAttackPlayerP1)), MEDIUM, BLACK, WIDTH / 4.7, HEIGHT * .38)
    Hit_P1 = ((totalHitPlayerP1 / totalAttackPlayerP1)*100)
    Hit_P1_Percentage = round(Hit_P1, 2)
    Missed_P1 = ((totalMissedPlayerP1 / totalAttackPlayerP1)*100)
    Missed_P1_Percentage = round(Missed_P1, 2)
    displayText("Hit %:" + (str(Hit_P1_Percentage)), MEDIUM, BLACK, WIDTH / 4.7, HEIGHT * .48)
    displayText("Miss %:" + (str(Missed_P1_Percentage)), MEDIUM, BLACK, WIDTH / 4.7, HEIGHT * .58)
    displayText("Bag:", MEDIUM, BLACK, WIDTH / 4.7, HEIGHT * .68) # still working on this
    displayText("Switches:", MEDIUM, BLACK, WIDTH / 4.7, HEIGHT * .78) # still working on this

    displayText("Total Attacks:", MEDIUM, BLACK, WIDTH / 1.3, HEIGHT * .38) # still working on this
    # hit2 = ((totalhitPlayer2 / totalAttackPlayer2) * 100)
    # hit2Percentage = round(hit2, 2)
    # missed2 = ((totalMissedPlayer2 / totalAttackPlayer2) * 100)
    # missed2Percentage = round(missed2, 2)
    displayText("Hit %:", MEDIUM, BLACK, WIDTH / 1.3, HEIGHT * .48) # still working on this
    displayText("Miss %:", MEDIUM, BLACK, WIDTH / 1.3, HEIGHT * .58) # still working on this
    displayText("Bag:", MEDIUM, BLACK, WIDTH / 1.3, HEIGHT * .68) # still working on this
    displayText("Switches:", MEDIUM, BLACK, WIDTH / 1.3, HEIGHT * .78) # still working on this

    # DISPLAY BUTTONS
    btnRestart = displayButton("RESTART GAME", SMALL, BLACK, WIDTH / 2.7, HEIGHT * .90)
    btnQuit = displayButton("QUIT", SMALL, BLACK, WIDTH / 1.5, HEIGHT * .90)

    # TRACK BUTTONS
    if mouseClick(btnRestart):
        print("\n[RETURNING TO START SCREEN]\n")
        gameState = "startScreen"
        controlScreen(gameState)

    if mouseClick(btnQuit):
        quitGame()

def controlScreen(gameState):
    """
    Handles control of the screen via game state
    Args:
        gameState (string) - the current game state
    Returns:
        None
    """
    if gameState == "startScreen" or gameState == "fightScreen" or gameState == "fightMenu" or gameState == "bagMenu" or gameState == "progmonMenu" or gameState == "endScreen":
        while gameState == "startScreen":
            eventHandler()
            startScreen()
        while gameState == "fightScreen":
            eventHandler()
            fightScreen()
        while gameState == "fightMenu":
            eventHandler()
            fightMenu()
        while gameState == "bagMenu":
            eventHandler()
            bagMenu()
        while gameState == "progmonMenu":
            eventHandler()
            progmonMenu()
        while gameState == "endScreen":
            eventHandler()
            endScreen()
    else:
        print("ERROR: Invalid gameState")
        quitGame()

def AITurn():
    """
    Handles the decisions (FIGHT, BAG, PROGMON, QUIT) the AI has to make during their turn depending on their health and the enemy's health
    Args:
        None
    Returns:
        None
    """
    global winner
    global gameState
    global myAI
    global progmonAI
    global progmonNameAI

    pygame.draw.rect(SCREEN, WHITE, (WIDTH * .518, HEIGHT * .71, 480, 140), 0) # FILLED BOX FOR PLAYER AI'S MESSAGES
    displayText("Player AI is thinking...", MINI, BLACK, WIDTH * .75, HEIGHT * .75)

    if(myP1.checkAlive() != True):
        winner = "Player AI"
        pygame.draw.rect(SCREEN, WHITE, (WIDTH * .518, HEIGHT * .71, 480, 140), 0) # FILLED BOX FOR PLAYER AI'S MESSAGES
        displayText(("Player 1's {} has fainted. You lose!".format(progmonNameP1)), MINI, BLACK, WIDTH * .75, HEIGHT * .8)
        print("Player 1's {} has fainted. Player AI wins!".format(progmonNameP1))
        pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
        gameState = "endScreen"
        controlScreen(gameState)

    P1critical = (myP1.getCurrentHealth() / myP1.getHp()) #check if P1 is at critical health (<= 20% of max health)
    AIcritical = (myP1.getCurrentHealth() / myP1.getHp()) #check if AI is at critical health (<= 20% of max health)

    if(myAI.getStunStatus() == True): #if stunned, skip turn
        print("{} has been stunned by {}!".format(progmonNameAI, progmonNameP1))
        myAI.stunned = False
        pygame.draw.rect(SCREEN, WHITE, (WIDTH * .518, HEIGHT * .71, 480, 140), 0) # FILLED BOX FOR PLAYER AI'S MESSAGES
        displayText(("{} has been stunned by {}!".format(progmonNameAI, progmonNameP1)), MINI, BLACK, WIDTH * .75, HEIGHT * .75)
        pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
    elif(P1critical <= .2): #if P1 is critical, always attack
        messageToShow = myAI.AIAttack(myP1)
        print("{} attacking...".format(progmonNameAI))
        displayText(("{} attacking...".format(progmonNameAI)), MINI, BLACK, WIDTH * .75, HEIGHT * .8)
        print("{}".format(messageToShow))
        displayText(("{}".format(messageToShow)), MINI, BLACK, WIDTH * .75, HEIGHT * .85)
    elif((AIcritical <= .2) and ("healthPotion" in myAI.getBag())): #if AI is critical but P1 is not, use healing potion (if AI has it)
        myAI.useHealthPotion()
        print("Player AI used a Health Potion!")
        displayText("Player AI used a Health Potion!", MINI, BLACK, WIDTH * .75, HEIGHT * .8)
    elif(AIcritical <= .2): #if AI is critical but P1 is not and there is no healing potion, 20% chance to run (else attack)
        percentage = random.randint(1, 100)
        if(percentage <= 20):
            print("Player AI ran!")
            displayText("Player AI ran!", MINI, BLACK, WIDTH * .75, HEIGHT * .8)
            pygame.time.wait(3000) # WAIT
            gameState = "endScreen"
            controlScreen(gameState)
        else:
            print("{} attacking...".format(progmonNameAI))
            displayText(("{} attacking...".format(progmonNameAI)), MINI, BLACK, WIDTH * .75, HEIGHT * .8)
            if messageToShow[0] == True:
                displayImage('Sprites/hitMarker.png', WIDTH * .2, HEIGHT * .45) # HIT MARKER ON PLAYER 1 PROGMON
            print("{}".format(messageToShow[1]))
            displayText(("{}".format(messageToShow[1])), MINI, BLACK, WIDTH * .75, HEIGHT * .8)
    else: #give 70% chance to attack, 20% to use bag item (if bag empty, attack), 7% chance to switch progmon (currently disabled) 3% chance to run
        print("\n[WORK IN PROGRESS]\n")
        percentage = random.randint(1, 100)
        if(percentage <= 70):
            messageToShow = myAI.AIAttack(myP1)
            print("{} attacking...".format(progmonNameAI))
            displayText(("{} attacking...".format(progmonNameAI)), MINI, BLACK, WIDTH * .75, HEIGHT * .8)
            if messageToShow[0] == True:
                displayImage('Sprites/hitMarker.png', WIDTH * .2, HEIGHT * .45) # HIT MARKER ON PLAYER 1 PROGMON
            print("{}".format(messageToShow[1]))
            displayText(("{}".format(messageToShow[1])), MINI, BLACK, WIDTH * .75, HEIGHT * .85)
        elif(percentage <= 90):
            if(myAI.bagEmpty() == True): #attack
                print("Player AI's Bag is empty!")
                messageToShow = myAI.AIAttack(myP1)
                print("{} attacking!".format(progmonNameAI))
                displayText(("{} attacking!".format(progmonNameAI)), MINI, BLACK, WIDTH * .75, HEIGHT * .8)
                if messageToShow[0] == True:
                    displayImage('Sprites/hitMarker.png', WIDTH * .2, HEIGHT * .45) # HIT MARKER ON PLAYER 1 PROGMON
                print("{}".format(messageToShow[1]))
                displayText(("{}".format(messageToShow[1])), MINI, BLACK, WIDTH * .75, HEIGHT * .85)
            else:
                if("statBoost" in myAI.getBag()):
                    print("Player AI used a Stat Boost!")
                    myAI.useStatBoost()
                    displayText("Player AI used a Stat Boost!", MINI, BLACK, WIDTH * .75, HEIGHT * .8)
                elif("defenseBoost" in myAI.getBag()):
                    print("Player AI used a Defense Boost!")
                    myAI.useDefenseBoost()
                    displayText("Player AI used a Defense Boost!", MINI, BLACK, WIDTH * .75, HEIGHT * .8)
                elif("healthPotion" in myAI.getBag()):
                    print("Player AI used a Health Potion!")
                    myAI.useHealthPotion()
                    displayText("Player AI used a Health Potion!", MINI, BLACK, WIDTH * .75, HEIGHT * .8)
        elif(percentage <= 97):
            print("Player AI is switching their Progmon")
            displayText("Player AI is switching their Progmon", MINI, BLACK, WIDTH * .75, HEIGHT * .8)
            switchControl = random.randint(1, 4)
            if(switchControl == 1): #switch to electric cat (or, if currently electric cat, then final boss)
                curHp = myAI.getCurrentHealth()
                curBag = myAI.getBag()
                curStatBoost = myAI.getStatBoost()
                curDefenseBoost = myAI.getDefenseBoost()
                if(progmonAI != "ElectricCat"):
                    myAI = ElectricCat()
                    progmonAI = "ElectricCat"
                    progmonNameAI = "Electric Cat"
                else:
                    myAI = FinalBoss()
                    progmonAI = "FinalBoss"
                    progmonNameAI = "Final Boss"
                myAI.setBag(curBag)
                myAI.setStatBoost(curStatBoost)
                myAI.setDefenseBoost(curDefenseBoost)
                if(curHp < myAI.getHp()): #if AI had less health than new progmon's max (before the switch), reduce health
                    myAI.setCurrentHealth(curHp)
                print("Player AI switched to {}".format(progmonNameAI))
                displayText("Player AI switched to {}".format(progmonNameAI), MINI, BLACK, WIDTH * .75, HEIGHT * .85)
                pygame.time.delay(1200) # WAIT
            elif(switchControl == 2): #switch to fire dragon (or, if currently fire dragon, then final boss)
                curHp = myAI.getCurrentHealth()
                curBag = myAI.getBag()
                curStatBoost = myAI.getStatBoost()
                curDefenseBoost = myAI.getDefenseBoost()
                if(progmonAI != "FireDragon"):
                    myAI = FireDragon()
                    progmonAI = "FireDragon"
                    progmonNameAI = "Fire Dragon"
                else:
                    myAI = FinalBoss()
                    progmonAI = "FinalBoss"
                    progmonNameAI = "Final Boss"
                myAI.setBag(curBag)
                myAI.setStatBoost(curStatBoost)
                myAI.setDefenseBoost(curDefenseBoost)
                if(curHp < myAI.getHp()): #if AI had less health than new progmon's max (before the switch), reduce health
                    myAI.setCurrentHealth(curHp)
                print("Player AI switched to {}".format(progmonNameAI))
                displayText("Player AI switched to {}".format(progmonNameAI), MINI, BLACK, WIDTH * .75, HEIGHT * .85)
                pygame.time.delay(1200) # WAIT
            elif(switchControl == 3): #switch to water turtle (or, if currently water turtle, then final boss)
                curHp = myAI.getCurrentHealth()
                curBag = myAI.getBag()
                curStatBoost = myAI.getStatBoost()
                curDefenseBoost = myAI.getDefenseBoost()
                if(progmonAI != "WaterTurtle"):
                    myAI = WaterTurtle()
                    progmonAI = "WaterTurtle"
                    progmonNameAI = "Water Turtle"
                else:
                    myAI = FinalBoss()
                    progmonAI = "FinalBoss"
                    progmonNameAI = "Final Boss"
                myAI.setBag(curBag)
                myAI.setStatBoost(curStatBoost)
                myAI.setDefenseBoost(curDefenseBoost)
                if(curHp < myAI.getHp()): #if AI had less health than new progmon's max (before the switch), reduce health
                    myAI.setCurrentHealth(curHp)
                print("Player AI switched to {}".format(progmonNameAI))
                displayText("Player AI switched to {}".format(progmonNameAI), MINI, BLACK, WIDTH * .75, HEIGHT * .85)
                pygame.time.delay(1200) # WAIT
        else:
            print("Player AI ran away!")
            displayText("Player AI ran away!", MINI, BLACK, WIDTH * .75, HEIGHT * .8)
            pygame.time.wait(3000) # WAIT
            gameState = "endScreen"
            controlScreen(gameState)

if __name__ == "__main__":
    gameState = "startScreen"
    controlScreen(gameState)

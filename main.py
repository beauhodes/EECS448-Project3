import random
import pygame
import pygame.gfxdraw
from fireDragon import FireDragon
from electricCat import ElectricCat
from waterTurtle import WaterTurtle
from progmon import Progmon, FireDragonTester, ElectricCatTester, WaterTurtleTest

# INITIALIZE PYGAME AND GLOBAL DISPLAY VARIABLES
pygame.init()
displayWidth = 1080
displayHeight = 720
display = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('EECS448 Project 4: Progmon Battle Simulator')

# GLOBAL TEXT OBJECT VARIABLES FOR PYGAME
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
miniText = pygame.font.Font('freesansbold.ttf', 24)
smallText = pygame.font.Font('freesansbold.ttf', 32)
mediumText = pygame.font.Font('freesansbold.ttf', 36)
largeText = pygame.font.Font('freesansbold.ttf', 42)

# GLOBAL VARIABLES
global myP1
progmonP1 = ""
progmonNameP1 = ""
global myAI
progmonAI = ""
progmonNameAI = ""

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
    print("Quitting...")
    pygame.quit()
    quit()

def createTextObject(textToDisplay, fontToUse):
    """
    Creates a text object with textToDisplay and fontToUse
    Args:
        textToDisplay (string) - text to be displayed
        fontToUse (string) - font of the displayed text
    Returns:
        The created textSurface and textSurface_RECT
    """
    textSurface = fontToUse.render(textToDisplay, True, BLACK)
    return textSurface, textSurface.get_rect()

def isButtonClickDetected(surfaceRect):
    """
    Checks if mouse-click is within the bounds of a surfaceRect
    Args:
        surfaceRect (Pygame.Rect) - surface object that is being checked
    Returns:
        (bool) - True if mouse-click is in surfaceRect, otherwise False
    """
    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE
    if surfaceRect.collidepoint(mouse):
        pygame.draw.rect(display, RED, surfaceRect, 3) # BOX AROUND surfaceRect
        if pygame.mouse.get_pressed() == (1, 0, 0):
            pygame.time.delay(500) # WAIT TO PREVENT MULTIPLE BUTTON CLICKS
            return True
    return False

def detectFaintedAI():
    """
    Checks if Player AI's Progmon has fainted
    Args:
        None
    Returns:
        None
    """
    # MESSAGE TO PLAYER 1
    pygame.gfxdraw.box(display, (displayWidth * 0.06, displayHeight * 0.79, 450, 100), WHITE) # FILLED BOX FOR DISPLAYING THE MESSAGE TO PLAYER 1
    pygame.draw.rect(display, BLACK, (displayWidth * 0.06, displayHeight * 0.79, 450, 100), 5) # BOX AROUND MESSAGE TO PLAYER 1
    textMessage, textMessage_RECT = createTextObject("Player AI's Progmon fainted. You win!", miniText)
    textMessage_RECT.center = (displayWidth / 3.7, displayHeight / 1.2)
    display.blit(textMessage, textMessage_RECT)
    pygame.display.update()
    pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE

# (UNFINISHED)
def startScreen():
    """
    Displays and tracks all objects on the Start Screen
    Args:
        None
    Returns:
        None
    """
    global myP1
    global progmonP1
    global myAI
    global progmonAI

    # PLAYER 1'S PROGMON OPTIONS
    textPlayer1, textPlayer1_RECT = createTextObject("Player 1's Progmon", largeText)
    textPlayer1_RECT.center = (displayWidth / 4, displayHeight / 19)
    # PLAYER 1'S PROGMON BUTTONS
    textElectricCatP1, textElectricCatP1_RECT = createTextObject("Electric Cat", smallText)
    textElectricCatP1_RECT.center = (displayWidth / 4, displayHeight / 7.5)
    textFireDragonP1, textFireDragonP1_RECT = createTextObject("Fire Dragon", smallText)
    textFireDragonP1_RECT.center = (displayWidth / 4, displayHeight / 4)
    # PLAYER 1'S PROGMON IMAGES
    imageSmallElectricCatP1 = pygame.image.load('Sprites/smallElectricCat.png')
    imageSmallElectricCatP1_RECT = imageSmallElectricCatP1.get_rect()
    imageSmallElectricCatP1_RECT.center = (displayWidth / 9, displayHeight / 7.5)
    imageSmallFireDragonP1 = pygame.image.load('Sprites/smallFireDragon.png')
    imageSmallFireDragonP1_RECT = imageSmallFireDragonP1.get_rect()
    imageSmallFireDragonP1_RECT.center = (displayWidth / 9, displayHeight / 4)

    # PLAYER AI'S PROGMON OPTIONS
    textPlayerAI, textPlayerAI_RECT = createTextObject("Player AI's Progmon", largeText)
    textPlayerAI_RECT.center = (displayWidth / 1.3, displayHeight / 19)
    # PLAYER AI'S PROGMON BUTTONS
    textElectricCatAI, textElectricCatAI_RECT = createTextObject("Electric Cat", smallText)
    textElectricCatAI_RECT.center = (displayWidth / 1.3, displayHeight / 7.5)
    textFireDragonAI, textFireDragonAI_RECT = createTextObject("Fire Dragon", smallText)
    textFireDragonAI_RECT.center = (displayWidth / 1.3, displayHeight / 4)
    # PLAYER AI'S PROGMON IMAGES
    imageSmallElectricCatAI = pygame.image.load('Sprites/smallElectricCat.png')
    imageSmallElectricCatAI_RECT = imageSmallElectricCatAI.get_rect()
    imageSmallElectricCatAI_RECT.center = (displayWidth / 1.6, displayHeight / 7.5)
    imageSmallFireDragonAI = pygame.image.load('Sprites/smallFireDragon.png')
    imageSmallFireDragonAI_RECT = imageSmallFireDragonAI.get_rect()
    imageSmallFireDragonAI_RECT.center = (displayWidth / 1.6, displayHeight / 4)
    imageBackground = pygame.image.load('Sprites/background.png')
    imageBackground_RECT = imageSmallFireDragonAI.get_rect()
    imageBackground_RECT.center = (displayWidth/30, displayHeight/20)

    # PLAY BUTTON
    textPlay, textPlay_RECT = createTextObject("PLAY", mediumText)
    textPlay_RECT.center = (displayWidth / 2, displayHeight / 1.2)

    # DISPLAY TEXT OBJECTS AND IMAGES
    display.fill(WHITE)
    display.blit(imageBackground, imageBackground_RECT)
    display.blit(imageSmallElectricCatP1, imageSmallElectricCatP1_RECT)
    display.blit(imageSmallFireDragonP1, imageSmallFireDragonP1_RECT)
    display.blit(textPlayer1, textPlayer1_RECT)
    display.blit(textElectricCatP1, textElectricCatP1_RECT)
    display.blit(textFireDragonP1, textFireDragonP1_RECT)
    display.blit(imageSmallElectricCatAI, imageSmallElectricCatAI_RECT)
    display.blit(imageSmallFireDragonAI, imageSmallFireDragonAI_RECT)
    display.blit(textPlayerAI, textPlayerAI_RECT)
    display.blit(textElectricCatAI, textElectricCatAI_RECT)
    display.blit(textFireDragonAI, textFireDragonAI_RECT)
    display.blit(textPlay, textPlay_RECT)

    # TRACK PROGMON BUTTONS FOR PLAYER 1
    if isButtonClickDetected(textElectricCatP1_RECT):
        myP1 = ElectricCatTester()
        progmonP1 = "ElectricCat"
        # print("progmonP1 =", progmonP1) # TESTER CODE
    elif isButtonClickDetected(textFireDragonP1_RECT):
        myP1 = FireDragonTester()
        progmonP1 = "FireDragon"
        # print("progmonP1 =", progmonP1) # TESTER CODE

    # TRACK PROGMON BUTTONS FOR PLAYER AI
    if isButtonClickDetected(textElectricCatAI_RECT):
        myAI = ElectricCatTester()
        progmonAI = "ElectricCat"
        # print("progmonAI =", progmonAI) # TESTER CODE
    elif isButtonClickDetected(textFireDragonAI_RECT):
        myAI = FireDragonTester()
        progmonAI = "FireDragon"
        # print("progmonAI =", progmonAI) # TESTER CODE

    # TRACK THE PLAY BUTTON
    if isButtonClickDetected(textPlay_RECT):
        if progmonP1 != "" and progmonAI != "":
            controlScreen("fightScreen")
        else:
            if progmonP1 == "":
                print("ERROR: Player 1 needs to select a Progmon")
            elif progmonAI == "":
                print("ERROR: Player AI needs to select a Progmon")

# (UNFINISHED)
def fightScreen():
    """
    Displays and tracks all objects on the Fight Screen
    Args:
        None
    Returns:
        None
    """
    global myP1
    global progmonNameP1
    global myAI
    global progmonNameAI

    # MESSAGE TO PLAYER 1
    textMessage, textMessage_RECT = createTextObject("What do you want to do?", miniText)
    textMessage_RECT.center = (displayWidth / 3.7, displayHeight / 1.2)

    # BATTLE MENU OPTIONS
    textFight, textFight_RECT = createTextObject("FIGHT", smallText)
    textFight_RECT.center = (displayWidth / 1.4, displayHeight / 1.2)
    textBag, textBag_RECT = createTextObject("BAG", smallText)
    textBag_RECT.center = (displayWidth / 1.1, displayHeight / 1.2)
    textProgmon, textProgmon_RECT = createTextObject("PROGMON", smallText)
    textProgmon_RECT.center = (displayWidth / 1.4, displayHeight / 1.1)
    textQuit, textQuit_RECT = createTextObject("QUIT", smallText)
    textQuit_RECT.center = (displayWidth / 1.1, displayHeight / 1.1)

    # PLAYER 1
    textNameP1, textNameP1_RECT = createTextObject("Player 1", mediumText)
    textNameP1_RECT.center = (displayWidth / 4.5, displayHeight / 30)
    textProgmonP1, textProgmonP1_RECT = createTextObject(progmonNameP1, mediumText)
    textProgmonP1_RECT.center = (displayWidth / 4.5, displayHeight / 10)
    if progmonP1 == "ElectricCat":
        progmonNameP1 = "Electric Cat"
        progmonImageP1 = pygame.image.load('Sprites/largeElectricCat.png')
        progmonImageP1_RECT = progmonImageP1.get_rect()
        progmonImageP1_RECT.center = (displayWidth / 4.5, displayHeight / 2.5)
    elif progmonP1 == "FireDragon":
        progmonNameP1 = "Fire Dragon"
        progmonImageP1 = pygame.image.load('Sprites/largeFireDragon.png')
        progmonImageP1_RECT = progmonImageP1.get_rect()
        progmonImageP1_RECT.center = (displayWidth / 4.5, displayHeight / 2.5)
    # (UNFINISHED) CREATE HEALTH BAR FOR PLAYER 1'S PROGMON
    progmonHealthP1 = myP1.getCurrentHealth()
    # print("progmonHealthP1 =", progmonHealthP1) # TESTER CODE
    textHealthP1 = smallText.render(str(progmonHealthP1), True, BLACK, None)
    textHealthP1_RECT = textHealthP1.get_rect()
    textHealthP1_RECT.center = (displayWidth / 3.2, displayHeight / 6)

    # PLAYER AI
    textNameAI, textNameAI_RECT = createTextObject("Player AI", mediumText)
    textNameAI_RECT.center = (displayWidth / 1.3, displayHeight / 30)
    textProgmonAI, textProgmonAI_RECT = createTextObject(progmonNameAI, mediumText)
    textProgmonAI_RECT.center = (displayWidth / 1.3, displayHeight / 10)
    if progmonAI == "ElectricCat":
        progmonNameAI = "Electric Cat"
        progmonImageAI = pygame.image.load('Sprites/largeElectricCat.png')
        progmonImageAI_RECT = progmonImageAI.get_rect()
        progmonImageAI_RECT.center = (displayWidth / 1.3, displayHeight / 2.5)
    elif progmonAI == "FireDragon":
        progmonNameAI = "Fire Dragon"
        progmonImageAI = pygame.image.load('Sprites/largeFireDragon.png')
        progmonImageAI_RECT = progmonImageAI.get_rect()
        progmonImageAI_RECT.center = (displayWidth / 1.3, displayHeight / 2.5)
    # (UNFINISHED) CREATE HEALTH BAR FOR PLAYER AI'S PROGMON
    progmonHealthAI = myAI.getCurrentHealth()
    # print("progmonHealthAI =", progmonHealthAI) # TESTER CODE
    textHealthAI = smallText.render(str(progmonHealthAI), True, BLACK, None)
    textHealthAI_RECT = textHealthAI.get_rect()
    textHealthAI_RECT.center = (displayWidth / 1.145, displayHeight / 6)

    # DISPLAY TEXT OBJECTS AND IMAGES
    display.fill(WHITE)
    display.blit(progmonImageP1, progmonImageP1_RECT)
    display.blit(textNameP1, textNameP1_RECT)
    display.blit(textProgmonP1, textProgmonP1_RECT)
    display.blit(textHealthP1, textHealthP1_RECT)
    display.blit(progmonImageAI, progmonImageAI_RECT)
    display.blit(textNameAI, textNameAI_RECT)
    display.blit(textProgmonAI, textProgmonAI_RECT)
    display.blit(textHealthAI, textHealthAI_RECT)
    display.blit(textFight, textFight_RECT)
    display.blit(textBag, textBag_RECT)
    display.blit(textProgmon, textProgmon_RECT)
    display.blit(textQuit, textQuit_RECT)
    display.blit(textMessage, textMessage_RECT)
    pygame.draw.rect(display, BLACK, (displayWidth * 0.62, displayHeight * 0.79, 370, 120), 5) # BOX AROUND BATTLE MENU OPTIONS
    pygame.draw.rect(display, BLACK, (displayWidth * 0.06, displayHeight * 0.065, 350, 100), 5) # BOX AROUND PLAYER 1'S PROGMON NAME AND HEALTH
    pygame.draw.rect(display, BLACK, (displayWidth * 0.6, displayHeight * 0.065, 350, 100), 5) # BOX AROUND PLAYER AI'S PROGMON NAME AND HEALTH
    pygame.draw.rect(display, BLACK, (displayWidth * 0.06, displayHeight * 0.79, 450, 100), 5) # BOX AROUND MESSAGE TO PLAYER 1
    pygame.draw.rect(display, BLACK, (displayWidth * .16, displayHeight * .14, 125, 40), 5) #outline for P1 health bar
    pygame.draw.rect(display, RED, (displayWidth * .162, displayHeight * .141, 121, 37), 0) #fill for P1 health bar
    pygame.draw.rect(display, (0, 200, 0 ), (displayWidth * .162, displayHeight * .141, 121*(progmonHealthP1/myP1.getHp()), 37), 0) #fill for P1 health bar
    pygame.draw.rect(display, BLACK, (displayWidth * .72, displayHeight * .14, 125, 40), 5) #outline for AI health bar
    pygame.draw.rect(display, RED, (displayWidth * .722, displayHeight * .141, 121, 37), 0) #fill for AI health bar
    pygame.draw.rect(display, (0, 200, 0 ), (displayWidth * .722, displayHeight * .141, 121*(progmonHealthAI/myAI.getHp()), 37), 0) #fill for AI health bar

    # TRACK BATTLE MENU BUTTONS
    if isButtonClickDetected(textFight_RECT):
        controlScreen("fightMenu")
    elif isButtonClickDetected(textBag_RECT):
        if myP1.bagEmpty():
            # print("Player 1 has nothing in their Bag") # TESTER CODE

            # MESSAGE TO PLAYER 1
            pygame.gfxdraw.box(display, (displayWidth * 0.06, displayHeight * 0.79, 450, 100), WHITE) # FILLED BOX FOR DISPLAYING THE MESSAGE TO PLAYER 1
            pygame.draw.rect(display, BLACK, (displayWidth * 0.06, displayHeight * 0.79, 450, 100), 5) # BOX AROUND MESSAGE TO PLAYER 1
            textMessage, textMessage_RECT = createTextObject("Your Bag is empty!", miniText)
            textMessage_RECT.center = (displayWidth / 3.7, displayHeight / 1.2)
            display.blit(textMessage, textMessage_RECT)
            pygame.display.update()
            pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
            controlScreen("fightScreen")
        else:
            controlScreen("bagMenu")
        pygame.time.delay(1200) # WAIT BEFORE THE AI GETS TO GO
        AITurn()
    elif isButtonClickDetected(textProgmon_RECT):
        controlScreen("progmonMenu")
    elif isButtonClickDetected(textQuit_RECT):
        quitGame()

# (UNFINISHED)
def fightMenu():
    """
    Displays and tracks the Fight Menu for Player 1 after "FIGHT" has been clicked
    Args:
        None
    Returns:
        None
    """
    global myP1
    global myAI
    global progmonP1

    pygame.gfxdraw.box(display, (displayWidth * 0.62, displayHeight * 0.79, 370, 120), WHITE) # FILLED BOX FOR DISPLAYING THE ATTACK MENU
    pygame.draw.rect(display, BLACK, (displayWidth * 0.62, displayHeight * 0.79, 370, 120), 5) # BOX AROUND ATTACK MENU

    # MESSAGE TO PLAYER 1
    pygame.gfxdraw.box(display, (displayWidth * 0.06, displayHeight * 0.79, 450, 100), WHITE) # FILLED BOX FOR DISPLAYING THE MESSAGE TO PLAYER 1
    pygame.draw.rect(display, BLACK, (displayWidth * 0.06, displayHeight * 0.79, 450, 100), 5) # BOX AROUND MESSAGE TO PLAYER 1
    textMessage, textMessage_RECT = createTextObject("Which attack do you want to use?", miniText)
    textMessage_RECT.center = (displayWidth / 3.7, displayHeight / 1.2)
    display.blit(textMessage, textMessage_RECT)

    #get P1's list of attacks
    P1attackList = myP1.getAttackList()
    if (len(P1attackList) == 4):
        textAttack1, textAttack1_RECT = createTextObject(str(P1attackList[0]), miniText)
        textAttack1_RECT.center = (displayWidth / 1.4, displayHeight / 1.2)
        textAttack2, textAttack2_RECT = createTextObject(str(P1attackList[1]), miniText)
        textAttack2_RECT.center = (displayWidth / 1.15, displayHeight / 1.1)
        textAttack3, textAttack3_RECT = createTextObject(str(P1attackList[2]), miniText)
        textAttack3_RECT.center = (displayWidth / 1.4, displayHeight / 1.1)
        textAttack4, textAttack4_RECT = createTextObject(str(P1attackList[3]), miniText)
        textAttack4_RECT.center = (displayWidth / 1.14, displayHeight / 1.2)

        display.blit(textAttack1, textAttack1_RECT)
        display.blit(textAttack2, textAttack2_RECT)
        display.blit(textAttack3, textAttack3_RECT)
        display.blit(textAttack4, textAttack4_RECT)

        # TRACK FIGHT MENU BUTTONS
        if isButtonClickDetected(textAttack1_RECT):
            # print("Player 1's Electric Cat used Lightning Bolt!") # TESTER CODE
            myP1.attack1(myAI)
            # MESSAGE TO PLAYER 1
            pygame.gfxdraw.box(display, (displayWidth * 0.06, displayHeight * 0.79, 450, 100), WHITE) # FILLED BOX FOR DISPLAYING THE MESSAGE TO PLAYER 1
            pygame.draw.rect(display, BLACK, (displayWidth * 0.06, displayHeight * 0.79, 450, 100), 5) # BOX AROUND MESSAGE TO PLAYER 1
            textMessage, textMessage_RECT = createTextObject(("Player 1's {} used {}!".format(progmonP1, P1attackList[0])), miniText)
            textMessage_RECT.center = (displayWidth / 3.7, displayHeight / 1.2)
            display.blit(textMessage, textMessage_RECT)
            pygame.display.update()
            pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE

            if myAI.checkAlive():
                pygame.time.delay(1200) # WAIT BEFORE LETTING AI GO
                AITurn()
                controlScreen("fightScreen")
            else:
                print("Player AI's", progmonNameAI, "has fainted. You win!") # TESTER CODE
                detectFaintedAI()
        elif isButtonClickDetected(textAttack2_RECT):
            # print("Player 1's Electric Cat used Energy Beam!") # TESTER CODE
            myP1.attack2(myAI)
            # MESSAGE TO PLAYER 1
            pygame.gfxdraw.box(display, (displayWidth * 0.06, displayHeight * 0.79, 450, 100), WHITE) # FILLED BOX FOR DISPLAYING THE MESSAGE TO PLAYER 1
            pygame.draw.rect(display, BLACK, (displayWidth * 0.06, displayHeight * 0.79, 450, 100), 5) # BOX AROUND MESSAGE TO PLAYER 1
            textMessage, textMessage_RECT = createTextObject(("Player 1's {} used {}!".format(progmonP1, P1attackList[1])), miniText)
            textMessage_RECT.center = (displayWidth / 3.7, displayHeight / 1.2)
            display.blit(textMessage, textMessage_RECT)
            pygame.display.update()
            pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE

            if myAI.checkAlive():
                pygame.time.delay(1200) # WAIT BEFORE LETTING AI GO
                AITurn()
                controlScreen("fightScreen")
            else:
                print("Player AI's", progmonNameAI, "has fainted. You win!") # TESTER CODE
                detectFaintedAI()
        elif isButtonClickDetected(textAttack3_RECT):
            # print("Player 1's Electric Cat used Electric Scratch!") # TESTER CODE
            myP1.attack3(myAI)
            # MESSAGE TO PLAYER 1
            pygame.gfxdraw.box(display, (displayWidth * 0.06, displayHeight * 0.79, 450, 100), WHITE) # FILLED BOX FOR DISPLAYING THE MESSAGE TO PLAYER 1
            pygame.draw.rect(display, BLACK, (displayWidth * 0.06, displayHeight * 0.79, 450, 100), 5) # BOX AROUND MESSAGE TO PLAYER 1
            textMessage, textMessage_RECT = createTextObject(("Player 1's {} used {}!".format(progmonP1, P1attackList[2])), miniText)
            textMessage_RECT.center = (displayWidth / 3.7, displayHeight / 1.2)
            display.blit(textMessage, textMessage_RECT)
            pygame.display.update()
            pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE

            if myAI.checkAlive():
                pygame.time.delay(1200) # WAIT BEFORE LETTING AI GO
                AITurn()
                controlScreen("fightScreen")
            else:
                print("Player AI's", progmonNameAI, "has fainted. You win!") # TESTER CODE
                detectFaintedAI()
        elif isButtonClickDetected(textAttack4_RECT):
            # print("Player 1's Electric Cat used Bite!") # TESTER CODE
            myP1.attack4(myAI)
            # MESSAGE TO PLAYER 1
            pygame.gfxdraw.box(display, (displayWidth * 0.06, displayHeight * 0.79, 450, 100), WHITE) # FILLED BOX FOR DISPLAYING THE MESSAGE TO PLAYER 1
            pygame.draw.rect(display, BLACK, (displayWidth * 0.06, displayHeight * 0.79, 450, 100), 5) # BOX AROUND MESSAGE TO PLAYER 1
            textMessage, textMessage_RECT = createTextObject(("Player 1's {} used {}!".format(progmonP1, P1attackList[3])), miniText)
            textMessage_RECT.center = (displayWidth / 3.7, displayHeight / 1.2)
            display.blit(textMessage, textMessage_RECT)
            pygame.display.update()
            pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE

            if myAI.checkAlive():
                pygame.time.delay(1200) # WAIT BEFORE LETTING AI GO
                AITurn()
                controlScreen("fightScreen")
            else:
                print("Player AI's", progmonNameAI, "has fainted. You win!") # TESTER CODE
                detectFaintedAI()

# (UNFINISHED)
def bagMenu():
    """
    Displays and tracks the Bag Menu for Player 1 after "BAG" has been clicked
    Args:
        None
    Returns:
        None
    """
    pygame.gfxdraw.box(display, (displayWidth * 0.62, displayHeight * 0.79, 370, 120), WHITE) # FILLED BOX FOR DISPLAYING THE BAG MENU
    pygame.draw.rect(display, BLACK, (displayWidth * 0.62, displayHeight * 0.79, 370, 120), 5) # BOX AROUND BAG MENU

    # MESSAGE TO PLAYER 1
    pygame.gfxdraw.box(display, (displayWidth * 0.06, displayHeight * 0.79, 450, 100), WHITE) # FILLED BOX FOR DISPLAYING THE MESSAGE TO PLAYER 1
    pygame.draw.rect(display, BLACK, (displayWidth * 0.06, displayHeight * 0.79, 450, 100), 5) # BOX AROUND MESSAGE TO PLAYER 1
    textMessage, textMessage_RECT = createTextObject("Which item do you want to use?", miniText)
    textMessage_RECT.center = (displayWidth / 3.7, displayHeight / 1.2)

    # PLAYER 1'S BAG ITEMS
    textHealthPotion, textHealthPotion_RECT = createTextObject("Health Potion", miniText)
    textHealthPotion_RECT.center = (displayWidth / 1.4, displayHeight / 1.2)

    display.blit(textMessage, textMessage_RECT)
    display.blit(textHealthPotion, textHealthPotion_RECT)

    if isButtonClickDetected(textHealthPotion_RECT):
        # print("Player 1 has used a Health Potion!") # TESTER CODE
        myP1.useHealthPotion()
        # MESSAGE TO PLAYER 1
        pygame.gfxdraw.box(display, (displayWidth * 0.06, displayHeight * 0.79, 450, 100), WHITE) # FILLED BOX FOR DISPLAYING THE MESSAGE TO PLAYER 1
        pygame.draw.rect(display, BLACK, (displayWidth * 0.06, displayHeight * 0.79, 450, 100), 5) # BOX AROUND MESSAGE TO PLAYER 1
        textMessage, textMessage_RECT = createTextObject("Player 1 has used a Health Potion!", miniText)
        textMessage_RECT.center = (displayWidth / 3.7, displayHeight / 1.2)
        display.blit(textMessage, textMessage_RECT)
        pygame.display.update()
        pygame.time.wait(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE

        pygame.time.delay(1200) # WAIT BEFORE THE AI GETS TO GO
        AITurn()
        controlScreen("fightScreen")

# (UNFINISHED)
def progmonMenu():
    """
    Displays and tracks the Progmon Menu for Player 1 after "PROGMON" has been clicked
    Args:
        None
    Returns:
        None
    """
    pygame.gfxdraw.box(display, (displayWidth * 0.62, displayHeight * 0.79, 370, 120), WHITE) # FILLED BOX FOR DISPLAYING THE PROGMON MENU
    pygame.draw.rect(display, BLACK, (displayWidth * 0.62, displayHeight * 0.79, 370, 120), 5) # BOX AROUND PROGMON MENU

    # MESSAGE TO PLAYER 1
    pygame.gfxdraw.box(display, (displayWidth * 0.06, displayHeight * 0.79, 450, 100), WHITE) # FILLED BOX FOR DISPLAYING THE MESSAGE TO PLAYER 1
    pygame.draw.rect(display, BLACK, (displayWidth * 0.06, displayHeight * 0.79, 450, 100), 5) # BOX AROUND MESSAGE TO PLAYER 1
    textMessage, textMessage_RECT = createTextObject("Which Progmon do you want to use?", miniText)
    textMessage_RECT.center = (displayWidth / 3.7, displayHeight / 1.2)
    display.blit(textMessage, textMessage_RECT)

    controlScreen("fightScreen") # TEMPORARY FIX FOR UN-IMPLEMENTED FEATURE

# (UNFINISHED)
def controlScreen(gameState):
    """
    Handles control of the screen via game state
    Args:
        gameState (string) - the current game state
    Returns:
        None
    """
    if gameState == "startScreen" or gameState == "fightScreen" or gameState == "fightMenu" or gameState == "bagMenu" or gameState == "progmonMenu":
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
    else:
        print("ERROR: Invalid gameState")
        quitGame()

# (UNFINISHED)
def AITurn():
    """
    Handles the decisions (FIGHT, BAG, PROGMON, QUIT) the AI has to make during their turn depending on their health and enemy's health
    Args:
        None
    Returns:
        None
    """
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
        # now we should display some sort of window/message for the user saying if they hit or not
        # update player's health in the UI
        if(myP1.checkAlive() != True):
            print("P1 progmon has died")
            # quitGame()
    # elif(myAI.currentHealth <= critical and myAI.bagEmpty):   #this should be the AI's last option - AI is going to die if it's hit again
        # DISPLAY SOME SORT OF MESSAGE SAYING THE THIS PLAYER CHOSE TO RUN
        # quitGame()
    elif(myAI.currentHealth <= critical):  #if AI is low, it will use potion
        if myAI.bagEmpty():
            print("Player AI's Bag is empty!")
            myAI.AIAttack(myP1)
        else:
            myAI.useHealthPotion() # ERRORS ON SECOND CALL
    else:   # if progmonP1 is not low and AI is not low, then all we can do is attack the other player
        myAI.AIAttack(myP1)
        # now we should display some sort of window/message for the user saying if they hit or not
        # update player's health in the UI
    # playerTurn()    #after turn is over, let the player go

if __name__ == "__main__":
    controlScreen("startScreen")

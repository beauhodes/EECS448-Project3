"""
BUG LIST:
    > When a Progmon faints, their HealthBar and Health does NOT update to display 0 HP
    > Progmon fainted message not staying on screen after mouse is moved
        --> Need this message to stay on screen as long as we have not switched to the endScreen
    > Player AI's MessageBox is NOT updating to display turn-by-turn Attack Messages
    > Need to display the specific details of each item to the Player's in fightScreen
        --> Health Potion healed ProgmonName for 30 HP.
        --> +10 outgoing damage and change to stun enemy.
        --> -10 incoming damage on the next attack.
    > After using an Item in the Bag, the bagMenu continues to be partially displayed on the screen for a short period
"""
import random
import pygame
import pygame.gfxdraw
from progmon import Progmon, FireDragonProgmon, ElectricCatProgmon, WaterTurtleProgmon

# GLOBAL VARIABLES
global myP1
progmonP1 = ""
progmonNameP1 = ""
global myAI
progmonAI = ""
progmonNameAI = ""

# INITIALIZE PYGAME AND GLOBAL DISPLAY/TEXT OBJECT VARIABLES
pygame.init()
displayWidth = 1080
displayHeight = 720
display = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('EECS448 Project 4: Progmon Battle Simulator')
miniText = pygame.font.Font('freesansbold.ttf', 24)
smallText = pygame.font.Font('freesansbold.ttf', 32)
mediumText = pygame.font.Font('freesansbold.ttf', 36)
largeText = pygame.font.Font('freesansbold.ttf', 42)
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
LIGHT_GREEN = pygame.Color(0, 200, 0)
GREEN = pygame.Color(160, 219, 154)  # endScreen background color
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

def createTextObject(textToDisplay, fontToUse, colorToUse):
    """
    Creates a text object with textToDisplay and fontToUse
    Args:
        textToDisplay (string) - text to be displayed
        fontToUse (string) - font of the displayed text
    Returns:
        (Pygame.Surface) - The created textSurface and textSurface_RECT
    """
    textSurface = fontToUse.render(textToDisplay, True, colorToUse)
    return textSurface, textSurface.get_rect()

def isButtonClickDetected(surfaceRect):
    """
    Checks if mouse-click is within the bounds of a surfaceRect
    Args:
        surfaceRect (Pygame.Rect) - surface object that is being checked
    Returns:
        (bool) - True if mouse-click is in surfaceRect, otherwise False
    """
    mousePosition = pygame.mouse.get_pos() # GETS (x, y) COORDINATE OF MOUSE
    if surfaceRect.collidepoint(mousePosition):
        pygame.draw.rect(display, RED, surfaceRect, 3) # UNFILLLED BOX AROUND surfaceRect
        if pygame.mouse.get_pressed() == (1, 0, 0):
            pygame.time.delay(500) # WAIT TO PREVENT MULTIPLE BUTTON CLICKS
            return True
    return False

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
    global progmonNameP1
    global myAI
    global progmonAI
    global progmonNameAI

    # BACKGROUND
    imgBackground = pygame.image.load('Sprites/startScreen.png')
    imgBackground_RECT = imgBackground.get_rect()
    imgBackground_RECT.center = (displayWidth * .5, displayHeight * .5)
    display.blit(imgBackground, imgBackground_RECT)

    # PLAYER 1
    txtP1, txtP1_RECT = createTextObject("Player 1's Progmon", largeText, WHITE)
    txtP1_RECT.center = (displayWidth / 4, displayHeight / 19)
    display.blit(txtP1, txtP1_RECT)
    pygame.draw.rect(display, BLACK, (displayWidth * .15, displayHeight * .1, 220, 320), 0) # FILLED BOX FOR P1 PROGMON OPTIONS
    txtElectricCatP1, txtElectricCatP1_RECT = createTextObject("Electric Cat", smallText, WHITE)
    txtElectricCatP1_RECT.center = (displayWidth / 4, displayHeight / 7.5)
    display.blit(txtElectricCatP1, txtElectricCatP1_RECT)
    txtFireDragonP1, txtFireDragonP1_RECT = createTextObject("Fire Dragon", smallText, WHITE)
    txtFireDragonP1_RECT.center = (displayWidth / 4, displayHeight / 4)
    display.blit(txtFireDragonP1, txtFireDragonP1_RECT)
    txtWaterTurtleP1, txtWaterTurtleP1_RECT = createTextObject("Water Turtle", smallText, WHITE)
    txtWaterTurtleP1_RECT.center = (displayWidth / 4, displayHeight / 2.7)
    display.blit(txtWaterTurtleP1, txtWaterTurtleP1_RECT)
    txtFinalBossP1, txtFinalBossP1_RECT = createTextObject("Final Boss", smallText, WHITE)
    txtFinalBossP1_RECT.center = (displayWidth / 4, displayHeight / 2)
    display.blit(txtFinalBossP1, txtFinalBossP1_RECT)
    imgSmallElectricCatP1 = pygame.image.load('Sprites/smallElectricCat.png')
    imgSmallElectricCatP1_RECT = imgSmallElectricCatP1.get_rect()
    imgSmallElectricCatP1_RECT.center = (displayWidth / 9, displayHeight / 7.5)
    display.blit(imgSmallElectricCatP1, imgSmallElectricCatP1_RECT)
    imgSmallFireDragonP1 = pygame.image.load('Sprites/smallFireDragon.png')
    imgSmallFireDragonP1_RECT = imgSmallFireDragonP1.get_rect()
    imgSmallFireDragonP1_RECT.center = (displayWidth / 9, displayHeight / 4)
    display.blit(imgSmallFireDragonP1, imgSmallFireDragonP1_RECT)
    imgSmallWaterTurtleP1 = pygame.image.load('Sprites/smallWaterTurtle.png')
    imgSmallWaterTurtleP1_RECT = imgSmallWaterTurtleP1.get_rect()
    imgSmallWaterTurtleP1_RECT.center = (displayWidth / 9, displayHeight / 2.7)
    display.blit(imgSmallWaterTurtleP1, imgSmallWaterTurtleP1_RECT)
    imgSmallFinalBossP1 = pygame.image.load('Sprites/smallFinalBoss.png')
    imgSmallFinalBossP1_RECT = imgSmallFinalBossP1.get_rect()
    imgSmallFinalBossP1_RECT.center = (displayWidth / 8.6, displayHeight / 2.08)
    display.blit(imgSmallFinalBossP1, imgSmallFinalBossP1_RECT)
    if isButtonClickDetected(txtElectricCatP1_RECT):
        myP1 = ElectricCatProgmon()
        progmonP1 = "ElectricCat"
        progmonNameP1 = "Electric Cat"
    elif isButtonClickDetected(txtFireDragonP1_RECT):
        myP1 = FireDragonProgmon()
        progmonP1 = "FireDragon"
        progmonNameP1 = "Fire Dragon"
    elif isButtonClickDetected(txtWaterTurtleP1_RECT):
        myP1 = WaterTurtleProgmon()
        progmonP1 = "WaterTurtle"
        progmonNameP1 = "Water Turtle"
    # elif isButtonClickDetected(txtFinalBossP1_RECT):
    #     myP1 = FinalBossProgmon() # (UNFINISHED - NEED FINAL BOSS PROGMON)
    #     progmonP1 = "FinalBoss"
    #     progmonNameP1 = "Final Boss"

    # PLAYER AI
    txtAI, txtAI_RECT = createTextObject("Player AI's Progmon", largeText, WHITE)
    txtAI_RECT.center = (displayWidth / 1.3, displayHeight / 19)
    display.blit(txtAI, txtAI_RECT)
    pygame.draw.rect(display, BLACK, (displayWidth * .67, displayHeight * .1, 220, 320), 0) # FILLED BOX FOR AI PROGMON OPTIONS
    txtElectricCatAI, txtElectricCatAI_RECT = createTextObject("Electric Cat", smallText, WHITE)
    txtElectricCatAI_RECT.center = (displayWidth / 1.3, displayHeight / 7.5)
    display.blit(txtElectricCatAI, txtElectricCatAI_RECT)
    txtFireDragonAI, txtFireDragonAI_RECT = createTextObject("Fire Dragon", smallText, WHITE)
    txtFireDragonAI_RECT.center = (displayWidth / 1.3, displayHeight / 4)
    display.blit(txtFireDragonAI, txtFireDragonAI_RECT)
    txtWaterTurtleAI, txtWaterTurtleAI_RECT = createTextObject("Water Turtle", smallText, WHITE)
    txtWaterTurtleAI_RECT.center = (displayWidth / 1.3, displayHeight / 2.7)
    display.blit(txtWaterTurtleAI, txtWaterTurtleAI_RECT)
    txtFinalBossAI, txtFinalBossAI_RECT = createTextObject("Final Boss", smallText, WHITE)
    txtFinalBossAI_RECT.center = (displayWidth / 1.3, displayHeight / 2)
    display.blit(txtFinalBossAI, txtFinalBossAI_RECT)
    imgSmallElectricCatAI = pygame.image.load('Sprites/smallElectricCat.png')
    imgSmallElectricCatAI_RECT = imgSmallElectricCatAI.get_rect()
    imgSmallElectricCatAI_RECT.center = (displayWidth / 1.6, displayHeight / 7.5)
    display.blit(imgSmallElectricCatAI, imgSmallElectricCatAI_RECT)
    imgSmallFireDragonAI = pygame.image.load('Sprites/smallFireDragon.png')
    imgSmallFireDragonAI_RECT = imgSmallFireDragonAI.get_rect()
    imgSmallFireDragonAI_RECT.center = (displayWidth / 1.6, displayHeight / 4)
    display.blit(imgSmallFireDragonAI, imgSmallFireDragonAI_RECT)
    imgSmallWaterTurtleAI = pygame.image.load('Sprites/smallWaterTurtle.png')
    imgSmallWaterTurtleAI_RECT = imgSmallWaterTurtleAI.get_rect()
    imgSmallWaterTurtleAI_RECT.center = (displayWidth / 1.6, displayHeight / 2.7)
    display.blit(imgSmallWaterTurtleAI, imgSmallWaterTurtleAI_RECT)
    imgSmallFinalBossAI = pygame.image.load('Sprites/smallFinalBoss.png')
    imgSmallFinalBossAI_RECT = imgSmallFinalBossAI.get_rect()
    imgSmallFinalBossAI_RECT.center = (displayWidth / 1.577, displayHeight / 2.08)
    display.blit(imgSmallFinalBossAI, imgSmallFinalBossAI_RECT)
    if isButtonClickDetected(txtElectricCatAI_RECT):
        myAI = ElectricCatProgmon()
        progmonAI = "ElectricCat"
        progmonNameAI = "Electric Cat"
    elif isButtonClickDetected(txtFireDragonAI_RECT):
        myAI = FireDragonProgmon()
        progmonAI = "FireDragon"
        progmonNameAI = "Fire Dragon"
    elif isButtonClickDetected(txtWaterTurtleAI_RECT):
        myAI = WaterTurtleProgmon()
        progmonAI = "WaterTurtle"
        progmonNameAI = "Water Turtle"
    # elif isButtonClickDetected(txtFinalBossAI_RECT):
    #     myAI = FinalBossProgmon() # (UNFINISHED - NEED FINAL BOSS PROGMON)
    #     progmonAI = "FinalBoss"
    #     progmonNameAI = "Final Boss"

    # PLAY BUTTON
    txtPlay, txtPlay_RECT = createTextObject("PLAY", mediumText, WHITE)
    txtPlay_RECT.center = (displayWidth * .5, displayHeight * .9)
    display.blit(txtPlay, txtPlay_RECT)
    if isButtonClickDetected(txtPlay_RECT):
        if progmonP1 != "" and progmonAI != "":
            controlScreen("fightScreen")
        else:
            # (UNFINISHED - DISPLAY AN ERROR MESSAGE ON PYGAME DISPLAY)
            if progmonP1 == "":
                print("ERROR: Player 1 needs to select a Progmon") # TESTER CODE
            elif progmonAI == "":
                print("ERROR: Player AI needs to select a Progmon") # TESTER CODE

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

    # BACKGROUND
    imgBackground = pygame.image.load('Sprites/fightScreen.png')
    imgBackground_RECT = imgBackground.get_rect()
    imgBackground_RECT.center = (displayWidth * .5, displayHeight * .5)
    display.blit(imgBackground, imgBackground_RECT)

    # PLAYER 1
    txtNameP1, txtNameP1_RECT = createTextObject("Player P1", mediumText, WHITE)
    txtNameP1_RECT.center = (displayWidth * .175, displayHeight * .035)
    display.blit(txtNameP1, txtNameP1_RECT)
    txtProgmonP1, txtProgmonP1_RECT = createTextObject(progmonNameP1, mediumText, WHITE)
    txtProgmonP1_RECT.center = (displayWidth * .175, displayHeight * .105)
    display.blit(txtProgmonP1, txtProgmonP1_RECT)
    progmonHealthP1 = myP1.getCurrentHealth()
    txtHealthP1 = smallText.render(str(progmonHealthP1), True, WHITE, None)
    txtHealthP1_RECT = txtHealthP1.get_rect()
    txtHealthP1_RECT.center = (displayWidth * .28, displayHeight * .168)
    display.blit(txtHealthP1, txtHealthP1_RECT)
    pygame.draw.rect(display, WHITE, (displayWidth * .05, displayHeight * .14, 200, 40), 5) # UNFILLED BOX FOR PLAYER 1'S PROGMON HEALTH BAR
    pygame.draw.rect(display, RED, (displayWidth * .052, displayHeight * .141, 196, 37), 0) # FILLED BOX FOR PLAYER 1'S PROGMON HEALTH BAR
    pygame.draw.rect(display, LIGHT_GREEN, (displayWidth * .052, displayHeight * .141, 196 * (progmonHealthP1 / myP1.getHp()), 37), 0) # FILLED BOX FOR PLAYER 1'S PROGMON HEALTH BAR
    pygame.draw.rect(display, WHITE, (displayWidth * .037, displayHeight * .71, 480, 140), 0) # FILLED BOX FOR PLAYER 1'S MESSAGES
    if progmonP1 == "ElectricCat":
        imgProgmonP1 = pygame.image.load('Sprites/largeElectricCat.png')
    elif progmonP1 == "FireDragon":
        imgProgmonP1 = pygame.image.load('Sprites/largeFireDragon.png')
    elif progmonP1 == "WaterTurtle":
        imgProgmonP1 = pygame.image.load('Sprites/largeWaterTurtle.png')
    elif progmonP1 == "FinalBoss":
        imgProgmonP1 = pygame.image.load('Sprites/largeFinalBoss.png')
    imgProgmonP1_RECT = imgProgmonP1.get_rect()
    imgProgmonP1_RECT.center = (displayWidth * .2, displayHeight * .45)
    display.blit(imgProgmonP1, imgProgmonP1_RECT)

    # PLAYER AI
    txtNameAI, txtNameAI_RECT = createTextObject("Player AI", mediumText, WHITE)
    txtNameAI_RECT.center = (displayWidth * .825, displayHeight * .035)
    display.blit(txtNameAI, txtNameAI_RECT)
    txtProgmonAI, txtProgmonAI_RECT = createTextObject(progmonNameAI, mediumText, WHITE)
    txtProgmonAI_RECT.center = (displayWidth * .825, displayHeight * .105)
    display.blit(txtProgmonAI, txtProgmonAI_RECT)
    progmonHealthAI = myAI.getCurrentHealth()
    txtHealthAI = smallText.render(str(progmonHealthAI), True, WHITE, None)
    txtHealthAI_RECT = txtHealthAI.get_rect()
    txtHealthAI_RECT.center = (displayWidth * .925, displayHeight * .168)
    display.blit(txtHealthAI, txtHealthAI_RECT)
    pygame.draw.rect(display, WHITE, (displayWidth * .699, displayHeight * .14, 200, 40), 5) # UNFILLED BOX FOR PLAYER AI'S PROGMON HEALTH BAR
    pygame.draw.rect(display, RED, (displayWidth * .701, displayHeight * .141, 196, 37), 0) # FILLED BOX FOR PLAYER AI'S PROGMON HEALTH BAR
    pygame.draw.rect(display, LIGHT_GREEN, (displayWidth * .701, displayHeight * .141, 196 * (progmonHealthAI / myAI.getHp()), 37), 0) # FILLED BOX FOR PLAYER AI'S PROGMON HEALTH BAR
    pygame.draw.rect(display, WHITE, (displayWidth * .518, displayHeight * .71, 480, 140), 0) # FILLED BOX FOR PLAYER AI'S MESSAGES
    if progmonAI == "ElectricCat":
        progmonNameAI = "Electric Cat"
        imgProgmonAI = pygame.image.load('Sprites/largeElectricCat.png')
    elif progmonAI == "FireDragon":
        progmonNameAI = "Fire Dragon"
        imgProgmonAI = pygame.image.load('Sprites/largeFireDragon.png')
    elif progmonAI == "WaterTurtle":
        progmonNameAI = "Water Turtle"
        imgProgmonAI = pygame.image.load('Sprites/largeWaterTurtle.png')
    elif progmonAI == "FinalBoss":
        imgProgmonAI = pygame.image.load('Sprites/largeFinalBoss.png')
    imgProgmonAI_RECT = imgProgmonAI.get_rect()
    imgProgmonAI_RECT.center = (displayWidth * .8, displayHeight * .45)
    display.blit(imgProgmonAI, imgProgmonAI_RECT)

    # BATTLE MENU
    pygame.draw.rect(display, WHITE, (displayWidth * .037, displayHeight * .92, 1000, 50), 0) # FILLED BOX FOR BATTLE MENU BUTTONS
    txtFight, txtFight_RECT = createTextObject("FIGHT", smallText, BLACK)
    txtFight_RECT.center = (displayWidth * 0.2, displayHeight * 0.955)
    display.blit(txtFight, txtFight_RECT)
    txtBag, txtBag_RECT = createTextObject("BAG", smallText, BLACK)
    txtBag_RECT.center = (displayWidth * 0.4, displayHeight * 0.955)
    display.blit(txtBag, txtBag_RECT)
    txtProgmon, txtProgmon_RECT = createTextObject("PROGMON", smallText, BLACK)
    txtProgmon_RECT.center = (displayWidth * 0.6, displayHeight * 0.955)
    display.blit(txtProgmon, txtProgmon_RECT)
    txtQuit, txtQuit_RECT = createTextObject("QUIT", smallText, BLACK)
    txtQuit_RECT.center = (displayWidth * 0.8, displayHeight * 0.955)
    display.blit(txtQuit, txtQuit_RECT)

    if myP1.getStunStatus() == False:
        txtMsgP1, txtMsgP1_RECT = createTextObject("What would you like to do?", miniText, BLACK)
        txtMsgP1_RECT.center = (displayWidth * .25, displayHeight * .75)
        display.blit(txtMsgP1, txtMsgP1_RECT)
        # TRACK BATTLE MENU BUTTONS
        if isButtonClickDetected(txtFight_RECT):
            controlScreen("fightMenu")
        elif isButtonClickDetected(txtBag_RECT):
            if myP1.bagEmpty() == False:
                controlScreen("bagMenu")
            else:
                txtMsgP1, txtMsgP1_RECT = createTextObject("Your Bag is empty!", miniText, BLACK)
                txtMsgP1_RECT.center = (displayWidth * .25, displayHeight * .8)
                display.blit(txtMsgP1, txtMsgP1_RECT)
                pygame.time.delay(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
                controlScreen("fightScreen")
        elif isButtonClickDetected(txtProgmon_RECT):
            controlScreen("progmonMenu")
        elif isButtonClickDetected(txtQuit_RECT):
            quitGame()
    elif myP1.getStunStatus() == True:
        myP1.stunned = False
        txtMsgP1, txtMsgP1_RECT = createTextObject(("{} has been stunned by {}!".format(progmonNameP1, progmonNameAI)), miniText, BLACK)
        txtMsgP1_RECT.center = (displayWidth * .25, displayHeight * .75)
        display.blit(txtMsgP1, txtMsgP1_RECT)
        pygame.time.delay(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
        AITurn()

def fightMenu():
    """
    Displays and tracks the Fight Menu for Player 1 after "FIGHT" has been clicked
    Args:
        None
    Returns:
        None
    """
    global myP1
    global progmonP1
    global progmonNameP1
    global myAI

    pygame.gfxdraw.box(display, (displayWidth * 0.037, displayHeight * 0.92, 1000, 50), WHITE) # FILLED BOX FOR FIGHT MENU BUTTONS

    pygame.draw.rect(display, WHITE, (displayWidth * .037, displayHeight * .71, 480, 140), 0) # FILLED BOX FOR PLAYER 1'S MESSAGES
    txtMsgP1, txtMsgP1_RECT = createTextObject("Which attack would you like to use?", miniText, BLACK)
    txtMsgP1_RECT.center = (displayWidth * .25, displayHeight * .75)
    display.blit(txtMsgP1, txtMsgP1_RECT)

    # ATTACKS
    attackList = myP1.getAttackList()
    if len(attackList) == 4:
        txtAttack1, txtAttack1_RECT = createTextObject(str(attackList[0]), miniText, BLACK)
        txtAttack1_RECT.center = (displayWidth * .2, displayHeight * .955)
        display.blit(txtAttack1, txtAttack1_RECT)
        txtAttack2, txtAttack2_RECT = createTextObject(str(attackList[1]), miniText, BLACK)
        txtAttack2_RECT.center = (displayWidth * .4, displayHeight * .955)
        display.blit(txtAttack2, txtAttack2_RECT)
        txtAttack3, txtAttack3_RECT = createTextObject(str(attackList[2]), miniText, BLACK)
        txtAttack3_RECT.center = (displayWidth * .6, displayHeight * .955)
        display.blit(txtAttack3, txtAttack3_RECT)
        txtAttack4, txtAttack4_RECT = createTextObject(str(attackList[3]), miniText, BLACK)
        txtAttack4_RECT.center = (displayWidth * .8, displayHeight * .955)
        display.blit(txtAttack4, txtAttack4_RECT)

    # TRACK FIGHT MENU BUTTONS
    if isButtonClickDetected(txtAttack1_RECT):
        attackHit = myP1.attack1(myAI)
        txtMsgP1, txtMsgP1_RECT = createTextObject(("{} used {}!".format(progmonNameP1, attackList[0])), miniText, BLACK)
        txtMsgP1_RECT.center = (displayWidth * .25, displayHeight * .8)
        display.blit(txtMsgP1, txtMsgP1_RECT)
        pygame.time.delay(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
        if attackHit[0] == True:
            txtMsgP1, txtMsgP1_RECT = createTextObject("{}".format(attackHit[1]), miniText, BLACK)
            txtMsgP1_RECT.center = (displayWidth * .25, displayHeight * .85)
            display.blit(txtMsgP1, txtMsgP1_RECT)
            pygame.time.delay(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
        else:
            txtMsgP1, txtMsgP1_RECT = createTextObject("{}".format(attackHit[1]), miniText, BLACK)
            txtMsgP1_RECT.center = (displayWidth * .25, displayHeight * .85)
            display.blit(txtMsgP1, txtMsgP1_RECT)
            pygame.time.delay(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE

        if myAI.checkAlive():
            pygame.time.delay(1200) # WAIT BEFORE THE AI GETS TO GO
            AITurn()
            controlScreen("fightScreen")
        else:
            pygame.draw.rect(display, WHITE, (displayWidth * .037, displayHeight * .71, 480, 140), 0) # FILLED BOX FOR PLAYER 1'S MESSAGES
            txtMsgP1, txtMsgP1_RECT = createTextObject(("Player AI's {} has fainted. You win!".format(progmonNameAI)), miniText, BLACK)
            txtMsgP1_RECT.center = (displayWidth * .25, displayHeight * .8)
            display.blit(txtMsgP1, txtMsgP1_RECT)
            pygame.time.delay(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
            controlScreen("endScreen") # (UNFINISHED - NEED END SCREEN TO BE CREATED)

    if isButtonClickDetected(txtAttack2_RECT):
        attackHit = myP1.attack2(myAI)
        txtMsgP1, txtMsgP1_RECT = createTextObject(("{} used {}!".format(progmonNameP1, attackList[1])), miniText, BLACK)
        txtMsgP1_RECT.center = (displayWidth * .25, displayHeight * .8)
        display.blit(txtMsgP1, txtMsgP1_RECT)
        pygame.time.delay(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
        if attackHit[0] == True:
            txtMsgP1, txtMsgP1_RECT = createTextObject("{}".format(attackHit[1]), miniText, BLACK)
            txtMsgP1_RECT.center = (displayWidth * .25, displayHeight * .85)
            display.blit(txtMsgP1, txtMsgP1_RECT)
            pygame.time.delay(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
        else:
            txtMsgP1, txtMsgP1_RECT = createTextObject("{}".format(attackHit[1]), miniText, BLACK)
            txtMsgP1_RECT.center = (displayWidth * .25, displayHeight * .85)
            display.blit(txtMsgP1, txtMsgP1_RECT)
            pygame.time.delay(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE

        if myAI.checkAlive():
            pygame.time.delay(1200) # WAIT BEFORE THE AI GETS TO GO
            AITurn()
            controlScreen("fightScreen")
        else:
            pygame.draw.rect(display, WHITE, (displayWidth * .037, displayHeight * .71, 480, 140), 0) # FILLED BOX FOR PLAYER 1'S MESSAGES
            txtMsgP1, txtMsgP1_RECT = createTextObject(("Player AI's {} has fainted. You win!".format(progmonNameAI)), miniText, BLACK)
            txtMsgP1_RECT.center = (displayWidth * .25, displayHeight * .8)
            display.blit(txtMsgP1, txtMsgP1_RECT)
            pygame.time.delay(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
            controlScreen("endScreen") # (UNFINISHED - NEED END SCREEN TO BE CREATED)

    if isButtonClickDetected(txtAttack3_RECT):
        attackHit = myP1.attack3(myAI)
        txtMsgP1, txtMsgP1_RECT = createTextObject(("{} used {}!".format(progmonNameP1, attackList[2])), miniText, BLACK)
        txtMsgP1_RECT.center = (displayWidth * .25, displayHeight * .8)
        display.blit(txtMsgP1, txtMsgP1_RECT)
        pygame.time.delay(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
        if attackHit[0] == True:
            txtMsgP1, txtMsgP1_RECT = createTextObject("{}".format(attackHit[1]), miniText, BLACK)
            txtMsgP1_RECT.center = (displayWidth * .25, displayHeight * .85)
            display.blit(txtMsgP1, txtMsgP1_RECT)
            pygame.time.delay(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
        else:
            txtMsgP1, txtMsgP1_RECT = createTextObject("{}".format(attackHit[1]), miniText, BLACK)
            txtMsgP1_RECT.center = (displayWidth * .25, displayHeight * .85)
            display.blit(txtMsgP1, txtMsgP1_RECT)
            pygame.time.delay(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE

        if myAI.checkAlive():
            pygame.time.delay(1200) # WAIT BEFORE THE AI GETS TO GO
            AITurn()
            controlScreen("fightScreen")
        else:
            pygame.draw.rect(display, WHITE, (displayWidth * .037, displayHeight * .71, 480, 140), 0) # FILLED BOX FOR PLAYER 1'S MESSAGES
            txtMsgP1, txtMsgP1_RECT = createTextObject(("Player AI's {} has fainted. You win!".format(progmonNameAI)), miniText, BLACK)
            txtMsgP1_RECT.center = (displayWidth * .25, displayHeight * .8)
            display.blit(txtMsgP1, txtMsgP1_RECT)
            pygame.time.delay(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
            controlScreen("endScreen") # (UNFINISHED - NEED END SCREEN TO BE CREATED)

    if isButtonClickDetected(txtAttack4_RECT):
        attackHit = myP1.attack4(myAI)
        txtMsgP1, txtMsgP1_RECT = createTextObject(("{} used {}!".format(progmonNameP1, attackList[3])), miniText, BLACK)
        txtMsgP1_RECT.center = (displayWidth * .25, displayHeight * .8)
        display.blit(txtMsgP1, txtMsgP1_RECT)
        pygame.time.delay(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
        if attackHit[0] == True:
            txtMsgP1, txtMsgP1_RECT = createTextObject("{}".format(attackHit[1]), miniText, BLACK)
            txtMsgP1_RECT.center = (displayWidth * .25, displayHeight * .85)
            display.blit(txtMsgP1, txtMsgP1_RECT)
            pygame.time.delay(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
        else:
            txtMsgP1, txtMsgP1_RECT = createTextObject("{}".format(attackHit[1]), miniText, BLACK)
            txtMsgP1_RECT.center = (displayWidth * .25, displayHeight * .85)
            display.blit(txtMsgP1, txtMsgP1_RECT)
            pygame.time.delay(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE

        if myAI.checkAlive():
            pygame.time.delay(1200) # WAIT BEFORE THE AI GETS TO GO
            AITurn()
            controlScreen("fightScreen")
        else:
            pygame.draw.rect(display, WHITE, (displayWidth * .037, displayHeight * .71, 480, 140), 0) # FILLED BOX FOR PLAYER 1'S MESSAGES
            txtMsgP1, txtMsgP1_RECT = createTextObject(("Player AI's {} has fainted. You win!".format(progmonNameAI)), miniText, BLACK)
            txtMsgP1_RECT.center = (displayWidth * .25, displayHeight * .8)
            display.blit(txtMsgP1, txtMsgP1_RECT)
            pygame.time.delay(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE
            controlScreen("endScreen") # (UNFINISHED - NEED END SCREEN TO BE CREATED)

def bagMenu():
    """
    Displays and tracks the Bag Menu for Player 1 after "BAG" has been clicked
    Args:
        None
    Returns:
        None
    """
    pygame.gfxdraw.box(display, (displayWidth * 0.037, displayHeight * 0.92, 1000, 50), WHITE) # FILLED BOX FOR BAG MENU BUTTONS

    pygame.draw.rect(display, WHITE, (displayWidth * .037, displayHeight * .71, 480, 140), 0) # FILLED BOX FOR PLAYER 1'S MESSAGES
    txtMsgP1, txtMsgP1_RECT = createTextObject("Select an item to use", miniText, BLACK)
    txtMsgP1_RECT.center = (displayWidth * .25, displayHeight * .75)
    display.blit(txtMsgP1, txtMsgP1_RECT)

    # ITEMS
    if "healthPotion" in myP1.getBag():
        txtHealthPotion, txtHealthPotion_RECT = createTextObject("Health Potion", miniText, BLACK)
        txtHealthPotion_RECT.center = (displayWidth * .2, displayHeight * .955)
        display.blit(txtHealthPotion, txtHealthPotion_RECT)
        if isButtonClickDetected(txtHealthPotion_RECT):
            myP1.useHealthPotion()
            txtMsgP1, txtMsgP1_RECT = createTextObject("Player 1 has used a Health Potion!", miniText, BLACK)
            txtMsgP1_RECT.center = (displayWidth * .25, displayHeight * .8)
            display.blit(txtMsgP1, txtMsgP1_RECT)


            # (UNFINISHED - LOWER MESSAGE TO PLAYER 1)


            pygame.time.delay(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE

            pygame.time.delay(1200) # WAIT BEFORE THE AI GETS TO GO
            AITurn()
            controlScreen("fightScreen")

    if "statBoost" in myP1.getBag():
        txtStatBoost, txtStatBoost_RECT = createTextObject("Stat Boost", miniText, BLACK)
        txtStatBoost_RECT.center = (displayWidth * .4, displayHeight * .955)
        display.blit(txtStatBoost, txtStatBoost_RECT)
        if isButtonClickDetected(txtStatBoost_RECT):
            myP1.useStatBoost()
            txtMsgP1, txtMsgP1_RECT = createTextObject("Player 1 has used a Stat Boost!", miniText, BLACK)
            txtMsgP1_RECT.center = (displayWidth * .25, displayHeight * .8)
            display.blit(txtMsgP1, txtMsgP1_RECT)


            # (UNFINISHED - LOWER MESSAGE TO PLAYER 1)


            pygame.time.delay(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE

            pygame.time.delay(1200) # WAIT BEFORE THE AI GETS TO GO
            AITurn()
            controlScreen("fightScreen")

    if "defenseBoost" in myP1.getBag():
        txtDefenseBoost, txtDefenseBoost_RECT = createTextObject("Defense Boost", miniText, BLACK)
        txtDefenseBoost_RECT.center = (displayWidth * .6, displayHeight * .955)
        display.blit(txtDefenseBoost, txtDefenseBoost_RECT)
        if isButtonClickDetected(txtDefenseBoost_RECT):
            myP1.useDefenseBoost()
            txtMsgP1, txtMsgP1_RECT = createTextObject("Player 1 has used a Defense Boost!", miniText, BLACK)
            txtMsgP1_RECT.center = (displayWidth * .25, displayHeight * .8)
            display.blit(txtMsgP1, txtMsgP1_RECT)


            # (UNFINISHED - LOWER MESSAGE TO PLAYER 1)


            pygame.time.delay(3000) # WAIT FOR PLAYER 1 TO READ THE MESSAGE

            pygame.time.delay(1200) # WAIT BEFORE THE AI GETS TO GO
            AITurn()
            controlScreen("fightScreen")

def progmonMenu():
    """
    Displays and tracks the Progmon Menu for Player 1 after "PROGMON" has been clicked
    Args:
        None
    Returns:
        None
    """
    # (UNFINISHED - PROGMON SWITCHING)
    print("PROGMON SWITCHING HAS NOT BEEN IMPLEMENTED")

def endScreen():
    display.fill(GREEN)

    #Display progmon of 2 players
    PlayerVS_AItext = progmonP1 + "   VS  " + progmonAI
    TextSurf, TextRect = createTextObject(PlayerVS_AItext, mediumText, BLACK)
    TextRect.center = ((displayWidth / 2), (displayHeight * .05))
    display.blit(TextSurf, TextRect)

    #Display Player1's progmon's image
    if progmonP1 == "ElectricCat":    
        imageSmallElectricCatP1 = pygame.image.load('Sprites/smallElectricCat.png')
        imageSmallElectricCatP1_RECT = imageSmallElectricCatP1.get_rect()
        imageSmallElectricCatP1_RECT.center = (displayWidth / 4.65, displayHeight * .06)
        display.blit(imageSmallElectricCatP1, imageSmallElectricCatP1_RECT)
    elif progmonP1 == "FireDragon":
        imageSmallFireDragonP1 = pygame.image.load('Sprites/smallFireDragon.png')
        imageSmallFireDragonP1_RECT = imageSmallFireDragonP1.get_rect()
        imageSmallFireDragonP1_RECT.center = (displayWidth / 4.65, displayHeight * .06)
        display.blit(imageSmallFireDragonP1, imageSmallFireDragonP1_RECT)
    elif progmonP1 == "WalterTurtle":
        imgSmallWaterTurtleP1 = pygame.image.load('Sprites/smallWaterTurtle.png')
        imgSmallWaterTurtleP1_RECT = imgSmallWaterTurtleP1.get_rect()
        imgSmallWaterTurtleP1_RECT.center = (displayWidth / 4.65, displayHeight * .06)
        display.blit(imgSmallWaterTurtleP1, imgSmallWaterTurtleP1_RECT)
    elif progmonP1 == "FinalBoss":
        imgSmallFinalBossP1 = pygame.image.load('Sprites/smallFinalBoss.png')
        imgSmallFinalBossP1_RECT = imgSmallFinalBossP1.get_rect()
        imgSmallFinalBossP1_RECT.center = (displayWidth / 4.65, displayHeight * .06)
        display.blit(imgSmallFinalBossP1, imgSmallFinalBossP1_RECT)


    #Display AI's progmon's image
    if progmonAI == "ElectricCat":
        imageSmallElectricCatAI = pygame.image.load('Sprites/smallElectricCat.png')
        imageSmallElectricCatAI_RECT = imageSmallElectricCatAI.get_rect()
        imageSmallElectricCatAI_RECT.center = (displayWidth / 1.26, displayHeight * .06)
        display.blit(imageSmallElectricCatAI, imageSmallElectricCatAI_RECT)
    elif progmonAI == "FireDragon":
        imageSmallFireDragonAI = pygame.image.load('Sprites/smallFireDragon.png')
        imageSmallFireDragonAI_RECT = imageSmallFireDragonAI.get_rect()
        imageSmallFireDragonAI_RECT.center = (displayWidth / 1.26, displayHeight * .06)
        display.blit(imageSmallFireDragonAI, imageSmallFireDragonAI_RECT)
    elif progmonAI == "WalterTurtle":
        imgSmallWaterTurtleAI = pygame.image.load('Sprites/smallWaterTurtle.png')
        imgSmallWaterTurtleAI_RECT = imgSmallWaterTurtleAI.get_rect()
        imgSmallWaterTurtleAI_RECT.center = (displayWidth / 1.26, displayHeight * .06)
        display.blit(imgSmallWaterTurtleAI, imgSmallWaterTurtleAI_RECT)
    elif progmonAI == "FinalBoss":
        imgSmallFinalBossAI = pygame.image.load('Sprites/smallFinalBoss.png')
        imgSmallFinalBossAI_RECT = imgSmallFinalBossAI.get_rect()
        imgSmallFinalBossAI_RECT.center = (displayWidth / 1.26, displayHeight * .06)
        display.blit(imgSmallFinalBossAI, imgSmallFinalBossAI_RECT)

    #Display winner of the game
    WinnerText = pygame.font.Font('freesansbold.ttf', 50)
    text = "winner +  wins!"
    TextSurf, TextRect = createTextObject(text, WinnerText, BLACK)
    TextRect.center = ((displayWidth / 2), (displayHeight * .14))
    display.blit(TextSurf, TextRect)


    #Score for Player 1
    text_Player1 = "Player 1"
    # creates text surface variable and text rectangle variable
    TextSurf, TextRect = createTextObject(text_Player1, largeText, BLACK)
    # modifies the center of text rectangle based on pygame GUI window
    TextRect.center = ((displayWidth/4.2), (displayHeight*.39))
    display.blit(TextSurf, TextRect)


    text_Player1_Attack = "Total Attacked: " 
    TextSurf, TextRect = createTextObject(text_Player1_Attack, mediumText, BLACK)
    TextRect.center = ((displayWidth/4), (displayHeight*.55))
    display.blit(TextSurf, TextRect)


    # hit1 = ((totalhitPlayer1 / totalAttackPlayer1)*100)
    # hit1Percentage = round(hit1, 2)
    # missed1 = ((totalMissedPlayer1 / totalAttackPlayer1)*100)
    # missed1Percentage = round(missed1, 2)

    text_Player1_Hit = "Hit in %: "
    TextSurf, TextRect = createTextObject(text_Player1_Hit, mediumText, BLACK)
    TextRect.center = ((displayWidth/4), (displayHeight*.65))
    display.blit(TextSurf, TextRect)


    text_Player1_Miss = "Missed in %: " 
    TextSurf, TextRect = createTextObject(text_Player1_Miss, mediumText, BLACK)
    TextRect.center = ((displayWidth/4), (displayHeight*.75))
    display.blit(TextSurf, TextRect)


    #Score for AI
    text_PlayerAI = "Player AI"
    TextSurf, TextRect = createTextObject(text_PlayerAI, largeText, BLACK)
    TextRect.center = ((displayWidth / 1.3), (displayHeight * .39))
    display.blit(TextSurf, TextRect)

    text_PlayerAI_Attack = "Total Attacked: "
    TextSurf, TextRect = createTextObject(text_PlayerAI_Attack, mediumText, BLACK)
    TextRect.center = ((displayWidth / 1.3), (displayHeight * .55))
    display.blit(TextSurf, TextRect)

    # hit2 = ((totalhitPlayer2 / totalAttackPlayer2) * 100)
    # hit2Percentage = round(hit2, 2)
    # missed2 = ((totalMissedPlayer2 / totalAttackPlayer2) * 100)
    # missed2Percentage = round(missed2, 2)

    text_PlayerAI_Hit = "Hit in %: "
    TextSurf, TextRect = createTextObject(text_PlayerAI_Hit, mediumText, BLACK)
    TextRect.center = ((displayWidth / 1.3), (displayHeight * .65))
    display.blit(TextSurf, TextRect) 
           
    text_PlayerAI_Miss = "Missed in %: " 
    TextSurf, TextRect = createTextObject(text_PlayerAI_Miss, mediumText, BLACK)
    TextRect.center = ((displayWidth / 1.3), (displayHeight * .75))
    display.blit(TextSurf, TextRect)
















    
    #update Display
    pygame.display.update()


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
        # (UNFINISHED - DISPLAY AN ERROR MESSAGE ON PYGAME DISPLAY)
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
    global myP1
    global myAI

    if(myP1.checkAlive() != True):
        print("P1 progmon has died")
        controlScreen("endScreen") # (UNFINISHED - NEED END SCREEN TO BE CREATED)

    P1critical = (myP1.getCurrentHealth() / myP1.getHp()) #check if P1 is at critical health (<= 20% of max health)
    AIcritical = (myP1.getCurrentHealth() / myP1.getHp()) #check if AI is at critical health (<= 20% of max health)

    if(myAI.getStunStatus() == True): #if stunned, skip turn
        myAI.stunned = False
        print("The AI was stunned, turn skipped!\n")
        #DISPLAY: "The AI was stunned, turn skipped!"
    elif(P1critical <= .2): #if P1 is critical, always attack
        messageToShow = myAI.AIAttack(myP1)
        print("{}\n".format(messageToShow))
        #DISPLAY: messageToShow
    elif((AIcritical <= .2) and ("healthPotion" in myAI.getBag())): #if AI is critical but P1 is not, use healing potion (if AI has it)
        myAI.useHealthPotion()
        #DISPLAY: the same thing that use health potion is printing to terminal
    elif(AIcritical <= .2): #if AI is critical but P1 is not and there is no healing potion, 30% chance to run (else attack)
        percentage = random.randint(1, 101)
        if(percentage <= 30):
            print("AI will run")
            #make AI run
        else:
            messageToShow = myAI.AIAttack(myP1)        #go back and remove second parameter
            print("{}\n".format(messageToShow))
            #DISPLAY: messageToShow
    else: #give 70% chance to attack, 20% to use bag item (if bag empty, attack), 7% chance to switch progmon (currently disabled) 3% chance to run
        print("WORK IN PROGRESS")
        percentage = random.randint(1, 101)
        if(percentage <= 70):
            messageToShow = myAI.AIAttack(myP1)
            print("{}\n".format(messageToShow))
            #DISPLAY: messageToShow
        elif(percentage <= 90):
            if(myAI.bagEmpty() == True): #attack
                messageToShow = myAI.AIAttack(myP1)
                print("{}\n".format(messageToShow))
                #DISPLAY: messageToShow
            else:
                if("statBoost" in myAI.getBag()):
                    myAI.useStatBoost()
                    #DISPLAY: the same thing that use stat potion is printing to terminal
                elif("defenseBoost" in myAI.getBag()):
                    myAI.useDefenseBoost()
                    #DISPLAY: the same thing that use defense boost is printing to terminal
                elif("healthPotion" in myAI.getBag()):
                    myAI.useHealthPotion()
                    #DISPLAY: the same thing that use health potion is printing to terminal
        elif(percentage <= 97):
            print("This will switch progmon\n")
        else:
            print("AI will run")
            #make AI run

if __name__ == "__main__":
    controlScreen("startScreen")

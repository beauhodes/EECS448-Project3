import random
import pygame
import pygame.gfxdraw
from fireDragon import FireDragon
from electricCat import ElectricCat

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
playerMove = ""
attackChoiceP1 = ""
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

def isPointInRect(x, y, rect):
    """
    Checks if coordinate (x, y) is within the bounds of a Pygame.Rect object (rect.x, rect.y)
    Args:
        x (float) - x coordinate
        y (float) - y coordinate
        rect (Pygame.Rect) - object to see if x any y are in
    Returns:
        (bool) - True if (x, y) is in rect, otherwise False
    """
    if x < rect.x + rect.width and x > rect.x and y < rect.y + rect.height and y > rect.y:
        return True
    return False

def displayStartScreen():
    """
    Displays all objects on the Start Screen
    Args:
        None
    Returns:
        None
    """
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

    # PLAY BUTTON
    textPlay, textPlay_RECT = createTextObject("PLAY", mediumText)
    textPlay_RECT.center = (displayWidth / 2, displayHeight / 1.2)

    # DISPLAY TEXT OBJECTS AND IMAGES
    display.fill(WHITE)
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

def trackButtonsStartScreen():
    """
    Handles all button input on the Start Screen
    Args:
        None
    Returns:
        None
    """
    global progmonP1
    global myP1
    global progmonAI
    global myAI
    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE

    # PLAYER 1'S BUTTONS
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

    # PLAYER AI'S BUTTONS
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

    # PLAY BUTTON
    if displayWidth * 0.45 + 110 > mouse[0] > displayWidth * 0.45 and displayHeight * 0.805 + 40 > mouse[1] > displayHeight * 0.805: # VALID LOCATION OF PLAY BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.45, displayHeight * 0.805, 110, 40), 5) # BOX AROUND PLAY
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if progmonP1 != "" and progmonAI != "":
                if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.45, displayHeight * 0.805, 110, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PLAY BUTTON
                    controlScreen("fightScreen")
            else:
                if progmonP1 == "":
                    print("ERROR: Player 1 needs to select a Progmon")
                    pygame.time.delay(500) # WAIT TO PREVENT MULTIPLE BUTTON CLICKS
                elif progmonAI == "":
                    print("ERROR: Player AI needs to select a Progmon")
                    pygame.time.delay(500) # WAIT TO PREVENT MULTIPLE BUTTON CLICKS

def displayFightScreen():
    """
    Displays all objects on the Fight Screen
    Args:
        None
    Returns:
        None
    """
    global myP1
    global progmonNameP1
    global myAI
    global progmonNameAI

    # BATTLE MENU OPTIONS
    textFight, textFight_RECT = createTextObject("FIGHT", smallText)
    textFight_RECT.center = (displayWidth / 1.4, displayHeight / 1.2)
    textBag, textBag_RECT = createTextObject("BAG", smallText)
    textBag_RECT.center = (displayWidth / 1.1, displayHeight / 1.2)
    textProgmon, textProgmon_RECT = createTextObject("PROGMON", smallText)
    textProgmon_RECT.center = (displayWidth / 1.4, displayHeight / 1.1)
    textQuit, textQuit_RECT = createTextObject("QUIT", smallText)
    textQuit_RECT.center = (displayWidth / 1.1, displayHeight / 1.1)

    # (UNFINISHED) CREATE USER INPUT PROMPT MESSAGE
    textUserPrompt, textUserPrompt_RECT = createTextObject("What would you like to do?", smallText)
    textUserPrompt_RECT.center = (displayWidth / 3.7, displayHeight / 1.2)

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
    textHealthP1_RECT.center = (displayWidth / 4.5, displayHeight / 6)

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
    textHealthAI_RECT.center = (displayWidth / 1.3, displayHeight / 6)

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
    display.blit(textUserPrompt, textUserPrompt_RECT)

def trackButtonsFightScreen():
    """
    Handles all button input on the Fight Screen
    Args:
        None
    Returns:
        None
    """
    global playerMove
    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE

    # THESE DO NOT DISPLAY WHEN INSIDE OF displayFightScreen()
    pygame.draw.rect(display, BLACK, (displayWidth * 0.62, displayHeight * 0.79, 370, 120), 5) # BOX AROUND BATTLE MENU OPTIONS
    pygame.draw.rect(display, BLACK, (displayWidth * 0.06, displayHeight * 0.065, 350, 100), 5) # BOX AROUND PLAYER 1'S PROGMON NAME AND HEALTH
    pygame.draw.rect(display, BLACK, (displayWidth * 0.6, displayHeight * 0.065, 350, 100), 5) # BOX AROUND PLAYER AI'S PROGMON NAME AND HEALTH
    pygame.draw.rect(display, BLACK, (displayWidth * 0.06, displayHeight * 0.79, 450, 100), 5) # BOX AROUND USER INPUT PROMPT MESSAGE

    # BATTLE MENU BUTTONS
    if displayWidth * 0.665 + 110 > mouse[0] > displayWidth * 0.665 and displayHeight * 0.805 + 40 > mouse[1] > displayHeight * 0.805: # VALID LOCATION OF FIGHT BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.665, displayHeight * 0.805, 110, 40), 5) # BOX AROUND FIGHT ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.665, displayHeight * 0.805, 110, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR FIGHT BUTTON
                playerMove = "FIGHT"
                pygame.time.delay(500) # WAIT TO PREVENT MULTIPLE BUTTON CLICKS
                controlScreen("fightMenu")
                # p1Attack = random.randint(0, 5)
                # # print("p1Attack =", p1Attack) # TESTER CODE
                # if progmonP1 == "FireDragon":
                #     if p1Attack == 1:
                #         print("Player 1's", progmonNameP1, "used Roar!")
                #         myP1.RoarAttack(myAI)
                #     elif p1Attack == 2:
                #         print("Player 1's", progmonNameP1, "used Claw Swipe!")
                #         myP1.ClawSwipeAttack(myAI)
                #     elif p1Attack == 3:
                #         print("Player 1's", progmonNameP1, "used Fire Breath!")
                #         myP1.FireBreathAttack(myAI)
                #     elif p1Attack == 4:
                #         print("Player 1's", progmonNameP1, "used Tail Whip!")
                #         myP1.TailWhipAttack(myAI)
                # elif progmonP1 == "ElectricCat":
                #     if p1Attack == 1:
                #         print("Player 1's", progmonNameP1, "used Lightning Bolt!")
                #         myP1.LightningBoltAttack(myAI)
                #     elif p1Attack == 2:
                #         print("Player 1's", progmonNameP1, "used Electric Scratch!")
                #         myP1.ElectricScratchAttack(myAI)
                #     elif p1Attack == 3:
                #         print("Player 1's", progmonNameP1, "used Energy Beam!")
                #         myP1.EnergyBeamAttack(myAI)
                #     elif p1Attack == 4:
                #         print("Player 1's", progmonNameP1, "used Bite!")
                #         myP1.BiteAttack(myAI)
                if myAI.checkAlive() != True:
                    print("Player AI's", progmonNameAI, "has fainted. You win!\n")
                    quitGame()
                # pygame.time.delay(1200) # WAIT BEFORE THE AI GETS TO GO
                # AITurn()
    elif displayWidth * 0.63 + 180 > mouse[0] > displayWidth * 0.63 and displayHeight * 0.88 + 40 > mouse[1] > displayHeight * 0.88: # VALID LOCATION OF PROGMON BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.63, displayHeight * 0.88, 180, 40), 5) # BOX AROUND PROGMON ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.63, displayHeight * 0.88, 180, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PROGMON BUTTON
                playerMove = "PROGMON"
                pygame.time.delay(500) # WAIT TO PREVENT MULTIPLE BUTTON CLICKS
                controlScreen("progmonMenu")
    elif displayWidth * 0.87 + 80 > mouse[0] > displayWidth * 0.87 and displayHeight * 0.805 + 40 > mouse[1] > displayHeight * 0.805: # VALID LOCATION OF BAG BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.87, displayHeight * 0.805, 80, 40), 5) # BOX AROUND BAG ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.87, displayHeight * 0.805, 80, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR BAG BUTTON
                playerMove = "BAG"
                pygame.time.delay(500) # WAIT TO PREVENT MULTIPLE BUTTON CLICKS
                controlScreen("bagMenu")
                # if myP1.bagEmpty():
                #     print("Player 1 has nothing in their Bag.\n")
                #     playerMove = "FIGHT"
                #     pygame.time.delay(500) # WAIT TO PREVENT MULTIPLE BUTTON CLICKS
                #     return
                # else:
                #     myP1.useHealthPotion()
                #     print("Player 1 has used a Health Potion!\n")
                # pygame.time.delay(1200) # WAIT BEFORE THE AI GETS TO GO
                # AITurn()
    elif displayWidth * 0.865 + 95 > mouse[0] > displayWidth * 0.865 and displayHeight * 0.88 + 40 > mouse[1] > displayHeight * 0.88: # VALID LOCATION OF QUIT BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.865, displayHeight * 0.88, 95, 40), 5) # BOX AROUND QUIT ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.865, displayHeight * 0.88, 95, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR QUIT BUTTON
                quitGame()

# (UNFINISHED)
def displayFightMenu():
    """
    Displays the Fight Menu for Player 1 after "FIGHT" has been clicked
    Args:
        None
    Returns:
        None
    """
    global progmonP1

    pygame.gfxdraw.box(display, (displayWidth * 0.62, displayHeight * 0.79, 370, 120), WHITE) # FILLED BOX FOR DISPLAYING THE ATTACK MENU
    pygame.draw.rect(display, BLACK, (displayWidth * 0.62, displayHeight * 0.79, 370, 120), 5) # BOX AROUND ATTACK MENU

    if progmonP1 == "ElectricCat":
        textLightningBolt, textLightningBolt_RECT = createTextObject("Lightning Bolt", miniText)
        textLightningBolt_RECT.center = (displayWidth / 1.4, displayHeight / 1.2)
        textBite, textBite_RECT = createTextObject("Bite", miniText)
        textBite_RECT.center = (displayWidth / 1.15, displayHeight / 1.1)
        textElectricScratch, textElectricScratch_RECT = createTextObject("Electric Scratch", miniText)
        textElectricScratch_RECT.center = (displayWidth / 1.4, displayHeight / 1.1)
        textEnergyBeam, textEnergyBeam_RECT = createTextObject("Energy Beam", miniText)
        textEnergyBeam_RECT.center = (displayWidth / 1.14, displayHeight / 1.2)

        display.blit(textLightningBolt, textLightningBolt_RECT)
        display.blit(textBite, textBite_RECT)
        display.blit(textElectricScratch, textElectricScratch_RECT)
        display.blit(textEnergyBeam, textEnergyBeam_RECT)
    elif progmonP1 == "FireDragon":
        textRoar, textRoar_RECT = createTextObject("Roar", miniText)
        textRoar_RECT.center = (displayWidth / 1.4, displayHeight / 1.2)
        textClawSwipe, textClawSwipe_RECT = createTextObject("Claw Swipe", miniText)
        textClawSwipe_RECT.center = (displayWidth / 1.15, displayHeight / 1.2)
        textFireBreath, textFireBreath_RECT = createTextObject("Fire Breath", miniText)
        textFireBreath_RECT.center = (displayWidth / 1.4, displayHeight / 1.1)
        textTailWhip, textTailWhip_RECT = createTextObject("Tail Whip", miniText)
        textTailWhip_RECT.center = (displayWidth / 1.15, displayHeight / 1.1)

        display.blit(textRoar, textRoar_RECT)
        display.blit(textClawSwipe, textClawSwipe_RECT)
        display.blit(textFireBreath, textFireBreath_RECT)
        display.blit(textTailWhip, textTailWhip_RECT)

def checkAliveAI():
    """
    Checks if Player AI's Progmon is still alive
    Args:
        None
    Returns:
        None
    """
    global myAI
    global progmonNameAI

    if myAI.checkAlive() == True:
        return True
    else:
        return False

# (UNFINISHED) RENAME TO handleFightMenu() FOR CONTROLLING PLAYER 1'S TURN (???)
def trackButtonsFightMenu():
    """
    Handles all button input on the Fight Menu
    Args:
        None
    Returns:
        None
    """
    global myP1
    global myAI
    global progmonP1
    global attackChoiceP1
    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE

    if progmonP1 == "ElectricCat":
        if displayWidth * 0.635 + 175 > mouse[0] > displayWidth * 0.635 and displayHeight * 0.805 + 40 > mouse[1] > displayHeight * 0.805: # VALID LOCATION OF LIGHTNING BOLT BUTTON
            pygame.draw.rect(display, RED, (displayWidth * 0.635, displayHeight * 0.805, 175, 40), 5) # BOX AROUND LIGHTNING BOLT ON MOUSE-HOVER
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.635, displayHeight * 0.805, 175, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR LIGHTNING BOLT BUTTON
                    print("Player 1's Electric Cat used Lightning Bolt!")
                    myP1.LightningBoltAttack(myAI)
                    pygame.time.delay(500) # WAIT TO PREVENT MULTIPLE BUTTON CLICKS
                    if checkAliveAI():
                        AITurn()
                        controlScreen("fightScreen")
                    else:
                        print("Player AI's", progmonNameAI, "has fainted. You win!\n") # TESTER CODE
                        controlScreen("endScreen")
        elif displayWidth * 0.8 + 165 > mouse[0] > displayWidth * 0.8 and displayHeight * 0.805 + 40 > mouse[1] > displayHeight * 0.805: # VALID LOCATION OF ENERGY BEAM BUTTON
            pygame.draw.rect(display, RED, (displayWidth * 0.8, displayHeight * 0.805, 165, 40), 5) # BOX AROUND ENERGY BEAM ON MOUSE-HOVER
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.8, displayHeight * 0.805, 165, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR ENERGY BEAM BUTTON
                    print("Player 1's Electric Cat used Energy Beam!")
                    myP1.EnergyBeamAttack(myAI)
                    pygame.time.delay(500) # WAIT TO PREVENT MULTIPLE BUTTON CLICKS
                    if checkAliveAI():
                        AITurn()
                        controlScreen("fightScreen")
                    else:
                        print("Player AI's", progmonNameAI, "has fainted. You win!\n") # TESTER CODE
                        controlScreen("endScreen")
        elif displayWidth * 0.625 + 195 > mouse[0] > displayWidth * 0.625 and displayHeight * 0.88 + 40 > mouse[1] > displayHeight * 0.88: # VALID LOCATION OF ELECTRIC SCRATCH BUTTON
            pygame.draw.rect(display, RED, (displayWidth * 0.625, displayHeight * 0.88, 195, 40), 5) # BOX AROUND ELECTRIC SCRATCH ON MOUSE-HOVER
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.625, displayHeight * 0.88, 195, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR ELECTRIC SCRATCH BUTTON
                    print("Player 1's Electric Cat used Electric Scratch!")
                    myP1.ElectricScratchAttack(myAI)
                    pygame.time.delay(500) # WAIT TO PREVENT MULTIPLE BUTTON CLICKS
                    if checkAliveAI():
                        AITurn()
                        controlScreen("fightScreen")
                    else:
                        print("Player AI's", progmonNameAI, "has fainted. You win!\n") # TESTER CODE
                        controlScreen("endScreen")
        elif displayWidth * 0.845 + 60 > mouse[0] > displayWidth * 0.845 and displayHeight * 0.88 + 40 > mouse[1] > displayHeight * 0.88: # VALID LOCATION OF BITE BUTTON
            pygame.draw.rect(display, RED, (displayWidth * 0.845, displayHeight * 0.88, 60, 40), 5) # BOX AROUND BITE ON MOUSE-HOVER
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.845, displayHeight * 0.88, 60, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR BITE BUTTON
                    print("Player 1's Electric Cat used Bite!")
                    myP1.BiteAttack(myAI)
                    pygame.time.delay(500) # WAIT TO PREVENT MULTIPLE BUTTON CLICKS
                    if checkAliveAI():
                        AITurn()
                        controlScreen("fightScreen")
                    else:
                        print("Player AI's", progmonNameAI, "has fainted. You win!\n") # TESTER CODE
                        controlScreen("endScreen")
    elif progmonP1 == "FireDragon":
        if displayWidth * 0.68 + 70 > mouse[0] > displayWidth * 0.68 and displayHeight * 0.805 + 40 > mouse[1] > displayHeight * 0.805: # VALID LOCATION OF ROAR BUTTON
            pygame.draw.rect(display, RED, (displayWidth * 0.68, displayHeight * 0.805, 70, 40), 5) # BOX AROUND ROAR ON MOUSE-HOVER
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.68, displayHeight * 0.805, 70, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR ROAR BUTTON
                    print("Player 1's Fire Dragon used Roar!")
                    myP1.RoarAttack(myAI)
                    pygame.time.delay(500) # WAIT TO PREVENT MULTIPLE BUTTON CLICKS
                    if checkAliveAI():
                        AITurn()
                        controlScreen("fightScreen")
                    else:
                        print("Player AI's", progmonNameAI, "has fainted. You win!\n") # TESTER CODE
                        controlScreen("endScreen")
        elif displayWidth * 0.8 + 150 > mouse[0] > displayWidth * 0.8 and displayHeight * 0.805 + 40 > mouse[1] > displayHeight * 0.805: # VALID LOCATION OF CLAW SWIPE BUTTON
            pygame.draw.rect(display, RED, (displayWidth * 0.8, displayHeight * 0.805, 150, 40), 5) # BOX AROUND CLAW SWIPE ON MOUSE-HOVER
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.8, displayHeight * 0.805, 150, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR CLAW SWIPE BUTTON
                    print("Player 1's Fire Dragon used Claw Swipe!")
                    myP1.ClawSwipeAttack(myAI)
                    pygame.time.delay(500) # WAIT TO PREVENT MULTIPLE BUTTON CLICKS
                    if checkAliveAI():
                        AITurn()
                        controlScreen("fightScreen")
                    else:
                        print("Player AI's", progmonNameAI, "has fainted. You win!\n") # TESTER CODE
                        controlScreen("endScreen")
        elif displayWidth * 0.65 + 135 > mouse[0] > displayWidth * 0.65 and displayHeight * 0.88 + 40 > mouse[1] > displayHeight * 0.88: # VALID LOCATION OF FIRE BREATH BUTTON
            pygame.draw.rect(display, RED, (displayWidth * 0.65, displayHeight * 0.88, 135, 40), 5) # BOX AROUND FIRE BREATH ON MOUSE-HOVER
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.65, displayHeight * 0.88, 135, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR FIRE BREATH BUTTON
                    print("Player 1's Fire Dragon used Fire Breath!")
                    myP1.FireBreathAttack(myAI)
                    pygame.time.delay(500) # WAIT TO PREVENT MULTIPLE BUTTON CLICKS
                    if checkAliveAI():
                        AITurn()
                        controlScreen("fightScreen")
                    else:
                        print("Player AI's", progmonNameAI, "has fainted. You win!\n") # TESTER CODE
                        controlScreen("endScreen")
        elif displayWidth * 0.815 + 120 > mouse[0] > displayWidth * 0.815 and displayHeight * 0.88 + 40 > mouse[1] > displayHeight * 0.88: # VALID LOCATION OF TAIL WHIP BUTTON
            pygame.draw.rect(display, RED, (displayWidth * 0.815, displayHeight * 0.88, 120, 40), 5) # BOX AROUND TAIL WHIP ON MOUSE-HOVER
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.815, displayHeight * 0.88, 120, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR TAIL WHIP BUTTON
                    print("Player 1's Fire Dragon used Tail Whip!")
                    myP1.TailWhipAttack(myAI)
                    pygame.time.delay(500) # WAIT TO PREVENT MULTIPLE BUTTON CLICKS
                    if checkAliveAI():
                        AITurn()
                        controlScreen("fightScreen")
                    else:
                        print("Player AI's", progmonNameAI, "has fainted. You win!\n") # TESTER CODE
                        controlScreen("endScreen")
# (UNFINISHED)
def displayBagMenu():
    """
    Displays the Bag Menu for Player 1 after "BAG" has been clicked
    Args:
        None
    Returns:
        None
    """
    pygame.gfxdraw.box(display, (displayWidth * 0.62, displayHeight * 0.79, 370, 120), WHITE) # FILLED BOX FOR DISPLAYING THE BAG MENU
    pygame.draw.rect(display, BLACK, (displayWidth * 0.62, displayHeight * 0.79, 370, 120), 5) # BOX AROUND BAG MENU

    textHealthPotion, textHealthPotion_RECT = createTextObject("Health Potion", miniText)
    textHealthPotion_RECT.center = (displayWidth / 1.4, displayHeight / 1.2)

    display.blit(textHealthPotion, textHealthPotion_RECT)

# (UNFINISHED)
def trackButtonsBagMenu():
    """
    Handles all button input on the Bag Menu
    Args:
        None
    Returns:
        None
    """
    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE

    if displayWidth * 0.635 + 170 > mouse[0] > displayWidth * 0.635 and displayHeight * 0.805 + 40 > mouse[1] > displayHeight * 0.805: # VALID LOCATION OF HEALTH POTION BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.635, displayHeight * 0.805, 170, 40), 5) # BOX AROUND HEALTH POTION ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.635, displayHeight * 0.805, 170, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR HEALTH POTION BUTTON
                pygame.time.delay(500) # WAIT TO PREVENT MULTIPLE BUTTON CLICKS
                if myP1.bagEmpty():
                    print("Player 1 has nothing in their Bag\n")
                    controlScreen("fightScreen")
                    pygame.time.delay(500) # WAIT TO PREVENT MULTIPLE BUTTON CLICKS
                    return
                else:
                    myP1.useHealthPotion()
                    print("Player 1 has used a Health Potion!\n")
                    controlScreen("fightScreen")

# (UNFINISHED)
def displayProgmonMenu():
    """
    Displays the Progmon Menu for Player 1 after "PROGMON" has been clicked
    Args:
        None
    Returns:
        None
    """
    pygame.gfxdraw.box(display, (displayWidth * 0.62, displayHeight * 0.79, 370, 120), WHITE) # FILLED BOX FOR DISPLAYING THE PROGMON MENU
    pygame.draw.rect(display, BLACK, (displayWidth * 0.62, displayHeight * 0.79, 370, 120), 5) # BOX AROUND PROGMON MENU

# (UNFINISHED)
def trackButtonsProgmonMenu():
    """
    Handles all button input on the Progmon Menu
    Args:
        None
    Returns:
        None
    """
    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE

# (UNFINISHED)
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
            displayStartScreen()
            trackButtonsStartScreen()
        while gameState == "fightScreen":
            eventHandler()
            displayFightScreen()
            trackButtonsFightScreen()
            # playerTurn()
        while gameState == "fightMenu":
            eventHandler()
            displayFightMenu()
            trackButtonsFightMenu()
        while gameState == "bagMenu":
            eventHandler()
            displayBagMenu()
            trackButtonsBagMenu()
        while gameState == "progmonMenu":
            eventHandler()
            displayProgmonMenu()
            # trackButtonsProgmonMenu()
        while gameState == "endScreen":
            eventHandler()
            # displayEndScreen()
            # trackButtonsEndScreen()
    else:
        print("ERROR: Invalid gameState")
        quitGame()

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
    # (UNFINISHED) ADD MORE ITEMS TO THE BAG PLUS NEED ABILITY TO SELECT THE ITEM YOU WANT TO USE
    elif(playerMove == "BAG"):
        if (myP1.bagEmpty()):
            print("Player 1 has nothing in their Bag.\n")
        else:
            myP1.useHealthPotion()
            print("Player 1 has used a Health Potion!\n") # TESTER CODE
            # AIBagTrack += 1 #lets AI track how many items you've use from your bag so it can be more AI-ish
    # (UNFINISHED) ALLOW PLAYER 1 THE ABILITY TO CHANGE THEIR PROGMON DURING THE BATTLE
    elif(playerMove == "PROGMON"):
        # progmonP1.switchProgmon()
        print("PROGMON SWITCHING IS NOT AVAILABLE AT THIS TIME")

    # (UNFINISHED) AFTER PLAYER 1'S TURN IS OVER, LET PLAYER AI GO
    AITurn()

# HANDLES THE DECISIONS THE AI HAS TO MAKE DURING THEIR TURN DEPENDING ON THEIR HEALTH AND ENEMY'S HEALTH
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
            quitGame()
    elif(myAI.currentHealth <= critical and myAI.bagEmpty):   #this should be the AI's last option - AI is going to die if it's hit again
        # DISPLAY SOME SORT OF MESSAGE SAYING THE THIS PLAYER CHOSE TO RUN
        quitGame()
    elif(myAI.currentHealth <= critical):  #if AI is low, it will use potion
        myAI.useHealthPotion()
    else:   # if progmonP1 is not low and AI is not low, then all we can do is attack the other player
        myAI.AIAttack(myP1)
        # now we should display some sort of window/message for the user saying if they hit or not
        # update player's health in the UI
    # playerTurn()    #after turn is over, let the player go

# MAIN
if __name__ == "__main__":
    controlScreen("startScreen")

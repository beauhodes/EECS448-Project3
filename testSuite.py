import random
from progmon import Progmon, FireDragon, ElectricCat, WaterTurtle, FinalBoss

global myP1
progmonNameP1 = ""
global myAI
progmonNameAI = ""

def runTestSuite():
    print("\n[RUNNING TEST SUITE]\n")
    testProgmonSelection() # DONE
    testBag() # DONE
    testStunEffect() # DONE
    testProgmonSwitching() # DONE
    # testHealthPotion() # NOT DONE
    # testRestorePotion() # NOT DONE

def testProgmonSelection():
    global myP1
    global progmonNameP1
    global myAI
    global progmonNameAI

    # PLAYER 1 PROGMON RANDOM SELECTION
    progmonControlP1 = random.randint(1, 4)
    if progmonControlP1 == 1:
        myP1 = ElectricCat()
        progmonNameP1 = "Electric Cat"
    elif progmonControlP1 == 2:
        myP1 = FireDragon()
        progmonNameP1 = "Fire Dragon"
    elif progmonControlP1 == 3:
        myP1 = WaterTurtle()
        progmonNameP1 = "Water Turtle"
    elif progmonControlP1 == 4:
        myP1 = FinalBoss()
        progmonNameP1 = "Final Boss"

    # PLAYER AI PROGMON RANDOM SELECTION
    progmonControlAI = random.randint(1, 4)
    if progmonControlAI == 1:
        myAI = ElectricCat()
        progmonNameAI = "Electric Cat"
    elif progmonControlAI == 2:
        myAI = FireDragon()
        progmonNameAI = "Fire Dragon"
    elif progmonControlAI == 3:
        myAI = WaterTurtle()
        progmonNameAI = "Water Turtle"
    elif progmonControlAI == 4:
        myAI = FinalBoss()
        progmonNameAI = "Final Boss"

    if myP1 != None and myAI != None:
        print("TEST #1: Player 1 and Player AI Progmon randomly selected... PASSED")
        print("\tPlayer 1's Progmon =", progmonNameP1)
        print("\tPlayer AI's Progmon =", progmonNameAI)
    else:
        print("TEST #1: Player 1 and Player AI Progmon randomly selected... FAILED")
        if myP1 == None:
            print("\tERROR: Player 1 needs a Progmon")
        elif myAI == None:
            print("\tERROR: Player AI needs a Progmon")

def testBag():
    global myP1

    # 0 TOTAL ITEM REMOVALS FOR PLAYER 1
    if myP1.bagEmpty() == False:
        print("\nTEST #2: Player 1's Bag contains 4 Items... PASSED")
        print("\tPlayer 1's Bag =", myP1.getBag())
    else:
        print("\nTEST #2: Player 1's Bag contains 4 Items... FAILED")
        print("\tPlayer 1's Bag =", myP1.getBag())

    # 2 TOTAL ITEM REMOVALS FOR PLAYER 1
    myP1.bag.remove("healthPotion")
    myP1.bag.remove("statBoost")
    if myP1.bagEmpty() == False:
        print("\nTEST #3: Player 1's Bag contains 2 Items... PASSED")
        print("\tPlayer 1's Bag =", myP1.getBag())
    else:
        print("\nTEST #3: Player 1's Bag contains 2 Items... FAILED")
        print("\tPlayer 1's Bag =", myP1.getBag())

    # 4 TOTAL ITEM REMOVALS FOR PLAYER 1
    myP1.bag.remove("defenseBoost")
    myP1.bag.remove("restorePotion")
    if myP1.bagEmpty() == True:
        print("\nTEST #4: Player 1's Bag contains 0 Items... PASSED")
        print("\tPlayer 1's Bag =", myP1.getBag())
    else:
        print("\nTEST #4: Player 1's Bag contains 0 Items... FAILED")
        print("\tPlayer 1's Bag =", myP1.getBag())

def testStunEffect():
    global myP1

    # NO ACTIVE STUN EFFECT
    if myP1.getStunStatus() == False:
        print("\nTEST #5: Player 1's Progmon is NOT stunned... PASSED")
        print("\tPlayer 1's Progmon Stunned Status =", myP1.stunned)
    else:
        print("\nTEST #5: Player 1's Progmon is NOT stunned... FAILED")
        print("\tPlayer 1's Progmon Stunned Status =", myP1.stunned)

    # ACTIVATE STUN EFFECT
    myP1.setStunStatus(True)
    if myP1.getStunStatus() == True:
        print("\nTEST #6: Player 1's Progmon is stunned... PASSED")
        print("\tPlayer 1's Progmon Stunned Status =", myP1.stunned)
    else:
        print("\nTEST #6: Player 1's Progmon is stunned... FAILED")
        print("\tPlayer 1's Progmon Stunned Status =", myP1.stunned)

def testProgmonSwitching():
    global myP1
    global progmonNameP1

    myP1.bag = ["healthPotion", "restorePotion"] # UPDATE PLAYER 1'S BAG FOR TESTS #7 - #10

    print("\nTEST #7 (PRE-PROGMON-SWITCHING): Player 1's Progmon and Bag")
    print("\tPlayer 1's Progmon =", progmonNameP1)
    print("\tPlayer 1's Health =", myP1.getCurrentHealth())
    print("\tPlayer 1's Bag =", myP1.getBag())
    print("\tPlayer 1's Stat Boost =", myP1.getStatBoost())
    print("\tPlayer 1's Defense Boost =", myP1.getDefenseBoost())

    switchControl = random.randint(1, 3)
    if switchControl == 1: # SWITCH TO ELECTRIC CAT (OR, IF CURRENTLY ELECTRIC CAT, THEN FINAL BOSS)
        currentHP = myP1.getCurrentHealth()
        currentBag = myP1.getBag()
        currentStatBoost = myP1.getStatBoost()
        currentDefenseBoost = myP1.getDefenseBoost()
        if progmonNameP1 != "ElectricCat":
            myP1 = ElectricCat()
            progmonNameP1 = "Electric Cat"
        else:
            myP1 = FinalBoss()
            progmonNameP1 = "Final Boss"
        myP1.setBag(currentBag)
        myP1.setStatBoost(currentStatBoost)
        myP1.setDefenseBoost(currentDefenseBoost)
        if currentHP < myP1.getHP(): # IF P1 HAD LESS HEALTH THAN NEW PROGMON'S MAX (BEFORE THE SWITCH), THEN REDUCE HEALTH
            myP1.setCurrentHealth(currentHP)
        print("\tPlayer 1 switched to {}".format(progmonNameP1))
    elif switchControl == 2: # SWITCH TO FIRE DRAGON (OR, IF CURRENTLY FIRE DRAGON, THEN FINAL BOSS)
        currentHP = myP1.getCurrentHealth()
        currentBag = myP1.getBag()
        currentStatBoost = myP1.getStatBoost()
        currentDefenseBoost = myP1.getDefenseBoost()
        if progmonNameP1 != "Fire Dragon":
            myP1 = FireDragon()
            progmonNameP1 = "Fire Dragon"
        else:
            myP1 = FinalBoss()
            progmonNameP1 = "Final Boss"
        myP1.setBag(currentBag)
        myP1.setStatBoost(currentStatBoost)
        myP1.setDefenseBoost(currentDefenseBoost)
        if currentHP < myP1.getHP(): # IF P1 HAD LESS HEALTH THAN NEW PROGMON'S MAX (BEFORE THE SWITCH), THEN REDUCE HEALTH
            myP1.setCurrentHealth(currentHP)
        print("\tPlayer 1 switched to {}".format(progmonNameP1))
    elif switchControl == 3: # SWITCH TO WATER TURTLE (OR, IF CURRENTLY WATER TURTLE, THEN FINAL BOSS)
        currentHP = myP1.getCurrentHealth()
        currentBag = myP1.getBag()
        currentStatBoost = myP1.getStatBoost()
        currentDefenseBoost = myP1.getDefenseBoost()
        if progmonNameP1 != "Water Turtle":
            myP1 = WaterTurtle()
            progmonNameP1 = "Water Turtle"
        else:
            myP1 = FinalBoss()
            progmonNameP1 = "Final Boss"
        myP1.setBag(currentBag)
        myP1.setStatBoost(currentStatBoost)
        myP1.setDefenseBoost(currentDefenseBoost)
        if currentHP < myP1.getHP(): #if P1 had less health than new progmon's max (before the switch), reduce health
            myP1.setCurrentHealth(currentHP)
        print("\tPlayer 1 switched to {}".format(progmonNameP1))

    print("\nTEST #7 (POST-PROGMON-SWITCHING): Player 1's Progmon and Bag")
    print("\tPlayer 1's Progmon =", progmonNameP1)
    print("\tPlayer 1's Health =", myP1.getCurrentHealth())
    print("\tPlayer 1's Bag =", myP1.getBag())
    print("\tPlayer 1's Stat Boost =", myP1.getStatBoost())
    print("\tPlayer 1's Defense Boost =", myP1.getDefenseBoost())

def testHealthPotion():
    global myP1
    global myAI

    # PLAYER 1
    myP1.setCurrentHealth(50)
    print("\nPlayer 1's Progmon Health BEFORE Health Potion =", myP1.getCurrentHealth())
    myP1.bag = ["healthPotion"]
    myP1.useHealthPotion()
    if myP1.getCurrentHealth() == 80:
        print("TEST #8: Player 1's Progmon was healed for 30 HP... PASSED")
        print("Player 1's Progmon Health AFTER Health Potion =", myP1.getCurrentHealth())
    else:
        print("TEST #8: Player 1's Progmon was healed for 30 HP... FAILED")
        print("Player 1's Progmon Health AFTER Health Potion =", myP1.getCurrentHealth())

    # PLAYER AI
    myAI.setCurrentHealth(myAI.hp)
    print("\nPlayer AI's Progmon Health BEFORE Health Potion =", myAI.getCurrentHealth())
    myAI.bag = ["healthPotion"]
    myAI.useHealthPotion()
    if myAI.getCurrentHealth() == myAI.hp:
        print("TEST #9: Player AI's Progmon was healed for 0 HP... PASSED")
        print("Player AI's Progmon Health AFTER Health Potion =", myAI.getCurrentHealth())
    else:
        print("TEST #9: Player AI's Progmon was healed for 0 HP... FAILED")
        print("Player AI's Progmon Health AFTER Health Potion =", myAI.getCurrentHealth())

def testRestorePotion():
    global myP1
    global myAI

    myP1.setCurrentHealth(10)
    print("Player 1's current Health BEFORE Restore Potion =", myP1.getCurrentHealth())
    myP1.bag = ["restorePotion"]
    myP1.useRestorePotion()
    print("Player 1's current Health AFTER Restore Potion =", myP1.getCurrentHealth())

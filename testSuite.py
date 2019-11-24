from main import *

global myP1
progmonNameP1 = ""
global myAI
progmonNameAI = ""

def runTestSuite():
    print("\n[RUNNING TEST SUITE]\n")
    testProgmonSelection()
    testProgmonBag()
    testProgmonStun()
    testProgmonSwitching()
    testHealthPotion() # NOT WORKING
    testRestorePotion() # NOT WORKING

def testProgmonSelection():
    global myP1
    global progmonNameP1
    global myAI
    global progmonNameAI

    # PLAYER 1 PROGMON RANDOM SELECTION
    randomProgmonP1 = random.randint(1, 4)
    if randomProgmonP1 == 1:
        myP1 = ElectricCat()
        progmonNameP1 = "Electric Cat"
    elif randomProgmonP1 == 2:
        myP1 = FireDragon()
        progmonNameP1 = "Fire Dragon"
    elif randomProgmonP1 == 3:
        myP1 = WaterTurtle()
        progmonNameP1 = "Water Turtle"
    elif randomProgmonP1 == 4:
        myP1 = FinalBoss()
        progmonNameP1 = "Final Boss"

    # PLAYER AI PROGMON RANDOM SELECTION
    randomProgmonAI = random.randint(1, 4)
    if randomProgmonAI == 1:
        myAI = ElectricCat()
        progmonNameAI = "Electric Cat"
    elif randomProgmonAI == 2:
        myAI = FireDragon()
        progmonNameAI = "Fire Dragon"
    elif randomProgmonAI == 3:
        myAI = WaterTurtle()
        progmonNameAI = "Water Turtle"
    elif randomProgmonAI == 4:
        myAI = FinalBoss()
        progmonNameAI = "Final Boss"

    if myP1 != None and myAI != None:
        print("TEST #1: Player 1 and Player AI Progmon randomly selected... PASSED")
        print("myP1 =", progmonNameP1) # TESTER CODE
        print("myAI =", progmonNameAI) # TESTER CODE
    else:
        print("TEST #1: Player 1 and Player AI Progmon randomly selected... FAILED")
        if myP1 == None:
            print("ERROR: Player 1 Progmon NOT randomly selected")
        elif myAI == None:
            print("ERROR: Player AI Progmon NOT randomly selected")

def testProgmonBag():
    global myP1
    global myAI

    # 0 TOTAL REMOVALS FOR BOTH PLAYERS
    if myP1.bagEmpty() == False:
        print("\nTEST #2: Player 1's Bag is NOT empty... PASSED")
        print("myP1's Bag =", myP1.getBag())
    else:
        print("\nTEST #2: Player 1's Bag is NOT empty... FAILED")
        print("myP1's Bag =", myP1.getBag())

    if myAI.bagEmpty() == False:
        print("\nTEST #2: Player AI's Bag is NOT empty... PASSED")
        print("myAI's Bag =", myAI.getBag())
    else:
        print("\nTEST #2: Player AI's Bag is NOT empty... FAILED")
        print("myAI's Bag =", myAI.getBag())

    # 2 TOTAL REMOVALS FOR BOTH PLAYERS
    myP1.bag.remove("healthPotion")
    myP1.bag.remove("statBoost")
    myAI.bag.remove("healthPotion")
    myAI.bag.remove("statBoost")

    if myP1.bagEmpty() == False:
        print("\nTEST #3: Player 1's Bag is NOT empty after 2 removals... PASSED")
        print("myP1's Bag =", myP1.getBag())
    else:
        print("\nTEST #3: Player 1's Bag is NOT empty after 2 removals... FAILED")
        print("myP1's Bag =", myP1.getBag())

    if myAI.bagEmpty() == False:
        print("\nTEST #3: Player AI's Bag is NOT empty after 2 removals... PASSED")
        print("myAI's Bag =", myAI.getBag())
    else:
        print("\nTEST #3: Player AI's Bag is NOT empty after 2 removals... FAILED")
        print("myAI's Bag =", myAI.getBag())

    # 4 TOTAL REMOVALS FOR BOTH PLAYERS
    myP1.bag.remove("defenseBoost")
    myP1.bag.remove("restorePotion")
    myAI.bag.remove("defenseBoost")
    myAI.bag.remove("restorePotion")

    if myP1.bagEmpty() == True:
        print("\nTEST #4: Player 1's Bag is empty after 4 removals... PASSED")
        print("myP1's Bag =", myP1.getBag())
    else:
        print("\nTEST #4: Player 1's Bag is empty after 4 removals... FAILED")
        print("myP1's Bag =", myP1.getBag())

    if myAI.bagEmpty() == True:
        print("\nTEST #4: Player AI's Bag is empty after 4 removals... PASSED")
        print("myAI's Bag =", myAI.getBag())
    else:
        print("\nTEST #4: Player AI's Bag is empty after 4 removals... FAILED")
        print("myAI's Bag =", myAI.getBag())

def testProgmonStun():
    global myP1
    global myAI

    # STUN EFFECT NOT ACTIVE
    if myP1.getStunStatus() == False:
        print("\nTEST #5: Player 1's Progmon is NOT stunned... PASSED")
    else:
        print("\nTEST #5: Player 1's Progmon is NOT stunned... FAILED")

    if myAI.getStunStatus() == False:
        print("\nTEST #5: Player AI's Progmon is NOT stunned... PASSED")
    else:
        print("\nTEST #5: Player AI's Progmon is NOT stunned... FAILED")

    # STUN EFFECT ACTIVE
    myP1.setStunStatus(True)
    myAI.setStunStatus(True)

    if myP1.getStunStatus() == True:
        print("\nTEST #6: Player 1's Progmon is stunned after setStunStatus(True)... PASSED")
    else:
        print("\nTEST #6: Player 1's Progmon is stunned after setStunStatus(True)... FAILED")

    if myAI.getStunStatus() == True:
        print("\nTEST #6: Player AI's Progmon is stunned after setStunStatus(True)... PASSED")
    else:
        print("\nTEST #6: Player AI's Progmon is stunned after setStunStatus(True)... FAILED")

def testProgmonSwitching():
    global myP1
    global progmonNameP1
    global myAI
    global progmonNameAI

    # PLAYER 1
    print("\nTEST #7 (PRE): Player 1's Progmon and Bag BEFORE Progmon Switching")
    print("Player 1's Progmon =", progmonNameP1)
    print("Player 1's Health =", myP1.getCurrentHealth())
    print("Player 1's Bag =", myP1.getBag())
    print("Player 1's Stat Boost =", myP1.getStatBoost())
    print("Player 1's Defense Boost =", myP1.getDefenseBoost())

    switchControl = random.randint(1, 3)
    if switchControl == 1: # SWITCH TO ELECTRIC CAT (OR, IF CURRENTLY ELECTRIC CAT, FINAL BOSS)
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
        if currentHP < myP1.getHP(): #if P1 had less health than new progmon's max (before the switch), reduce health
            myP1.setCurrentHealth(currentHP)
        print("Player 1 switched to {}".format(progmonNameP1))
    elif switchControl == 2: # SWITCH TO FIRE DRAGON (OR, IF CURRENTLY FIRE DRAGON, FINAL BOSS)
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
        if currentHP < myP1.getHP(): #if P1 had less health than new progmon's max (before the switch), reduce health
            myP1.setCurrentHealth(currentHP)
        print("Player 1 switched to {}".format(progmonNameP1))
    elif switchControl == 3: # SWITCH TO WATER TURTLE (OR, IF CURRENTLY WATER TURTLE, FINAL BOSS)
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
        print("Player 1 switched to {}".format(progmonNameP1))

    print("\nTEST #7 (POST): Player 1's Progmon and Bag AFTER Progmon Switching")
    print("Player 1's Progmon =", progmonNameP1)
    print("Player 1's Health =", myP1.getCurrentHealth())
    print("Player 1's Bag =", myP1.getBag())
    print("Player 1's Stat Boost =", myP1.getStatBoost())
    print("Player 1's Defense Boost =", myP1.getDefenseBoost())

    # PLAYER AI
    print("\nTEST #7 (PRE): Player AI's Progmon and Bag BEFORE Progmon Switching")
    print("Player AI's Progmon =", progmonNameAI)
    print("Player AI's Health =", myAI.getCurrentHealth())
    print("Player AI's Bag =", myAI.getBag())
    print("Player AI's Stat Boost =", myAI.getStatBoost())
    print("Player AI's Defense Boost =", myAI.getDefenseBoost())

    switchControl = random.randint(1, 3)
    if switchControl == 1: # SWITCH TO ELECTRIC CAT (OR, IF CURRENTLY ELECTRIC CAT, FINAL BOSS)
        currentHP = myAI.getCurrentHealth()
        currentBag = myAI.getBag()
        currentStatBoost = myAI.getStatBoost()
        currentDefenseBoost = myAI.getDefenseBoost()
        if progmonNameAI != "ElectricCat":
            myAI = ElectricCat()
            progmonNameAI = "Electric Cat"
        else:
            myAI = FinalBoss()
            progmonNameAI = "Final Boss"
        myAI.setBag(currentBag)
        myAI.setStatBoost(currentStatBoost)
        myAI.setDefenseBoost(currentDefenseBoost)
        if currentHP < myAI.getHP(): #if AI had less health than new progmon's max (before the switch), reduce health
            myAI.setCurrentHealth(currentHP)
        print("Player AI switched to {}".format(progmonNameAI))
    elif switchControl == 2: # SWITCH TO FIRE DRAGON (OR, IF CURRENTLY FIRE DRAGON, FINAL BOSS)
        currentHP = myAI.getCurrentHealth()
        currentBag = myAI.getBag()
        currentStatBoost = myAI.getStatBoost()
        currentDefenseBoost = myAI.getDefenseBoost()
        if progmonNameAI != "Fire Dragon":
            myAI = FireDragon()
            progmonNameAI = "Fire Dragon"
        else:
            myAI = FinalBoss()
            progmonNameAI = "Final Boss"
        myAI.setBag(currentBag)
        myAI.setStatBoost(currentStatBoost)
        myAI.setDefenseBoost(currentDefenseBoost)
        if currentHP < myAI.getHP(): #if AI had less health than new progmon's max (before the switch), reduce health
            myAI.setCurrentHealth(currentHP)
        print("Player AI switched to {}".format(progmonNameAI))
    elif switchControl == 3: # SWITCH TO WATER TURTLE (OR, IF CURRENTLY WATER TURTLE, FINAL BOSS)
        currentHP = myAI.getCurrentHealth()
        currentBag = myAI.getBag()
        currentStatBoost = myAI.getStatBoost()
        currentDefenseBoost = myAI.getDefenseBoost()
        if progmonNameAI != "Water Turtle":
            myAI = WaterTurtle()
            progmonNameAI = "Water Turtle"
        else:
            myAI = FinalBoss()
            progmonNameAI = "Final Boss"
        myAI.setBag(currentBag)
        myAI.setStatBoost(currentStatBoost)
        myAI.setDefenseBoost(currentDefenseBoost)
        if currentHP < myAI.getHP(): #if AI had less health than new progmon's max (before the switch), reduce health
            myAI.setCurrentHealth(currentHP)
        print("Player AI switched to {}".format(progmonNameAI))

    print("\nTEST #7 (POST): Player AI's Progmon and Bag AFTER Progmon Switching")
    print("Player AI's Progmon =", progmonNameAI)
    print("Player AI's Health =", myAI.getCurrentHealth())
    print("Player AI's Bag =", myAI.getBag())
    print("Player AI's Stat Boost =", myAI.getStatBoost())
    print("Player AI's Defense Boost =", myAI.getDefenseBoost())

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

if __name__ == "__main__":
    runTestSuite()

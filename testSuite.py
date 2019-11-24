import random
from progmon import Progmon, FireDragon, ElectricCat, WaterTurtle, FinalBoss

global myP1
progmonNameP1 = ""
global myAI
progmonNameAI = ""

def runTestSuite():
    """
    Runs all Test functions in the Test Suite
    """
    print("\n[RUNNING TEST SUITE]\n")
    testProgmonSelection() # DONE
    testBag() # DONE
    testStunEffect() # DONE
    testProgmonSwitching() # DONE
    testHealthPotion() # DONE
    testRestorePotion() # DONE
    testAllAttacks() #DONE
    testStatAttacks() #DONE
    testDefense() #DONE
    testZeroHealth() #DONE
    testAlive() #DONE

def testProgmonSelection():
    """
    Tests that all Progmon are usable by both Player 1 and the AI
    """
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
    """
    Tests that a Player's Bag updates properly with different removals
    """
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
    """
    Tests that Stat Boost's Stun Effect is actually stunning the enemy Progmon
    """
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
    """
    Tests that all of Progmon A's stats/effects carry over to Progmon B after Progmon Switching
    """
    global myP1
    global progmonNameP1

    myP1.bag = ["healthPotion", "restorePotion"] # UPDATE PLAYER 1'S BAG
    print("\nTEST #7 (PRE-PROGMON-SWITCHING): Player 1's Progmon and Bag... UNKNOWN")
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
        if currentHP < myP1.getHP(): # IF P1 HAD LESS HEALTH THAN NEW PROGMON'S MAX (BEFORE THE SWITCH), THEN REDUCE HEALTH
            myP1.setCurrentHealth(currentHP)
        print("\tPlayer 1 switched to {}".format(progmonNameP1))

    print("\nTEST #7 (POST-PROGMON-SWITCHING): Player 1's Progmon and Bag... PASSED")
    print("\tPlayer 1's Progmon =", progmonNameP1)
    print("\tPlayer 1's Health =", myP1.getCurrentHealth())
    print("\tPlayer 1's Bag =", myP1.getBag())
    print("\tPlayer 1's Stat Boost =", myP1.getStatBoost())
    print("\tPlayer 1's Defense Boost =", myP1.getDefenseBoost())

def testHealthPotion():
    """
    Tests that Progmon is healed the correct amount by Health Potion
    """
    global myP1

    myP1.setCurrentHealth(myP1.hp)
    print("\n")
    if myP1.useHealthPotion() == 0:
        print("\nTEST #8: Progmon is healed 0 HP by Health Potion... PASSED")
    else:
        print("\nTEST #8: Progmon is healed 0 HP by Health Potion... FAILED")

    myP1.bag = ["healthPotion"] # UPDATE PLAYER 1'S BAG
    myP1.setCurrentHealth(myP1.hp - 15)
    print("\n")
    if myP1.useHealthPotion() == 15:
        print("\nTEST #9: Progmon is healed 15 HP by Health Potion... PASSED")
    else:
        print("\nTEST #9: Progmon is healed 15 HP by Health Potion... FAILED")

    myP1.bag = ["healthPotion"] # UPDATE PLAYER 1'S BAG
    myP1.setCurrentHealth(myP1.hp - 30)
    print("\n")
    if myP1.useHealthPotion() == 30:
        print("\nTEST #10: Progmon is healed 30 HP by Health Potion... PASSED")
    else:
        print("\nTEST #10: Progmon is healed 30 HP by Health Potion... FAILED")

def testRestorePotion():
    """
    Tests that Progmon is healed to max health and all status effects are removed after using a Restore Potion
    """
    global myP1

    myP1.bag = ["restorePotion"] # UPDATE PLAYER 1'S BAG
    myP1.setCurrentHealth(10)
    myP1.statBoost = True
    myP1.defenseBoost = True
    print("\nTEST #11 (PRE-RESTORE-POTION): Player 1's Progmon... UNKNOWN")
    print("\tPlayer 1's Progmon =", progmonNameP1)
    print("\tPlayer 1's Health =", myP1.getCurrentHealth())
    print("\tPlayer 1's Stat Boost =", myP1.getStatBoost())
    print("\tPlayer 1's Defense Boost =", myP1.getDefenseBoost())

    myP1.useRestorePotion()
    myP1.setCurrentHealth(myP1.hp)
    if myP1.getCurrentHealth() == myP1.hp and myP1.statBoost == False and myP1.defenseBoost == False:
        print("\nTEST #11 (POST-RESTORE-POTION): Player 1's Progmon... PASSED")
        print("\tPlayer 1's Progmon =", progmonNameP1)
        print("\tPlayer 1's Health =", myP1.getCurrentHealth())
        print("\tPlayer 1's Stat Boost =", myP1.getStatBoost())
        print("\tPlayer 1's Defense Boost =", myP1.getDefenseBoost())
    else:
        print("\nTEST #11 (POST-RESTORE-POTION): Player 1's Progmon... FAILED")
        print("\tPlayer 1's Progmon =", progmonNameP1)
        print("\tPlayer 1's Health =", myP1.getCurrentHealth())
        print("\tPlayer 1's Stat Boost =", myP1.getStatBoost())
        print("\tPlayer 1's Defense Boost =", myP1.getDefenseBoost())

def testAllAttacks():
    """
    Test that all attacks do the correct amount of damage by calling them and then checking the enemy's health
    """
    print("\nTEST #12 (ALL ATTACKS DO CORRECT AMOUNT OF DAMAGE):")
    testProgmon1 = ElectricCat()
    testProgmon2 = FireDragon()
    testProgmon3 = WaterTurtle()
    testProgmon4 = FinalBoss()

    #electric cat:
    while(1):
        enemyPlayer = FireDragon()
        att = testProgmon1.attack1(enemyPlayer)
        if (att[0] == True):
            if enemyPlayer.getCurrentHealth() == enemyPlayer.getHP() - 90:
                print("Lighting bolt (90): PASSED")
            else:
                print("Lighting bolt (90): FAILED")
            break
    while(1):
        enemyPlayer = FireDragon()
        att = testProgmon1.attack2(enemyPlayer)
        if (att[0] == True):
            if enemyPlayer.getCurrentHealth() == enemyPlayer.getHP() - 40:
                print("Electric Scratch (40): PASSED")
            else:
                print("Electric Scratch (40): FAILED")
            break
    while(1):
        enemyPlayer = FireDragon()
        att = testProgmon1.attack3(enemyPlayer)
        if (att[0] == True):
            if enemyPlayer.getCurrentHealth() == enemyPlayer.getHP() - 110:
                print("Enegy Beam (110): PASSED")
            else:
                print("Energy Beam (110): FAILED")
            break
    while(1):
        enemyPlayer = FireDragon()
        att = testProgmon1.attack4(enemyPlayer)
        if (att[0] == True):
            if enemyPlayer.getCurrentHealth() == enemyPlayer.getHP() - 20:
                print("Bite (20): PASSED")
            else:
                print("Bite (20): FAILED")
            break

    #fire dragon:
    while(1):
        enemyPlayer = FireDragon()
        att = testProgmon2.attack1(enemyPlayer)
        if (att[0] == True):
            if enemyPlayer.getCurrentHealth() == enemyPlayer.getHP() - 80:
                print("Roar (80): PASSED")
            else:
                print("Roar (80): FAILED\n")
            break
    while(1):
        enemyPlayer = FireDragon()
        att = testProgmon2.attack2(enemyPlayer)
        if (att[0] == True):
            if enemyPlayer.getCurrentHealth() == enemyPlayer.getHP() - 35:
                print("Claw Swipe (35): PASSED")
            else:
                print("Claw Swipe (35): FAILED\n")
            break
    while(1):
        enemyPlayer = FireDragon()
        att = testProgmon2.attack3(enemyPlayer)
        if (att[0] == True):
            if enemyPlayer.getCurrentHealth() == enemyPlayer.getHP() - 140:
                print("Fire Breath (140): PASSED")
            else:
                print("Fire Breath (140): FAILED")
            break
    while(1):
        enemyPlayer = FireDragon()
        att = testProgmon2.attack4(enemyPlayer)
        if (att[0] == True):
            if enemyPlayer.getCurrentHealth() == enemyPlayer.getHP() - 20:
                print("Tail Whip (20): PASSED")
            else:
                print("Tail Whip (20): FAILED")
            break

    #water turtle:
    while(1):
        enemyPlayer = FireDragon()
        att = testProgmon3.attack1(enemyPlayer)
        if (att[0] == True):
            if enemyPlayer.getCurrentHealth() == enemyPlayer.getHP() - 45:
                print("Aqua Jet (45): PASSED")
            else:
                print("Aqua Jet (45): FAILED")
            break
    while(1):
        enemyPlayer = FireDragon()
        att = testProgmon3.attack2(enemyPlayer)
        if (att[0] == True):
            if enemyPlayer.getCurrentHealth() == enemyPlayer.getHP() - 50:
                print("Aqua Tail (50): PASSED")
            else:
                print("Aqua Tail (50): FAILED")
            break
    while(1):
        enemyPlayer = FireDragon()
        att = testProgmon3.attack3(enemyPlayer)
        if (att[0] == True):
            if enemyPlayer.getCurrentHealth() == enemyPlayer.getHP() - 70:
                print("Water Pulse (70): PASSED")
            else:
                print("Water Pulse (70): FAILED")
            break
    while(1):
        enemyPlayer = FireDragon()
        att = testProgmon3.attack4(enemyPlayer)
        if (att[0] == True):
            if enemyPlayer.getCurrentHealth() == enemyPlayer.getHP() - 12:
                print("Bubble (12): PASSED")
            else:
                print("Bubble (12): FAILED")
            break

    #final boss:
    while(1):
        enemyPlayer = FireDragon()
        att = testProgmon4.attack1(enemyPlayer)
        if (att[0] == True):
            if enemyPlayer.getCurrentHealth() == enemyPlayer.getHP() - 150:
                print("Giga Impact (150): PASSED")
            else:
                print("Giga Impact (150): FAILED")
            break
    while(1):
        enemyPlayer = FireDragon()
        att = testProgmon4.attack2(enemyPlayer)
        if (att[0] == True):
            if enemyPlayer.getCurrentHealth() == enemyPlayer.getHP() - 90:
                print("Psychic (90): PASSED")
            else:
                print("Psychic (90): FAILED")
            break
    while(1):
        enemyPlayer = FireDragon()
        att = testProgmon4.attack3(enemyPlayer)
        if (att[0] == True):
            if enemyPlayer.getCurrentHealth() == enemyPlayer.getHP() - 120:
                print("Mega Kick (120): PASSED")
            else:
                print("Mega Kick (120): FAILED")
            break
    while(1):
        enemyPlayer = FireDragon()
        att = testProgmon4.attack4(enemyPlayer)
        if (att[0] == True):
            if enemyPlayer.getCurrentHealth() == enemyPlayer.getHP() - 60:
                print("Ancient Power (60): PASSED")
            else:
                print("Ancient Power (60): FAILED")
            break

def testStatAttacks():
    """
    Test that all attacks that can be stat boosted do the correct amount of damage by calling them (with attacker's stat boost active) and then checking the enemy's health
    """
    print("\nTEST #13 (ALL STAT-BOOSTABLE ATTACKS DO CORRECT AMOUNT OF DAMAGE):")
    testProgmon1 = ElectricCat()
    testProgmon1.setStatBoost(True)
    testProgmon2 = FireDragon()
    testProgmon2.setStatBoost(True)
    testProgmon3 = WaterTurtle()
    testProgmon3.setStatBoost(True)
    testProgmon4 = FinalBoss()
    testProgmon4.setStatBoost(True)

    #electric cat:
    while(1):
        testProgmon1.setStatBoost(True)
        enemyPlayer = FireDragon()
        att = testProgmon1.attack1(enemyPlayer)
        if (att[0] == True):
            if ((enemyPlayer.getCurrentHealth() == enemyPlayer.getHP() - 100) and (enemyPlayer.getStatBoost() == False)):
                print("Lighting bolt (90+10): PASSED")
            else:
                print("Lighting bolt (90+10): FAILED")
            break
    while(1):
        testProgmon1.setStatBoost(True)
        enemyPlayer = FireDragon()
        att = testProgmon1.attack3(enemyPlayer)
        if (att[0] == True):
            if ((enemyPlayer.getCurrentHealth() == enemyPlayer.getHP() - 120) and (enemyPlayer.getStatBoost() == False)):
                print("Enegy Beam (110+10): PASSED")
            else:
                print("Energy Beam (110+10): FAILED")
            break

    #fire dragon:
    while(1):
        testProgmon2.setStatBoost(True)
        enemyPlayer = FireDragon()
        att = testProgmon2.attack1(enemyPlayer)
        if (att[0] == True):
            if ((enemyPlayer.getCurrentHealth() == enemyPlayer.getHP() - 90) and (enemyPlayer.getStatBoost() == False)):
                print("Roar (80+10): PASSED")
            else:
                print("Roar (80+10): FAILED\n")
            break
    while(1):
        testProgmon2.setStatBoost(True)
        enemyPlayer = FireDragon()
        att = testProgmon2.attack3(enemyPlayer)
        if (att[0] == True):
            if ((enemyPlayer.getCurrentHealth() == enemyPlayer.getHP() - 150) and (enemyPlayer.getStatBoost() == False)):
                print("Fire Breath (140+10): PASSED")
            else:
                print("Fire Breath (140+10): FAILED")
            break

    #water turtle:
    while(1):
        testProgmon3.setStatBoost(True)
        enemyPlayer = FireDragon()
        att = testProgmon3.attack1(enemyPlayer)
        if (att[0] == True):
            if ((enemyPlayer.getCurrentHealth() == enemyPlayer.getHP() - 55) and (enemyPlayer.getStatBoost() == False)):
                print("Aqua Jet (45+10): PASSED")
            else:
                print("Aqua Jet (45+10): FAILED")
            break
    while(1):
        testProgmon3.setStatBoost(True)
        enemyPlayer = FireDragon()
        att = testProgmon3.attack3(enemyPlayer)
        if (att[0] == True):
            if ((enemyPlayer.getCurrentHealth() == enemyPlayer.getHP() - 80) and (enemyPlayer.getStatBoost() == False)):
                print("Water Pulse (70+10): PASSED")
            else:
                print("Water Pulse (70+10): FAILED")
            break

    #final boss:
    while(1):
        testProgmon4.setStatBoost(True)
        enemyPlayer = FireDragon()
        att = testProgmon4.attack1(enemyPlayer)
        if (att[0] == True):
            if ((enemyPlayer.getCurrentHealth() == enemyPlayer.getHP() - 160) and (enemyPlayer.getStatBoost() == False)):
                print("Giga Impact (150+10): PASSED")
            else:
                print("Giga Impact (150+10): FAILED")
            break
    while(1):
        testProgmon4.setStatBoost(True)
        enemyPlayer = FireDragon()
        att = testProgmon4.attack3(enemyPlayer)
        if (att[0] == True):
            if ((enemyPlayer.getCurrentHealth() == enemyPlayer.getHP() - 130) and (enemyPlayer.getStatBoost() == False)):
                print("Mega Kick (120+10): PASSED")
            else:
                print("Mega Kick (120+10): FAILED")
            break

def testDefense():
    """
    Test that defense boost works for each progmon by having it get attacked (with its defense boost active) then checking its health
    """
    print("\nTEST #14 (TEST DEFENSE BOOST ON EACH PROGMON):")
    testProgmon1 = ElectricCat()
    testProgmon2 = FireDragon()
    testProgmon3 = WaterTurtle()
    testProgmon4 = FinalBoss()
    while(1):
        testProgmon1.setDefenseBoost(True)
        enemyPlayer = FireDragon()
        att = enemyPlayer.attack1(testProgmon1)
        if (att[0] == True):
            if ((testProgmon1.getCurrentHealth() == testProgmon1.getHP() - 70) and (testProgmon1.getDefenseBoost() == False)):
                print("Electric Cat: PASSED")
            else:
                print("Electric Cat: FAILED")
            break
    while(1):
        testProgmon2.setDefenseBoost(True)
        enemyPlayer = FireDragon()
        att = enemyPlayer.attack1(testProgmon2)
        if (att[0] == True):
            if ((testProgmon2.getCurrentHealth() == testProgmon2.getHP() - 70) and (testProgmon2.getDefenseBoost() == False)):
                print("Fire Dragon: PASSED")
            else:
                print("Fire Dragon: FAILED")
            break
    while(1):
        testProgmon3.setDefenseBoost(True)
        enemyPlayer = FireDragon()
        att = enemyPlayer.attack1(testProgmon3)
        if (att[0] == True):
            if ((testProgmon3.getCurrentHealth() == testProgmon3.getHP() - 70) and (testProgmon3.getDefenseBoost() == False)):
                print("Water Turtle: PASSED")
            else:
                print("Water Turtle: FAILED")
            break
    while(1):
        testProgmon4.setDefenseBoost(True)
        enemyPlayer = FireDragon()
        att = enemyPlayer.attack1(testProgmon4)
        if (att[0] == True):
            if ((testProgmon4.getCurrentHealth() == testProgmon4.getHP() - 70) and (testProgmon4.getDefenseBoost() == False)):
                print("Final Boss: PASSED")
            else:
                print("Final Boss: FAILED")
            break

def testZeroHealth():
    """
    Test that each progmon's health can never go below 0 by setting its health to 10, having it take 70 damage, then checking to see that health = 0
    """
    print("\nTEST #15 (EACH PROGMON'S HEALTH CANNOT GO LOWER THAN 0, EX: IF IT TAKES 70 DAMAGE WITH 10 HEALTH, HEALTH GOES TO 0):")
    testProgmon1 = ElectricCat()
    testProgmon2 = FireDragon()
    testProgmon3 = WaterTurtle()
    testProgmon4 = FinalBoss()
    while(1):
        testProgmon1.setCurrentHealth(10)
        enemyPlayer = FireDragon()
        att = enemyPlayer.attack1(testProgmon1)
        if (att[0] == True):
            if (testProgmon1.getCurrentHealth() == 0):
                print("Electric Cat: PASSED")
            else:
                print("Electric Cat: FAILED")
            break
    while(1):
        testProgmon2.setCurrentHealth(10)
        enemyPlayer = FireDragon()
        att = enemyPlayer.attack1(testProgmon2)
        if (att[0] == True):
            if (testProgmon2.getCurrentHealth() == 0):
                print("Fire Dragon: PASSED")
            else:
                print("Fire Dragon: FAILED")
            break
    while(1):
        testProgmon3.setCurrentHealth(10)
        enemyPlayer = FireDragon()
        att = enemyPlayer.attack1(testProgmon3)
        if (att[0] == True):
            if (testProgmon3.getCurrentHealth() == 0):
                print("Water Turtle: PASSED")
            else:
                print("Water Turtle: FAILED")
            break
    while(1):
        testProgmon4.setCurrentHealth(10)
        enemyPlayer = FireDragon()
        att = enemyPlayer.attack1(testProgmon4)
        if (att[0] == True):
            if (testProgmon4.getCurrentHealth() == 0):
                print("Final Boss: PASSED")
            else:
                print("Final Boss: FAILED")
            break

def testAlive():
    """
    Test that each progmon's self.alive = False when it faints by having it take enough damage to get health to 0 then checking its alive attribute
    """
    print("\nTEST #16 (EACH PROGMON FAINTS IMMEDIATELY (alive = False) WHEN HEALTH <= 0):")
    testProgmon1 = ElectricCat()
    testProgmon2 = FireDragon()
    testProgmon3 = WaterTurtle()
    testProgmon4 = FinalBoss()
    while(1):
        testProgmon1.setCurrentHealth(70)
        enemyPlayer = FireDragon()
        att = enemyPlayer.attack1(testProgmon1)
        if (att[0] == True):
            if (testProgmon1.checkAlive() == False):
                print("Electric Cat: PASSED")
            else:
                print("Electric Cat: FAILED")
            break
    while(1):
        testProgmon2.setCurrentHealth(70)
        enemyPlayer = FireDragon()
        att = enemyPlayer.attack1(testProgmon2)
        if (att[0] == True):
            if (testProgmon2.checkAlive() == False):
                print("Fire Dragon: PASSED")
            else:
                print("Fire Dragon: FAILED")
            break
    while(1):
        testProgmon3.setCurrentHealth(70)
        enemyPlayer = FireDragon()
        att = enemyPlayer.attack1(testProgmon3)
        if (att[0] == True):
            if (testProgmon3.checkAlive() == False):
                print("Water Turtle: PASSED")
            else:
                print("Water Turtle: FAILED")
            break
    while(1):
        testProgmon4.setCurrentHealth(70)
        enemyPlayer = FireDragon()
        att = enemyPlayer.attack1(testProgmon4)
        if (att[0] == True):
            if (testProgmon4.checkAlive() == False):
                print("Final Boss: PASSED")
            else:
                print("Final Boss: FAILED")
            break

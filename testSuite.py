from main import *

global myP1
progmonP1 = ""
progmonNameP1 = ""
global myAI
progmonAI = ""
progmonNameAI = ""

def runTestSuite():
    print("\n[RUNNING TEST SUITE]\n")
    testProgmonSelection()
    testProgmonBag()

def testProgmonSelection():
    global myP1
    global progmonP1
    global progmonNameP1
    global myAI
    global progmonAI
    global progmonNameAI

    # PLAYER 1
    randomProgmonP1 = random.randint(1, 4)
    if randomProgmonP1 == 1:
        myP1 = ElectricCat()
        progmonP1 = "ElectricCat"
        progmonNameP1 = "Electric Cat"
    elif randomProgmonP1 == 2:
        myP1 = FireDragon()
        progmonP1 = "FireDragon"
        progmonNameP1 = "Fire Dragon"
    elif randomProgmonP1 == 3:
        myP1 = WaterTurtle()
        progmonP1 = "WaterTurtle"
        progmonNameP1 = "Water Turtle"
    elif randomProgmonP1 == 4:
        myP1 = FinalBoss()
        progmonP1 = "FinalBoss"
        progmonNameP1 = "Final Boss"

    # PLAYER AI
    randomProgmonAI = random.randint(1, 4)
    if randomProgmonAI == 1:
        myAI = ElectricCat()
        progmonAI = "ElectricCat"
        progmonNameAI = "Electric Cat"
    elif randomProgmonAI == 2:
        myAI = FireDragon()
        progmonAI = "FireDragon"
        progmonNameAI = "Fire Dragon"
    elif randomProgmonAI == 3:
        myAI = WaterTurtle()
        progmonAI = "WaterTurtle"
        progmonNameAI = "Water Turtle"
    elif randomProgmonAI == 4:
        myAI = FinalBoss()
        progmonAI = "FinalBoss"
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

    # PLAYER 1
    if myP1.bagEmpty() == False:
        print("TEST #2: Player 1's Bag is NOT empty... PASSED")
    else:
        print("TEST #2: Player 1's Bag is NOT empty... FAILED")

    if myAI.bagEmpty() == False:
        print("TEST #2: Player AI's Bag is NOT empty... PASSED")
    else:
        print("TEST #2: Player AI's Bag is NOT empty... FAILED")

    myP1.bag.remove("healthPotion")
    myP1.bag.remove("statBoost")

    if myP1.bagEmpty() == True:
        print("TEST #3: Player 1's Bag is NOT empty after 2 removals... PASSED")
    else:
        print("TEST #3: Player 1's Bag is NOT empty after 2 removals... FAILED")

    myAI.bag.remove("healthPotion")
    myAI.bag.remove("statBoost")

    if myAI.bagEmpty() == True:
        print("TEST #3: Player AI's Bag is NOT empty after 2 removals... PASSED")
    else:
        print("TEST #3: Player AI's Bag is NOT empty after 2 removals... FAILED")

    myP1.bag.remove("healthPotion")
    myP1.bag.remove("statBoost")

    if myP1.bagEmpty() == True:
        print("TEST #3: Player 1's Bag is NOT empty after 2 removals... PASSED")
    else:
        print("TEST #3: Player 1's Bag is NOT empty after 2 removals... FAILED")

    myAI.bag.remove("healthPotion")
    myAI.bag.remove("statBoost")

    if myAI.bagEmpty() == True:
        print("TEST #3: Player AI's Bag is NOT empty after 2 removals... PASSED")
    else:
        print("TEST #3: Player AI's Bag is NOT empty after 2 removals... FAILED")

if __name__ == "__main__":
    runTestSuite()

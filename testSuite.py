from main import *

print("\n[RUNNING TEST SUITE]\n")
gameState = "startScreen"

if gameState == "startScreen":
    randomProgmonP1 = random.randint(1, 4)
    print("randomProgmonP1 =", randomProgmonP1) # TESTER CODE
    if randomProgmonP1 == 1:
        myP1 = ElectricCat()
    elif randomProgmonP1 == 2:
        myP1 = FireDragon()
    elif randomProgmonP1 == 3:
        myP1 = WaterTurtle()
    elif randomProgmonP1 == 4:
        myP1 = FinalBoss()

    print("myP1 =", myP1) # TESTER CODE

    randomProgmonAI = random.randint(1, 4)
    print("randomProgmonAI =", randomProgmonAI) # TESTER CODE
    if randomProgmonAI == 1:
        myAI = ElectricCat()
    elif randomProgmonAI == 2:
        myAI = FireDragon()
    elif randomProgmonAI == 3:
        myAI = WaterTurtle()
    elif randomProgmonAI == 4:
        myAI = FinalBoss()

    print("myAI =", myAI) # TESTER CODE

    if myP1 != None and myAI != None:
        print("fightScreen")
        # gameState = "fightScreen"
        # controlScreen(gameState)

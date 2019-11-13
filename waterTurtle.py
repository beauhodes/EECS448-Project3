import random

class WaterTurtle:
    """
    Class for the new Water Turtle Progmon
    """

    def __init__(self):
        """
        Creates variables associated with WaterTurtle
        Args:
            self (object) - WaterTurtle
        Returns:
            None
        """
        self.name = "Water Turtle"
        self.hp = 200
        self.currentHealth = 200
        self.alive = True
        self.bag = ["healthPotion", "statBoost", "defenseBoost"]

    def doDamage(self, damageDone):
        """
        Deals damage to the enemy's health; set alive to False if health goes below 1
        Args:
            self (object) - WaterTurtle
            damageDone (int) - amount of damage to do
        Returns:
            None
        """
        self.currentHealth = self.currentHealth - damageDone
        if(self.currentHealth <= 0):
            self.alive = False

    def checkAlive(self):
        """
        Checks if WaterTurtle is alive
        Args:
            self (object) - WaterTurtle
        Returns:
            (bool) - True if WaterTurtle is alive, otherwise False
        """
        if(self.alive == True):
            return True
        else:
            return False

    def getCurrentHealth(self):
        """
        Gets the currentHealth of WaterTurtle
        Args:
            self (object) - WaterTurtle
        Returns:
            WaterTurtle's currentHealth
        """
        return self.currentHealth

    def getHp(self):
        """
        Gets the currentHealth of WaterTurtle
        Args:
            self (object) - FireDragon
        Returns:
            FireDragon's currentHealth
        """
        return self.hp

    def aquaJet(self):
        chanceToHit = random.randint(1, 101)
        if(chanceToHit <= 70):
            enemyPlayer.doDamage(45)
            print("Aqua Jet did 45 damage!\n")
            return True
        else:
            print("Aqua Jet missed!\n")
            return False

    def aquaTail(self):
        chanceToHit = random.randint(1, 101)
        if(chanceToHit <= 55):
            enemyPlayer.doDamage(50)
            print("Aqua Tail did 50 damage!\n")
            return True
        else:
            print("Aqua Tail missed!\n")
            return False

    def waterPulse(self):
        chanceToHit = random.randint(1, 101)
        if(chanceToHit <= 48):
            enemyPlayer.doDamage(70)
            print("Water Pulse did 70 damage!\n")
            return True
        else:
            print("Water Pulse missed!\n")
            return False

    def tackle(self):
        enemyPlayer.doDamage(10)
        print("Tackle did 10 damage!\n")
        return True

    def bubble(self):
        enemyPlayer.doDamage(12)
        print("Tackle did 12 damage!\n")
        return True

    def AIAttack(self, enemy):
        """
        Attacks enemy Progmon with a randomly chosen attack
        Args:
            self (object) - WaterTurtle
            enemyPlayer (object) - enemy Progmon
        Returns:
            (string) - the attack that was used by the AI
            (bool) - True if the attack hit, otherwise False
        """
        attackToUse = random.randint(1, 5)
        tempHealth = enemyPlayer.getCurrentHealth()
        if(attackToUse == 1):
            self.aquaJet(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "AI Aqua Jet hit for 45 damage!", True
            else:
                return "AI Aqua Jet missed!\n", False
        if(attackToUse == 2):
            self.aquaTail(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "AI Aqua Tail hit!\n", True
            else:
                return "AI Aqua Tail missed!\n", False
        if(attackToUse == 3):
            self.waterPulse(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "AI Water Pulse hit!\n", True
            else:
                return "AI Water Pulse missed!\n", False
        if(attackToUse == 4):
            self.tackle(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "AI Tackle hit!\n", True
            else:
                return "AI Tackle missed!\n", False
        if(attackToUse == 5):
            self.bubble(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "AI Bubble hit!\n", True
            else:
                return "AI Bubble missed!\n", False

    def useHealthPotion(self):
        """
        Uses a healthPotion to heal 30 points of health
        Args:
            self (object) - WaterTurtle
        Returns:
            None
        """
        self.currentHealth = self.currentHealth + 30
        self.bag.remove("healthPotion")

    def bagEmpty(self):
        """
        Checks if the Bag is empty
        Args:
            self (object) - WaterTurtle
        Returns:
            (bool) - True if Bag is empty, otherwise False
        """
        if(self.bag):
            return False
        else:
            return True

import random

class WaterTurtle(Progmon):
    """
    Class for Water Turtle Progmon
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
        self.bag = ["healthPotion", "statBoost", "defenseBoost", "restorePotion"]
        self.attackList = ["Aqua Jet", "Aqua Tail", "Water Pulse", "Bubble"]
        self.stunned = False
        self.statBoost = False
        self.defenseBoost = False

    def doDamage(self, damageDone):
        """
        Deals damage to the enemy's health; set alive to False if health goes below 1
        Args:
            self (object) - WaterTurtle
            damageDone (int) - amount of damage to do
        Returns:
            None
        """
        if(self.defenseBoost == True):
            self.currentHealth = self.currentHealth - damageDone + 10
            self.defenseBoost = False
        else:
            self.currentHealth = self.currentHealth - damageDone

        if(self.currentHealth <= 0):
            self.currentHealth = 0
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

    def getAttackList(self):
        """
        Gets the attack list of Water Turtle
        Args:
            self (object) - Water Turtle
        Returns:
            Water Turtle's attackList
        """
        return self.attackList

    def setBag(self, newBag):
        """
        Sets the bag of Progmon
        Args:
            self (object)
            newBag (array) - what to set bag to
        Returns:
            None
        """
        self.bag = newBag

    def getBag(self):
        """
        Gets the bag list of WaterTurtle
        Args:
            self (object)
        Returns:
            WaterTurtle's bag
        """
        return self.bag

    def getCurrentHealth(self):
        """
        Gets the currentHealth of WaterTurtle
        Args:
            self (object) - WaterTurtle
        Returns:
            WaterTurtle's currentHealth
        """
        return self.currentHealth

    def setCurrentHealth(self, newHealth):
        """
        Sets the current health of WaterTurtle
        Args:
            self (object)
            newHealth (int) - what to set current health to
        Returns:
            None
        """
        self.currentHealth = newHealth

    def getHP(self):
        """
        Gets the max health of WaterTurtle
        Args:
            self (object) - WaterTurtle
        Returns:
            WaterTurtle's max health
        """
        return self.hp

    def setStunStatus(self, setter):
        """
        Sets the stun status of WaterTurtle
        Args:
            self (object)
            setter (boolean) - what to set stunned to
        Returns:
            None
        """
        self.stunned = setter

    def getStunStatus(self):
        """
        Gets the stun status of WaterTurtle
        Args:
            self (object)
        Returns:
            WaterTurtle's stunned status
        """
        return self.stunned

    def setDefenseBoost(self, setter):
        """
        Sets the defense boost of WaterTurtle
        Args:
            self (object)
            setter (boolean) - what to set defense boost to
        Returns:
            None
        """
        self.defenseBoost = setter

    def getDefenseBoost(self):
        """
        Gets the defense boost of WaterTurtle
        Args:
            self (object)
        Returns:
            WaterTurtle's defense boost
        """
        return self.defenseBoost

    def setStatBoost(self, setter):
        """
        Sets the stat boost of WaterTurtle
        Args:
            self (object)
            setter (boolean) - what to set stat boost to
        Returns:
            None
        """
        self.statBoost = setter

    def getStatBoost(self):
        """
        Gets the defense boost of WaterTurtle
        Args:
            self (object)
        Returns:
            WaterTurtle's defense boost
        """
        return self.statBoost

    def attack1(self, enemyPlayer):
        """
        Attacks enemy Progmon with Aqua Jet and has a chance to stun
        Args:
            self (object) - WaterTurtle
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True if attack hit, otherwise False
            (string) - attack message
        """
        chanceToHit = random.randint(1, 100)
        if(self.statBoost == True and chanceToHit <= 70):
            self.statBoost = False
            enemyPlayer.doDamage(55)
            enemyPlayer.setStunStatus(True)
            return True, "It did 55 damage and stunned the enemy!"
        if(chanceToHit <= 70):
            enemyPlayer.doDamage(45)
            return True, "Aqua Jet did 45 damage!"
        else:
            return False, "Aqua Jet missed!"

    def attack2(self, enemyPlayer):
        """
        Attacks enemy Progmon with Aqua Tail
        Args:
            self (object) - WaterTurtle
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True if attack hit, otherwise False
            (string) - attack message
        """
        chanceToHit = random.randint(1, 100)
        if(chanceToHit <= 55):
            enemyPlayer.doDamage(50)
            return True, "Aqua Tail did 50 damage!"
        else:
            return False, "Aqua Tail missed!"

    def attack3(self, enemyPlayer):
        """
        Attacks enemy Progmon with Water Pulse and has a chance to potentially stun
        Args:
            self (object) - WaterTurtle
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True if attack hit, otherwise False
            (string) - attack message
        """
        chanceToHit = random.randint(1, 100)
        if(self.statBoost == True and chanceToHit <= 48):
            self.statBoost = False
            enemyPlayer.doDamage(80)
            enemyPlayer.setStunStatus(True)
            return True, "It did 80 damage and stunned the enemy!"
        if(chanceToHit <= 48):
            enemyPlayer.doDamage(70)
            return True, "Water Pulse did 70 damage!"
        else:
            return False, "Water Pulse missed!"

    def attack4(self, enemyPlayer):
        """
        Attacks enemy Progmon with Bubble
        Args:
            self (object) - WaterTurtle
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True
            (string) - attack message
        """
        enemyPlayer.doDamage(12)
        return True, "Bubble did 12 damage!"

    def AIAttack(self, enemyPlayer):
        """
        Attacks enemy Progmon with a randomly chosen attack
        Args:
            self (object) - WaterTurtle
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True if attack hit, otherwise False
            (string) - the attack that was used by the AI
        """
        #randomly choose one of FireDragon's attacks and then use it
        #returns a string of which attack was used so that user can know what AI did/if it was successful
        attackToUse = random.randint(1, 4)
        tempHealth = enemyPlayer.getCurrentHealth()

        if(attackToUse == 1):
            attackHit = self.attack1(enemyPlayer) # ATTACK HIT / MISS TRACKER
            if attackHit[0] == True:
                if(tempHealth != enemyPlayer.getCurrentHealth()):
                    return True, str("{}".format(attackHit[1]))
            else:
                return False, str("{}".format(attackHit[1]))

        if(attackToUse == 2):
            attackHit = self.attack2(enemyPlayer) # ATTACK HIT / MISS TRACKER
            if attackHit[0] == True:
                if(tempHealth != enemyPlayer.getCurrentHealth()):
                    return True, str("{}".format(attackHit[1]))
            else:
                return False, str("{}".format(attackHit[1]))

        if(attackToUse == 3):
            attackHit = self.attack3(enemyPlayer) # ATTACK HIT / MISS TRACKER
            if attackHit[0] == True:
                if(tempHealth != enemyPlayer.getCurrentHealth()):
                    return True, str("{}".format(attackHit[1]))
            else:
                return False, str("{}".format(attackHit[1]))

        if(attackToUse == 4):
            attackHit = self.attack4(enemyPlayer) # ATTACK HIT / MISS TRACKER
            if attackHit[0] == True:
                if(tempHealth != enemyPlayer.getCurrentHealth()):
                    return True, str("{}".format(attackHit[1]))
            else:
                return False, str("{}".format(attackHit[1]))

    def useHealthPotion(self):
        """
        Uses a healthPotion to heal 30 points of health
        Args:
            self (object) - WaterTurtle
        Returns:
            (int) - amount of health that was healed for
        """
        if(self.currentHealth+30 > self.hp):
            hpToAdd = self.hp - self.currentHealth
            self.currentHealth + hpToAdd
            print("Health Potion healing Water Turtle for:", hpToAdd, "HP")
            self.bag.remove("healthPotion")
            return hpToAdd
        else:
            self.currentHealth + 30
            print("Health Potion healing Water Turtle for: 30HP")
            self.bag.remove("healthPotion")
            return 30

    def useRestorePotion(self):
        """
        Uses a restorePotion that heals to max hp
        Args:
            self (object) - WaterTurtle
        Returns:
            None
        """
        print("Restore Potion has healed Water Turtle to full health! All Boosts deactivated!")
        self.bag.remove("restorePotion")
        self.statBoost = False
        self.defenseBoost = False

    def useStatBoost(self):
        """
        Allows WaterTurtle to use a statBoost Potion
        Args:
            self (object) - WaterTurtle
        Returns:
            None
        """
        self.statBoost = True
        print("Stat Boost for Water Turtle activated! +10 damage and chance to stun on the next attack!")
        self.bag.remove("statBoost")

    def useDefenseBoost(self):
        """
        Allows WaterTurtle to use a defense Potion
        Args:
            self (object) - WaterTurtle
        Returns:
            None
        """
        self.defenseBoost = True
        print("Defense Boost for Water Turtle activated! Water Turtle will take 10 less damage on the next attack!")
        self.bag.remove("defenseBoost")

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

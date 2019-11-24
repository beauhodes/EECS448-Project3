import random

class ElectricCat(Progmon):
    """
    Class for the Electric Cat Progmon
    """
    def __init__(self):
        """
        Creates variables associated with ElectricCat
        Args:
            self (object) - ElectricCat
        Returns:
            None
        """
        self.name = "Electric Cat"
        self.hp = 250
        self.currentHealth = 250
        self.alive = True
        self.bag = ["healthPotion", "statBoost", "defenseBoost", "restorePotion"]
        self.attackList = ["Lightning Bolt", "Electric Scratch", "Energy Beam", "Bite"]
        self.stunned = False
        self.statBoost = False
        self.defenseBoost = False

    def doDamage(self, damageDone):
        """
        Deals damage to the enemy's health; set alive to False if health goes below 1
        Args:
            self (object) - ElectricCat
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
        Checks if ElectricCat is alive
        Args:
            self (object) - ElectricCat
        Returns:
            (bool) - True if ElectricCat is alive, otherwise False
        """
        if(self.alive == True):
            return True
        else:
            return False

    def getAttackList(self):
        """
        Gets the attack list of Electric Cat
        Args:
            self (object) - Electric Cat
        Returns:
            Electric Cat's attackList
        """
        return self.attackList

    def setBag(self, newBag):
        """
        Sets the bag of Electric Cat
        Args:
            self (object) - Electric Cat
            newBag (array) - what to set bag to
        Returns:
            None
        """
        self.bag = newBag

    def getBag(self):
        """
        Gets the bag list of Electric Cat
        Args:
            self (object) - Electric Cat
        Returns:
            Electric Cat's bag
        """
        return self.bag

    def getCurrentHealth(self):
        """
        Gets the currentHealth of ElectricCat
        Args:
            self (object) - ElectricCat
        Returns:
            ElectricCat's currentHealth
        """
        return self.currentHealth

    def setCurrentHealth(self, newHealth):
        """
        Sets the current health of ElectricCat
        Args:
            self (object) - ElectricCat
            newHealth (int) - what to set current health to
        Returns:
            None
        """
        self.currentHealth = newHealth

    def getHP(self):
        """
        Gets the max health of ElectricCat
        Args:
            self (object) - ElectricCat
        Returns:
            ElectricCat's max health
        """
        return self.hp

    def setStunStatus(self, setter):
        """
        Sets the stun status of ElectricCat
        Args:
            self (object) - ElectricCat
            setter (boolean) - what to set stunned to
        Returns:
            None
        """
        self.stunned = setter

    def getStunStatus(self):
        """
        Gets the stun status of ElectricCat
        Args:
            self (object) - ElectricCat
        Returns:
            ElectricCat's stunned status
        """
        return self.stunned

    def setDefenseBoost(self, setter):
        """
        Sets the defense boost of ElectricCat
        Args:
            self (object) - ElectricCat
            setter (boolean) - what to set defense boost to
        Returns:
            None
        """
        self.defenseBoost = setter

    def getDefenseBoost(self):
        """
        Gets the defense boost of ElectricCat
        Args:
            self (object) - ElectricCat
        Returns:
            ElectricCat's defense boost
        """
        return self.defenseBoost

    def setStatBoost(self, setter):
        """
        Sets the stat boost of ElectricCat
        Args:
            self (object) - ElectricCat
            setter (boolean) - what to set stat boost to
        Returns:
            None
        """
        self.statBoost = setter

    def getStatBoost(self):
        """
        Gets the defense boost of ElectricCat
        Args:
            self (object) - ElectricCat
        Returns:
            ElectricCat's defense boost
        """
        return self.statBoost

    def attack1(self, enemyPlayer): # 90 damage, 45 accuracy
        """
        Attacks enemy Progmon with Lightning Bolt
        Args:
            self (object) - ElectricCat
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True if attack hit, otherwise False
            (string) - attack message
        """
        chanceToHit = random.randint(1, 100)
        if(self.statBoost == True and chanceToHit <= 45):
            self.statBoost = False
            enemyPlayer.doDamage(100)
            enemyPlayer.setStunStatus(True)
            return True, "It did 100 damage and stunned the enemy!"
        elif(chanceToHit <= 45):
            enemyPlayer.doDamage(90)
            return True, "Lightning Bolt did 90 damage!"
        else:
            return False, "Lightning Bolt missed!"

    def attack2(self, enemyPlayer): # 40 damage, 90 accuracy
        """
        Attacks enemy Progmon with Electric Scratch
        Args:
            self (object) - ElectricCat
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True if attack hit, otherwise False
            (string) - attack message
        """
        chanceToHit = random.randint(1, 100)
        if(chanceToHit <= 90):
            enemyPlayer.doDamage(40)
            return True, "Electric Scratch did 40 damage!"
        else:
            return False, "Electric Scratch missed!"

    def attack3(self, enemyPlayer): # 110 damage, 40 accuracy
        """
        Attacks enemy Progmon with Energy Beam
        Args:
            self (object) - ElectricCat
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True if attack hit, otherwise False
            (string) - attack message
        """
        chanceToHit = random.randint(1, 100)
        if(self.statBoost == True and chanceToHit <= 40):
            self.statBoost = False
            enemyPlayer.doDamage(120)
            enemyPlayer.setStunStatus(True)
            return True, "It did 120 damage and stunned the enemy!"
        elif(chanceToHit <= 40):
            enemyPlayer.doDamage(110)
            return True, "Energy Beam did 110 damage!"
        else:
            return False, "Energy Beam missed!"

    def attack4(self, enemyPlayer): # 20 damage, 100 accuracy
        """
        Attacks enemy Progmon with Bite
        Args:
            self (object) - ElectricCat
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True
            (string) - attack message
        """
        enemyPlayer.doDamage(20)
        return True, "Bite did 20 damage!"

    def AIAttack(self, enemyPlayer):
        """
        Attacks enemy Progmon with a randomly chosen attack
        Args:
            self (object) - ElectricCat
            enemyPlayer (object) - enemy Progmon
        Returns:
            (string) - the attack that was used by the AI
            (bool) - True if attack hit, otherwise False
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
        Uses a healthPotion to heal up to 30 points of health
        Args:
            self (object) - ElectricCat
        Returns:
            (int) - amount of health that was healed for
        """
        if(self.currentHealth+30 > self.hp):
            hpToAdd = self.hp - self.currentHealth
            self.currentHealth + hpToAdd
            print("Health Potion healing Electric Cat for:", hpToAdd, "HP")
            self.bag.remove("healthPotion")
            return hpToAdd
        else:
            self.currentHealth + 30
            print("Health Potion healing Electric Cat for: 30HP")
            self.bag.remove("healthPotion")
            return 30

    def useRestorePotion(self):
        """
        Uses a restorePotion that heals ElectricCat to max hp
        Args:
            self (object) - Electric Cat
        Returns:
            None
        """
        print("Restore Potion has healed Electric Cat to full health! All Boosts deactivated!")
        self.bag.remove("restorePotion")
        self.statBoost = False
        self.defenseBoost = False

    def useStatBoost(self):
        """
        Allows ElectricCat to use a statBoost Potion
        Args:
            self (object) - Electric Cat
        Returns:
            None
        """
        self.statBoost = True
        print("Stat Boost for Electric Cat activated! +10 damage and chance to stun on the next attack!")
        self.bag.remove("statBoost")

    def useDefenseBoost(self):
        """
        Allows Electric Cat to use a defense Potion
        Args:
            self (object) - ElectricCat
        Returns:
            None
        """
        self.defenseBoost = True
        print("Defense Boost for Electric Cat activated! Electric Cat will take 10 less damage on the next attack!")
        self.bag.remove("defenseBoost")

    def bagEmpty(self):
        """
        Checks if the Bag is empty
        Args:
            self (object) - ElectricCat
        Returns:
            (bool) - True if Bag is empty, otherwise False
        """
        if(self.bag):
            return False
        else:
            return True

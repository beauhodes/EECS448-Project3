import random

class FinalBoss(Progmon):
    """
    Class for the Final Boss Progmon
    """
    def __init__(self):
        """
        Creates variables associated with FinalBoss
        Args:
            self (object) - FinalBoss
        Returns:
            None
        """
        self.name = "Final Boss"
        self.hp = 120
        self.currentHealth = 120
        self.alive = True
        self.bag = ["healthPotion", "statBoost", "defenseBoost", "restorePotion"]
        self.attackList = ["Giga Impact", "Psychic", "Mega Kick", "Ancient Power"]
        self.stunned = False
        self.statBoost = False
        self.defenseBoost = False

    def doDamage(self, damageDone):
        """
        Deals damage to the enemy's health; set alive to False if health goes below 1
        Args:
            self (object) - FinalBoss
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
        Checks if FinalBoss is alive
        Args:
            self (object) - FinalBoss
        Returns:
            (bool) - True if FinalBoss is alive, otherwise False
        """
        if(self.alive == True):
            return True
        else:
            return False

    def getAttackList(self):
        """
        Gets the attack list of FinalBoss
        Args:
            self (object) - FinalBoss
        Returns:
            FinalBoss's attackList
        """
        return self.attackList

    def setBag(self, newBag):
        """
        Sets the bag of FinalBoss
        Args:
            self (object) - FinalBoss
            newBag (array) - what to set bag to
        Returns:
            None
        """
        self.bag = newBag

    def getBag(self):
        """
        Gets the bag list of FinalBoss
        Args:
            self (object) - FinalBoss
        Returns:
            FinalBoss's bag
        """
        return self.bag

    def getCurrentHealth(self):
        """
        Gets the currentHealth of FinalBoss
        Args:
            self (object) - FinalBoss
        Returns:
            FinalBoss's currentHealth
        """
        return self.currentHealth

    def setCurrentHealth(self, newHealth):
        """
        Sets the current health of FinalBoss
        Args:
            self (object) - FinalBoss
            newHealth (int) - what to set current health to
        Returns:
            None
        """
        self.currentHealth = newHealth

    def getHP(self):
        """
        Gets the max health of FinalBoss
        Args:
            self (object) - FinalBoss
        Returns:
            FinalBoss's max health
        """
        return self.hp

    def setStunStatus(self, setter):
        """
        Sets the stun status of FinalBoss
        Args:
            self (object) - FinalBoss
            setter (boolean) - what to set stunned to
        Returns:
            None
        """
        self.stunned = setter

    def getStunStatus(self):
        """
        Gets the stun status of FinalBoss
        Args:
            self (object) - FinalBoss
        Returns:
            FinalBoss's stunned status
        """
        return self.stunned

    def setDefenseBoost(self, setter):
        """
        Sets the defense boost of FinalBoss
        Args:
            self (object) - FinalBoss
            setter (boolean) - what to set defense boost to
        Returns:
            None
        """
        self.defenseBoost = setter

    def getDefenseBoost(self):
        """
        Gets the defense boost of FinalBoss
        Args:
            self (object) - FinalBoss
        Returns:
            FinalBoss's defense boost
        """
        return self.defenseBoost

    def setStatBoost(self, setter):
        """
        Sets the stat boost of FinalBoss
        Args:
            self (object) - FinalBoss
            setter (boolean) - what to set stat boost to
        Returns:
            None
        """
        self.statBoost = setter

    def getStatBoost(self):
        """
        Gets the defense boost of FinalBoss
        Args:
            self (object) - FinalBoss
        Returns:
            FinalBoss's defense boost
        """
        return self.statBoost

    def attack1(self, enemyPlayer):
        """
        Attacks enemy Progmon with Giga Impact
        Args:
            self (object) - FinalBoss
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True if attack hit, otherwise False
            (string) - attack message
        """
        chanceToHit = random.randint(1, 100)
        if(self.statBoost == True and chanceToHit <= 90):
            self.statBoost = False
            enemyPlayer.doDamage(160)
            enemyPlayer.setStunStatus(True)
            return True, "It did 160 damage and stunned the enemy!"
        if(chanceToHit <= 90):
            enemyPlayer.doDamage(150)
            return True, "Giga Impact did 150 damage!"
        else:
            return False, "Giga Impact missed!"

    def attack2(self, enemyPlayer):
        """
        Attacks enemy Progmon with Psychic
        Args:
            self (object) - FinalBoss
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True if attack hit, otherwise False
            (string) - attack message
        """
        chanceToHit = random.randint(1, 100)
        if(chanceToHit <= 99):
            enemyPlayer.doDamage(90)
            return True, "Psychic did 90 damage!"
        else:
            return False, "Psychic missed!"

    def attack3(self, enemyPlayer):
        """
        Attacks enemy Progmon with Mega Kick
        Args:
            self (object) - FinalBoss
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True if attack hit, otherwise False
            (string) - attack message
        """
        chanceToHit = random.randint(1, 100)
        if(self.statBoost == True and chanceToHit <= 75):
            self.statBoost = False
            enemyPlayer.doDamage(130)
            enemyPlayer.setStunStatus(True)
            return True, "It did 130 damage and stunned the enemy!"
        if(chanceToHit <= 75):
            enemyPlayer.doDamage(120)
            return True, "Mega Kick did 120 damage!"
        else:
            return False, "Mega Kick missed!"

    def attack4(self, enemyPlayer):
        """
        Attacks enemy Progmon with Ancient Power
        Args:
            self (object) - FinalBoss
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True
            (string) - attack message
        """
        enemyPlayer.doDamage(60)
        return True, "Ancient Power did 60 damage!"

    def AIAttack(self, enemyPlayer):
        """
        Attacks enemy Progmon with a randomly chosen attack
        Args:
            self (object) - FinalBoss
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
        Uses a healthPotion to heal up to 30 points of health
        Args:
            self (object) - FinalBoss
        Returns:
            (int) - amount of health that was healed for
        """
        if(self.currentHealth+30 > self.hp):
            hpToAdd = self.hp - self.currentHealth
            self.currentHealth + hpToAdd
            print("Health Potion healing Final Boss for:", hpToAdd, "HP")
            self.bag.remove("healthPotion")
            return hpToAdd
        else:
            self.currentHealth + 30
            print("Health Potion healing Final Boss for: 30HP")
            self.bag.remove("healthPotion")
            return 30

    def useRestorePotion(self):
        """
        Uses a restorePotion that heals FinalBoss to max hp
        Args:
            self (object) - FinalBoss
        Returns:
            None
        """
        print("Restore Potion has healed Final Boss to full health! All Boosts deactivated!")
        self.bag.remove("restorePotion")
        self.statBoost = False
        self.defenseBoost = False

    def useStatBoost(self):
        """
        Allows FinalBoss to use a statBoost Potion
        Args:
            self (object) - FinalBoss
        Returns:
            None
        """
        self.statBoost = True
        print("Stat Boost for Final Boss activated! +10 damage and chance to stun on the next attack!")
        self.bag.remove("statBoost")

    def useDefenseBoost(self):
        """
        Allows FinalBoss to use a defense Potion
        Args:
            self (object) - FinalBoss
        Returns:
            None
        """
        self.defenseBoost = True
        print("Defense Boost for Final Boss activated! Final Boss will take 10 less damage on the next attack!")
        self.bag.remove("defenseBoost")

    def bagEmpty(self):
        """
        Checks if the Bag is empty
        Args:
            self (object) - FinalBoss
        Returns:
            (bool) - True if Bag is empty, otherwise False
        """
        if(self.bag):
            return False
        else:
            return True

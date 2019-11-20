import random

class FinalBoss:
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
        self.bag = ["healthPotion", "statBoost", "defenseBoost"]
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
        Gets the attack list of Progmon
        Args:
            self (object)
        Returns:
            Progmon's attackList
        """
        return self.attackList

    def getCurrentHealth(self):
        """
        Gets the currentHealth of FinalBoss
        Args:
            self (object) - FinalBoss
        Returns:
            FinalBoss's currentHealth
        """
        return self.currentHealth

    def getHp(self):
        """
        Gets the currentHealth of FinalBoss
        Args:
            self (object) - FinalBoss
        Returns:
            FinalBoss's currentHealth
        """
        return self.hp

    def setStunStatus(self, setter):
        """
        Sets the stun status of Progmon
        Args:
            self (object)
        Returns:
            None
        """
        self.stunned = setter

    def getStunStatus(self):
        """
        Gets the stun status of Progmon
        Args:
            self (object)
        Returns:
            Progmon's stunned
        """
        return self.stunned

    def attack1(self):
        """
        Attacks enemy Progmon with Giga Impact
        Args:
            self (object) - FinalBoss
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        chanceToHit = random.randint(1, 101)
        if(self.statBoost == True and chanceToHit <= 90):
            self.statBoost = False
            enemyPlayer.doDamage(150)
            enemyPlayer.setStunStatus()
            print("Final Boss does 150 damage and stuns the enemy!\n")
            return True
        if(chanceToHit <= 90):
            enemyPlayer.doDamage(150)
            print("Giga Impact did 150 damage!\n")
            return True
        else:
            print("Giga Impact missed!\n")
            return False

    def attack2(self):
        """
        Attacks enemy Progmon with Psychic
        Args:
            self (object) - FinalBoss
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        chanceToHit = random.randint(1, 101)
        if(chanceToHit <= 99):
            enemyPlayer.doDamage(90)
            print("Psychic did 90 damage!\n")
            return True
        else:
            print("Psychic missed!\n")
            return False

    def attack3(self):
        """
        Attacks enemy Progmon with Mega Kick
        Args:
            self (object) - FinalBoss
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        chanceToHit = random.randint(1, 101)
        if(self.statBoost == True and chanceToHit <= 75):
            self.statBoost = False
            enemyPlayer.doDamage(120)
            enemyPlayer.setStunStatus()
            print("Final Boss does 120 damage and stuns the enemy!\n")
            return True
        if(chanceToHit <= 75):
            enemyPlayer.doDamage(120)
            print("Mega Kick did 120 damage!\n")
            return True
        else:
            print("Mega Kick missed!\n")
            return False

    def attack4(self):
        """
        Attacks enemy Progmon with Ancient Power
        Args:
            self (object) - FinalBoss
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        enemyPlayer.doDamage(60)
        print("Ancient Power did 60 damage!\n")
        return True

    def AIAttack(self, enemyPlayer):
        """
        Attacks enemy Progmon with a randomly chosen attack
        Args:
            self (object) - FinalBoss
            enemyPlayer (object) - enemy Progmon
        Returns:
            (string) - the attack that was used by the AI
            (bool) - True if the attack hit, otherwise False
        """
        attackToUse = random.randint(1, 5)
        tempHealth = enemyPlayer.getCurrentHealth()
        if(attackToUse == 1):
            self.attack1(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "AI Giga Impact hit for 45 damage!", True
            else:
                return "AI Giga Impact missed!\n", False
        if(attackToUse == 2):
            self.attack2(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "AI Psychic hit!\n", True
            else:
                return "AI Psychic missed!\n", False
        if(attackToUse == 3):
            self.attack3(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "AI Mega Kick hit!\n", True
            else:
                return "AI Mega Kick missed!\n", False
        if(attackToUse == 4):
            self.attack4(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "AI Ancient Power hit!\n", True
            else:
                return "AI Ancient Power missed!\n", False

    def useHealthPotion(self):
        """
        Uses a healthPotion to heal 30 points of health
        Args:
            self (object) - FinalBoss
        Returns:
            None
        """
        if(self.currentHealth+30 > self.hp):
            hpToAdd = self.hp - self.currentHealth
            self.currentHealth + hpToAdd
            print("Health Potion healed you for:", hpToAdd, "\n")
            self.bag.remove("healthPotion")

        else:
            self.currentHealth + 30
            print("Health Potion healed you for: 30\n")
            self.bag.remove("healthPotion")

    def useStatBoost(self):
        """
        Allows this Progmon to use a statBoost Potion
        Args:
            self (object) - FinalBoss
        Returns:
            None
        """
        self.statBoost = True
        print("Stat Boost for Final Boss is activated!\n You will do +10 damage and have a chance to stun!\n")
        self.bag.remove("statBoost")

    def useDefenseBoost(self):
        """
        Allows this progmon to use a defense Potion
        Args:
            self (object) - FinalBoss
        Returns:
            None
        """
        self.defenseBoost = True
        print("Defense boost for Final Boss is now activated!\n You will take 10 less damage on the next attack.\n")
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

import random

class FireDragon:
    """
    Class for the Fire Dragon Progmon
    """
    def __init__(self):
        """
        Creates variables associated with FireDragon
        Args:
            self (object) - FireDragon
        Returns:
            None
        """
        self.name = "Fire Dragon"
        self.hp = 300
        self.currentHealth = 300
        self.alive = True
        self.bag = ["healthPotion", "statBoost", "defenseBoost"]
        self.stunned = False
        self.statBoost = False
        self.defenseBoost = False

    def doDamage(self, damageDone):
        """
        Deals damage to the enemy's health; set alive to False if health goes below 1
        Args:
            self (object) - FireDragon
            damageDone (int) - amount of damage to do
        Returns:
            None
        """
        if(self.defenseBoost == True):
            self.currentHealth = self.currentHealth - damageDone + 10
        else:
            self.currentHealth = self.currentHealth - damageDone

        if(self.currentHealth <= 0):
            self.alive = False

    def checkAlive(self):
        """
        Checks if FireDragon is alive
        Args:
            self (object) - FireDragon
        Returns:
            (bool) - True if FireDragon is alive, otherwise False
        """
        if(self.alive == True):
            return True
        else:
            return False

    def getCurrentHealth(self):
        """
        Gets the currentHealth of FireDragon
        Args:
            self (object) - FireDragon
        Returns:
            FireDragon's currentHealth
        """
        return self.currentHealth

    def getHp(self):
        """
        Gets the currentHealth of FireDragon
        Args:
            self (object) - FireDragon
        Returns:
            FireDragon's currentHealth
        """
        return self.hp

    def setStunStatus(self):
        self.stunned = True

    def getStunStatus(self):
        return self.stunned

    def RoarAttack(self, enemyPlayer): # 80 damage, 45 accuracy
        """
        Attacks enemy Progmon with Roar
        Args:
            self (object) - FireDragon
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        chanceToHit = random.randint(1, 101)
        if(self.statBoost == True and chanceToHit <= 45):
            self.statBoost = False
            enemyPlayer.doDamage(80)
            enemyPlayer.setStunStatus()
            print("Fire Dragon does 80 damage and stuns the enemy!\n")
        if(chanceToHit <= 45):
            enemyPlayer.doDamage(80)
            print("Roar did 80 damage!\n")
            return True
        else:
            print("Roar missed!\n")
            return False

    def ClawSwipeAttack(self, enemyPlayer): # 35 damage, 90 accuracy
        """
        Attacks enemy Progmon with Claw Swipe
        Args:
            self (object) - FireDragon
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        chanceToHit = random.randint(1, 101)
        if(chanceToHit <= 90):
            enemyPlayer.doDamage(35)
            print("Claw Swipe did 35 damage!\n")
            return True
        else:
            print("Claw Swipe missed!\n")
            return False

    def FireBreathAttack(self, enemyPlayer): # 140 damage, 30 accuracy
        """
        Attacks enemy Progmon with Fire Breath
        Args:
            self (object) - FireDragon
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        chanceToHit = random.randint(1, 101)
        if(self.statBoost == True and chanceToHit <= 30):
            self.statBoost = False
            enemyPlayer.doDamage(140)
            enemyPlayer.setStunStatus()
            print("Fire Dragon does 140 damage and stuns the enemy!\n")
        if(chanceToHit <= 30):
            enemyPlayer.doDamage(140)
            print("Fire Breath did 140 damage!\n")
            return True
        else:
            print("Fire Breath missed!\n")
            return False

    def TailWhipAttack(self, enemyPlayer): # 20 damage, 100 accuracy
        """
        Attacks enemy Progmon with Tail Whip
        Args:
            self (object) - FireDragon
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        enemyPlayer.doDamage(20)
        print("Tail Whip did 20 damage!\n")
        return True

    def AIAttack(self, enemyPlayer):
        """
        Attacks enemy Progmon with a randomly chosen attack
        Args:
            self (object) - FireDragon
            enemyPlayer (object) - enemy Progmon
        Returns:
            (string) - the attack that was used by the AI
            (bool) - True if the attack hit, otherwise False
        """
        #randomly choose one of FireDragon's attacks and then use it
        #returns a string of which attack was used so that user can know what AI did/if it was successful
        attackToUse = random.randint(1, 5)
        tempHealth = enemyPlayer.getCurrentHealth()
        if(attackToUse == 1):
            self.RoarAttack(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "Roar", True
            else:
                return "Roar", False
        if(attackToUse == 2):
            self.ClawSwipeAttack(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "ClawSwipe", True
            else:
                return "ClawSwipe", False
        if(attackToUse == 3):
            self.FireBreathAttack(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "FireBreath", True
            else:
                return "FireBreath", False
        if(attackToUse == 4):
            self.TailWhipAttack(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "TailWhip", True
            else:
                return "TailWhip", False

    def useHealthPotion(self):
        """
        Uses a healthPotion to heal 30 points of health
        Args:
            self (object) - FireDragon
        Returns:
            None
        """
        if(self.currentHealth+30 > self.hp):
            hpToAdd = self.hp - self.currentHealth
            self.currentHealth + hpToAdd
            print("Health potion healed you for:", hpToAdd, "\n")
            self.bag.remove("healthPotion")

        else:
            self.currentHealth + 30
            print("Health potion healed you for: 30\n")
            self.bag.remove("healthPotion")

    def useStatBoost(self):
        """
        Allows this Progmon to use a statBoost Potion
        Args:
            self (object) - FireDragon
        Returns:
            None
        """
        self.statBoost = True
        print("Stat Boost for Fire Dragon is activated!\n You will do +10 damage and have a chance to stun!\n")
        self.bag.remove("statBoost")

    def useDefenseBoost(self):
        """
        Allows this progmon to use a defense Potion
        Args:
            self (object) - FireDragon
        Returns:
            None
        """
        self.defenseBoost = True
        print("Defense boost for Fire Dragon is now activated!\n You will take 10 less damage on the next attack.\n")
        self.bag.remove("defenseBoost")

    def bagEmpty(self):
        """
        Checks if the Bag is empty
        Args:
            self (object) - FireDragon
        Returns:
            (bool) - True if Bag is empty, otherwise False
        """
        if(self.bag):
            return False
        else:
            return True

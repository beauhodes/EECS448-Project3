import random

class ElectricCat:
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
        self.bag = ["healthPotion", "statBoost", "defenseBoost"]
        self.stunned = False
        self.statBoost = False

    def doDamage(self, damageDone):
        """
        Deals damage to the enemy's health; set alive to False if health goes below 1
        Args:
            self (object) - ElectricCat
            damageDone (int) - amount of damage to do
        Returns:
            None
        """
        self.currentHealth = self.currentHealth - damageDone
        if(self.currentHealth <= 0):
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

    def getCurrentHealth(self):
        """
        Gets the currentHealth of ElectricCat
        Args:
            self (object) - ElectricCat
        Returns:
            ElectricCat's currentHealth
        """
        return self.currentHealth

    def getHp(self):
        """
        Gets the currentHealth of ElectricCat
        Args:
            self (object) - ElectricCat
        Returns:
            ElectricCat's currentHealth
        """
        return self.hp

    def setStunStatus(self):
        self.stunned = True

    def getStunStatus(self):
        return self.stunned

    def LightningBoltAttack(self, enemyPlayer): # 90 damage, 45 accuracy
        """
        Attacks enemy Progmon with Lightning Bolt
        Args:
            self (object) - ElectricCat
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        chanceToHit = random.randint(1, 101)
        if(chanceToHit <= 45):
            enemyPlayer.doDamage(90)
            print("Lightning Bolt did 90 damage!\n")
            return True
        else:
            print("Lightning Bolt missed!\n")
            return False

    def ElectricScratchAttack(self, enemyPlayer): # 40 damage, 90 accuracy
        """
        Attacks enemy Progmon with Electric Scratch
        Args:
            self (object) - ElectricCat
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        chanceToHit = random.randint(1, 101)
        if(chanceToHit <= 90):
            enemyPlayer.doDamage(40)
            print("Electric Scratch did 40 damage!\n")
            return True
        else:
            print("Electric Scratch missed!\n")
            return False

    def EnergyBeamAttack(self, enemyPlayer): # 110 damage, 40 accuracy
        """
        Attacks enemy Progmon with Energy Beam
        Args:
            self (object) - ElectricCat
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        chanceToHit = random.randint(1, 101)
        if(chanceToHit <= 40):
            enemyPlayer.doDamage(110)
            print("Energy Beam did 110 damage!\n")
            return True
        else:
            print("Energy Beam missed!\n")
            return False

    def BiteAttack(self, enemyPlayer): # 20 damage, 100 accuracy
        """
        Attacks enemy Progmon with Bite
        Args:
            self (object) - ElectricCat
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        enemyPlayer.doDamage(20)
        print("Bite did 20 damage!\n")
        return True

    def AIAttack(self, enemyPlayer):
        """
        Attacks enemy Progmon with a randomly chosen attack
        Args:
            self (object) - ElectricCat
            enemyPlayer (object) - enemy Progmon
        Returns:
            (string) - the attack that was used by the AI
            (bool) - True if the attack hit, otherwise False
        """
        #randomly choose one of ElectricCat's attacks and then use it
        #returns a string of which attack was used so that user can know what AI did/if it was successful
        attackToUse = random.randint(1, 5)
        tempHealth = enemyPlayer.getCurrentHealth()
        if(attackToUse == 1):
            self.LightningBoltAttack(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "LightningBolt", True
            else:
                return "LightningBolt", False
        if(attackToUse == 2):
            self.ElectricScratchAttack(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "ElectricScratch", True
            else:
                return "ElectricScratch", False
        if(attackToUse == 3):
            self.EnergyBeamAttack(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "EnergyBeam", True
            else:
                return "EnergyBeam", False
        if(attackToUse == 4):
            self.BiteAttack(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "Bite", True
            else:
                return "Bite", False

    def useHealthPotion(self):
        """
        Uses a healthPotion to heal 30 points of health
        Args:
            self (object) - ElectricCat
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
            self (object) - WaterTurtle
        Returns:
            None
        """
        self.statBoost = True
        print("Stat Boost for Electric Cat is activated!\n You will do +10 damage and have a chance to stun!\n")
        self.bag.remove("statBoost")

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

import random

class ElectricCat:
    """
    Class for fire dragon fighter
    """

    def __init__(self):
        """
        Creates variables associated with the class

        Args: None

        Returns: None
        """

        self.name = "Electric Cat"
        self.hp = 250
        self.currentHealth = 250
        self.alive = True
        self.bag = ["healthPotion"] #will add more after project 3

    def doDamage(self, damageDone):
        """
        Deals damage to the dragon's health, set alive to false if health gets below 1

        Args:
        damageDone: Amount of damage to do

        Returns: None
        """

        self.currentHealth = self.currentHealth - damageDone
        if (self.currentHealth <= 0):
            self.alive = False

    def checkAlive(self):
        """
        Checks if the dragon is alive

        Args: None
        Returns: None
        """

        if(self.alive == True):
            return True
        else:
            return False

    def getCurrentHealth(self):
        """
        Gets current health

        Args: None

        Returns: Current health
        """
        return self.currentHealth

    def LightningBoltAttack(self, enemyPlayer):
        """
        Attacks enemy fighter object with lightning bolt

        Args:
        enemyPlayer: The enemy fighter object

        Returns: None
        """

        chanceToHit = random.randint(1,101)
        if (chanceToHit <= 45):
            enemyPlayer.doDamage(90)
            print("Lightning Bolt did 90 damage!\n")
        else:
            print("Lightning Bolt missed!\n")

    def ElectricScratchAttack(self, enemyPlayer):
        """
        Attacks enemy fighter object with electric scratch

        Args:
        enemyPlayer: The enemy fighter object

        Returns: None
        """

        chanceToHit = random.randint(1,101)
        if (chanceToHit <= 90):
            enemyPlayer.doDamage(40)
            print("Electric Scratch did 40 damage!\n")
        else:
            print("Electric Scratch missed!\n")

    def EnergyBeamAttack(self, enemyPlayer):
        """
        Attacks enemy fighter object with energy beam

        Args:
        enemyPlayer: The enemy fighter object

        Returns: None
        """

        chanceToHit = random.randint(1,101)
        if (chanceToHit <= 40):
            enemyPlayer.doDamage(110)
            print("Energy Beam did 110 damage!\n")
        else:
            print("Energy Beam missed!\n")

    def BiteAttack(self, enemyPlayer):
        """
        Attacks enemy fighter object with bite

        Args:
        enemyPlayer: The enemy fighter object

        Returns: None
        """

        enemyPlayer.doDamage(20)
        print("Bite did 20 damage!\n")

    def AIAttack(self, enemyPlayer):
        """
        Attacks enemy fighter object with a randomly chosen attack

        Args:
        enemyPlayer: The enemy fighter object

        Returns:
        String of which attack was used
        Boolean of whether it succeeded or not
        """

        #randomly choose one of Electric Cat's attacks and then use it
        #returns a string of which attack was used so that user can know what AI did/if it was successful
        attackToUse = random.randint(1,5)
        tempHealth = enemyPlayer.getCurrentHealth()
        if (attackToUse == 1):
            self.LightningBoltAttack(enemyPlayer)
            if (tempHealth != enemyPlayer.getCurrentHealth()):
                return "LightningBolt", True
            else:
                return "LightningBolt", False
        if (attackToUse == 2):
            self.ElectricScratchAttack(enemyPlayer)
            if (tempHealth != enemyPlayer.getCurrentHealth()):
                return "ElectricScratch", True
            else:
                return "ElectricScratch", False
        if (attackToUse == 3):
            self.EnergyBeamAttack(enemyPlayer)
            if (tempHealth != enemyPlayer.getCurrentHealth()):
                return "EnergyBeam", True
            else:
                return "EnergyBeam", False
        if (attackToUse == 4):
            self.BiteAttack(enemyPlayer)
            if (tempHealth != enemyPlayer.getCurrentHealth()):
                return "Bite", True
            else:
                return "Bite", False

    def useHealthPotion(self):
        """
        Uses health potion to heal 30 points of health

        Args: None

        Returns: None
        """

        self.currentHealth = self.currentHealth + 30
        self.bag.remove("healthPotion")

    def bagEmpty(self):
        """
        Checks if bag is empty

        Args: None

        Returns: None
        """

        if (self.bag):
            return False
        else:
            return True

import random

class FireDragon:
    """
    Class for fire dragon fighter
    """

    def __init__(self):
        """
        Creates variables associated with the class

        Args: None

        Returns: None
        """

        #continue to add features
        self.name = "Fire Dragon"
        self.hp = 300
        self.currentHealth = 300
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

    def RoarAttack(self, enemyPlayer): #80 damage, 45 accuracy
        """
        Attacks enemy fighter object with roar

        Args:
        enemyPlayer: The enemy fighter object

        Returns: None
        """

        chanceToHit = random.randint(1,101)
        if (chanceToHit <= 45):
            enemyPlayer.doDamage(80)

    def ClawSwipeAttack(self, enemyPlayer): #35 damage, 90 accuracy
        """
        Attacks enemy fighter object with claw swipe

        Args:
        enemyPlayer: The enemy fighter object

        Returns: None
        """

        chanceToHit = random.randint(1,101)
        if (chanceToHit <= 90):
            enemyPlayer.doDamage(35)

    def FireBreathAttack(self, enemyPlayer): #140 damage, 30 accuracy
        """
        Attacks enemy fighter object with fire breath

        Args:
        enemyPlayer: The enemy fighter object

        Returns: None
        """
        chanceToHit = random.randint(1,101)
        if (chanceToHit <= 30):
            enemyPlayer.doDamage(140)

    def TailWhipAttack(self, enemyPlayer): #20 damage, 100 accuracy
        """
        Attacks enemy fighter object with tail whip

        Args:
        enemyPlayer: The enemy fighter object

        Returns: None
        """
        enemyPlayer.doDamage(20)

    def AIAttack(self, enemyPlayer):
        """
        Attacks enemy fighter object with a randomly chosen attack

        Args:
        enemyPlayer: The enemy fighter object

        Returns:
        String of which attack was used
        Boolean of whether it succeeded or not
        """
        #randomly choose one of Fire Dragon's attacks and then use it
        #returns a string of which attack was used so that user can know what AI did/if it was successful
        attackToUse = random.randint(0,5)
        tempHealth = enemyPlayer.getCurrentHealth()
        if (attackToUse == 1):
            RoarAttack(enemyPlayer)
            if (tempHealth != enemyPlayer.getCurrentHealth()):
                return "Roar", True
            else:
                return "Roar", False
        if (attackToUse == 2):
            ClawSwipeAttack(enemyPlayer)
            if (tempHealth != enemyPlayer.getCurrentHealth()):
                return "ClawSwipe", True
            else:
                return "ClawSwipe", False
        if (attackToUse == 3):
            FireBreathAttack(enemyPlayer)
            if (tempHealth != enemyPlayer.getCurrentHealth()):
                return "FireBreath", True
            else:
                return "FireBreath", False
        if (attackToUse == 4):
            SlashAttack(enemyPlayer)
            if (tempHealth != enemyPlayer.getCurrentHealth()):
                return "TailWhip", True
            else:
                return "TailWhip", False

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

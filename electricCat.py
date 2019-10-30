import random

class ElectricCat:
    def __init__(self):
        """
        Initialize arguments
        Args:
        None
        Returns:
        None
        """
        self.name = "Electric Cat"
        self.hp = 250
        self.currentHealth = 250
        self.alive = True
        self.bag = ["healthPotion"] #will add more after project 3

    def doDamage(self, damageDone):
        self.currentHealth = self.currentHealth - damageDone
        if (self.currentHealth <= 0):
            self.alive = False

    def checkAlive(self):
        if(self.alive == True):
            return True
        else:
            return False

    def LightningBoltAttack(self, enemyPlayer):
        chanceToHit = random.randint(1,101)
        if (chanceToHit <= 45):
            enemyPlayer.doDamage(90)

    def ElectricScratchAttack(self, enemyPlayer):
        chanceToHit = random.randint(1,101)
        if (chanceToHit <= 90):
            enemyPlayer.doDamage(40)

    def EnergyBeamAttack(self, enemyPlayer):
        chanceToHit = random.randint(1,101)
        if (chanceToHit <= 40):
            enemyPlayer.doDamage(110)

    def BiteAttack(self, enemyPlayer):
        enemyPlayer.doDamage(20)

    def AIAttack(self, enemyPlayer):
        #randomly choose one of Electric Cat's attacks and then use it
        #returns a string of which attack was used so that user can know what AI did/if it was successful
        attackToUse = random.randint(0,5)
        tempHealth = self.currentHealth
        if (attackToUse == 1):
            LightningBoltAttack(enemyPlayer)
            if (tempHealth != self.currentHealth):
                return "LightningBolt", True
            else:
                return "LightningBolt", False
        if (attackToUse == 2):
            ElectricScratchAttack(enemyPlayer)
            if (tempHealth != self.currentHealth):
                return "ElectricScratch", True
            else:
                return "ElectricScratch", False
        if (attackToUse == 3):
            EnergyBeamAttack(enemyPlayer)
            if (tempHealth != self.currentHealth):
                return "EnergyBeam", True
            else:
                return "EnergyBeam", False
        if (attackToUse == 4):
            BiteAttack(enemyPlayer)
            if (tempHealth != self.currentHealth):
                return "Bite", True
            else:
                return "Bite", False

    def useHealthPotion():
        self.currentHealth = self.currentHealth + 30
        self.bag.remove("healthPotion")

    def bagEmpty():
        if (bag):
            return False
        else:
            return True

import random

class Pikachu:
    def __init__(self):
        """
        Initialize arguments
        Args:
        None
        Returns:
        None
        """
        self.name = "Pikachu"
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

    def ThunderBoltAttack(self, enemyPlayer):
        #attack with thunder bolt
        chanceToHit = random.randint(1,101)
        if (chanceToHit <= 45):
            enemyPlayer.doDamage(90)

    def QuickAttack(self, enemyPlayer):
        #attack with quick attack
        chanceToHit = random.randint(1,101)
        if (chanceToHit <= 90):
            enemyPlayer.doDamage(40)

    def ThunderAttack(self, enemyPlayer):
        #attack with thunder
        chanceToHit = random.randint(1,101)
        if (chanceToHit <= 40):
            enemyPlayer.doDamage(110)

    def GrowlAttack(self, enemyPlayer):
        #attack with growl
        enemyPlayer.doDamage(20)

    def AIAttack(self, enemyPlayer):
        #randomly choose one of Pikachu's attacks and then use it
        #returns a string of which attack was used so that user can know what AI did/if it was successful
        attackToUse = random.randint(0,5)
        tempHealth = self.currentHealth
        if (attackToUse == 1):
            ThunderBoltAttack(enemyPlayer)
            if (tempHealth != self.currentHealth):
                return "ThunderBolt", True
            else:
                return "ThunderBolt", False
        if (attackToUse == 2):
            QuickAttack(enemyPlayer)
            if (tempHealth != self.currentHealth):
                return "Quick", True
            else:
                return "Quick", False
        if (attackToUse == 3):
            ThunderAttack(enemyPlayer)
            if (tempHealth != self.currentHealth):
                return "Thunder", True
            else:
                return "Thunder", False
        if (attackToUse == 4):
            GrowlAttack(enemyPlayer)
            if (tempHealth != self.currentHealth):
                return "Growl", True
            else:
                return "Growl", False

    def useHealthPotion():
        self.currentHealth = self.currentHealth + 30
        self.bag.remove("healthPotion")

    def bagEmpty():
        if (bag):
            return False
        else:
            return True

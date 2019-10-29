import random

class Charizard:
    def __init__(self):
        """
        Initialize arguments
        Args:
        None
        Returns:
        None
        """
        #continue to add features
        self.name = "Charizard"
        self.hp = 300
        self.currentHealth = 300
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

    def HeatWaveAttack(self, enemyPlayer): #80 damage, 45 accuracy
        #attack with thunder bolt
        chanceToHit = random.randint(1,101)
        if (chanceToHit <= 45):
            enemyPlayer.doDamage(80)

    def DragonRageAttack(self, enemyPlayer): #35 damage, 90 accuracy
        chanceToHit = random.randint(1,101)
        if (chanceToHit <= 90):
            enemyPlayer.doDamage(35)

    def FireSpinAttack(self, enemyPlayer): #140 damage, 30 accuracy
        chanceToHit = random.randint(1,101)
        if (chanceToHit <= 30):
            enemyPlayer.doDamage(140)

    def SlashAttack(self, enemyPlayer): #20 damage, 100 accuracy
        enemyPlayer.doDamage(20)

    def AIAttack(self, enemyPlayer):
        #randomly choose one of Charizard's attacks and then use it
        #returns a string of which attack was used so that user can know what AI did/if it was successful
        attackToUse = random.randint(0,5)
        tempHealth = self.currentHealth
        if (attackToUse == 1):
            HeatWaveAttack(enemyPlayer)
            if (tempHealth != self.currentHealth):
                return "HeatWave", True
            else:
                return "HeatWave", False
        if (attackToUse == 2):
            DragonRageAttack(enemyPlayer)
            if (tempHealth != self.currentHealth):
                return "DragonRage", True
            else:
                return "DragonRage", False
        if (attackToUse == 3):
            FireSpinAttack(enemyPlayer)
            if (tempHealth != self.currentHealth):
                return "FireSpin", True
            else:
                return "FireSpin", False
        if (attackToUse == 4):
            SlashAttack(enemyPlayer)
            if (tempHealth != self.currentHealth):
                return "Slash", True
            else:
                return "Slash", False

    def useHealthPotion():
        self.currentHealth = self.currentHealth + 30
        self.bag.remove("healthPotion")

    def bagEmpty():
        if (bag):
            return False
        else:
            return True

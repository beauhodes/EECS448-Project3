from abc import ABC, abstractmethod
import random

class Progmon(ABC):
    """
    Abstract class for all progmon
    """
    def __init__(self):
        """
        Creates variables associated with progmon
        Args:
            self (object)
        Returns:
            None
        """
        self.name = ""
        self.hp = 0
        self.currentHealth = 0
        self.alive = True
        self.bag = []
        self.attackList = []

    def doDamage(self, damageDone):
        """
        Deals damage to the enemy's health; set alive to False if health goes below 1
        Args:
            self (object)
            damageDone (int) - amount of damage to do
        Returns:
            None
        """
        pass

    def checkAlive(self):
        """
        Checks if FireDragon is alive
        Args:
            self (object)
        Returns:
            (bool) - True if progmon is alive, otherwise False
        """
        pass

    def getCurrentHealth(self):
        """
        Gets the currentHealth of progmon
        Args:
            self (object)
        Returns:
            progmon's currentHealth
        """
        pass

    def getHp(self):
        """
        Gets the currentHealth of progmon
        Args:
            self (object)
        Returns:
            progmon's currentHealth
        """
        pass

    def getAttackList(self):
        """
        Gets the attackList of progmon
        Args:
            self (object)
        Returns:
            progmon's attackList
        """
        pass

    def attack1(self, enemyPlayer):
        """
        Attacks enemy Progmon
        Args:
            self (object)
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        pass

    def attack2(self, enemyPlayer):
        """
        Attacks enemy Progmon
        Args:
            self (object)
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        pass

    def attack3(self, enemyPlayer):
        """
        Attacks enemy Progmon
        Args:
            self (object)
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        pass

    def attack4(self, enemyPlayer):
        """
        Attacks enemy Progmon
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
            self (object)
            enemyPlayer (object) - enemy Progmon
        Returns:
            (string) - the attack that was used by the AI
            (bool) - True if the attack hit, otherwise False
        """
        pass

    def useHealthPotion(self):
        """
        Uses a healthPotion to heal 30 points of health
        Args:
            self (object)
        Returns:
            None
        """
        pass

    def bagEmpty(self):
        """
        Checks if the Bag is empty
        Args:
            self (object)
        Returns:
            (bool) - True if Bag is empty, otherwise False
        """
        pass







class FireDragonTester(Progmon):
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
        self.bag = ["healthPotion"]
        self.attackList = ["Roar", "Claw Swipe", "Fire Breath", "Tail Whip"]

    def doDamage(self, damageDone):
        """
        Deals damage to the enemy's health; set alive to False if health goes below 1
        Args:
            self (object) - FireDragon
            damageDone (int) - amount of damage to do
        Returns:
            None
        """
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

    def getAttackList(self):
        """
        Gets the attackList of FireDragon
        Args:
            self (object) - FireDragon
        Returns:
            FireDragon's attackList
        """
        return self.attackList

    def attack1(self, enemyPlayer): # 80 damage, 45 accuracy
        """
        Attacks enemy Progmon with Roar
        Args:
            self (object) - FireDragon
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        chanceToHit = random.randint(1, 101)
        if(chanceToHit <= 45):
            enemyPlayer.doDamage(80)
            print("Roar did 80 damage!\n")
            return True
        else:
            print("Roar missed!\n")
            return False

    def attack2(self, enemyPlayer): # 35 damage, 90 accuracy
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

    def attack3(self, enemyPlayer): # 140 damage, 30 accuracy
        """
        Attacks enemy Progmon with Fire Breath
        Args:
            self (object) - FireDragon
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        chanceToHit = random.randint(1, 101)
        if(chanceToHit <= 30):
            enemyPlayer.doDamage(140)
            print("Fire Breath did 140 damage!\n")
            return True
        else:
            print("Fire Breath missed!\n")
            return False

    def attack4(self, enemyPlayer): # 20 damage, 100 accuracy
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
            self.attack1(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "Roar", True
            else:
                return "Roar", False
        if(attackToUse == 2):
            self.attack2(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "ClawSwipe", True
            else:
                return "ClawSwipe", False
        if(attackToUse == 3):
            self.attack3(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "FireBreath", True
            else:
                return "FireBreath", False
        if(attackToUse == 4):
            self.attack4(enemyPlayer)
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







class ElectricCatTester(Progmon):
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
        self.bag = ["healthPotion"]
        self.attackList = ["Lightning Bolt", "Electric Scratch", "Energy Beam", "Bite"]

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
            self (object) - FireDragon
        Returns:
            FireDragon's currentHealth
        """
        return self.hp

    def getAttackList(self):
        """
        Gets the attackList of ElectricCat
        Args:
            self (object) - ElectricCat
        Returns:
            ElectricCat's attackList
        """
        return self.attackList

    def attack1(self, enemyPlayer): # 90 damage, 45 accuracy
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

    def attack2(self, enemyPlayer): # 40 damage, 90 accuracy
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

    def attack3(self, enemyPlayer): # 110 damage, 40 accuracy
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

    def attack4(self, enemyPlayer): # 20 damage, 100 accuracy
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
            self.attack1(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "LightningBolt", True
            else:
                return "LightningBolt", False
        if(attackToUse == 2):
            self.attack2(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "ElectricScratch", True
            else:
                return "ElectricScratch", False
        if(attackToUse == 3):
            self.attack3(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "EnergyBeam", True
            else:
                return "EnergyBeam", False
        if(attackToUse == 4):
            self.attack4(enemyPlayer)
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
            print("Health potion healed you for:", hpToAdd, "\n")
            self.bag.remove("healthPotion")

        else:
            self.currentHealth + 30
            print("Health potion healed you for: 30\n")
            self.bag.remove("healthPotion")

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







class WaterTurtleTest(Progmon):
    """
    Class for the new Water Turtle Progmon
    """

    def __init__(self):
        """
        Creates variables associated with WaterTurtle
        Args:
            self (object) - WaterTurtle
        Returns:
            None
        """
        self.name = "Water Turtle"
        self.hp = 200
        self.currentHealth = 200
        self.alive = True
        self.bag = ["healthPotion", "statBoost", "defenseBoost"]
        self.attackList = ["Aqua Jet", "Aqua Tail", "Water Pulse", "Tackle"]

    def doDamage(self, damageDone):
        """
        Deals damage to the enemy's health; set alive to False if health goes below 1
        Args:
            self (object) - WaterTurtle
            damageDone (int) - amount of damage to do
        Returns:
            None
        """
        self.currentHealth = self.currentHealth - damageDone
        if(self.currentHealth <= 0):
            self.alive = False

    def checkAlive(self):
        """
        Checks if WaterTurtle is alive
        Args:
            self (object) - WaterTurtle
        Returns:
            (bool) - True if WaterTurtle is alive, otherwise False
        """
        if(self.alive == True):
            return True
        else:
            return False

    def getCurrentHealth(self):
        """
        Gets the currentHealth of WaterTurtle
        Args:
            self (object) - WaterTurtle
        Returns:
            WaterTurtle's currentHealth
        """
        return self.currentHealth

    def getHp(self):
        """
        Gets the currentHealth of WaterTurtle
        Args:
            self (object) - FireDragon
        Returns:
            FireDragon's currentHealth
        """
        return self.hp

    def getAttackList(self):
        """
        Gets the attackList of WaterTurtle
        Args:
            self (object) - WaterTurtle
        Returns:
            WaterTurtle's attackList
        """
        return self.attackList

    def attack1(self):
        chanceToHit = random.randint(1, 101)
        if(chanceToHit <= 70):
            enemyPlayer.doDamage(45)
            print("Aqua Jet did 45 damage!\n")
            return True
        else:
            print("Aqua Jet missed!\n")
            return False

    def attack2(self):
        chanceToHit = random.randint(1, 101)
        if(chanceToHit <= 55):
            enemyPlayer.doDamage(50)
            print("Aqua Tail did 50 damage!\n")
            return True
        else:
            print("Aqua Tail missed!\n")
            return False

    def attack3(self):
        chanceToHit = random.randint(1, 101)
        if(chanceToHit <= 48):
            enemyPlayer.doDamage(70)
            print("Water Pulse did 70 damage!\n")
            return True
        else:
            print("Water Pulse missed!\n")
            return False

    def attack4(self):
        enemyPlayer.doDamage(12)
        print("Tackle did 12 damage!\n")
        return True

    def AIAttack(self, enemy):
        """
        Attacks enemy Progmon with a randomly chosen attack
        Args:
            self (object) - WaterTurtle
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
                return "AI Aqua Jet hit for 45 damage!", True
            else:
                return "AI Aqua Jet missed!\n", False
        if(attackToUse == 2):
            self.attack2(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "AI Aqua Tail hit!\n", True
            else:
                return "AI Aqua Tail missed!\n", False
        if(attackToUse == 3):
            self.attack3(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "AI Water Pulse hit!\n", True
            else:
                return "AI Water Pulse missed!\n", False
        if(attackToUse == 4):
            self.attack4(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "AI Tackle hit!\n", True
            else:
                return "AI Tackle missed!\n", False

    def useHealthPotion(self):
        """
        Uses a healthPotion to heal 30 points of health
        Args:
            self (object) - WaterTurtle
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

    def bagEmpty(self):
        """
        Checks if the Bag is empty
        Args:
            self (object) - WaterTurtle
        Returns:
            (bool) - True if Bag is empty, otherwise False
        """
        if(self.bag):
            return False
        else:
            return True

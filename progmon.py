import random
from abc import ABC, abstractmethod

class Progmon(ABC):
    """
    Abstract class for all Progmon
    """
    def __init__(self):
        """
        Creates variables associated with Progmon
        Args:
            self (object) - Progmon
        Returns:
            None
        """
        self.name = ""
        self.hp = 0
        self.currentHealth = 0
        self.alive = True
        self.bag = []
        self.attackList = []
        self.stunned = False
        self.statBoost = False
        self.defenseBoost = False

    def doDamage(self, damageDone):
        """
        Deals damage to the enemy's health; set alive to False if health goes below 1
        Args:
            self (object) - Progmon
            damageDone (int) - amount of damage to do
        Returns:
            None
        """
        pass

    def checkAlive(self):
        """
        Checks if Progmon is alive
        Args:
            self (object) - Progmon
        Returns:
            (bool) - True if Progmon is alive, otherwise False
        """
        pass

    def getAttackList(self):
        """
        Gets the attack list of Progmon
        Args:
            self (object) - Progmon
        Returns:
            Progmon's attackList
        """
        pass

    def setBag(self, newBag):
        """
        Sets the Bag of Progmon
        Args:
            self (object) - Progmon
            newBag (array) - what to fill the Bag with
        Returns:
            None
        """
        pass

    def getBag(self):
        """
        Gets the Bag of Progmon
        Args:
            self (object) - Progmon
        Returns:
            Progmon's Bag
        """
        pass

    def getCurrentHealth(self):
        """
        Gets the currentHealth of Progmon
        Args:
            self (object) - Progmon
        Returns:
            Progmon's currentHealth
        """
        pass

    def setCurrentHealth(self, newHealth):
        """
        Sets the currentHealth of Progmon
        Args:
            self (object) - Progmon
            newHealth (int) - what to set currentHealth to
        Returns:
            None
        """
        pass

    def getHP(self):
        """
        Gets the max health of Progmon
        Args:
            self (object) - Progmon
        Returns:
            Progmon's HP
        """
        pass

    def setStunStatus(self, setter):
        """
        Sets the stun status of Progmon
        Args:
            self (object) - Progmon
            setter (boolean) - what to set stunned to
        Returns:
            None
        """
        pass

    def getStunStatus(self):
        """
        Gets the stun status of Progmon
        Args:
            self (object) - Progmon
        Returns:
            (bool) - True if Progmon is stunned, otherwise False
        """
        pass

    def setDefenseBoost(self, setter):
        """
        Sets the defense boost of Progmon
        Args:
            self (object) - Progmon
            setter (boolean) - what to set defense boost to
        Returns:
            None
        """
        pass

    def getDefenseBoost(self):
        """
        Gets the defense boost of Progmon
        Args:
            self (object) - Progmon
        Returns:
            Progmon's defense boost
        """
        pass

    def setStatBoost(self, setter):
        """
        Sets the stat boost of Progmon
        Args:
            self (object) - Progmon
            setter (boolean) - what to set stat boost to
        Returns:
            None
        """
        pass

    def getStatBoost(self):
        """
        Gets the defense boost of Progmon
        Args:
            self (object) - Progmon
        Returns:
            Progmon's defense boost
        """
        pass

    def getAttackList(self):
        """
        Gets the attackList of Progmon
        Args:
            self (object) - Progmon
        Returns:
            Progmon's attackList
        """
        pass

    def attack1(self, enemyPlayer):
        """
        Attacks enemy Progmon
        Args:
            self (object) - Progmon
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        pass

    def attack2(self, enemyPlayer):
        """
        Attacks enemy Progmon
        Args:
            self (object) - Progmon
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        pass

    def attack3(self, enemyPlayer):
        """
        Attacks enemy Progmon
        Args:
            self (object) - Progmon
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        pass

    def attack4(self, enemyPlayer):
        """
        Attacks enemy Progmon
        Args:
            self (object) - Progmon
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        pass

    def AIAttack(self, enemyPlayer):
        """
        Attacks enemy Progmon with a randomly chosen attack
        Args:
            self (object) - Progmon
            enemyPlayer (object) - enemy Progmon
        Returns:
            (string) - the attack that was used by the AI
            (bool) - True if the attack hit, otherwise False
        """
        pass

    def useHealthPotion(self):
        """
        Uses a healthPotion to heal up to 30 points of health
        Args:
            self (object) - Progmon
        Returns:
            None
        """
        pass

    def useRestorePotion(self):
        """
        Uses a restorePotion that heals to max hp
        Args:
            self (object) - Progmon
        Returns:
            None
        """
        pass

    def useStatBoost(self):
        """
        Allows this Progmon to use a statBoost Potion
        Args:
            self (object) - Progmon
        Returns:
            None
        """
        pass

    def useDefenseBoost(self):
        """
        Allows this progmon to use a defense Potion
        Args:
            self (object) - Progmon
        Returns:
            None
        """
        pass

    def bagEmpty(self):
        """
        Checks if the Bag is empty
        Args:
            self (object) - Progmon
        Returns:
            (bool) - True if Bag is empty, otherwise False
        """
        pass



class ElectricCat(Progmon):
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
        self.bag = ["healthPotion", "statBoost", "defenseBoost", "restorePotion"]
        self.attackList = ["Lightning Bolt", "Electric Scratch", "Energy Beam", "Bite"]
        self.stunned = False
        self.statBoost = False
        self.defenseBoost = False

    def doDamage(self, damageDone):
        """
        Deals damage to the enemy's health; set alive to False if health goes below 1
        Args:
            self (object) - ElectricCat
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

    def getAttackList(self):
        """
        Gets the attack list of Electric Cat
        Args:
            self (object) - Electric Cat
        Returns:
            Electric Cat's attackList
        """
        return self.attackList

    def setBag(self, newBag):
        """
        Sets the bag of Electric Cat
        Args:
            self (object) - Electric Cat
            newBag (array) - what to set bag to
        Returns:
            None
        """
        self.bag = newBag

    def getBag(self):
        """
        Gets the bag list of Electric Cat
        Args:
            self (object) - Electric Cat
        Returns:
            Electric Cat's bag
        """
        return self.bag

    def getCurrentHealth(self):
        """
        Gets the currentHealth of ElectricCat
        Args:
            self (object) - ElectricCat
        Returns:
            ElectricCat's currentHealth
        """
        return self.currentHealth

    def setCurrentHealth(self, newHealth):
        """
        Sets the current health of ElectricCat
        Args:
            self (object) - ElectricCat
            newHealth (int) - what to set current health to
        Returns:
            None
        """
        self.currentHealth = newHealth

    def getHP(self):
        """
        Gets the max health of ElectricCat
        Args:
            self (object) - ElectricCat
        Returns:
            ElectricCat's max health
        """
        return self.hp

    def setStunStatus(self, setter):
        """
        Sets the stun status of ElectricCat
        Args:
            self (object) - ElectricCat
            setter (boolean) - what to set stunned to
        Returns:
            None
        """
        self.stunned = setter

    def getStunStatus(self):
        """
        Gets the stun status of ElectricCat
        Args:
            self (object) - ElectricCat
        Returns:
            ElectricCat's stunned status
        """
        return self.stunned

    def setDefenseBoost(self, setter):
        """
        Sets the defense boost of ElectricCat
        Args:
            self (object) - ElectricCat
            setter (boolean) - what to set defense boost to
        Returns:
            None
        """
        self.defenseBoost = setter

    def getDefenseBoost(self):
        """
        Gets the defense boost of ElectricCat
        Args:
            self (object) - ElectricCat
        Returns:
            ElectricCat's defense boost
        """
        return self.defenseBoost

    def setStatBoost(self, setter):
        """
        Sets the stat boost of ElectricCat
        Args:
            self (object) - ElectricCat
            setter (boolean) - what to set stat boost to
        Returns:
            None
        """
        self.statBoost = setter

    def getStatBoost(self):
        """
        Gets the defense boost of ElectricCat
        Args:
            self (object) - ElectricCat
        Returns:
            ElectricCat's defense boost
        """
        return self.statBoost

    def attack1(self, enemyPlayer): # 90 damage, 45 accuracy
        """
        Attacks enemy Progmon with Lightning Bolt
        Args:
            self (object) - ElectricCat
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True if attack hit, otherwise False
            (string) - attack message
        """
        chanceToHit = random.randint(1, 100)
        if(self.statBoost == True and chanceToHit <= 45):
            self.statBoost = False
            enemyPlayer.doDamage(100)
            enemyPlayer.setStunStatus(True)
            return True, "It did 100 damage and stunned the enemy!"
        elif(chanceToHit <= 45):
            enemyPlayer.doDamage(90)
            return True, "Lightning Bolt did 90 damage!"
        else:
            return False, "Lightning Bolt missed!"

    def attack2(self, enemyPlayer): # 40 damage, 90 accuracy
        """
        Attacks enemy Progmon with Electric Scratch
        Args:
            self (object) - ElectricCat
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True if attack hit, otherwise False
            (string) - attack message
        """
        chanceToHit = random.randint(1, 100)
        if(chanceToHit <= 90):
            enemyPlayer.doDamage(40)
            return True, "Electric Scratch did 40 damage!"
        else:
            return False, "Electric Scratch missed!"

    def attack3(self, enemyPlayer): # 110 damage, 40 accuracy
        """
        Attacks enemy Progmon with Energy Beam
        Args:
            self (object) - ElectricCat
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True if attack hit, otherwise False
            (string) - attack message
        """
        chanceToHit = random.randint(1, 100)
        if(self.statBoost == True and chanceToHit <= 40):
            self.statBoost = False
            enemyPlayer.doDamage(120)
            enemyPlayer.setStunStatus(True)
            return True, "It did 120 damage and stunned the enemy!"
        elif(chanceToHit <= 40):
            enemyPlayer.doDamage(110)
            return True, "Energy Beam did 110 damage!"
        else:
            return False, "Energy Beam missed!"

    def attack4(self, enemyPlayer): # 20 damage, 100 accuracy
        """
        Attacks enemy Progmon with Bite
        Args:
            self (object) - ElectricCat
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True
            (string) - attack message
        """
        enemyPlayer.doDamage(20)
        return True, "Bite did 20 damage!"

    def AIAttack(self, enemyPlayer):
        """
        Attacks enemy Progmon with a randomly chosen attack
        Args:
            self (object) - ElectricCat
            enemyPlayer (object) - enemy Progmon
        Returns:
            (string) - the attack that was used by the AI
            (bool) - True if attack hit, otherwise False
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
            self (object) - ElectricCat
        Returns:
            (int) - amount of health that was healed for
        """
        if(self.currentHealth+30 > self.hp):
            hpToAdd = self.hp - self.currentHealth
            self.currentHealth + hpToAdd
            print("Health Potion healing Electric Cat for:", hpToAdd, "HP")
            self.bag.remove("healthPotion")
            return hpToAdd
        else:
            self.currentHealth + 30
            print("Health Potion healing Electric Cat for: 30HP")
            self.bag.remove("healthPotion")
            return 30

    def useRestorePotion(self):
        """
        Uses a restorePotion that heals ElectricCat to max hp
        Args:
            self (object) - Electric Cat
        Returns:
            None
        """
        print("Restore Potion has healed Electric Cat to full health! All Boosts deactivated!")
        self.bag.remove("restorePotion")
        self.statBoost = False
        self.defenseBoost = False

    def useStatBoost(self):
        """
        Allows ElectricCat to use a statBoost Potion
        Args:
            self (object) - Electric Cat
        Returns:
            None
        """
        self.statBoost = True
        print("Stat Boost for Electric Cat activated! +10 damage and chance to stun on the next attack!")
        self.bag.remove("statBoost")

    def useDefenseBoost(self):
        """
        Allows Electric Cat to use a defense Potion
        Args:
            self (object) - ElectricCat
        Returns:
            None
        """
        self.defenseBoost = True
        print("Defense Boost for Electric Cat activated! Electric Cat will take 10 less damage on the next attack!")
        self.bag.remove("defenseBoost")

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



class FireDragon(Progmon):
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
        self.bag = ["healthPotion", "statBoost", "defenseBoost", "restorePotion"]
        self.attackList = ["Roar", "Claw Swipe", "Fire Breath", "Tail Whip"]
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
            self.defenseBoost = False
        else:
            self.currentHealth = self.currentHealth - damageDone

        if(self.currentHealth <= 0):
            self.currentHealth = 0
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

    def getAttackList(self):
        """
        Gets the attack list of FireDragon
        Args:
            self (object) - FireDragon
        Returns:
            FireDragon's attackList
        """
        return self.attackList

    def setBag(self, newBag):
        """
        Sets the bag of FireDragon
        Args:
            self (object) - FireDragon
            newBag (array) - what to set bag to
        Returns:
            None
        """
        self.bag = newBag

    def getBag(self):
        """
        Gets the bag list of FireDragon
        Args:
            self (object) - FireDragon
        Returns:
            FireDragon's bag
        """
        return self.bag

    def getCurrentHealth(self):
        """
        Gets the currentHealth of FireDragon
        Args:
            self (object) - FireDragon
        Returns:
            FireDragon's currentHealth
        """
        return self.currentHealth

    def setCurrentHealth(self, newHealth):
        """
        Sets the current health of FireDragon
        Args:
            self (object) - FireDragon
            newHealth (int) - what to set current health to
        Returns:
            None
        """
        self.currentHealth = newHealth

    def getHP(self):
        """
        Gets the max health of FireDragon
        Args:
            self (object) - FireDragon
        Returns:
            FireDragon's max health
        """
        return self.hp

    def setStunStatus(self, setter):
        """
        Sets the stun status of Fire Dragon
        Args:
            self (object) - FireDragon
            setter (boolean) - what to set stunned to
        Returns:
            None
        """
        self.stunned = setter

    def getStunStatus(self):
        """
        Gets the stun status of FireDragon
        Args:
            self (object) - FireDragon
        Returns:
            FireDragon's stunned status
        """
        return self.stunned

    def setDefenseBoost(self, setter):
        """
        Sets the defense boost of FireDragon
        Args:
            self (object) - FireDragon
            setter (boolean) - what to set defense boost to
        Returns:
            None
        """
        self.defenseBoost = setter

    def getDefenseBoost(self):
        """
        Gets the defense boost of FireDragon
        Args:
            self (object) - FireDragon
        Returns:
            FireDragon's defense boost
        """
        return self.defenseBoost

    def setStatBoost(self, setter):
        """
        Sets the stat boost of FireDragon
        Args:
            self (object) - FireDragon
            setter (boolean) - what to set stat boost to
        Returns:
            None
        """
        self.statBoost = setter

    def getStatBoost(self):
        """
        Gets the defense boost of FireDragon
        Args:
            self (object) - FireDragon
        Returns:
            FireDragon's defense boost
        """
        return self.statBoost

    def attack1(self, enemyPlayer): # 80 damage, 45 accuracy
        """
        Attacks enemy Progmon with Roar
        Args:
            self (object) - FireDragon
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True if attack hit, otherwise False
            (string) - attack message
        """
        chanceToHit = random.randint(1, 100)
        if(self.statBoost == True and chanceToHit <= 45):
            self.statBoost = False
            enemyPlayer.doDamage(90)
            enemyPlayer.setStunStatus(True)
            return True, "It did 90 damage and stunned the enemy!"
        elif(chanceToHit <= 45):
            enemyPlayer.doDamage(80)
            return True, "Roar did 80 damage!"
        else:
            return False, "Roar missed!"

    def attack2(self, enemyPlayer): # 35 damage, 90 accuracy
        """
        Attacks enemy Progmon with Claw Swipe
        Args:
            self (object) - FireDragon
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True if attack hit, otherwise False
            (string) - attack message
        """
        chanceToHit = random.randint(1, 100)
        if(chanceToHit <= 90):
            enemyPlayer.doDamage(35)
            return True, "Claw Swipe did 35 damage!"
        else:
            return False, "Claw Swipe missed!"

    def attack3(self, enemyPlayer): # 140 damage, 30 accuracy
        """
        Attacks enemy Progmon with Fire Breath
        Args:
            self (object) - FireDragon
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True if attack hit, otherwise False
            (string) - attack message
        """
        chanceToHit = random.randint(1, 100)
        if(self.statBoost == True and chanceToHit <= 30):
            self.statBoost = False
            enemyPlayer.doDamage(150)
            enemyPlayer.setStunStatus(True)
            return True, "It did 150 damage and stunned the enemy!"
        elif(chanceToHit <= 30):
            enemyPlayer.doDamage(140)
            return True, "Fire Breath did 140 damage!"
        else:
            return False, "Fire Breath missed!"

    def attack4(self, enemyPlayer): # 20 damage, 100 accuracy
        """
        Attacks enemy Progmon with Tail Whip
        Args:
            self (object) - FireDragon
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True
            (string) - attack message
        """
        enemyPlayer.doDamage(20)
        return True, "Tail Whip did 20 damage!"

    def AIAttack(self, enemyPlayer):
        """
        Attacks enemy Progmon with a randomly chosen attack
        Args:
            self (object) - FireDragon
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
            self (object) - FireDragon
        Returns:
            (int) - amount of health that was healed for
        """
        if(self.currentHealth+30 > self.hp):
            hpToAdd = self.hp - self.currentHealth
            self.currentHealth + hpToAdd
            print("Health Potion healing Fire Dragon for:", hpToAdd, "HP")
            self.bag.remove("healthPotion")
            return hpToAdd
        else:
            self.currentHealth + 30
            print("Health Potion healing Fire Dragon for: 30HP")
            self.bag.remove("healthPotion")
            return 30

    def useRestorePotion(self):
        """
        Uses a restorePotion that heals FireDragon to max hp
        Args:
            self (object) - FireDragon
        Returns:
            None
        """
        print("Restore Potion has healed Fire Dragon to full health! All Boosts deactivated!")
        self.bag.remove("restorePotion")
        self.statBoost = False
        self.defenseBoost = False

    def useStatBoost(self):
        """
        Allows FireDragon to use a statBoost Potion
        Args:
            self (object) - FireDragon
        Returns:
            None
        """
        self.statBoost = True
        print("Stat Boost for Fire Dragon activated! +10 damage and chance to stun on the next attack!")
        self.bag.remove("statBoost")

    def useDefenseBoost(self):
        """
        Allows Fire Dragon to use a defense Potion
        Args:
            self (object) - FireDragon
        Returns:
            None
        """
        self.defenseBoost = True
        print("Defense Boost for Fire Dragon activated! Fire Dragon will take 10 less damage on the next attack!")
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


class WaterTurtle(Progmon):
    """
    Class for Water Turtle Progmon
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
        self.bag = ["healthPotion", "statBoost", "defenseBoost", "restorePotion"]
        self.attackList = ["Aqua Jet", "Aqua Tail", "Water Pulse", "Bubble"]
        self.stunned = False
        self.statBoost = False
        self.defenseBoost = False

    def doDamage(self, damageDone):
        """
        Deals damage to the enemy's health; set alive to False if health goes below 1
        Args:
            self (object) - WaterTurtle
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

    def getAttackList(self):
        """
        Gets the attack list of Water Turtle
        Args:
            self (object) - Water Turtle
        Returns:
            Water Turtle's attackList
        """
        return self.attackList

    def setBag(self, newBag):
        """
        Sets the bag of Progmon
        Args:
            self (object)
            newBag (array) - what to set bag to
        Returns:
            None
        """
        self.bag = newBag

    def getBag(self):
        """
        Gets the bag list of WaterTurtle
        Args:
            self (object)
        Returns:
            WaterTurtle's bag
        """
        return self.bag

    def getCurrentHealth(self):
        """
        Gets the currentHealth of WaterTurtle
        Args:
            self (object) - WaterTurtle
        Returns:
            WaterTurtle's currentHealth
        """
        return self.currentHealth

    def setCurrentHealth(self, newHealth):
        """
        Sets the current health of WaterTurtle
        Args:
            self (object)
            newHealth (int) - what to set current health to
        Returns:
            None
        """
        self.currentHealth = newHealth

    def getHP(self):
        """
        Gets the max health of WaterTurtle
        Args:
            self (object) - WaterTurtle
        Returns:
            WaterTurtle's max health
        """
        return self.hp

    def setStunStatus(self, setter):
        """
        Sets the stun status of WaterTurtle
        Args:
            self (object)
            setter (boolean) - what to set stunned to
        Returns:
            None
        """
        self.stunned = setter

    def getStunStatus(self):
        """
        Gets the stun status of WaterTurtle
        Args:
            self (object)
        Returns:
            WaterTurtle's stunned status
        """
        return self.stunned

    def setDefenseBoost(self, setter):
        """
        Sets the defense boost of WaterTurtle
        Args:
            self (object)
            setter (boolean) - what to set defense boost to
        Returns:
            None
        """
        self.defenseBoost = setter

    def getDefenseBoost(self):
        """
        Gets the defense boost of WaterTurtle
        Args:
            self (object)
        Returns:
            WaterTurtle's defense boost
        """
        return self.defenseBoost

    def setStatBoost(self, setter):
        """
        Sets the stat boost of WaterTurtle
        Args:
            self (object)
            setter (boolean) - what to set stat boost to
        Returns:
            None
        """
        self.statBoost = setter

    def getStatBoost(self):
        """
        Gets the defense boost of WaterTurtle
        Args:
            self (object)
        Returns:
            WaterTurtle's defense boost
        """
        return self.statBoost

    def attack1(self, enemyPlayer):
        """
        Attacks enemy Progmon with Aqua Jet and has a chance to stun
        Args:
            self (object) - WaterTurtle
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True if attack hit, otherwise False
            (string) - attack message
        """
        chanceToHit = random.randint(1, 100)
        if(self.statBoost == True and chanceToHit <= 70):
            self.statBoost = False
            enemyPlayer.doDamage(55)
            enemyPlayer.setStunStatus(True)
            return True, "It did 55 damage and stunned the enemy!"
        if(chanceToHit <= 70):
            enemyPlayer.doDamage(45)
            return True, "Aqua Jet did 45 damage!"
        else:
            return False, "Aqua Jet missed!"

    def attack2(self, enemyPlayer):
        """
        Attacks enemy Progmon with Aqua Tail
        Args:
            self (object) - WaterTurtle
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True if attack hit, otherwise False
            (string) - attack message
        """
        chanceToHit = random.randint(1, 100)
        if(chanceToHit <= 55):
            enemyPlayer.doDamage(50)
            return True, "Aqua Tail did 50 damage!"
        else:
            return False, "Aqua Tail missed!"

    def attack3(self, enemyPlayer):
        """
        Attacks enemy Progmon with Water Pulse and has a chance to potentially stun
        Args:
            self (object) - WaterTurtle
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True if attack hit, otherwise False
            (string) - attack message
        """
        chanceToHit = random.randint(1, 100)
        if(self.statBoost == True and chanceToHit <= 48):
            self.statBoost = False
            enemyPlayer.doDamage(80)
            enemyPlayer.setStunStatus(True)
            return True, "It did 80 damage and stunned the enemy!"
        if(chanceToHit <= 48):
            enemyPlayer.doDamage(70)
            return True, "Water Pulse did 70 damage!"
        else:
            return False, "Water Pulse missed!"

    def attack4(self, enemyPlayer):
        """
        Attacks enemy Progmon with Bubble
        Args:
            self (object) - WaterTurtle
            enemyPlayer (object) - enemy Progmon
        Returns:
            (bool) - True
            (string) - attack message
        """
        enemyPlayer.doDamage(12)
        return True, "Bubble did 12 damage!"

    def AIAttack(self, enemyPlayer):
        """
        Attacks enemy Progmon with a randomly chosen attack
        Args:
            self (object) - WaterTurtle
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
        Uses a healthPotion to heal 30 points of health
        Args:
            self (object) - WaterTurtle
        Returns:
            (int) - amount of health that was healed for
        """
        if(self.currentHealth+30 > self.hp):
            hpToAdd = self.hp - self.currentHealth
            self.currentHealth + hpToAdd
            print("Health Potion healing Water Turtle for:", hpToAdd, "HP")
            self.bag.remove("healthPotion")
            return hpToAdd
        else:
            self.currentHealth + 30
            print("Health Potion healing Water Turtle for: 30HP")
            self.bag.remove("healthPotion")
            return 30

    def useRestorePotion(self):
        """
        Uses a restorePotion that heals to max hp
        Args:
            self (object) - WaterTurtle
        Returns:
            None
        """
        print("Restore Potion has healed Water Turtle to full health! All Boosts deactivated!")
        self.bag.remove("restorePotion")
        self.statBoost = False
        self.defenseBoost = False

    def useStatBoost(self):
        """
        Allows WaterTurtle to use a statBoost Potion
        Args:
            self (object) - WaterTurtle
        Returns:
            None
        """
        self.statBoost = True
        print("Stat Boost for Water Turtle activated! +10 damage and chance to stun on the next attack!")
        self.bag.remove("statBoost")

    def useDefenseBoost(self):
        """
        Allows WaterTurtle to use a defense Potion
        Args:
            self (object) - WaterTurtle
        Returns:
            None
        """
        self.defenseBoost = True
        print("Defense Boost for Water Turtle activated! Water Turtle will take 10 less damage on the next attack!")
        self.bag.remove("defenseBoost")

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

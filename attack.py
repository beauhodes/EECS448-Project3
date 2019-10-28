class Attack:
    def __init__(self):
        """
        Initialize arguments
        self.name: name of the class which contains all of the attack options for which every Pokemon can use

        """
        self.name = "Attacks"
        self.attackStyle = [fighting, fire, flying, ground, ice] #list of type of attacks styles -- each style will have its own attacks


    def fighting():
        print("Fighting attack style function")
        #under this we want different types of fighting attacks such as:

        # FOCUS BLAST
            # accuracy: 70, power: 120
            # Focus Blast is rather inaccurate, but when it hits, you get the 120 points of Close Combat and Superpower without any stat decreases,
            # and it even has a 10% chance to lower your opponent's Special Defense.
        # CLOSE COMBAT
            # accuracy: 100, power: 120
            # decreases Defense and Special Defense. Since your Attack remains steady, you can repeatedly use Close Combat without losing strength,
            # though each activation will lower your defenses, so be ready to switch out if needed.
        # COUNTER
            # accuracy: 100, power: 0
            # Counter grants decreased priority, meaning you'll be moving last that turn.
            # However, it reflects the last physical strike used against you back for twice the damage dealt, letting you hit foes for huge amounts of pain.
            # The damage is fixed, so Counter isn't better or worse against specific types.

    def fire():
        print("Fire attack style function")
        # MAGMA STORM
            # accuracy: 70, power: 120
            # The foe becomes trapped in a maelstrom of fire that rages for two to five turns
        # FIRE BLAST
            # accuracy: 85, power: 110
            # The target is attacked with an intense blast of all-consuming fire. This may also leave the target with a burn.
        # HEAT WAVE
            # accuracy: 90, power: 95
            # The user attacks by exhaling hot breath on the opposing Pokémon. This may also leave those Pokémon with a burn.

    def flying():
        print("Flying attack style functions")
        # SKY ATTACK
            # accuracy: 90, power: 140
            # A second-turn attack move where critical hits land more easily. This may also make the target flinch.
            # (first turn: your Pokemon must prepare for its next turn, second turn: your Pokemon does SKY ATTACK)
        # DRAGON ASCENT
            # accuracy: 100, power: 120
            # After soaring upward, the user attacks its target by dropping out of the sky at high speeds.
            # But it lowers its own Defense and Sp. Def stats in the process.
        # ROOST
            # accuracy: 0, power: 0
            # The user lands and rest its body. It restores the user's HP by up to half of its max HP.
    def ground():
        print("Ground attack style functions")
        # EARTHQUAKE
            # accuracy: 100, power: 100
            # The user sets off an earthquake that strikes every Pokémon around it.
        # BONE CLUB
            # accuracy: 85, power: 65
            # The user clubs the target with a bone. This may also make the target flinch.
        # BULLDOZE
            # accuracy: 100, power: 60
            # The user strikes everything around it by stomping down on the ground. This lowers the Speed stat of those hit.
    def ice():
        print("Ice attack style functions")
        # ICE BEAM
            # accuracy: 100, power: 90
            # The user hits the target with an icy-cold beam of energy. In addition, the target will be frozen solid.
        # SHEER COLD
            # accuracy: (Lvl User - Lvl Target) + 30, power: instant faint
            # The foe is attacked with a blast of absolute-zero cold. The foe instantly faints if it hits, unless it's protected from One-hit KOs
        # FREEZE SHOCK
            # accuracy: 90, power: 140
            # On the second turn, the user hits the target with electrically charged ice. This may also leave the target with paralysis.

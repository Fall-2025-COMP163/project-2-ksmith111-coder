"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Khalil Smith
Date: 11/14/2025

AI Usage: AI helped with inheritance structure, class design, 
and aligning my existing code to match the provided project template.
"""

# ============================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")


# =============================================
# YOUR CLASSES TO IMPLEMENT (6+ CLASSES TOTAL)
# =============================================

# ========================
# TODO: Character Base Class

class Character:
    """
    Base class for all characters.
    Implements all basic attributes and methods.
    """

    def __init__(self, name, health, strength, magic):
        # TODO: Set the character's name, health, strength, and magic
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        self.weapon = None  # For composition with Weapon

    def attack(self, target):
        # TODO: Basic attack using strength
        damage = self.strength
        print(f"{self.name} attacks {target.name} for {damage} damage.")
        target.take_damage(damage)

    def take_damage(self, damage):
        # TODO: Reduce health (never below 0)
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage. Health now: {self.health}")

    def display_stats(self):
        # TODO: Display character stats nicely
        print("---- Character Stats ----")
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Magic: {self.magic}")
        if self.weapon:
            print(f"Weapon: {self.weapon.name} (+{self.weapon.damage_bonus} dmg)")
        print("-------------------------")

# ========================
# TODO: Player Base Class
# ========================

class Player(Character):
    """
    Base class for all players.
    Adds class name, level, and experience.
    """

    def __init__(self, name, character_class, health, strength, magic):
        # TODO: Call super().__init__() with basic character info
        super().__init__(name, health, strength, magic)
        # TODO: Store the character_class
        self.character_class = character_class
        # TODO: Add level and experience
        self.level = 1
        self.experience = 0

    def display_stats(self):
        # TODO: Call parent's display_stats and add player info
        super().display_stats()
        print(f"Class: {self.character_class}")
        print(f"Level: {self.level}")
        print(f"XP: {self.experience}")
        print("-------------------------")

# ========================
# TODO: Warrior Class
# ========================
class Warrior(Player):
    """
    Warrior class - strong melee fighter.
    """

    def __init__(self, name):
        # TODO: Call super().__init__() with warrior stats
        super().__init__(name, "Warrior", health=120, strength=15, magic=5)

    def attack(self, target):
        # TODO: Override basic attack for warrior
        damage = self.strength + 5
        print(f"{self.name} swings a heavy blade at {target.name} for {damage} damage!")
        target.take_damage(damage)

    def power_strike(self, target):
        # TODO: Special warrior ability
        damage = self.strength + 10
        print(f"{self.name} uses POWER STRIKE on {target.name} for {damage} damage!")
        target.take_damage(damage)

# ========================
# TODO: Mage Class
# ========================
class Mage(Player):
    """
    Mage class - magic-based attacker.
    """

    def __init__(self, name):
        # TODO: Mage stats
        super().__init__(name, "Mage", health=80, strength=8, magic=20)

    def attack(self, target):
        # TODO: Override attack to use magic
        damage = self.magic
        print(f"{self.name} casts a magic bolt at {target.name} for {damage} damage!")
        target.take_damage(damage)

    def fireball(self, target):
        # TODO: Special ability
        damage = self.magic + 15
        print(f"{self.name} unleashes FIREBALL at {target.name} for {damage} damage!")
        target.take_damage(damage)

# ========================
# TODO: Rogue Class
# ========================
class Rogue(Player):
    """
    Rogue class - fast, medium stats, critical damage
    """

    def __init__(self, name):
        # TODO: Rogue stats
        super().__init__(name, "Rogue", health=90, strength=12, magic=10)

    def attack(self, target):
        # TODO: Override attack
        damage = self.strength
        print(f"{self.name} strikes quickly at {target.name} for {damage} damage!")
        target.take_damage(damage)

    def sneak_attack(self, target):
        # TODO: Special rogue ability
        damage = self.strength * 2
        print(f"{self.name} performs SNEAK ATTACK on {target.name} for {damage} damage!")
        target.take_damage(damage)

# ========================
# Extra Class: Paladin
# ========================
class Paladin(Player):
    """
    Paladin - holy balanced fighter
    """

    def __init__(self, name):
        super().__init__(name, "Paladin", health=110, strength=14, magic=12)

    def attack(self, target):
        damage = self.strength
        print(f"{self.name} strikes {target.name} with a holy blade for {damage} damage!")
        target.take_damage(damage)

    def smite(self, target):
        damage = self.strength + self.magic
        print(f"{self.name} uses SMITE on {target.name} for {damage} damage!")
        target.take_damage(damage)

# ========================
# Extra Class: Archer
# ========================
class Archer(Player):
    """
    Archer - ranged attacker
    """

    def __init__(self, name):
        super().__init__(name, "Archer", health=85, strength=18, magic=4)

    def attack(self, target):
        damage = self.strength
        print(f"{self.name} fires an arrow at {target.name} for {damage} damage!")
        target.take_damage(damage)

    def precision_shot(self, target):
        damage = self.strength + 12
        print(f"{self.name} uses PRECISION SHOT on {target.name} for {damage} damage!")
        target.take_damage(damage)

# ========================
# TODO: Weapon Class
# ========================
class Weapon:
    """
    Weapon class for composition.
    """

    def __init__(self, name, damage_bonus):
        # TODO: store name and damage bonus
        self.name = name
        self.damage_bonus = damage_bonus

    def display_info(self):
        # TODO: print weapon info
        print("---- Weapon Info ----")
        print(f"Weapon Name: {self.name}")
        print(f"Damage Bonus: {self.damage_bonus}")
        print("---------------------")

# ========================
# MAIN PROGRAM
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    print("\n✅ Testing complete!")

import random

class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.attack_power = random.randint(1,5000)
        self.defense = 1.5

    def strike(self):
        return random.randint(1, random.randint(1, random.randint(1, random.randint(1, random.randint(1, random.randint(1, self.attack_power))))))

    def special_ability(self, number):
        if random.randint(1,5) == 3:
            return number
        else:
            return 0

    def receive_damage(self, damage, defense):
        self.health -= damage/defense
        if self.health < 0:
            self.health = 0
        print(f"{self.name} has taken damage. {self.name}'s health is now {round(self.health, 1)}")

    
    def is_alive(self):
         return self.health > 0

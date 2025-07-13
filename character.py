class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
    
    def attack(self, other):
        if self.is_alive():
            print(f"{self.name} attacks {other.name} for {self.attack_power}")
            other.hp -= self.attack_power
            if other.hp < 0:
                other.hp = 0
        else:
            print(f"{self.name} cannot attack beacuse they're defeated")

    def __str__(self):
        return f"{self.name}(HP: {self.hp}, AP: {self.attack_power})"

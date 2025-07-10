from character import Character

class Enemy(Character):
    def __init__(self, name, hp=20, attack_power=5):
        super().__init__(name, hp, attack_power)

    def taunt(self):
        print(f"{self.name} growls menacingly...")

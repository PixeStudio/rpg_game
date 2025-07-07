from character import Character

class Hero(Character):
    def __init__(self,name):
        super().__init__(name, hp=50, attack_power=7)
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item} added to inventory")

    def show_inventory(self):
        print(f"{self.name}'s Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")
from character import Character

# Tworzymy dwie postacie
hero = Character("Archer", 30, 5)
enemy = Character("Goblin", 20, 3)

# Test 1 – status postaci
print(f"{hero.name} HP: {hero.hp}")
print(f"{enemy.name} HP: {enemy.hp}")
print("Is hero alive?", hero.is_alive())

# Test 2 – walka
hero.attack(enemy)
print(f"{enemy.name} HP after attack: {enemy.hp}")

enemy.attack(hero)
print(f"{hero.name} HP after attack: {hero.hp}")

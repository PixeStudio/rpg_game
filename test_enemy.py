from enemy import Enemy
from hero import Hero  # zakładam, że masz Hero do testów

# Tworzymy przeciwnika
enemy = Enemy("Goblin", hp=30, attack_power=7)
print(f"{enemy.name} has {enemy.hp} HP and {enemy.attack_power} attack power.")

# Sprawdzenie czy żyje
print(f"Is {enemy.name} alive? {enemy.is_alive()}")

# Tworzymy bohatera do testu walki
hero = Hero("Archer", hp=25, attack_power=5)

# Wróg atakuje bohatera
enemy.attack(hero)
print(f"{hero.name} has {hero.hp} HP after attack.")

# Wróg tauntuje
enemy.taunt()

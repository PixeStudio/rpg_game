from hero import Hero
from enemy import Enemy
from battle import battle

hero  = Hero("Archer", hp=40, attack_power=6)
enemy = Enemy("Goblin", hp=25, attack_power=4)

battle(hero, enemy)          # log zapisze się w battle_log.txt

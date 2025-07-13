from enemy import Enemy
from hero import Hero

def battle(hero, enemy):

    try:
        print(f"A wild {enemy.name}")
        print(f"{hero.name} engages in Battle")

        log = []

        while hero.is_alive() and enemy.is_alive():
            enemy.take_damage(hero.attack_power)
            msg = f"{hero.name} hits {enemy.name} for {hero.attack_power} damage."
            print(msg); log.append(msg)

            if not enemy.is_alive():
                msg = f"{enemy.name} is defeated"
                print(msg); log.append(msg)
                break

            hero.take_damage(enemy.attack_power)
            msg = f"{enemy.name} strickes back for {enemy.attack_power} damage."
            print(msg); log.append(msg)

            if not hero.is_alive():
                msg = f"{hero.name} has been defeated"
                print(msg); log.append(msg)

            with open("log_file.txt", "w", encoding="utf-8") as file:
                file.write("\n".join(log))
    except Exception as exc:
        print("Battle error", exc)
from hero import Hero

# Create a hero instance
hero = Hero("Darius")

# Show initial inventory (should be empty)
hero.show_inventory()

# Add some items
hero.add_item("Health Potion")
hero.add_item("Iron Sword")

# Show inventory again
hero.show_inventory()

# Test attack and health
hero.attack()
print(f"Is {hero.name} alive? {hero.is_alive()}")

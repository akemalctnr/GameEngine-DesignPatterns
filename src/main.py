class GameObject: 
    def __init__(self, name, object_type):
        self.name = name
        self.object_type = object_type
        self.health = 100 
        self.position = (0, 0)

    def update(self):
        if self.object_type == "Player":
            print(f"{self.name}(Player) is moving with keyboard input.")
        elif self.object_type == "Enemy":
            print(f"{self.name}(Enemy) is patrolly automatically")
        elif self.object_type == "Item":
            print(f"{self.name}(Item) is rotating on the ground")

    def render(self):
        if self.object_type == "Player":
            print(f"Drawing Blue Square for {self.name}")
        elif self.object_type == "Enemy":
            print(f"Drawing Red Circle for {self.name}")
        elif self.object_type == "Item":
            print(f"Drawing Golden Coin for {self.name}")

if __name__ == "__main__":
    objects = [
        GameObject("Hero", "Player"),
        GameObject("Goblin", "Enemy"),
        GameObject("HealthPotion", "Item")
    ]

    for obj in objects:
        obj.update()
        obj.render()

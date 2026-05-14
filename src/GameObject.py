from abc import ABC, abstractmethod

class GameObject(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self):
        pass

class Player(GameObject):
    def update(self):
        print(f"[Player] {self.name} is moving with WASD.")

    def render(self):
        print(f"Rendering {self.name} as a Blue Square.")

class Enemy(GameObject):
    def update(self):
        print(f"[Enemy] {self.name} is patrolling the area.")

    def render(self):
        print(f"Rendering {self.name} as a Red Circle.")

class Item(GameObject):
    def update(self):
        print(f"[Item] {self.name} is rotating.")

    def render(self):
        print(f"Rendering {self.name} as a Golden Coin.")

class GameObjectFactory:
    @staticmethod
    def create_object(object_type, name):
        target_type = object_type.lower()
        if target_type == "player":
            return Player(name)
        elif target_type == "enemy":
            return Enemy(name)
        elif target_type == "item":
            return Item(name)
        else:
            raise ValueError(f"Unknown object type: {object_type}")
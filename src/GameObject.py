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
        print(f"Rendering {self.name} (Blue Square).")

class Enemy(GameObject):
    def update(self):
        print(f"[Enemy] {self.name} is patrolling.")
    def render(self):
        print(f"Rendering {self.name} (Red Circle).")

class Item(GameObject):
    def update(self):
        print(f"[Item] {self.name} is rotating.")
    def render(self):
        print(f"Rendering {self.name} (Golden Coin).")

class GameObjectFactory:
    @staticmethod
    def create_object(object_type, name):
        target_type = object_type.lower()
        if target_type == "player": return Player(name)
        elif target_type == "enemy": return Enemy(name)
        elif target_type == "item": return Item(name)
        else: raise ValueError(f"Unknown type: {object_type}")

class LegacySoundLibrary:
    def play_wav_file(self, filename):
        print(f"🎶 [Legacy Sound] Playing: {filename}")

class SoundAdapter(GameObject):
    def __init__(self, name, sound_lib):
        super().__init__(name)
        self.sound_lib = sound_lib

    def update(self):
        self.sound_lib.play_wav_file(f"{self.name}_bg.wav")

    def render(self):
        pass

class GameObjectDecorator(GameObject):
    def __init__(self, decorated_obj):
        self._decorated_obj = decorated_obj
        super().__init__(decorated_obj.name)

    def update(self):
        self._decorated_obj.update()

    def render(self):
        self._decorated_obj.render()

class ShieldDecorator(GameObjectDecorator):
    def render(self):
        super().render()
        print(f"🛡️ [Shield Effect] Visual shield active around {self.name}!")
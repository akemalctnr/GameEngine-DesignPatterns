from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update_info(self, message): pass

class AchievementTracker(Observer):
    def update_info(self, message):
        print(f"🏆 [Achievement] Event Logged: {message}")

class MoveStrategy(ABC):
    @abstractmethod
    def move(self, name): pass

class KeyboardMove(MoveStrategy):
    def move(self, name): print(f"🎮 {name} is moving via WASD keyboard input.")

class PatrolMove(MoveStrategy):
    def move(self, name): print(f"🤖 {name} is patrolling on a pre-defined path.")

# --- CORE STRUCTURE ---
class GameObject(ABC):
    def __init__(self, name):
        self.name = name
        self._observers = []
        self.move_strategy = None

    def add_observer(self, obs): self._observers.append(obs)
    def notify(self, msg):
        for obs in self._observers: obs.update_info(msg)

    @abstractmethod
    def update(self): pass
    @abstractmethod
    def render(self): pass

class Player(GameObject):
    def update(self):
        if self.move_strategy:
            self.move_strategy.move(self.name)
        else:
            print(f"{self.name} stands still.")

    def render(self): print(f"Rendering Player: {self.name} (Blue Square).")

class ShieldDecorator(GameObject):
    def __init__(self, decorated_obj):
        super().__init__(decorated_obj.name)
        self.obj = decorated_obj
    def update(self): self.obj.update()
    def render(self):
        self.obj.render()
        print(f"🛡️  [Shield] Visual aura active around {self.name}!")

class LegacySoundSystem:
    def play_sound(self, file): print(f"🎶 [Legacy Sound] Playing: {file}")

class SoundAdapter(GameObject):
    def __init__(self, name, legacy_sys):
        super().__init__(name)
        self.legacy_sys = legacy_sys
    def update(self): self.legacy_sys.play_sound(f"{self.name}.wav")
    def render(self): pass

class GameObjectFactory:
    @staticmethod
    def create_object(object_type, name):
        t = object_type.lower()
        if t == "player": return Player(name)
        raise ValueError(f"Unknown type: {object_type}")
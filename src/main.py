from GameObject import GameObjectFactory

if __name__ == "__main__":
    factory = GameObjectFactory()
    try:
        game_objects = [
            factory.create_object("player", "Hero_Ali"),
            factory.create_object("enemy", "Goblin_Chief"),
            factory.create_object("item", "Magic_Sword")
        ]
        
        print("\n--- Game Engine Initializing ---")
        for obj in game_objects:
            obj.update()
            obj.render()
            print("-" * 30)
            
    except ValueError as e:
        print(f"Hata: {e}")
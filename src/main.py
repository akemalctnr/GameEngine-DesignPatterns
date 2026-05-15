from GameObject import GameObjectFactory, LegacySoundLibrary, SoundAdapter, ShieldDecorator

if __name__ == "__main__":
    factory = GameObjectFactory()
    
    hero = factory.create_object("player", "Arishikusu")
    
    shielded_hero = ShieldDecorator(hero)
    
    old_lib = LegacySoundLibrary()
    background_music = SoundAdapter("Epic_Theme", old_lib)

    game_objects = [shielded_hero, background_music]

    print("\n--- Phase 2: Structural Patterns Running ---")
    for obj in game_objects:
        obj.update()
        obj.render()
        print("-" * 30)
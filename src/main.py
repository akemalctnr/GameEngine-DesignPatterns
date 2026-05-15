from GameObject import (
    GameObjectFactory, KeyboardMove, PatrolMove, 
    AchievementTracker, ShieldDecorator, 
    LegacySoundSystem, SoundAdapter
)

if __name__ == "__main__":

    hero = GameObjectFactory.create_object("player", "Arishikusu")

    hero.move_strategy = KeyboardMove()
    
    achievements = AchievementTracker()
    hero.add_observer(achievements)

    shielded_hero = ShieldDecorator(hero)
    sound_engine = SoundAdapter("MainTheme", LegacySoundSystem())

    print("\n--- Phase 3: Game Engine Final Demo ---")
    
    shielded_hero.update()
    shielded_hero.notify("First Level Started!")
    
    print("\n--- Changing Strategy to Patrol Mode ---")
    hero.move_strategy = PatrolMove()
    shielded_hero.update()
    
    shielded_hero.render()
    sound_engine.update()
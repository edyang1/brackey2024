label s_a1_forest_minigame:
    
    
    "As you forge ahead, you enter a forest"




    play music "fantasy_suspense.mp3" loop fadein 1.0

label forest_minigame_success:
    "hello"

label forest_minigame_setback:
    menu:
        "Try again!":
            jump s_a1_forest_minigame

        "Call for help":
            jump s_a1_healer
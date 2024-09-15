label s_a1_forest_minigame:
    "hello"




    play music "fantasy_suspense.mp3" loop fadein 1.0

label forest_minigame_success:


label forest_minigame_setback:
    menu:
        "Try again!":
            jump s_a1_forest_minigame

        "Call for help":
            jump s_a1_healer
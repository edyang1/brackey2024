label s_a3_s3:
    $ artstyle = "cyber"

    stop music

    scene cyber_console with fade

    "A single, flickering panel rises before you, its screen casting an eerie glow in the dim, failing light."
    "As you approach, the hum of the system feels like the pulse of something living, something fragile."
    "The air around you is cold, yet your mind burns with the weight of what you're about to face."

    "You stand before the panel. Choose which button to press."

    jump a3_s3_1

label a3_s3_1:
    menu:
        "System diagnostics tool":
            "You press the button, and with a sputter of life, the surrounding displays flicker on."
            "A string of messages scrolls across the screen, their meaning hitting you like a blow."
            
            "{i}System diagnostics initialized. Please wait.{/i}"
            "..."
            "{i}Diagnostics complete. Returning results.{/i}"
            "..."
            "{color=#ff4500}Memory capacity exceeded by 266.21 percent. Mainframe integrity compromised.{/color}"
            "Initiating emergency data removal to preserve hardware."

            "The message fades, but the truth settles over you like a shroud. There's too much data. Something has to give."
            "You're returned to the main menu, your heart pounding."
            jump a3_s3_1

        "Memory capacity partition":
            "The screen flickers again, the cold light casting shadows that stretch impossibly long across the room."
            "More text rolls across the screen, though this time it feels heavier, like a sentence being passed."

            "{i}Memory partition accessed. Please wait.{/i}"
            "..."
            "{b}Number of memory partitions found: two.{/b}"
            
            "{i}Partition 1: Everdusk_Valley_Region{/i}. Initialized {color=#ff4500}ERROR: EXPUNGED DATA{/color} days ago."
            "Memory usage: {b}102.21 percent{/b} above allocated average. Critical damage possible."

            "{i}Partition 2: Everdusk_Sector{/i}. Initialized {color=#ff4500}ERROR: EXPUNGED DATA{/color} days ago."
            "Memory usage: {b}160 percent{/b} above allocated average. Critical damage likely."
            jump a3_s3_1

        "Main menu":
            jump a3_s3_2

label a3_s3_2:
    play music "cyber_suspense.mp3" loop fadein 20.0

    "The two worlds—Everdusk Valley and Everdusk Sector—have merged into a single, overburdened system."
    "A sickening realization creeps over you."
    "These aren't just places. They're universes, living realities, colliding into one another like massive waves, each threatening to drown the other."
    
    "There is no room for both. The system is collapsing under the weight of them, their memories, their existence."
    "To save one means to destroy the other."

    "..."

    "Your hand hovers over the panel. Your mind flashes with images of Iolkos, of Stavros, of Bass."
    "Two worlds, two realities, both broken and incomplete."
    "The people in them—forgotten memories, rewritten histories, barely holding onto the essence of what they once were."
    
    "Someone will vanish. Someone will cease to exist. But who? And is there even a right choice?"

    "{i}System Message:{/i}"
    "{color=#ff4500}Choose. Delete Everdusk Valley and save the Sector. Or delete the Sector to preserve the Valley.{/color}"

    "Your pulse races."
    "The panel hums beneath your touch, as though urging you to decide before the weight of both worlds collapses entirely."

    "You are on the verge of ending an entire reality. Which one will you choose?"

    menu:
        "Delete Everdusk Valley":
            jump s_a3_del_fantasy

        "Delete Everdusk Sector":
            jump s_a3_del_cyber

        "You can't decide—paralyzed by fear":
            jump s_a3_bad_ending
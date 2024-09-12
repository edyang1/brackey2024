label act1_scene1:
    # FSY Section

    scene fantasy_town with fade
    "You are a traveler from distant lands, a stranger threading foreign soil."
    "Whether it is the pull of adventure or the escape from something left behind, you’ve made the decision to seek out new horizons."

    "After days of wandering along paths both familiar and unknown, you find yourself in a remote mountain range, its craggy peaks looming against the twilight sky."
    "The dirt road beneath your feet winds through the shadowy terrain, flanked by low stone walls, their weathered edges telling stories of an age long forgotten."
    "The wind bites your skin, carrying with it the scent of pine and cold earth."

    "The air is thin, stealing your breath with every labored step."
    "Your limbs grow leaden, each motion slower than the last, and the cold seeps into your bones."
    "You know you must make a choice."

    menu:
        "Keep walking, driven by the hope of finding shelter soon.":
            "With what remains of your strength, you force yourself forward, your feet dragging through the dirt."
            "Minutes stretch into eternity before, at last, you see a thin plume of smoke curling up into the sky."
            "There, nestled beside a graveyard, stands a lone cottage."
            # jump fighter_location

        "Rest on the stone wall, taking a moment to gather your strength.":
            "You sit on the low wall, the cold stone pressing into your legs."
            "The world around you fades as you take a long swig from your waterskin, its warmth futile against the cold."
            "As your head tilts back, your eyes drift shut, and sleep takes you like a thief in the night."
            # jump golem_location

        "Collapse to the ground, cursing your misfortune, no longer able to bear the weight of exhaustion.":
            "Your legs buckle, sending you to your knees in the dirt."
            "A strangled cry escapes your lips as tears blur your vision."
            "You claw at the earth, helpless and lost."
            "Through the haze of despair, you barely register the sound of approaching footsteps."
            "A pair of woodsmen appear, their expressions soft with pity as they lift you from the ground and offer to take you to the nearby hospital."
            # jump healer_location

    # CYB Section

    scene cyberpunk_town with fade
    "The fog clung to you as you moved further into the neon-lit mist, its grainy tendrils wrapping around your skin like damp silk."
    "The road stretched out before you, framed by the skeletal remains of towering buildings, long abandoned."
    "Somewhere behind you, the wooden automaton watched from the shadows of its forgotten inn."
    "But you didn’t turn back."

    "The air grew heavier, thick with moisture and the acrid tang of chemicals."
    "A distant hum filled your ears, like the rush of a far-off river, but darker, more mechanical."
    "The noise built and built, until it drowned out the world around you."
    "Then, with a sudden jolt, your legs gave way beneath you."

    "You snap awake, your breath ragged."
    "The damp, fog-filled streets are gone."
    "Instead, you find yourself in a strange, enclosed space."
    "Cold, sterile lights pulse overhead, their glow casting sharp, unnatural shadows."
    "A glass panel flickers in front of you, covered in lines of unreadable code, though your mind pieces together fragments—numbers, addresses, names."
    "Your fingers twitch."

    menu:
        "Flee from the strange machine, desperate to escape.":
            "You fumble with the contraption’s controls, forcing open one of the side doors."
            "A rush of cool air hits your face, mingling with the faint chemical sting of the city’s fog."
            "Beyond the machine, a building looms, its name scrawled in flickering orange light: 'Cherub.'"
            # jump fighter_location

        "Select the one address you can make out, trusting your instincts to guide you.":
            "With a confidence you didn’t know you possessed, your hands move across the panel, selecting a destination among the rows of blue-lit lines."
            "The machine whirs to life, and without further input, it glides smoothly into motion."
            "You lose track of time as the machine weaves through the streets, only stopping when it reaches an alleyway smeared in shadow."
            # jump android_location

        "Panic, pressing random buttons as fear tightens around your chest.":
            "Panic floods your system, your hands trembling as they slap at the glowing buttons."
            "The machine lurches violently beneath you, its metal frame screeching as it careens forward."
            "The lights flash, a burst of sound fills your ears, and before you can react, the world goes white."
            "You crash into the darkness, the pain lost in the flood of overwhelming light."
            # jump healer_location
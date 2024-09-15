label s_a1_glitch:
    $ artstyle = "fantasy"

    scene fantasy_healer with fade
    play music "fantasy_casual.mp3" loop fadein 1.0
    play sound "a_town.mp3" loop fadein 2.0
    
    "The village of Everdusk Valley lies before you, shrouded in an ethereal mist. The cobblestone streets wind like veins through the quiet town, the buildings quaint yet heavy with the weight of time."
    "Few people walk the streets, and those who do keep their heads low, their movements hurried, as if the air itself whispers of things best left unnoticed."
    "You wander, letting your feet guide you, the subtle pull of something unknown tugging at the edges of your mind."
    "The marketplace, now silent, is lined with empty stalls and faded banners fluttering weakly in the breeze."
    "You pass by, feeling drawn toward the outskirts, where the village's stone walls fade into the darkened forest."
    "As you walk, you notice something strange—a glimmer beneath the roots of an ancient tree,"
    "just beyond the last row of cottages. It's faint, barely noticeable, but it pulses with an odd, rhythmic glow."

    menu:
        "Investigate":
            "You bend down, your fingers brushing the cool earth as you reach for the glimmering light."
            "The object pulses faintly beneath your touch, a sudden warmth spreading through your hand."
            "Before you can react, the stone begins to glow brighter,"
            "sending a shiver down your spine as the ground trembles beneath your feet."

        "Don't mess with it":
            "You take a step back, hesitant to tamper with something so strange and out of place."
            "But as you turn to leave, the glimmering light pulses again, this time stronger, as if responding to your retreat."
            "The ground trembles, and you feel a sudden pull—a magnetic force drawing you back toward the object."
            "Before you can react, the stone begins to glow brighter,"
            "sending a shiver down your spine as the ground trembles beneath your feet."

    jump a1_glitch1

label a1_glitch1:
    python:
        for i in range (50):
            renpy.music.set_pan(renpy.random.uniform(-1, 1), 0)
            renpy.pause(renpy.random.uniform(0.02, 0.1))

    "Your vision blurs as the village around you seems to warp, the trees flickering in and out of existence."

    python:
        for i in range(2):
            renpy.music.set_pause(True)
            renpy.pause(renpy.random.uniform(0.1, 0.3))  
            
            renpy.music.set_pause(False)
            renpy.pause(renpy.random.uniform(0.05, 0.2))

    "{b}MEMORY LEAK: Invalid memory reference at 0x0000FF. Core dump initiated.{/b}"

    "The ground beneath your feet shudders, and the sky seems to ripple like water, distorting the landscape."

    "Reality splinters as the village dissolves, replaced by jagged, shifting fragments of what once was."

    python:
        for i in range(10):
            renpy.music.set_pause(True)
            renpy.pause(renpy.random.uniform(0.1, 0.3))  
            
            renpy.music.set_pause(False)
            renpy.pause(renpy.random.uniform(0.05, 0.2))

    "{b}m€mø®¥ Øverfłøw{/b}"

    python:
        glitch_sounds = ["glitch1.mp3", "glitch2.mp3", "glitch3.mp3", "glitch4.mp3"]
        for i in range (1): # how many times to play any sound
            random_sound = renpy.random.choice(glitch_sounds)
            renpy.sound.play(random_sound)
            renpy.pause(renpy.random.uniform(3, 5))

    "You stumble, the world around you collapsing into a chaotic swirl of colors and shapes."

    "{b}ERROR: UNDEFINED ENTITY{/b}"

    "The trees stretch unnaturally, twisting into impossible angles as the ground beneath you splits open."

    "{b}rEboOtiNG... SYSTEM FAILURE{/b}"

    python:
        for i in range(5):
            renpy.music.set_pause(True)
            random_sound = renpy.random.choice(glitch_sounds)
            renpy.sound.play(random_sound)
            renpy.pause(renpy.random.uniform(1, 2))
            
            renpy.music.set_pause(False)

            random_sound = renpy.random.choice(glitch_sounds)
            renpy.sound.play(random_sound)
            renpy.pause(renpy.random.uniform(1, 2))
            

    "Suddenly, everything goes black."

    scene black

    "{b}MeM0Ry... FRAgMentEd...{/b}"

    "{b}eRr0rrrRrrRR: CoRruptED pAThWay{/b}"
    
    python:
        for i in range(3):
            renpy.music.set_pause(True)
            random_sound = renpy.random.choice(glitch_sounds)
            renpy.sound.play(random_sound)
            renpy.pause(renpy.random.uniform(1, 2))
            
            renpy.music.set_pause(False)

            random_sound = renpy.random.choice(glitch_sounds)
            renpy.sound.play(random_sound)
            renpy.pause(renpy.random.uniform(1, 2))
    
    "{b}Rebuilding n#n#-><-- ... //r€AL_ity....{/b}"

    "The ground stabilizes for a moment, but your surroundings flicker, caught between what was and what is."

    "{b}SHuTtInG DowN iNN->ffñteEe.... 10... 9... 8...{/b}"

    python:
        glitch_sounds = ["glitch1.mp3", "glitch2.mp3", "glitch3.mp3", "glitch4.mp3"]
        for i in range(3):
            renpy.music.set_pause(True)
            random_sound = renpy.random.choice(glitch_sounds)
            renpy.sound.play(random_sound)
            renpy.pause(renpy.random.uniform(1, 2))
            
            renpy.music.set_pause(False)

            random_sound = renpy.random.choice(glitch_sounds)
            renpy.sound.play(random_sound)
            renpy.pause(renpy.random.uniform(1, 2))

    stop music
    stop sound

    jump s_a2_knight

"""
PAUSE/PLAY GLITCH

    python:
        for i in range(2):
            renpy.music.set_pause(True)
            renpy.pause(renpy.random.uniform(0.1, 0.3))  
            
            renpy.music.set_pause(False)
            renpy.pause(renpy.random.uniform(0.05, 0.2))

SOUNDS GLITCH

    python:
        glitch_sounds = ["glitch1.mp3", "glitch2.mp3", "glitch3.mp3", "glitch4.mp3"]
        for i in range (5): # how many times to play any sound
            random_sound = renpy.random.choice(glitch_sounds)
            renpy.sound.play(random_sound)
            renpy.pause(renpy.random.uniform(3, 5))

PITCH GLITCH

    python:
        for i in range (50):
            renpy.music.set_pan(renpy.random.uniform(-1, 1), 0)
            renpy.pause(renpy.random.uniform(0.02, 0.1))
"""
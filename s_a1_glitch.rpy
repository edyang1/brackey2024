label s_a1_glitch:
    $ artstyle = "fantasy"

    scene fantasy_healer with fade
    play music "fantasy_casual.mp3" loop fadein 1.0
    
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

label a1_glitch1: #it gets crazy
    "hello world"
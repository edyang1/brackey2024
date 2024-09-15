label s_a1_f_start:
    # FSY Section
    
    $ artstyle = "fantasy"

    scene fantasy_knight with fade
    play music "fantasy_casual.mp3" loop fadein 1.0
    
    "The wind whispers through the tall grass, carrying the lingering scent of the damp forest behind you."
    "You are lulled into a sense of security by the warmth of the sun on your back."
    "The rhythmic crunch of gravel beneath your boots sets a steady beat, your mind drifting to distant lands and forgotten tales."
    "Maybe you'll spot one of those two-tailed foxes the old tomes speak of."
    "Or perhaps you'll stumble upon an apothecary in Everdusk Valley, eager to buy the plants you've gathered in the forest."
    "You estimate by the sun's position that you have about an hour of daylight left."
    "The air is thick with the scent of pine and earth, but something else stirs—a faint,"
    "unsettling presence, like the ghost of forgotten magic clinging to the breeze."
    "You pause, trying to make out the source of long shadows that stretch across the path ahead."
    "It is a cemetery, jagged tombstones casting long shadows under a fading sky, their edges softened by the last golden hues of the setting sun."
    "As you step closer, you see him: a man in armor, standing still amidst the tombstones."
    "You remember hearing that Everdusk Valley is close, just beyond this stretch of road,"
    "but this figure seems out of place amidst the quiet graves."
    "He looks almost like a statue, his broad, brawny frame etched in the dying light."
    "His face is solemn, eyes downcast, focused on something far beyond the graves at his feet."
    "The missing arm speaks of battles hard-fought, scars earned in silence."
    "His armor is scratched and worn, bearing the weight of a soldier who has seen far too much."
    "Do you approach him?"

    menu:
        "Approach the knight.":
            jump s_a1_knight
        "Leave him be.":
            jump s_a1_knight
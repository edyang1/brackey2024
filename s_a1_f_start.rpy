label s_a1_f_start:
    # FSY Section
    
    $ artstyle = "fantasy"

    play music "fantasy_casual.mp3" loop fadein 1.0
    scene fantasy_knight with fade

    "The wind whispered through the tall grass, carrying the lingering scent of the damp forest behind you."
    "You had been lulled into a sense of security by the warmth of the sun on your back."
    "The rhythmic crunch of gravel beneath your boots set a steady beat, your mind drifting to distant lands and forgotten tales."
    "Maybe you’d spot one of those two-tailed foxes the old tomes spoke of."
    "Or perhaps you’d stumble upon an apothecary eager to buy the plants you’d gathered in the forest."
    "You estimated by the sun's position that you'd have about an hour of daylight left."
    "The air was thick with the scent of pine and earth, but something else stirred—a faint, unsettling presence, like the ghost of forgotten magic clinging to the breeze."
    "You paused, trying to make out the source of long shadows that stretched across the path ahead."
    "It was a cemetery,  jagged tombstones casting long shadows under a fading sky, their edges softened by the last golden hues of the setting sun."
    "As you stepped closer, you saw him: a man in armor, standing still amidst the tombstones."
    "He looked almost like a statue, his broad, brawny frame etched in the dying light."
    "His face was solemn, eyes downcast, focused on something far beyond the graves at his feet."
    "The missing arm spoke of battles hard-fought, scars earned in silence."
    "His armor was scratched and worn, bearing the weight of a soldier who had seen far too much."
    "Do you approach him?"

    menu:
        "Approach the knight.":
            jump s_a1knight
        "Leave him be.":
            return
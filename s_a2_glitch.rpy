label s_a2_glitch:
    $ artstyle = "cyber"

    play music "cyber_casual.mp3" loop fadein 1.0
    play sound "a_safehouse.mp3" loop fadein 1.0

    scene cyber_healer with fade

    "You once again find yourself wandering the towering streets of the Everdusk Sector, dwarfed by endless buildings and artificial suns."
    "Your restless desire for exploration pushes you forward, just as it did in the mountains—alone, searching for something beyond these looming shadows."
    
    python:
        for i in range(10):
            renpy.music.set_pause(True)
            renpy.pause(renpy.random.uniform(0.1, 0.3))  
            
            renpy.music.set_pause(False)
            renpy.pause(renpy.random.uniform(0.05, 0.2))
    
    "What once felt alien now feels familiar. The flashing lights, the sharp hum of powerlines, the mechanical hum of vehicles—it all blends into the rhythm of the city, a living organism breathing beneath your feet."

    "{b}MEMORY ERROR: Stack overflow detected. Process limit exceeded{/b}"
    
    python:
        for i in range(20):
            renpy.music.set_pause(True)
            renpy.pause(renpy.random.uniform(0.1, 0.3))  
            
            renpy.music.set_pause(False)
            renpy.pause(renpy.random.uniform(0.05, 0.2))

    "The colors, the noise—they no longer assault your senses. You've learned to tolerate the overwhelming pulse of this place."
    "The Everdusk nightlife surrounds you, though the lack of a visible sky leaves you uncertain of the time. Is it even night?"

    "{b}WARNING: Memory fragmentation at address 0xF3A5{/b}"

    "A narrow alley catches your eye."


    python:
        glitch_sounds = ["glitch1.mp3", "glitch2.mp3", "glitch3.mp3", "glitch4.mp3"]
        for i in range (2): # how many times to play any sound
            random_sound = renpy.random.choice(glitch_sounds)
            renpy.sound.play(random_sound)
            renpy.pause(renpy.random.uniform(3, 5))

    "Steam rises from a nearby vent, lingering unnaturally low, swirling like a coiled serpent."
    "Your chest tightens as familiar memories surge—memories of this fog, this exact sensation. It pulls you in."

    "{b}SEGMENTATION FAULT: Invalid memory access at 0x7FFF0002{/b}"

    "You step into the mist."

    "{b}MEMORY ALLOCATION FAILURE: Unable to allocate memory block 0x0001F4{/b}"

    "A flicker catches your peripheral vision—a wall shifting unnaturally, like something glitched."
    "As the fog thickens, reality itself seems to distort. Signs dissolve into grids of grey squares, buildings blur and stretch."

    "{b}CRITICAL ERROR: Memory address out of bounds. Heap corruption detected.{/b}"

    python:
        glitch_sounds = ["glitch1.mp3", "glitch2.mp3", "glitch3.mp3", "glitch4.mp3"]
        renpy.music.set_pause(True)
        random_sound = renpy.random.choice(glitch_sounds)
        renpy.sound.play(random_sound)
        renpy.pause(renpy.random.uniform(1, 2))
        
        renpy.music.set_pause(False)

        random_sound = renpy.random.choice(glitch_sounds)
        renpy.sound.play(random_sound)
        renpy.pause(renpy.random.uniform(1, 2))

    "The city's hum fractures into chaotic screeches that pierce your skull."

    "{b}MEMORY DUMP: Segment violation at 0xA7B2F. Core dumped.{/b}"

    "Staggering out of the fog, you're struck by a biting wind. The neon lights, the towering buildings—they're gone."
    "Instead, the dry mountain air fills your lungs. Trees loom ahead, but they don't feel real, their shapes shifting in your vision."

    "{b}MEMORY LEAK: Memory block 0xA7B2F inaccessible. Clearing cache... FAILED.{/b}"

    "Beneath your feet, the ground crumbles unnervingly, each step echoing with a hollow, discordant sound."

    "You move forward, but the forest feels wrong—unnatural. The trees shift like flat, painted panels, moving out of sync with the rest of the world."

    "{b}eROrrrRRrrRR: MEMorY. aLLoc..aTION ERROooor{/b}"

    python:
        glitch_sounds = ["glitch1.mp3", "glitch2.mp3", "glitch3.mp3", "glitch4.mp3"]
        for i in range(5):
            renpy.music.set_pause(True)
            random_sound = renpy.random.choice(glitch_sounds)
            renpy.sound.play(random_sound)
            renpy.pause(renpy.random.uniform(1, 2))
            
            renpy.music.set_pause(False)

            random_sound = renpy.random.choice(glitch_sounds)
            renpy.sound.play(random_sound)
            renpy.pause(renpy.random.uniform(1, 2))

    "Panic rises as you press on, desperate to reach the familiar road, but the deeper you go, the more the world warps around you."

    "{b}MEMORY CORRUPTED: Unable tOooo resT0RE...{/b}"

    "{b}eeEEEEEeRRR0rRRR: STACK OOOvErflW!!{/b}"

    python:
        glitch_sounds = ["glitch1.mp3", "glitch2.mp3", "glitch3.mp3", "glitch4.mp3"]
        for i in range(10):
            renpy.music.set_pause(True)
            random_sound = renpy.random.choice(glitch_sounds)
            renpy.sound.play(random_sound)
            renpy.pause(renpy.random.uniform(1, 2))
            
            renpy.music.set_pause(False)

            random_sound = renpy.random.choice(glitch_sounds)
            renpy.sound.play(random_sound)
            renpy.pause(renpy.random.uniform(1, 2))

    "{b}SYStEeM SHUttttDOWN INITTTTiated: MeMmMmORYYY UNDEeFfined... 10... 9...{/b}"

    stop music
    stop sound
    jump s_a3_s1

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
label act1_scene1:
    # FSY Section
    
    $ artstyle = "fantasy"

    play music "fantasy_ambient.mp3" loop fadein 1.0
    scene fantasy_cottage with fade

    "You are a traveler from distant lands, a stranger threading foreign soil."
    "Whether it is the pull of adventure or the desire to escape something left behind, you've made the decision to seek out new horizons."

    "In this world, adventure comes not with fanfare but in quiet steps along forgotten paths."
    "The path beneath you is uneven, worn by time and the steps of many travelers long gone."
    "Ahead, the mountains rise like ancient sentinels, their jagged peaks cutting against the darkening sky, silhouetted by the fading light of day."
    "The air is thick with the scent of pine and earth, but there is something else—something faint but unsettling, like the remnants of forgotten magic lingering in the air."

    "Your feet tread this road as an outsider, feeling the weight of every step in a land that does not yet know you."
    "The cold bites at your skin, sharp and unforgiving, carried by the wind that seems to whisper in a language you cannot understand."

    "The wind carries with it not just the scent of pine and cold earth, but the faintest echo of voices—long silenced by time, yet still present in the stones beneath your feet."
    "As you press forward, the road narrows, winding its way through the shadowy terrain."
    "Low stone walls flank either side, their surfaces weathered and crumbling, overgrown with moss and lichen."
    "The stones seem to murmur in the twilight, telling stories of an age long forgotten, of battles fought and lives lost, of kingdoms that once stood tall but are now nothing more than dust in the wind."

    "Your breath fogs in the air before you, every step slower than the last."
    "The sun has nearly disappeared behind the peaks, leaving only the faintest traces of light."
    "Soon, the world will be plunged into night, and you must find shelter—or keep moving into the unknown, where the mountain’s embrace is less forgiving."

    "You know you must make a choice."

    menu:
        "Keep walking, driven by the hope of finding shelter soon.":
            "With what remains of your strength, you push forward, each step heavier than the last."
            "The path narrows as the trees close in, their branches reaching out like skeletal fingers to snag at your clothing."
            "The minutes stretch into eternity, the landscape around you shifting from shadowed forests to rolling hills of frostbitten grass."
            "Just as you think you cannot go any further, a thin plume of smoke curls into the sky ahead, like a lifeline."
            "There, nestled beside a small graveyard, stands a lone cottage."
            "The tombstones are arranged in a semi-circle, their shapes obscured by a thin layer of frost."
            "A single light flickers in the window, casting a warm glow that feels at odds with the surrounding desolation."
            "Exhausted but driven by the promise of warmth, you press onward."
            # jump fighter_location

        "Rest on the stone wall, taking a moment to gather your strength.":
            "The cold stone wall beckons, a solid presence in a world that feels increasingly uncertain."
            "You sit down, letting the chill of the rock press into your legs as you exhale a long breath."
            "The world around you feels distant, muted by the encroaching darkness."
            "You take a long swig from your waterskin, but the liquid is tepid, offering little comfort against the biting cold."
            "As your head tilts back, your eyes drift shut."
            "In the haze of sleep, the earth beneath you shifts, rumbling softly as if stirred by ancient forces."
            "The air grows heavy, thick with a presence you cannot see but can sense."
            "You awaken to find the world changed, the sky darker, the stone beneath you no longer feels cold—it feels alive."
            # jump golem_location

        "Collapse to the ground, cursing your misfortune, no longer able to bear the weight of exhaustion.":
            "Your legs buckle beneath you, sending you sprawling to the cold, unforgiving earth."
            "A strangled cry escapes your lips as your knees hit the dirt, hands clawing at the frozen ground in a futile attempt to pull yourself forward."
            "But there is no strength left in your limbs."
            "Tears blur your vision, the wind howls around you, mocking your helplessness."
            "Through the haze of despair, you barely register the sound of footsteps crunching through the frozen grass."
            "Two figures emerge from the shadows, woodsmen with hard faces and soft eyes. They lift you gently from the ground."
            "'We’ll get you to the hospice,' one of them says. 'You’ll be alright.'"
            "In the distance, you see the faint outline of a building—a small hospice tucked away on the edge of the forest."
            # jump healer_location

    # CYB Section

    $ artstyle = "cyber"

    stop music fadeout 2.0
    # play music "cyberpunk_town.mp3" fadein 1.0

    scene cyber_android with fade

    "The fog clung to you as you moved further into the neon-lit mist, its grainy tendrils wrapping around your skin like damp silk."
    "The air was thick with an acrid stench—a chemical tang of oil, burning circuitry, and decay that gnawed at your senses."
    "Faint flickers of neon signs blinked erratically in the distance, half-broken, their distorted light casting jagged shadows across the shattered streets."
    "The road stretched out before you, framed by the skeletal remains of towering buildings, their broken windows like hollow eyes watching your every move."
    "You felt the weight of the city pressing in around you, a mechanical beast, its broken heart still beating in the dark."

    "Somewhere behind you, the wooden automaton stood silent in the shadows of its forgotten inn, a relic of another world."
    "You didn’t turn back. You couldn’t."

    "The air grew heavier, thick with moisture and the dense fog that blurred the lines between the real and the unreal."
    "A distant hum filled your ears—low, mechanical, like the whisper of a giant machine slowly awakening. It was everywhere and nowhere at once, filling the air with an unsettling vibration."
    "The noise built and built, growing louder with each step until it became a suffocating presence, drowning out your thoughts."
    "Your legs faltered beneath you, the world around you spinning as the weight of exhaustion took hold."

    "Then, with a sudden jolt, everything gave way, and the world fell out from under you."

    "You snap awake, your breath ragged and shallow."
    "The fog-filled streets and neon lights are gone, vanished like a dream forgotten in the morning light."
    "Instead, you find yourself inside a sterile, enclosed space—a room too clean, too cold."
    "The air here is sharp, metallic, devoid of life. The lights overhead pulse in rhythm with your heartbeat, their harsh, white glow throwing long, jagged shadows against the chrome walls."

    "A glass panel flickers in front of you, lines of unreadable code flashing across its surface like the pulse of a dying system."
    "You stare at it, fragments of information blurring before your eyes—numbers, names, locations—all of it slipping through your grasp before you can make sense of it."
    "Your fingers twitch involuntarily, like your body is remembering something your mind can’t quite reach."

    menu:
        "Try to stand, your legs unsteady beneath you.":
            "Your body feels heavy, like the weight of the world is pressing down on your shoulders."
            "You push yourself up from the cold metallic floor, your hands slipping slightly on the smooth surface as you rise to your feet."
            "Your vision swims for a moment, the sterile lights above pulsing brighter before dimming again, steadying."
            "The flickering glass panel looms in front of you, its symbols flashing faster now, as if anticipating your movements."
            "The hum returns—a deep, mechanical growl reverberating through the floor beneath you, vibrating through your bones."
            "Somewhere, hidden in the walls, something watches."
            # jump corporate_trooper_location

        "Reach out for the glass panel, trying to make sense of the code.":
            "Your hand moves instinctively toward the glass panel, as though something within you knows what to do."
            "As your fingers brush the surface, the panel pulses with a faint warmth, the cold sterility of the room momentarily replaced by a subtle, strange heat."
            "The code on the screen begins to shift, swirling and rearranging itself into fragments of data—faces, locations, commands—flashes of a life you don’t recognize."
            "The world around you fades for a moment as memories—not your own—flood your mind, glitching in and out like static on a broken screen."
            "A sudden, heavy hum echoes from behind you, vibrating through the metal walls, growing louder, mechanical and relentless."
            "You can feel it—something watching, lurking just outside the edges of your vision."
            # jump android_location

        "Remain still, gathering your bearings in this unfamiliar place.":
            "You sit in silence, your heart racing, trying to make sense of the unfamiliar surroundings."
            "The sterile lights overhead seem to pulse in time with your thoughts, casting long, angular shadows across the room."
            "The walls, sleek and metallic, are oppressively close, reflecting distorted versions of yourself in jagged fragments of light and shadow."
            "The air smells faintly of disinfectant and burnt wiring, the stench of a world far removed from anything natural."
            "A low, distant hum fills the space—a mechanical sound, like the breath of a slumbering beast, omnipresent but impossible to locate."
            "As you scan the room, you notice something—small, almost imperceptible: the glass panel in front of you flickers, its code blinking in irregular intervals, as though the system itself is on the edge of failure."
            "You can feel it now, more acutely than before—the sensation of being watched, observed by something unseen."
            # jump medtech_location
label s_a1_c_start:
    $ artstyle = "cyber"

    stop music fadeout 2.0
    play music "cyber_casual.mp3" loop fadein 1.0

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
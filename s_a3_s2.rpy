label s_a3_s2:
    $ artstyle = "cyber"

    play music "cyber_suspense.mp3" loop fadein 1.0
    play sound "a_safehouse.mp3" loop fadein 1.0

    "You wake up in the same car as before, the one you found yourself in when this all started."
    "Your clothes have shifted once again to match those of the Everdusk Sector, the stark change only confirming your return."
    "The panic that gripped you mere moments ago slowly fades, replaced by a strange sense of calm. You're not dead. You're still here."

    "Taking a deep breath, you regain your bearings. The soft hum of the vehicle's display fills the silence."
    "You're exactly where you started—the car's enclosure, the dashboard humming softly as though nothing has changed."
    scene cyber_healer with fade

    "But you know better now."

    "Without hesitation, you summon the display, drawing on your fresh memories of Everdusk Valley and all that has transpired."

    jump a3_s2_1

label a3_s2_1:
    menu:
        "Head for the Cherub, to check on Stars.":
            scene cyber_fighter with fade
            play music "cyber_suspense.mp3" loop fadein 1.0

            "You leave the car and make your way toward the nightclub where you first met Stars."
            "Something feels off from the moment you step onto the street. It's quieter than before, the neon lights dimmer than what you remember."
            "The constant hum of the city, once deafening, is now reduced to a faint whisper, making the whole world feel less alive."

            "The strange lines and squares from Everdusk Valley haven't left your vision. Instead, they've blended into it."
            "What few citizens you pass bear the same overlays as those in the mountains—green and yellow bars, numbered squares, and abstract icons floating above them."

            "You pass through the sliding doors of the club."

            "The interior is eerily silent. Only a single patron sits at the counter, nursing a tall glass."
            "No one else is here. Dahlia, the barmaid, is absent from her usual spot. The contract brokers are missing too."
            "Even the mercenaries of the Eisenbahn collective have vanished."
            "The screens lining the walls hum with static, providing no information, just white noise."

            "You take a seat next to Hatterlode, who acknowledges your presence immediately."

            show stan neu at close_to_camera

            stan "Oh, it's you. How's it going? Found anything useful?"

            menu:
                "Yes, I spoke with Bass, but... what happened here? Where is everyone?":
                    "He raises an eyebrow, glancing around the empty club."
                    
                    show stan sup at tilt_left
                    stop music fadeout 10.0

                    stan "What do you mean? There's no one here. It's always this empty."
                    stan "This place has been abandoned for a long time."

            menu:
                "But there used to be dozens of Eisenbahn members here. I remember them. What happened to them?":
                    "Hatterlode's expression shifts from confusion to disappointment."

                    show stan sad at lean_back

                    stan "Nothing happened, pal. I have no idea what you're talking about with this Eisenbahn thing."
                    stan "But there's never been anyone here. Not since I've been around."

                    "He turns back to his drink, staring into the liquid as if searching for answers."

                    scene cyber_console with flash
                    show stan ang at look_down
                    scene cyber_fighter with flash

                    stan "I've always been alone."

                    python:
                        for i in range(5):
                            renpy.music.set_pause(True)
                            renpy.pause(renpy.random.uniform(0.1, 0.3))  
                            
                            renpy.music.set_pause(False)
                            renpy.pause(renpy.random.uniform(0.05, 0.2))

                    "No matter how much you call his name, Stephen Hatterlode no longer responds. His attention is elsewhere, locked onto his drink."

                    "You notice the now-familiar overlay forming around his body. The number 50 stands out clearly in the square, while a second panel displays three bullets aligned over a shield."

                    show stan neu at subtle_breathe

                    "The bar remains empty and silent, populated only by the dull hum of its appliances."
                    jump a3_s2_1
            
        "Go straight to Temple Quay and see if Callie is still there.":
            scene cyber_healer with fade
            play music "cyber_suspense.mp3" loop fadein 1.0

            "The vehicle glides through the city with its usual elegance and speed, but the vibrancy of the urban landscape has drained away."
            "As you move through the Sector levels, fewer and fewer people appear. In fact, there may be no one left."
            "The streets are lined with husks of buildings, skeletons of infrastructure—"
            "The lifeblood of the mega city has seeped away, leaving behind empty arteries and vessels."

            "Your transport continues along its course, following the address you input into the navigation system."
            "Suddenly, an alert pops up on the display, warning of a potential issue with the unit's pathfinding."
            
            "Confused, you inquire further through the display, which causes more screens to open in front of you—"
            "Overlays similar to the ones you've seen before, lingering like remnants from the other world."
            
            "The new screens provide detailed information about the vehicle and the actions it can take."
            "As you try to make sense of which options might be useful, you spot something unusual in the distance—"
            "a large van with white and blue colors."
            
            "Curiosity takes hold, and you drive closer to the van."
            "As you pull alongside it, you recognize the driver: an ashen-haired woman with cyber prosthetics,"
            "speeding away from the city as fast as she can."
            
            scene cyber_console with flash
            stop music fadeout 10.0
            scene cyber_healer with flash

            menu:
                "Callie, it's me! Please stop!":
                    "You shout through the vehicle's communication system, hoping she can hear you."
            
            "There's no response. Her vehicle only accelerates, pulling ahead as you struggle to keep up."
            
            python:
                for i in range(5):
                    renpy.music.set_pause(True)
                    renpy.pause(renpy.random.uniform(0.1, 0.3))  
                    
                    renpy.music.set_pause(False)
                    renpy.pause(renpy.random.uniform(0.05, 0.2))

            "Both of your transports are following the same road, and soon you realize where she's headed."
            "Callie is driving straight towards a ring of gray mist, slowly closing in on the city."
            
            menu:
                "Callie, stop! Before it's too late!":
                    "But she doesn't slow down. Determined, you reluctantly ease off the throttle,"
                    "increasing the distance between the two vehicles."
            
            "You watch as her van becomes a small colored dot against the warm, chalky horizon—"
            "And then she's gone, swallowed by the fog."
            jump a3_s2_1

        "Drive to the safehouse to meet with Bass.":
            scene cyber_android with fade
            play music "cyber_suspense.mp3" loop fadein 1.0

            "Your transport takes you through the same roads as before, following the familiar address already loaded in its system."
            "But unlike the first time, the vitality of the urban landscape is gone."
            "Intersections, bridges, once teeming with life, now feel cold and hollow."
            "The world around you feels too big—an enormous empty shell."
            "The vast concrete spaces are now like playgrounds for pets that no longer exist,"
            "and the towering levels of the Sector loom over you like abandoned coliseums."

            "The alley where Bass' safehouse is located is shrouded in pitch darkness."
            "Only a single streetlight casts a dim yellow glow, keeping the encroaching night at bay."

            "Your car slows to a stop, but the sound it makes is twisted and broken, like the flapping of a live wire on a metal plate."

            "You exit the vehicle as quickly as you can, the grating noise still echoing in your mind as you make your way to the safehouse door."

            "The marker lights are out, but the door slides open when you interact with it."

            "The corridor beyond is dimly lit, a single emergency light flickering sporadically overhead."
            "You follow the sharp turn and reach the second door, entering the safehouse."

            "Inside, the apartment is almost completely dark."
            "The only light comes from the bright blue glow of the computer screen on the desk."
            "In front of it, a small android clad in a red hoodie sits in silhouette,"
            "the flickering light casting long shadows across the room."

            show b neu at subtle_breathe

            b "Huh? Who are you?"

            stop music fadeout 10.0

            "The android's voice is flat, and its head display shows low, tired eyes."

            menu:
                "Bass, it's me. We talked about our memory issues. You even offered me some snacks, remember?":
                    "Bass tilts its head to the side, and you hear a strong whirring noise, followed by a short pause."

                    show b sup at tilt_right

            b "I'm sorry, but I don't recall any of that. I'm reading these documents to try and understand why I'm sitting here."

            "Bass' head snaps back toward you."

            show b sup at jitter

            b "You said something before, like a name? Was that my name?"

            python:
                for i in range(5):
                    renpy.music.set_pause(True)
                    renpy.pause(renpy.random.uniform(0.1, 0.3))  
                    
                    renpy.music.set_pause(False)
                    renpy.pause(renpy.random.uniform(0.05, 0.2))

            menu:
                "Yes, Bass. That's your name. You told me that.":
                    "The machine's head display flickers and refreshes a few times, the screen momentarily blank."

                    show b ang at jitter

            b "I'm sorry, but I can't tell if that's my real name or not."
            b "I don't remember. I don't remember anything."

            show b ang at subtle_breathe

            b "I—I—I—"

            "Bass' voice stutters, and the display on its face refreshes frantically."
            "Its limbs and body begin to fizzle, colors draining away as tiny grey squares spread across its form."

            scene cyber_console with flash
            show b sad at shrink_back
            scene cyber_android with flash

            "A granular mist seeps out of its joints and crevices, the same fog you've encountered before."

            "In seconds, Bass is gone, his body decomposed into a myriad of cubes, consumed by the menacing fog."

            jump a3_s1_1

        "Exit.":
            jump a3_s2_2

label a3_s2_2:
    play music "fantasy_casual_glitched.mp3" loop fadein 1.0 volume 0.5

    scene cyber_android with flash
    
    "NO."
    
    scene fantasy_cottage with flash

    python:
        for i in range (50):
            renpy.music.set_pan(renpy.random.uniform(-1, 1), 0)
            renpy.pause(renpy.random.uniform(0.02, 0.1))

    "{size=*0.9}{i}{color=#ff1493}Page fault—insufficient memory resources{/color}{/i}"
    "{size=+5}{color=#ff6347}System HALT: Stack trace corrupted—cannot continue.{/color}"
    
    scene fantasy_knight with flash

    "no no no NO no stop STOP stop STOP—"
    "StOpStoPSTOPSTOPSTOPstopSTOPSTOPStOpSTOPSTOP—"

    python:
        for i in range (50):
            renpy.music.set_pan(renpy.random.uniform(-1, 1), 0)
            renpy.pause(renpy.random.uniform(0.02, 0.1))

    scene cyber_console with flash

    "{size=*1.7}{b}{color=#ff4500}Segmentation fault. Memory access violation. Reboot required...{/color}{/b}"
    
    scene cyber_healer with flash

    "plEaSePLEASEpleASEplEASEplease—NO—NO!"

    python:
        glitch_sounds = ["glitch1.mp3", "glitch2.mp3", "glitch3.mp3", "glitch4.mp3"]
        for i in range (2): # how many times to play any sound
            random_sound = renpy.random.choice(glitch_sounds)
            renpy.sound.play(random_sound)
            renpy.pause(renpy.random.uniform(3, 5))

    "STOPSTOPSTOPstopSTOPSSTOPstpSTOPSTOPSTOP—"

    python:
        glitch_sounds = ["glitch1.mp3", "glitch2.mp3", "glitch3.mp3", "glitch4.mp3"]
        for i in range(7):
            renpy.music.set_pause(True)
            random_sound = renpy.random.choice(glitch_sounds)
            renpy.sound.play(random_sound)
            renpy.pause(renpy.random.uniform(1, 2))
            
            renpy.music.set_pause(False)

            random_sound = renpy.random.choice(glitch_sounds)
            renpy.sound.play(random_sound)
            renpy.pause(renpy.random.uniform(1, 2))

    scene fantasy_knight with flash

    "pleaSEpleaSEpLEASEpleasePLZ—"
    
    "{size=*1.5}{s}{i}Memory buffer underrun...data {color=#0000ff}loss imminent{/color}{/i}{/s}"
    
    "NO!NO!NO!NO!noNONONONOnoNONOnononoNONO—"

    scene fantasy_cottage with flash

    "STOPSTOpSToPstopSTOPstOpSTOPSTOPSTOP—"

    python:
        glitch_sounds = ["glitch1.mp3", "glitch2.mp3", "glitch3.mp3", "glitch4.mp3"]
        for i in range (3): # how many times to play any sound
            random_sound = renpy.random.choice(glitch_sounds)
            renpy.sound.play(random_sound)
            renpy.pause(renpy.random.uniform(3, 5))
    
    "{size=+6}{color=#ff4500}DISK F@ILURE{/color}"
    "{size=*1.3}Invalid memory read at address {size=*0.8}{u}{color=#4682b4}0x0000FFFF{/color}{/u}"
    
    scene fantasy_golem with flash

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

    "PLSPLSPLSPLSPLSPLS—NO NO—"

    jump s_a3_s3
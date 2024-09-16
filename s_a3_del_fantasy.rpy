label s_a3_del_fantasy:
    $ artstyle = "cyber"

    play music "cyber_casual.mp3" loop fadein 2.0
    play sound "a_safehouse.mp3" loop fadein 2.0

    scene cyber_android with fade

    "The hum of the city drags you from restless sleep. You twitch in your seat, unsettled by the relentless lights and sounds."
    "Your head knocks against the cold metal of the car, and for a moment, you're almost glad to feel the dull ache."

    "As your vision clears, you take in the overwhelming neon glow outside the canopy. Below the gleaming spires of the Arcology, the tidal wave of people moves like clockwork through the streets—alive, unaware, endlessly churning beneath the city's brilliant facade."

    "You stretch your limbs, your muscles stiff from the journey. The car's display starts to beep, and the phone in your pocket vibrates, both demanding attention."
    "Your fingers trace the edges of every item in the car's console—like you're discovering them for the first time."

    "This world is safe. But you can't rest yet. Not until you see for yourself what happened to the people you've met."
    jump a3_del_fantasy_1

default visited_stars = False
default visited_callie = False
default visited_bass = False

label a3_del_fantasy_1:
    menu:
        "Who will you visit?"
        "Visit Stars" if not visited_stars:
            $ visited_stars = True

            scene cyber_fighter with fade
            "The Cherub is alive with energy, the familiar hum of conversation and the clinking of glasses filling the air."
            "Every corner is occupied by members of the Eisenbahn, lounging at the tables, their easy confidence matched by the club's signature atmosphere."

            "You approach the counter, and there, seated with a vibrant blue drink in front of him, is a one-armed man."
            "Dahlia, the barmaid, catches your eye from behind the bar, winking as she nods toward the veteran mercenary."

            "Your gaze meets Stars'. His eyes are sharp, filled with the calculating shrewdness you've come to expect, but softened by the satisfied smile tugging at his lips."
            "He lifts his glass in a casual toast, the golden Eisenbahn pin on his chest catching the light in a brief, brilliant flash."

            "You raise your hand in return, acknowledging the gesture before turning away, stepping back into the familiar shadows of the club."
            jump a3_del_fantasy_1

        "Visit Callie" if not visited_callie:
            $ visited_callie = True

            scene cyber_healer with fade

            "The clinic bustles with activity, a crowd gathered outside while construction vehicles line the street."
            "You weave through the sea of people, a faint unease settling in as you wonder if something's gone wrong."

            "But then you spot Wollerback, her white hair catching the light as she emerges from behind the construction coverings, a wide smile spreading across her face. Relief washes over you."

            "Nearby, workers move purposefully around the site, while the chief engineer stands beside Callie, projecting a blueprint from his tablet."
            "The design shows a much larger building, one that reflects the ambitious vision you know she's always had."

            "You let a soft smile play on your lips, watching her in her element before turning back toward the road, your heart lighter than before."
            jump a3_del_fantasy_1

        "Visit Bass" if not visited_bass:
            $ visited_bass = True
            
            scene cyber_android with fade

            "The safehouse sits tucked away in its usual alley, just as hidden as you remember."
            "You reach it like always, setting the address into your navigation system."
            "But as you approach the door, something feels off—it's closed, which wasn't the case last time."

            "Confused, you knock, waiting for a response that never comes."
            "Bewildered, you head back to the vehicle, fumbling with the communication system, hoping to reach Bass."

            "As you climb into the cockpit, a rare gust of wind sweeps through the street, scattering debris and lifting papers into the air."
            "And that's when you see it—just for a moment—a lanky figure in a red hoodie, the zipper pulled up tight, backpack slung over one shoulder."
            "Its big head bobs slightly as it rounds the corner and disappears from sight."

            "A knowing smile crosses your face as you step back, retracing your path with a quiet sense of understanding."
            jump a3_del_fantasy_1

        "Leave and contemplate.":
            scene black with fade
            stop sound fadeout 2.0

            "The city hums around you, its neon lights flickering like distant stars in the growing night."

            "Each step you take echoes through the concrete jungle, bringing back memories of those you met: Bass, now drifting in his own path;"
            "Callie, still healing, expanding her work with a smile. Their lives continue, even as the world moves on around them."

            "But even as you navigate the bustling streets, the weight of what you left behind lingers—"
            "the world you couldn't save, now a distant memory."

            "The peaceful forests, the ancient hills, the magic that once filled the air—all vanished into the void."
            "Everdusk Valley, the lives, the stories—all gone, now existing only in the fragments of your mind."

            "You think of Stavros, laid to rest beneath the quiet peaks;"
            "Caharel, forever smiling, tending to his village; Iolkos, free at last, but no longer a part of this reality."

            "Their faces fade into the background, distant phantoms in a world that no longer remembers them."

            "You feel the weight of your decision, the world you now call home thriving with life,"
            "but at the cost of a reality once filled with peace, magic, and timeless history."

            "There is life here, yes. But life comes with the shadow of loss,"
            "knowing that not everything could be brought forward."

            "As the neon lights pulse above, casting their glow over the city, you keep walking,"
            "not with answers, but with the understanding that every choice leaves something behind."

            jump s_a4
label s_a3_del_cyber:
    $ artstyle = "fantasy"

    play music "fantasy_casual.mp3" loop fadein 2.0
    play sound "a_fantasy.mp3" loop fadein 2.0

    scene fantasy_knight with fade

    "The wind hits your body before the light fades entirely."
    "You stumble, collapsing onto the dark, cold earth beneath you. When your eyes open, the world rushes back into view."
    "Mighty peaks stretch toward the sky, soft hills rolling endlessly in the distance."
    "Above, a striped kestrel slices through the air with unmatched grace and speed."

    "You blink, taking a sharp breath. Your legs, your arms, your chest—they're all here. You feel whole."
    "You jolt upright, sitting up as the reality of your return hits you."

    "The icy gusts claw at your exposed skin, biting and stinging, but you welcome the chill with a quiet smile."
    "It's the most beautiful thing you've ever felt."

    "With trembling hands, you dig into the earth beneath you, clawing at the damp soil as if to reassure yourself that this world is real."
    "The scent of wet dirt fills your lungs, grounding you, centering you."

    "You stand, unsteady but determined, your eyes wide as you take in the landscape."
    "It's as if you can't get enough, like a man starved and desperate for sustenance."
    "This world is real. This world is safe."

    "But something nags at the back of your mind. You can't rest, not yet."
    "Not until you know what happened to the people you've met, to the ones who shared this journey with you."
    jump a3_del_cyber_1

label a3_del_cyber_1:
    menu:
        "Visit Stavros":
            scene fantasy_cottage with fade
            
            "The hut sits as quietly as ever, nestled among the mountains. The air is still, and there's no smoke rising from the chimney."

            "You step closer, noticing the firewood pile has been completely cleared, and the shutters are drawn tightly over the windows."
            "Circling the house, you strain your ears, but no sound escapes from within—only silence greets you."

            "Then, something catches your eye."

            scene fantasy_knight with fade

            "In the small cemetery beside the house, there's an extra tombstone now, one that wasn't there before."

            "Your heart quickens as you hurry toward the grave."

            "Two small marble statues stand vigil over the new tomb. You kneel before it, brushing your hand over the smooth stone, your fingers tracing the chiseled letters carved into its surface."

            "The inscription reads:"

            scene black with fade

            centered "{b}Stavros Attelides{/b}"
            centered "Former commander of the regional militia of Everdusk."
            centered "and leader of the Cordean Kestrel."
            centered "Hero of our country."

            scene fantasy_knight with fade

            "Your breath catches in your throat as you rest your hand against the tombstone, the weight of the moment pressing down on you."

            "With a quiet farewell, you rise, casting one last look at the grave before turning back toward the path."

            scene black with fade
            jump a3_del_cyber_1

        "Visit Caharel":
            scene fantasy_healer with fade

            "The hospice is bustling with life. A crowd has gathered outside, but something feels different—"
            "there's no panic or urgency, only a sense of celebration."

            "You weave through the gathered townspeople, searching for a glimpse of Caharel, worried that some accident might have occurred."

            "But then, you spot it—his unmistakable white mane appearing through the doorway,"
            "his arms full of a basket laden with medical supplies, a broad smile lighting up his face."

            "The people around him flock eagerly, offering small gifts, which he fumbles to accept, bowing in gratitude to each person."
            "Laughter and joy ripple through the crowd as they shower him with appreciation."

            "There's no sickness here today, no wounds to tend—just a town showing their thanks to the one who has done so much for them."

            "A soft smirk tugs at your lips as you watch him, his awkwardness only adding to the warmth of the scene."

            "Content with what you've seen, you turn your back on the lively crowd and head back toward the road,"
            "feeling a sense of quiet peace."

            scene black with fade
            jump a3_del_cyber_1

        "Visit Iolkos":
            scene fantasy_golem with fade

            "The inn remains tucked away in the forest, as it always has been,"
            "hidden along the familiar wooded path that leads you there."

            "When the inn comes into view, you spot an old man with short white hair"
            "and a neatly trimmed mustache standing by the entrance, his long robe swaying gently in the breeze."

            "As you watch, the door creaks open and the small figure of Iolkos comes bounding out,"
            "his short frame rushing toward the old man."

            "The two embrace warmly, and a gust of wind carries the scent of a hearty meal—"
            "cabbage soup mixed with the rich aroma of milk and cheese—straight to you."

            "You pause, observing as the old man affectionately pats the golem on the head,"
            "and you notice something—no more threads tethering Iolkos."

            "Together, they head back into the inn, shutting the door behind them,"
            "the warmth of their reunion leaving a quiet smile on your face."

            "You turn and begin retracing your steps, your smirk lingering as you disappear back into the forest."

            scene black with fade
            jump a3_del_cyber_1

        "Exit":
            scene black with fade
            stop sound fadeout 2.0

            "The wind brushes past you as you stand at the edge of the world, looking out over the mountains and forests you've wandered through."

            "Each step brought you back to those you met: Stavros, now at rest;"
            "Caharel, still healing with a smile; Iolkos, finally free. Their lives continue in quiet ways."

            "But even as you walk through this land, you can't shake the heavy weight of absence—the world you couldn't save."

            "The echoes of neon-lit streets, the pulse of a city that once thrived, now forever out of reach."
            "Everdusk Sector, the people, the lives, all faded into the void."

            "The faces of those you left behind drift into your thoughts: Bass, lost in the fog;"
            "Callie, driving away into the unknown. A world erased in an instant, its stories now mere fragments in your memory."

            "You feel the weight of both worlds—the one you saved, and the one that slipped away,"
            "taking with it all its colors, its sounds, its lives."

            "There is peace here, yes. But peace comes with the price of loss,"
            "of knowing that not everything could be carried forward."

            "The sky fades into twilight, casting a soft glow over the land. The path ahead is uncertain, but you move forward,"
            "not with answers, but with the knowledge that every choice has a cost."

            jump s_a4
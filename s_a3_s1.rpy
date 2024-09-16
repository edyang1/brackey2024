label s_a3_s1:
    $ artstyle = "fantasy"

    $ renpy.music.set_pan(0, 0)

    play music "fantasy_suspense.mp3" loop fadein 1.0
    play sound "a_town.mp3" loop fadein 1.0

    scene fantasy_knight with fade
    jump a3_s1_1

default investigated_stavros = False
default investigated_caharel = False
default investigated_iolkos = False

label a3_s1_1:
    menu:
        "Who will you check on?"
        "Head for Stavros' house near the cemetery to check on him." if not investigated_stavros:
            $ investigated_stavros = True

            scene fantasy_cottage with fade
            play music "fantasy_suspense.mp3" loop fadein 1.0

            "With uncertainty weighing on your heart, you try to recall the path to the former knight's hut."
            "Your footsteps no longer emit that awful, screeching sound, but the unease persists."
            "You tread carefully on the damp soil, nearly losing your footing several times as you grip the stone wall beside the road."
            "Upon closer inspection, you realize the familiar square stones have been replaced by clusters of triangles, glinting and shifting as they catch the light at different angles."
            
            "Alarmed, you quicken your pace."
            "The hills blur past as you hurry along the path, scanning the landscape for more of the strange anomalies you've encountered, yet dreading each one you might find."
            
            "As you huff and puff, nearly running, two colored lines—a green and a yellow one—appear at the edge of your vision."
            "You glance upward, expecting to see something in the sky, but the lines follow your gaze, moving wherever your eyes go."
            "You blink, shake your head, even close and reopen your eyes, but the lines remain, always hovering in place."
            "The yellow line is shorter than the green."

            "Uneasy, you press on, making your way toward Stavros' house."
            "Just before arriving, you stop to catch your breath, noticing the yellow bar has grown even shorter while the green one remains unchanged."
            "Now, a square has appeared between the lines, its center filled with the same gray squares you saw when you entered the fog in the Everdusk Sector."

            "Finally, you reach Stavros' house. You knock on the door."

            stav "Who is it?"

            show stav neu at subtle_breathe

            "A husk-like male voice responds from within. The door cracks open, revealing the brawny frame of a one-armed man."

            stav "Oh, it's you. Come on in."

            show stav hap at nod

            "He gestures for you to enter."

            show stav neu at step_forward

            "The house is exactly as you remember—same furniture, same items, all in their place."
            "Stavros settles by the fire, motioning for you to do the same."

            stav "Back so soon? Did you manage to speak with the old man at the inn?"

            stop music fadeout 10.0

            menu:
                "What old man? Didn't you say it was a young man?":
                    show stav sup at tilt_left
                    "The knight's face twists into a puzzled expression."

            stav "What do you mean? I've never met a young lad in that place. There was an old man who used to live there before… Before…"

            scene cyber_console with flash
            show stav neu at lean_back
            scene fantasy_cottage with flash

            "He trails off, his bewilderment deepening."

            stav "My memory... it's playing tricks on me. I can't seem to recall the last time I went there."
            stav "Maybe it was back when I was still a farmer."

            show stav sup at subtle_breathe
            "Your mind races. He never said he used to be a farmer."

            menu:
                "Maybe it was when you were commander of the Kestrels, fifteen years ago.":
                    stav "Kestrels? Those are the birds of prey that live in this region. I never commanded anything in my life."

            "A cold shock rushes through you as you hear Stavros' words."
            "Your vision trembles, and your eyes blink uncontrollably. Stavros' body is outlined by a faint blue glow."
            
            python:
                for count in range(5):
                    renpy.music.set_pause(True)
                    renpy.pause(renpy.random.uniform(0.1, 0.3))  
                    
                    renpy.music.set_pause(False)
                    renpy.pause(renpy.random.uniform(0.05, 0.2))
            
            "A small panel with colored lines and a square appears above him. The number '50' is displayed next to the green and yellow bars."
            "For a brief moment, you spot the shape of a shield crossed by a blade before the image jitters and vanishes, leaving the box empty."

            "You glance toward the cemetery. It's gone."
            "Not a single tombstone remains standing—each one replaced by a flat, gray sheet of matte, opaque metal."
            jump a3_s1_1

        "Go and check Caharel's hospice, further down the road." if not investigated_caharel:
            $ investigated_caharel = True

            scene fantasy_healer with fade
            play music "fantasy_suspense.mp3" loop fadein 1.0

            "Your soles dig into the soft ground, almost slipping as you steady yourself on the stone wall running beside the road."
            "But as you get closer, you notice something off—the familiar square stones have been replaced by rough, uneven cubes."
            "They glitter strangely, their angles shifting as you pass, catching the light at odd moments."

            "Disturbed by the sight, you quicken your pace, racing past the fields that cling to the slopes."
            "Your movements feel urgent, desperate, as though you're competing in a race whose rules you don't even understand."

            "With your blood pounding in your ears, you suddenly notice a series of light grey rectangles at the edge of your vision."
            "You look up, expecting them to vanish, but they don't. Instead, they follow your gaze no matter where you look."
            "You blink, shake your head, even close your eyes, but the rectangles remain, beeping softly."
            "At times, they squirm and twitch more noticeably when you focus on them, making the sight all the more unsettling."

            stop music fadeout 10.0

            "Disturbed and increasingly disoriented, you push forward, determined to reach the hospice."
            "You mentally retrace your steps, searching for the stone building in the distance, but it never appears."
            "You keep walking, each step heavier than the last, your energy draining, but still, the hospice remains out of sight."

            scene cyber_console with flash
            "Baffled, you push yourself to run for another ten minutes, desperation creeping into your movements."
            scene fantasy_healer with flash

            "Suddenly, you realize something is wrong."
            
            "You look down at your feet, watching as the world around you shifts. It moves with you for a moment, then abruptly jerks itself back, as though resetting."
            "You watch this happen over and over, each step forward resetting the space around you."
            "Exhausted, you finally stop, your breath ragged as the truth sinks in."

            "Whatever lies beyond the bend in the road is simply out of reach—an illusion,"

            python:
                for count in range(5):
                    renpy.music.set_pause(True)
                    renpy.pause(renpy.random.uniform(0.1, 0.3))  
                    
                    renpy.music.set_pause(False)
                    renpy.pause(renpy.random.uniform(0.05, 0.2))

            "a space that doesn't exist in the reality you're trapped in."
            "Each step toward it displaces you back to where you started, and as you walk,"
            "the ground stretches and warps, triangles bending into impossible shapes before snapping back into place."
            "The hospice is gone. It was never there."
            jump a3_s1_1

        "Reach Iolkos' inn and see if everything's in order." if not investigated_iolkos:
            $ investigated_iolkos = True

            scene fantasy_golem with fade
            play music "fantasy_suspense.mp3" loop fadein 1.0

            "With uncertainty weighing heavily in your heart, you try to recall the way to the golem's abandoned inn."
            "You tread carefully on the frozen earth, almost losing your footing on the slick ground."
            "As you steady yourself against the stone wall running parallel to the road, you notice something strange."
            "What should have been square stones are now jagged clusters of triangles, shifting and glittering as the light hits them at odd angles."

            "Caught by confusion, you hasten your steps."
            "The trees blur past as you quicken your pace, scanning the landscape for more strange anomalies, dreading each one you might find."

            "Your heart races. In the corner of your vision, you notice two colored lines—green and yellow—alongside a small square filled with blocky scribbles."
            "You look up, expecting them to disappear, but they follow your every gaze, locked in place no matter where you look."
            "You blink, shake your head, but the lines and square remain, etched into your vision."

            "Unsettled, you push forward, heading for Iolkos' inn."
            "You stop to catch your breath as you near the entrance, noticing the yellow bar has shrunk considerably, while the green remains unchanged."
            "A larger square has now appeared, filled with the same gray blocks you saw when you first encountered the fog in the Sector."

            stop music fadeout 10.0

            "The inn's door is swung wide open. No light spills from within, no scent of food greets you."
            "The silence is heavy, unsettling."

            "As you step closer, something stirs within the darkness—small, almost childlike, skittering along the edge of the doorframe."
            "A thin figure emerges, clutching the wooden beams of the entrance. Its bright, pearl-like eyes and crafted metallic body glint faintly in the dim light."

            show i neu at subtle_breathe

            python:
                for count in range(5):
                    renpy.music.set_pause(True)
                    renpy.pause(renpy.random.uniform(0.1, 0.3))  
                    
                    renpy.music.set_pause(False)
                    renpy.pause(renpy.random.uniform(0.05, 0.2))

            i "Who are you? What are you doing here?"

            "The golem's voice trembles with fear, its frame barely visible as it peers out from behind the wall."

            menu:
                "Iolkos, it's me. We talked before, remember? You even had me taste your soup.":
                    "You inch closer, your voice gentle, but with every step, the golem retreats further into the shadows."

            show i sup at lean_back

            i "I don't remember you! I don't know who you are!"

            scene cyber_console with flash
            show i ang at jitter
            scene fantasy_golem with flash

            "Iolkos cries out, his voice rising in fear."

            i "I'm always alone! No one ever comes here! You're lying!"

            "The golem's pearl eyes twist into oblique lines, glowing with anger."

            show i ang at tilt_right

            i "You're bad! You're a liar! No one has ever been in here with me!"
            i "People only come by to break things and steal from the outside!"

            show i ang at step_back

            "The automaton scuttles toward the door, its small frame moving with frantic energy as it slams the door shut."

            show i ang at subtle_breathe

            i "Don't come any closer! I want to be alone!"

            "Iolkos yells one final time before slamming the door, locking himself inside the decaying inn."

            show i neu at look_down

            "You're left standing alone beneath the trees. Before the door shut, you noticed something odd—"
            "A purple outline surrounded Iolkos' small frame, with two colored bars hovering above him and two squares."
            "One read '50,' while the other bore the symbol of a cog and flame, flickering briefly before disappearing into the shadows."

            "Alone beneath the dark canopy of trees, questions swirl in your mind, but the answers remain just out of reach."
            jump a3_s1_1

        "Move on.":
            "This world makes little sense to you now. It is not the same world you left behind when you crossed over."
            "The reality you've returned to feels more alien, more fractured than the one you stumbled into by mistake."
            "Iolkos and Stavros seem to have lost or had their memories wiped. Caharel, on the other hand, feels like a figment—"
            "a being who never existed, his hospice sealed off, erased from this very region."

            "You turn, your breath heavy, mind clouded with confusion and dread."
            "On the horizon, distant mountain peaks slowly dissolve, melting into the skyline like wax under heat."
            "You try to move, but you notice it—a shimmering, grainy fog creeping over the land."
            "It washes over the slopes, swallowing up hills, homes, and roads. Everything vanishes under its relentless tide."

            "Houses, trees, animals—all dismantled, erased by the squirming fog you know all too well."
            
            "{size=*0.8}{b}!!W@RN¡NG!!:{/b} Recursive loop detected in m€møry ₲{size=*1.4}{color=#00ff00}43FZ{/color}..."
            
            "Instinctively, you want to run, but there is nowhere to run to."
            "You take a few desperate steps, but the fog overtakes you, clinging to your body like damp sand."
            "Your arms and legs flail, trying to fight it off, but there is no escaping it. The fog smothers you, tightening its grip."
           
            "{size=+4}{color=#ff0000}ERR0RRRRRrrrrr{size=+7}rRrrrRrrRrrRrr{/size}{/color}"
            
            "You twitch violently, gasping for air. Your head slams against cold metal."
            
            "{size=*0.6}Memory leak in thread {size=*1.3}{color=#8b0000}#5432... attempting to resolve{/color}{/size}"
            
            scene black with flash

            stop music
            stop sound

            jump s_a3_s2
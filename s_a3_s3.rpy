label s_a3_s3:
    $ artstyle = "cyber"

    stop music

    scene cyber_console with fade

    "A single, flickering panel rises before you, its screen casting an eerie glow in the dim, failing light."
    "As you approach, the hum of the system feels like the pulse of something living, something fragile."
    "The air around you is cold, yet your mind burns with the weight of what you're about to face."

    "You stand before the panel. Choose which button to press."

    jump a3_s3_1

label a3_s3_1:
    menu:
        "System diagnostics tool":
            "You press the button, and with a sputter of life, the surrounding displays flicker on."
            "A string of messages scrolls across the screen, their meaning hitting you like a blow."
            
            "{i}System diagnostics initialized. Please wait.{/i}"
            "..."
            "{i}Diagnostics complete. Returning results.{/i}"
            "..."
            "{color=#ff4500}Memory capacity exceeded by 266.21 percent. Mainframe integrity compromised.{/color}"
            "Initiating emergency data removal to preserve hardware."

            "The message fades, but the truth settles over you like a shroud. There's too much data. Something has to give."
            "You're returned to the main menu, your heart pounding."
            jump a3_s3_1

        "Memory capacity partition":
            "The screen flickers again, the cold light casting shadows that stretch impossibly long across the room."
            "More text rolls across the screen, though this time it feels heavier, like a sentence being passed."

            "{i}Memory partition accessed. Please wait.{/i}"
            "..."
            "{b}Number of memory partitions found: two.{/b}"
            
            "{i}Partition 1: Everdusk_Valley_Region{/i}. Initialized {color=#ff4500}ERROR: EXPUNGED DATA{/color} days ago."
            "Memory usage: {b}102.21 percent{/b} above allocated average. Critical damage possible."

            "{i}Partition 2: Everdusk_Sector{/i}. Initialized {color=#ff4500}ERROR: EXPUNGED DATA{/color} days ago."
            "Memory usage: {b}160 percent{/b} above allocated average. Critical damage likely."
            jump a3_s3_1

        "Main menu":
            jump a3_s3_2

label a3_s3_2:
    play music "cyber_suspense.mp3" loop fadein 20.0

    "The two worlds—Everdusk Valley and Everdusk Sector—have merged into a single, overburdened system."
    "A sickening realization creeps over you."
    "These aren't just places. They're universes, living realities, colliding into one another like massive waves, each threatening to drown the other."
    
    "There is no room for both. The system is collapsing under the weight of them, their memories, their existence."
    "To save one means to destroy the other."

    "..."

    "Your hand hovers over the panel. Your mind flashes with images of Iolkos, of Stavros, of Bass."
    "Two worlds, two realities, both broken and incomplete."
    "The people in them—forgotten memories, rewritten histories, barely holding onto the essence of what they once were."
    
    "Someone will vanish. Someone will cease to exist. But who? And is there even a right choice?"

    "{i}System Message:{/i}"
    "{color=#ff4500}Choose. Delete Everdusk Valley and save the Sector. Or delete the Sector to preserve the Valley.{/color}"

    "Your pulse races."
    "The panel hums beneath your touch, as though urging you to decide before the weight of both worlds collapses entirely."

    "You are on the verge of ending an entire reality. Which one will you choose?"

    menu:
        "Delete Everdusk Valley":
            stop music fadeout 5.0
            "Your finger presses down on the button, sealing the fate of Everdusk Valley."
            
            "A cold, hollow feeling spreads through your chest. It's done."
            "The Valley, with its rustic charm, its people, its histories—all of it will be gone. Forever."
            
            "The screen flickers, then displays the final message with brutal simplicity."

            "{color=#ff4500}Partition Everdusk_Valley_Region has been deleted.{/color}"

            "There's a sudden stillness in the control room. The air feels heavy, like a weight pressing down on your chest."
            "The soft hum of the machines continues, indifferent to the destruction you've just witnessed."

            play music "ambient_somber.mp3" fadein 5.0

            "You stare at the panel, but the reality of what you've done feels distant, unreal."
            "The world that once existed just moments ago—its mountains, forests, the faces of Iolkos, Stavros—it's all gone now, wiped from existence as though it never was."
            "Not even a memory remains."

            menu:
                "I—I didn't even say goodbye...":
                    "The thought punches you in the gut, doubling the weight on your heart."
                    "You didn't get to tell them."
                    "You never warned them."
            
            "Did they know? Did they feel it when it happened?"
            "The faces of Iolkos and Stavros flash before your mind's eye—one last time."
            "Their voices, their lives, all erased in a moment, replaced by the cold emptiness of this control room."
            
            "But something remains in your chest—an unbearable, sinking grief."

            "{color=#ff4500}System Status: Memory restored. Partition successfully deleted.{/color}"

            "You want to scream. You want to undo everything."
            "The control room feels like a tomb—silent, hollow, lifeless."
            "The screens flicker, but all you hear is the pounding of your own heart, thundering in your ears."

            "Somewhere in the back of your mind, a tiny, cruel voice whispers."
            "Was it worth it?"

            "{color=#ff4500}Partition: Everdusk Sector. Memory capacity at 85%.{/color}"
            
            "The world you chose to save... lives on. The city, with its cold neon lights and crumbling streets, persists. But the cost—"

            menu:
                "Was this the right choice?":
                    "The machines in the control room buzz on, utterly indifferent to the moral weight of what's been done."
            
            "You stand there, hands trembling, feeling the void left in the wake of Everdusk Valley's erasure. That world... those people... it all depended on you."
            
            "And now, it's gone."

            # Pause for emotional impact
            scene black with fade
            "{i}{size=40}...{/size}{/i}"

            "You sit back in the chair, staring at the lifeless screen."
            "You can feel it—a hole where Everdusk Valley used to be."
            "The system hums, oblivious to the universe you've just erased."
            "The blue screen flickers, but now, it's just noise. It feels like you're surrounded by ghosts."
            
            "And all you can hear is the finality of what you've done."

            "Gone. Forever."
            jump s_a3_del_fantasy

        "Delete Everdusk Sector":
            stop music fadeout 2.0

            "Your hand trembles as you press down on the button, sealing the fate of Everdusk Sector."
    
            "A cold shiver runs through your body as the weight of the decision bears down on you. It's done."
            "The sprawling neon streets, the towering megastructures, Bass, Callie, the life of the city—all of it will be gone. Wiped from existence in an instant."

            "The screen flickers, showing the final message in harsh, clinical text."

            "{color=#ff4500}Partition Everdusk_Sector has been deleted.{/color}"

            "The control room falls silent. You feel the emptiness press down on you, the once vibrant hum of technology now a cold, indifferent void."
            "The city, with all its life, its struggles, its pulse—it's all gone now. Like it never existed."

            "You stare at the screen, but the reality of your action feels distant, like you're trapped in a dream you can't wake from."
            "The Sector is gone. No more neon lights. No more steel towers scraping the sky. No more whispers in the dim alleys."
            "Bass... Callie... even Stars—they're gone too."

            menu:
                "I didn't even get to... say goodbye.":
                    "The realization hits you harder than anything. You never warned them. They never saw it coming."
            
            "Did Bass even understand? Did Callie feel it when the world started to crumble? Or did they simply... vanish?"

            "{color=#ff4500}System Status: Partition successfully deleted. Memory restored.{/color}"

            "The words feel like a punch to the gut, too sterile for the enormity of what you've just done."
            "You think of Bass, sitting in his hideout, trying to remember who he was. Callie, speeding away in her van, unaware of the doom about to fall on her. Stars, alone at the bar, still waiting for you to return."
            "But they're gone now. Not even their memories remain."

            "Your hand tightens into a fist. The control room's quiet hum seems to mock you, indifferent to the loss of an entire world."

            menu: 
                "Was this the right choice?":
                    "The screens flicker again, but now it's just empty static. The city is gone—its people, its stories, all erased in a moment. And yet... the system hums on, as if nothing has changed."

            "{color=#ff4500}Partition: Everdusk_Valley_Region. Memory capacity at 85%.{/color}"
            
            "The valley, with its forests and villages, is still there. The mountains and ancient paths, preserved. But the world you chose to destroy... it's gone. Erased like a fleeting thought."

            menu:
                "Why does it feel so empty?":
                    "The machines around you hum softly, but they don't care. They never cared. The world you've just erased is nothing but code, bits of data deleted from the system. But for you, it was more than that."
            
            "Bass, with his confusion and search for identity. Callie, running from a world that never understood her. Stars, grizzled and alone, but holding onto hope in his own quiet way."
            "They're all gone now. Just... gone."

            # Pause for emotional impact
            scene black with fade
            "{i}{size=40}...{/size}{/i}"

            "You sink into the chair, staring at the screen, feeling the weight of what you've just done."
            "The city, its people, its stories... they've vanished without a trace."
            "And yet the screen glows on, the system quietly humming, indifferent to the universe it once held."
            
            "The room feels like a grave—cold, sterile, and filled with the weight of what's been lost."

            menu:
                "Did I make the right choice? Or did I just doom them all?":
                    "But there's no answer. Only the quiet hum of the machines, continuing on as though nothing has changed."
            jump s_a3_del_cyber

        "You can't decide—paralyzed by fear":
            stop music fadeout 2.0

            "Your hand hovers over the panel, shaking, as your mind churns with indecision. The choice lies before you—two worlds, two fates—and yet... you can't move."
            "The memories of Iolkos, Stavros, Bass, and Callie flash before you in rapid succession, but no matter how hard you try, you can't decide."
            
            "Everdusk Valley, with its quiet villages, the forests, the looming mountains... or Everdusk Sector, the neon-lit city with its steel towers and dark alleys."
            "Both worlds, both alive in their own ways, but you know in your heart that they cannot coexist. One must go. But... how could you choose?"
            
            "The screen flickers impatiently before you, as if the system itself knows time is running out."
            
            "{color=#ff4500}System overload detected.{/color}"
            "{color=#ff4500}Memory allocation exceeding critical capacity...{/color}"
            
            menu:
                "I—I can't...":
                    "You pull back from the screen, hands trembling, heart pounding in your chest."
            "The weight of the decision crushes you, and for a moment, you wish someone else could choose for you."
            
            menu:
                "I can't do this... I can't destroy them... I can't...":
                    "But no one is here to make the choice. It's just you, trapped between two worlds, unable to save either."
            
            "{color=#ff4500}Warning: System collapse imminent. Partition integrity failing.{/color}"
            
            "The screen blinks again, more urgently this time. Your pulse races, but still, your fingers freeze, hovering just above the buttons."
            "The control panel flickers. Red warnings flash across the screen like dying embers."
            
            "{color=#ff4500}Partition collapse in 10...{/color}"
            
            "You can't do it. You can't choose. Both worlds, both filled with people and stories, feel too important to erase. The weight of responsibility presses down on your chest, suffocating."
            
            "{color=#ff4500}9...{/color}"
            
            "Your mind spins. Iolkos, that scared little golem, clinging to his world, desperate not to be forgotten."
            "Bass, searching for his identity in the cold, chaotic city streets."
            
            "{color=#ff4500}8...{/color}"
            
            "Callie, driving toward an unknown fate, hoping for survival."
            "Stavros, his mind fractured, his memories crumbling just like the world around him."
            
            "{color=#ff4500}7...{/color}"
            
            menu:
                "I can't let them die... I can't let them vanish...":
                    "{color=#ff4500}6...{/color}"
            
            "But you can't move. Your fingers twitch, but you can't force yourself to press the button."
            "Both worlds spin in your head, entangled, inseparable."

            "{color=#ff4500}5...{/color}"

            "Time slows. Your vision blurs as the countdown inches toward oblivion."

            menu:
                "Please... someone... anyone... make it stop...":
                    "{color=#ff4500}4...{/color}"

            "You can almost hear their voices, faint echoes calling out to you, but you know it's already too late."

            "{color=#ff4500}3...{/color}"

            "The screen flickers violently now, the system overloaded beyond recovery."
            "The room trembles, the hum of the machines turning into a low, ominous roar."

            "{color=#ff4500}2...{/color}"

            "You want to scream, but no sound comes out. Your mind is a storm of indecision, crashing against itself. You can't choose. You can't choose."

            "{color=#ff4500}1...{/color}"

            "And then, in the final second, the screen flashes bright red, and the system collapses."

            "{size=+20}{b}{color=#ff4500}CRITICAL SYSTEM FAILURE{/color}{/b}{/size}"

            "The lights flicker wildly around you, and the world—the control room, the screens, the air itself—seems to warp and distort."
            "You fall to your knees as the room begins to tear apart at the seams, reality buckling under the strain of the overloaded system."

            "{color=#ff4500}System overload... memory partitions... erasing all data...{/color}"

            menu:
                "No... no... I didn't... I didn't choose!":
                    "But it's too late. The two worlds, Everdusk Valley and Everdusk Sector, are collapsing in on themselves, their existence unravelling like fragile threads caught in a storm."

            "The memories of Iolkos, Bass, Callie, Stavros—all of them flicker and fade, like stars blinking out of existence, one by one."
            
            menu:
                "No...!":
                    "The room disintegrates around you, consumed by the encroaching fog, the same fog that tore Bass apart."
            "You can feel it now—pulling at you, too—erasing everything it touches, erasing you."

            "{i}{color=#ff4500}Both worlds have been deleted.{/color}{/i}"

            "You reach out, but there is nothing to hold on to. No world left to save. No world left to mourn."
            "Only emptiness."

            "{size=20}The{/size}"
            "{size=30}fog{/size}"
            "{size=40}wraps{/size}"
            "{size=50}itself{/size}"
            "{size=60}around{/size}"
            "{size=70}you,{/size}"
            "{size=80}and{/size}"
            "{size=90}in{/size}"
            "{size=100}a{/size}"
            "{size=110}moment,{/size}"
            "{size=120}there's{/size}"
            "{size=130}nothing{/size}"
            "{size=140}left.{/size}"

            jump s_a3_bad_ending
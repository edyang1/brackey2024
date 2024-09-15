label s_a2_android:
    $ artstyle = "cyber"

    play music "cyber_casual.mp3" loop fadein 1.0

    scene fantasy_golem with fade
    

    "The street corner is steeped in shadow, occasionally disrupted by the flicker of neon lights and the soft hum of electric signs above."
    "Under the concrete maze of buildings and archways, the small street feels almost forgotten,"
    "a quiet respite in an otherwise busy city."
    "The silicate-heavy urban air fills your lungs,"
    "and the ever-present hum of the city thrums in your ears as you approach a lone door,"
    "the vehicle having parked itself in front of it."
    "As you step closer, the littered remains of packaging, news sheets, and urban debris crunch beneath your feet."
    "From behind, you hear a strange beeping noise coming from the car."
    "Two red dots blink to life on the door as you near, and a voice crackles from an intercom next to the handle."
    
    b "It's you, isn't it? Got Star's message. Come in."

    "The door slides open, revealing a short, sharp-turning corridor bathed in bright light."
    "The door seals itself behind you with a mechanical hiss."
    "You follow the corridor, rounding the corner to another door at the far end."
    "Two soft green dots pulse steadily as you approach."
    "When you open the door, you're greeted by a small, well-organized apartment."
    "The shutters are drawn, casting the room in muted light."
    "A desk is piled high with snacks and vending machine baubles."
    "The furniture is sparse, and the open dressers reveal no clothes or personal belongings."
    "Your attention is drawn to a figure seated at the desk, their back turned to you,"
    "a red hoodie draped over their metallic form."
    "They're tinkering with something on the desk,"
    "but their awareness of your arrival is clear as the door slides shut behind you."

    b "The Office must still be in the dark if someone like you can find me."

    "The voice is soft, almost mechanical, as the figure swivels around in the chair."
    "You realize quickly—they're not human."
    "Metallic limbs glint under the hoodie, attached to a torso concealed by the red fabric."
    "The android's head is a black square screen, two bright white dots serving as eyes that track your every movement."

    b "Well? Are you going to say something?"

    "The android's tone sharpens slightly as it regards your silence. Its left 'eye' stretches upwards,"
    "while the right one shrinks, an expression of... curiosity? You can almost hear the transistors whirring inside."
    "A moment later, the eyes widen back to their original shape, now adorned with white lines that mimic eyebrows, moving in tandem with the pupils."

    b "Oh, I know what you need! Come here."

    "The android rolls over to the vending pile,"
    "grabbing a CannonBall fizzy drink and two Super Beams chocolate bars—banana and whole nuts."
    "Your stomach growls as you accept the snacks, popping open the can and unwrapping the bars."
    "The sweet taste of the chocolate and the fizz of the drink hit your senses, grounding you in the moment."
    jump a2_android_conversation_menu_1:

label a2_android_conversation_menu_1:
    b "So, how is it? I picked those flavors just for you."
    menu:
        "It's good, I like the banana one.":
            "The android's face brightens, the eyes and eyebrows on the screen shifting into a pleased expression."
            b "Banana, huh? Glad you liked it! I think I'd like it too... if I could actually taste anything."

        "It's good, I like the whole nuts one.":
            "The android's screen flickers with what looks like a grin, eyebrows lifting in satisfaction."
            b "Whole nuts, solid choice. I can't taste, but I bet it's crunchy as hell."

        "I don't really like chocolate.":
            "The android's face shifts, the eyes drooping slightly, mimicking a sad expression."
            b "Oh... well, that's a shame. I guess I picked wrong. Not that I could tell—no taste buds and all."

    b "You can call me Bass, by the way."
    b "You're... [f_name]. Nice."
    jump a2_android_conversation_menu_2

label a2_android_conversation_menu_2:
    menu:
        "Inquire about the memory issue he seems to be having.":
            "The android stares at you, thoughtful."
            b "You're having trouble with your memory? Sounds familiar."
            "It tilts its head, eyes flickering as if processing."
            b "Although I'm guessing your case is a different kettle of fish from mine."
            b "You're not a migration android, after all."
            "It turns back to its computer, pulling up files that flicker on the screen."
            "You can hear the low hum of circuits inside its chassis, almost like it's humming under its breath."
            b "I'm assuming you don't remember much about how you got here?"
            "You nod, surprised by the sharpness of Bass' observation."
            "It continues scanning through the files, humming as it goes,"
            "as though your strange situation is just another puzzle to solve."
            b "Since you're definitely a full-fleshed human and not an android like me, I doubt your software's corrupted."
            b "No faulty uploads either."
            "It scrolls through more data on the screen, then leans back in its wheeled chair,"
            "tapping a metallic finger against its chin."
            b "Hmmm..."
            "Its eyes narrow as a soft whirring fills the air—its processors working overtime."
            b "Human brains are... different. More organic, less efficient, but the neural pathways are essentially the same."
            "It leans forward again, tapping a few keys."
            b "Maybe what you need is a medical practitioner, someone more familiar with your kind of circuitry."
            jump a2_android_conversation_menu_2

        "Ask about his name; it sounds exotic.":
            "The android tilts its head, its eyes flickering slightly."
            b "My name? It's nothing special."
            "It pauses for a second, as if considering something."
            b "Bass isn't my real name, though."
            "It lifts the left sleeve of its zipper hoodie, revealing the metal arm underneath."
            "Just above the chest plate, stamped in red letters, you see a serial number etched into the metal."
            b "I'm a prototype. Alius Alloy synthetic human-machine interface, batch four, specimen twenty-two,"
            "modification type C."
            "The numbers and letters glow faintly in the low light, like some sort of corporate branding."
            b "B4/22C. A.Z.Tech's bleeding-edge for neural transmigration."
            "It lets the sleeve fall back down, its eyes fixing on yours."
            b "Back at the Office, some of the staff started calling me Bass."
            "It gives a small shrug, almost human-like."
            b "So, that's what I go by now."
            jump a2_android_conversation_menu_2

        "Ask about the Office he mentioned earlier.":
            b "The Office? That's where I'm from."
            "Its voice shifts, almost as if reminiscing."
            b "Back on Level 12 of the Arcology. One of the big research facilities the corporation has here on the East Coast."
            "The android's eyes flicker briefly, like it's running through old data."
            b "It's one of the main ones. Explains why security was such a hassle to get past."
            "It gestures toward the desktop screen, the faint hum of its internal systems filling the air."
            b "I had to secretly log in, download a bunch of blueprints for the structure and security systems."
            "Its face brightens, as much as a screen with shifting pixels can."
            b "That part was funny, actually. It felt... natural."
            "It leans back, tapping a metal finger on the desk."
            b "I even managed to snag the location and access codes to one of their safehouses."
            "There's a flicker of what almost seems like pride in its voice."
            jump a2_android_conversation_menu_2

        "Ask about why he's stuck inside; is it hiding?":
            "The machine raises one of its eyes at you, clearly puzzled."
            b "Well, yeah. Seems obvious to me, doesn't it?"
            "Its tone carries a hint of amusement, as if stating the obvious."
            b "Why else would I be holed up in here? A.Z.Tech is looking for me as we speak."
            b "I need to keep hacking into their communication arrays, scrambling their signals."
            "It leans back, casually tapping a finger on the desk."
            b "Otherwise, they'll pick up on the lack of communications from this hideout."
            "Bass watches you closely, as if gauging your understanding."
            b "And if you're wondering, your car has the same signature as this safehouse, but not the corporation's."
            "It taps its chin thoughtfully."
            b "I accessed its data and figured you weren't from the Office since you lacked their biometric input."
            "Bass raises a hand, summoning a bright azure display mid-air."
            "It scribbles something with its digits, flipping the screen to show you."
            "You see several schematics of the vehicle you arrived in, plus sketches of you from various angles."
            b "You're not a corpo trooper, nor one of A.Z.Tech's scientists, so I figured you were harmless."
            "Its eyes flash with satisfaction as it continues."
            b "And I was right."
            "It smiles complacently, the pixelated eyebrows rising with a faint beep."
            jump a2_android_conversation_menu_2

        "Exit.":
            jump a2_android_conversation_menu_3

label a2_android_conversation_menu_3:
    menu:
        "Ask for the name of the doctor he's mentioned for your problem.":

            jump a2_android_conversation_menu_3

        "Ask for more information about itself. What's a migration android?":

            jump a2_android_conversation_menu_3

        "Ask how exactly he escaped from this Office. It sounded difficult.":

            jump a2_android_conversation_menu_3

        "Inquire what he's been doing this whole time inside this safehouse.":

            jump a2_android_conversation_menu_3

        "Exit.":
            jump a2_android_conversation_menu_4

label a2_android_conversation_menu_4:
    menu:

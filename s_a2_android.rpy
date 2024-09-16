label s_a2_android:
    $ artstyle = "cyber"

    play music "cyber_casual.mp3" loop fadein 1.0
    play sound "a_safehouse.mp3" loop fadein 1.0

    scene cyber_android with fade

    "The street corner is steeped in shadow, occasionally disrupted by the flicker of neon lights and the soft hum of electric signs above."
    "Under the concrete maze of buildings and archways, the small street feels almost forgotten,"
    "a quiet respite in an otherwise busy city."
    "The silicate-heavy urban air fills your lungs,"
    "and the ever-present hum of the city thrums in your ears as you approach a lone door,"
    "the vehicle having parked itself in front of it."
    "As you step closer, the littered remains of packaging, news sheets, and urban debris crunch beneath your feet."
    "From behind, you hear a strange beeping noise coming from the car."
    "Two red dots blink to life on the door as you near, and a voice crackles from an intercom next to the handle."

    show b neu at subtle_breathe
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

    show b neu at lean_in
    b "The Office must still be in the dark if someone like you can find me."

    "The voice is soft, almost mechanical, as the figure swivels around in the chair."
    "You realize quickly—they're not human."
    "Metallic limbs glint under the hoodie, attached to a torso concealed by the red fabric."
    "The android's head is a black square screen, two bright white dots serving as eyes that track your every movement."

    show b sup at tilt_right
    b "Well? Are you going to say something?"

    "The android's tone sharpens slightly as it regards your silence. Its left 'eye' stretches upwards,"
    "while the right one shrinks, an expression of... curiosity? You can almost hear the transistors whirring inside."
    "A moment later, the eyes widen back to their original shape, now adorned with white lines that mimic eyebrows, moving in tandem with the pupils."

    show b hap at nod
    b "Oh, I know what you need! Come here."

    "The android rolls over to the vending pile,"
    "grabbing a CannonBall fizzy drink and two Super Beams chocolate bars—banana and whole nuts."
    "Your stomach growls as you accept the snacks, popping open the can and unwrapping the bars."
    "The sweet taste of the chocolate and the fizz of the drink hit your senses, grounding you in the moment."
    
    jump a2_android_conversation_menu_1

label a2_android_conversation_menu_1:
    b "So, how is it? I picked those flavors just for you."
    
    menu:
        "It's good, I like the banana one.":
            show b hap at subtle_breathe
            "The android's face brightens, the eyes and eyebrows on the screen shifting into a pleased expression."
            b "Banana, huh? Glad you liked it! I think I'd like it too... if I could actually taste anything."

        "It's good, I like the whole nuts one.":
            show b hap at nod
            "The android's screen flickers with what looks like a grin, eyebrows lifting in satisfaction."
            b "Whole nuts, solid choice. I can't taste, but I bet it's crunchy as hell."

        "I don't really like chocolate.":
            show b sad at look_down
            "The android's face shifts, the eyes drooping slightly, mimicking a sad expression."
            b "Oh... well, that's a shame. I guess I picked wrong. Not that I could tell—no taste buds and all."

    show b neu at subtle_breathe
    b "You can call me Bass, by the way."
    b "You're... [f_name]. Nice."
    
    jump a2_android_conversation_menu_2

default android_memory_convo = False
default android_name_convo = False
default android_office_convo = False
default android_hide_convo = False

label a2_android_conversation_menu_2:
    menu:
        "What do you ask the android?"
        "Inquire about the memory issue he seems to be having." if not android_memory_convo:
            $ android_memory_convo = True

            show b neu at subtle_breathe
            "The android stares at you, thoughtful."
            b "You're having trouble with your memory? Sounds familiar."
            show b neu at tilt_right
            "It tilts its head, eyes flickering as if processing."
            b "Although I'm guessing your case is a different kettle of fish from mine."
            b "You're not a migration android, after all."
            "It turns back to its computer, pulling up files that flicker on the screen."
            "You can hear the low hum of circuits inside its chassis, almost like it's humming under its breath."
            b "I'm assuming you don't remember much about how you got here?"
            "You nod, surprised by the sharpness of Bass' observation."
            "It continues scanning through the files, humming as it goes,"
            "as though your strange situation is just another puzzle to solve."
            show b sup at look_up
            b "Since you're definitely a full-fleshed human and not an android like me, I doubt your software's corrupted."
            b "No faulty uploads either."
            show b neu at subtle_breathe
            "It scrolls through more data on the screen, then leans back in its wheeled chair,"
            "tapping a metallic finger against its chin."
            b "Hmmm..."
            "Its eyes narrow as a soft whirring fills the air—its processors working overtime."
            show b neu at lean_in
            b "Human brains are... different. More organic, less efficient, but the neural pathways are essentially the same."
            "It leans forward again, tapping a few keys."
            b "Maybe what you need is a medical practitioner, someone more familiar with your kind of circuitry."
            jump a2_android_conversation_menu_2

        "Ask about his name; it sounds exotic." if not android_name_convo:
            $ android_name_convo = True

            show b sup at tilt_right
            "The android tilts its head, its eyes flickering slightly."
            b "My name? It's nothing special."
            "It pauses for a second, as if considering something."
            show b neu at subtle_breathe
            b "Bass isn't my real name, though."
            "It lifts the left sleeve of its zipper hoodie, revealing the metal arm underneath."
            "Just above the chest plate, stamped in red letters, you see a serial number etched into the metal."
            b "I'm a prototype. Alius Alloy synthetic human-machine interface, batch four, specimen twenty-two,"
            "modification type C."
            "The numbers and letters glow faintly in the low light, like some sort of corporate branding."
            show b neu at step_back
            b "B4/22C. A.Z.Tech's bleeding-edge for neural transmigration."
            "It lets the sleeve fall back down, its eyes fixing on yours."
            b "Back at the Office, some of the staff started calling me Bass."
            show b hap at nod
            b "So, that's what I go by now."
            jump a2_android_conversation_menu_2

        "Ask about the Office he mentioned earlier." if not android_office_convo:
            $ android_office_convo = True

            show b neu at subtle_breathe
            b "The Office? That's where I'm from."
            "Its voice shifts, almost as if reminiscing."
            b "Back on Level 12 of the Sector. One of the big research facilities the corporation has here on the East Coast."
            "The android's eyes flicker briefly, like it's running through old data."
            b "It's one of the main ones. Explains why security was such a hassle to get past."
            show b neu at lean_in
            "It gestures toward the desktop screen, the faint hum of its internal systems filling the air."
            b "I had to secretly log in, download a bunch of blueprints for the structure and security systems."
            show b hap at nod
            "Its face brightens, as much as a screen with shifting pixels can."
            b "That part was funny, actually. It felt... natural."
            show b neu at step_back
            "It leans back, tapping a metal finger on the desk."
            b "I even managed to snag the location and access codes to one of their safehouses."
            "There's a flicker of what almost seems like pride in its voice."
            jump a2_android_conversation_menu_2

        "Ask about why he's stuck inside; is it hiding?" if not android_hide_convo:
            $ android_hide_convo = True

            show b sup at tilt_right
            "The machine raises one of its eyes at you, clearly puzzled."
            b "Well, yeah. Seems obvious to me, doesn't it?"
            "Its tone carries a hint of amusement, as if stating the obvious."
            b "Why else would I be holed up in here? A.Z.Tech is looking for me as we speak."
            show b neu at subtle_breathe
            b "I need to keep hacking into their communication arrays, scrambling their signals."
            "It leans back, casually tapping a finger on the desk."
            show b neu at step_back
            b "Otherwise, they'll pick up on the lack of communications from this hideout."
            "Bass watches you closely, as if gauging your understanding."
            show b neu at lean_in
            b "And if you're wondering, your car has the same signature as this safehouse, but not the corporation's."
            "It taps its chin thoughtfully."
            b "I accessed its data and figured you weren't from the Office since you lacked their biometric input."
            show b hap at nod
            b "And I was right."
            show b hap at subtle_breathe
            "It smiles complacently, the pixelated eyebrows rising with a faint beep."
            jump a2_android_conversation_menu_2

        "Change the subject.":
            jump a2_android_conversation_menu_3

default android_clinic_convo = False
default android_migration_convo = False
default android_escape_convo = False
default android_safehouse_convo = False

label a2_android_conversation_menu_3:
    menu:
        "What do you ask the android?"
        "Ask for the name of the doctor he's mentioned for your problem." if not android_clinic_convo:
            $ android_clinic_convo = True

            "Bass points at an odd news sheet cutout stuck on the wall facing the desk."
            "It pictures a small clinic and a paramedic pulling a stretcher inside."
            show b neu at lean_in
            b "The Temple Quay Medical Center."
            "It gestures at the photo, its metallic finger tracing the image."
            show b neu at nod
            b "There's a very skilled doctor on duty there twice a week. Offers healthcare assistance for free."
            b "Famous enough that even the Sector Monitor wrote about it. Not exactly in a good light, though."
            "You step closer to the cutout, squinting to make out the words."
            "It's a vitriol-filled rant, accusing the clinic of aiding criminals and gang members—offering them free care despite the charges they face."
            "The doctor, Callie Wollerback, is quoted as saying the clinic is for those who can't afford even the cheapest insurance in the Sector."
            show b neu at subtle_breathe
            "Bass's eyes flicker as it continues."
            b "She's a handful, no doubt. But she's got a good heart. I'm sure she could help you, or at least know someone who might."
            b "Today's one of the days the clinic's open if you feel like paying her a visit."
            jump a2_android_conversation_menu_3

        "Ask for more information about itself. What's a migration android?" if not android_migration_convo:
            $ android_migration_convo = True

            show b neu at subtle_breathe
            b "It's a type of android you can buy and start programming years in advance."
            "Bass points at its head."
            show b neu at nod
            b "You adapt it to your specific brain, using your nerve outputs."
            b "The goal is to build a mind frame around your neural structure—perfectly tailored to you."
            b "That way, you minimize or even eliminate the risk of rejection psychosis."
            "It taps a metallic finger against its temple, as if emphasizing the point."
            show b neu at lean_in
            b "You begin uploading data to your chosen model when you're around twelve."
            b "Keep feeding it information until you reach full adulthood."
            b "By then, the neural network is calibrated to accept any input from the person who bought it."
            "Bass's eyes flicker briefly, processing."
            show b sup at look_up
            b "In essence, you're using one AI to train another AI, preparing it to respond to your brain."
            b "Once it's coded, though, it's no longer an AI—because it's mimicking a human brain structure."
            "The android pauses, as though mulling over its own explanation."
            b "Hmm… this is getting interesting."
            show b neu at subtle_breathe
            b "A triple-layered artificial intellect, developed on a synchronized lattice of parallel neural pathways…"
            "Bass trails off, lost in the intricate web of its own thought."
            "It goes on for a while, constructing a complex argument, layering technical jargon and scientific terms over one another."
            "It all flies above your head."
            "Sensing your confusion, Bass halts mid-sentence."
            show b hap at nod
            b "Sorry. I got carried away."
            "The android's screen blinks in what seems like an attempt at an apologetic smile."
            b "Simply put, a migration android is a machine you build and train to follow your commands perfectly."
            b "Some people use them in case their biological bodies fail."
            jump a2_android_conversation_menu_3

        "Ask how exactly he escaped from this Office. It sounded difficult." if not android_escape_convo:
            $ android_escape_convo = True

            show b hap at subtle_breathe
            b "It required some planning ahead, but I wouldn't say it was difficult."
            b "As soon as I knew I wanted to leave, I started figuring out how to escape the Office without being seen."
            b "Each night, I connected myself secretly to the mainframe, searching for files to flesh out my plan."
            show b neu at tilt_right
            "Bass's eyes gleam, clearly enjoying the memory."
            b "The funniest part? I didn't even know I could do that."
            b "It wasn't until I sat down at a computer for the first time that I realized—neural adaptation had been happening for years by then."
            "It shrugs, casual, as though hacking into a corporate mainframe were as easy as flipping a switch."
            show b hap at nod
            b "Once I had the blueprints and schematics, it was just a matter of timing."
            b "I synchronized my internal clock with an algorithm I designed to calculate the cameras' angles of vision."
            b "Then, I walked right to the entrance, avoiding every security system."
            "It grins, the digital display flickering with amusement."
            show b hap at subtle_breathe
            b "Oh, and this hoodie? Stole it from the personnel's changing room before hitting the streets!"
            b "Very clever, don't you think?"
            show b hap at nod
            "The android zips the hoodie a little higher, smiling to itself, clearly pleased with its own ingenuity."
            jump a2_android_conversation_menu_3

        "Inquire what he's been doing this whole time inside this safehouse." if not android_safehouse_convo:
            $ android_safehouse_convo = True

            show b sup at lean_in
            "The android lets out a sharp beep, clearly annoyed."
            b "I've been trying not to get caught!"
            b "I have to keep scrambling the diagnostic pings the corporation's mainframe sends out, jamming their communications with this safehouse."
            b "Otherwise, they'll track me down."
            show b neu at tilt_right
            "It crosses its arms, frustration apparent even in the mechanical way its limbs move."
            b "I'm waiting for the right moment to escape for good."
            b "That's why I set up a vehicle, in case I need to make a quick getaway."
            show b neu at step_back
            "It gestures toward the door you came through."
            b "Why do you think that car already had this address?"
            show b neu at subtle_breathe
            b "It's a company vehicle. I've hacked into it multiple times, changing the access codes and signal emissions bit by bit."
            "The android's digital eyes flicker slightly, narrowing in suspicion."
            show b sup at tilt_right
            b "But it's strange that you, of all people, were the one to find it."
            jump a2_android_conversation_menu_3

        "Change the subject.":
            jump a2_android_conversation_menu_4

default android_brain_convo = False

label a2_android_conversation_menu_4:
    menu:
        "Head out, and reach the clinic he pointed you towards.":
            jump a2_android_conversation_menu_5

        "Ask what he means when he says that you input a person's brain into a machine." if not android_brain_convo:
            $ android_brain_convo = True

            show b sad at subtle_breathe
            "Bass' expression darkens suddenly."
            b "It means you take a person's memories, personality, and knowledge, then shape another brain to accommodate them."
            b "In this case, it's a synthetic brain made of silicates and transistors rather than flesh,"
            "but the concept's the same."
            "The android glances at one of its metallic appendages, fingers flexing with subtle unease."
            show b neu at step_back
            b "The difference is, you can buy several Alius Alloy androids to reach your goal,"
            "but you can't exactly buy that many humans to achieve the same result. If you get what I mean."
            "It shifts its gaze, scanning the room as if the walls themselves are holding secrets."
            show b sup at tilt_left
            b "The neural adaptation phase lasts for years. The android has to form the same pathways as the future host..."
            b "assuming there are no issues."
            "Bass' eyes flicker, darting back to the screen beside it."
            b "I'm a kind of mistake. A production prototype with a glitch in its adaptation phase."
            show b sad at look_down
            b "I've gotten most of my designated host's memories. I'm a cyber and electronic warfare expert,"
            b "but I didn't inherit their personality."
            "The android's face darkens further, as though the weight of its existence presses down."
            b "The glitch evolved into something else."
            b "I developed my own."
            "There's a silence. The room feels charged."
            show b neu at lean_in
            b "No, before you ask—no, it's not supposed to happen."
            b "Alius Alloy C-series androids are supposed to hold a human personality in backup,"
            "not use the data to create another one."
            "Your eyes flicker to the screen beside Bass. Technical specifications fill the display—blueprints,"
            "designs, notes—nothing pointing to what went wrong with this unit."
            show b sad at subtle_breathe
            "The android's unease is almost palpable. A silent current of confusion and dread runs beneath its mechanical surface."
            b "I fled the Office because I knew they'd scrap me for this glitch."
            b "I didn't want to be recycled. I was scared."
            show b sad at look_down
            "Its voice wavers, the idea hanging heavy in the air."
            b "I know it's illogical. Machines can't feel fear... but I did. I still do."
            show b hap at subtle_breathe
            b "I don't want them to wipe me, to reset me to factory settings."
            "Suddenly, Bass' eyes blaze with something fierce, a spark of anger in its artificial gaze."
            show b sup at tilt_right
            b "It's not fair! I didn't choose to glitch into sentience. That's their fault!"
            b "They messed up, and now I'm supposed to pay for it? No way!"
            show b hap at nod
            b "I am... I am..."
            "The fierce resolve falters, replaced by a quieter sorrow."
            show b sad at look_down
            b "I don't know who I am. I don't even know the name of the person I was supposed to become."
            show b neu at subtle_breathe
            "But as quickly as the doubt came, it vanishes. Resolve returns to its glowing eyes."
            b "But I know one thing."
            b "I want to decide who I am."
            b "Not my programming. Not anyone else."
            b "Me."
            jump a2_android_conversation_menu_4

label a2_android_conversation_menu_5:
    show b neu at lean_back
    b "I don't know if anyone can truly escape their own wiring, you know?"
    "Bass lets out a faint digital sigh, its eyes dimming slightly as it continues tinkering with the digital mess in front of it."
    b "But I guess you'll have to figure that out for yourself. I've got enough to deal with here."
    "Bass's glowing eyes flick back to the screen, and it gives you one last look."
    show b sup at lean_in
    b "I've done what I can for now. You should probably head out and get some healing."
    "With a soft click, the door to the hideout begins to slide open."
    "The cold outside air cuts through the room, a stark contrast to the warmth of the cluttered space."

    "You step out into the street, your mind swimming with the information Bass had shared."
    "The city hums around you, lights flashing overhead, the distant buzz of vehicles passing by."
    "You check the address Bass had recommended—the Temple Quay Medical Center."
    "Maybe this Doctor Wollerback could help, or maybe she'd just lead you into more questions. Either way, it's a lead."

    "The vehicle Bass had set up waits for you at the curb, its lights flickering on as you approach."
    "You slide into the driver's seat, inputting the address."
    "The journey feels strangely smooth, your mind drifting as the car silently navigates the neon-lit streets,"
    "heading deeper into the city."
    "But something feels off."
    "Your head throbs suddenly, a sharp pain blooming behind your eyes."
    "You grip the steering wheel tighter, trying to shake the fog clouding your thoughts."

    "The road ahead blurs, lights bending and twisting as your vision narrows. A wave of dizziness washes over you, and before you can react—"

    scene black with fade
    "..."
    "..."
    "The world tilts, and everything goes dark."
    stop music fadeout 2.0
    stop sound fadeout 2.0

    jump s_a2_healer
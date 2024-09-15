label s_a2_healer:
    $ artstyle = "cyber"

    play music "cyber_casual.mp3" loop fadein 1.0
  
    "The kaleidoscope of lights and sounds was drowned out by a sudden, encroaching blackness that consumed you just as you lay inside the white puff of cloth."
    "You have scarce memories of people yelling something and more vehicles moving around you."
    "Not understanding much, you do however remember the canopy being opened up and someone grabbing you."

    scene fantasy_healer with fade

    "You come back to your senses on a short bed,"
    "surrounded by beeping contraptions you are hooked to via a tube and a cable placed on your left arm."
    "You feel some pain in your head and legs and can spot bandaging around your shins and feet."
    "The room is not spacious, but cozy enough to be in."
    "What personal belongings you had, not much really—"
    "perhaps just a slim rectangular appliance and a small plastic card—have been placed in a box next to your bed."
    "You don't feel pain, but you are far from your peak form."
    "Your head swings from side to side sometimes, and you have trouble focusing on more than one thing at a time."

    "A pleasant smell breaks your concentration, shifting your attention from the box to a tray left at your side."
    "A dish with spindly, yellowish threads sits under a transparent lid, not fully locked, the cover clouded with moisture."
    "You sense onions and see thick juice pooling underneath the strands."
    "You grab the dish and the fork left beside it, indulging in the meal."

    cal "Glad you woke up so soon."

    "A voice calls out from the doorframe."
    "Looking up from your food, strands of noodles hanging off your fork, you meet the gaze of a tall, thin woman."
    "She's dressed in work fatigues, a white patch on her right arm."
    "Her fingers are mechanic, sharp-looking, and parts of her face have been replaced with sleek cyber enhancements,"
    "color-matching her bright ashen hair."
    "Yet, despite the cold metal, her features radiate warmth, a relaxing shine that eases you."
    "She moves closer, checking the monitors of the machines you're connected to."
    "She chuckles when she notices how you're enjoying the meal."
    "You realize just how starving you feel."

    "The woman smiles."

    cal "I'm happy you like them."
    cal "They're from the restaurant down the street."
    cal "I eat them all the time—they're quite cheap and absolutely delicious."
    cal "They're called noodles."

    "The woman chuckles softly."

    cal "I could tell you were starving from the sound your stomach made as we brought you in after the car crash."
    cal "Figured you'd enjoy something like noodles to help you recover."

    "She gives you a quick glance over, then flashes a warm, almost motherly smile."

    cal "By the way, I'm Doctor Callie Wollerback, but you can just call me Callie."
    jump a2_healer_conversation_menu_1

label a2_healer_conversation_menu_1:
    menu:
        "Why do you work here, offering free care in a place like this?":
            cal "Why do I work here?"
            cal "In a place like this?"
            
            "She looks away for a moment, eyes tracing the room as if searching for an answer she's already known too well."
            
            cal "Most people would say it's a waste of time. They'd call me naive, soft-hearted."
            
            "Her lips twitch into the faintest of smiles, though it doesn't reach her eyes."
            
            cal "But I've seen what happens when no one cares. When people are left to rot, with nothing but the cold and their own pain."
            
            "She folds her arms, almost like she's protecting herself from a memory she'd rather forget."
            
            cal "I couldn't live with that. Couldn't walk away knowing I had the skills to help but didn't."
            
            "For a moment, she pauses, her expression softening."
            
            cal "Maybe I'm just trying to make the world... a little less broken. One person at a time."
            
            "Her gaze locks onto you, clear and unwavering."
            
            cal "It's not about saving the world. It's about saving who's in front of me."
            
            "She exhales, the weight of her own words heavy but familiar."
            
            cal "And if that means staying in this hole, getting my hands dirty, then so be it."
            jump a2_healer_conversation_menu_1
   
        "How do you handle losing patients, especially when you've done everything you can?":
            cal "Have I ever lost someone?"
    
            "She closes her eyes, a shadow crossing her face, as if the memories resurface too quickly to suppress."
            
            cal "More times than I care to count."
            
            "Her voice is steady, but there's a tension beneath it, the kind that only comes from deep, unresolved grief."
            
            cal "It's not something you ever really get used to."
            
            "She leans against the counter, fingers tapping lightly, almost subconsciously."
            
            cal "There's always that moment…"
            
            "Her gaze flickers downward, distant, like she's reliving it in real-time."
            
            cal "That moment where you think, ‘maybe this time, I can pull them back.'"
            
            "A small, bitter laugh escapes her, though there's no humor in it."
            
            cal "And then you can't."
            
            "The silence that follows is palpable, hanging between you like an unspoken truth."
            
            cal "I've had people flatline right in my arms. No matter what I did... it wasn't enough."
            
            "Her hands flex, as if trying to grasp something invisible, something lost."
            
            cal "It makes you question yourself. Your skills. Your resolve."
            
            "She straightens up, her eyes narrowing, hardening."
            
            cal "But I can't let that stop me. Every loss is a scar, but every life saved... that's the step forward."
            
            "Her voice softens, though the resolve remains."
            
            cal "I owe it to the ones I couldn't save, to keep trying. To keep learning. To do better."
            
            "She turns away slightly, her shoulders stiff, as though bracing herself for the next battle."
            
            cal "Because someone else will need me, and I can't afford to let them down."
            jump a2_healer_conversation_menu_1

        "Is it ever difficult to hold onto your ideals in a place like this?":
            cal "Struggle with my morals?"
    
            "She sighs, her expression softening, as if the weight of the question presses down on her."
            
            cal "Every day."
            
            "She crosses her arms, looking off to the side, her jaw tightening as if holding back something more."
            
            cal "You patch someone up, send them back out into this broken city... knowing full well they might get hurt again."
            
            "Her voice drops, lower, more intense, almost as if she's questioning herself."
            
            cal "Sometimes, I wonder if I'm really helping. Or just delaying the inevitable."
            
            "She pauses, her fingers tracing the edge of a nearby medical tray absentmindedly, her thoughts elsewhere."
            
            cal "And then there's the system. The corporations, the politics, the greed."
            
            "Her hands clench into fists, knuckles white with frustration."
            
            cal "You save someone today, only for them to be swallowed by the same mess tomorrow."
            
            "There's a brief silence, and for a moment, you see the cracks in her resolve, the doubt creeping in."
            
            cal "It would be so easy to just... give in, let the city take over."
            
            "Her eyes narrow, hardening with renewed focus."
            
            cal "But I can't. I won't."
            
            "She uncrosses her arms, standing straighter, her expression sharp again."
            
            cal "Because if I stop fighting, if I stop caring, then what's left? Who's left to pick up the pieces?"
            
            "Her gaze locks onto yours, fierce and unwavering."
            
            cal "People think I'm naive for trying to make a difference. Maybe I am. But someone has to."
            
            "She sighs again, but this time it's not out of frustration—it's determination."
            
            cal "I can't let this city take away what's left of me. I have to believe there's still some good I can do, even if it's just for one more person."
            jump a2_healer_conversation_menu_1

        "Exit":
            jump a2_healer_conversation_menu_2

label a2_healer_conversation_menu_2:
    "hello world"
        
label s_a1knight:
    
    "He noticed you before you had a chance to turn away."
    "His gaze, sharp and thoughtful, settled on you with the calm focus of someone used to watching over others."
    stav "A traveler?"
    "His voice was low and gravelly."
    stav "I don't see many passing through here anymore."
    "The knight raised his good arm in a welcoming gesture, though his tone carried a note of wariness."

    python:
        f_name = renpy.input("What's your name?", default = "Cassiopeia")
        f_name = f_name.strip()
        if f_name == "":
            f_name = "Cassiopeia"
    
    "He nodded slightly, as if turning the name over in his mind. "
    stav "Well met, [f_name]. I'm Stavros."
    stav "These parts don't offer much in the way of hospitality, but if you're in need of rest, I have room for one more."
    "He glanced briefly at the tombstones, his expression momentarily darkening."
    stav"I've seen enough of the dead for one day."
    "He stepped away from the graves and motioned for you to follow."
    stav "Come on. My home's not far."
    stav "It'll be night soon, and the cold isn't something to face out here."

    "You followed him as the sun slipped lower, casting longer shadows over the road."
    "His movements were deliberate, the result of years spent adjusting to the loss of his arm."
    "The silence between you was comfortable, only broken by the distant call of some forest creature—an odd, lilting sound that echoed through the trees." 
    "It was unlike anything you'd heard before, a soft whine that turned into a sharp, two-toned yip, almost as if two voices were calling out at once."
    "The sound was fleeting, swallowed quickly by the wind, but it lingered in your mind, tugging at old stories of creatures said to roam these lands."

    "As you rounded a bend, his home came into view—a small, unassuming cottage with smoke curling from its chimney."
    "The simple structure stood alone, with small, rounded tombstones from the cemetery nestled nearby."
    "The knight pushed open the wooden door with a nod."
    stav "I'll be damned if I let anyone freeze to death on my doorstep. Come on in."

    scene fantasy_cottage with dissolve

    "Inside, the warmth of the fire greeted you, the comforting scent of herbs and simmering soup filling the air."
    "The walls were simple daub, washed white with plaster, with wooden beams poking through the construction material."
    "Hanging from the beams were herbs and dried meats, swaying gently with the draft from the door."
    "A bubbling pot hung over the fire, sending out a rich, earthy aroma."
    stav "It's nothing fancy, but it'll keep the cold out."
    "He gestured for you to take a seat at the table."
    "He moved slowly, surely, to a cupboard near the chimney."
    "After taking out a plate with wooden cutlery, he set it on the table before pouring you a cup of warm, sweet wine from a terracotta ewer sitting by the fire."
    "Then, he dished out two bowls of thick soup, the hearty smell of chestnuts, onions, and dried venison rising with the steam."
    stav "[f_name]. What are you doing out here?"
    
    menu:
        "I'm a traveler on a search for adventure. I've been wandering for a while now.":
            jump a1_knight1
        "I got lost in the forest. I wasn't expecting to end up here.":
            jump a1_knight1
            
label a1_knight1:
    stav "You don't look like you're from around here, especially given how the cold seems to have taken its toll on you."
    stav "These mountains can be unforgiving, and winter's only just starting to settle in."
    "He paused, studying you for a moment."
    "Where are you from?"

    menu:
        "I don't know, I don't recall how I got here.":
            stav "You mean you don't remember whence you came? And just did you manage to get this far?"
            stav "You're lucky I found you before the wolves did."
            "You take a moment to look around his home."
            jump a1_conversation_menu

label a1_conversation_menu:
    menu:
        "Ask him about his name and trade.":
            "The man seems taken aback by your question, his brows furrowing in brief confusion. But the moment passes quickly, and he regains his composure."
            "He lets out a small chuckle."
            stav "Stavros Attelides. I once led the Marquis' militia in these parts."
            "As he speaks, his voice drifts off, and you notice his gaze faltering, his eyes fixed somewhere beyond you."
            "A flicker of sorrow crosses his face before he snaps back to the present, almost too abruptly."
            stav "Forgive me. I tend to... slip away sometimes. Old ghosts. They'll never rest."
            "His voice is quieter now, tinged with something deeper."
            "He gestures towards you with his maimed arm, his expression softening slightly."
            stav "You're not the first one to come through here, lost in more ways than one."
            stav "There's someone else, like you... struggling to remember who they are."
            "He pauses, as if the weight of his own words settles on him."
            stav "Memory's a complicated thing, isn't it?"
            jump a1_conversation_menu

        "Point at the shield. There must be a story behind that.":
            "The man's eyes brighten for a moment, a rare spark lighting up his otherwise gruff demeanor as you mention the shield."
            stav "Ah, that old thing."
            "His voices fills with pride and nostalgia."
            stav "That's the shield I carried back when I led the Kestrels—the Marquis' finest militia."
            "It's seen more battles than I care to remember."
            "He gives a low, gruff chuckle, but it's bittersweet."
            "His expression hardens for a moment as he raises the stump where his arm used to be, the humor fading from his voice."
            stav "That was before... Before I lost the arm. Can't wield it anymore. Haven't touched a shield in years."
            "He sighs, a heavy sound."
            "You take a closer look at the shield, noticing its lozenge shape and the deep wear on its surface, signs of many hard-fought battles."
            "Its background is a weathered yellow, crossed by a black stripe running down the middle."
            "On one side, you see a vertical line with three tapering streaks—like a stylized pine tree."
            "The other half bears the image of a bird, painted black, its large tail feathers unmistakably those of a kestrel."
            stav "The Kestrel... fitting, isn't it?" 
            "He spoke softly now, his rough exterior cracking just enough to let some warmth through."
            stav "That bird—it's a fighter. Like we all were. Fast, sharp, but..."
            stav "But not invincible."
            "He looks at the shield again, but this time with a quieter, softer gaze."
            "His fingers gently trace the outline of the kestrel."
            stav "This thing's all that's left of that life."
            "He straightens up, the moment of softness gone as quickly as it came."
            stav "I keep it around to remind myself what it cost. Every scratch, every mark—there's a story there. Not all of them good."
            "He turns away, his voice gruff again, but there's a slight crack in the facade."
            stav "Enough about the past. Doesn't do much good to dwell on it, eh?"
            jump a1_conversation_menu

        "Ask him about the cemetery.":
            "The man turned his face to the window, his gaze drifting beyond the rough glass panels."
            "He shifted slightly in his chair."
            stav "That's the final resting place of the Cordean Kestrels," 
            "His voice takes on a reverence you hadn't heard before."
            stav "My brothers-in-arms. I'm their warden now. Their caretaker."
            "He paused, eyes lingering on the graves as if he could still see them standing there, alive and ready for battle."
            "Then he pointed to the shield hung over the door, the same one he had spoken of earlier."
            stav "That's the old insignia of the regional militia. The Kestrels… we were the best."
            "One of the finest companies the Marquis ever had. Way back in the day." 
            "There was pride in his voice, but it was tinged with something heavier—regret, or perhaps the weight of memory."
            "He turned back to you, pushing himself up from his chair with a slow, deliberate movement."
            stav "Since we're speaking of them, it's only right I honor them properly."
            "Stavros walked to the cupboard, his movements measured, as if this was a ritual he had performed many times before."
            "He pulled out a small bottle, its contents dark, and poured a portion into a cup."
            "Without a word, he made his way to the fireplace."
            "The fire crackled softly as he tossed the liquid into the flames, which leaped higher in response, casting long shadows across the room."
            stav "To your health, brothers. May you rest in peace."
            "He stood there for a moment longer, the flames reflecting in his eyes, before returning to the table."
            "Noticing your puzzled expression, he let out a low, tired chuckle."
            stav "It's an old tradition,"
            "Among knights and military brotherhoods. We offer a glass to those who aren't here anymore... those who fell before us."
            "He paused, then added, almost as if to himself,"
            stav "It's the least we can do to keep their memory alive."
            jump a1_conversation_menu
            
        "Ask about the woodcarving implements on the far side of the room.":
            "The man glanced down at the scattered wood shavings beneath the bench, his lips curling into a small, crooked smirk."
            stav "That’s what keeps me busy these days."
            stav "Ever since the militia put me out to pasture."
            "He nodded toward the table, where the simple wooden cutlery lay neatly arranged."
            stav "Made all of these myself over the years. Keeps the hands busy… what's left of them, anyway."
            jump a1_conversation_menu

        "Exit":
            jump a1_knight2

label a1_knight2:

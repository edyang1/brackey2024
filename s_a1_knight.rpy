label s_a1_knight:

    "He notices you before you have a chance to turn away."
    "His gaze, sharp and thoughtful, settles on you with the calm focus of someone used to watching over others."
    stav "A traveler?"
    "His voice is low and gravelly."
    stav "I don't see many passing through here anymore."
    "The knight raises his good arm in a welcoming gesture, though his tone carries a note of wariness."

    python:
        f_name = renpy.input("What's your name?", default = "Cassiopeia")
        f_name = f_name.strip()
        if f_name == "":
            f_name = "Cassiopeia"

    "He nods slightly, as if turning the name over in his mind."
    stav "Well met, [f_name]. I'm Stavros."
    stav "These parts don't offer much in the way of hospitality, but if you're in need of rest, I have room for one more."
    "He glances briefly at the tombstones, his expression momentarily darkening."
    stav "I've seen enough of the dead for one day."
    "He steps away from the graves and motions for you to follow."
    stav "Come on. My home's not far."
    stav "It'll be night soon, and the cold isn't something to face out here."

    "You follow him as the sun slips lower, casting longer shadows over the road."
    "His movements are deliberate, the result of years spent adjusting to the loss of his arm."
    "The silence between you is comfortable, only broken by the distant call of some forest creature—an odd, lilting sound that echoes through the trees."
    "It is unlike anything you've heard before, a soft whine that turns into a sharp, two-toned yip, almost as if two voices are calling out at once."
    "The sound is fleeting, swallowed quickly by the wind, but it lingers in your mind, tugging at old stories of creatures said to roam these lands."

    "As you round a bend, his home comes into view—a small, unassuming cottage with smoke curling from its chimney."
    "The simple structure stands alone, with small, rounded tombstones from the cemetery nestled nearby."
    "The knight pushes open the wooden door with a nod."
    stav "I'll be damned if I let anyone freeze to death on my doorstep. Come on in."

    scene fantasy_cottage with dissolve

    "Inside, the warmth of the fire greets you, the comforting scent of herbs and simmering soup filling the air."
    "The walls are simple daub, washed white with plaster, with wooden beams poking through the construction material."
    "Hanging from the beams are herbs and dried meats, swaying gently with the draft from the door."
    "A bubbling pot hangs over the fire, sending out a rich, earthy aroma."
    stav "It's nothing fancy, but it'll keep the cold out."
    "He gestures for you to take a seat at the table."
    "He moves slowly, surely, to a cupboard near the chimney."
    "After taking out a plate with wooden cutlery, he sets it on the table before pouring you a cup of warm, sweet wine from a terracotta ewer sitting by the fire."
    "Then, he dishes out two bowls of thick soup, the hearty smell of chestnuts, onions, and dried venison rising with the steam."
    stav "[f_name]. What are you doing out here?"

    menu:
        "I'm a traveler on a search for adventure. I've been wandering for a while now.":
            jump a1_knight1
        "I got lost in the forest. I wasn't expecting to end up here.":
            jump a1_knight1

label a1_knight1:
    stav "You don't look like you're from around here, especially given how the cold seems to have taken its toll on you."
    stav "These mountains can be unforgiving, and winter's only just starting to settle in."
    "He pauses, studying you for a moment."
    stav "Where are you from?"

    menu:
        "I don't know, I don't recall how I got here.":
            stav "You mean you don't remember whence you came? And just how did you manage to get this far?"
            stav "You're lucky I found you before the wolves did."
            "You take a moment to look around his home."
            jump a1_knight_conversation_menu1

label a1_knight_conversation_menu1:
    menu:
        "Ask him about his name and trade.":
            "The man seems taken aback by your question, his brows furrowing in brief confusion. But the moment passes quickly, and he regains his composure."
            "He lets out a small chuckle."
            stav "Stavros Attelides. I once led the Marquis' militia in these parts."
            "As he speaks, his voice drifts off, and you notice his gaze faltering, his eyes fixed somewhere beyond you."
            "A flicker of sorrow crosses his face before he snaps back to the present, almost too abruptly."
            stav "Forgive me. I tend to... slip away sometimes. Old ghosts. They never rest."
            "His voice is quieter now, tinged with something deeper."
            "He gestures toward you with his maimed arm, his expression softening slightly."
            stav "You're not the first one to come through here, lost in more ways than one."
            stav "There's someone else, like you... struggling to remember who they are."
            "He pauses, as if the weight of his own words settles on him."
            stav "Memory's a complicated thing, isn't it?"
            jump a1_knight_conversation_menu1

        "Point at the shield. There must be a story behind that.":
            "The man's eyes brighten for a moment, a rare spark lighting up his otherwise gruff demeanor as you mention the shield."
            stav "Ah, that old thing."
            "His voice fills with pride and nostalgia."
            stav "That's the shield I carried back when I led the Kestrels—the Marquis' finest militia."
            "It's seen more battles than I care to remember."
            "He gives a low, gruff chuckle, but it's bittersweet."
            "His expression hardens for a moment as he raises the stump where his arm used to be, the humor fading from his voice."
            stav "That was before... before I lost the arm. Can't wield it anymore. Haven't touched a shield in years."
            "He sighs, a heavy sound."
            "You take a closer look at the shield, noticing its lozenge shape and the deep wear on its surface, signs of many hard-fought battles."
            "Its background is a weathered yellow, crossed by a black stripe running down the middle."
            "On one side, you see a vertical line with three tapering streaks—like a stylized pine tree."
            "The other half bears the image of a bird, painted black, its large tail feathers unmistakably those of a kestrel."
            stav "The Kestrel... fitting, isn't it?"
            "He speaks softly now, his rough exterior cracking just enough to let some warmth through."
            stav "That bird—it's a fighter. Like we all were. Fast, sharp, but..."
            stav "But not invincible."
            "He looks at the shield again, but this time with a quieter, softer gaze."
            "His fingers gently trace the outline of the kestrel."
            stav "This thing's all that's left of that life."
            "He straightens up, the moment of softness gone as quickly as it came."
            stav "I keep it around to remind myself what it cost. Every scratch, every mark—there's a story there. Not all of them good."
            "He turns away, his voice gruff again, but there's a slight crack in the facade."
            stav "Enough about the past. Doesn't do much good to dwell on it, eh?"
            jump a1_knight_conversation_menu1

        "Ask him about the cemetery.":
            "The man turns his face to the window, his gaze drifting beyond the rough glass panels."
            "He shifts slightly in his chair."
            stav "That's the final resting place of the Cordean Kestrels."
            "His voice takes on a reverence you haven't heard before."
            stav "My brothers-in-arms. I'm their warden now. Their caretaker."
            "He pauses, eyes lingering on the graves as if he can still see them standing there, alive and ready for battle."
            "Then he points to the shield hung over the door, the same one he had spoken of earlier."
            stav "That's the old insignia of the regional militia. The Kestrels… we were the best."
            "One of the finest companies the Marquis ever had. Way back in the day."
            "There is pride in his voice, but it is tinged with something heavier—regret, or perhaps the weight of memory."
            "He turns back to you, pushing himself up from his chair with a slow, deliberate movement."
            stav "Since we're speaking of them, it's only right I honor them properly."
            "Stavros walks to the cupboard, his movements measured, as if this is a ritual he has performed many times before."
            "He pulls out a small bottle, its contents dark, and pours a portion into a cup."
            "Without a word, he makes his way to the fireplace."
            "The fire crackles softly as he tosses the liquid into the flames, which leap higher in response, casting long shadows across the room."
            stav "To your health, brothers. May you rest in peace."
            "He stands there for a moment longer, the flames reflecting in his eyes, before returning to the table."
            "Noticing your puzzled expression, he lets out a low, tired chuckle."
            stav "It's an old tradition."
            "Among knights and military brotherhoods. We offer a glass to those who aren't here anymore... those who fell before us."
            "He pauses, then adds, almost as if to himself,"
            stav "It's the least we can do to keep their memory alive."
            jump a1_knight_conversation_menu1

        "Ask about the woodcarving implements on the far side of the room.":
            "The man glances down at the scattered wood shavings beneath the bench, his lips curling into a small, crooked smirk."
            stav "That's what keeps me busy these days."
            stav "Ever since the militia put me out to pasture."
            "He nods toward the table, where the simple wooden cutlery lay neatly arranged."
            stav "Made all of these myself over the years. Keeps the hands busy… what's left of them, anyway."
            jump a1_knight_conversation_menu1

        "Exit":
            "He sighs deeply, taking a long sip of the soup and leaning back in his chair."
            jump a1_knight_conversation_menu2

label a1_knight_conversation_menu2:
    menu:
        "Ask about the other person suffering from your same ailment.":
            stav "He's an odd one, no doubt, but a decent sort. Stays over at an inn not too far from here."
            "He pauses for a moment, as if weighing his words carefully."
            stav "Might be worth your time to seek him out. Have a chat."
            stav "Who knows—maybe there's something that can be done for both of you."
            jump a1_knight_conversation_menu2

        "Inquire more about the Kestrels he mentioned earlier.":
            "Stavros leans back in his chair, settling in with a slow sip of the sweetened wine."
            "He pauses for a long time, his gaze fixed on the flames dancing in the hearth."
            "As he speaks, his voice grows softer, more reflective."
            stav "The Cordean Kestrels... we were a brotherhood, born in these mountains."
            stav "Just a group of militiamen from the highlands, where the kestrels fly."
            "He pauses, as if remembering a time long past."
            stav "I joined them young, maybe seventeen, still green but eager."
            "His gaze remains fixed on the mountains, as if trying to pull something from their jagged silhouettes."
            "The weight of years seems to settle over him like a heavy cloak."
            stav "We fought together for more than a decade and a half, serving under the Marquis' banner."
            stav "By the time the battle for the plateau came, I'd taken command after old Menavlios fell in combat."
            stav "Led the men myself... right into the storm."
            "He falls silent, his eyes no longer on the peaks but scanning the room,"
            "eventually resting on a tall piece of furniture draped in cloth in the far corner."
            "The memories seem to hang in the air between you."
            stav "Now, I'm the only one left."
            "For a moment, the room feels colder, despite the fire crackling in the hearth."
            "The words linger, heavy, as if the weight of the entire brotherhood rests on his shoulders."
            stav "I do what I can to keep their memory alive."
            "His voice has dimmed, worn by the years of carrying the burden alone."
            stav "But it's not enough, is it? You bury your brothers, and what's left? Just me."
            stav "One old man trying to hold onto something that's long gone."
            jump a1_knight_conversation_menu2

        "Ask why he's chosen to stay and take care of the graveyard.":
            stav "After the battle at the plateau, the Marquis makes me a knight."
            stav "Calls me an 'honorable hero of the region,' and offers me a peaceful retirement—"
            "a plot of land, the means to live comfortably."
            stav "A reward for all the blood I've spilled, I suppose."
            "He pauses, his tone turning bitter."
            stav "All while my comrades lay dead in the dirt."
            "Stavros raises his sole hand, gesturing at the walls around him, as if they are more a prison than a home."
            stav "I refuse at first."
            stav "Tell the Marquis that four walls and a roof can never compare to the lives of the men I lost."
            stav "What good is peace when your brothers-in-arms are gone?"
            "He shakes his head, his expression hardening."
            stav "But the Marquis... well, he convinces me to take it, eventually."
            "There is a heaviness in his voice, and then he adds, quieter, but with conviction."
            stav "But I make one demand. My comrades—they have to come with me."
            "His gaze sweeps to the window, where the gravestones stand like silent sentinels."
            stav "I have them build this house, and with it, the cemetery."
            stav "I become their guardian. Their warden."
            "He falls silent for a long moment, the weight of the years pressing down on him."
            stav "Now I wait."
            stav "Watch over them until my time comes... and I can join them, one last time."
            stav "It's the price I pay, for surviving."
            stav "For losing an arm, and all the rest of it."
            jump a1_knight_conversation_menu2

        "Ask for how long he's been practicing whittling, since he's very good at it.":
            stav "That was my trade once."
            "His voice softens, a hint of nostalgia in his words."
            stav "My father teaches me when I am just a boy."
            stav "I spend my younger years honing the craft, day after day."
            stav "Carvings of horses, birds, mountains, you name it."
            stav "They are terrible, of course, but I keep at it."
            stav "Carving, shaping—figure it'd be my life's work."
            "He pauses, his gaze turning to the chimney, where two finely polished stone statuettes sit,"
            "their features carved in grey marble—a man and a woman."
            stav "But things change."
            stav "The plague comes through, takes my parents with it."
            stav "Leaves me with nothing but stone and silence."
            "He glances at the statuettes again, the weight of the memory pulling at his words."
            stav "That's when I leave it all behind."
            stav "Join the Kestrels."
            stav "Figure the battlefield is better company than an empty workshop."
            jump a1_knight_conversation_menu2

        "Exit":
            "He takes a slow, deliberate sip of the soup, savoring the warmth as it spreads through him."
            "The flickering firelight dances across his weathered face, casting long shadows that cling to the lines of his brow."
            jump a1_knight2

label a1_knight2:
    "hey"
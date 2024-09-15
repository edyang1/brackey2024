label s_a1_knight:
    $ artstyle = "fantasy"

    "He notices you before you have a chance to turn away."
    show stav hap at close_to_camera with dissolve
    "His gaze, sharp and thoughtful, settles on you with the calm focus of someone used to watching over others."
    show stav neu at subtle_breathe
    stav "A traveler?"
    "His voice is low and gravelly."
    stav "I don't see many passing through here anymore."
    show stav sup at lean_in
    "The knight raises his good arm in a welcoming gesture, though his tone carries a note of wariness."

    python:
        f_name = renpy.input("What's your name?", default = "Cassiopeia")
        f_name = f_name.strip()
        if f_name == "":
            f_name = "Cassiopeia"

    show stav neu at nod
    "He nods slightly, as if turning the name over in his mind."
    stav "Well met, [f_name]. I'm Stavros."
    stav "These parts don't offer much in the way of hospitality, but if you're in need of rest, I have room for one more."
    show stav sad at look_away
    "He glances briefly at the tombstones, his expression momentarily darkening."
    stav "I've seen enough of the dead for one day."
    show stav neu at step_forward
    "He steps away from the graves and motions for you to follow."
    stav "Come on. My home's not far."
    show stav hap
    stav "It'll be night soon, and the cold isn't something to face out here."

    show stav neu at exit_confident
    "You follow him as the sun slips lower, casting longer shadows over the road."
    "His movements are deliberate, the result of years spent adjusting to the loss of his arm."
    "The silence between you is comfortable, only broken by the distant call of some forest creature—an odd, lilting sound that echoes through the trees."
    "It is unlike anything you've heard before, a soft whine that turns into a sharp, two-toned yip, almost as if two voices are calling out at once."
    "The sound is fleeting, swallowed quickly by the wind, but it lingers in your mind, tugging at old stories of creatures said to roam these lands."

    "As you round a bend, his home comes into view—a small, unassuming cottage with smoke curling from its chimney."
    "The simple structure stands alone, with small, rounded tombstones from the cemetery nestled nearby."
    "The knight pushes open the wooden door with a nod."
    show stav sup at enter_hesitant
    stav "I'll be damned if I let anyone freeze to death on my doorstep. Come on in."

    scene fantasy_cottage with dissolve

    show stav hap at subtle_breathe
    "Inside, the warmth of the fire greets you, the comforting scent of herbs and simmering soup filling the air."
    "The walls are simple daub, washed white with plaster, with wooden beams poking through the construction material."
    "Hanging from the beams are herbs and dried meats, swaying gently with the draft from the door."
    "A bubbling pot hangs over the fire, sending out a rich, earthy aroma."
    stav "It's nothing fancy, but it'll keep the cold out."
    show stav neu at step_forward
    "He gestures for you to take a seat at the table."
    "He moves slowly, surely, to a cupboard near the chimney."
    "After taking out a plate with wooden cutlery, he sets it on the table before pouring you a cup of warm, sweet wine from a terracotta ewer sitting by the fire."
    show stav sad at look_down
    "Then, he dishes out two bowls of thick soup, the hearty smell of chestnuts, onions, and dried venison rising with the steam."
    stav "[f_name]. What are you doing out here?"

    menu:
        "I'm a traveler on a search for adventure. I've been wandering for a while now.":
            jump a1_knight1
        "I got lost in the forest. I wasn't expecting to end up here.":
            jump a1_knight1

label a1_knight1:
    show stav neu at subtle_breathe
    stav "You don't look like you're from around here, especially given how the cold seems to have taken its toll on you."
    show stav sad at look_away
    stav "These mountains can be unforgiving, and winter's only just starting to settle in."
    show stav neu at lean_in
    "He pauses, studying you for a moment."
    stav "Where are you from?"

    menu:
        "I don't know, I don't recall how I got here.":
            show stav sup at tilt_right
            stav "You mean you don't remember whence you came? And just how did you manage to get this far?"
            stav "You're lucky I found you before the wolves did."
            "You take a moment to look around his home."
            jump a1_knight_conversation_menu1

label a1_knight_conversation_menu1:
    menu:
        "Ask him about his name and trade.":
            show stav ang at lean_back
            "The man seems taken aback by your question, his brows furrowing in brief confusion. But the moment passes quickly, and he regains his composure."
            show stav neu at subtle_breathe
            "He lets out a small chuckle."
            stav "Stavros Attelides. I once led the Marquis' militia in these parts."
            "As he speaks, his voice drifts off, and you notice his gaze faltering, his eyes fixed somewhere beyond you."
            show stav sad at look_away
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
            show stav hap at lean_in
            "The man's eyes brighten for a moment, a rare spark lighting up his otherwise gruff demeanor as you mention the shield."
            stav "Ah, that old thing."
            show stav hap at subtle_breathe
            "His voice fills with pride and nostalgia."
            stav "That's the shield I carried back when I led the Kestrels—the Marquis' finest militia."
            stav "It's seen more battles than I care to remember."
            show stav neu at nod
            "He gives a low, gruff chuckle, but it's bittersweet."
            "His expression hardens for a moment as he raises the stump where his arm used to be, the humor fading from his voice."
            stav "That was before... before I lost the arm. Can't wield it anymore. Haven't touched a shield in years."
            "He sighs, a heavy sound."
            "You take a closer look at the shield, noticing its lozenge shape and the deep wear on its surface, signs of many hard-fought battles."
            "Its background is a weathered yellow, crossed by a black stripe running down the middle."
            "On one side, you see a vertical line with three tapering streaks—like a stylized pine tree."
            "The other half bears the image of a bird, painted black, its large tail feathers unmistakably those of a kestrel."
            show stav neu at look_away
            stav "The Kestrel... fitting, isn't it?"
            "He speaks softly now, his rough exterior cracking just enough to let some warmth through."
            stav "That bird—it's a fighter. Like we all were. Fast, sharp, but..."
            stav "But not invincible."
            show stav sad at look_down
            "He looks at the shield again, but this time with a quieter, softer gaze."
            "His fingers gently trace the outline of the kestrel."
            stav "This thing's all that's left of that life."
            show stav neu at subtle_breathe
            "He straightens up, the moment of softness gone as quickly as it came."
            stav "I keep it around to remind myself what it cost. Every scratch, every mark—there's a story there. Not all of them good."
            show stav sup at step_back
            "He turns away, his voice gruff again, but there's a slight crack in the facade."
            stav "Enough about the past. Doesn't do much good to dwell on it, eh?"
            jump a1_knight_conversation_menu1

        "Ask him about the cemetery.":
            show stav sad at look_away
            "The man turns his face to the window, his gaze drifting beyond the rough glass panels."
            "He shifts slightly in his chair."
            stav "That's the final resting place of the Cordean Kestrels."
            show stav sad at subtle_breathe
            "His voice takes on a reverence you haven't heard before."
            stav "My brothers-in-arms. I'm their warden now. Their caretaker."
            show stav sad at look_down
            "He pauses, eyes lingering on the graves as if he can still see them standing there, alive and ready for battle."
            show stav neu at nod
            "Then he points to the shield hung over the door, the same one he had spoken of earlier."
            stav "That's the old insignia of the regional militia. The Kestrels… we were the best."
            stav "One of the finest companies the Marquis ever had. Way back in the day."
            "There is pride in his voice, but it is tinged with something heavier—regret, or perhaps the weight of memory."
            "He turns back to you, pushing himself up from his chair with a slow, deliberate movement."
            stav "Since we're speaking of them, it's only right I honor them properly."
            "Stavros walks to the cupboard, his movements measured, as if this is a ritual he has performed many times before."
            "He pulls out a small bottle, its contents dark, and pours a portion into a cup."
            show stav neu at step_forward
            "Without a word, he makes his way to the fireplace."
            "The fire crackles softly as he tosses the liquid into the flames, which leap higher in response, casting long shadows across the room."
            stav "To your health, brothers. May you rest in peace."
            "He stands there for a moment longer, the flames reflecting in his eyes, before returning to the table."
            show stav sad at look_down
            "Noticing your puzzled expression, he lets out a low, tired chuckle."
            stav "It's an old tradition."
            stav "Among knights and military brotherhoods. We offer a glass to those who aren't here anymore... those who fell before us."
            "He pauses, then adds, almost as if to himself,"
            stav "It's the least we can do to keep their memory alive."
            jump a1_knight_conversation_menu1

        "Ask about the woodcarving implements on the far side of the room.":
            show stav hap at subtle_breathe
            "The man glances down at the scattered wood shavings beneath the bench, his lips curling into a small, crooked smirk."
            stav "That's what keeps me busy these days."
            show stav neu at nod
            stav "Ever since the militia put me out to pasture."
            "He nods toward the table, where the simple wooden cutlery lay neatly arranged."
            stav "Made all of these myself over the years. Keeps the hands busy… what's left of them, anyway."
            jump a1_knight_conversation_menu1

        "Exit":
            show stav sad at subtle_breathe
            "He sighs deeply, taking a long sip of the soup and leaning back in his chair."
            jump a1_knight_conversation_menu2

label a1_knight_conversation_menu2:
    menu:
        "Ask about the other person suffering from your same ailment.":
            show stav neu at tilt_right
            stav "He's an odd one, no doubt, but a decent sort. Stays over at an inn not too far from here."
            show stav sup at subtle_breathe
            "He pauses for a moment, as if weighing his words carefully."
            stav "Might be worth your time to seek him out. Have a chat."
            stav "Who knows—maybe there's something that can be done for both of you."
            jump a1_knight_conversation_menu2

        "Inquire more about the Kestrels he mentioned earlier.":
            show stav sad at look_away
            "Stavros leans back in his chair, settling in with a slow sip of the sweetened wine."
            "He pauses for a long time, his gaze fixed on the flames dancing in the hearth."
            "As he speaks, his voice grows softer, more reflective."
            stav "The Cordean Kestrels... we were a brotherhood, born in these mountains."
            show stav neu at subtle_breathe
            stav "Just a group of militiamen from the highlands, where the kestrels fly."
            "He pauses, as if remembering a time long past."
            stav "I joined them young, maybe seventeen, still green but eager."
            show stav sad at look_away
            "His gaze remains fixed on the mountains, as if trying to pull something from their jagged silhouettes."
            "The weight of years seems to settle over him like a heavy cloak."
            stav "We fought together for more than a decade and a half, serving under the Marquis' banner."
            stav "By the time the battle for the plateau came, I'd taken command after old Menavlios fell in combat."
            show stav sup at nod
            stav "Led the men myself... right into the storm."
            "He falls silent, his eyes no longer on the peaks but scanning the room,"
            "eventually resting on a tall piece of furniture draped in cloth in the far corner."
            "The memories seem to hang in the air between you."
            show stav sad at look_down
            stav "Now, I'm the only one left."
            "For a moment, the room feels colder, despite the fire crackling in the hearth."
            show stav sad at look_away
            "The words linger, heavy, as if the weight of the entire brotherhood rests on his shoulders."
            stav "I do what I can to keep their memory alive."
            stav "But it's not enough, is it? You bury your brothers, and what's left? Just me."
            stav "One old man trying to hold onto something that's long gone."
            jump a1_knight_conversation_menu2

        "Ask why he's chosen to stay and take care of the graveyard.":
            show stav neu at nod
            stav "After the battle at the plateau, the Marquis makes me a knight."
            stav "Calls me an 'honorable hero of the region,' and offers me a peaceful retirement—"
            "a plot of land, the means to live comfortably."
            show stav sad at look_down
            stav "A reward for all the blood I've spilled, I suppose."
            "He pauses, his tone turning bitter."
            show stav ang at shake_head
            stav "All while my comrades lay dead in the dirt."
            show stav sad at look_away
            "Stavros raises his sole hand, gesturing at the walls around him, as if they are more a prison than a home."
            stav "I refuse at first."
            stav "Tell the Marquis that four walls and a roof can never compare to the lives of the men I lost."
            stav "What good is peace when your brothers-in-arms are gone?"
            "He shakes his head, his expression hardening."
            show stav sad at look_down
            stav "But the Marquis... well, he convinces me to take it, eventually."
            show stav neu at subtle_breathe
            "There is a heaviness in his voice, and then he adds, quieter, but with conviction."
            stav "But I make one demand. My comrades—they have to come with me."
            "His gaze sweeps to the window, where the gravestones stand like silent sentinels."
            show stav sup at step_forward
            stav "I have them build this house, and with it, the cemetery."
            show stav sad at look_down
            stav "I become their guardian. Their warden."
            "He falls silent for a long moment, the weight of the years pressing down on him."
            stav "Now I wait."
            stav "Watch over them until my time comes... and I can join them, one last time."
            stav "It's the price I pay, for surviving."
            stav "For losing an arm, and all the rest of it."
            jump a1_knight_conversation_menu2

        "Ask for how long he's been practicing whittling, since he's very good at it.":
            show stav neu at subtle_breathe
            stav "That was my trade once."
            "His voice softens, a hint of nostalgia in his words."
            stav "My father teaches me when I am just a boy."
            show stav hap at nod
            stav "I spend my younger years honing the craft, day after day."
            stav "Carvings of horses, birds, mountains, you name it."
            stav "They are terrible, of course, but I keep at it."
            stav "Carving, shaping—figure it'd be my life's work."
            "He pauses, his gaze turning to the chimney, where two finely polished stone statuettes sit,"
            "their features carved in grey marble—a man and a woman."
            show stav sad at look_away
            stav "But things change."
            stav "The plague comes through, takes my parents with it."
            stav "Leaves me with nothing but stone and silence."
            "He glances at the statuettes again, the weight of the memory pulling at his words."
            stav "That's when I leave it all behind."
            stav "Join the Kestrels."
            show stav neu at nod
            stav "Figure the battlefield is better company than an empty workshop."
            jump a1_knight_conversation_menu2

        "Exit":
            show stav sad at subtle_breathe
            "He takes a slow, deliberate sip of the soup, savoring the warmth as it spreads through him."
            "The flickering firelight dances across his weathered face, casting long shadows that cling to the lines of his brow."
            jump a1_knight_conversation_menu3

label a1_knight_conversation_menu3:
    menu:
        "Head for the inn Stavros mentioned.":
            show stav neu at subtle_breathe
            "You fall into a deep sleep, the warmth of Stavros' cottage and the crackling fire lulling you into rest."

            stop music fadeout 1.0
            scene black with fade
            "... ..."
            "... ..."
            "... ..."
            "... ..."
            "..."

            play music "fantasy_casual.mp3" loop fadein 1.0
            scene fantasy_cottage with dissolve

            "Morning comes quietly. You wake to the smell of porridge cooking, and see Stavros at the fire."
            show stav neu at step_forward
            stav "Morning. Figured you'd need something before heading out."
            show stav hap at subtle_breathe
            "He sets a simple bowl of porridge on the table in front of you."
            stav "Eat up. The inn's west, past the river. You'll find it easy enough."
            show stav sad at look_away
            "You finish the meal in silence, Stavros glancing toward the window, avoiding direct eye contact."
            stav "If you're ever back this way… there's room here. Not many travelers these days."
            jump a1_knight3

        "Ask about the battle he's just mentioned.":
            show stav sad at look_down
            "Stavros' face darkens, his expression hardening as turbulent memories rise to the surface."
            stav "Years ago, the Marquis set his sights on expanding control over the western mountains."
            show stav neu at subtle_breathe
            stav "There's a vast plateau up there, less than half a day's march from here."
            stav "It's a natural stronghold, commanding the valley below."
            stav "The Marquis knew if we didn't secure it, the hamlets and villages would remain vulnerable to raids."
            stav "The gnolls had been attacking for years."
            show stav sad at look_away
            "He pauses for a moment, his eyes distant, as if weighing the past."
            stav "And truth be told, he wasn't wrong."
            stav "The Pinestripe gnolls were relentless, always descending from the hills to pillage and burn."
            stav "They were quick, using the mountains to their advantage, disappearing before we could properly retaliate."
            show stav ang at step_forward
            stav "But this time, the Marquis had had enough."
            stav "He ordered us to draw them out and crush them, once and for all."
            show stav neu at subtle_breathe
            "Stavros shifts in his seat, straightening as his voice takes on a harder edge, his military discipline rising to the surface."
            stav "Our plan was simple—at least it seemed so."
            stav "We'd march through the valley, luring them in, forcing them to commit to a fight on the open ground."
            stav "But we had another card to play."
            show stav sup at tilt_right
            stav "I sent our cavalry around the far ridge, hoping to flank them."
            stav "If we could close the pincer, we'd cut off their retreat into the mountains."
            stav "The Kestrels were leading the charge, with the rest of the infantry following behind."
            stav "We needed to hit hard and fast to secure the plateau before they could escape."
            show stav sad at look_away
            "He shakes his head, the weight of hindsight settling over him."
            stav "But the gnolls were smarter than we gave them credit for."
            show stav sad at step_back
            stav "They anticipated our cavalry's maneuver and had scouts posted on the high ground."
            stav "By the time our horsemen reached the ridge, the gnolls had already repositioned, using the rocks and narrow paths to bottle us in."
            stav "They knew the terrain better than we did."
            show stav sad at subtle_breathe
            stav "Their slingers and javelin throwers rained hell down on us from the cliffs."
            stav "Our cavalry was pinned, unable to maneuver."
            show stav sad at shake_head
            "You listen intently, feeling the weight of the battle building in his voice, as if he's reliving every step."
            stav "Our plan to cut them off had failed."
            stav "Worse still, the infantry—my Kestrels—had pushed too far ahead."
            stav "We were exposed on the plateau, waiting for the reinforcements that never came."
            stav "The gnolls attacked swiftly, waves of them pouring down from the mountains."
            stav "They didn't fight like we did."
            show stav sad at look_down
            stav "They were more fluid, breaking apart, reforming, always moving."
            stav "They hit our flanks first, trying to break our line with a mixture of fear and chaos."
            "He takes a slow breath, the memory clearly painful."
            stav "I sent my reserves to reinforce the line, trying to hold them off while our archers took positions, but it was no use."
            show stav sad at step_back
            stav "Their slingers kept us pinned, and we couldn't form up properly."
            stav "We were losing ground, losing men, and fast."
            show stav sup at lean_back
            "He pauses, taking a breath, and the weight of his next words hangs heavy between you."
            stav "I knew we couldn't hold the plateau."
            stav "I gave the order to retreat, to fall back to the entrance where we could regroup."
            stav "But the gnolls… they smelled blood."
            show stav sad at look_down
            stav "They pursued us, harrying us all the way down."
            stav "By the time the reinforcements arrived, the plateau was drenched in blood."
            show stav sad at look_away
            "He raises his arm, or what's left of it, and looks at the stump with hollow eyes."
            stav "A Pinestripe warrior struck my shield arm with an axe."
            stav "Crushed it to the bone."
            stav "They had to take it off at the shoulder."
            stav "I couldn't even carry my standard off the field."
            show stav sad at subtle_breathe
            "Stavros' gaze drifts to a corner of the room, where a piece of furniture is covered with a cloth."
            "His voice softens, but the bitterness remains."
            stav "We won the battle, but at what cost?"
            stav "I lost everything that mattered."
            stav "My brothers, my family… all gone, because of an order I gave."
            "He exhales slowly, as if trying to push the weight of it all away."
            stav "I can't shake it."
            stav "Never will."
            show stav sad at look_down
            "He turns back to you, his eyes hard again, though the sorrow lingers in them."
            stav "The Marquis offered me a reward after the victory."
            stav "Called me a hero."
            stav "Gave me a knighthood and a plot of land."
            show stav sad at look_away
            stav "I accepted… but on one condition."
            stav "My comrades, my brothers, would be buried with me."
            stav "I built this place, their graves just outside."
            stav "I watch over them."
            stav "It's all I have left."
            show stav sad at look_down
            "His gaze flickers back to the corner, where the strange, human-shaped object stands, covered in dust and neglect."
            stav "I've never put that commander's armor back on."
            stav "Haven't touched it since that day."
            show stav sad at subtle_breathe
            "He pauses, the silence thick and heavy, before he adds quietly,"
            stav "I'll watch over them until it's my turn to join them."
            stav "That's the only promise I have left to keep."
            stav "Until then, I'll help those in need… when I can."
            show stav sad at look_away
            "You feel the weight of his words, like the room itself is holding its breath."
            jump a1_knight_conversation_menu3

label a1_knight3:
    menu:
        "Thank him sincerely.":
            show stav hap at subtle_breathe
            stav "Yeah, yeah. Get moving."
            show stav neu at look_away
            stav "Take care of yourself."

            stop music fadeout 2.0
            scene black with fade
            jump s_a1_forest_minigame

        "Leave quietly, with a smile.":
            show stav neu at nod
            "You smile and nod, understanding his quiet offer."
            show stav sad at subtle_breathe
            stav "Take care of yourself."

            stop music fadeout 2.0
            scene black with fade
            jump s_a1_forest_minigame
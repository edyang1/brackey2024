label s_a1_golem:
    $ artstyle = "fantasy"

    scene fantasy_golem with fade
    play music "fantasy_casual.mp3" loop fadein 1.0
    play sound "a_fantasy.mp3" loop fadein 2.0

    "Finally, through the trees, you spot a weathered structure, sagging under the weight of moss and ivy."
    "The door is closed, though the building feels alive with a strange energy."
    "As your hand touches the door's handle, the wood seems to shift, warping and stretching unnaturally."
    "Tendrils of something—wood, metal, or perhaps something else—curl around you, pulling you inside before you can react."
    "You blink, and you're standing in the dim, dusty interior."
    "The smell of old wood and stale air mingles with the sharp tang of boiling cabbage."
    "Candles flicker weakly in the corners, casting trembling shadows across the room."
    "Shattered chairs and broken tables are scattered about, their remains little more than skeletal shapes barely clinging to form."
    "A counter sits at the far end, its shelves lined with dusty, opaque bottles."
    "The air feels heavy, almost watchful."
    "A narrow staircase draws your eye, and you ascend slowly, the wooden steps groaning under your weight."
    "The upper floor is eerily still."
    "The corridor stretches ahead, lined with rooms, each door either smashed open or hanging crookedly from broken hinges."
    "Despite the decay, the floor is oddly clean, the dust and debris swept into careful piles along the walls, leaving a clear path forward."
    "The sense of something unseen watching you grows stronger."

    i "Hey, I've never seen you before. Who are you?"

    "A sudden voice shatters the stillness, catching you off guard."
    "You stumble back a few steps, your eyes darting to a shadowy corner."
    "There, by the faint glow of a candle, sits a small figure, like a child but with an unsettling stillness, holding an open book."
    "As the initial shock wears off and your eyes adjust to the dim light, you begin to make out more details."

    "The figure's skin is a gleaming brown, almost polished, and its thin, lanky frame is made more striking by the impossibly slender proportions of its limbs."
    "Its head is round, without a visible mouth or nose, just two large, opaque black eyes that reflect the flickering candlelight."
    "The figure closes the book, standing with a strange grace, and places it on a nearby shelf."

    menu:
    "Explain how Stavros pointed you in this direction.":
        show i neu at subtle_breathe
        "The figure's eyes seem to brighten at your words, its expressionless face somehow conveying excitement."
        show i hap at nod
        i "Oh, the old knight! He's a good man, I'm glad he sent you."

    "Explain that you stumbled upon this place by accident.":
        show i sup at tilt_right
        "The figure tilts its head, its eyes narrowing slightly as if considering your words."
        show i neu at subtle_breathe
        i "Accident? That's strange. This place isn't easy to find by chance."

    "You look cold, though. Come with me!"

    show i neu at step_forward
    "Despite the lack of movement in its features, the voice is crisp and clear, as if spoken directly into your mind."
    "The figure gestures for you to follow and strides downstairs, its movements fluid and purposeful."

    "You descend the stairs after it, entering what was once the kitchen of the old establishment."
    "A cast iron pot hangs over the stove, gently steaming, while bits of vegetables are scattered around a worn table where a knife and cutting board rest."
    "The figure moves swiftly, retrieving a cup from under the counter and filling it with milk from a jug."
    "With ease, it scoops some soup from the pot into a horn bowl and places both the bowl and cup in front of you."

    i "Here. The old man always said when you're cold, you should eat and drink something warm."

    show i sup at lean_in
    "The figure hands you a bowl, then settles on the floor, watching you with its unblinking eyes, its head slightly tilted as if waiting for your reaction."

    i "So, how is it?"

    show i neu at subtle_breathe
    "You take a bite with a cracked spoon, the warmth of the cabbage and milk spreading through you."
    "There's no salt, and the overpowering taste of pepper lingers, but it's comforting in its simplicity."

    menu:
        "It's good, just needs some more adjustments.":
            show i hap at nod
            "You can't quite explain it, but the figure's face seems to brighten."
            i "Really? I'm so happy! I try cooking, but I can't taste the food and I'm always alone, so I never know if it's any good."

        "It's filling, but it could use some salt.":
            show i hap at nod
            "You can't quite explain it, but the figure's face seems to brighten."
            i "Really? I'm so happy! I try cooking, but I can't taste the food and I'm always alone, so I never know if it's any good."

        "It's... It's food, at least.":
            show i sad at look_down
            "You notice the figure's expression subtly fall, though you can't understand how."
            i "I'm sorry. I try cooking, but I can't taste the food and I'm always alone, so I never know if it's any good."

    show i neu at subtle_breathe
    i "But enough about that. What were you doing before? I could sense you were in a bad situation."
    jump a1_golem_conversation_menu1

label a1_golem_conversation_menu1:
    menu:
        "Explain how you have little memories of what led you here.":
            show i sup at tilt_right
            "The statue's eyes shift, narrowing into thoughtful slits as it listens to you, lost in contemplation."
            show i neu at subtle_breathe
            "After a moment, they return to their original shape."
            i "I get it... you're like me, huh? I can't remember much from my past either."
            show i sad at look_down
            "For a brief moment, it seems to sag, as though something unseen weighs on it."
            i "To be honest, I can't remember almost anything from before a year ago."
            i "Maybe... maybe there's a connection between your case and mine?"
            show i neu at subtle_breathe
            "It raises its gaze to the ceiling, thoughtfully stroking its chin."
            i "I'll have to look through some of the old man's notes. He might've written something relevant."
            "It pauses, studying you intently from head to toe, as if measuring something."
            i "But... you're not a golem, are you? So, I'm not sure if it's exactly the same issue. Oh!"
            show i hap at lean_in
            "It suddenly stretches out its hand toward you, eyes bright with realization."
            i "My name is Iolkos. The old man told me that's what I should say when introducing myself."
            jump a1_golem_conversation_menu1
        
        "Ask why it's alone in this building. It doesn't seem a great place to be.":
            show i sup at lean_back
            "The statue looks at you, confusion flickering in its gaze."
            show i neu at tilt_left
            "It tilts its head as though trying to raise an eyebrow—if it even had one, you reckon."
            i "What do you mean? This is my home. I like it here! It's full of books and strange little things to play with."
            i "Plus, the old man said I should stay here for now."
            show i neu at subtle_breathe
            "It lifts its arms and shrugs, a gesture that seems oddly casual for something so mechanical."
            i "Besides, I can't really leave... I mean, I *literally* can't."
            show i sup at look_down
            "It gestures toward its wrists, indicating the delicate threads attached to them."
            "When you look closer, you notice a thin filament trailing from its wrists upward."
            show i neu at tilt_left
            "Your eyes follow the threads, and they disappear somewhere into the ceiling, but their exact origin remains a mystery."
            i "These little things are great for doing all sorts of tasks, but they've got one drawback—they won't let me out."
            i "Not through the windows, and definitely not through the door. Trust me, I've tried."
            show i neu at step_back
            i "They always get tangled in the frame. Frustrating, right?"
            jump a1_golem_conversation_menu1

        "Inquire more about the old man it mentioned.":
            show i neu at nod
            i "He's the one who told me what to do here. He's also the one who collected all these books you see."
            "The golem gestures toward the bookshelves on the upper floor, extending a hand."
            "With the faintest rumble, the wooden planks shift and bend, releasing a book that slowly lowers on one of the shimmering threads connected to its limbs."
            "It catches it, flipping through the pages."
            show i neu at subtle_breathe
            i "He was a person of great knowledge—he read all these books and even more!"
            i "He's written down a lot of what he did, and where he went, in this book here."
            show i sup at tilt_right
            "Its eyes narrow slightly, forming curious, diagonal shapes as it mutters to itself."
            i "Diary? Is that what it's called?"
            show i hap at nod
            "It nods, seemingly satisfied with the word."
            i "In his diary, he says he bought this inn to have somewhere quiet to study... important things."
            i "I know because he told me. Well, sort of."
            show i sad at look_down
            "The golem's voice lowers slightly, its tone more somber."
            i "He made me, but he hasn't come back since I woke up... a year ago."
            "It flips through the pages with a strange precision, as if searching for a hidden answer."
            "You catch glimpses of the handwritten notes—symbols and words in a language unfamiliar to you, though the golem reads it effortlessly."
            "Diagrams of spheres, circles, and strange charts fill entire pages, adding to the mystery."
            show i neu at step_back
            "At last, it stops at the very end of the book."
            i "See? He says he made me, and that I'm supposed to do something for him."
            show i neu at nod
            i "I just... need to figure out what."
            jump a1_golem_conversation_menu1

        "Ask about how it managed to take you here.":
            show i neu at tilt_right
            i "Oh, that? It's something I can do pretty easily with these."
            "The golem lifts its wrists, twisting them slightly to reveal the delicate threads extending from its joints."
            "You follow them upward with your gaze, noticing how they vanish somewhere into the ceiling."
            show i neu at subtle_breathe
            i "I can use them to move things or change how they behave—inside this place and even outside."
            i "But... when I try to reach beyond the inn, it gets much harder."
            show i sup at lean_in
            "Its right hand extends toward the stove."
            "A thread detaches from the main strand, snaking out and clumsily grabbing the ladle, stirring the soup with jerky, imprecise movements."
            "Another thread reaches for the jug of milk, tipping it toward the pot with awkward care, splashing more than pouring."
            i "They're useful for a lot of things, but... they lack finesse sometimes."
            show i sad at look_down
            i "And they definitely won't let me leave."
            "For just a moment, a shadow of sadness flickers across its dark eyes before disappearing, as fleeting as it came."
            show i neu at nod
            i "But it's fine! The old man gave them to me, so I'm sure there's something I haven't figured out yet."
            i "Maybe there's something in one of the books he left behind."
            jump a1_golem_conversation_menu1

        "Exit":
            show i neu at subtle_breathe
            "He moves with careful precision, his delicate threads guiding the ladle to his lips as he takes a slow sip of the soup."
            "The faint glow of the nearby candlelight reflects off his polished skin,"
            "casting intricate patterns across his face, the threads shimmering as they catch the light."
            jump a1_golem_conversation_menu2

label a1_golem_conversation_menu2:
    menu:
        "State that maybe your memory problem may be caused by some disease you caught on the way here.":
            show i neu at subtle_breathe
            i "Well, it could be. It seems that humans and other similar species can contract diseases from all sorts of sources—water, air, food, plants..."
            "Iolkos begins rattling off an extensive list of contagion methods, each ailment sounding progressively worse."
            "Its knowledge on the subject is disturbingly thorough, but after a moment, it notices you're no longer following along and abruptly stops."
            show i sup at tilt_right
            i "Hmm, I'm guessing you haven't consumed any fermented basilisk eyes lately, so we can probably rule out ophthalmic spiral spikes."
            show i neu at subtle_breathe
            i "But it could be some other kind of disease entirely—maybe even one that hasn't been discovered yet."
            "The golem closes its eyes, falling into a deep, contemplative silence."
            "For a moment, you wonder if it has fallen asleep, but your theory is quickly disproved when it jolts up, its face lighting up with excitement."
            show i hap at lean_in
            i "I just remembered something! The old man once lent some books to the head physician at the local hospice."
            i "He might know what's wrong with you—it's definitely worth checking out!"
            jump a1_golem_conversation_menu2

        "Ask what exactly it means by 'fun'.":
            show i ang at subtle_breathe
            "The golem's expression darkens, a hint of frustration in its eyes."
            i "There's plenty of fun to be had here, you know!"
            show i neu at tilt_left
            i "There are five hundred ninety-four books on thirty-two different subjects,"
            i "and I've only read a third of them—some are even in languages I don't know yet!"
            i "There's so much to discover,"
            i "like how to make broth using horse hooves or how long sparrow beaks are if they hatch in autumn when it's cold!"
            "It launches into a tirade, painstakingly explaining why everything it does is incredibly fun and entertaining."
            "As you listen, you start to grasp that this place means more to it than the words can convey."
            "The books, the old man, the inn—they're all tied together in some deep, unspoken way for this strange being."
            "It gestures toward the cooking implements you noticed earlier."
            show i neu at nod
            i "I'm teaching myself how to cook for when the old man comes back."
            i "I've read half a dozen cookbooks and have been practicing for a month."
            i "I also try to fix things."
            show i neu at subtle_breathe
            "As it mentions this, you begin to notice a series of small repairs throughout the inn."
            "Doorframes have been mended with sawdust mixed with a dense liquid, bonding it to the wood."
            "Nails have been replaced by wooden pegs, carefully shaped to fit where the metal once was."
            "You realize it's doing its best to take care of the inn."
            "A pile of cannibalized tables and chairs lies in the corner,"
            "their parts used to replace floorboards and patch the counter."
            show i hap at lean_in
            i "Oh, and sometimes I manage to watch people while they travel and even... sort of talk to them."
            "Noticing your skepticism, the golem clarifies."
            show i neu at tilt_right
            i "Just like I sensed you were in trouble, I can feel people nearby when they aren't too far from the inn."
            i "I can shift things around, move things between places."
            show i neu at step_forward
            i "That's how I get the ingredients to practice my cooking."
            "It raises a hand, almost in defense."
            show i sup at tilt_left
            i "And of course, I leave money in place of the goods I take."
            i "The old man said that's how people trade, right?"
            show i neu at subtle_breathe
            "All of this feels like a person trying to create order in their world,"
            "struggling against chaos in an effort to build a quiet, meaningful existence."
            "The golem speaks with passion about its life here, but you can't shake the feeling that this life,"
            "this place, wasn't meant for it alone."
            jump a1_golem_conversation_menu2

        "Question it about where the old man may be now.":
            show i sad at look_down
            "The golem's expression darkens, uncertainty clouding its features."
            i "I... I don't know."
            i "I haven't seen him since I woke up."
            i "Maybe he went on one of the trips he wrote about in his diary."
            i "But... he didn't leave any instructions."
            "The sadness in its voice seems to dim the hopeful energy you've seen up to now."
            show i neu at subtle_breathe
            i "I know I'm supposed to wait for him, but I also feel like I need to do what he told me—explore both the inside and outside of the inn."
            show i sad at look_down
            "Its gaze falls, and for the first time, you see the weight of its uncertainty fully."
            i "I don't know what to do."
            i "I'd love to know when he's coming back... but I also want to find a way to walk outside with my own feet, not just through these threads."
            jump a1_golem_conversation_menu2

        "Ask for more information about the strange threads.":
            show i neu at nod
            i "I'm sure they work with my body because I can only use them to interact with things if a part of me is touching them."
            "You recall the golem always keeping its feet on the ground while manipulating the cookware with its threads."
            show i neu at step_forward
            i "But, I can also make them work outside the inn if I'm touching certain materials—like hardwood, slatestone, or metals."
            i "That's how I bring in the things I buy from the outside."
            show i sup at look_away
            "It glances up at the ceiling, then down at its hands, and finally back at you, a flicker of doubt crossing its face."
            i "You know, sometimes I wonder if they're meant to keep me in here."
            show i neu at subtle_breathe
            i "But... that wouldn't make sense, right?"
            i "The old man said that one day I'd have to go outside and see the world."
            jump a1_golem_conversation_menu2

        "Exit":
            show i neu at subtle_breathe
            "The golem's eyes study you lazily."
            jump a1_golem_conversation_menu3

label a1_golem_conversation_menu3:
    menu:
        "Head for the hospice Iolkos mentioned.":
            call a1_golem1

            stop music fadeout 2.0
            stop sound fadeout 2.0
            scene black with fade

            jump s_a1_healer

        "Explore Everdusk Valley.": 
            call a1_golem1

            stop music fadeout 2.0
            stop sound fadeout 2.0
            scene black with fade

            jump s_a1_glitch

        "Ask how it can be certain that the old man will come back.":
            show i sup at subtle_breathe
            "The golem's expression shifts from bubbling excitement to meek uncertainty as you pose your question."

            i "I... I am not. I honestly have no clue."
            show i sad at look_down
            i "The Illyrian left so many things written down for me, but not everything was meant for me specifically."
            i "Sometimes he mentions other names—names that sound like mine, but aren't."
            i "They look like other golems, but I can't find any trace of them, and I've searched this inn inch by inch."

            "It pauses, the thought seemingly weighing on it."
            show i sup at tilt_right
            i "Maybe they were my siblings? Is that what they'd be called?"

            show i neu at look_away
            "The black pearls that serve as its eyes drift away from you, scanning the ceiling and nearby walls,"
            "roaming the room once more as if searching for something unseen."
            "The action feels almost habitual, like it has done this countless times before,"
            "always searching for that missing piece, that unknown realization that might unlock the puzzle of its existence."

            show i sad at subtle_breathe
            "In that moment, you catch a glimpse of something deeper—the dismay that lingers beneath its resolve."
            "It's as if the burden of its purpose, its loneliness,"
            "has slipped through the carefully constructed facade it keeps up."

            show i neu at subtle_breathe
            "You picture this small, human-shaped creation, living out its days alone within these decaying walls,"
            "surrounded by silence and the cryptic words left behind in old notebooks."
            "Perhaps it finds some strange comfort in interpreting the vague notes of long-gone scholars,"
            "rocked to sleep, if it ever sleeps, by their wisdom, just as its master once did."

            show i neu at step_forward
            "And yet, there's a resolve in the golem—a determination that surprises you,"
            "a fierce desire to push beyond the boundaries of what you thought possible for such a creature."

            i "I know there's much the old man hasn't told me yet, but I *have* to figure it all out before he comes back."
            i "I need to understand how the world works—how people live."
            i "That's my purpose. I'm sure of it."

            show i hap at lean_in
            "Its voice rises with renewed energy, the earlier hesitation all but gone."

            i "And I *know* he'll come back. I can feel it deep inside me."
            i "When he does, I'll have done everything he expected of me, and we'll have dinner together, just like you and I!"

            show i hap at nod
            "The sudden surge of enthusiasm seems to banish the earlier dread,"
            "pushing it back into the shadows as the golem's eyes sparkle with an iridescent curiosity and intellect."
            jump a1_golem_conversation_menu3
label a1_golem1:
    "You drift into a restless sleep, the strange energy of the inn lingering in your thoughts."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with fade

    "... ..."
    "... ..."
    "... ..."
    "... ..."
    "..."

    play music "fantasy_casual.mp3" loop fadein 1.0
    play sound "a_town.mp3" loop fadein 2.0
    scene fantasy_golem with dissolve

    "Morning arrives softly, the quiet hum of threads moving through the air the first sound you hear."
    "You open your eyes to see Iolkos busy near the stove, its threads delicately stirring a pot."

    show i neu at subtle_breathe
    i "Ah, you're awake! Morning. I made some soup. Not the best for breakfast, maybe, but it's all I've got right now."
    "Iolkos sets a steaming bowl in front of you, the aroma of simple broth filling the air."

    show i neu at nod
    i "Eat up. The hospice is west, past the village. You'll find it soon enough."

    "You sip the soup, its warmth filling you, while Iolkos hovers nearby, occasionally adjusting things with its threads."
    "For a moment, it seems to hesitate, its eyes shifting slightly as if lost in thought."

    show i sad at look_down
    i "You know… if you ever come back this way, I could use the company. It's… pretty quiet here most of the time."

    show i sup at subtle_breathe
    "Its voice softens, just for a moment, before it resumes its usual bright tone."

    show i neu at nod
    i "But, of course, no pressure! Just thought I'd mention it."
    
    i "Well... I guess this is goodbye for now, huh?"

    show i sad at look_away
    "Iolkos' eyes gleam softly, the ever-present threads swirling around it as if hesitant to let go of the moment."

    show i hap at lean_in
    i "I really hope you find what you're looking for out there. I'll keep the place tidy, just in case you come back."

    "It gives a small, awkward wave, the threads fluttering slightly in response."

    show i neu at subtle_breathe
    i "Remember, the world's a big place... but I think you'll do just fine."
    i "I'll be here, learning, waiting, and maybe... maybe one day I'll step outside too."

    show i sad at look_down
    "For a brief moment, the golem's expression shifts, its eyes reflecting something deeper—a flicker of hope and longing."

    show i hap at nod
    i "Take care out there. And if you ever need a strange little inn with a strange little golem, you know where to find me!"

    "It gives you a warm, albeit clumsy smile, and with a final wave, it turns back to its tasks."
    "The soft clinking of threads and quiet hum of its world are the last sounds you hear as you step out the door."

    return
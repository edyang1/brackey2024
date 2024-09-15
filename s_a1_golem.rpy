label s_a1_golem:
    scene fantasy_golem with fade
    play music "fantasy_casual.mp3" loop fadein 1.0

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
            "The figure's eyes seem to brighten at your words, its expressionless face somehow conveying excitement."
            i "Oh, the old knight! He's a good man, I'm glad he sent you."

        "Explain that you stumbled upon this place by accident.":
            "The figure tilts its head, its eyes narrowing slightly as if considering your words."
            i "Accident? That's strange. This place isn't easy to find by chance."

    "You look cold, though. Come with me!"

    "Despite the lack of movement in its features, the voice is crisp and clear, as if spoken directly into your mind."
    "The figure gestures for you to follow and strides downstairs, its movements fluid and purposeful."

    "You descend the stairs after it, entering what was once the kitchen of the old establishment."
    "A cast iron pot hangs over the stove, gently steaming, while bits of vegetables are scattered around a worn table where a knife and cutting board rest."
    "The figure moves swiftly, retrieving a cup from under the counter and filling it with milk from a jug."
    "With ease, it scoops some soup from the pot into a horn bowl and places both the bowl and cup in front of you."

    i "Here. The old man always said when you're cold, you should eat and drink something warm."

    "The figure hands you a bowl, then settles on the floor, watching you with its unblinking eyes, its head slightly tilted as if waiting for your reaction."

    i "So, how is it?"

    "You take a bite with a cracked spoon, the warmth of the cabbage and milk spreading through you."
    "There's no salt, and the overpowering taste of pepper lingers, but it's comforting in its simplicity."

    menu:
        "It's good, just needs some more adjustments.":
            "You can't quite explain it, but the figure's face seems to brighten."
            i "Really? I'm so happy! I try cooking, but I can't taste the food and I'm always alone, so I never know if it's any good."
            
        "It's filling, but it could use some salt.":
            "You can't quite explain it, but the figure's face seems to brighten."
            i "Really? I'm so happy! I try cooking, but I can't taste the food and I'm always alone, so I never know if it's any good."
            
        "It's... It's food, at least.":
            "You notice the figure's expression subtly fall, though you can't understand how."
            i "I'm sorry. I try cooking, but I can't taste the food and I'm always alone, so I never know if it's any good."

    i "But enough about that. What were you doing before? I could sense you were in a bad situation."
    jump a1_golem_conversation_menu1

label a1_golem_conversation_menu1:
    menu:
        "Explain how you have little memories of what led you here.":
            "The statue's eyes shift, narrowing into thoughtful slits as it listens to you, lost in contemplation."
            "After a moment, they return to their original shape."
            i "I get it... you're like me, huh? I can't remember much from my past either."
            "For a brief moment, it seems to sag, as though something unseen weighs on it."
            i "To be honest, I can't remember almost anything from before a year ago."
            i "Maybe... maybe there's a connection between your case and mine?"
            "It raises its gaze to the ceiling, thoughtfully stroking its chin."
            i "I'll have to look through some of the old man's notes. He might've written something relevant."
            "It pauses, studying you intently from head to toe, as if measuring something."
            i "But... you're not a golem, are you? So, I'm not sure if it's exactly the same issue. Oh!"
            "It suddenly stretches out its hand toward you, eyes bright with realization."
            i "My name is Iolkos. The old man told me that's what I should say when introducing myself."
            jump a1_golem_conversation_menu1
        
        "Ask why it's alone in this building. It doesn't seem a great place to be.":
            "The statue looks at you, confusion flickering in its gaze."
            "It tilts its head as though trying to raise an eyebrow—if it even had one, you reckon."
            i "What do you mean? This is my home. I like it here! It's full of books and strange little things to play with."
            i "Plus, the old man said I should stay here for now."
            "It lifts its arms and shrugs, a gesture that seems oddly casual for something so mechanical."
            i "Besides, I can't really leave... I mean, I *literally* can't."
            "It gestures toward its wrists, indicating the delicate threads attached to them."
            "When you look closer, you notice a thin filament trailing from its wrists upward."
            "Your eyes follow the threads, and they disappear somewhere into the ceiling, but their exact origin remains a mystery."
            i "These little things are great for doing all sorts of tasks, but they've got one drawback—they won't let me out."
            i "Not through the windows, and definitely not through the door. Trust me, I've tried."
            i "They always get tangled in the frame. Frustrating, right?"
            jump a1_golem_conversation_menu1

        "Inquire more about the old man it mentioned.":
            i "He's the one who told me what to do here. He's also the one who collected all these books you see."
            "The golem gestures toward the bookshelves on the upper floor, extending a hand."
            "With the faintest rumble, the wooden planks shift and bend, releasing a book that slowly lowers on one of the shimmering threads connected to its limbs."
            "It catches it, flipping through the pages."
            i "He was a person of great knowledge—he read all these books and even more!"
            i "He's written down a lot of what he did, and where he went, in this book here."
            "Its eyes narrow slightly, forming curious, diagonal shapes as it mutters to itself."
            i "Diary? Is that what it's called?"
            "It nods, seemingly satisfied with the word."
            i "In his diary, he says he bought this inn to have somewhere quiet to study... important things."
            i "I know because he told me. Well, sort of."
            "The golem's voice lowers slightly, its tone more somber."
            i "He made me, but he hasn't come back since I woke up... a year ago."
            "It flips through the pages with a strange precision, as if searching for a hidden answer."
            "You catch glimpses of the handwritten notes—symbols and words in a language unfamiliar to you, though the golem reads it effortlessly."
            "Diagrams of spheres, circles, and strange charts fill entire pages, adding to the mystery."
            "At last, it stops at the very end of the book."
            i "See? He says he made me, and that I'm supposed to do something for him."
            i "I just... need to figure out what."
            jump a1_golem_conversation_menu1

        "Ask about how it managed to take you here.":
            i "Oh, that? It's something I can do pretty easily with these."
            "The golem lifts its wrists, twisting them slightly to reveal the delicate threads extending from its joints."
            "You follow them upward with your gaze, noticing how they vanish somewhere into the ceiling."
            i "I can use them to move things or change how they behave—inside this place and even outside."
            i "But... when I try to reach beyond the inn, it gets much harder."
            "Its right hand extends toward the stove."
            "A thread detaches from the main strand, snaking out and clumsily grabbing the ladle, stirring the soup with jerky, imprecise movements."
            "Another thread reaches for the jug of milk, tipping it toward the pot with awkward care, splashing more than pouring."
            i "They're useful for a lot of things, but... they lack finesse sometimes."
            i "And they definitely won't let me leave."
            "For just a moment, a shadow of sadness flickers across its dark eyes before disappearing, as fleeting as it came."
            i "But it's fine! The old man gave them to me, so I'm sure there's something I haven't figured out yet."
            i "Maybe there's something in one of the books he left behind."
            jump a1_golem_conversation_menu1

        "Exit":
            "He moves with careful precision, his delicate threads guiding the ladle to his lips as he takes a slow sip of the soup."
            "The faint glow of the nearby candlelight reflects off his polished skin,"
            "casting intricate patterns across his face, the threads shimmering as they catch the light."
            jump a1_golem_conversation_menu2

label a1_golem_conversation_menu2:
    "hello world"
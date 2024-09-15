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
    "You took a moment to look around his home."
    jump a1_conversation_menu

label a1_conversation_menu:
    # Define flags for menu options
    define asked_about_man = False
    define asked_about_shield = False
    define asked_about_cemetery = False
    define asked_about_woodcarving = False

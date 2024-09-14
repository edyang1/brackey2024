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
    stav "These parts don’t offer much in the way of hospitality, but if you’re in need of rest, I have room for one more."
    "He glanced briefly at the tombstones, his expression momentarily darkening."
    stav"I’ve seen enough of the dead for one day."

    "He stepped away from the graves and motioned for you to follow."
    stav "Come on. My home’s not far."
    stav "It’ll be night soon, and the cold isn’t something to face out here."
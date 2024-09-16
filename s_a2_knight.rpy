label s_a2_knight:
    $ artstyle = "cyber"

    $ renpy.music.set_pan(0, 0)

    scene black
    play music "cyber_suspense.mp3" loop

    python:
        c_name = renpy.input("ENTER YOUR ALIAS", default = "Ca55ioP0X")
        c_name = c_name.strip()
        if c_name == "":
            c_name = "Ca55ioP0X"

    "READY?"

    scene cyber_fighter with fade

    "You find yourself in the heart of a gritty neon-lit alleyway. A gang of cyber-enhanced thugs has you pinned down."
    "Sparks fly as bullets ricochet off the metal walls around you."
    "Your neural interface starts buzzing, calculating your chances of survival."
    "Time slows for a split second as you analyze the battlefield."
    "You spot the leader of the gang: a towering figure with a glowing red visor,"
    "his augmented limbs crackling with electricity. This is going to be tough."

    menu:
        "Take a shot!":
            "You peek out from behind cover and fire a quick shot. The bullet connects,"
            "hitting the gang leader square in the chest, sending sparks flying from his armor."
            "He growls, taking a step back but still standing strong."
            "You reload quickly, but the rest of the gang begins advancing toward you."
            "Before you can line up another shot, one of the thugs catches you off guard with a blow to the ribs."
            "The pain shoots through your side, and you stumble backward, gasping for breath."

        "Take Cover":
            "You dive behind a pile of metal crates, bullets whizzing over your head."
            "The crates rattle as they take the brunt of the fire."
            "The gang leader motions to one of his crew members, signaling them to flank you."
            "Before you can react, a stray bullet grazes your arm, sending a sharp pain down your side as blood starts to trickle down."
            "You grit your teeth, realizing you'll need to make a move fast."

        "Dodge and Move":
            "You roll to the side just as a barrage of bullets slams into the spot where you were standing."
            "Your reflexes save you from the worst of it, but the gang leader isn't slowing down."
            "He draws a massive energy weapon from his back, charging it up with a hum of power."
            "As you dodge again, a thug catches you with a punch to the side, knocking the wind out of you."
            "You stumble, feeling the impact reverberate through your chest."

    "The gang leader raises his energy weapon, and you can feel the heat radiating from it even at this distance."
    "You need to act fast."

    menu:
        "Shoot again!":
            "You fire another round, this time hitting the gang leader's arm. The energy weapon clatters to the ground, useless."
            "He lets out a roar of frustration, sparks flying from his wounded arm."
            "But before you can celebrate, the remaining gang members start advancing aggressively."

        "Take cover again!":
            "You press yourself against the cold metal wall of the alley, waiting for the right moment."
            "The gang leader yells at his men to keep firing, but their shots go wide, ricocheting off the nearby walls."
            "You realize the only way out is to take down the leader quickly."

        "Charge forward!":
            "With a burst of adrenaline, you rush straight at the gang leader."
            "His eyes widen in surprise as you knock him off balance with a powerful strike to his torso."
            "He staggers backward, momentarily stunned, but the rest of the gang is still closing in."

    "The gang leader is reeling, but his crew is still on the offensive. You need to make your final move."

    menu:
        "Finish the leader off with a final shot.":
            "You aim carefully and fire the last bullet, hitting the leader right between the eyes."
            "He collapses to the ground, his red visor flickering as the light fades from his body."
            "The remaining gang members hesitate, seeing their leader fall, and begin to retreat into the shadows."

        "Escape while the gang is distracted.":
            "With the leader temporarily out of commission, you seize the opportunity to slip away."
            "You sprint down the alley, your boots slamming against the pavement as the gang's shouts fade behind you."
            "You disappear into the city, the chaos of the shootout left behind."

    "The fight is over, and you're left standing in the quiet aftermath, the scent of burnt circuitry still hanging in the air."

    stop music fadeout 2.0

    stan "Nice shooting, kid."

    play music "cyber_casual.mp3" loop fadein 1.0

    "The voice comes from behind you, deep and gravelly."
    "You turn, spotting a grizzled man standing at the edge of the alley."
    
    show stan neu at enter_slow
    "His cybernetic arm gleams in the neon light, the red glow of his ocular implant fixated on you."
    "It's Stan, an older fighter with more than his share of battle scars,"
    "someone who's clearly seen the worst the city has to offer."

    show stan hap at nod
    stan "Didn't think you'd make it out in one piece, to be honest."

    "He gives a dry chuckle, his lips curling into a smirk as he walks over, surveying the damage with a casual glance."
    
    show stan neu at subtle_breathe
    "His metal fingers tap rhythmically against his belt."

    stan "Most rookies in Cyberdusk Sector don't last long when they start picking fights with the wrong people."
    stan "But you… you've got potential."
    stan "Stupid and reckless, maybe, but potential nonetheless."

    "You catch your breath, wiping some blood from a small wound on your cheek."
    "The tension in your muscles begins to fade, replaced by a sense of cautious relief."

    stan "Tell you what."

    show stan neu at step_forward
    "Stan reaches into his pocket and pulls out a black metal card with an insignia—"
    "a cog with three rails converging at its center. He flicks it toward you with a sharp motion, and you catch it midair."

    show stan hap at nod
    stan "Why don't you come down to the Cherub? We could use someone with your skills."
    stan "Plus, you look like you could use a drink."

    "You glance at the card in your hand. It feels heavier than it should,"
    "the weight of something much larger than just an invitation."

    stan "Ever been? It's the kind of place that's rough around the edges but..."
    stan "if you're looking for work or a little less trouble finding you, it might be just the place you need."

    show stan neu at lean_in
    "He starts walking toward the end of the alley, pausing only to turn back and give you a knowing look."

    stan "You've got that look in your eyes. That 'I-don't-know-what-I'm-doing-here' look."
    stan "Trust me, kid, we've all been there. So come by the Cherub. If nothing else, it's better than bleeding out in some alley."

    stan "Kid, what do I call you?"
    stan "... ..."
    
    show stan sup at tilt_right
    stan "[c_name], huh? Not bad. Memorable."

    "You watch as Stan's figure disappears into the neon-lit haze of the city,"
    "leaving you alone with the quiet hum of distant street noises."
    
    "You make your way through the twisting streets,"
    "the weight of the card in your pocket reminding you of the strange turn your night has taken."
    "Soon, you find yourself standing before the Cherub, a dimly lit bar nestled between towering buildings."
    "Neon signs flicker overhead, the logo of a winged figure barely visible through the haze of the city's lights."
    "The door creaks open, and the noise of conversation and the clinking of glasses spills out. You step inside."
    "..."

    play sound "a_club.mp3" loop fadein 2.0

    stan "You look like you could use something to drink."

    show stan neu at nod
    "He taps the counter with three fingers, and the bartender, a girl with a bright green braid, responds almost instantly, her hair swaying with the movement."
    
    "\"What's your poison, Stars?\" she chimes, her voice light but confident."
    
    "The man raises two fingers, his expression relaxed but unreadable."
    
    stan "Get this fellow a Nine Mills, and stick it on my tab."

    show stan neu at subtle_breathe
    "Dahlia nods, flipping a glass in the air with her left hand, catching it mid-flight with her right. It's clear she's done this a thousand times."
    
    "She folds beneath the counter, producing several bottles and an assortment of mixing tools, her hands moving with a practiced ease."
    
    "What happens next is almost like a performance—bottles flipping, twirling, the liquids measured perfectly as if they danced to a silent rhythm."
    
    "Finally, the concoction takes form in the glass, the vibrant blue liquid shimmering under the bar's neon light."
    
    "She finishes with a perfect square of blue citrus wedged on the rim, passing the drink over with a sly smile."

    "\"Nine Mills, extra strong. On the house,\" she winks."

    show stan hap at nod
    "Stars lets out a bitter laugh, shaking his head as he raises his glass."

    stan "You shouldn't spoil an old man like this, Dahlia."

    "He raises his glass to yours, the metal clinking softly in the dim light."

    stan "To luck and a serene life."

    "The irony in his voice lingers for a moment before he grumbles under his breath."

    show stan sad at look_down
    stan "Yeah, I wish."

    "He downs the drink in one go, his expression unchanging as the liquid disappears. You bring your glass to your lips, hesitating for just a second."

    "The powerful scent of lemon and alcohol assaults your senses, and as you take a sip, the burn hits you hard—sharp and biting, your throat feeling as if it's been stabbed with heat."

    show stan neu at subtle_breathe
    stan "You don't belong here, do you?"
    stan "I happen to know another person who doesn't belong here either."
    stan "You'll get along like a processor and a calculation core."

    jump a2_knight_conversation_menu_1

default stan_about_convo = False
default stan_cherub_convo = False
default stan_gear_convo = False
default stan_symbol_convo = False

label a2_knight_conversation_menu_1:
    menu:
        "Ask for more information about him." if not stan_about_convo:
            $ stan_about_convo = True

            "The man shifts his weight on the stool, turning to face you."
            "You notice a half cape draped over his left shoulder, covering the stump where his arm once was."
            
            show stan neu at subtle_breathe
            stan "They call me Stars around here. Full name's Stephen Hatterlode, but no one uses it anymore."
            
            show stan neu at lean_in
            "Now that he's turned toward you, you can clearly see the various pieces of gear strapped to his body."
            "The most notable are the white plastic auto-injectors lined along his belt and a worn pistol holster on his right thigh."
            "His face is deeply lined, his skin rough and weathered like old fabric."
            "His hair, streaked with white in more places than one, adds to his worn, battle-hardened appearance."
            "You can't help but notice the stark contrast between him and the younger patrons around the bar."
            "Most of them don't look a day over twenty-five, while Stars seems well into his thirties, if not older."
            
            show stan sup at tilt_right
            "He catches your observation and smirks, a knowing glint in his eye."
            stan "There's an old saying in the Eisenbahn: 'Pity the old in a trade where they die young.'"
            stan "Guess I'm lucky—or cursed—depending on how you see it."
            
            show stan sad at look_down
            "His words hang in the air, not filled with dread but with a quiet resignation."
            "Your curiosity piques as you glance around, taking in the crowd."
            "Everyone here, men, women, even teens, is armed to the teeth with some form of weaponry."
            "It's clear now—they're all mercenaries."
            jump a2_knight_conversation_menu_1

        "Ask about the Cherub. The clientele don't seem very diverse." if not stan_cherub_convo:
            $ stan_cherub_convo = True

            "The man chuckles softly."
            
            show stan hap at nod
            stan "Of course, it isn't. We're all mercenaries here, from the greenest punk to the seasoned veterans."
            
            "He raises his maimed arm, a wry smile tugging at the corner of his mouth."
            show stan hap at lean_back
            stan "Or chopped veterans, I should say. Not much seasoning left to do here."
            stan "Might as well throw myself into the pot and call it a day."
            
            "You notice that when you mentioned the look of the crowd, his demeanor shifted."
            "There's more behind his words than he's letting on."
            
            show stan neu at step_back
            "His face relaxes a little, and he almost lights up as he takes another sip of his Nine Mills."
            stan "The rest of these kids... They've still got a lot to learn before they make it as mercs in this place."
            stan "Most of them have never set foot outside the middle levels of the Sector."
            stan "Let alone gotten the kind of experience it takes to secure a corporate trooper contract."
            
            show stan sad at look_down
            "He sighs, shaking his head slightly."
            stan "But they won't shut up about how good they are."
            
            show stan sup at tilt_left
            stan "None of them has the sense to ask the older folk how this business really works."
            
            show stan hap at nod
            "He gives you a pointed look, the corners of his eyes crinkling with a faint smile."
            stan "They could learn something from you."
            jump a2_knight_conversation_menu_1

        "Mention that his gear looks impressive." if not stan_gear_convo:
            $ stan_gear_convo = True

            show stan neu at nod
            stan "This stuff cost me a fortune, but it was credits well spent."
            stan "High-density polymer ballistic plates with a nanotubular carbon rod lattice as the base."
            stan "Even has an EMP dampener and an IR countermeasure."
            stan "Toys straight from Zhang Fei Defence Solutions."
            
            "He taps a finger on the chest plate, the sound echoing slightly in the noisy bar."
            show stan neu at step_forward
            stan "This gear's kept me alive more than once when the bullets started flying."
            
            show stan neu at look_down
            "You notice silver splashes across parts of the chest plate, chipped paint revealing the wear and tear."
            "Some of the damage is more recent, while other spots show signs of careful maintenance."
            "It's clear this armor has seen action."
            jump a2_knight_conversation_menu_1

        "Point out the strange symbol everyone seems to have." if not stan_symbol_convo:
            $ stan_symbol_convo = True

            "The man reaches for a pocket inside his shirt and pulls out a jet-black plastic card."
            "Stamped on it in gold is the same symbol you noticed earlier—three rails converging into a cog,"
            "though here it's more crisp and stylized."
            
            show stan neu at subtle_breathe
            stan "That's the symbol of the Eisenbahn."
            stan "Everyone you see here, even sweet Dahlia behind the counter, is part of the collective."
            stan "If you're hanging around the Cherub, you're either in the organization or at least lingering near it."
            stan "Not much different from you or me."

            "As he mentions Dahlia, you turn to look at her."
            "She's arranging bottles on the far side of the counter, her back to you."
            "Her bright orange shirt peeks out from beneath a black waistcoat, and her emerald braid sways with her movements."
            "A silver hairclip with three prongs ending in a ridged circle holds the braid in place."

            show stan hap at nod
            stan "When you officially join the organization, they give you one of these."
            
            "He raises the card again, showing it to you."
            
            show stan neu at lean_in
            stan "It means you handle the jobs organized here—unless you're doing other things,"
            stan "like sourcing contracts or providing hardware."
            jump a2_knight_conversation_menu_1

        "Change the subject.":
            jump a2_knight_conversation_menu_2

default stan_person_convo = False
default stan_org_convo = False
default stan_corp_convo = False
default stan_corp_name_convo = False

label a2_knight_conversation_menu_2:
    menu:
        "Ask for the name of the other person who doesn't belong." if not stan_person_convo:
            $ stan_person_convo = True

            "Stars takes another drink, his eyes drifting for a moment before he answers."
            
            show stan neu at subtle_breathe
            stan "There's someone I heard about during one of my last gigs."
            stan "I'm owed a favor, so it wouldn't be an issue if I sent you over there."
            
            "He picks up a slim black device, similar to the one you found earlier."
            "The screen glows with a soft blue hue as his fingers tap across it, writing something."
            
            show stan neu at look_down
            stan "The place isn't too far."
            stan "I've sent a message ahead. They'll expect you soon enough."
            
            show stan neu at lean_in
            "His eyes flick back to you, studying your expression."
            stan "The guy's cautious, but just like you, his memory tends to fail him now and then."
            stan "Maybe you two can help each other piece things together."
            jump a2_knight_conversation_menu_2

        "Inquire more about this organization." if not stan_org_convo:
            $ stan_org_convo = True

            "The man stretches his remaining arm, massaging his neck."
            
            show stan neu at subtle_breathe
            stan "It's a collective of mercenaries and other criminals moving about the underworld."
            stan "Difference is, you won't find any screwhead running on synth-comps or back-alley street punk trying to score big here."
            stan "We do things differently."
            
            show stan neu at step_back
            stan "We vet applicants thoroughly before they get a chance to call themselves members of the Eisenbahn."
            stan "Our name's a guarantee of quality, and all the contract fixers and middlemen know that."
            stan "Taking on the wrong folk would hurt our reputation, and bad reputation's bad for business, you know?"

            "He grabs the glass, lifting it toward his face as he points with his index finger across the club."

            show stan sup at tilt_right
            stan "Those guys over there? They know it. That's why they're here all the time."

            "You follow his gaze to a table where four people sit, their faces lit by the blue glow of large tablets,"
            "projecting square screens just above their displays."
            "They're dressed differently from the mercenaries—suits in varying shades of gray and black,"
            "adorned with high-end accessories."
            "No guns on them, only sleek communication devices and earpieces."
            "They look like they're practicing a different kind of trade."

            show stan hap at nod
            stan "Those are the contract fixers."
            stan "They broker deals from up high, down to the people pulling triggers and taking punches."

            show stan sad at look_down
            stan "Almost as bad as the muscle for hire, but less likely to stab you in the back. Truth be told."
            jump a2_knight_conversation_menu_2

        "Question him about the corporation he mentioned earlier." if not stan_corp_convo:
            $ stan_corp_convo = True

            show stan neu at nod
            stan "The ZFDS, huh? That's a major player in the arms industry. They handle private security too."
            stan "I've worked with them a few times over the years."
            stan "Pay's solid, and they offer discounts on gear."
            stan "Not bad... until you realize they cut corners with the folks they hire."
            stan "Cheap labor means headaches for people like me."

            "Stars scratches a spot on his armor, as if the memory irritates him."

            show stan neu at step_forward
            stan "See those two over there?"

            "He gestures behind him, pointing toward a man and a woman seated at a nearby table."

            "The man has a missing left leg, replaced by a sleek cybernetic prosthesis, while the woman is busy tinkering with a cyberarm."

            show stan sad at look_down
            stan "They were on the wrong end of that hiring policy."
            jump a2_knight_conversation_menu_2

        "Ask for clarification about the name of the organization. It sounds weird." if not stan_corp_name_convo:
            $ stan_corp_name_convo = True

            show stan neu at subtle_breathe
            stan "I have no idea what it means."
            stan "It's not a local name, that's for sure. Came from a guy out of West Germany years ago."
            stan "He used to be a military officer, or at least that's what the rumors say."
            stan "No one knows the whole story."

            "Stars shrugs his shoulders, clearly unconcerned with the mystery."

            show stan neu at nod
            stan "From what I've picked up over the years, he showed up after the First Corporate War."
            stan "Pulled together the scraps of all those scattered corporate trooper militias."
            stan "Somehow, he got them to agree to work together, and that's how the Eisenbahn was born."

            "He taps the card with the symbol."

            show stan neu at lean_in
            stan "The symbol? Yeah, that was his idea too."
            stan "Maybe it's got something to do with trains."
            jump a2_knight_conversation_menu_2

        "Change the subject.":
            jump a2_knight_conversation_menu_3

default stan_backstab_convo = False

label a2_knight_conversation_menu_3:
    menu:
        "Ask more about the life he's been talking about. Why the backstabbing?" if not stan_backstab_convo:
            $ stan_backstab_convo = True

            "He laughs bitterly, almost amused by your question."

            show stan hap at lean_back
            stan "Why that? Take a look around."
            stan "Do you really think any of us is trustworthy? Go on, take a good look."

            "You shift your gaze to the patrons hanging around the tables and the counter."
            "Dahlia, the bartender, is pouring a drink for a man who's barely conscious, slumped over his stool."

            "On the far side of the bar, contract brokers sit behind two imposing mercenaries with even more cybernetic augmentations than the rest."
            "Their hands glide over spreadsheets, eyes fixed on floating holographic screens,"
            "scanning information, making deals with the efficiency of machines."

            "You glance at the regulars, none of whom look unprepared."
            "They're not relaxed either, always on edge, just like Stars sitting next to you."

            "Hatterlode motions to his missing arm."

            show stan sad at look_down
            stan "In this life, you don't trust anyone. The moment you do, you're done for."
            stan "Most pay for it with their lives."
            stan "Me? I just had to pay with an arm this time."

            show stan neu at subtle_breathe
            "He downs his drink in one gulp, and you see Dahlia already preparing another one."

            show stan neu at nod
            stan "Trust makes you weak. Vulnerable. In the underworld, that's a death sentence."
            stan "The moment someone sees you as easy prey, they'll strike."
            stan "Happened to me once. Lucky to be sitting here talking to you now."

            "He watches Dahlia mix the drink, his eyes narrowing slightly."

            show stan neu at lean_in
            stan "She was a young mercenary. Reminded me of myself, so I cut her some slack."
            stan "Trained her, mentored her, gave her a chance when others wouldn't."
            stan "She was skilled, no doubt. But I got soft. Trusted her too much."

            show stan sad at look_down
            "He lets out a slow, bitter laugh."

            stan "Last job we did together, I let her secure the escape route."
            stan "Turns out, she double-crossed us. Took a second job on the side with the Marshani smugglers."
            stan "Got double the pay for selling us out."

            "He motions to his missing arm again, the scars telling the rest of the story."

            show stan neu at subtle_breathe
            stan "I made it out, barely. Medtech had to amputate the arm."
            stan "Smart girl, though. She hasn't shown her face around here since."

            show stan hap at nod
            "He chuckles again, the bitterness cutting through."

            stan "Smart indeed."
            jump a2_knight_conversation_menu_3

        "Head for the address he's given you, to visit the other person having issues with his memory.":
            jump a2_knight_conversation_menu_4

label a2_knight_conversation_menu_4:
    "You decide it's time to leave. You thank Stars for the drink and the conversation, offering to return the favor."

    show stan hap at subtle_breathe
    "He waves it off immediately, a tired smile crossing his face."

    show stan hap at nod
    stan "Don't worry about it. Just watch your back out there."
    stan "Also, word of advice. You should probably see a medtech."

    "You take a mental note of the address he gave you and head toward the exit."

    show stan neu at lean_in
    "As you enter the vehicle, you input the location,"
    "only to be surprised when the system informs you that the address is already stored."

    "The car hums to life, engines purring softly, and you're on your way."

    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene black with fade
    jump s_a2_android
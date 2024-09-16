label s_a1_healer:
    $ artstyle = "fantasy"

    scene fantasy_healer with fade
    play music "fantasy_casual.mp3" loop fadein 1.0
    play sound "a_town.mp3" loop fadein 2.0

    "The moment you step inside the hospice, the warmth hits you like a wave, pushing back the bitter cold that had settled deep into your bones."
    "The room is long and narrow, lined with simple wooden beds draped in rough, woolen blankets."
    "Braziers at either end of the room glow faintly, their embers casting a soft, flickering light that dances along the stone walls."
    "The air is thick with the scent of herbs—pine, sage, and something faintly floral—mixing with the tang of heated metal from the braziers."
    "It feels both comforting and strange, like a place caught between life and death."
    "At least a dozen beds line the walls, and while many are empty, a few are occupied by figures swathed in blankets."
    "Some stir and groan in their sleep, while others lie unnervingly still."
    "You're ushered to one of the few empty beds near the far end of the room, where the light is dimmer and the smell of herbs stronger."
    "The bed creaks slightly as you sit down, the mattress beneath you little more than thin padding over a wooden frame,"
    "though the warmth from the braziers seeps into the fabric, making it bearable."
    "The room is quiet, save for the occasional cough from the sick and the soft murmur of healers tending to the patients."
    "You spot a few figures dressed in pale blue robes moving between beds, their steps soundless against the worn stone floor."
    "They work efficiently, yet there's an air of fatigue hanging over them, as though they've been performing these same tasks day after day without rest."
    "You notice shelves along one side of the room, crowded with glass jars and faded tomes, their spines cracked with age."
    "Bundles of dried herbs hang from the ceiling rafters, swaying slightly in the heat rising from the braziers."
    "You've barely had time to take in your surroundings when a slender figure approaches, his footsteps soft but deliberate."
    "His pale ashen hair almost blends into the gray walls, and his eyes—sharp, yet distant—meet yours with a practiced detachment."
    "He carries a small, weathered box under one arm, and without a word, he pulls up a stool beside your bed."
    
    show cah neu at enter_confident
    cah "Well then, let's see what mess you've dragged yourself into this time."
    
    "He sighs, setting the box on the floor with a soft clink, before turning his attention to you, the air of professionalism never leaving his movements."
    
    show cah neu at subtle_breathe
    cah "Well then, let's see what mess you've dragged yourself into this time."
    
    "His voice carries a note of weary disinterest, but his hands move with practiced efficiency as he places a small, weathered box of tools beside your bed."
    "The tools clink faintly as they settle, and Caharel sighs, more out of routine than exasperation."
    
    show cah neu at look_down
    cah "Tell me, what exactly happened?"

    menu:
        "I was traveling along the road when exhaustion took over.":
            show cah neu at lean_back
            cah "Ah, yes, wandering into the cold. A choice neither wise nor brave."
            show cah neu at shake_head
            cah "It's astonishing what people are willing to risk for the illusion of adventure."
            
            "He doesn't look up as he speaks, his hands already moving with quick, methodical precision as he begins his examination."
            "You feel the cool touch of metal against your skin as Caharel inspects your ears, then your mouth, his strange, intricate tools revealing his sharp attention to detail despite the dismissive tone of his words."
            
            "There's a professionalism in his movements, but it's distant, as though you're just another patient in a long, endless line. He's not unkind, just... detached."
            
            show cah neu at subtle_breathe
            cah "Still, you'll be fine. A few days' rest and you should be right as rain."
            
            # Caharel pauses, noticing something about the player.
            show cah sup at lean_in
            cah "You don't look familiar."
            "You tell him your name, and he nods, though his expression remains unreadable."
            show cah neu at nod
            cah "Nice to meet you, [f_name]. I'm Caharel."

        "It was too cold, I thought my time had come.":
            show cah neu at lean_back
            cah "Ah, yes, wandering into the cold. A choice neither wise nor brave."
            show cah neu at shake_head
            cah "It's astonishing what people are willing to risk for the illusion of adventure."
            
            "He doesn't look up as he speaks, his hands already moving with quick, methodical precision as he begins his examination."
            "You feel the cool touch of metal against your skin as Caharel inspects your ears, then your mouth, his strange, intricate tools revealing his sharp attention to detail despite the dismissive tone of his words."
            
            "There's a professionalism in his movements, but it's distant, as though you're just another patient in a long, endless line. He's not unkind, just... detached."
            
            show cah neu at subtle_breathe
            cah "Still, you'll be fine. A few days' rest and you should be right as rain."

        "It was just an accident. I tripped.":
            show cah sup at tilt_left
            cah "Of course it was. It's always an accident, isn't it?"
            "He lets out a soft chuckle, almost to himself, though it carries no real warmth."
            show cah neu at subtle_breathe
            cah "Funny how accidents tend to land people right on my doorstep."
            
            "With practiced ease, he opens his weathered toolkit and begins the examination."
            "His touch is clinical, professional, but there's a noticeable distance—like someone who's long since stopped being surprised by the people who end up in his care."
            
            "The tools he uses are strange, foreign in design, gleaming faintly in the dim light."
            "Caharel works with sharp precision, his face calm, though something in his eyes betrays a deeper weariness."
        
            show cah neu at subtle_breathe
            cah "You'll be fine. Just some exhaustion and bruising. A few days' rest and you'll be back on your feet."       

    "He pauses then, something in your appearance catching his eye. His hand, previously so steady, hovers for a moment in the air, and he fixes you with an intense gaze."    
    show cah sup at lean_in
    cah "You don't look familiar."
    "You tell him your name, and he nods, though his expression remains unreadable."
    show cah neu at nod
    cah "Nice to meet you, [f_name]. I'm Caharel."
    cah "Any questions about your treatment? Any questions at all, really."
    jump a1_healer_conversation_menu1

default healer_plague_convo = False
default healer_mentor_convo = False
default healer_calm_convo = False

label a1_healer_conversation_menu1:
    menu:
        "What do you ask Caharel?"
        "What can you tell me about the plague? Or the kind of work you do here?" if not healer_plague_convo:
            $ healer_plague_convo = True

            "Caharel's fingers pause over the instruments in his hands, and for a moment, his eyes narrow, as if he's considering whether to give you a proper answer or just brush it aside."
            "Then, he lets out a breath, a slow, controlled exhalation."

            show cah neu at subtle_breathe
            cah "The plague? Yes, it's been and gone. Took more than it left, I suppose."
            
            "He offers a small, almost mechanical smile—polite, practiced, but empty."
            show cah hap at lean_back
            "It doesn't reach his eyes, which remain cool, detached, as if recalling the events like he's reading from a dry medical text."

            show cah neu at look_down
            cah "We saved as many as we could. But death..."
            cah "...death is insistent. You can't negotiate with it. You can't outthink it or overpower it."
            "No matter how skilled you are, it's always waiting."

            "His hands move again, adjusting your blanket, checking your pulse with clinical precision."
            show cah neu at subtle_breathe
            "His touch is efficient but distant, like he's performing a task he's done thousands of times before, without feeling."

            cah "We tried, of course. Xantos, my mentor, and I."
            cah "There were moments, brief moments, when we thought we could turn the tide."
            cah "But the truth is, medicine isn't magic. We couldn't save everyone."

            show cah neu at shift_left
            "There's a brief flicker of something behind his calm exterior—regret, or perhaps something darker."
            "But it vanishes almost as quickly as it appears, swallowed up by his well-practiced detachment."

            cah "People prefer to see me as some kind of savior. It's easier for them, I suppose."
            show cah sup at tilt_left
            cah "Easier than facing the truth—that sometimes, survival isn't in our hands at all."
            cah "They want to believe that skill alone can keep death at bay."

            show cah neu at look_down
            "His smile fades entirely, and there's a hollowness in his gaze,"
            "as if the weight of all the lives lost is something he's long since stopped carrying—"
            "or perhaps he's buried it deep inside, where it can't reach him anymore."

            show cah neu at subtle_breathe
            cah "They don't like to think too much about the cost of being saved."
            cah "The cost to them, the cost to me. After all,"
            cah "if you start thinking about what it really takes to stand on the edge between life and death, you might not want to face it at all."

            show cah neu at lean_back
            "He leans back slightly, studying you for a moment longer than necessary, his expression unreadable."
            "His hands are still now, resting lightly in his lap, the tools lying forgotten beside him."

            cah "I've watched too many people slip away, one breath at a time, while we tried to keep them tethered to life."
            cah "It does something to you after a while. You start seeing people as... fragile. Just a few heartbeats from the end."

            show cah sad at look_down
            "His voice softens, almost as if he's talking to himself."
            
            cah "You stop feeling it after a while. Not the way you should. And maybe that's the price."
            cah "You can save a life, but you lose a little of yourself each time."

            show cah neu at subtle_breathe
            "He falls silent, staring at nothing for a moment before his gaze refocuses on you."
            "Whatever vulnerability had slipped through his words vanishes, replaced by his usual calm detachment."

            cah "But you're not here for philosophy. You'll be fine. A little rest, and you'll be on your way."
            jump a1_healer_conversation_menu1

        "Tell me about your mentor. About Xantos." if not healer_mentor_convo:
            $ healer_mentor_convo = True

            "Caharel's movements slow for a moment, his hand hesitating over the tools on the tray beside him."
            "His sharp eyes grow distant, as if reaching back to a memory he's not sure he wants to revisit."

            show cah sup at look_up
            cah "Xantos… now there was a man who believed in the impossible."

            show cah neu at subtle_breathe
            "His tone softens, the usual edge in his voice replaced by something else."
            "Respect? Perhaps even admiration."
            "But whatever it is, it's fleeting, like a shadow passing over his face before it disappears."

            show cah hap at lean_in
            cah "He had this unwavering belief that no illness was beyond his reach, no life too far gone to save."
            cah "He used to say that if you can study hard enough, learn enough, there's always a way."

            "Caharel lets out a quiet, humorless chuckle, but there's no real warmth in it—just a bitter acknowledgment of his mentor's idealism."

            show cah neu at lean_back
            cah "He stretched his knowledge to its very limits."
            cah "I've never seen someone fight so hard for people he barely knew."
            cah "Day after day, he worked himself to the bone, chasing answers that didn't exist, hoping to save them."
            cah "But in the end..."

            show cah sad at look_down
            "He pauses, his eyes narrowing slightly as his voice drops."

            cah "...in the end, the plague didn't care."
            cah "It took him too."
            cah "Took him like it took everyone else."
            cah "His brilliance, his determination… none of it made a difference."
            cah "Death doesn't care how skilled you are."

            show cah neu at subtle_breathe
            "The flicker of emotion vanishes as quickly as it appeared, and Caharel's expression hardens again."
            "He turns away from you, busying himself with the instruments on his tray, his fingers moving with cold precision."

            cah "Now I run this hospice."

            "His voice is matter-of-fact, devoid of the reverence or passion you might expect when speaking of such responsibility."
            show cah neu at step_back
            "His hands work with the tools, but it feels like more of a reflex than a labor of love,"
            "as though the motions have become automatic after years of repetition."

            cah "The people here—they're grateful, of course."
            cah "They see me as some kind of successor to Xantos, a healer who can work miracles just like he did."
            cah "But the truth is…"

            show cah sup at lean_in
            "He pauses, the tools in his hands stilling for just a moment, his gaze fixed on the table in front of him."

            cah "The truth is, I don't care for their gratitude."
            cah "Not anymore."

            "He resumes his work, his hands moving with their usual efficiency, but there's a coldness to his actions now, a sense of distance."
            show cah neu at subtle_breathe
            "His skill is undeniable, but it's mechanical—precise, but devoid of passion or warmth."

            cah "You spend enough time watching people die, watching them slip away despite everything you do,"
            cah "and eventually, you stop feeling much of anything."
            cah "You just… do the work."
            cah "Because it's what's expected of you."
            cah "Because it's all you know how to do."

            show cah sad at look_down
            "There's a heavy silence that follows his words, as if he's said too much and is retreating back into himself."
            "His gaze remains averted, focused on the task at hand, his expression unreadable."

            cah "Xantos believed in the impossible."
            cah "But me? I believe in what's left when the impossible is gone."
            cah "The work."
            cah "That's all there is."
            cah "You treat what you can, and you bury the rest."

            show cah sup at lean_in
            "For a moment, his hands still completely, and he looks up at you with an intensity that catches you off guard."
            "There's something in his eyes—something bitter, something broken."

            cah "That's the real lesson I learned from him."
            cah "No matter how hard you try, sometimes the only thing left to do is let go."

            show cah neu at subtle_breathe
            "He lets out a slow breath, his expression neutral again, as though he's said everything he intended to say."

            cah "Now, let's see to you."
            cah "There's no point dwelling on the dead."
            jump a1_healer_conversation_menu1

        "How can you be so calm about it all? Life, death... doesn't it affect you?" if not healer_calm_convo:
            $ healer_calm_convo = True

            "Caharel's expression remains unreadable for a moment, his gaze shifting slightly, though not meeting yours."
            "He seems to weigh your question before responding, the air around him thick with the weight of unspoken thoughts."

            show cah neu at tilt_left
            cah "Calm? No, I wouldn't call it calm."

            "He finally looks at you, his pale eyes steady and unblinking, cold and distant like a winter sky just before the first frost."

            show cah neu at subtle_breathe
            cah "It's... clarity. A kind of understanding that comes with time. Life, death—they're not opposites."
            cah "They're part of the same fragile thread. You come to see that people are like flickering lights in a storm."
            cah "Some flames burn longer than others, but eventually, they all go out."

            show cah neu at nod
            "His voice is soft but carries an unshakable certainty, as if he's repeated these thoughts to himself over and over again,"
            "until they've become his truth."

            cah "Sometimes, you can keep the flame going a little longer. Other times, it flickers out before you can even blink."
            cah "You learn not to fight it. You learn to accept it."

            show cah neu at look_down
            "He taps his fingers lightly against the edge of the bed, the sound faint, almost rhythmic,"
            "like he's counting out the beats of a life fading away."

            cah "You get used to it. The human heart can only take so much before it hardens, before it protects itself."
            "My hands may heal, but my soul... my soul learned long ago to let go."

            show cah sad at look_down
            "There's a pause, the silence stretching out between you like a vast, empty chasm."
            "The space between the two of you feels colder now, as if the warmth of human connection has been lost to the endless cycle of life and death he's seen."

            cah "It's not heartlessness. It's survival. For both me and them."

            show cah neu at step_back
            "He rises slowly, as if the conversation has taken its toll on him, though his expression remains calm, steady—unyielding."

            cah "If I let every loss break me, I wouldn't be able to help the next person. And there's always a next person."
            jump a1_healer_conversation_menu1
        
        "Change the subject.":
            jump a1_healer1

label a1_healer1:
    "Days pass slowly in the hospice, each one blurring into the next."
    "The faint scent of pine and sage lingers in the air, mixing with the constant,"
    "comforting crackle of the hearth at the far end of the room."
    "You spend most of your time lying in bed, your body still weak from the cold and exhaustion."
    "Outside, the world carries on, but here within the stone walls, it feels like time has slowed to a crawl."
    "Caharel visits intermittently, his presence as steady and routine as the ticking of a clock."
    
    show cah neu at subtle_breathe
    "He checks your pulse, examines your recovery with the same detached precision as before,"
    "but always with the same quiet efficiency."

    "The sound of his tools, the rustle of his robes, the scrape of his chair—these become the background noise of your recovery."
    "And though his touch is careful, you can't help but feel the distance in it."
    "But slowly, you feel your strength returning. At first, it's a flicker—just enough to sit up in bed,"
    "to hold a cup of warm broth in your hands without trembling."
    
    show cah neu at step_back
    "The warmth spreads through you with each sip,"
    "the rich taste of marigold and chamomile soothing the last remnants of your fatigue."
    "The world beyond the small window seems brighter, more alive, though still distant."

    "By the end of the week, you manage to stand, taking tentative steps around the room."
    "The floor is cool beneath your feet, the stone rough but familiar."

    show cah neu at lean_in
    "Caharel watches from a distance, his arms crossed, his sharp gaze never lingering too long,"
    "as if making sure you don't falter."

    "Finally, one evening, he approaches, his voice as calm as ever."
    
    show cah neu at nod
    cah "You're healing well. Soon, you'll be strong enough to leave."
    
    show cah neu at subtle_breathe
    "His words are simple, almost clinical, but there's a faint softness in his tone."
    "The smallest sign that, despite everything, your recovery means something. Even if he would never say it."

    menu:
        "Resume your search for the mysterious stranger Stavros mentioned.":
            "After resting for a few more hours, you feel your strength return. The weight of Stavros' words lingers in your mind, urging you onward."
            "You gather your belongings, the familiar chill of the forest wrapping around you as you step back onto the worn path."
            "The trees close in once more, their twisted branches arching above like a dark canopy, and the distant calls of forest creatures echo through the woods."
            "Your footsteps quicken as you remember the direction Stavros gave you—west, past the river. The air grows cooler as the sun begins to sink lower in the sky."
            "You press on, navigating the narrowing trail, your breath visible in the cold air."

            stop music fadeout 1.0
            stop sound fadeout 1.0
            scene black with fade
            jump s_a1_golem

        "Explore Everdusk Valley.":
            stop music fadeout 1.0
            stop sound fadeout 1.0
            scene black with fade
            jump s_a1_glitch
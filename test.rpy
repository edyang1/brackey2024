label char_test:
    $ artstyle = "fantasy"
    
    play music "fantasy_casual.mp3" loop fadein 1.0
    scene fantasy_healer with fade

    "This is a test."
    "Hello, world!"

    show stav hap
    stav "Hi, I'm Stavros Attelides!"
    show stav sad
    stav "I'm sad."
    show stav ang
    stav "I'm angry."
    show stav sup
    stav "I'm surprised."
    show stav neu
    stav "I'm neutral."
    stav "Seeya!"
    hide stav

    show cah hap
    cah "Hi, I'm Caharel!"
    show cah sad
    cah "I'm sad."
    show cah ang
    cah "I'm angry."
    show cah sup
    cah "I'm surprised."
    show cah neu
    cah "I'm neutral."
    cah "Seeya!"
    hide cah

    show i hap
    i "Hi, I'm Iolkos!"
    show i sad
    i "I'm sad."
    show i ang
    i "I'm angry."
    show i sup
    i "I'm surprised."
    show i neu
    i "I'm neutral."
    i "Seeya!"
    hide i
    
    $ artstyle = "cyber"

    play music "cyber_casual.mp3" loop fadein 1.0
    scene cyber_healer with fade

    show stan hap
    stan "Hi, I'm Stanley “Stars” Hatterlode!"
    show stan sad
    stan "I'm sad."
    show stan ang
    stan "I'm angry."
    show stan sup
    stan "I'm surprised."
    show stan neu
    stan "I'm neutral."
    stan "Seeya!"
    hide stan

    show cal hap
    cal "Hi, I'm Callie Wollerback!"
    show cal sad
    cal "I'm sad."
    show cal ang
    cal "I'm angry."
    show cal sup
    cal "I'm surprised."
    show cal neu
    cal "I'm neutral."
    cal "Seeya!"
    hide cal

    show b hap
    b "Hi, I'm B4/22C (Bass)!"
    show b sad
    b "I'm sad."
    show b ang
    b "I'm angry."
    show b sup
    b "I'm surprised."
    show b neu
    b "I'm neutral."
    b "Seeya!"
    hide b

    return

label bg_test:
    $ artstyle = "fantasy"
    scene black with fade
    "Let's go to fantasy cottage."
    scene fantasy_cottage with fade
    "Let's go to fantasy golem."
    scene fantasy_golem with fade
    "Let's go to fantasy healer."
    scene fantasy_healer with fade
    "Let's go to fantasy knight."
    scene fantasy_knight with fade

    "Let's go to the cyber world."

    $ artstyle = "cyber"
    scene black with fade
    "Let's go to cyber android."
    scene cyber_android with fade
    "Let's go to cyber console."
    scene cyber_console with fade
    "Let's go to cyber fighter."
    scene cyber_fighter with fade
    "Let's go to cyber healer."
    scene cyber_healer with fade

    "I just lost my dog. And my brother taught me how to chase the bag."

    return

label fx_test:
    $ artstyle = "fantasy"
    scene fantasy_cottage with dissolve
    
    play music "fantasy_casual.mp3" loop fadein 1.0
    "Let's play some music."
    "Now, let's glitch it."
    
    # Start the glitch effect (in parallel)
    $ start_stop_start_glitch("fantasy_casual.mp3")
    
    "The music is glitching now!"
    
    "Stop the glitch."
    
    # Stop the glitch effect
    $ stop_stop_start_glitch()
    
    "The glitch has stopped."
    
    return
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
    show stan bigsup
    stan "I'm very surprised."
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

label pos_test:
    $ artstyle = "fantasy"
    scene fantasy_cottage with fade

    show stav neu at close_to_camera
    stav "I'm neutral and close to the camera."
    hide stav

    show stav neu at lean_in
    stav "I'm neutral and lean in."
    hide stav

    show stav neu at lean_back
    stav "I'm neutral and lean back."
    hide stav

    show stav neu at shift_left
    stav "I'm neutral and shift left."
    hide stav

    show stav neu at shift_right
    stav "I'm neutral and shift right."
    hide stav

    show stav neu at tilt_left
    stav "I'm neutral and tilt left."
    hide stav

    show stav neu at tilt_right
    stav "I'm neutral and tilt right."
    hide stav

    show stav neu at nod
    stav "I'm neutral and nod."
    hide stav

    show stav neu at shake_head
    stav "I'm shaking my head."
    hide stav

    show stav neu at subtle_breathe
    stav "I'm subtly breathing."
    hide stav

    show stav neu at sway_left_right
    stav "I'm swaying left and right."
    hide stav

    show stav neu at shrink_back
    stav "I'm shrinking back."
    hide stav

    show stav neu at jitter
    stav "I'm jittery."
    hide stav

    show stav neu at step_forward
    stav "I'm stepping forward."
    hide stav

    show stav neu at step_back
    stav "I'm stepping back."
    hide stav

    show stav neu at look_away
    stav "I'm looking away."
    hide stav

    show stav neu at look_up
    stav "I'm looking up."
    hide stav

    show stav neu at look_down
    stav "I'm looking down."
    hide stav

    show stav neu at enter_slow
    stav "I just entered the scene slowly."
    hide stav at exit_slow

    show stav neu at enter_quick
    stav "I'm in a hurry, so I entered quickly."
    hide stav at exit_quick

    show stav neu at enter_hesitant
    stav "I'm not sure about this, so I entered hesitantly."
    hide stav at exit_hesitant

    show stav neu at enter_confident
    stav "I'm confident, so I made a bold entrance."
    hide stav at exit_confident

    show stav neu at enter_shy
    stav "I'm feeling shy, so I entered cautiously."
    hide stav at exit_shy

    show stav neu at enter_bold
    stav "I made a dramatic and sudden entrance!"
    hide stav at exit_bold

    show stav neu at enter_subtle
    stav "I sneaked in quietly with a subtle entrance."
    hide stav at exit_subtle

    "Holy crap we're done."

    show stav neu at close_to_camera
    stav "I'm neutral and close to the camera."
    hide stav

    

    show cah neu at close_to_camera
    cah "I'm neutral and close to the camera."
    hide cah

    show i neu at close_to_camera
    i "I'm neutral and close to the camera."
    hide i

    "Lets go over to the cyber world."
    $ artstyle = "cyber"
    scene cyber_fighter with fade

    show stan neu at close_to_camera
    stan "I'm neutral and close to the camera."
    hide stan

    show cal neu at close_to_camera
    cal "I'm neutral and close to the camera."
    hide cal

    show b neu at close_to_camera
    b "I'm neutral and close to the camera."
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
    "Now, let's glitch it by pausing and resuming."

    python:
        for count in range(2):
            renpy.music.set_pause(True)
            renpy.pause(renpy.random.uniform(0.1, 0.3))  
            
            renpy.music.set_pause(False)
            renpy.pause(renpy.random.uniform(0.05, 0.2))
    
    "The glitch has stopped."
    
    "Glitch it with random sound effects."

    python:
        glitch_sounds = ["glitch1.mp3", "glitch2.mp3", "glitch3.mp3", "glitch4.mp3"]
        for count in range (5): # how many times to play any sound
            random_sound = renpy.random.choice(glitch_sounds)
            renpy.sound.play(random_sound)
            renpy.pause(renpy.random.uniform(3, 5))

    "The glitch has stopped."

    "Glitch the pitch."
    
    python:
        for count in range (50):
            renpy.music.set_pan(renpy.random.uniform(-1, 1), 0)
            renpy.pause(renpy.random.uniform(0.02, 0.1))

    "The pitch glitch has stopped."
    
    # "Let's try something new!"

    
    # python:
    #     renpy.music.set_audio_filter("music", [renpy.audio.filter.Reverb(0.5), renpy.audio.filter.Lowpass(440)])

    # "The music is now glitched!"
    
    return

label choice_test:
    $ artstyle = "fantasy"
    scene fantasy_cottage with fade

    "Let's make a choice between 2."

    menu:
        "Option 1":
            "You chose option 1."
        "Option 2":
            "You chose option 2."
    
    "Let's make a choice between 3."

    menu:
        "Option 1":
            "You chose option 1."
        "Option 2":
            "You chose option 2."
        "Option 3":
            "You chose option 3."
    
    "Let's make a choice between 4."

    menu:
        "Option 1":
            "You chose option 1."
        "Option 2":
            "You chose option 2."
        "Option 3":
            "You chose option 3."
        "Option 4":
            "You chose option 4."

    "Excellent job! Let's go to the cyberpunk world."

    $ artstyle = "cyber"
    scene cyber_android with fade

    "Let's make a choice between 2."

    menu:
        "Option 1":
            "You chose option 1."
        "Option 2":
            "You chose option 2."
    
    "Let's make a choice between 3."

    menu:
        "Option 1":
            "You chose option 1."
        "Option 2":
            "You chose option 2."
        "Option 3":
            "You chose option 3."
    
    "Let's make a choice between 4."

    menu:
        "Option 1":
            "You chose option 1."
        "Option 2":
            "You chose option 2."
        "Option 3":
            "You chose option 3."
        "Option 4":
            "You chose option 4."
        
    return
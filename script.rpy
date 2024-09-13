# CHARACTERS
define stav = Character("stav") #Stavros Attelides
define cah = Character("cah") #Caharel
define i = Character("i") #Iolkos

define stan = Character("stan") #Stanley “Stars” Hatterlode
define cal = Character("cal") #Callie Wollerback
define b = Character("b") #B4/22C (Bass)

# ANIMATIONS
transform close_to_camera:
    xpos 0.5
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    zoom 1.5

transform barge_into_center:
    center
    xpos 1.2
    ypos 0.8
    easeout_quint 0.3 xpos 0.5
    easein_back 0.1 xpos 0.45
    easeout 0.1 xpos 0.5

# START
label start:
    # call act1_scene1

    call char_test
    call pos_test
    call bg_test
    # call fx_test

    call act1_scene1
    
    return
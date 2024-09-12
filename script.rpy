# CHARACTERS

define stav = Character("stav")
define cah = Character("cah")
define i = Character("i")

define stan = Character("stan")
define cal = Character("cal")
define b = Character("b")

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
    easeout_quint 0.3 xpos 0.5
    easein_back 0.1 xpos 0.45
    easeout 0.1 xpos 0.5

# START

label start:
    call act1_scene1
    return
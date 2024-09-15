# CHARACTERS
define stav = Character("Stavros", color="#007a02", image="stav")  # Stavros Attelides
define cah = Character("Caharel", color="#7fb638", image="cah")  # Caharel (they)
define i = Character("Iolkos", color = "#684930", image="i")  # Iolkos

define fox = Character("Two-tailed fox", color="#ff7f00", image="fox")  # Fox

define stan = Character("Stanley", color="#5d89f7", image="stan")  # Stanley “Stars” Hatterlode
define cal = Character("Callie", color="#ff764a", image="cal")  # Callie Wollerback
define b = Character("B4/22C", color="#d9a832", image="b")  # B4/22C (Bass)

define f_name = "Cassiopeia"
define cyber_name = "CassioP0X"

# ANIMATIONS
transform close_to_camera:
    xpos 0.5
    ypos 0.45
    xanchor 0.5
    yanchor 0.5
    zoom 1.12

transform barge_into_center:
    center
    xpos 1.2
    ypos 0.8
    easeout_quint 0.3 xpos 0.5
    easein_back 0.1 xpos 0.45
    easeout 0.1 xpos 0.5

# START
label start:

    call s_a1_f_start

    # call choice_test
    # call char_test
    # call pos_test
    # call bg_test
    # call fx_test
    
    return
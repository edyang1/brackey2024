# CHARACTERS
define stav = Character("Stavros", color="#7a0000", image="stav")  # Stavros Attelides
define cah = Character("Caharel", color="#7fb638", image="cah")  # Caharel (they)
define i = Character("Iolkos", color = "#684930", image="i")  # Iolkos

define fox = Character("Two-tailed fox", color="#ff7f00", image="fox")  # Fox

define stan = Character("Stanley", color="#5d89f7", image="stan")  # Stanley “Stars” Hatterlode
define cal = Character("Callie", color="#ff764a", image="cal")  # Callie Wollerback
define b = Character("B4/22C", color="#d9a832", image="b")  # B4/22C (Bass)

define f_name = "Cassiopeia"
define c_name = "Ca55ioP0X"

# POSITIONS/ANIMATIONS
transform close_to_camera:
    xpos 0.5
    ypos 0.45
    xanchor 0.5
    yanchor 0.5
    zoom 1.12

# Subtle movement forward, like leaning in during conversation.
transform lean_in:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    ease 0.3 ypos 0.44
    pause 0.2

# Subtle movement backward, like leaning back after a statement.
transform lean_back:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    ease 0.3 ypos 0.46
    pause 0.2

# A small shift to the left, indicating thought or hesitation.
transform shift_left:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    easeout 0.4 xpos 0.48
    pause 0.2
    easein 0.4 xpos 0.5

# A small shift to the right, showing contemplation or doubt.
transform shift_right:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    easeout 0.4 xpos 0.52
    pause 0.2
    easein 0.4 xpos 0.5

# Slightly tilting to one side, representing curiosity or a reaction.
transform tilt_left:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    rotate -3
    linear 0.5 rotate 0

transform tilt_right:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    rotate 3
    linear 0.5 rotate 0

# A nodding motion, subtle head tilt down and back up for agreement.
transform nod:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    linear 0.2 ypos 0.44
    linear 0.2 ypos 0.45

# A subtle shake of the head for disagreement or disapproval.
transform shake_head:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    linear 0.2 xpos 0.48
    linear 0.2 xpos 0.52
    linear 0.2 xpos 0.5

# Breathing effect, like the character is calm or thoughtful.
transform subtle_breathe:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    zoom 1.0
    linear 1.2 zoom 1.02
    linear 1.2 zoom 1.0
    repeat

# A small bounce up and down to show enthusiasm or excitement.
transform bounce_up:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    easeout_back 0.4 ypos 0.42
    easein 0.4 ypos 0.45

# A soft sway from side to side, like pacing or nervousness.
transform sway_left_right:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    linear 0.5 xpos 0.48
    linear 0.5 xpos 0.52
    linear 0.5 xpos 0.5
    repeat 1

# Shrink a bit, like the character is shrinking back in embarrassment or fear.
transform shrink_back:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    zoom 1.0
    easein_quint 0.4 zoom 0.95
    easeout 0.4 zoom 1.0

# A quick, jittery movement like the character is startled.
transform jitter:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    easeout 0.05 xpos 0.52
    easein 0.05 xpos 0.48
    easeout 0.05 xpos 0.5

# Step forward slowly, like cautiously advancing in the conversation.
transform step_forward:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    ease 0.6 ypos 0.44
    pause 0.2

# Step back slowly, indicating retreat or hesitation during the conversation.
transform step_back:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    ease 0.6 ypos 0.46
    pause 0.2

# Rotate slightly to indicate the character is looking away or becoming distant.
transform look_away:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    rotate -5
    pause 0.3
    linear 0.5 rotate 0

# A subtle look upwards, useful for when the character is thinking or reminiscing.
transform look_up:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    linear 0.4 ypos 0.42
    pause 0.3
    linear 0.4 ypos 0.45

# Look down slightly, showing sadness or regret.
transform look_down:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    linear 0.4 ypos 0.47
    pause 0.3
    linear 0.4 ypos 0.45

# ENTER/EXIT SCENE

# Slow and deliberate entrance, suitable for calm or serious characters.
transform enter_slow:
    xpos 1.2 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    ease 1.0 xpos 0.5

# Quick and energetic entrance, for more excitable or enthusiastic characters.
transform enter_quick:
    xpos 1.2 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    ease 0.5 xpos 0.5

# Nervous or hesitant entrance, with a slight stop.
transform enter_hesitant:
    xpos 1.2 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    ease 0.7 xpos 0.6
    pause 0.2
    ease 0.5 xpos 0.5

# Confident, swagger-like entrance, with a small pause as if surveying the scene.
transform enter_confident:
    xpos 1.2 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    easeout 0.6 xpos 0.55
    pause 0.2
    easein 0.4 xpos 0.5

# Shy, timid entrance, slow and cautious.
transform enter_shy:
    xpos 1.2 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    ease 0.8 xpos 0.5
    zoom 0.9
    linear 0.5 zoom 1.0

# Bold, sudden entrance for characters who like to make a dramatic appearance.
transform enter_bold:
    xpos 1.2 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    easeout_back 0.4 xpos 0.5

# Subtle and unnoticed entrance, like sneaking into a conversation.
transform enter_subtle:
    xpos 1.2 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    linear 1.2 xpos 0.5

# Slow and deliberate exit, for characters who leave calmly or solemnly.
transform exit_slow:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    ease 1.0 xpos -0.2

# Quick exit, for when the character is in a hurry or feeling flustered.
transform exit_quick:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    ease 0.5 xpos -0.2

# Hesitant exit, for when the character isn’t sure if they should leave.
transform exit_hesitant:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    ease 0.6 xpos 0.4
    pause 0.2
    ease 0.5 xpos -0.2

# Confident and bold exit, suitable for proud or arrogant characters.
transform exit_confident:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    easein 0.4 xpos 0.55
    pause 0.2
    easeout 0.6 xpos -0.2

# Shy, timid exit, with the character retreating almost cautiously.
transform exit_shy:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    ease 0.8 xpos -0.2
    zoom 1.0
    linear 0.5 zoom 0.9

# Dramatic and sudden exit for characters who want to storm out.
transform exit_bold:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    easein_back 0.4 xpos -0.2

# Quiet, unnoticed exit for characters who want to slip away.
transform exit_subtle:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    linear 1.2 xpos -0.2

# Shrinking exit, like someone withdrawing or feeling embarrassed.
transform exit_shrink:
    xpos 0.5 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    ease 0.6 zoom 0.8
    ease 0.6 xpos -0.2

# Expanding entrance, like someone building confidence as they arrive.
transform enter_expand:
    xpos 1.2 ypos 0.45
    xanchor 0.5
    yanchor 0.5
    zoom 0.8
    ease 0.6 xpos 0.5 zoom 1.0

# START
label start:

    # call s_a1_golem

    # call s_a1_f_start

    # call choice_test
    # call char_test
    call pos_test
    # call bg_test
    # call fx_test
    
    return
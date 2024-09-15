# CHARACTERS
define stav = Character("Stavros", color="#fdea11", image="stav")  # Stavros Attelides
define cah = Character("Caharel", color="#2b43c9", image="cah")  # Caharel (they)
define i = Character("Iolkos", color = "#3c8734", image="i")  # Iolkos

define fox = Character("Two-tailed fox", color="#ff7f00", image="fox")  # Fox

define stan = Character("Stanley", color="#c65df7", image="stan")  # Stanley “Stars” Hatterlode
define cal = Character("Callie", color="#39bd93", image="cal")  # Callie Wollerback
define b = Character("B4/22C", color="#d93232", image="b")  # B4/22C (Bass)

# PLAYER NAMES
define f_name = "Cassiopeia"
define c_name = "Ca55ioP0X"


# SCENE EFFECTS

define flash = Fade(0.1, 0.0, 0.5, color="#fff")

# TRANSFORM GUIDE

# 1. close_to_camera
# Description: Places the character close to the camera with a slight zoom for emphasis.
# Use Case: When the character is engaging in an intimate conversation or taking a prominent role in the scene.

# 2. lean_in
# Description: Moves the character slightly forward, as if leaning in during conversation.
# Use Case: Useful for showing engagement or interest in a conversation.

# 3. lean_back
# Description: Moves the character slightly back, simulating leaning away.
# Use Case: Appropriate for moments of reflection or pulling back after a statement.

# 4. shift_left
# Description: Shifts the character a bit to the left.
# Use Case: Perfect for moments of hesitation or thinking.

# 5. shift_right
# Description: Shifts the character a bit to the right.
# Use Case: Used when showing contemplation, doubt, or a moment of surprise.

# 6. tilt_left
# Description: Tilts the character slightly to the left.
# Use Case: For expressions of curiosity, consideration, or light confusion.

# 7. tilt_right
# Description: Tilts the character slightly to the right.
# Use Case: Expresses curiosity or reacting with a slight emotional shift.

# 8. nod
# Description: Subtle head nod to show agreement.
# Use Case: When the character agrees or acknowledges something.

# 9. shake_head
# Description: Shakes the character's head left and right in disagreement.
# Use Case: Perfect for disapproval or rejection.

# 10. subtle_breathe
# Description: A subtle breathing effect for a calm or thoughtful stance.
# Use Case: Use when the character is calm, contemplative, or thinking deeply.

# 11. bounce_up
# Description: Small bounce upwards.
# Use Case: Suitable for excitement, enthusiasm, or happiness.

# 12. sway_left_right
# Description: Soft sway from side to side.
# Use Case: Ideal for nervousness, impatience, or pacing.

# 13. shrink_back
# Description: The character shrinks back slightly, like retreating in fear or embarrassment.
# Use Case: When the character feels embarrassed, afraid, or hesitant.

# 14. jitter
# Description: Quick, jittery movement to show the character is startled.
# Use Case: Useful for showing surprise, nervousness, or shock.

# 15. step_forward
# Description: The character steps forward slowly.
# Use Case: Used when a character cautiously advances in the conversation or physically moves closer.

# 16. step_back
# Description: The character steps back slowly.
# Use Case: Appropriate for moments of hesitation or retreat during a conversation.

# 17. look_away
# Description: Rotates the character away slightly, as if looking elsewhere.
# Use Case: Represents the character becoming distant, distracted, or emotionally withdrawn.

# 18. look_up
# Description: Character looks upwards.
# Use Case: Ideal for moments of thought, reflection, or daydreaming.

# 19. look_down
# Description: Character looks downwards.
# Use Case: Represents sadness, regret, or introspection.

# 20. enter_slow
# Description: Slow and deliberate entrance into the scene.
# Use Case: Suitable for calm or serious characters entering without haste.

# 21. enter_quick
# Description: Quick and energetic entrance.
# Use Case: For characters who are enthusiastic or in a hurry.

# 22. enter_hesitant
# Description: Nervous or hesitant entrance with a slight stop.
# Use Case: Best for shy or unsure characters entering a scene cautiously.

# 23. enter_confident
# Description: Confident entrance with a slight pause to survey the scene.
# Use Case: Perfect for bold or self-assured characters making an entrance.

# 24. enter_shy
# Description: Slow, shy entrance with a slight zoom effect.
# Use Case: Use for timid or introverted characters entering cautiously.

# 25. enter_bold
# Description: Bold and sudden entrance.
# Use Case: Dramatic entrances for characters who want to make a statement.

# 26. enter_subtle
# Description: Subtle, unnoticed entrance.
# Use Case: Best for sneaky or quiet characters entering a scene without drawing attention.

# 27. exit_slow
# Description: Slow and deliberate exit.
# Use Case: Used for characters leaving calmly or solemnly.

# 28. exit_quick
# Description: Quick and energetic exit.
# Use Case: For characters who are in a hurry to leave.

# 29. exit_hesitant
# Description: Hesitant exit with a slight pause.
# Use Case: Perfect for characters who aren't sure if they should leave.

# 30. exit_confident
# Description: Bold and confident exit with a slight pause.
# Use Case: Suitable for proud or bold characters leaving a scene.

# 31. exit_shy
# Description: Shy, cautious exit with a zoom-out effect.
# Use Case: Use for characters who retreat or leave quietly.

# 32. exit_bold
# Description: Dramatic and sudden exit.
# Use Case: Suitable for characters who want to storm out or leave dramatically.

# 33. exit_subtle
# Description: Quiet, unnoticed exit.
# Use Case: For sneaky characters who want to slip away without being noticed.

# 34. exit_shrink
# Description: Shrinking exit, like someone withdrawing or feeling embarrassed.
# Use Case: For characters who feel embarrassed, defeated, or wish to disappear.

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

# Hesitant exit, for when the character isn't sure if they should leave.
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
    $ artstyle = "fantasy"

    # "ERROR: {size=*1.5}{color=#f00}M€mø®¥ Sėgmêntâ†ïøñ Fåûł†{/color}{/size}"
    # "WARNING: {size=*0.7}{b}Stack Overflow Detected{/b}. Data integrity compromised."
    # "Corrupt Memory Block: {size=*1.2}{s}0xFFAC201{/s}{/size} {size=*0.5}{color=#00ff00}Attempting to recover{/color}..."
    # "{size=*0.8}{i}Runtime Exception: Unexpected NULL pointer dereference{/i}{/size}"
    # "{size=+7}{color=#f00}Fø®mât Šķÿñë {s}inva...invali{/s}d{/color}"
    # "{size=*1.8}{color=#ff4500}Data breach in sector XX—cr¡t¡cal failure. M¿smätçh detected.{/color}"
    # "{size=*0.4}{i}{color=#0000ff}Rebooting...rebOoOOting...{/color}{/i}"
    # "{size=*2}{u}{color=#8a2be2}Warning: Heap overflow detected!{/color}{/u}"
    # "{size=*1.3}{s}Faulty{/s} segment in {i}Mₑₘₒᵣᵧ₋ₛₜₐcₖ₁{/i}."
    

    jump s_a3_bad_ending

    # call s_a1_f_start

    # call choice_test
    # call char_test
    # call pos_test
    # call bg_test
    # call fx_test
    
    return
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
    easeout_quint 0.3 xpos 0.5
    easein_back 0.1 xpos 0.45
    easeout 0.1 xpos 0.5

# GLITCH FX
python:
    import renpy.random

    # Global variable to control whether the audio stop-start glitch effect should be running
    stop_start_glitch_active = False

    def stop_start_glitch(audio_file):
        """
        Creates a glitch effect by stopping and restarting the audio file at random intervals.
        """
        global stop_start_glitch_active
        
        # Loop to apply the stop-start effect while active
        while stop_start_glitch_active:
            renpy.stop_music()
            renpy.pause(renpy.random.uniform(0.1, 0.3))  # Random pause between 0.1 and 0.3 seconds
            renpy.play_music(audio_file)  # Corrected play function
            renpy.pause(renpy.random.uniform(0.05, 0.2))  # Random pause between 0.05 and 0.2 seconds
            renpy.stop_music()
            renpy.pause(renpy.random.uniform(0.1, 0.25))  # Random pause between 0.1 and 0.25 seconds
            renpy.play_music(audio_file)

    def start_stop_start_glitch(audio_file):
        global stop_start_glitch_active
        stop_start_glitch_active = True
        stop_start_glitch(audio_file)

    def stop_stop_start_glitch():
        global stop_start_glitch_active
        stop_start_glitch_active = False
        renpy.stop_music() 

    # Global variable to control whether the sound glitch effect should be running
    sound_glitch_active = False

    def sound_glitch_effect():
        """
        Plays glitch sound effects at random intervals if sound_glitch_active is True.
        """
        global sound_glitch_active
        
        # Define the array of glitch sound effects
        glitch_sounds = ["audio/glitch1.ogg", "audio/glitch2.ogg", "audio/glitch3.ogg"]

        # Loop through the glitch sound effects and play them at random intervals
        while sound_glitch_active:
            for sound in glitch_sounds:
                if not sound_glitch_active:
                    break  # If stopped during the loop, exit early
                renpy.play(sound)
                renpy.pause(renpy.random.uniform(0.1, 0.4))  # Random pause between 0.1 and 0.4 seconds

    def start_sound_glitch():
        global sound_glitch_active
        sound_glitch_active = True
        sound_glitch_effect()

    def stop_sound_glitch():
        global sound_glitch_active
        sound_glitch_active = False
        renpy.stop_all_sounds()  # Stop all sounds playing

    # Global variable to control whether the pitch glitch effect should be running
    pitch_glitch_active = False

    def pitch_glitch_effect():
        """
        Applies a glitch effect by rapidly changing the pan of the music at random intervals.
        """
        global pitch_glitch_active
        
        # Loop to apply random pan changes while the glitch effect is active
        while pitch_glitch_active:
            renpy.music.set_pan(-1)  # Left speaker
            renpy.pause(renpy.random.uniform(0.05, 0.2))  # Random pause between 0.05 and 0.2 seconds
            renpy.music.set_pan(1)   # Right speaker
            renpy.pause(renpy.random.uniform(0.05, 0.2))  # Random pause between 0.05 and 0.2 seconds
            renpy.music.set_pan(0)   # Center speaker
            renpy.pause(renpy.random.uniform(0.05, 0.2))  # Random pause between 0.05 and 0.2 seconds

    def start_pitch_glitch():
        global pitch_glitch_active
        pitch_glitch_active = True
        pitch_glitch_effect()

    def stop_pitch_glitch():
        global pitch_glitch_active
        pitch_glitch_active = False
        renpy.music.set_pan(0)  # Reset to center speaker
        renpy.stop_music()

# START
label start:
    # call act1_scene1



    # call char_test
    # call bg_test
    call fx_test
    return
label s_a1_forest_minigame:
    play music "fantasy_casual.mp3" loop fadein 1.0
    scene fantasy_knight with fade

    "As you forge ahead, the forest begins to envelop you, its tall, thick trees casting long shadows over the path."
    "The deeper you venture, the more the woods seem to close in around you, a quiet stillness hanging in the air."
    "It feels as though lost magic lingers here, barely perceptible but unmistakable."
    "Suddenly, you hear a familiar sound—the two-toned yip of a wild animal, like two voices calling at once."
    "It's the same call you heard back at Stavros' home, echoing faintly through the trees."
    "You note the large amount of thick roots and brambles, making sure not to trip."
    jump forest_minigame_start

label forest_minigame_start:
    play music "fantasy_suspense.mp3" loop fadein 1.0

    "Don't trip over the roots!"
    menu:
        "Root":
            "Your foot catches on a root, and you hit the ground hard, pain exploding in your ankle, leaving you unable to stand."
            jump forest_minigame_setback

        "Path":
            "You navigate the path carefully, avoiding roots and obstacles, continuing forward without trouble."
            jump forest_minigame_2

        "Large root":
            "You slam into a large root and fall, pain flaring through your ankle, making it impossible to stand on your own."
            jump forest_minigame_setback

label forest_minigame_2:
    "Don't trip!"
    menu:
        "Fox den":
            "You stumble over the entrance of a hidden fox den, falling to the ground and twisting your ankle painfully."
            jump forest_minigame_setback

        "Overgrown roots":
            "Thick, gnarled roots snake across the path, and you catch your foot on one, sending you crashing to the ground."
            jump forest_minigame_setback

        "Moss-covered log":
            "Your foot slips on a moss-covered log, slick with morning dew, sending you headfirst into the dirt."
            jump forest_minigame_setback

        "Clear path":
            "You carefully step over the roots and logs, navigating the forest floor with ease as you move forward."
            jump forest_minigame_3

label forest_minigame_3:
    "Watch your step!"
    menu:
        "Choose me!":
            "You step forward, but the ground shifts beneath you, and you lose your footing, tumbling to the ground."
            jump forest_minigame_setback

        "Right path?":
            "You cautiously pick what seems like the safe path, but a loose rock sends you stumbling into the undergrowth."
            jump forest_minigame_setback

        "Boulder?":
            "You decide to climb over the large boulder, finding stable footing and a clear path ahead."
            jump forest_minigame_4

        "Rock?":
            "You avoid the larger obstacles, only to trip over a small rock hidden under the leaves."
            jump forest_minigame_setback

label forest_minigame_4: #plant quiz
    "Your stomach growls as you notice a patch of unfamiliar plants growing along the path."
    "You're tempted to eat, but you're not sure if it's safe."

    menu:
        "Eat the plant immediately":
            "You grab a handful and eat it without thinking."
            "Almost immediately, your stomach twists painfully, and you realize it was a bad choice."

            "Disclaimer: take our survival advice with a grain of salt."
            "Please do your due dilligence before exploring the wilderness."
            jump forest_minigame_setback

        "Perform an edibility test (rub it on skin first)":
            "You carefully rub a piece of the plant on your skin and wait. After several minutes, nothing happens."
            "It seems safe to taste a small piece."

            "Disclaimer: take our survival advice with a grain of salt."
            "Please do your due dilligence before exploring the wilderness."
            jump forest_minigame_5

        "If animals are eating it, it must be safe":
            "You assume it's safe since you saw a rabbit nibbling nearby."
            "Unfortunately, what's safe for animals isn't always safe for humans, and soon you feel dizzy."

            "Disclaimer: take our survival advice with a grain of salt."
            "Please do your due dilligence before exploring the wilderness."
            jump forest_minigame_setback

label forest_minigame_5: #navigation. establish animal calls for later puzzle
    "You continue on the path, the distant calls of animals reaching your ears."
    "First, the chittering of a squirrel, then the hoot of an owl, and finally, the familiar two-toned yip of the fox."

    "As you listen, however, you realize you've lost track of your direction."
    "Panic begins to creep in as you recognize you're lost in the thick of the forest."
    "How will you find your way?"

    menu:
        "Follow the moss on trees, it always grows on the north side.":
            "While it's a common myth, moss doesn't always grow only on the north side. It tends to grow on the shadier, damper side of trees, but this can vary."
            "You follow the moss, but it leads you further into unfamiliar territory."
            jump forest_minigame_setback

        "Use the sun's position and shadows to determine direction.":
            "You calm yourself and focus on the sun's position. It rises in the east and sets in the west. In the afternoon, facing the sun means you're roughly facing west."
            "Using this method, you regain your bearings and resume your path."
            jump forest_minigame_6

        "Walk downhill until you find a water source, then follow it.":
            "Walking downhill might lead you to a water source, but water doesn't necessarily flow in a straight line. Rivers can twist and turn, leading you off course."
            "You walk for what seems like hours, but end up more disoriented."
            jump forest_minigame_setback

label forest_minigame_6: #animal calls puzzle
    "The forest seems to be shifting around you, its paths winding and confusing. You stop to listen closely."
    "The animal calls seem to echo in a specific pattern, drawing you toward something... but what?"

    "You realize you need to follow the order of the calls to find your way through the forest."

    menu:
        "Follow the chittering of the squirrel first.":
            "You follow the sound of the squirrel's chittering, and the forest seems to lighten. The trees open up slightly, giving you a clearer path."
            jump forest_minigame_7

        "Follow the hoot of the owl first.":
            "You follow the owl's call, but the forest grows darker, and the trees seem to close in. You sense you're heading in the wrong direction."
            jump forest_minigame_6

        "Follow the two-toned yip of the fox first.":
            "You follow the fox's call, but it echoes strangely, leading you in circles."
            jump forest_minigame_6

label forest_minigame_7: #animal calls puzzle 2
    "You've chosen wisely. The path opens up slightly, but the forest is still thick ahead."
    
    menu:
        "Follow the owl's hoot.":
            "You follow the hoot of the owl, and the forest feels still, almost as if it's watching you. The trees part just enough to let you through."
            jump forest_minigame_8

        "Ignore the owl, follow the fox's call next.":
            "You follow the fox's call, but the air grows thick and heavy, and the path becomes unclear."
            jump forest_minigame_6

label forest_minigame_8: #animal calls puzzle 3
    "With the owl guiding you, the forest begins to feel less oppressive."
    "Now, the two-toned yip of the fox sounds closer, clearer."

    menu:
        "Follow the fox's two-toned call.":
            "You follow the fox's call, and the forest finally opens up into a wide clearing."
            "The air is crisp, and you feel the magic of the forest all around."
            "In the center of the clearing, you see the two-tailed fox, watching you with gleaming eyes."
            jump fox_intro

label fox_intro: #introduction to the fox\
    "It rises gracefully from the stone, pacing back and forth in front of you, its gaze never leaving yours."
    fox "If you wish to proceed, and walk the forest free,"
    fox "You must answer my riddles, not one but three."

    fox "A conducting bar of length l moves to the right on two frictionless rails, as shown in the figure below. A uniform magnetic field directed into the page has a magnitude of 0.30 T. Assume l = 35 cm and R = 9.0 ohms. At what constant speed should the bar move to produce an 8.5-mA current in the resistor? What is the direction of this induced current?"
    menu:
        "0.73 meters per second counterclockwise":
            fox "Wait, how on earth did you get that right?"
            jump fox_intro_2

        "0.37 meters per second clockwise":
            fox "Ah, good try."
            jump fox_intro_2

        "Huh?":
            jump fox_intro_2

label fox_intro_2:
    fox "Haha dude, I was totally messing with you."
    fox "You should have seen the look on your face."

    "The two-tailed fox grins mischievously, its tails flicking back and forth."
    "They glow faintly as the fox studies you."

    fox "dude, is it? Been a while since I've seen a human."
    fox "Lowkey, it gets lonely as hell out here."
    fox "But you seem chill."
    fox "How about we do some riddles?"

    menu:
        "How about no?":
            fox "Oh, come on, don't be like that."
            fox "Such a killjoy."
            fox "I'm just trying to lighten the mood."
            fox "Well listen, dude, you kinda don't have a choice."
            fox "As the spirit guardian of this forest, I've got magic powers. I can't let you leave yet."
            fox "Chill with me for a bit, and I'll send you right on your way."
            jump forest_minigame_9
        "Let me at em!":
            fox "That's the spirit!"
            jump forest_minigame_9

label forest_minigame_9: #two foxes puzzle
    "The two-tailed fox flicks its tails, and suddenly there are two identical foxes standing before you."
    "One tail on each fox glows faintly, making it hard to distinguish which is real."
    fox "dude, only one of us speaks the truth. The other... well, let's just say I like to play with the truth a little."
    fox "You can ask one question to find out which path will lead you safely through the forest."

    "The two foxes grin mischievously, each waiting for your question."
    menu:
        "Ask: 'If I asked the other fox which path is safe, what would they say?'":
            "One fox tilts its head, the other grins wider."
            fox "The other would say to take the left path."
            fox "So would I."
            "You realize that both foxes would point to the wrong path in this scenario."
            jump forest_minigame_10

        "Ask: 'Which path would you take?'":
            "Both foxes smile knowingly, but their answers are cryptic. You're unsure which one to trust."
            jump forest_minigame_9

        "Ask: 'Is the left path safe?'":
            "One fox nods, while the other shakes its head. You're left uncertain."
            jump forest_minigame_9

label forest_minigame_10: #pawns
    "The eight of us go forth, not back, to protect our king from a foe's attack. What are we?"
    menu:
        "Soldiers":
            fox "Close, but nah. Soldiers can retreat too, can't they?"
            fox "Think more like… pieces on a board."
            jump forest_minigame_10

        "Chess pawns":
            fox "Boom! You got it. Pawns are always marching forward, never back."
            jump forest_minigame_11

        "Guardians":
            fox "Ooo, nice guess, but guardians aren't limited to just moving forward."
            fox "Try again, friend."
            jump forest_minigame_10

        "The king's army":
            fox "Sounds cool, but nope. Armies can retreat—pawns, though, they keep pushing forward."
            jump forest_minigame_10

label forest_minigame_11: #keyboard
    fox "I have keys but no locks. I have space but no room. You can enter, but you can't go outside. What am I?"
    menu:
        "A keyboard":
            fox "Exactly! A keyboard has keys but no locks, it has space (the space bar) but no room, and you can enter without going anywhere physically."
            jump forest_minigame_12

        "A map":
            fox "Close, but not quite. A map does have keys, but 'space with no room'? Not so much. Try again."
            jump forest_minigame_11

        "A book":
            fox "Books are a bit too literal here, don't you think? They don't exactly have 'keys' like a keyboard does."
            jump forest_minigame_11

        "A computer":
            fox "Computers have locks, and you can definitely leave your desk, dude."
            jump forest_minigame_11

label forest_minigame_12: #foxes at a table
    fox "Alright, dude, this one's a doozy."
    "The fox grins and twirls, suddenly splitting into four identical versions of itself—each a different color."
    "The foxes sit down at a round table, tails flicking in unison, waiting for your answer."
    
    fox "There are four versions of me—one red, one blue, one green, and one yellow—sitting at this round table."
    fox "Now, tell me, how many ways can you arrange us at this table?"
    "The foxes all tilt their heads expectantly, as if daring you to solve the puzzle."

    menu:
        "12 ways":
            fox "Oof, not quite! You forgot something important about round tables."
            fox "Remember, in a circle, one position is fixed!"
            jump forest_minigame_12

        "24 ways":
            fox "You're close, but that's how many ways you'd arrange us if it wasn't a round table."
            fox "In a circle, things are a bit different—one seat is fixed!"
            jump forest_minigame_12

        "6 ways":
            fox "That's the one! In a circle, we fix one fox's position, leaving three to arrange."
            fox "Nice work!"
            jump forest_minigame_success

        "4 ways":
            fox "Haha, good guess, but we can swap places a lot more than that!"
            fox "Try thinking about the fact that we're sitting at a round table—it's not the same as a straight line!"
            jump forest_minigame_12

label forest_minigame_success:
    play music "fantasy_casual.mp3" loop fadein 1.0
    
    fox "Nice, dude. I'll let you go now. You're pretty chill."
    fox "Can I get your insta?"
    menu:
        "What's an insta?":
            fox "Oh my bad, dude."

    "The fox extends a paw."
    menu:
        "Dap him up.":
            fox "Alright, dude, I'll see you around. Take care."
    
    stop music fadeout 2.0
    scene black with fade
    jump s_a1_golem

label forest_minigame_setback:
    menu:
        "Try again!":
            jump forest_minigame_start

        "Call for help":
            jump s_a1_healer
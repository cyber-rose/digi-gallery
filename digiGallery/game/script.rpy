# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")
define r = Character('Receptionist', color="#34ebcc")

#init:
#image receptionist:
#zoom 0.5

    #image hannibal:
    #   zoom 0.5
    # = "sprites/hannibal.png"
#    fit "scale-down"

# define h = Character('Hannibal', color="#7e7d85")
# define e = Character('Eyve', color="#3b22a9")
define test = "hello"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene grandentrance:
        fit "scale-up"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "Welcome to the Digital Gallery!"

    $ guide = "" #set the museum guide to no one

    scene staircase:
        fit "scale-up"

    play music "audio/gallery-01-193541.mp3"

    show receptionist

    "You head to the reception desk."

    r "Hello, welcome to the digital museum! A place to uplift community and artists through digital spaces. Please choose your tour guide!"

    #resize the sprites accordingly, receptionist is 743 pixels tall
    show hannibal at left with dissolve: 
        fit "contain"
        ysize (743) 

    define h = Character('Hannibal', color="#7e7d85")

    h "I will either find art. Or I will make some. Pledge thyself to me: Tin-can-nnibal. Together we shall conquer a vast world of knowledge and art."

    #resize the sprites accordingly, receptionist is 743 pixels tall
    show eyve at right with dissolve:
        fit "contain"
        ysize(743)

    define e = Character('Eyve', color="#1d0587")

    e "Hiyah honeyspun shortcakes! Call me Eyve. You wanna see some sweet tart art?"

    menu:

        "Tin-can-ibal":
            jump tin

        "Eyve":
            jump eyve

    #selected Hannibal as the guide
    label tin:
    
        #define h = Character('Hannibal', color="#7e7d85")
        $ guide = h

        hide eyve
        hide receptionist
        show hannibal at center with move

        guide "Impeccable judgment. Seeds of wisdom shall proudly rise as we journey into these halls."
        jump ask

    #selected Eyve as the guide
    label eyve:

        define e = Character('Eyve', color="#1d0587")
        $ guide = e

        hide hannibal
        hide receptionist

        show eyve at center with move
        guide "Hell yeah! Let's get a move on!"
        jump ask

    label ask:
        if guide == e:
            "So, anything catch your eye? Pick a genre, and I\'ll take ya there!"
        if guide == h:
            "Select thy inquiry, and I will fish its history from the depths of my knowledge."
        #guide "Where do you want to go first? Please pick a genre:"
        menu:

            "Painting":
                jump tbc

            "Plants":
                jump tbc

            "People":
                jump tbc
            
            "Misc":
                jump tbc

    label tbc:
        "to be continued..."
    # This ends the game.
    return

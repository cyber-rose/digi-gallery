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

    scene museumoutside:
        fit "fill"
        xysize (1980, 1080) 


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "Welcome to the Digital Gallery!"

    $ guide = "" #set the museum guide to no one

    scene staircase:
        fit "scale-up"

    play music "audio/gallery-01-193541.mp3"

    image receptionist desk = "images/sprites/Receptionist_desk_no_background.png"

    show receptionist desk at center with dissolve:
        fit "contain"
        ysize (1000)

    #receptionist with dissolve 
    #Receptionist_desk_no_background #"images/Receptionist_desk_no_backRground.png"

    "You head to the reception desk."

    r "Hello, welcome to the digital museum! A place to uplift community and artists through digital spaces. Please choose your tour guide!"

    #resize the sprites accordingly, receptionist is 743 pixels tall
    show tin-can-nibal at left with dissolve: 
        fit "contain"
        ysize (743) 

    define h = Character('Tin-can-nibal', color="#7e7d85")

    h "I will either find art. Or I will make some. Pledge thyself to me: Tin-can-nibal. Together we shall conquer a vast world of knowledge and art."

    #resize the sprites accordingly, receptionist is 743 pixels tall
    show eyve at right with dissolve:
        fit "contain"
        ysize(743)

    define e = Character('Eyve', color="#1d0587")

    e "Hiyah honeyspun shortcakes! Call me Eyve. You wanna see some sweet tart art?"

    menu:

        "Tin-can-nibal":
            jump tin

        "Eyve":
            jump eyve

    #selected Hannibal as the guide
    label tin:
    
        $ guide = h

        hide eyve
        hide receptionist desk
        show tin-can-nibal at center with move

        guide "Impeccable judgment. Seeds of wisdom shall proudly rise as we journey into these halls."
        jump ask

    #selected Eyve as the guide
    label eyve:

        $ guide = e

        hide tin-can-nibal
        hide receptionist desk

        show eyve at center with move
        guide "Hell yeah! Let's get a move on!"
        jump ask

    label ask:
        if guide == e:
            e "So, anything catch your eye? Pick a genre, and I\'ll take ya there!"
        if guide == h:
            h "Select thy inquiry, and I will fish its history from the depths of my knowledge."
        menu:
            "Gallery1":
                jump enter_gallery1
    
            "Gallery2":
                jump enter_gallery2

    label tbc:
        "to be continued..."
    # This ends the game.
    return

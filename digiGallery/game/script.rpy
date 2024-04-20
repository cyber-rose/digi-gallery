# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")
define r = Character('Receptionist', color="#34ebcc")

# define h = Character('Hannibal', color="#7e7d85")
# define e = Character('Eyve', color="#1d0587")
define test = "hello"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg outside

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "Welcome!"

    $ guide = ""

    scene bg lobby

    show receptionist

    "You head to the reception desk."

    r "Hello, welcome to the digital museum! Choose your tour guide!"

    show hannibal happy at left
    show eyve happy at right

    menu:

        "Tin-can-ibal":
            jump tin

        "Eyve":
            jump eyve

    label tin:
    
        define h = Character('Hannibal', color="#7e7d85")
        $ guide = h

        hide eyve happy
        hide receptionist happy
        show hannibal happy at center

        guide "Hello, my name is Tin-can-ibal and I'll be your guide today."
        jump ask

    label eyve:

        define e = Character('Eyve', color="#1d0587")
        $ guide = e

        hide hannibal happy
        hide receptionist happy

        show eyve happy at center
        guide "Hello, my name is Eyve and I'll be your guide today."
        jump ask

    label ask:
        guide "Where do you want to go first? Please pick a genre:"
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

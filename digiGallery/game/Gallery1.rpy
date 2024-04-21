define img_size = 300

define artist = "Artist Name"
define handle = "@handle"

label enter_gallery1:
    "You enter Gallery 1 and see a bunch of offshooting hallways. You browse the artist name plaque overhead each one."

    guide "Which artist do you want to check out?"

    menu:
            "Artist1":
                define artist = "Maggie Johnson"
                define handle = "@jellyfisharepeopletoo on instagram"
                jump artist1
    
            "Artist2":
                jump artist2

            "Go back to the reception area":
                jump ask

label artist1:

    call screen imenu("images/booferandwhippet.png", "images/dinno.png", "images/cupcake.png") # add many images as many as you want...
    
    jump questions

label questions:
    if guide == e:
        show eyve at left with move
    if guide == h:
        show tin-can-nibal at left with move

    if _return == 0:
        show info at right
        image a = "images/booferandwhippet.png"
        show a at center:
            yalign 0
            fit "contain"
            ysize(743)
        
    elif _return == 1: # 2nd image is picked
        $ title = "Dinno"
        show info1 at right
        image b = "images/dinno.png"
        show b at center:
            yalign 0
            fit "contain"
            ysize(743)
        

    elif _return == 2: # 3rd image is picked
        $ title = "Cupcake"
        show info2 at right
        image c = "images/cupcake.png"
        show c at center:
            yalign 0
            fit "contain"
            ysize(743)

    menu:
            "What is the title of this piece?":
                jump titleQ
    
            "What is the context of this piece?":
                jump tbc

            "Let me check out another piece.":
                hide a
                hide b
                hide c
                hide info
                hide info1
                hide info2
                if guide == e:
                    show eyve at center with move
                if guide == h:
                    show tin-can-nibal at center with move
                jump artist1

$ title = ""
label titleQ:
    if _return == 0: # represents that the first image is picked...
        $ title = "Boofer and Whippet"
    elif _return == 1: # 2nd image is picked
        $ title = "Dinno"
    elif _return == 2: # 3rd image is picked
        $ title = "Cupcake"
    guide "The title of this piece is %(title)s."
    jump questions
    
    

label artist2:
    jump tbc

screen imenu(*imgs):
    text artist size 100 xalign 0.5 yalign 0 color"#000000"
    text handle size 50 xalign 0.5 yalign 0.1 color"#000000"
    vbox xalign 0.5 yalign 0.5 spacing 300:
        hbox xalign 0.5 yalign 0.5 spacing (1920-(len(imgs))*img_size)/len(imgs):
            for i, img in enumerate(imgs):
                imagebutton:
                    idle im.Scale(img, img_size,img_size)
                    action Return(i)
        hbox xalign 0.5 yalign 0.5:
            imagebutton:
                    idle im.Scale(img, img_size,100)
                    action Jump("enter_gallery1")